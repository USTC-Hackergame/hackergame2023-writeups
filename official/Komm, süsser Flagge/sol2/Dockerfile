FROM alpine:latest
RUN apk add --no-cache nftables curl
ADD init.sh /
CMD ["/init.sh"]
