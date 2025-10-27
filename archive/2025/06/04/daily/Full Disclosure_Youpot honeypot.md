---
title: Youpot honeypot
url: https://seclists.org/fulldisclosure/2025/Jun/0
source: Full Disclosure
date: 2025-06-04
fetch_date: 2025-10-06T22:56:37.617116
---

# Youpot honeypot

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

![Previous](/images/left-icon-16x16.png)
[By Date](date.html#0)
[![Next](/images/right-icon-16x16.png)](1)

![Previous](/images/left-icon-16x16.png)
[By Thread](index.html#0)
[![Next](/images/right-icon-16x16.png)](1)

![](/shared/images/nst-icons.svg#search)

# Youpot honeypot

---

*From*: Jacek Lipkowski via Fulldisclosure <fulldisclosure () seclists org>
*Date*: Mon, 2 Jun 2025 01:08:33 +0200 (CEST)

---

```
Hi,

I made a novel honeypot for worms called Youpot.
```

Normally a honeypot will try to implement whatever service it thinks the
attacker would like. For a high interaction or pure honeypot this is often
impossible, because of the thousands of possibilities. Even a simple
telnet server will have thousands of variants: different banners,
different shells, different default passwords, on different IoT devices
etc.

```

```

Youpot works around this by listening on all TCP ports, and connects to
the attacker IP on the same port he connected to us, and proxyies the
traffic back to him. No need to implement any service emulation, and yet
the worm gets exactly the service it wants. And it is on a real system
(attacker's system, but he doesn't know it), so this is a pure honeypot.

```
We can just sit back and enjoy the show as the attacker attacks himself.
```

TLS and SSH protocols are detected and further MiTM is executed against
it. Otherwise youpot is just a simple TCP proxy.

```

```

Also for people with a wierd sense of humor there is some support for
replacing parts of traffic with our own data :)

```
More info here:
https://github.com/sq5bpf/youpot
https://lipkowski.com/youpot/
```

This project will be presented today at the Confidence 2025 conference in
Cracow/Poland.

```
Have fun :)

Jacek

_______________________________________________
Sent through the Full Disclosure mailing list
https://nmap.org/mailman/listinfo/fulldisclosure
Web Archives & RSS: https://seclists.org/fulldisclosure/
```

---

![Previous](/images/left-icon-16x16.png)
[By Date](date.html#0)
[![Next](/images/right-icon-16x16.png)](1)

![Previous](/images/left-icon-16x16.png)
[By Thread](index.html#0)
[![Next](/images/right-icon-16x16.png)](1)

### Current thread:

* **Youpot honeypot** *Jacek Lipkowski via Fulldisclosure (Jun 03)*

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