from scapy.contrib.gtp import (
    GTP_U_Header,
    GTPPDUSessionContainer)
from scapy.layers.inet import IP, UDP, Ether
from scapy.layers.dns import DNS, DNSQR
from scapy.all import *

# DNS Query Packet
sendp(
    Ether() /
    IP(src="127.0.10.100", dst="127.0.1.100") /
    UDP(sport=2152, dport=2152) /
    GTP_U_Header(teid=0x00000001) /
    IP(src="172.16.0.2", dst="8.8.8.8") /
    UDP(sport=53, dport=53) /
    DNS(rd=1, qd=DNSQR(qname="connectivitycheck.gstatic.com", qtype="A")),
    iface="VMware Network Adapter VMnet1", count=1
)
