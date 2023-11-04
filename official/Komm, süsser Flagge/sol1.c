#include <arpa/inet.h>
#include <netinet/ip.h>
#include <netinet/tcp.h>
#include <stdio.h>
#include <stdlib.h>
#include <string.h>
#include <sys/socket.h>
#include <unistd.h>

int main(int argc, char** argv) {
    if (argc != 3) {
        printf("Usage: %s <ip> <port>\n", argv[0]);
        return 0;
    }
    struct sockaddr_in addr;
    memset(&addr, 0, sizeof(addr));
    addr.sin_family = AF_INET;
    addr.sin_addr.s_addr = inet_addr(argv[1]);
    addr.sin_port = htons(atoi(argv[2]));

    int fd;
    if ((fd = socket(AF_INET, SOCK_STREAM, IPPROTO_TCP)) < 0) {
        perror("socket");
        return 1;
    }
    if (connect(fd, (struct sockaddr*)&addr, sizeof(addr)) < 0) {
        perror("connect");
        goto cleanup;
    }

    char buf[1024];
    strcpy(buf, "P");
    int buflen = 1;
    if (write(fd, buf, buflen) != buflen) {
        perror("write");
        goto cleanup;
    }
    int yes = 1;
    if (setsockopt(fd, IPPROTO_TCP, TCP_NODELAY, &yes, sizeof(yes)) < 0) {
        perror("setsockopt");
        goto cleanup;
    }

    const char token[] = "114514:qqxx";
    const int token_len = strlen(token);
    buflen = sprintf(buf, "OST / HTTP/1.1\r\nHost: example.com\r\nContent-Length: %d\r\n\r\n%s", token_len, token);
    if (write(fd, buf, buflen) != buflen) {
        perror("write");
        goto cleanup;
    }
    if (shutdown(fd, SHUT_WR) != 0) {
        perror("shutdown");
        goto cleanup;
    }

    while ((buflen = read(fd, buf, sizeof(buf))) > 0) {
        if (write(STDOUT_FILENO, buf, buflen) != buflen) {
            perror("write");
            goto cleanup;
        }
    }
    if (buflen < 0) {
        perror("read");
        goto cleanup;
    }

cleanup:
    if (close(fd) != 0) {
        perror("close");
        return 1;
    }
}
