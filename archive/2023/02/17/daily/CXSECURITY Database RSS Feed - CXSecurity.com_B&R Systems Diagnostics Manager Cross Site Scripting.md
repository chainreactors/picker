---
title: B&R Systems Diagnostics Manager Cross Site Scripting
url: https://cxsecurity.com/issue/WLB-2023020027
source: CXSECURITY Database RSS Feed - CXSecurity.com
date: 2023-02-17
fetch_date: 2025-10-04T06:50:54.179758
---

# B&R Systems Diagnostics Manager Cross Site Scripting

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
|  |  | |  | | --- | | **B&R Systems Diagnostics Manager Cross Site Scripting** **2023.02.16**  Credit:  **[Gerhard Hechenberger](https://cxsecurity.com/author/Gerhard%2BHechenberger/1/)**  Risk: **Low**  Local: **No**  Remote: ****Yes****  CVE: **[CVE-2022-4286](https://cxsecurity.com/cveshow/CVE-2022-4286/ "Click to see CVE-2022-4286")**  CWE: **[CWE-79](https://cxsecurity.com/cwe/CWE-79 "Click to see CWE-79")** | |

SEC Consult Vulnerability Lab Security Advisory < 20230214-0 >
=======================================================================
title: Multiple XSS Vulnerabilities
product: B&R Systems Diagnostics Manager
vulnerable version: >=3.00 and <=C4.93
fixed version: >=D4.93
CVE number: CVE-2022-4286
impact: medium
homepage: https://www.br-automation.com
found: 2022-10-28
by: S. Robertz (Office Vienna)
G. Hechenberger (Office Vienna)
SEC Consult Vulnerability Lab
An integrated part of SEC Consult, an Atos company
Europe | Asia | North America
https://www.sec-consult.com
=======================================================================
Vendor description:
-------------------
"Our slogan is our mission. The pursuit of Perfection in Automation has
inspired and guided B&R for over 40 years. To us, perfection means more
than developing the best solutions in industrial automation. It also means
developing the best relationships – with our customers and partners as
well as our employees and suppliers.
Keen foresight and entrepreneurial courage helped us rise quickly into
the ranks of top global players in industrial automation. An intuitive sense
of market dynamics and emerging trends has established us as a pioneer,
leading the way with the most innovative technology on the market.
Our role as the ABB Group's global center for machine and factory automation
strengthens our position of leadership and adds new momentum to our
impressive record of sustained growth."
Source: https://www.br-automation.com/en/about-us/
Business recommendation:
------------------------
The vendor provides a software update which should be installed immediately.
SEC Consult highly recommends to perform a thorough security review of the
product conducted by security professionals to identify and resolve potential
further security issues.
Vulnerability overview/description:
-----------------------------------
1) Multiple Reflected Cross-Site-Scripting Vulnerabilities (CVE-2022-4286)
An attacker can execute arbitrary JavaScript code in the context of the
victim's session, thus perform all actions, exfiltrate information, etc.
In order to exploit this vulnerability the attacker will have to trick
the user into visiting a manipulated URL.
Proof of concept:
-----------------
1) Multiple Reflected Cross-Site-Scripting Vulnerabilities (CVE-2022-4286)
The following URL has to be visited by the victim in order to execute
arbitrary JavaScript code.
http://<PLC-IP>/sdm/cgiFileLoop.cgi?service=javascript:alert(document.domain);%2f%2f&type=512&scope=%3Cfile:///etc/passwd%3E&module=Snapshot&option=3
A very similar vulnerability can be found at another endpoint of the
System Diagnostic Manager (SDM).
http://<PLC-IP>/sdm/svg.cgi?type=cpuusage&index=1%3Cscript%3Ealert(document.domain)%3C/script%3E
Vulnerable / tested versions:
-----------------------------
The following device and firmware version has been tested:
\* B&R X20CP3687X SwModuleVersion 186
According to the vendor, all B&R Automation Runtime (AR) versions >=3.00 and <=C4.93
are affected.
Vendor contact timeline:
------------------------
2022-11-21: Contacting vendor through cybersecurity@br-automation.com.
Sent encrypted advisory.
2022-11-22: Vendor requests B&R Automation Runtime version.
2022-12-01: Vendor confirms vulnerability. Will be fixed with next release.
Asking for timeline.
2022-12-13: Advisory and patch will be published on 2023-02-10.
Vendor offers to share the advisory for review purposes.
2023-01-25: Reviewing vendor advisory, receiving CVE + affected/fixed version
numbers
2023-02-10: Vendor provides the patch.
2023-02-14: Coordinated release of security advisory.
Solution:
---------
The vendor supplies a patch, which should be installed immediately.
The following version mitigates the identified XSS issues:
\* B&R Automation Runtime version >=D4.93
The vendor has published the following security advisory:
https://www.br-automation.com/downloads\_br\_productcatalogue/assets/1675607299099-en-original-1.0.pdf
Workaround:
-----------
Administrators can deactivate the System Diagnostics Manager in case it is not
needed.
Advisory URL:
-------------
https://sec-consult.com/vulnerability-lab/
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
SEC Consult Vulnerability Lab
SEC Consult, an Atos company
Europe | Asia | North America
About SEC Consult Vulnerability Lab
The SEC Consult Vulnerability Lab is an integrated part of SEC Consult, an
Atos company. It ensures the continued knowledge gain of SEC Consult in the
field of network and application security to stay ahead of the attacker. The
SEC Consult Vulnerability Lab supports high-quality penetration testing and
the evaluation of new offensive and defensive technologies for our customers.
Hence our customers obtain the most current information about vulnerabilities
and valid recommendation about the risk profile of new technologies.
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
Interested to work with the experts of SEC Consult?
Send us your application https://sec-consult.com/career/
Interested in improving your cyber security with the experts of SEC Consult?
Contact our local offices https://sec-consult.com/contact/
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
Mail: security-research at sec-consult dot com
Web: https://www.sec-consult.com
Blog: http://blog.sec-consult.com
Twitter: https://twitter.com/sec\_consult
EOF S. Robertz, G. Hechenberger / @2023

[**See this note in RAW Version**](https://cxsecurity.com/ascii/WLB-2023020027)

[Tweet](https://twitter.com/share)

Vote for this issue:
 0
 0

50%

50%

#### **Thanks for you vote!**

####...