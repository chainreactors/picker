---
title: Tiki Wiki CMS Groupware 25.0 Cross Site Request Forgery
url: https://cxsecurity.com/issue/WLB-2023010014
source: CXSECURITY Database RSS Feed - CXSecurity.com
date: 2023-01-12
fetch_date: 2025-10-04T03:36:14.552413
---

# Tiki Wiki CMS Groupware 25.0 Cross Site Request Forgery

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
|  |  | |  | | --- | | **Tiki Wiki CMS Groupware 25.0 Cross Site Request Forgery** **2023.01.11**  Credit:  **[EgiX](https://cxsecurity.com/author/EgiX/1/)**  Risk: **Low**  Local: **No**  Remote: ****Yes****  CVE: **[CVE-2023-22852](https://cxsecurity.com/cveshow/CVE-2023-22852/ "Click to see CVE-2023-22852")**  CWE: **[CWE-352](https://cxsecurity.com/cwe/CWE-352 "Click to see CWE-352")** | |

------------------------------------------------------------------------------
Tiki Wiki CMS Groupware <= 25.0 Two Cross-Site Request Forgery
Vulnerabilities
------------------------------------------------------------------------------
[-] Software Link:
https://tiki.org
[-] Affected Versions:
Version 25.0 and prior versions.
[-] Vulnerabilities Description:
1) The /tiki-importer.php script does not implement any protection
against Cross-Site Request Forgery (CSRF) attacks. As such, an attacker
might force an authenticated user to import arbitrary content (wiki
pages) into TikiWiki by tricking a victim user into browsing to a
specially crafted web page.
2) The /tiki-import\_sheet.php script does not implement any protection
against Cross-Site Request Forgery (CSRF) attacks. As such, an attacker
might force an authenticated user to import arbitrary sheets into
TikiWiki by tricking a victim user into browsing to a specially crafted
web page. Successful exploitation of this vulnerability requires the
“Spreadsheets” feature to be enabled.
[-] Solution:
No official solution is currently available.
[-] Disclosure Timeline:
[06/03/2022] - Vendor notified
[09/01/2023] - Public disclosure
[-] CVE Reference:
The Common Vulnerabilities and Exposures project (cve.mitre.org)
has assigned the name CVE-2023-22852 to this vulnerability.
[-] Credits:
Vulnerabilities discovered by Egidio Romano.
[-] Original Advisory:
http://karmainsecurity.com/KIS-2023-01

[**See this note in RAW Version**](https://cxsecurity.com/ascii/WLB-2023010014)

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