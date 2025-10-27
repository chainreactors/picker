---
title: Sitefinity 15.0 Cross Site Scripting
url: https://cxsecurity.com/issue/WLB-2024060014
source: CXSECURITY Database RSS Feed - CXSecurity.com
date: 2024-06-05
fetch_date: 2025-10-06T16:55:14.558990
---

# Sitefinity 15.0 Cross Site Scripting

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
|  |  | |  | | --- | | **Sitefinity 15.0 Cross Site Scripting** **2024.06.04**  Credit:  **[Aldi Saputra Wahyudi](https://cxsecurity.com/author/Aldi%2BSaputra%2BWahyudi/1/)**  Risk: **Low**  Local: **No**  Remote: ****Yes****  CVE: **[CVE-2023-27636](https://cxsecurity.com/cveshow/CVE-2023-27636/ "Click to see CVE-2023-27636")**  CWE: **[CWE-79](https://cxsecurity.com/cwe/CWE-79 "Click to see CWE-79")** | |

# Exploit Title: Sitefinity 15.0 - Cross-Site Scripting (XSS)
# Date: 2023-12-05
# Exploit Author: Aldi Saputra Wahyudi
# Vendor Homepage: https://www.progress.com/sitefinity-cms
# Version: < 15.0.0
# Tested on: Windows/Linux
# CVE : CVE-2023-27636
# Description: In the backend of the Sitefinity CMS, a Cross-site scripting vulnerability has been discovered in all features that use SF-Editor
# Steps To Reproduce:
Attacker as lower privilege
Victim as Higher privilege
1. Login as an Attacker
2. Go to the function using the SF Editor, go to the news page as example
3. Create or Edit news item
4. On the content form, insert the XSS payload as HTML
5. After the payload is inserted, click on the content form (just click) and publish or save
6. If the victim visits the page with XSS payload, XSS will be triggered
Payload: <noalert><iframe src="javascript:alert(document.domain);">

[**See this note in RAW Version**](https://cxsecurity.com/ascii/WLB-2024060014)

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