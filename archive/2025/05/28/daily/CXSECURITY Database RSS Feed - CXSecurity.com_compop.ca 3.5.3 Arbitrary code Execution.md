---
title: compop.ca 3.5.3 Arbitrary code Execution
url: https://cxsecurity.com/issue/WLB-2025050051
source: CXSECURITY Database RSS Feed - CXSecurity.com
date: 2025-05-28
fetch_date: 2025-10-06T22:25:11.926371
---

# compop.ca 3.5.3 Arbitrary code Execution

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
|  |  | |  | | --- | | **compop.ca 3.5.3 Arbitrary code Execution** **2025.05.27**  Credit:  **[dmlino](https://cxsecurity.com/author/dmlino/1/)**  Risk: **Medium**  Local: **No**  Remote: ****Yes****  CVE: **[CVE-2024-48445](https://cxsecurity.com/cveshow/CVE-2024-48445/ "Click to see CVE-2024-48445")**  CWE: **N/A**  **[**Dork:** Terms of Use inurl:compop.vip](https://cxsecurity.com/dorks/)** | |

# Exploit Title: compop.ca 3.5.3 - Arbitrary code Execution
# Google Dork: Terms of Use inurl:compop.vip
# Date: 22/12/2024
# Exploit Author: dmlino
# Vendor Homepage: https://www.compop.ca/
# Version: 3.5.3
# CVE : CVE-2024-48445
The restaurant management system implements authentication using a Unix
timestamp parameter ("ts") in the URL. This implementation is vulnerable to
manipulation as it relies solely on time-based validation without proper
authentication mechanisms.
Technical Details:
The application uses a URL parameter "ts" which accepts a Unix timestamp
value.
Steps:
1. Find a vulnerable restaurant.
2. Get the current time in the UNIX format:
Linux: $date +%s
Windows Powershell: [int](Get-Date -UFormat %s -Millisecond 0)
3. Replace parameter in url with the new value

[**See this note in RAW Version**](https://cxsecurity.com/ascii/WLB-2025050051)

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