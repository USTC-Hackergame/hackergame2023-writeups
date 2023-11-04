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
import base64
import OpenSSL
from collections import defaultdict

from secret import secret_key, BOT_SECRET

app = Flask(__name__)
app.secret_key = secret_key

app.config["MAX_CONTENT_LENGTH"] = 2 * 1024 * 1024

with open("./cert.pem") as f:
    cert = OpenSSL.crypto.load_certificate(OpenSSL.crypto.FILETYPE_PEM, f.read())


@app.before_request
def check():
    if request.path.startswith("/static/"):
        return
    if request.args.get("bot") == BOT_SECRET:
        # Check to not allow reading others' comments
        if not session.get("token", "").endswith(":bot"):
            user_id = request.args.get("id")
            session["token"] = user_id + ":bot"  # "1:bot"
            return redirect(url_for("bot"))
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


# user_id, is_bot
def get_user_id() -> tuple[int, bool]:
    user_id = session["token"].split(":", 1)[0]
    if session["token"].endswith(":bot"):
        return user_id, True
    return user_id, False


MEMORY = defaultdict(lambda: {"score": None, "comments": ""})


@app.route("/", methods=["GET", "POST"])
def index():
    if request.method == "POST":
        q1, q2, q3, q4, q5 = (
            request.form["q1"],
            request.form["q2"],
            request.form["q3"],
            request.form["q4"],
            request.form["q5"],
        )
        q1 = q1.strip()
        q2 = q2.strip()
        q3 = q3.strip()
        q4 = q4.strip()
        q5 = q5.strip()
        # expected ans:
        # q1 => 0.6673001696
        # q2 => 0.0766761537
        # q3 => 1.0362686330
        # q4 => 31.7000000000
        # q5 => 1244.4054463185
        score = 0
        if q1 == "0.6673001696":
            score += 20
        if q2 == "0.0766761537":
            score += 20
        if q3 == "1.0362686330":
            score += 20
        if q4 == "31.7000000000":
            score += 20
        if q5 == "1244.4054463185":
            score += 20
        user_id, is_bot = get_user_id()
        # if is_bot:
        #     return "You are a bot."
        MEMORY[user_id]["score"] = score
        return redirect(url_for("result"))
    else:
        return send_file("static/index.html")


BLOCKLIST = ["&", ">", "<", "'", "(", ")", "`", ".", ",", "%"]


def construct_filler_js(selector, template, input, safe=True):
    input = str(input)
    if safe:
        for i in BLOCKLIST:
            if i in input:
                return f'alert("发现危险输入！"); updateElement("{selector}", "发现危险输入！");'
    html = template.format(el=input)
    return f'updateElement("{selector}", "{html}");'


@app.route("/result", methods=["GET", "POST"])
def result():
    user_id, is_bot = get_user_id()
    if MEMORY[user_id]["score"] is None:
        return redirect(url_for("index"))

    if request.method == "POST":
        comment = request.form["comment"]
        if len(comment) > 25:
            return "你的评论太长了！"
        MEMORY[user_id]["comments"] = comment

    comment = MEMORY[user_id]["comments"]
    if comment == "":
        comment = "（还没有评论）"
    js = (
        construct_filler_js("#score", "你的得分是 <b>{el}</b> 分", MEMORY[user_id]["score"])
        + "\n"
        + construct_filler_js("#comment", "你留下的评论：{el}", comment)
    )

    return render_template("result.html", js=js)


@app.route("/bot", methods=["GET"])
def bot():
    # bot landing page
    if not get_user_id()[1]:
        return "You are not a bot."
    return "OK"


if __name__ == "__main__":
    # this will not be executed in uwsgi
    app.run(host="127.0.0.1", port=19198, debug=True)
