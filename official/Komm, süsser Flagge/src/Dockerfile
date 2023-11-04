FROM golang:1-alpine AS builder
WORKDIR /src/
COPY *.go /src/
RUN go build -o main -ldflags='-s -w' *.go

FROM alpine:latest
RUN apk add --no-cache iptables
COPY init.sh /
COPY --from=builder /src/main /
CMD ["/init.sh"]
