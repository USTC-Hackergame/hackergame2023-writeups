from flask import (
    Flask,
    request,
    make_response,
    render_template,
    session,
    redirect,
    url_for,
)
import socket
import os
import base64
import OpenSSL
import hashlib
from collections import defaultdict
from flag import flag1, flag2, flag3

from secret import secret_key

app = Flask(__name__)
app.secret_key = secret_key

app.config["MAX_CONTENT_LENGTH"] = 10 * 1024 * 1024

with open("./cert.pem") as f:
    cert = OpenSSL.crypto.load_certificate(OpenSSL.crypto.FILETYPE_PEM, f.read())


@app.before_request
def check():
    if request.path.startswith("/static/"):
        return
    if request.args.get("token"):
        try:
            token = request.args.get("token")
            id, sig = token.split(":", 1)
            sig = base64.b64decode(sig, validate=True)
            OpenSSL.crypto.verify(cert, sig, id.encode(), "sha256")
            session["token"] = token
        except Exception:
            session["token"] = None
        return redirect(url_for("index"))
    if session.get("token") is None:
        return make_response(render_template("error.html"), 403)


def sha256(msg: bytes):
    return hashlib.sha256(msg).hexdigest()


def get_user_id():
    return session["token"].split(":", 1)[0]


global_collections = defaultdict(set)
global_flag2 = defaultdict(bool)

EXAMPLE_REQUEST = b"GET / HTTP/1.1\\r\\n\nHost: example.com\\r\\n\\r\\n"


def check_flags() -> list[str]:
    cnt = len(global_collections[get_user_id()])
    token = session["token"]
    flags = []
    if cnt >= 5:
        flags.append(flag1(token))
    if global_flag2[get_user_id()] is True:
        flags.append(flag2(token))
    if cnt >= 12:
        flags.append(flag3(token))
    return flags


@app.route("/", methods=["GET", "POST"])
def index():
    if request.method == "POST":
        user_id = get_user_id()
        user_request = request.form.get("request")

        original_request = user_request

        # parse user request
        # 1. remove all \n and \r
        user_request = user_request.replace("\n", "").replace("\r", "")
        # 2. escape existing characters in user's request
        user_request = user_request.encode("utf-8").decode("unicode_escape")

        print(f"{user_id}: {repr(user_request)}")

        buf = b""
        is_timeout = False
        is_reset = False
        try:
            s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
            s.settimeout(0.5)
            s.connect(("http_backend1", 80))

            s.sendall(user_request.encode())
            s.shutdown(socket.SHUT_WR)
            while True:
                data = s.recv(8192)
                if not data:
                    break
                buf += data
                if len(buf) > 8192:
                    break
        except TimeoutError:
            is_timeout = True
        except ConnectionResetError:
            is_reset = True
        # parse status line
        # https://www.w3.org/Protocols/rfc2616/rfc2616-sec6.html
        # Status-Line = HTTP-Version SP Status-Code SP Reason-Phrase CRLF
        # 1. find first CRLF
        crlf = buf.find(b"\r\n")
        if buf.strip() != b"":
            try:
                if crlf == -1:
                    raise ValueError("No CRLF found")
                status_line = buf[:crlf]
                http_version, status_code, reason_phrase = status_line.split(b" ", 2)
                status_code = int(status_code)
            except ValueError:
                buf += "（无状态码）".encode()
                status_code = None
            if status_code is not None:
                global_collections[user_id].add(status_code)
            else:
                global_flag2[user_id] = True
        if is_timeout:
            buf += "（连接超时，已断开）".encode()
        if is_reset:
            buf += "（连接被重置，已断开）".encode()
        flags = check_flags()
        return render_template(
            "index.html",
            result=buf.decode(),
            code_set=sorted(global_collections[user_id]),
            user_request=original_request,
            flags=flags,
        )
    else:
        flags = check_flags()
        return render_template(
            "index.html",
            code_set=sorted(global_collections[get_user_id()]),
            user_request=EXAMPLE_REQUEST.decode(),
            flags=flags,
        )
