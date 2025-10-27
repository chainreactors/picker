---
title: Atrocore 1.5.25 Shell Upload
url: https://cxsecurity.com/issue/WLB-2023020029
source: CXSECURITY Database RSS Feed - CXSecurity.com
date: 2023-02-17
fetch_date: 2025-10-04T06:50:52.916585
---

# Atrocore 1.5.25 Shell Upload

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
|  |  | |  | | --- | | **Atrocore 1.5.25 Shell Upload** **2023.02.16**  Credit:  **[nu11secur1ty](https://cxsecurity.com/author/nu11secur1ty/1/)**  Risk: **High**  Local: **No**  Remote: ****Yes****  CVE: **N/A**  CWE: **[CWE-264](https://cxsecurity.com/cwe/CWE-264 "Click to see CWE-264")** | |

## Title: atrocore-1.5.25 User interaction - Unauthenticated File upload - RCE
## Author: nu11secur1ty
## Date: 02.16.2023
## Vendor: https://atropim.com/
## Software: https://github.com/atrocore/atrocore/releases/tag/1.5.25
## Reference: https://portswigger.net/web-security/file-upload
## Description:
The `Create Import Feed` option with `glyphicon-glyphicon-paperclip`
function appears to be vulnerable to User interaction -
Unauthenticated File upload - RCE attacks.
The attacker can easily upload a malicious then can execute the file
and can get VERY sensitive information about the configuration of this
system, after this he can perform a very nasty attack.
STATUS: HIGH Vulnerability CRITICAL
[+]Payload:
```PHP
<?php
phpinfo();
?>
```
## Reproduce:
[href](https://github.com/nu11secur1ty/CVE-nu11secur1ty/tree/main/vendors/atrocore/atrocore-1.5.25)
## Reference:
[href](https://portswigger.net/web-security/file-upload)
## Proof and Exploit:
[href](https://streamable.com/g8998d)
## Time spend:
00:45:00
--
System Administrator - Infrastructure Engineer
Penetration Testing Engineer
Exploit developer at https://packetstormsecurity.com/
https://cve.mitre.org/index.html
https://cxsecurity.com/ and https://www.exploit-db.com/
0day Exploit DataBase https://0day.today/
home page: https://www.nu11secur1ty.com/
hiPEnIMR0v7QCo/+SEH9gBclAAYWGnPoBIQ75sCj60E=
nu11secur1ty <http://nu11secur1ty.com/>

[**See this note in RAW Version**](https://cxsecurity.com/ascii/WLB-2023020029)

[Tweet](https://twitter.com/share)

Vote for this issue:
 2
 0

100%

0%

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