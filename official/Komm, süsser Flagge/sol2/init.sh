#!/bin/sh

nft -f - << EOF
flush ruleset
table ip filter {
  chain OUTPUT {
    type filter hook output priority mangle; policy accept;
    ip daddr $SERVER_ADDR tcp dport $SERVER_PORT @th,100,1 set 1
  }
}
EOF
exec curl -X POST -d "114514:qqxx" -vs "http://$SERVER_ADDR:$SERVER_PORT/"
