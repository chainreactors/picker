---
title: Dinstar FXO Analog VoIP Gateway DAG2000-16O Cross Site Scripting
url: https://cxsecurity.com/issue/WLB-2022100066
source: CXSECURITY Database RSS Feed - CXSecurity.com
date: 2022-10-27
fetch_date: 2025-10-03T20:57:35.099560
---

# Dinstar FXO Analog VoIP Gateway DAG2000-16O Cross Site Scripting

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
|  |  | |  | | --- | | **Dinstar FXO Analog VoIP Gateway DAG2000-16O Cross Site Scripting** **2022.10.26**  Credit:  **[Yehia Elghaly](https://cxsecurity.com/author/Yehia%2BElghaly/1/)**  Risk: **Low**  Local: **No**  Remote: ****Yes****  CVE: **N/A**  CWE: **[CWE-79](https://cxsecurity.com/cwe/CWE-79 "Click to see CWE-79")** | |

# Exploit Title: Dinstar FXO Analog VoIP Gateway DAG2000-16O Stored Cross Site Scripting
# Google Dork: NA
# Date: 25/10/2022
# Exploit Author: Yehia Elghaly
# Vendor Homepage: https://www.dinstar.com/
# Software Link: https://www.dinstar.com/analog-voip-gateway/16-fxo/
# Version: DAG2000-16O
# CVE: N/A
Summary: DAG1000-16O FXO analog gateway is a type of access gateway offering seamless connectivity between IP-based telephony networks and legacy telephones (POTS) and PBX systems. The analog gateway has 16 FXO ports and is used to connect to analog PBX or the PSTN lines of telecom carriers. With the standard SIP protocol, it's compatible with leading IMS/NGN platforms and SIP-based IP Phone systems. It provides low-cost and easy-to-use VoIP solutions for small and medium businesses, call centers, SOHO, remote offices as well as enterprises with multiple branches.
Description: The attacker can able to convince a victim to visit a URL referencing a vulnerable page, malicious JavaScript content may be executed within the context of the victim's browser.: Stored XSS found on when (Add new Port) affected field is (Primary Authenticate ID)
Payload: <script>alert(44)</script>
[Affected Component]
(Add new Port)--> (Primary Authenticate ID)

[**See this note in RAW Version**](https://cxsecurity.com/ascii/WLB-2022100066)

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