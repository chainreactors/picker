---
title: OpenBSD sppp_pap_input: PAP authentication bypass
url: https://seclists.org/fulldisclosure/2026/Jun/15
source: Full Disclosure
date: 2026-06-21
fetch_date: 2026-06-22T07:16:59.901967
---

# OpenBSD sppp_pap_input: PAP authentication bypass

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
[By Date](date.html#15)
[![Next](/images/right-icon-16x16.png)](17)

[![Previous](/images/left-icon-16x16.png)](21)
[By Thread](index.html#15)
[![Next](/images/right-icon-16x16.png)](17)

![](/shared/images/nst-icons.svg#search)

# OpenBSD sppp\_pap\_input: PAP authentication bypass

---

*From*: shj <shahriyar () byteray co uk>
*Date*: Tue, 16 Jun 2026 21:27:44 +0200

---

```
------------------------------------------------------------------------
OpenBSD sppp_pap_input: PAP Authentication Bypass via Zero-Length bcmp
------------------------------------------------------------------------

Affected:  OpenBSD all versions through 7.6 (fixed in -current)
Vendor:    OpenBSD
Severity:  High
Reporter:  Argus
Date:      2026-06-16

1. SUMMARY
==========

The sppp_pap_input() function in sys/net/if_spppsubr.c uses the
attacker-controlled name_len and passwd_len fields from the incoming
PAP frame directly as the comparison length for bcmp() against
configured credentials.

When both fields are set to zero, bcmp() returns 0 unconditionally
(bcmp with length 0 always succeeds). The existing upper-bound guard
(> AUTHMAXLEN) allows zero through. As a result, a PAP Auth-Request
with name_len=0 and passwd_len=0 passes credential validation and
triggers a PAP_ACK, authenticating the peer without any knowledge of
the configured username or password.

A secondary kernel heap over-read exists via the same root cause:
supplying a name_len larger than the allocation of the stored
credential causes bcmp to read past the heap object.

2. AFFECTED VERSIONS
====================

The bcmp comparison pattern was introduced with the original sppp
code import on 1999-07-01 (commit bda3414e, "lmc driver; ported by
chris () dqc org"). The zero-length bypass has been exploitable since
that date.

In February 2009 (commit 9c2f3d605fc), auth credential fields were
changed from fixed-size struct arrays to dynamically allocated
malloc(strlen()+1), and the bounds check was changed to
> AUTHMAXLEN (256). This decoupled the allocation size from the
comparison bound, enabling the heap over-read.

Confirmed against OpenBSD 7.6 (amd64) in QEMU/KVM.

3. DETAILS
==========

Vulnerable code (sys/net/if_spppsubr.c, sppp_pap_input):

  if (name_len > AUTHMAXLEN ||
      passwd_len > AUTHMAXLEN ||
      bcmp(name, sp->hisauth.name, name_len) != 0 ||
      bcmp(passwd, sp->hisauth.secret, passwd_len) != 0) {
          /* authentication failed */

name_len and passwd_len are parsed directly from the PAP frame
payload. bcmp(a, b, 0) always returns 0. The > AUTHMAXLEN guard
rejects values above 255 but permits zero.

The CHAP handler in the same file already had the correct pattern
with an exact-length pre-check:

  if (name_len != strlen(sp->hisauth.name)
      || bcmp(name, sp->hisauth.name, name_len) != 0) {

The PAP handler never received the same treatment.

4. REACHABILITY
===============

Both bugs are reachable via the PPPoE data path:

  pppoe_data_input -> pppoeintr -> sppp_input -> sppp_pap_input

Precondition: the target system must be configured as a PAP
authenticator (e.g. ifconfig pppoe0 peerproto pap peername <x>
peerkey <y>). The attacker does not need to know any credentials.

5. IMPACT
=========

An attacker on the same network segment can authenticate to a PPPoE
interface without credentials, establishing a full network-layer
link (LCP -> PAP -> IPCP -> IP).

When OpenBSD acts as a PPPoE client with mutual authentication, a
rogue server in the same broadcast domain can exploit the bypass to
impersonate a legitimate server, causing OpenBSD to route traffic
through the attacker's endpoint.

6. PROOF OF CONCEPT
===================

A Python PoC acts as a PPPoE server, completes discovery and
LCP negotiation, then sends a PAP Auth-Request with name_len=0 and
passwd_len=0.

Result:

  PAP_ACK received with empty credentials
  VM accepted name_len=0, passwd_len=0 as valid auth.

  IPCP Config-Ack received - link is UP
  ICMP echo reply from 10.0.0.1

  FULL LINK ESTABLISHED

PoC and full technical report:
  https://blog.argus-systems.ai/blog/openbsd-pap-27-year-auth-bypass.html

7. FIX
======

Fixed in -current by mvs on 2026-06-14. The fix mirrors the CHAP
handler's exact-length pre-check:

  if (name_len != strlen(sp->hisauth.name) ||
      passwd_len != strlen(sp->hisauth.secret) ||
      bcmp(name, sp->hisauth.name, name_len) != 0 ||
      bcmp(passwd, sp->hisauth.secret, passwd_len) != 0) {

Fix commit:
https://github.com/openbsd/src/commit/076e2b1c1fc4ac0883a72d3544131ad5cee7adf8

8. TIMELINE
===========

  2026-06-12  Reported to security () openbsd org with PoC
  2026-06-14  Fix committed to -current

9. CREDIT
=========

Discovered and reported by Argus (https://byteray.co.uk/).

10. REFERENCES
==============

Advisory:
  https://pop.argus-systems.ai/advisory/adv-038.html

Blog post:
https://blog.argus-systems.ai/blog/openbsd-pap-27-year-auth-bypass.html

Proof of concept:
  https://pop.argus-systems.ai/attachments/poc-001-pap-bypass.py

_______________________________________________
Sent through the Full Disclosure mailing list
https://nmap.org/mailman/listinfo/fulldisclosure
Web Archives & RSS: https://seclists.org/fulldisclosure/
```

---

[![Previous](/images/left-icon-16x16.png)](21)
[By Date](date.html#15)
[![Next](/images/right-icon-16x16.png)](17)

[![Previous](/images/left-icon-16x16.png)](21)
[By Thread](index.html#15)
[![Next](/images/right-icon-16x16.png)](17)

### Current thread:

* **OpenBSD sppp\_pap\_input: PAP authentication bypass** *shj (Jun 20)*

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