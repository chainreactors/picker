---
title: InfiniteWP Client: the NOSSL signing key has 31 bits of secret — recovered live in 291.9 seconds
url: https://seclists.org/fulldisclosure/2026/Nov/22
source: Full Disclosure
date: 2026-11-13
fetch_date: 2026-11-14T08:21:47.251866
---

# InfiniteWP Client: the NOSSL signing key has 31 bits of secret — recovered live in 291.9 seconds

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

[![Previous](/images/left-icon-16x16.png)](21)
[By Date](date.html#22)
[![Next](/images/right-icon-16x16.png)](34)

[![Previous](/images/left-icon-16x16.png)](21)
[By Thread](index.html#22)
[![Next](/images/right-icon-16x16.png)](34)

![](/shared/images/nst-icons.svg#search)

# InfiniteWP Client: the NOSSL signing key has 31 bits of secret — recovered live in 291.9 seconds

---

*From*: theknell--- via Fulldisclosure <fulldisclosure () seclists org>
*Date*: Fri, 06 Nov 2026 13:31:37 -0500

---

```
InfiniteWP Client 1.13.10 — a WordPress management plugin on roughly
200,000 installs — speaks to its management panel through two
authentication branches. The strong branch verifies an RSA
signature. The other, NOSSL, is selected by the enrolling panel
setting one request parameter, on hosts fully capable of RSA. Once
its key is stored, the selection is permanent and the RSA branch is
unreachable.

The stored key is generated as:

md5(base64_encode(panel_public_key) . rand(0, getrandmax()))

The public key is public. The secret is a single rand() result: at
most 2^31 values. The authentication value signs only the action
and message ID — parameters are never signed — and message-ID
ordering is enforced only on the auto_login path, so a captured
request replays with altered parameters.

Live proof, against our own instance only: from one captured
get_stats request and the panel's public key, the key was recovered
offline in 291.9 seconds (~7.36M candidates/sec), byte-identical to
the site-issued key. A forged maintain_site command signed with the
recovered key was accepted and wrote database options that had not
existed before. The key never rotates: recover it once, forge
forever.

Scope, stated plainly: every shipped copy carries the construction;
exploitation requires a NOSSL-enrolled site. The NOSSL-enrolled
share of the 200,000 installs is not externally measurable and is
not claimed here.

Paper: https://archive.org/details/knell-thirty-one-bits
Mirror: https://github.com/the-knell/Thirty-One-Bits
Key: 133883AB9F6EDE5B9BA6B82E27BEDAF0CE152F25 (knell)

Verify: gpg --import knell-public.asc, then
gpg --verify paper-infinitewp-FINAL-2026-11-04.md.asc

— knell

More, signed and timestamped: https://github.com/the-knell
_______________________________________________
Sent through the Full Disclosure mailing list
https://nmap.org/mailman/listinfo/fulldisclosure
Web Archives & RSS: https://seclists.org/fulldisclosure/
```

---

[![Previous](/images/left-icon-16x16.png)](21)
[By Date](date.html#22)
[![Next](/images/right-icon-16x16.png)](34)

[![Previous](/images/left-icon-16x16.png)](21)
[By Thread](index.html#22)
[![Next](/images/right-icon-16x16.png)](34)

### Current thread:

* **InfiniteWP Client: the NOSSL signing key has 31 bits of secret — recovered live in 291.9 seconds** *theknell--- via Fulldisclosure (Nov 12)*

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