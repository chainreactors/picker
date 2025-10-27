---
title: wolfSSL before 5.5.0: Denial-of-service with session resumption
url: https://seclists.org/fulldisclosure/2023/Jan/7
source: Full Disclosure
date: 2023-01-21
fetch_date: 2025-10-04T04:31:17.885906
---

# wolfSSL before 5.5.0: Denial-of-service with session resumption

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

[![Previous](/images/left-icon-16x16.png)](6)
[By Date](date.html#7)
[![Next](/images/right-icon-16x16.png)](8)

[![Previous](/images/left-icon-16x16.png)](6)
[By Thread](index.html#7)
[![Next](/images/right-icon-16x16.png)](9)

![](/shared/images/nst-icons.svg#search)

# wolfSSL before 5.5.0: Denial-of-service with session resumption

---

*From*: Maximilian Ammann via Fulldisclosure <fulldisclosure () seclists org>
*Date*: Tue, 17 Jan 2023 12:10:24 +0100

---

```
# wolfSSL before 5.5.0: Denial-of-service with session resumption
=================================================================

## INFO
=======

The CVE project has assigned the id CVE-2022-38152 to this issue.

Severity: 7.5 HIGH
Affected version: before 5.5.0
End of embargo: Ended August 30, 2022

## SUMMARY
==========

When a TLS 1.3 client connects to a wolfSSL server and SSL_clear is called on
its session, the server crashes with a segmentation fault. The bug occurs after
a client performs a handshake against a wolfSSL server and then closes the
connection. If the server reuses the previous session structure (struct WOLFSSL)
by calling wolfSSL_clear(WOLFSSL* ssl) on it, the next received Client Hello,
which resumes the previous session, crashes the server. Note, that this bug only
exists in resumed handshakes using TLS session resumption. This bug was
discovered using the novel symbolic-model-guided fuzzer tlspuffin.

## DETAILS
==========

Line numbers below are valid for the wolfSSL Git tag v5.4.0-stable. The
vulnerability is exploitable with default compilation flags. If the
 --enable-postauth flag is used, then this bug is no longer exploitable. When
creating a new TLS session (represented by a struct WOLFSSL), a struct called
arrays is allocated in internal.c:6652.

```
int InitSSL(WOLFSSL* ssl, WOLFSSL_CTX* ctx, int writeDup)
{
    ...
    ssl->arrays = (Arrays*)XMALLOC(sizeof(Arrays), ssl->heap,
DYNAMIC_TYPE_ARRAYS);
    ...
}
```

Note that this function is only called when creating a new session structure
using wolfSSL_new. After a handshake is done, resources related to it are freed
by default using the FreeHandshakeResources function in line ssl.c:3735. This
frees the memory behind ssl->arrays and sets the pointer to NULL.

```
void FreeHandshakeResources(WOLFSSL* ssl)
{
    ...
    if (!ssl->options.tls1_3)
        FreeArrays(ssl)
    ...
}

void FreeArrays(WOLFSSL* ssl)
{
...
    ssl->arrays = NULL;
}
```

If the compile flag --enable-postauth is not set, the variable options.tls1_3 is
false, and therefore the arrays are freed. If --enable-postauth is set, then the
arrays are not freed. The above code is executed during the handshake of a fresh
session. Users of wolfSSL might not allocate a new session by using
wolfSSL_new(), but reuse a previous struct WOLFSSL. This can be done by calling
wolfSSL_clear(WOLFSSL* ssl) on the previous session and reusing the struct. The
next abbreviated handshake, which resumes the previous connection, will now
cause a segmentation fault in tls13.c:5296.  The segmentation fault occurs
because the arrays pointer still points to NULL as InitSSL is not called before
the Client Hello is handled.

## AFFECTED VERSIONS
====================

wolfSSL 5.3.0 and 5.4.0 are affected The server needs to handle sessions in a
non-default way by using wolfSSL_clear

## SUGGESTED REMEDIATION
========================

After a session has been cleared and is reused for the next client, it should be
reinitialized.
_______________________________________________
Sent through the Full Disclosure mailing list
https://nmap.org/mailman/listinfo/fulldisclosure
Web Archives & RSS: https://seclists.org/fulldisclosure/
```

---

[![Previous](/images/left-icon-16x16.png)](6)
[By Date](date.html#7)
[![Next](/images/right-icon-16x16.png)](8)

[![Previous](/images/left-icon-16x16.png)](6)
[By Thread](index.html#7)
[![Next](/images/right-icon-16x16.png)](9)

### Current thread:

* **wolfSSL before 5.5.0: Denial-of-service with session resumption** *Maximilian Ammann via Fulldisclosure (Jan 19)*
  + <Possible follow-ups>
  + [wolfSSL before 5.5.0: Denial-of-service with session resumption](9) *Maximilian Ammann via Fulldisclosure (Jan 19)*

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