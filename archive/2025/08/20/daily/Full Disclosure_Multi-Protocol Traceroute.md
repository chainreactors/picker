---
title: Multi-Protocol Traceroute
url: https://seclists.org/fulldisclosure/2025/Aug/10
source: Full Disclosure
date: 2025-08-20
fetch_date: 2025-10-07T00:50:57.353486
---

# Multi-Protocol Traceroute

[![](/shared/images/nst-icons.svg#menu)](#menu)
![](/shared/images/nst-icons.svg#close)
[![Home page logo](/images/sitelogo.png)](/)

[Nmap.org](https://nmap.org/)
[Npcap.com](https://npcap.com/)
[Seclists.org](https://seclists.org/)
[Sectools.org](https://sectools.org)
[Insecure.org](https://insecure.org/)

![](/shared/images/nst-icons.svg#search)

[![fulldisclosure logo](/images/fulldisclosure-logo.png)](/fulldisclosure/)

## [Full Disclosure](/fulldisclosure/) mailing list archives

[![Previous](/images/left-icon-16x16.png)](18)
[By Date](date.html#10)
![Next](/images/right-icon-16x16.png)

[![Previous](/images/left-icon-16x16.png)](18)
[By Thread](index.html#10)
![Next](/images/right-icon-16x16.png)

![](/shared/images/nst-icons.svg#search)

# Multi-Protocol Traceroute

---

*From*: Usman Saeed via Fulldisclosure <fulldisclosure () seclists org>
*Date*: Thu, 14 Aug 2025 15:44:27 +0000

---

```
#!/usr/bin/env python3
"""
Adaptive Multi-Protocol Traceroute

Author: Usman Saeed
email: u () defzero net<mailto:u () defzero net>
Website: www.defzero.net<http://www.defzero.net>

Description:
This script is a TTL-based path mapper that reveals routes even when classic traceroute is
filtered. The idea was that it would run in passes: first a conventional trace (ICMP Echo and
rotating TCP SYN ports) to capture the operator view, then advanced carriers that slip past
restrictive policies—QUIC Initial (UDP/443), STUN (UDP/3478), TLS SYN (TCP/443), and
IP-in-IP—followed by optional extended carriers (DoH to a resolver you choose, DoT, TLS 0-RTT/ESNI
labels, GRE, VXLAN, BGP SYN, TLS Heartbeat, and HTTP CONNECT to a proxy). Each hop is annotated
with the technique that succeeded; mDNS/SSDP are auto-enabled only on local/link-local targets. The
script uses raw IP sockets (no Ethernet/ARP) so it works cleanly over tunnel interfaces, and
requires root or cap_net_raw.

(portable on macOS/BSD/Linux)
"""

import sys
import socket
import ipaddress
from random import getrandbits
from typing import Tuple, List, Optional, Callable

from scapy.all import (
    IP, UDP, TCP, ICMP, Raw, RandShort, sr1, GRE, Ether, conf, L3RawSocket
)

conf.L3socket = L3RawSocket
conf.use_pcap = False
conf.probfilter = "ip"
conf.verb = 0

DEFAULT_PORTS: List[int] = [443, 80, 53, 22, 110, 23, 21]

def require_raw_sockets_or_exit():
    try:
        s1 = socket.socket(socket.AF_INET, socket.SOCK_RAW, socket.IPPROTO_RAW)
        s1.close()
        s2 = socket.socket(socket.AF_INET, socket.SOCK_RAW,
                           socket.IPPROTO_ICMP)
        s2.close()
    except PermissionError:
        print("Raw socket privilege required. Use sudo (macOS/Linux) or grant cap_net_raw on Linux.")
        sys.exit(1)

def is_local_or_multicast(addr: str) -> bool:
    try:
        ip = ipaddress.ip_address(addr)
    except ValueError:
        return False
    return ip.is_private or ip.is_link_local or ip.is_multicast

def _build_quic_initial() -> bytes:
    hdr = b"\xc0\x00\x00\x00\x01" + b"\x00" * 2 + b"\x00" + b"\x02" + b"\x01\x02"
    return hdr.ljust(1200, b"\0")

STUN_COOKIE = b"\x21\x12\xA4\x42"

def _build_stun_binding() -> bytes:
    tid = getrandbits(96).to_bytes(12, "big")
    return b"\x00\x01\x00\x00" + STUN_COOKIE + tid

def _build_doh_http_query() -> Raw:
    q = (
        b"GET /dns-query?ct=application/dns-json&name=example.com&type=A HTTP/1.1\r\n"
        b"Host: cloudflare-dns.com\r\nConnection: close\r\n\r\n"
    )
    return Raw(q)

def _build_tls_client_hello() -> bytes:
    return b"\x16\x03\x01\x00\x2e" + b"\x01" * 0x2a

def _build_mdns_query() -> Raw:
    return Raw(
        b"\x00\x00\x00\x00\x00\x01\x00\x00"
        b"\x09_services" + b"\x07_dns-sd" + b"\x04_udp" +
        b"\x05local" + b"\x00\x00\xff\x00\x01"
    )

def _build_ssdp_discover() -> Raw:
    return Raw(
        b"M-SEARCH * HTTP/1.1\r\n"
        b"HOST:239.255.255.250:1900\r\n"
        b"MAN:\"ssdp:discover\"\r\nMX:1\r\nST:ssdp:all\r\n\r\n"
    )

def _build_gre_inner():
    return IP(src="192.0.2.1", dst="198.51.100.1") / UDP(sport=RandShort(), dport=33434)

def _build_vxlan_packet():
    inner_eth = Ether() / IP(src="192.0.2.1", dst="198.51.100.1") / \
        UDP(sport=RandShort(), dport=33434)
    vxlan_hdr = b"\x08\x00" + getrandbits(24).to_bytes(3, 'big') + b"\x00" * 4
    return Raw(vxlan_hdr) / inner_eth

def _build_tls_heartbeat() -> Raw:
    return Raw(b"\x18\x03\x01\x00\x03\x01\x00\x00\x00")

def build_icmp_probe(dst: str, ttl: int):
    return IP(dst=dst, ttl=ttl) / ICMP()

def build_tcp_cycle_probe(ports: List[int]) -> Callable[[str, int], object]:
    def _builder(dst: str, ttl: int):
        port = ports[(ttl - 1) % len(ports)]
        return IP(dst=dst, ttl=ttl) / TCP(sport=RandShort(), dport=port, flags="S")
    return _builder

def build_quic_probe(dst: str, ttl: int):
    return IP(dst=dst, ttl=ttl) / UDP(sport=RandShort(), dport=443) / Raw(_build_quic_initial())

def build_stun_probe(dst: str, ttl: int):
    return IP(dst=dst, ttl=ttl) / UDP(sport=RandShort(), dport=3478) / Raw(_build_stun_binding())

def build_tls_syn_probe(dst: str, ttl: int):
    return IP(dst=dst, ttl=ttl) / TCP(sport=RandShort(), dport=443, flags="S")

def build_ipip_probe(dst: str, ttl: int):
    inner = _build_gre_inner()
    return IP(dst=dst, ttl=ttl, proto=4) / inner

def build_doh_probe(doh_host: str) -> Callable[[str, int], object]:

    def _builder(_dst: str, ttl: int):
        return IP(dst=doh_host, ttl=ttl) / TCP(sport=RandShort(), dport=443, flags="S")
    return _builder

def build_dot_probe(dst: str, ttl: int):
    return IP(dst=dst, ttl=ttl) / TCP(sport=RandShort(), dport=853, flags="S")

def build_tls13_0rtt_probe(dst: str, ttl: int):

    return IP(dst=dst, ttl=ttl) / TCP(sport=RandShort(), dport=443, flags="S")

def build_esni_probe(dst: str, ttl: int):

    return IP(dst=dst, ttl=ttl) / TCP(sport=RandShort(), dport=443, flags="S")

def build_mdns_probe(dst: str, ttl: int):
    return IP(dst="224.0.0.251", ttl=ttl) / UDP(sport=RandShort(), dport=5353) / _build_mdns_query()

def build_ssdp_probe(dst: str, ttl: int):
    return IP(dst="239.255.255.250", ttl=ttl) / UDP(sport=RandShort(), dport=1900) / _build_ssdp_discover()

def build_gre_probe(dst: str, ttl: int):
    return IP(dst=dst, ttl=ttl, proto=47) / GRE() / _build_gre_inner()

def build_vxlan_probe(dst: str, ttl: int):
    return IP(dst=dst, ttl=ttl) / UDP(sport=RandShort(), dport=4789) / _build_vxlan_packet()

def build_bgp_probe(dst: str, ttl: int):
    return IP(dst=dst, ttl=ttl) / TCP(sport=RandShort(), dport=179, flags="S")

def build_http_connect_probe(proxy_host: str, proxy_port: int) -> Callable[[str, int], object]:

    def _builder(dst: str, ttl: int):
        req = f"CONNECT {dst}:443 HTTP/1.1\r\nHost: {dst}\r\nProxy-Connection: keep-alive\r\n\r\n".encode()
        return IP(dst=proxy_host, ttl=ttl) / TCP(sport=RandShort(), dport=proxy_port, flags="S") / Raw(req)
    return _builder

def build_tls_heartbeat_probe(dst: str, ttl: int):
    return IP(dst=dst, ttl=ttl) / TCP(sport=RandShort(), dport=443, flags="PA") / _build_tls_heartbeat()

def classify_response(pkt) -> Tuple[str, bool]:
    if pkt.haslayer(ICMP):
        t = pkt[ICMP].type
        if t == 11:
            return pkt.src, False
        if t in (0, 3):
            return pkt.src, True
    if pkt.haslayer(TCP):
        f = pkt[TCP].flags
        if f & 0x12 or f & 0x14:
            return pkt.src, True
    if pkt.haslayer(UDP):
        return pkt.src, True
    return pkt.src, False

Technique = Tuple[str, Callable[[str, int], object]]

def single_pass(dst: str, techs: List[Technique], max_ttl: int, timeout: float):
    for ttl in range(1, max_ttl + 1):
        reported = False
        for tag, builder in techs:
            pkt = builder(dst, ttl)
            try:
                ans = sr1(pkt, timeout=timeout, verbose=0)
            except PermissionError:
                print(
                    "Raw socket privilege required. Run with sudo or grant cap_net_raw.")
  ...