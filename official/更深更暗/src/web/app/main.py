from flask import Flask, request, make_response, send_file, render_template, session, redirect, url_for
import base64
import OpenSSL

app = Flask(__name__)

app.config["MAX_CONTENT_LENGTH"] = 1 * 1024 * 1024

with open("./cert.pem") as f:
    cert = OpenSSL.crypto.load_certificate(OpenSSL.crypto.FILETYPE_PEM, f.read())


@app.route("/", methods=["GET", "POST"])
def index():
    if request.method == "POST":
        try:
            req = request.get_json()
            token = req["token"]
            id, sig = token.split(":", 1)
            sig = base64.b64decode(sig, validate=True)
            OpenSSL.crypto.verify(cert, sig, id.encode(), "sha256")
        except Exception as e:
            print(repr(e))
            return "", 403
        return "", 200
    else:
        return send_file("static/index.html")
