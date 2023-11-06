import time

# import IPython
from scapy.all import *
import scapy.layers.inet
import scapy.sendrecv

# ip = '127.0.0.1'
# ip = '172.20.224.1'
# ip = '202.38.93.111'
ip = '192.168.23.1'
# port = 8000
port = 18081
sport = 9030
iface = 'hgovpn-guest'

with open('s.txt', 'rb') as f:
    payload = f.read()
# payload = payload + b'\r\n' * 2

#产生SYN包（FLAG = S 为SYN）
ret = scapy.sendrecv.srp(
    scapy.layers.inet.IP(dst=ip)
        / scapy.layers.inet.TCP(dport=port,sport=sport,flags='S',seq=17),
    verbose = False,
    iface=iface,
    timeout=1,
)
#响应的数据包产生数组([0]为响应，[1]为未响应)
list = ret[0].res
#第一层[0]位第一组数据包
#第二层[0]表示发送的包，[1]表示收到的包
#第三层[0]为IP信息，[1]为TCP信息，[2]为TCP数据
tcpfields_synack = list[0][1][1].fields

sc_sn = tcpfields_synack['seq'] + 1
cs_sn = tcpfields_synack['ack']
print(sc_sn)
print(cs_sn)

#发送ACK(flag = A),完成三次握手！
scapy.sendrecv.srp(
    scapy.layers.inet.IP(dst=ip)
        / scapy.layers.inet.TCP(dport=port,sport=sport,flags='A',seq=cs_sn,ack=sc_sn),
    verbose = False,
    iface=iface,
    timeout=0.01,
)

def reset() -> None:
    scapy.sendrecv.send(
        scapy.layers.inet.IP(dst=ip)
            / scapy.layers.inet.TCP(dport=port,sport=sport,flags='R',seq=cs_sn,ack=sc_sn),
        verbose = False,
    )

# packets = (
#     scapy.layers.inet.IP(dst=ip)
#         / scapy.layers.inet.TCP(dport=port, sport=sport, flags='PA', seq=cs_sn, ack=sc_sn)
#         / payload
# # ).fragment(20)
# )

t = (
    scapy.layers.inet.IP(dst=ip)
    / scapy.layers.inet.TCP(dport=port, sport=sport, flags='PA', seq=cs_sn, ack=sc_sn)
    / payload[:1]
)
# t.show()
# packets = t.fragment(20)
packets = (t,)

# print(packets)
first = True
for p in packets:
    scapy.sendrecv.srp(p, verbose=False, iface=iface, timeout=0.01)
    # if first:
    #     time.sleep(4)
    #     first = False
    time.sleep(0.1)

scapy.sendrecv.srp(
    scapy.layers.inet.IP(dst=ip)
        / scapy.layers.inet.TCP(dport=port, sport=sport, flags='PA', seq=cs_sn + 1, ack=sc_sn)
        / payload[1:],
    verbose = False,
    iface=iface,
    timeout=0.01,
)

# IPython.embed()

# time.sleep(1)
# reset()
