---
title: Windows Explorer - NTLM Hash Disclosure via .library-ms in ZIP Archive
url: https://cxsecurity.com/issue/WLB-2025060002
source: CXSECURITY Database RSS Feed - CXSecurity.com
date: 2025-06-05
fetch_date: 2025-10-06T22:49:43.835962
---

# Windows Explorer - NTLM Hash Disclosure via .library-ms in ZIP Archive

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
|  |  | |  | | --- | | **Windows Explorer - NTLM Hash Disclosure via .library-ms in ZIP Archive** **2025.06.04**  Credit:  **[Mohammed Idrees Banyamer](https://cxsecurity.com/author/Mohammed%2BIdrees%2BBanyamer/1/)**  Risk: **Medium**  Local: ****Yes****  Remote: **No**  CVE: **[CVE-2025-24071](https://cxsecurity.com/cveshow/CVE-2025-24071/ "Click to see CVE-2025-24071")**  CWE: **N/A** | |

#!/usr/bin/env python3
# Exploit Title: Windows Explorer - NTLM Hash Disclosure via .library-ms in ZIP Archive
# Exploit Author: Mohammed Idrees Banyamer
# Twitter/GitHub: @mbanyamer
# Date: 2025-05-27
# CVE: CVE-2025-24071
# Vendor: Microsoft
# Affected Versions: Windows 10/11 (All supporting .library-ms and SMB)
# Tested on: Windows 11 (23H2)
# Type: Local / Remote (NTLM Leak)
# Platform: Windows
# Vulnerability Type: Information Disclosure
# Description:
# Windows Explorer automatically initiates an SMB authentication request when a
# .library-ms file is extracted from a ZIP archive. This causes NTLM credentials
# (in hashed format) to be leaked to a remote SMB server controlled by the attacker.
# No user interaction is required beyond extraction.
# Country : Jordan
Description:
CVE-2025-24071 is a vulnerability that allows attackers to capture a victim’s NTLMv2 hash automatically upon extracting a specially crafted RAR or ZIP archive containing a .library-ms file. This file references an attacker-controlled SMB path within its <simpleLocation> tag.
Once the archive is extracted, Windows Explorer and the Windows Search Indexing service (SearchProtocolHost.exe) automatically parse the .library-ms file to generate metadata, icons, or previews. This parsing process initiates an unsolicited SMB connection to the attacker's server, resulting in the NTLMv2 hash of the victim being sent without any user interaction
Impact:
NTLMv2 hash disclosure
Enables pass-the-hash attacks
Facilitates lateral movement within internal networks
Exploitation Steps:
Create a .library-ms file pointing to a remote SMB share.
Compress it into a RAR or ZIP archive.
Deliver the archive to the target.
Upon extraction, the victim’s system initiates an SMB request to the attacker, leaking the NTLM hash.
Requirements:
Windows system with Explorer and Indexing Services enabled
Outbound SMB traffic not restricted
Mitigation:
Block outbound SMB (ports 445 and 139)
Disable Windows Search Indexing if unnecessary
Avoid extracting archives from untrusted sources

[**See this note in RAW Version**](https://cxsecurity.com/ascii/WLB-2025060002)

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