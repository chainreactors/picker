---
title: liblcf v0.8.1 Integer Overflow in liblcf `ReadInt()` Leads to Out-of-Bounds Reads and Denial of Service
url: https://seclists.org/fulldisclosure/2025/Aug/9
source: Full Disclosure
date: 2025-08-20
fetch_date: 2025-10-07T00:51:10.268914
---

# liblcf v0.8.1 Integer Overflow in liblcf `ReadInt()` Leads to Out-of-Bounds Reads and Denial of Service

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

[![Previous](/images/left-icon-16x16.png)](8)
[By Date](date.html#9)
[![Next](/images/right-icon-16x16.png)](11)

[![Previous](/images/left-icon-16x16.png)](8)
[By Thread](index.html#9)
[![Next](/images/right-icon-16x16.png)](11)

![](/shared/images/nst-icons.svg#search)

# liblcf v0.8.1 Integer Overflow in liblcf `ReadInt()` Leads to Out-of-Bounds Reads and Denial of Service

---

*From*: Ron E <ronaldjedgerson () gmail com>
*Date*: Sun, 17 Aug 2025 22:16:39 -0400

---

```
A crafted RPG Maker save file (`.lsd`) can trigger an integer overflow in
liblcfâ€™s lcfstrings compressed integer decoding logic
(`LcfReader::ReadInt()`), resulting in an unbounded shift and accumulation
loop. The overflowed value is later used in buffer size allocations and
structure parsing, causing large memory access requests and parsing errors.

*Steps to Reproduce*

1. Use the attached `.lsd` file (see PoC section).

2. Run: `./lcfstrings poc_overflow.lsd`

3. Observe invalid reads such as:

   - `Read 4294967205 bytes!`

   - Multiple `Invalid Primitive` and `Corrupted Chunk` warnings

   - Crash or excessive memory consumption in affected builds

*Proof of Concept:*

A `.lsd` file with a malformed compressed integer containing 11 bytes of
`0xFF` followed by `0x7F` triggers the overflow. This causes the loop in
`ReadInt()` to shift left repeatedly and accumulate a 32-bit integer
overflow (e.g., `0xFFFFFFFF`), resulting in corrupted internal values.
_______________________________________________
Sent through the Full Disclosure mailing list
https://nmap.org/mailman/listinfo/fulldisclosure
Web Archives & RSS: https://seclists.org/fulldisclosure/
```

---

[![Previous](/images/left-icon-16x16.png)](8)
[By Date](date.html#9)
[![Next](/images/right-icon-16x16.png)](11)

[![Previous](/images/left-icon-16x16.png)](8)
[By Thread](index.html#9)
[![Next](/images/right-icon-16x16.png)](11)

### Current thread:

* **liblcf v0.8.1 Integer Overflow in liblcf `ReadInt()` Leads to Out-of-Bounds Reads and Denial of Service** *Ron E (Aug 18)*

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