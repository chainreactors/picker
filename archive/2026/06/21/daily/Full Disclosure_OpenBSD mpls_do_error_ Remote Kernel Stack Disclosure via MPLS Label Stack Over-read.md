---
title: OpenBSD mpls_do_error: Remote Kernel Stack Disclosure via MPLS Label Stack Over-read
url: https://seclists.org/fulldisclosure/2026/Jun/17
source: Full Disclosure
date: 2026-06-21
fetch_date: 2026-06-22T07:16:59.580368
---

# OpenBSD mpls_do_error: Remote Kernel Stack Disclosure via MPLS Label Stack Over-read

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
[By Date](date.html#17)
![Next](/images/right-icon-16x16.png)

[![Previous](/images/left-icon-16x16.png)](15)
[By Thread](index.html#17)
![Next](/images/right-icon-16x16.png)

![](/shared/images/nst-icons.svg#search)

# OpenBSD mpls\_do\_error: Remote Kernel Stack Disclosure via MPLS Label Stack Over-read

---

*From*: shj <shahriyar () byteray co uk>
*Date*: Fri, 19 Jun 2026 07:32:14 +0200

---

```
------------------------------------------------------------------------
```

OpenBSD mpls\_do\_error: Remote Kernel Stack Disclosure via MPLS Label
Stack Over-read

```
------------------------------------------------------------------------

Affected:  OpenBSD -current prior to 2026-06-18 (fixed in -current)
Vendor:    OpenBSD
Severity:  Medium
Reporter:  Argus Systems
Date:      2026-06-12
CVE:       CVE-2026-56099

1. SUMMARY
==========

The mpls_do_error() function in sys/netmpls/mpls_input.c parses an
incoming MPLS label stack into a fixed-size local array,
struct shim_hdr stack[MPLS_INKERNEL_LOOP_MAX] (16 entries). When the
parse loop completes without encountering the Bottom-of-Stack (BoS)
label, nstk reaches MPLS_INKERNEL_LOOP_MAX (16). Several subsequent
code paths then compute a copy length of (nstk + 1) * sizeof(*shim)
-- 17 entries -- and use it with icmp_do_exthdr(), M_PREPEND(), and
m_copyback() against the 16-entry stack object. This reads one
struct shim_hdr (4 bytes) past the end of the array, and that data is
reflected back to the sender inside the generated ICMP/MPLS error
response.

2. AFFECTED VERSIONS
====================

The (nstk + 1) length computations against the 16-entry stack[] array
were introduced with the ICMP/MPLS error path on 2010-09-13 (commit
201d6983add, "First shot at ICMP error handling inside an MPLS path.
Currently only TTL exceeded errors for IPv4 are handled."). The parse
loop was bounded by MPLS_INKERNEL_LOOP_MAX (16), but nothing rejected
a stack that ran to completion without a BoS bit, so nstk could reach
16 and the subsequent (nstk + 1) reads accessed stack[16].

Affected: OpenBSD -current prior to 2026-06-18 (mpls_input.c pre
v1.82).

3. DETAILS
==========

Vulnerable code (sys/netmpls/mpls_input.c, mpls_do_error):

  struct shim_hdr stack[MPLS_INKERNEL_LOOP_MAX];   /* 16 entries */
  ...
  for (nstk = 0; nstk < MPLS_INKERNEL_LOOP_MAX; nstk++) {
      ...
      stack[nstk] = *mtod(m, struct shim_hdr *);
      m_adj(m, sizeof(*shim));
      if (MPLS_BOS_ISSET(stack[nstk].shim_label))
          break;
  }
  /* no guard: with no BoS bit set, nstk == 16 here */

  shim = &stack[0];
  ...
  case IPVERSION:
      ...
      if (icmp_do_exthdr(m, ICMP_EXT_MPLS, 1, stack,
          (nstk + 1) * sizeof(*shim)))
          return (NULL);
      ...

MPLS_INKERNEL_LOOP_MAX is defined as 16 and sizeof(struct shim_hdr) is
4. With nstk == 16, each of these copies 17 * 4 = 68 bytes from a
64-byte stack[] object, reading stack[16] -- one struct shim_hdr (4
bytes) of adjacent kernel stack -- and including it in the response.

The same (nstk + 1) length is later used to prepend and m_copyback()
the stack back onto the reflected packet:

  M_PREPEND(m, (nstk + 1) * sizeof(*shim), M_NOWAIT);
  ...
  m_copyback(m, 0, (nstk + 1) * sizeof(*shim), stack, M_NOWAIT);

so the leaked entry also travels on the wire as the 17th MPLS shim
header of the returned frame.

4. REACHABILITY
===============

The path is reachable remotely via mpls_input() -> mpls_do_error() on
systems that have MPLS enabled on an interface. The trigger is a
crafted MPLS frame (EtherType 0x8847) carrying 16 labels with no BoS
bit set and an outermost label TTL of 1, so the TTL-exceeded error
path is taken:

  mpls_input  (ttl <= 1)
    -> mpls_do_error(m, ICMP_TIMXCEED, ICMP_TIMXCEED_INTRANS, 0)

The inner payload must be IPv4 so the IPVERSION branch is reached.

5. IMPACT
=========

Each crafted packet leaks 4 bytes of kernel stack memory adjacent to
the stack[] array. The leak is carried in the ICMP/MPLS extension
object of the error response reflected back to the sender, so an
attacker can harvest the leaked bytes.

6. PROOF OF CONCEPT
===================

A Python/Scapy PoC sends a 16-label MPLS frame with no BoS bit set
and an outermost label TTL of 1, then captures the reply. On a
vulnerable kernel the reply carries 17 MPLS shim headers on the wire;
the 17th (stack[16]) is the leaked kernel stack data.

PoC:
https://pop.argus-systems.ai/attachments/poc-008-mpls-stack-leak.py

7. FIX
======

Fixed in -current by mvs on 2026-06-18. The fix adds a guard that
drops a label stack which runs to completion without a BoS bit, so
nstk can no longer reach MPLS_INKERNEL_LOOP_MAX:

  if (nstk >= MPLS_INKERNEL_LOOP_MAX) {
      m_freem(m);
      return (NULL);
  }

Fix commit (mpls_input.c v1.82):
https://github.com/openbsd/src/commit/6a23123ec05f1eb29cfcaae0f3a468b2e1983cfd

8. TIMELINE
===========

  2026-06-12  Reported to security () openbsd org with PoC
  2026-06-18  Fix committed to -current

9. CREDIT
=========

Discovered and reported by Argus Systems (https://byteray.co.uk/).

10. REFERENCES
==============

Advisory:
  https://pop.argus-systems.ai/advisory/adv-040.html

Proof of concept:
https://pop.argus-systems.ai/attachments/poc-008-mpls-stack-leak.py

Fix commit:
https://github.com/openbsd/src/commit/6a23123ec05f1eb29cfcaae0f3a468b2e1983cfd

_______________________________________________
Sent through the Full Disclosure mailing list
https://nmap.org/mailman/listinfo/fulldisclosure
Web Archives & RSS: https://seclists.org/fulldisclosure/
```

---

[![Previous](/images/left-icon-16x16.png)](15)
[By Date](date.html#17)
![Next](/images/right-icon-16x16.png)

[![Previous](/images/left-icon-16x16.png)](15)
[By Thread](index.html#17)
![Next](/images/right-icon-16x16.png)

### Current thread:

* **OpenBSD mpls\_do\_error: Remote Kernel Stack Disclosure via MPLS Label Stack Over-read** *shj (Jun 20)*

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
[![](/shared/images/nst-icons.svg#facebook)](https://facebook.com/nmap "...