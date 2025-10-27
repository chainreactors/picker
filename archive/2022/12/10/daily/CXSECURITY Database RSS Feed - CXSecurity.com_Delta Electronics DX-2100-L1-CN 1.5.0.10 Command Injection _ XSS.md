---
title: Delta Electronics DX-2100-L1-CN 1.5.0.10 Command Injection / XSS
url: https://cxsecurity.com/issue/WLB-2022120017
source: CXSECURITY Database RSS Feed - CXSecurity.com
date: 2022-12-10
fetch_date: 2025-10-04T01:05:21.145779
---

# Delta Electronics DX-2100-L1-CN 1.5.0.10 Command Injection / XSS

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
|  |  | |  | | --- | | **Delta Electronics DX-2100-L1-CN 1.5.0.10 Command Injection / XSS** **2022.12.09**  Credit:  **[T. Weber](https://cxsecurity.com/author/T.%2BWeber/1/)**  Risk: **Medium**  Local: **No**  Remote: ****Yes****  CVE: **N/A**  CWE: **[CWE-79](https://cxsecurity.com/cwe/CWE-79 "Click to see CWE-79")  [CWE-78](https://cxsecurity.com/cwe/CWE-78 "Click to see CWE-78")** | |

CyberDanube Security Research 20221130-0
-------------------------------------------------------------------------------
title| Multiple Vulnerabilities
product| Delta Electronics DX-2100-L1-CN
vulnerable version| V1.5.0.10
fixed version| V1.5.0.12
CVE number| -
impact| High
homepage| https://www.deltaww.com
found| 2022-08-01
by| T. Weber (Office Vienna)
| CyberDanube Security Research
| Vienna | St. Pölten
|
| https://www.cyberdanube.com
-------------------------------------------------------------------------------
Vendor description
-------------------------------------------------------------------------------
"Delta, founded in 1971, is a global provider of power and thermal
management
solutions. Its mission statement, "To provide innovative, clean and energy
-efficient solutions for a better tomorrow," focuses on addressing key
environmental issues such as global climate change. As an energy-saving
solutions provider with core competencies in power electronics and
automation,
Delta's business categories include Power Electronics, Automation, and
Infrastructure."
Source: https://www.deltaww.com/en-US/about/aboutProfile
Vulnerable versions
-------------------------------------------------------------------------------
DX-2100-L1-CN / V1.5.0.10
Vulnerability overview
-------------------------------------------------------------------------------
1) Authenticated Command Injection
An authenticated command injection has been identified in the web
configuration
service of the device. It can be used to execute system commands on the
OS from
the device in the context of the user "root". Therefore, a full
compromization
of the device is possible by having credentials for the web service only.
2) Stored Cross-Site Scripting
A stored cross-site scripting vulnerability has been identified in the
function
"net diagnosis" on the device's web configuration service. This can be
exploited in the context of a victim's session.
Proof of Concept
-------------------------------------------------------------------------------
1) Authenticated Command Injection
The parameter "diagnose\_address" contains the payload ";ls /;", which
basically
prints the content of the root directory to the serial terminal of the
device.
http://192.168.3.150/lform/net\_diagnose?action=diagnose&diagnose\_type=0&diagnose\_address=;ls%20/;
The output can be seen in the context of a virtualized firmware clone,
as used
to find this vulnerability, but is usually invisible to a customer.
Therefore,
a more visible payload may be commands that interact via the network, like
";ping 192.168.0.10;". This command will ping a device on the
corresponding IP
address within the local network.
2) Stored Cross-Site Scripting
The following code prints the current cached cookies of a user's session
to the
screen. The JavaScript code will be stored on the device permanently.
===============================================================================
POST /lform/urlfilter?action=save HTTP/1.1
Host: 192.168.3.150
Accept: \*/\*
Accept-Language: de,en-US;q=0.7,en;q=0.3
Accept-Encoding: gzip, deflate
Content-Type: application/x-www-form-urlencoded
Content-Length: 190
Connection: keep-alive
Cookie: language=en\_US; userindex=1; loginexpire=1648630746607; session=30
lan\_ipaddr=192.168.5.5&lan\_netmask=255.255.255.0&src\_addr\_start=&src\_addr\_end=&editnum=0&bfilter\_urllist=0&url\_addr=<script>alert(document.cookie)</script>&src\_addr\_type=0&filter\_state=1
===============================================================================
The vulnerabilities were manually verified on an emulated device by
using the
MEDUSA scalable firmware runtime (https://medusa.cyberdanube.com).
Solution
-------------------------------------------------------------------------------
Update to firmware version V1.5.0.12.
Workaround
-------------------------------------------------------------------------------
None
Recommendation
-------------------------------------------------------------------------------
CyberDanube recommends Delta Electronics customers to upgrade the
firmware to
the latest version available.
Contact Timeline
-------------------------------------------------------------------------------
2022-08-02: Contacting Delta Electronics.
2022-08-10: Vendor requested the advisory without encryption; Sent
advisory to
Delta Electronics.
2022-08-16: Security contact asked few questions regarding responsible
disclosure; Sent answers.
2022-08-30: Asked for an update.
2022-09-01: Vendor responded, that they will need more time to resolve the
issues; Provided additional 30 days (until 2022-11-02) for
patching.
2022-10-11: Asked for an update.
2022-10-12: Vendor responded, that fixing will be done 2022-11-15; Shifted
release date to this date.
2022-10-16: Vendor shifted release date again to 2022-11-18. Shifted
advisory
release date to the same day.
2022-10-17: Asked for an update regarding the release; No answer.
2022-10-18: Asked for an update and shifted release date to 2022-10-22.
2022-10-19: Vendor responded, that there were problems at releasing the
patch.
Contact stated, that the patch will delay until end of
November.
2022-10-21: Asked vendor for a concrete release date; No answer.
2022-10-28: Announced advisory release date for 2022-10-30 to vendor.
2022-10-29: Found firmware patches with issue date 2022-11-25 on vendors
website.
2022-10-30: Vendor confirmed fixes. Coordinated release of security
advisory.
Web: https://www.cyberdanube.com
Twitter: https://twitter.com/cyberdanube
Mail: research at cyberdanube dot com
EOF T. Weber / @2022

[**See this note in RAW Version**](https://cxsecurity.com/ascii/WLB-2022120017)

[Tweet](https://twitter.com/share)

Vote for this issue:
 0
 0

50%...