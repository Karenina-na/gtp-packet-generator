from scapy.contrib.gtp import (
    GTP_U_Header,
    GTPPDUSessionContainer)
from scapy.all import *

sendp(
    Ether() /
    IP(src="192.168.85.1", dst="192.168.85.100") /
    UDP(sport=2152, dport=2152)/GTP_U_Header(teid=100, next_ex=133) /
    GTPPDUSessionContainer(type=1, QFI=6) /
    IP(src="192.168.10.10", dst="8.8.8.8") /
    TCP(sport=5001, dport=53),

    iface="VMware Network Adapter VMnet1", count=5
)
