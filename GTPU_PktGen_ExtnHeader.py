from scapy.contrib.gtp import (
    GTP_U_Header,
    GTPPDUSessionContainer)
from scapy.layers.inet import IP, UDP, Ether
from scapy.layers.dns import DNS, DNSQR
from scapy.all import *

# DNS Query Packet
sendp(
    Ether(src='00:00:00:00:00:00', dst='00:00:00:00:00:00') /
    IP(src="127.0.1.1", dst="127.0.1.100", flags="DF", id=0x005678) /
    UDP(sport=2152, dport=2152) /
    GTP_U_Header(teid=0x00000005) /
    IP(src="172.16.0.5", dst="8.8.8.8", flags="DF") /
    UDP(sport=5678, dport=53) /
    DNS(id=0x1234, rd=1, qd=DNSQR(qname="www.baidu.com", qtype="A")),
    iface="wlp9s0", count=1
)
