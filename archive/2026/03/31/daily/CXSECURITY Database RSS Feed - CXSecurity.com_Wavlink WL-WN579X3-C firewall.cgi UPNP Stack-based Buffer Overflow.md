---
title: Wavlink WL-WN579X3-C firewall.cgi UPNP Stack-based Buffer Overflow
url: https://cxsecurity.com/issue/WLB-2026030037
source: CXSECURITY Database RSS Feed - CXSecurity.com
date: 2026-03-31
fetch_date: 2026-04-01T04:45:14.366459
---

# Wavlink WL-WN579X3-C firewall.cgi UPNP Stack-based Buffer Overflow

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
|  |  | |  | | --- | | **Wavlink WL-WN579X3-C firewall.cgi UPNP Stack-based Buffer Overflow** **2026.03.31**  Credit:  **[Mohammed Idrees Banyamer](https://cxsecurity.com/author/Mohammed%2BIdrees%2BBanyamer/1/)**  Risk: **Medium**  Local: **No**  Remote: ****Yes****  CVE: **[CVE-2026-5004](https://cxsecurity.com/cveshow/CVE-2026-5004/ "Click to see CVE-2026-5004")**  CWE: **[CWE-121 (Stack-based Buffer Overflow)](https://cxsecurity.com/cwe/CWE-121%20%28Stack-based%20Buffer%20Overflow%29 "Click to see CWE-121 (Stack-based Buffer Overflow)")**  **[**Dork:** no](https://cxsecurity.com/dorks/)** | |

# Exploit Title: Wavlink WL-WN579X3-C firewall.cgi UPNP Stack-based Buffer Overflow
# CVE: CVE-2026-5004
# Date: 2026-03-29
# Exploit Author: Mohammed Idrees Banyamer
# Author Country: Jordan
# Instagram: @banyamer\_security
# Author GitHub: https://github.com/mbanyamer
# Author Blog: https://banyamersecurity.com/blog/
# Vendor Homepage: https://www.wavlink.com
# Affected: Wavlink WL-WN579X3-C firmware version 231124
# Tested on: Wavlink WL-WN579X3-C (firmware 231124)
# Platform: MIPS
# Exploit Type: Remote Stack-based Buffer Overflow
# CVSS: 8.8 (High)
# Description:
A stack-based buffer overflow exists in /cgi-bin/firewall.cgi when the "firewall" parameter is set to "UPNP".
The UpnpEnabled parameter is copied into a small 8-byte stack buffer (in function sub\_4019FC), but uci\_init writes ~40 bytes,
causing a 32+ byte overflow that corrupts the saved return address.
This vulnerability can be triggered remotely without authentication if the web interface is exposed,
leading to Denial of Service (device crash / reboot). With additional ROP engineering, remote code execution may be possible.
# References:
- https://github.com/Litengzheng/vul\_db/blob/main/WL-WN579X3-C/vul\_200/README.md
- https://vuldb.com/vuln/353891
- https://nvd.nist.gov/vuln/detail/CVE-2026-5004
# Usage:
python3 exploit.py <target\_ip>
# PoC Code:

**##### References:**

ttps://github.com/Litengzheng/vul\_db/blob/main/WL-WN579X3-C/vul\_200/README.md

https://vuldb.com/vuln/353891

https://nvd.nist.gov/vuln/detail/CVE-2026-5004

https://www.thehackerwire.com/wavlink-wl-wn579x3-c-upnp-handler-stack-based-buffer-overflow-cve-2026-5004/

[**See this note in RAW Version**](https://cxsecurity.com/ascii/WLB-2026030037)

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

Copyright **2026**, cxsecurity.com

|  |

Back to Top