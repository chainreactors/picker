---
title: Drupal H5P Module 2.0.0 Zip Slip Traversal
url: https://cxsecurity.com/issue/WLB-2022120009
source: CXSECURITY Database RSS Feed - CXSecurity.com
date: 2022-12-06
fetch_date: 2025-10-04T00:33:19.982115
---

# Drupal H5P Module 2.0.0 Zip Slip Traversal

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
|  |  | |  | | --- | | **Drupal H5P Module 2.0.0 Zip Slip Traversal** **2022.12.05**  Credit:  **[EgiX](https://cxsecurity.com/author/EgiX/1/)**  Risk: **Medium**  Local: **No**  Remote: ****Yes****  CVE: **N/A**  CWE: **[CWE-22](https://cxsecurity.com/cwe/CWE-22 "Click to see CWE-22")** | |

------------------------------------------------------------------
Drupal H5P Module <= 2.0.0 (isValidPackage) Zip Slip Vulnerability
------------------------------------------------------------------
[-] Software Link:
https://www.drupal.org/project/h5p
[-] Affected Versions:
Version 2.0.0-alpha2 and prior versions.
Version 7.x-1.50 and prior versions.
[-] Vulnerability Description:
The vulnerability is located within the H5PValidator::isValidPackage()
method. This implements the following check in order to skip any file or
folder starting with a dot or underscore within the uploaded h5p
archive:
891. $fileName = $zip->statIndex($i)['name'];
892.
893. if (preg\_match('/(^[\.\_]|\/[\.\_])/', $fileName) !== 0) {
894. continue; // Skip any file or folder starting with a . or \_
894. }
This regex check should be enough to prevent path traversal attacks
through zipped filenames (Zip Slip attacks), because it checks for the
string “/.” within the filename, thus preventing directory traversal
attacks. However, the vulnerability exists if Drupal is running on a
Windows server, because in this case the attacker can provide a
malicious h5p archive containing a filename with path traversal
sequences like “..\..\..”, which would bypass the above regex check.
This can be exploited to write (or overwrite) semi-arbitrary files in
the file system via directory traversal sequences, potentially leading
to Stored Cross-Site Scripting (XSS) and other kind of attacks.
[-] Solution:
No official solution is currently available.
[-] Disclosure Timeline:
[22/11/2021] - Vendor notified
[28/02/2022] - Vendor proposed a possible patch
[28/02/2022] - Vendor notified about the ineffective patch, provided a
fix suggestion
[01/03/2022] - Vendor fixed the previous patch
[30/03/2022] - Asked update about the public disclosure and release of a
patch, no response
[22/11/2022] - After one year still no official solution available
[03/12/2022] - Public disclosure
[-] CVE Reference:
The Common Vulnerabilities and Exposures project (cve.mitre.org)
has not assigned a CVE identifier for this vulnerability.
[-] Credits:
Vulnerability discovered by Egidio Romano.
[-] Other References:
https://security.drupal.org/node/175968
[-] Original Advisory:
http://karmainsecurity.com/KIS-2022-06

[**See this note in RAW Version**](https://cxsecurity.com/ascii/WLB-2022120009)

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