from scapy.contrib.gtp import (
    GTP_U_Header,
    GTPEchoRequest,
    GTPEchoResponse
)
from scapy.all import *


def request():
    sendp(
        Ether() /
        IP(src="192.168.85.1", dst="192.168.85.100") /
        UDP(sport=2152, dport=2152)/GTP_U_Header(teid=100, next_ex=133) /
        GTPEchoRequest(),
        iface="VMware Network Adapter VMnet1", count=1
    )


def response():
    sendp(
        Ether() /
        IP(src="192.168.85.1", dst="192.168.85.100") /
        UDP(sport=2152, dport=2152)/GTP_U_Header(teid=100, next_ex=133) /
        GTPEchoResponse(),
        iface="VMware Network Adapter VMnet1", count=1
    )


if __name__ == "__main__":
    request()
    response()
