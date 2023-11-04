#include <arpa/inet.h>
#include <netinet/ip.h>
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

    char opt[12] = "\x00\x0CGET / HTTP";
    char opt2[14] = "\x00\x0E..GET / HTTP";
    int fd;
    if ((fd = socket(AF_INET, SOCK_STREAM, IPPROTO_TCP)) < 0) {
        perror("socket");
        return 1;
    }
    int i;
    for (i = 1; i <= 255; i++) {\
        opt[0] = opt2[0] = i;
        if (setsockopt(fd, SOL_IP, IP_OPTIONS, opt, sizeof(opt)) == 0) {
            printf("Option %d/0x%02X can setsockopt\n", i, i);
            if (connect(fd, (struct sockaddr*)&addr, sizeof(addr)) == 0) {
                printf("Option %d/0x%02X can connect\n", i, i);
                break;
            }
        }
        if (setsockopt(fd, SOL_IP, IP_OPTIONS, opt2, sizeof(opt2)) == 0) {
            printf("Alternative option %d/0x%02X can setsockopt\n", i, i);
            if (connect(fd, (struct sockaddr*)&addr, sizeof(addr)) == 0) {
                printf("Alternative option %d/0x%02X can connect\n", i, i);
                break;
            }
        }
    }
    if (i > 255) {
        fprintf(stderr, "No option supported\n");
        goto cleanup;
    }

    const char token[] = "114514:qqxx";
    const int token_len = strlen(token);
    char buf[1024];
    int buflen = sprintf(buf, "POST / HTTP/1.1\r\nHost: example.com\r\nContent-Length: %d\r\n\r\n%s", token_len, token);
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
