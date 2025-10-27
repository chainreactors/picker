---
title: sacco-1.0-Multiple-SQLi
url: https://cxsecurity.com/issue/WLB-2025090009
source: CXSECURITY Database RSS Feed - CXSecurity.com
date: 2025-09-22
fetch_date: 2025-10-02T20:29:49.361339
---

# sacco-1.0-Multiple-SQLi

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
|  |  | |  | | --- | | **sacco-1.0-Multiple-SQLi** **2025.09.21**  Credit:  **[nu11secur1ty](https://cxsecurity.com/author/nu11secur1ty/1/)**  Risk: **Medium**  Local: **No**  Remote: ****Yes****  CVE: **N/A**  CWE: **N/A** | |

# Titles: sacco-1.0-Multiple-SQLi
# sacco\_shield-1.0-msf-sqlmap-nu11secur1ty-BurpSuite-EXPLOIT!
# Author: nu11secur1ty
# Date: 09/20/2025
# Vendor: https://www.mayurik.com/
# Software: https://www.sourcecodester.com/php/15372/open-source-sacco-management-system-free-download.html
# Reference: https://portswigger.net/web-security/sql-injection
## Description:
The username parameter appears to be vulnerable to SQL injection attacks. A single quote was submitted in the username parameter, and a database error message was returned. Two single quotes were then submitted and the error message disappeared. You should review the contents of the error message, and the application's handling of other input, to confirm whether a vulnerability is present.
Additionally, the payload '+(select\*from(select(sleep(20)))a)+' was submitted in the username parameter. The application took 20023 milliseconds to respond to the request, compared with 19 milliseconds for the original request, indicating that the injected SQL command caused a time delay.
STATUS: HIGH-CRITICAL Vulnerability
[+]Exploit:
[href](https://nu11secur1ty.github.io/DownGit/#/home?url=https://github.com/nu11secur1ty/metasploit-framework-nu11secur1ty/tree/main/modules/auxiliary/MSF/sacco)
# Reproduce:
[href](https://www.patreon.com/posts/sacco-shield-1-0-139316124)
# Time spent:
35:15:00
WARNING: IF YOU USE THIS FOR AN UNAUTHORIZED ATTACK, YOU WILL BE RESPONSIBLE IN FRONT OF THE LAW!!! THIS IS A COUPLE OF DAYS' SECURITY RESEARCHING. PLEASE RESPECT THE WORK OF THE HACKERS - INCLUDING MY WORK, THE INTERNET WOULD NOT EXIST WITHOUT US! 😎
more: https://github.com/nu11secur1ty/metasploit-framework-nu11secur1ty
more: https://github.com/nu11secur1ty/sqlmap-nu11secur1ty
--
System Administrator - Infrastructure Engineer
Penetration Testing Engineer
Exploit developer at https://packetstormsecurity.com/ https://cve.mitre.org/index.html
https://cxsecurity.com/ and https://www.exploit-db.com/
home page: https://www.asc3t1c-nu11secur1ty.com/
hiPEnIMR0v7QCo/+SEH9gBclAAYWGnPoBIQ75sCj60E=
nu11secur1ty <http://nu11secur1ty.com/>

[**See this note in RAW Version**](https://cxsecurity.com/ascii/WLB-2025090009)

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