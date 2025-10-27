---
title: Zillya Total Security 3.0.2367.0  Local Privilege Escalation
url: https://cxsecurity.com/issue/WLB-2023040004
source: CXSECURITY Database RSS Feed - CXSecurity.com
date: 2023-04-03
fetch_date: 2025-10-04T11:29:14.677911
---

# Zillya Total Security 3.0.2367.0  Local Privilege Escalation

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
|  |  | |  | | --- | | **Zillya Total Security 3.0.2367.0 Local Privilege Escalation** **2023.04.02**  Credit:  **[M. Akil Gündoğan](https://cxsecurity.com/author/M.%2BAkil%2BG%C3%BCndo%C4%9Fan/1/)**  Risk: **Medium**  Local: ****Yes****  Remote: **No**  CVE: **N/A**  CWE: **[CWE-264](https://cxsecurity.com/cwe/CWE-264 "Click to see CWE-264")** | |

# Exploit Title: Zillya Total Security 3.0.2367.0 - Local Privilege Escalation
# Date: 02.12.2022
# Author: M. Akil Gündoğan
# Contact: https://twitter.com/akilgundogan
# Vendor Homepage: https://zillya.com/
# Software Link: (https://download.zillya.com/ZTS3.exe) / (https://download.zillya.com/ZIS3.exe)
# Version: IS (3.0.2367.0) / TS (3.0.2368.0)
# Tested on: Windows 10 Professional x64
# PoC Video: https://youtu.be/vRCZR1kd89Q
Vulnerabiliy Description:
---------------------------------------
Zillya's processes run in SYSTEM privileges. The user with low privileges in the system can copy any file they want
to any location by using the quarantine module in Zillya. This is an example of AVGater vulnerabilities that are often
found in antivirus programs.
You can read the article about AVGater vulnerabilities here:
https://bogner.sh/2017/11/avgater-getting-local-admin-by-abusing-the-anti-virus-quarantine/
The vulnerability affects both "Zillya Total Security" and "Zillya Internet Security" products.
Step by step produce:
---------------------------------------
1 - Attackers create new folder and into malicious file. It can be a DLL or any file.
2 - Attacker waits for "Zillya Total Security" or "Zillya Internet Security" to quarantine him.
3 - The created folder is linked with the Google Symbolic Link Tools "Create Mount Point" tools to the folder that
the current user does not have write permission to.
You can find these tools here: https://github.com/googleprojectzero/symboliclink-testing-tools
4 - Restores the quarantined file. When checked, it is seen that the file has been moved to an unauthorized location.
This is evidence of escalation vulnerability. An attacker with an unauthorized user can write to directories that require
authorization. Using techniques such as DLL hijacking, it can gain access to SYSTEM privileges.
Advisories:
---------------------------------------
Developers should not allow unauthorized users to restore from quarantine unless necessary.
Also, it should be checked whether the target file has been copied to the original location. Unless necessary, users
should not be able to interfere with processes running with SYSTEM privileges. All processes on the user's side should
be run with normal privileges.
Disclosure Timeline:
---------------------------------------
13.11.2022 - Vulnerability reported via email but no response was given and the fix was not released.
02.12.2022 - Full disclosure.

[**See this note in RAW Version**](https://cxsecurity.com/ascii/WLB-2023040004)

[Tweet](https://twitter.com/share)

Vote for this issue:
 1
 0

100%

0%

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