# Copyright 2022-2023 USTC-Hackergame
# Copyright 2021 PKU-GeekGame
#
# Redistribution and use in source and binary forms, with or without modification, are permitted provided that the following conditions are met:
#
# 1. Redistributions of source code must retain the above copyright notice, this list of conditions and the following disclaimer.
#
# 2. Redistributions in binary form must reproduce the above copyright notice, this list of conditions and the following disclaimer in the documentation and/or other materials provided with the distribution.
#
# 3. Neither the name of the copyright holder nor the names of its contributors may be used to endorse or promote products derived from this software without specific prior written permission.
#
# THIS SOFTWARE IS PROVIDED BY THE COPYRIGHT HOLDERS AND CONTRIBUTORS "AS IS" AND ANY EXPRESS OR IMPLIED WARRANTIES, INCLUDING, BUT NOT LIMITED TO, THE IMPLIED WARRANTIES OF MERCHANTABILITY AND FITNESS FOR A PARTICULAR PURPOSE ARE DISCLAIMED. IN NO EVENT SHALL THE COPYRIGHT HOLDER OR CONTRIBUTORS BE LIABLE FOR ANY DIRECT, INDIRECT, INCIDENTAL, SPECIAL, EXEMPLARY, OR CONSEQUENTIAL DAMAGES (INCLUDING, BUT NOT LIMITED TO, PROCUREMENT OF SUBSTITUTE GOODS OR SERVICES; LOSS OF USE, DATA, OR PROFITS; OR BUSINESS INTERRUPTION) HOWEVER CAUSED AND ON ANY THEORY OF LIABILITY, WHETHER IN CONTRACT, STRICT LIABILITY, OR TORT (INCLUDING NEGLIGENCE OR OTHERWISE) ARISING IN ANY WAY OUT OF THE USE OF THIS SOFTWARE, EVEN IF ADVISED OF THE POSSIBILITY OF SUCH DAMAGE.

from selenium import webdriver
import selenium
import time
import os
import subprocess
import urllib.parse

# secret.py 不提供
from secret import FLAG, BOT_SECRET

os.mkdir("/dev/shm/xss-data")
os.mkdir("/dev/shm/chromium-data")
FLAG = urllib.parse.quote_plus(FLAG)
# 环境变量 "hackergame_token" 是你的 token
id = int(os.environ["hackergame_token"].split(":")[0])

# Stage 1
print("请输入你的 HTML 文件，以仅包含 EOF 三个字母的行结束，该文件需要小于 5KiB。")
print("我会在本地启动一个静态的 HTTP 服务器提供这个文件。")

code = ""
while True:
    line = input()
    if line == "EOF":
        break
    code += line + "\n"
    if len(code) > 1024 * 5:
        print("你的 HTML 太大了，尝试短一些吧！")
        exit(1)

with open("/dev/shm/xss-data/index.html", "w") as f:
    f.write(code)
sp = subprocess.Popen(
    ["python3", "-m", "http.server", "-b", "127.0.0.1", "10240"], cwd="/dev/shm/xss-data",
    stdout=subprocess.DEVNULL, stderr=subprocess.DEVNULL
)
time.sleep(1)
if sp.poll() is not None:
    print("启动 HTTP 服务器失败，请联系管理员。")
    exit(1)

# BOT 用 "BOT_SECRET" 以「管理员权限」登录，然后降权到和你一样
LOGIN_URL = f"http://web/?bot={BOT_SECRET}&id={id}"
# 在题目服务器上，bot 会访问 http://web
# 本地调试时，需要做如下修改：
# LOGIN_URL = "http://题目地址/?token=your_token"


# Stage 2
try:
    options = webdriver.ChromeOptions()
    options.add_argument("--no-sandbox")  # sandbox not working in docker
    options.add_argument("--headless")
    options.add_argument("--disable-gpu")
    options.add_argument("--user-data-dir=/dev/shm/user-data")
    os.environ["TMPDIR"] = "/dev/shm/chromium-data/"
    options.add_experimental_option("excludeSwitches", ["enable-logging"])

    with webdriver.Chrome(options=options) as driver:
        ua = driver.execute_script("return navigator.userAgent")
        print(" I am using", ua)

        print("- Logining...")
        driver.get(LOGIN_URL)
        time.sleep(4)

        print(" Putting secret flag...")
        driver.execute_script(f'document.cookie="flag={FLAG}"')
        time.sleep(1)

        print("- Now browsing your website...")
        driver.get("http://localhost:10240")
        time.sleep(4)

        print("Bye bye!")
except Exception as e:
    print("ERROR", type(e))
    print("I'll not give you exception message this time.")
