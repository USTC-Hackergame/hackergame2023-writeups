import hashlib

sha256 = lambda x: hashlib.sha256(x.encode()).hexdigest()

def getflag1(token):
    return f"flag{{flatpak_install_curtail_15_linux_{sha256('example' + token)[:10]}}}"

def getflag2(token):
    return f"flag{{it's a mistake_{sha256('jpegxl' + token)[:10]}_that chr0mium thr0ws away JPEGXL}}"
