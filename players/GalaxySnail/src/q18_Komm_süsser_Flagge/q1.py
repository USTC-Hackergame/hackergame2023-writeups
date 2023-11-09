import sys
import io
import time
import socket

def main():
    addr = sys.argv[1]
    port = int(sys.argv[2])
    token = input("token: ").encode("ascii")
    data = (
        "POST / HTTP/1.1\r\n"
       f"Host: {addr}:{port}\r\n"
        "User-Agent: curl/8.4.0\r\n"
        "Accept: */*\r\n"
       f"Content-Length: {len(token)}\r\n"
        "Content-Type: application/x-www-form-urlencoded\r\n"
        "\r\n"
    ).encode("ascii") + token
    bio = io.BytesIO(data)

    sock = socket.create_connection((addr, port))
    sock.sendall(bio.read(2))
    time.sleep(1)
    sock.sendall(bio.read())

    while True:
        recv_data = sock.recv(4096)
        if not recv_data:
            break
        sys.stdout.buffer.write(recv_data)

main()
