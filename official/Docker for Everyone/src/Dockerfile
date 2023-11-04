FROM ustclug/debian:bookworm

RUN apt update && apt -y upgrade && \
    apt install --no-install-recommends -y qemu-system wget p7zip-full ca-certificates

ADD src /src
WORKDIR /src

RUN wget https://ftp.lug.ustc.edu.cn/~taoky/2023-004.7z && \
    7z x -p5sIwZaW6q0XFHuHyyG0Ocw 2023-004.7z && \
    echo "8cfd1662fb9408337cd902ec7044d0007422aed9fdceedb46ead74695b873e41 alpine.qcow2" | sha256sum -c && \
    rm 2023-004.7z

CMD ["/src/run.sh"]
