---
title: Easy!Appointments 1.5.1 Denial of Service
url: https://cxsecurity.com/issue/WLB-2025050022
source: CXSECURITY Database RSS Feed - CXSecurity.com
date: 2025-05-09
fetch_date: 2025-10-06T22:24:25.229318
---

# Easy!Appointments 1.5.1 Denial of Service

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
|  |  | |  | | --- | | **Easy!Appointments 1.5.1 Denial of Service** **2025.05.08**  Credit:  **[Abdullah Almutairi](https://cxsecurity.com/author/Abdullah%2BAlmutairi/1/)**  Risk: **Low**  Local: **No**  Remote: ****Yes****  CVE: **[CVE-2025-29448](https://cxsecurity.com/cveshow/CVE-2025-29448/ "Click to see CVE-2025-29448")**  CWE: **N/A** | |

# CVE-2025-29448
# Description
booking logic flaw in Easy!Appointments v1.5.1 allows unauthenticated attackers to create appointments with excessively long durations, causing a denial of service by blocking all future booking availability.
# Steps to Reproduce
1. Intercept an appointment booking request.
2. Locate the `post\_data[appointment][end\_datetime]` parameter in the request body.
3. Modify the parameter value to a date far in the future and send the request.
4. The application accepts the long booking, blocking all future availability and causing a denial of service.
# Fixed in Commit
https://github.com/alextselegidis/easyappointments/commit/74633b60f28bdef3cc9f905c0599cef121fee32b

[**See this note in RAW Version**](https://cxsecurity.com/ascii/WLB-2025050022)

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