---
title: SEH utnserver Pro/ProMAX / INU-100 20.1.22 XSS / DoS / File Disclosure
url: https://cxsecurity.com/issue/WLB-2024060028
source: CXSECURITY Database RSS Feed - CXSecurity.com
date: 2024-06-11
fetch_date: 2025-10-06T16:54:19.843131
---

# SEH utnserver Pro/ProMAX / INU-100 20.1.22 XSS / DoS / File Disclosure

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
|  |  | |  | | --- | | **SEH utnserver Pro/ProMAX / INU-100 20.1.22 XSS / DoS / File Disclosure** **2024.06.10**  Credit:  **[T. Weber](https://cxsecurity.com/author/T.%2BWeber/1/)**  Risk: **Medium**  Local: **No**  Remote: ****Yes****  CVE: **[CVE-2024-5422](https://cxsecurity.com/cveshow/CVE-2024-5422/ "Click to see CVE-2024-5422")** | **[CVE-2024-5420](https://cxsecurity.com/cveshow/CVE-2024-5420/ "Click to see CVE-2024-5420")** | **[CVE-2024-5421](https://cxsecurity.com/cveshow/CVE-2024-5421/ "Click to see CVE-2024-5421")**  CWE: **[CWE-79](https://cxsecurity.com/cwe/CWE-79 "Click to see CWE-79")** | |

CyberDanube Security Research 20240604-0
-------------------------------------------------------------------------------
title| Multiple Vulnerabilities
product| SEH utnserver Pro/ProMAX / INU-100
vulnerable version| 20.1.22
fixed version| 20.1.28
CVE number| CVE-2024-5420, CVE-2024-5421, CVE-2024-5422
impact| High
homepage| https://www.seh-technology.com/
found| 2024-03-04
by| T. Weber (Office Vienna)
| CyberDanube Security Research
| Vienna | St. Plten
|
| https://www.cyberdanube.com
-------------------------------------------------------------------------------
Vendor description
-------------------------------------------------------------------------------
"We are SEH from Bielefeld - manufacturer of high-quality network solutions.
With over 35 years of experience in the fields of printing and networks, we
offer our customers a broad and high-level expertise in solutions for all types
of business environments."
Source: https://www.seh-technology.com/us/company/about-us.html
Vulnerable versions
-------------------------------------------------------------------------------
utnserver Pro / 20.1.22
utnserver ProMAX / 20.1.22
INU-100 / 20.1.22
Vulnerability overview
-------------------------------------------------------------------------------
1) Stored Cross-Site Scripting (CVE-2024-5420)
A Stored Cross-Site Scripting vulnerability was identified in the web interface
of the device. Multiple parameters, e.g. the device description, can be abused
to inject JavaScript code. An attacker can exploit this vulnerability by luring
a victim to visit a malicious website. Furthermore, it is possible to hijack
the session of the attacked user.
2) Authenticated File Disclosure (CVE-2024-5421)
Files and content of directories can be disclosed by integrated functions of
the device.
3) Denial of Service (CVE-2024-5422)
A Denial-of-Service vulnerability has been identified in the web interface of
the device. This can be triggered by sending a lot of requests that trigger
serial interface access on the device.
Proof of Concept
-------------------------------------------------------------------------------
1) Stored Cross-Site Scripting (CVE-2024-5420)
By accessing to the following URL, an attacker can modify the device
description:
http://$IP/device/description\_en.html
By using malicious JavaScript payload, it is possible to execute arbitrary
code. This snippet demonstrates such a payload:
"><script>alert(document.location)</script>
Saving this text to the device description leads to a persistent cross-site
scripting. Therefore, everyone who openes the device description executes the
injected code in the context of the own browser.
2) Authenticated File Disclosure (CVE-2024-5421)
A hidden function in the web-interface of the device can be used to disclose
directories and files on operating system level. The function can be accessed
directly via the browser:
http://$IP/info/dir?/
This lists the current directory and provides the files to be downloaded.
3) Denial of Service (CVE-2024-5422)
For triggering a denial of service on the device, multiple file descriptors
are opened by using the following script:
-------------------------------------------------------------------------------
#!/bin/bash
echo "Parameters: $1 $2"
last\_iter=$(($2 - 1))
for ((i=1; i<=$2; i++))
do
echo "[$i] Downloading application binary"
if [[ "$i" == "$last\_iter" ]];then
curl http://$1/info/file?/application --output ./file\_${i}.txt &> /dev/null
else
curl http://$1/info/file?/application --output ./file\_${i}.txt &> /dev/null &
fi
done
-------------------------------------------------------------------------------
The vulnerabilities were manually verified on an emulated device by using the
MEDUSA scalable firmware runtime (https://medusa.cyberdanube.com).
Solution
-------------------------------------------------------------------------------
Install firmware version 20.1.28 to fix the vulnerabilities.
Workaround
-------------------------------------------------------------------------------
None
Recommendation
-------------------------------------------------------------------------------
CyberDanube recommends SEH Computertechnik customers to upgrade the firmware to
the latest version available.
Contact Timeline
-------------------------------------------------------------------------------
2024-03-11: Contacting SEH Computertechnik. Received reply from support. Sent
advisory to support.
2024-03-20: Asked for an update. Contact stated, that an internal timeline will
be defined.
2024-04-10: Asked for an update. Contact stated, that the vulnerabilities will
be patched soon.
2024-04-16: Contact sent link to patched firmware release candidate.
2024-05-31: Notified SEH Computertechnik that advisory will be released first
week of June. Received confirmation from SEH Computertechnik.
2024-06-04: Coordinated release of security advisory.
Web: https://www.cyberdanube.com
Twitter: https://twitter.com/cyberdanube
Mail: research at cyberdanube dot com
EOF T. Weber / @2024

[**See this note in RAW Version**](https://cxsecurity.com/ascii/WLB-2024060028)

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
|  | **{{ x.nick }}** ![]() | Date: {{ x.ux \* 1000 | date:'yyyy-MM-dd' }} *{{ x.ux \* 1000 | date:'HH:mm...