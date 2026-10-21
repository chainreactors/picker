---
title: PodcastGenerator 3.2.9 Stored XSS
url: https://cxsecurity.com/issue/WLB-2026100002
source: CXSECURITY Database RSS Feed - CXSecurity.com
date: 2026-10-20
fetch_date: 2026-10-21T06:46:59.442514
---

# PodcastGenerator 3.2.9 Stored XSS

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
|  |  | |  | | --- | | **PodcastGenerator 3.2.9 Stored XSS** **2026.10.20**  Credit:  **[Sahil Arya](https://cxsecurity.com/author/Sahil%2BArya/1/)**  Risk: **Low**  Local: **No**  Remote: ****Yes****  CVE: **[CVE-2025-70336](https://cxsecurity.com/cveshow/CVE-2025-70336/ "Click to see CVE-2025-70336")**  CWE: **[CWE-79](https://cxsecurity.com/cwe/CWE-79 "Click to see CWE-79")** | |

# Exploit Title: PodcastGenerator 3.2.9 - Stored XSS
# Date: 2026-08-08
# Exploit Author: Sahil Arya
# Vendor Homepage: https://github.com/PodcastGenerator/PodcastGenerator
# Software Link: https://github.com/PodcastGenerator/PodcastGenerator
# Version: 3.2.9
# Tested on: Windows 11 / XAMPP
# CVE : CVE-2025-70336
Description:
PodcastGenerator 3.2.9 contains a stored Cross-Site Scripting
vulnerability in the Live Items functionality.
An authenticated administrator can inject JavaScript through the
TITLE, SHORT DESCRIPTION, or LONG DESCRIPTION parameters. The
payload is stored and subsequently executed when the Live Item is
rendered in both the administrative Live Items listing and the
public Live Stream page.
Administrative privileges are required only to store the payload.
Unauthenticated access is sufficient to trigger the stored payload
through the public Live Stream page.
Proof of Concept:
1. Log in to the PodcastGenerator administrator panel.
2. Navigate to:
/admin/live\_create.php
3. Insert the following payload into TITLE, SHORT DESCRIPTION,
or LONG DESCRIPTION:
<script>alert(document.domain)</script>
4. Save the Live Item.
5. Navigate to:
/admin/live\_list.php
The JavaScript payload executes.
6. Open the public Live Stream page as an unauthenticated user:
/live.php
7. The same stored payload executes in the visitor's browser.
References:
CVE:
https://www.cve.org/CVERecord?id=CVE-2025-70336
NVD:
https://nvd.nist.gov/vuln/detail/CVE-2025-70336
Advisory:
https://github.com/aryasahil96-manu/CVE-Disclosures/blob/main/CVE-2025-70336

[**See this note in RAW Version**](https://cxsecurity.com/ascii/WLB-2026100002)

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

Copyright **2026**, cxsecurity.com

|  |

Back to Top