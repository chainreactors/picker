---
title: CKSource CKEditor5 35.4.0 Cross Site Scripting
url: https://cxsecurity.com/issue/WLB-2023020019
source: CXSECURITY Database RSS Feed - CXSecurity.com
date: 2023-02-10
fetch_date: 2025-10-04T06:12:18.838390
---

# CKSource CKEditor5 35.4.0 Cross Site Scripting

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
|  |  | |  | | --- | | **CKSource CKEditor5 35.4.0 Cross Site Scripting** **2023.02.09**  Credit:  **[Manish Pathak](https://cxsecurity.com/author/Manish%2BPathak/1/)**  Risk: **Low**  Local: **No**  Remote: ****Yes****  CVE: **[CVE-2022-48110](https://cxsecurity.com/cveshow/CVE-2022-48110/ "Click to see CVE-2022-48110")**  CWE: **[CWE-79](https://cxsecurity.com/cwe/CWE-79 "Click to see CWE-79")** | |

# Exploit Title: Cross Site Scripting in CKSource's CKEditor5 35.4.0
# Google Dork: N/A
# Date: February 09, 2023
# Exploit Author: Manish Pathak
# Vendor Homepage: https://cksource.com/
# Software Link: https://ckeditor.com/ckeditor-5/download/
# Version: 35.4.0
# Tested on: Linux / Web
# CVE : CVE-2022-48110
CKSource CKEditor5 35.4.0 was discovered to contain a cross-site scripting
(XSS) vulnerability via Full Featured CKEditor5 Widget as the editor fails
to sanitize user provided data.
An attacker can execute arbitrary script in the browser in the context of
the affected site. This can allow the attacker to steal cookie-based
authentication credentials and launch other attacks.
CKEditor5 version 35.4.0 is tested & found to be vulnerable.
Documentation avaiable at
https://ckeditor.com/docs/ckeditor5/latest/features/html-embed.html#security
Security Docs Says """The HTML embed feature does not currently execute
code in <script> tags. However, it will execute code in the on\* and
src="javascript:..." attributes."""
Payload:
<div class="raw-html-embed">
<script>alert(456)</script>
</div>

[**See this note in RAW Version**](https://cxsecurity.com/ascii/WLB-2023020019)

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