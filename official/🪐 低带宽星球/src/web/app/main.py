from flask import (
    Flask,
    request,
    make_response,
    render_template,
    session,
    redirect,
    url_for,
    send_file,
)
import socket
import os
import base64
import OpenSSL
import hashlib
import subprocess
from collections import defaultdict
from gevent.lock import BoundedSemaphore

from secret import secret_key
from jxltree import generate_res
from flag import getflag1, getflag2

app = Flask(__name__)
app.secret_key = secret_key

app.config["MAX_CONTENT_LENGTH"] = 1 * 1024 * 1024

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


locks = defaultdict(lambda: BoundedSemaphore(1))


@app.route("/", methods=["GET", "POST"])
def index():
    if request.method == "POST":
        token_id = get_user_id()
        if not os.path.exists(f"/dev/shm/{token_id}.png"):
            return render_template("index.html", result="请先下载生成的图片。")
        else:
            b1 = open(f"/dev/shm/{token_id}.png", "rb").read()
            b1_len = len(b1)
        token = session["token"]
        if request.files["file"].filename == "":
            return render_template("index.html", result="你似乎没有选择需要上传的文件。")
        file = request.files["file"].read()
        file_len = len(file)
        if file_len >= b1_len:
            return render_template("index.html", result="你上传的文件不小于原始文件。")
        if type(file) is str:
            # not sure how "file" is opened so just be careful
            file = file.encode()
        print(f"get upload from {get_user_id()}, {sha256(file)}")
        s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        s.connect((os.environ[f"nc_host"], int(os.environ["nc_port"])))

        buf = b""
        while True:
            buf += s.recv(4096)
            if buf == b"Please input your token: \n":
                break
        s.sendall(token.encode() + b"\n")

        buf = b""
        while True:
            buf += s.recv(4096)
            if not b"Base64 of binary:".startswith(buf):
                break

        if buf == b"Base64 of binary: ":
            s.sendall(base64.b64encode(b1) + b'!' + base64.b64encode(file) + b"\n")
            buf = b""
            while True:
                data = s.recv(4096)
                if not data:
                    break
                buf += data
        buf = buf.decode().strip()
        result = ""
        if buf == "OK":
            if file_len <= 2048:
                result += f"不大于 2048 字节，flag1: {getflag1(token)}\n"
            if file_len <= 50:
                result += f"不大于 50 字节，flag2: {getflag2(token)}\n"
            if result == "":
                result = "文件像素级一致，但是太大了，没有 flag"
        elif "Player connection rate limit exceeded" in buf:
            result = "连接过于频繁，超出服务器限制，请等待 10 秒后重试。"
        else:
            result = "文件没有像素级一致，不能给你 flag"
        return render_template("index.html", result=result)
    else:
        return render_template("index.html", result="")


@app.route("/image.png", methods=["GET"])
def generate():
    token_id = get_user_id()
    # check if it is in /dev/shm/{token_id}.png
    lock = locks[token_id]
    with lock:
        if not os.path.exists(f"/dev/shm/{token_id}.png"):
            # generate the file
            cost = 0
            while True:
                tree = generate_res(token_id, cost)
                r1 = subprocess.run(
                    ["jxl_from_tree", "/dev/stdin", "/dev/stdout"],
                    input=tree.encode(),
                    stdout=subprocess.PIPE,
                    stderr=subprocess.PIPE,
                )
                if r1.returncode != 0:
                    print(r1.stderr.decode())
                    return make_response("Failed to generate. Please contact admin.", 500)
                jxl_bytes = r1.stdout
                if len(jxl_bytes) > 50:
                    print("size > 50, retry")
                    cost += 1
                else:
                    break
            # write jxl to file, as djxl fails to read from stdin
            with open(f"/dev/shm/{token_id}.jxl", "wb") as f:
                f.write(jxl_bytes)
            r2 = subprocess.run(
                ["djxl", f"/dev/shm/{token_id}.jxl", f"/dev/shm/{token_id}.png"],
                input=jxl_bytes,
                stderr=subprocess.PIPE,
            )
            os.remove(f"/dev/shm/{token_id}.jxl")
            if r2.returncode != 0:
                print(r2.stderr.decode())
                return make_response("Failed to generate. Please contact admin.", 500)
        # provide the file
        return send_file(f"/dev/shm/{token_id}.png", as_attachment=True, download_name="image.png")
