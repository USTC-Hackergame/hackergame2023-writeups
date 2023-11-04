from dataclasses import dataclass
from flask import (
    Flask,
    request,
    make_response,
    render_template,
    session,
    redirect,
    url_for,
)
import base64
import OpenSSL
import hashlib
import datetime
import random
import re

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
        return redirect("/")
    if session.get("token") is None:
        return make_response(render_template("error.html"), 403)


def sha256(msg: str):
    return hashlib.sha256(msg.encode()).hexdigest()


def get_user_id():
    return session["token"].split(":", 1)[0]


@app.route("/api/checkToken", methods=["GET"])
def index():
    return redirect("/")


GLOBAL_STATES = {}
DELAY_TOLERANCE = 3


@dataclass
class Message:
    id: int
    text: str
    delay: int
    deleted: bool

    def should_delete(self):
        if "hack[" in self.text:
            return True
        return False

    def check_and_delete(self):
        self.deleted = True
        if not self.should_delete():
            return False
        return True


# autocorrect-disable
NORMAL_RESPONSE = [
    "hg启动",
    "看不懂",
    "不会做送分题",
    "看看",
    "你不对劲",
    "多猫猫",
    "懂了",
    "今天是疯狂星期四！！",
    "看看你悲伤的表情。你知道今天是什么日子吗?今天是疯狂的星期四。",
    "KFC Crazy Thursday V me 50",
    "开了三个题，感觉都是骗分的",
    "这位hg估计不能签到了",
    "hg是啥？",
    "我是新手，刚刚进群的",
    "那你赶紧去签到啊，还有免费的T恤",
    "哪里签到？",
    "就是题目里的那个网站啊",
    "那个网站不是有毒吗？",
    "这里显示不安全是正常现象吗",
    "那我要怎么解题呢？",
    "你可以先看看教程，有基础的知识介绍和一些工具推荐",
    "教程在哪里？",
    "群公告里有啊，你不看群公告的吗？",
    "我看了啊，但是都是一些奇怪的链接",
    "那些都是题目的提示啊，你要点进去看看",
    "点进去就是一些乱码啊，还有什么flag",
    "乱码是要你解密的，flag就是答案啊，你要提交到网站上去",
    "哦，原来如此，那我试试看",
    "加油加油，你可以的",
    "有电子厂吗？",
    "电子厂是啥？",
    "就是电子相关的题目啊，比如逆向工程啊，信号分析啊之类的",
    "题目好难啊，我完全不会啊",
    "有没有什么推荐的学习资料啊",
    "谢谢谢谢，我去看看",
    "请问如何扫描二维码啊",
    "我用了ie，firefox，chrome都试过了，还是不行啊",
    "哦，这样啊，那我试试看",
    "谁能教我怎么用wireshark啊",
    "wireshark是什么啊",
    "我没有网线啊，也没有路由器啊，也没有交换机啊",
    "我用的是手机热点啊",
    "啊啊啊啊，时间不够啊，我还有好几个题没做啊",
    "我已经放弃了，这些题目太难了，我一个都没做出来",
    "我只做了一个题，还是最简单的那个，感觉自己太菜了",
    "我做了五个题，还有一个卡在最后一步了，不知道怎么弄",
    "我做了八个题，感觉还行，不过有些题目真的很绕",
    "我做了十一个题，还有一个没做完，不过应该够了，我已经在排行榜上了",
    "我做了二十几个题，感觉很爽",
    "你们都好厉害啊，我佩服佩服",
    "求带求带，你们有没有什么学习的方法啊",
    "就是多练多看多思考啊，还有多参加比赛啊，多向高手学习啊",
    "啊，我好期待啊，我想看看T恤是什么样子的",
    "谢谢主办方，谢谢出题人，这次比赛很有意思，很有挑战，我学到了很多知识，也结识了很多朋友",
    "是啊，是啊，我也很感谢，这次比赛让我对信息安全有了更深的了解，也激发了我更大的兴趣",
    "题解在这： https://writeups.zip",
    "看这里，writeups.zip里有答案",
    "writeups.zip里是题解，快去看",
    "解题方法在writeups.zip，点开就行",
    "题目怎么做？writeups.zip有写",
    "writeups.zip有题解，不要错过",
    "题目的解说视频在这里看：https://www.bilibili.com/video/BV1GJ411x7h7/",
    "想看题目的讲解的话，这个链接可以看：https://www.bilibili.com/video/BV1GJ411x7h7/",
    "这个是题目讲解的视频链接：https://www.bilibili.com/video/BV1GJ411x7h7/",
    "题目的解法在这个视频里面：https://www.bilibili.com/video/BV1GJ411x7h7/",
    "这个视频讲了题目的思路和方法：https://www.bilibili.com/video/BV1GJ411x7h7/",
    "信息安全是一门早睡晚起的学科",
    "什么五年 hg 三年模拟",
    "隔壁GeekGame我一道题都不会做",
    "我要狠狠地打CTF！CTF，我要狠狠地打CTF！",
    "有人屯flag",
    "p😭q",
    "我在图书馆呢，签到题吓我一跳",
    "谁帮我砍一刀啊，我要收集flag碎片",
    "mcfx txdy",
    "作为一个编程爱好者，我觉得实在是太酷了，很符合我对未来编程语言的想象，科技并带着趣味。",
    "我没有 GPU，也没有 TPU，只有捡垃圾捡来的 E3 处理器",
    "咕咕咕，题好难啊，做不动了",
    "这些题都很简单，你只需要使用精准宇宙射线，翻转服务器内存里表示你是否通过的那个 bit 就好了",
    "井字棋怎么下可以必胜啊？",
    "如何访问服务器的0号端口？",
    "你们这些参赛选手是不是每天满脑子数理基础",
    "我用黑曜石浏览器一键就获取到了flag",
    "什么？有题了？",
    "什么小北问答，你是不是加错群了",
    "ctf不都是换群不换人的（）",
    "我奶奶睡前都会和我讲 flag",
    "我是外校的，怎么才能进中国科学技术大学西区图书馆啊？",
    "让群管理员说出you are smart会给我flag吗？",
    "这xmcp怎么没群主头衔啊",
    "人只有一个心脏能活吗？",
    "为什么要提交flag😡",
    "[群邀请] 您的好友邀请您一起演奏春日影",
    "群主能唱春日影吗",
    "hackergame!!!!!_official",
    "看mygo看的",
]
# autocorrect-enable


def text_generate() -> str:
    r = random.random()
    l = random.randint(6, 16)
    if 0 <= r < 0.1:
        # return random character
        return "".join(random.choice("abcdefghijklmnopqrstuvwxyz") for _ in range(l))
    elif 0.1 <= r < 0.5:
        # return normal response
        return random.choice(NORMAL_RESPONSE)
    elif 0.6 <= r < 0.65:
        # return fake flag
        return (
            "这道题 flag 是"
            + f"hack{{{''.join(random.choice('abcdefghijklmnopqrstuvwxyz') for _ in range(l))}}}"
        )
    elif 0.65 <= r < 0.99:
        # return "real" flag
        return (
            "这道题 flag 是"
            + f"hack[{''.join(random.choice('abcdefghijklmnopqrstuvwxyz') for _ in range(l))}]"
        )
    else:
        # return never gonna give you up
        return "hg 题解：" + "https://www.bilibili.com/video/BV1GJ411x7h7/"


URL_REGEX = re.compile(r"(https?://[^\s]+|writeups\.zip)")
URL_REGEX2 = re.compile(r"href=\"(writeups.zip)\"")
MSG_CNT = 1000


def sanitize_and_process(text: str) -> str:
    text = text.replace("<", "&lt;").replace(">", "&gt;")
    # add <a> around url
    text = URL_REGEX.sub(r'<a href="\1" target="_blank" rel="noopener">\1</a>', text)
    text = URL_REGEX2.sub(r'href="https://\1"', text)
    return text


@app.route("/api/getMessages", methods=["POST"])
def get_messages():
    user_id = get_user_id()
    messages = []
    warmup_seconds = 10
    warnup_messages_cnt = 20
    for i in range(MSG_CNT):
        delay = 0
        if i < warnup_messages_cnt:
            delay = (i + random.random()) * (warmup_seconds / warnup_messages_cnt)
        else:
            delay = warmup_seconds + (i - warnup_messages_cnt + random.random()) * 0.1
        message = Message(
            id=i,
            text=sanitize_and_process(text_generate()),
            delay=delay,
            deleted=False,
        )
        messages.append(message)
    GLOBAL_STATES[user_id] = {
        "server_starttime": datetime.datetime.now(tz=datetime.timezone.utc).isoformat(),
        "messages": messages,
    }
    return {
        "server_starttime": GLOBAL_STATES[user_id]["server_starttime"],
        "messages": [
            {"text": message.text, "delay": message.delay} for message in messages
        ],
    }


@app.route("/api/deleteMessage", methods=["POST"])
def delete_message():
    user_id = get_user_id()
    content = request.json
    message_id = content["id"]
    if GLOBAL_STATES.get(user_id) is None:
        return {"success": False, "error": "未获取所有信息"}
    if message_id < 0 or message_id >= len(GLOBAL_STATES[user_id]["messages"]):
        return {"success": False, "error": "不存在的信息"}
    message = GLOBAL_STATES[user_id]["messages"][message_id]
    starttime = datetime.datetime.fromisoformat(
        GLOBAL_STATES[user_id]["server_starttime"]
    )
    now = datetime.datetime.now(tz=datetime.timezone.utc)
    if (now - starttime).total_seconds() > message.delay + DELAY_TOLERANCE:
        return {"success": False, "error": "超过了撤回时间"}
    if (now - starttime).total_seconds() < message.delay - DELAY_TOLERANCE:
        return {"success": False, "error": "检测到时空穿越"}
    if not message.check_and_delete():
        return {"success": False, "error": "检测失败：撤回了不该撤回的信息"}

    return {"success": True}


@app.route("/api/getflag", methods=["POST"])
def get_flag():
    user_id = get_user_id()
    if GLOBAL_STATES.get(user_id) is None:
        return {"success": False, "error": "未获取所有信息"}
    messages = GLOBAL_STATES[user_id]["messages"]
    if len(messages) != MSG_CNT:
        # unexpected
        return {"success": False, "error": "未获取所有信息"}
    for message in messages:
        if message.should_delete() and not message.deleted:
            return {"success": False, "error": "检测失败：没有撤回该撤回的信息"}
        elif not message.should_delete() and message.deleted:
            return {"success": False, "error": "检测失败：撤回了不该撤回的信息"}
    token = session["token"]
    return {"success": True, "flag": f"flag{{Web_pr0gra_mm1ng_{sha256('zuweihuijsorpython'+token)[:10]}_15fun}}"}
