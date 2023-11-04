#!/usr/bin/env python
# -*- coding: UTF-8 -*-
# Original Author : tintinweb@oststrom.com <github.com/tintinweb>
'''
A simple TCP three-way handshake example

#> python scapy_tcp_handshake.py
DEBUG:__main__:init: ('oststrom.com', 80)
DEBUG:__main__:start
DEBUG:__main__:SND: SYN
DEBUG:__main__:RCV: SYN+ACK
DEBUG:__main__:SND: SYN+ACK -> ACK
DEBUG:__main__:RCV: None
DEBUG:__main__:RCV: None
None
DEBUG:__main__:SND: FIN
DEBUG:__main__:RCV: None

Note: linux might send an RST for forged SYN packets. Disable it by executing:
#> iptables -A OUTPUT -p tcp --tcp-flags RST RST -s <src_ip> -j DROP
'''
from scapy.all import *
import logging
logger = logging.getLogger(__name__)

class TcpHandshake(object):

    def __init__(self, target):
        self.seq = 0
        self.seq_next = 0
        self.target = target
        #self.dst = iter(Net(target[0])).next()
        self.dst = next(iter(Net(target[0])))
        self.dport = target[1]
        self.sport = random.randrange(0,2**16)
        self.l4 = IP(dst=target[0])/TCP(sport=self.sport, dport=self.dport, flags=0,
                                        seq=random.randrange(0,2**32), options=[(88, "GET / HTTP")])
        self.src = self.l4.src
        self.swin = self.l4[TCP].window
        self.dwin=1
        logger.debug("init: %s"%repr(target))

    def start(self):
        logger.debug("start")
        return self.send_syn()

    def match_packet(self, pkt):
        if pkt.haslayer(IP) and pkt[IP].dst == self.l4[IP].src \
           and pkt.haslayer(TCP) and pkt[TCP].dport == self.sport \
           and pkt[TCP].ack == self.seq_next:
           return True
        return False

    def _sr1(self, pkt):
        send(pkt)
        ans = sniff(filter="tcp port %s"%self.target[1],lfilter=self.match_packet,count=1,timeout=1)
        return ans[0] if ans else None

    def handle_recv(self, pkt):
        if pkt and pkt.haslayer(IP) and pkt.haslayer(TCP):
            if pkt[TCP].flags & 0x3f == 0x12:   # SYN+ACK
                logger.debug("RCV: SYN+ACK")
                return self.send_synack_ack(pkt)
            elif  pkt[TCP].flags & 4 != 0:      # RST
                logger.debug("RCV: RST")
                raise Exception("RST")
            elif pkt[TCP].flags & 0x1 == 1:     # FIN
                logger.debug("RCV: FIN")
                return self.send_finack(pkt)
            elif pkt[TCP].flags & 0x3f == 0x10: # FIN+ACK
                logger.debug("RCV: FIN+ACK")
                return self.send_ack(pkt)

        logger.debug("RCV: %s"%repr(pkt))
        return None

    def send_syn(self):
        logger.debug("SND: SYN")
        self.l4[TCP].flags = "S"
        self.seq_next = self.l4[TCP].seq + 1
        response = self._sr1(self.l4)
        self.l4[TCP].seq += 1
        return self.handle_recv(response)

    def send_synack_ack(self, pkt):
        logger.debug("SND: SYN+ACK -> ACK")
        self.l4[TCP].ack = pkt[TCP].seq+1
        self.l4[TCP].flags = "A"
        self.seq_next = self.l4[TCP].seq
        response = self._sr1(self.l4)
        return self.handle_recv(response)

    def send_data(self, d):
        self.l4[TCP].flags = "PA"
        response = self._sr1(self.l4/d)
        self.seq_next = self.l4[TCP].seq + len(d)
        self.l4[TCP].seq += len(d)
        return self.handle_recv(response)

    def send_fin(self):
        logger.debug("SND: FIN")
        self.l4[TCP].flags = "F"
        self.seq_next = self.l4[TCP].seq + 1
        response = self._sr1(self.l4)
        self.l4[TCP].seq += 1
        return self.handle_recv(response)

    def send_finack(self, pkt):
        logger.debug("SND: FIN+ACK")
        self.l4[TCP].flags = "FA"
        self.l4[TCP].ack = pkt[TCP].seq+1
        self.seq_next = self.l4[TCP].seq + 1
        response = send(self.l4)
        self.l4[TCP].seq += 1
        raise Exception("FIN+ACK")

    def send_ack(self, pkt):
        logger.debug("SND: ACK")
        self.l4[TCP].flags = "A"
        self.l4[TCP].ack = pkt[TCP].seq+1
        self.seq_next = self.l4[TCP].seq + 1
        response = self._sr1(self.l4)
        self.l4[TCP].seq += 1

if __name__=='__main__':
    logging.basicConfig(level=logging.DEBUG)
    logger.setLevel(logging.DEBUG)
    conf.verb = 0
    tcp_hs = TcpHandshake(("192.168.23.1", 18080))
    #tcp_hs = TcpHandshake(("202.38.93.111",18082))
    tcp_hs.start()
    data = "POST / HTTP/1.1\r\n"
    data += "HOST: foobar\r\n"
    data += "Content-Length: 101\r\n\r\n"
    data += '<FLAG_HERE>'
    print(repr(tcp_hs.send_data(data)))
    tcp_hs.send_fin()
