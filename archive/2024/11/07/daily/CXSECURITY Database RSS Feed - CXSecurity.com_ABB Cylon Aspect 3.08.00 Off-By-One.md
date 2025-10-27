---
title: ABB Cylon Aspect 3.08.00 Off-By-One
url: https://cxsecurity.com/issue/WLB-2024110006
source: CXSECURITY Database RSS Feed - CXSecurity.com
date: 2024-11-07
fetch_date: 2025-10-06T19:12:29.591526
---

# ABB Cylon Aspect 3.08.00 Off-By-One

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
|  |  | |  | | --- | | **ABB Cylon Aspect 3.08.00 Off-By-One** **2024.11.06**  Credit:  **[LiquidWorm](https://cxsecurity.com/author/LiquidWorm/1/)**  Risk: **Low**  Local: **No**  Remote: ****Yes****  CVE: **N/A**  CWE: **N/A** | |

ABB Cylon Aspect 3.08.00 (log(Mix/Yum)Lookup.php) Off-by-One Error in Log Parsing
Vendor: ABB Ltd.
Product web page: https://www.global.abb
Affected version: NEXUS Series, MATRIX-2 Series, ASPECT-Enterprise, ASPECT-Studio
Firmware: <=3.08.00
Summary: ASPECT is an award-winning scalable building energy management
and control solution designed to allow users seamless access to their
building data through standard building protocols including smart devices.
Desc: A vulnerability was identified in a PHP script where an off-by-one
error in array access could lead to undefined behavior and potential DoS.
The issue arises in a loop that iterates over an array using a <= condition,
allowing access to an out-of-bounds index. This can trigger errors or unexpected
behavior when processing data, potentially crashing the application. Successful
exploitation of this vulnerability can lead to a crash or disruption of service,
especially if the script handles large data sets.
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
Advisory ID: ZSL-2024-5861
Advisory URL: https://www.zeroscience.mk/en/vulnerabilities/ZSL-2024-5861.php
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
$ cat logYumLookup.php
...
...
$line = file($logFile);
{
$x = 0;
$data = "";
for ($i = 0; $i <= count($line); $i++) { // Off-by-one error
$data = $data . $line[$i]; // Potential out-of-bounds access
$nextNumber = $i + 1;
//need to check to see what the next line starts with so we know to include the next line in this bucket of data or a new bucket.
$arrValues[$x] = $data;
$x++;
$data = "";
}
}
...
...
$ cat logMixLookup.php
...
...
$x = 0;
$data = "";
for ($i = 0; $i <= count($line); $i++) { Off-by-one error
if ((strncmp($line[$i], "INFO", 4) == 0) || (strncmp($line[$i], "DEBUG", 5) == 0) || (strncmp($line[$i], "WARN", 4) == 0) || (strncmp($line[$i], "ERROR", 5) == 0) || (strncmp($line[$i], "FATAL", 5) == 0)) {
$logCode = lookupLogOptionValue(substr($line[$i], 0, 5));
...
...
$ curl http://192.168.73.31/logMixLookup.php?logFile=/var/log/yum.log
...
...
PHP Warning: Undefined array key 31337 in /var/log/yum.log on line 1337

[**See this note in RAW Version**](https://cxsecurity.com/ascii/WLB-2024110006)

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