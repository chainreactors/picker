---
title: ebankIT 6 Denial Of Service
url: https://cxsecurity.com/issue/WLB-2023050009
source: CXSECURITY Database RSS Feed - CXSecurity.com
date: 2023-05-04
fetch_date: 2025-10-04T11:36:44.446642
---

# ebankIT 6 Denial Of Service

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
|  |  | |  | | --- | | **ebankIT 6 Denial Of Service** **2023.05.03**  Credit:  **[Jake Murphy](https://cxsecurity.com/author/Jake%2BMurphy/1/)**  Risk: **Medium**  Local: **No**  Remote: ****Yes****  CVE: **[CVE-2023-30455](https://cxsecurity.com/cveshow/CVE-2023-30455/ "Click to see CVE-2023-30455")**  CWE: **N/A** | |

CVE-2023-30455
[Description]
An issue was discovered in ebankIT before version 7.
A Denial-of-Service attack is possible through the GET parameter
EStatementsIds located on the
/Controls/Generic/EBMK/Handlers/EStatements/DownloadEStatement.ashx endpoint.
The GET parameter accepts over 100 comma-separated e-statement IDs
without throwing an error. When this many IDs are supplied, the server
takes around 60 seconds to respond and successfully generate the
expected ZIP archive (during this time period, no other pages load). A
threat actor could issue a request to this endpoint with 100+ statement
IDs every 30 seconds, potentially resulting in an overload of the
server for all users.
------------------------------------------
[VulnerabilityType Other]
Denial of Service
------------------------------------------
[Vendor of Product]
ebankIT
------------------------------------------
[Affected Product Code Base]
ebankIT - Omnichannel Digital Banking Platform - Version 6, patched in version 7
------------------------------------------
[Affected Component]
The endpoint existing at /Controls/Generic/EBMK/Handlers/EStatements/DownloadEStatement.ashx?EStatementsIds=\*id\*,\*id\*,\*id\*,etc
------------------------------------------
[Attack Type]
Remote
------------------------------------------
[Impact Denial of Service]
true
------------------------------------------
[Attack Vectors]
I discovered it was possible to perform a Denial-of-Service attack on
the ebankIT platform, potentially resulting in a single user rendering
the entire application inaccessible. The vulnerable endpoint exists on
/Controls/Generic/EBMK/Handlers/EStatements/DownloadEStatement.ashx
and the EStatementsIds GET parameter accepts over 100
comma-separated e-statement IDs without throwing an error. When this
many IDs are supplied, the server takes around 60 seconds to respond
and successfully generate the expected zip file (during this 60
seconds, no other pages load). A threat actor could issue a request to
this endpoint with 100+ statement ID s every 30 seconds, potentially
resulting in overloading the server for all users of the ebankIT
platform. I believe this is being caused by a thread commitment issue
where there are no dedicated threads to individual processes.
------------------------------------------
[Discoverer]
Jake Murphy

[**See this note in RAW Version**](https://cxsecurity.com/ascii/WLB-2023050009)

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