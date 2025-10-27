---
title: phpMyFAQ 3.2.10 Unintended File Download Triggered by Embedded Frames
url: https://cxsecurity.com/issue/WLB-2025050012
source: CXSECURITY Database RSS Feed - CXSecurity.com
date: 2025-05-04
fetch_date: 2025-10-06T22:23:46.904645
---

# phpMyFAQ 3.2.10 Unintended File Download Triggered by Embedded Frames

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
|  |  | |  | | --- | | **phpMyFAQ 3.2.10 Unintended File Download Triggered by Embedded Frames** **2025.05.03**  Credit:  **[George Chen](https://cxsecurity.com/author/George%2BChen/1/)**  Risk: **Medium**  Local: **No**  Remote: ****Yes****  CVE: **N/A**  CWE: **N/A** | |

# Exploit Title: phpMyFAQ v3.2.10 - Unintended File Download Triggered by Embedded Frames
# Date: 13 Dec 2024
# Exploit Author: George Chen
# Vendor Homepage: https://github.com/thorsten/phpMyFAQ/
# Software Link: https://github.com/thorsten/phpMyFAQ/
# Version: v3.2.10
# Tested on: Mac, Win
# CVE : CVE-2024–55889
\*Summary\*
A vulnerability exists in the FAQ Record component of
https://github.com/thorsten/phpMyFAQ v3.2.10 where a privileged attacker
can trigger a file download on a victim’s machine upon page visit by
embedding it in an <iframe> element without user interaction or explicit
consent.
\*Details\*
In http://localhost/admin/index.php?action=editentry&id=20&lang=en, where a
FAQ record is either created or edited, an attacker can insert an iframe,
as “source code”, pointing to a prior “malicious” attachment that the
attacker has uploaded via FAQ “new attachment” upload, such that any page
visits to this FAQ will trigger an automated download (from the edit
screen, download is automated; from the faq page view as a normal user,
depending on the browser, a pop up confirmation may be presented before the
actual download. Firebox browser, for instance, does not require any
interactions).
[image: image.png]
\*PoC\*
1. create a new FAQ record and upload a “malicious” file — in my case, I
uploaded an eicar file. Take note of the uri, ie
“index.php?action=attachment&id=2”
2. in the FAQ record, insert a “source code” blob using the “< >” button
3. insert in the following snippet and save FAQ record:
<p><iframe src="index.php?action=attachment&id=2"></iframe></p> [image:
image.png]
4. Once the edit page reloads, the malicious code will be downloaded
onto the local machine without user interaction:[image: image.png]
Advisory:
https://github.com/thorsten/phpMyFAQ/security/advisories/GHSA-m3r7-8gw7-qwvc
Disclosure: https://geochen.medium.com/cve-2024-55889-03572ae6c35c

[**See this note in RAW Version**](https://cxsecurity.com/ascii/WLB-2025050012)

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