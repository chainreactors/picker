---
title: wolfSSL 5.3.0: Denial-of-service
url: https://seclists.org/fulldisclosure/2023/Jan/8
source: Full Disclosure
date: 2023-01-21
fetch_date: 2025-10-04T04:31:19.303375
---

# wolfSSL 5.3.0: Denial-of-service

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

[![Previous](/images/left-icon-16x16.png)](7)
[By Date](date.html#8)
[![Next](/images/right-icon-16x16.png)](9)

[![Previous](/images/left-icon-16x16.png)](9)
[By Thread](index.html#8)
[![Next](/images/right-icon-16x16.png)](11)

![](/shared/images/nst-icons.svg#search)

# wolfSSL 5.3.0: Denial-of-service

---

*From*: Maximilian Ammann via Fulldisclosure <fulldisclosure () seclists org>
*Date*: Tue, 17 Jan 2023 12:12:15 +0100

---

```
# wolfSSL 5.3.0: Denial-of-service
==================================

## INFO
=======

The CVE project has assigned the id CVE-2022-38153 to this issue.

Severity: 5.9 MEDIUM
Affected version: 5.3.0
End of embargo: Ended August 30, 2022
Blog Post: https://blog.trailofbits.com/2023/01/12/wolfssl-vulnerabilities-tlspuffin-fuzzing-ssh/

## SUMMARY
==========

In wolfSSL 5.3.0 man-in-the-middle attackers or a malicious server can crash TLS
1.2 clients during a handshake. If an attacker injects a large ticket (above 256
bytes) into a NewSessionTicket message in a TLS 1.2 handshake, and the client
has a non-empty session cache, the session cache frees a pointer which points to
non-allocated memory, causing the client to crash with a “free(): invalid
pointer”. Note: It is likely that this is also exploitable in TLS 1.3 handshakes
between a client and a malicious server. With TLS 1.3 it is not possible to
exploit this as a man-in-the-middle. This bug was discovered using the novel
symbolic-model-guided fuzzer tlspuffin.

## DETAILS
==========

Line numbers below are valid for the wolfSSL Git tag v5.3.0-stable. The bug
exists in the AddSessionToCache function in line ssh.c:13405. The
denial-of-service bug is only exploitable if the --enable-session-ticket compile
flag is used and the cache row of the session cache has an existing entry. This
is a random process because the used cache row depends on the hash of the
session id. Approximately 30 cached sessions are required in order to reach the
bug reliably. To exploit the bug, an attacker can inject a NewSessionTicket
message into the handshake with a large ticket (for example 700 bytes). It must
be larger than SESSION_TICKET_LEN in order to trigger a memory allocation in
ssl.c:13442.

```
    /* Alloc Memory here to avoid syscalls during lock */
    if (ticLen > SESSION_TICKET_LEN) {
        ticBuff = (byte*)XMALLOC(ticLen, NULL,
                DYNAMIC_TYPE_SESSION_TICK);
        …
    }
```

Because of this allocation, the condition in line ssl.c:13500 is true, which
sets cacheTicBuff pointer to the ticket of some cached session.

```
    /* If we can re-use the existing buffer in cacheSession then we won't touch
     * ticBuff at all making it a very cheap malloc/free. The page on a modern
      OS will most likely not even be allocated to the process. /
    if (ticBuff != NULL && cacheSession->ticketLenAlloc < ticLen) {
        cacheTicBuff = cacheSession->ticket;
        …
    }
```

This ticket is not allocated but is equal to the _staticTicket buffer, if
previous session’s tickets are smaller than SESSION_TICKET_LEN. This means that
cacheTicBuff points now to the _staticTicket buffer which is part of struct
WOLFSSL_SESSION. During the execution of wolfSSL_DupSession, the cached session
gets overwritten by the new session.

```
    /* Copy data into the cache object */
    ret = wolfSSL_DupSession(addSession, cacheSession, 1) == WOLFSSL_FAILURE;
```

A XMEMCPY in wolfSSL_DupSession copies fields from the new session to the cached
session.

```
    XMEMCPY((byte*)output + copyOffset, (byte*)input + copyOffset,
            sizeof(WOLFSSL_SESSION) - copyOffset);
```

Unfortunately, cacheTicBuff still points to _staticTicket after the copy. In
line ssl.c:13557 cacheTicBuff is freed which causes the process to crash.

```
    if (cacheTicBuff != NULL)
        XFREE(cacheTicBuff, NULL, DYNAMIC_TYPE_SESSION_TICK);
```

## AFFECTED VERSIONS
====================

The bug does not exist in versions before wolfSSL 5.3.0. This bug is no longer
exploitable on the current master branch with Git reference 218ab7e and version
5.4.0. The bug is circumvented on clients by the if condition in line
ssl.c:13692 with Git commit b6b007d. It is unclear whether this change was
intended as it is unrelated to the commit message. It could potentially be
reverted in the future if client-side session caching is wanted.

If wolfSSL clients make calls to wolfSSL_get_session, then this bug is still
exploitable. The function wolfSSL_get_session also calls AddSessionToCache on
clients. We observed that no other function calls AddSessionToCache.

The vulnerable code is still reachable on wolfSSL 5.4.0 servers, but the bug is
not exploitable because TLS clients can not control the length of session
tickets.

## SUGGESTED REMEDIATION
========================

Short term, check if ticketLenAlloc is not zero before freeing cacheTicBuff.
This ensures that the cacheTicBuff is only freed if the cached session contains
an allocated ticket. Long term, simplify the session cache to prevent
cross-session logical validation. Furthermore, we recommend that the static and
global mutex-protected session cache should be stored in the SSL context.
Therefore, its lifetime would be bound to the lifetime of the SSL context. By
limiting its lifetime the exploitability of caching related bugs is reduced.
_______________________________________________
Sent through the Full Disclosure mailing list
https://nmap.org/mailman/listinfo/fulldisclosure
Web Archives & RSS: https://seclists.org/fulldisclosure/
```

---

[![Previous](/images/left-icon-16x16.png)](7)
[By Date](date.html#8)
[![Next](/images/right-icon-16x16.png)](9)

[![Previous](/images/left-icon-16x16.png)](9)
[By Thread](index.html#8)
[![Next](/images/right-icon-16x16.png)](11)

### Current thread:

* **wolfSSL 5.3.0: Denial-of-service** *Maximilian Ammann via Fulldisclosure (Jan 19)*

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
[![](/shared/images/nst-icons.svg#github)](http...