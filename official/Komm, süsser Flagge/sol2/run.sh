#!/bin/sh

IMAGE=test-solution
NAME=test-solution

: ${SERVER_ADDR:=127.0.0.1} ${SERVER_PORT:=18081}

cd "$(dirname "$0")"
docker build -t "$IMAGE" .
docker run --name="$NAME" --rm -it \
  --cap-add=CAP_NET_ADMIN \
  -e SERVER_ADDR="$SERVER_ADDR" \
  -e SERVER_PORT="$SERVER_PORT" \
  "$IMAGE"
