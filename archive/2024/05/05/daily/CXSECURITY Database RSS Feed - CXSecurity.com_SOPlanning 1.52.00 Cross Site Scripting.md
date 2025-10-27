---
title: SOPlanning 1.52.00 Cross Site Scripting
url: https://cxsecurity.com/issue/WLB-2024050009
source: CXSECURITY Database RSS Feed - CXSecurity.com
date: 2024-05-05
fetch_date: 2025-10-06T17:14:06.351951
---

# SOPlanning 1.52.00 Cross Site Scripting

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
|  |  | |  | | --- | | **SOPlanning 1.52.00 Cross Site Scripting** **2024.05.04**  Credit:  **[liquidsky](https://cxsecurity.com/author/liquidsky/1/)**  Risk: **Low**  Local: **No**  Remote: ****Yes****  CVE: **N/A**  CWE: **[CWE-79](https://cxsecurity.com/cwe/CWE-79 "Click to see CWE-79")** | |

Exploit Title: SOPlanning v1.52.00 'groupe\_save.php' XSS (Reflected XSS)
Application: SOPlanning
Version: 1.52.00
Date: 4/22/24
Exploit Author: Joseph McPeters (Liquidsky)
Vendor Homepage: https://www.soplanning.org/en/
Software Link: https://sourceforge.net/projects/soplanning/
Tested on: Linux
CVE: Not yet assigned
Description: SOPlanning v1.52.00 is vulnerable to XSS via the 'groupe\_id' parameters a remote unautheticated attacker can hijack the admin account or other users. The remote attacker can hijack a users session or credentials and perform a takeover of the entire platform.
Example Payload:
"><script>alert('LiQUiDSKY')</script><!--
Reflected XSS: /soplanning/www/process/groupe\_save.php?saved=1&groupe\_id="><script>alert('LiQUiDSKY')</script><!--&nom=Project+New
Analysis: The landing page takes into consideration the user input then redirects to a page where the XSS is shown the payload included in the exploit, escapes the variable where it is held, and comments out the rest to perform a valid reflected XSS attack against any authenticated user the payload was sent to.

[**See this note in RAW Version**](https://cxsecurity.com/ascii/WLB-2024050009)

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