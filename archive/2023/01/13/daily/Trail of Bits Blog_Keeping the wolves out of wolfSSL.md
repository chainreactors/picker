---
title: Keeping the wolves out of wolfSSL
url: https://blog.trailofbits.com/2023/01/12/wolfssl-vulnerabilities-tlspuffin-fuzzing-ssh/
source: Trail of Bits Blog
date: 2023-01-13
fetch_date: 2025-10-04T03:44:59.442182
---

# Keeping the wolves out of wolfSSL

[The Trail of Bits Blog](/ "The Trail of Bits Blog")

[![Trail of Bits Logo](/img/tob.png)](https://trailofbits.com "Trail of Bits")

# Keeping the wolves out of wolfSSL

Max Ammann

January 12, 2023

[cryptography](/categories/cryptography/), [fuzzing](/categories/fuzzing/), [internship-projects](/categories/internship-projects/), [vulnerability-disclosure](/categories/vulnerability-disclosure/)

Trail of Bits is publicly disclosing four vulnerabilities that affect wolfSSL: [CVE-2022-38152](https://www.cve.org/CVERecord?id=CVE-2022-38152), [CVE-2022-38153](https://www.cve.org/CVERecord?id=CVE-2022-38153), [CVE-2022-39173](https://www.cve.org/CVERecord?id=CVE-2022-39173), and [CVE-2022-42905](https://www.cve.org/CVERecord?id=CVE-2022-42905). The four issues, which have CVSS scores ranging from medium to critical, can all result in a denial of service (DoS). These vulnerabilities have been discovered automatically using the novel protocol fuzzer [tlspuffin](https://github.com/tlspuffin/tlspuffin). This blog post will explore these vulnerabilities, then provide an in-depth overview of the fuzzer.

tlspuffin is a fuzzer inspired by formal protocol verification. Initially developed as part of my internship at [LORIA, INRIA, France](https://www.loria.fr/en/), it is especially targeted against cryptographic protocols like TLS or SSH.

During my internship at Trail of Bits, we pushed protocol fuzzing even further by supporting a new protocol (SSH), adding more fuzzing targets, and (re)discovering vulnerabilities. This work represents a milestone in the development of the first [Dolev-Yao model](https://en.wikipedia.org/wiki/Dolev%E2%80%93Yao_model)-guided fuzzer. By supporting an additional protocol, we proved that our fuzzing approach is agnostic with respect to the protocol. Going forward, we aim to support other protocols such as QUIC, OpenVPN, and WireGuard.

## Targeting wolfSSL

During my internship at Trail of Bits, we added several versions of wolfSSL as fuzzing targets. The wolfSSL library was an ideal choice because it was affected by two authentication vulnerabilities that were discovered in early 2022 ([CVE-2022-25640](https://www.cve.org/CVERecord?id=CVE-2022-25640) and [CVE-2022-25638](https://www.cve.org/CVERecord?id=CVE-2022-25638)). That meant we could verify that tlspuffin works by using it to rediscover the known vulnerabilities.

As tlspuffin is written in Rust, we first had to write bindings to wolfSSL. While the bindings were being implemented, several bugs were discovered in the OpenSSL compatibility layer that have also been reported to the wolfSSL team. With the bindings ready, we were ready to let the fuzzer do its job: discovering weird states within wolfSSL.

## Discovered Vulnerabilities

During my internship, I discovered several vulnerabilities in wolfSSL, which can result in a denial of service (DoS).

* **DOSC:** [CVE-2022-38153](https://cve.mitre.org/cgi-bin/cvename.cgi?name=CVE-2022-38153) allows MitM actors or malicious servers to perform a DoS attack against TLS 1.2 clients by intercepting and modifying a TLS packet. This vulnerability affects wolfSSL 5.3.0.
* **DOSS:** [CVE-2022-38152](https://cve.mitre.org/cgi-bin/cvename.cgi?name=CVE-2022-38152) is a DoS vulnerability against wolfSSL servers that use the `wolfSSL_clear` function instead of the sequence `wolfSSL_free; wolfSSL_new`. Resuming a session causes the server to crash with a NULL-pointer dereference. This vulnerability affects wolfSSL 5.3.0 to 5.4.0.
* **BUF:** [CVE-2022-39173](https://www.cve.org/CVERecord?id=CVE-2022-39173) is caused by a buffer overflow and causes a DoS of wolfSSL servers. It is caused by pretending to resume a session, and sending duplicate cipher suites in the Client Hello. It might allow an attacker to gain RCE on certain architectures or targets; however, this has not yet been confirmed. Versions of wolfSSL before 5.5.1 are affected.
* **HEAP:** [CVE-2022-42905](https://www.cve.org/CVERecord?id=CVE-2022-42905) is caused by a buffer overread while parsing TLS record headers. Versions of wolfSSL before 5.5.2 are affected.

### “A few CVEs for wolfSSL, one giant leap for tlspuffin.”

The vulnerabilities mark a milestone for the fuzzer: They are the first vulnerabilities found using this tool that have a far-reaching impact. We can also confidently say that this vulnerability would not have been easy to find with classical bit-level fuzzers. It’s especially intriguing that on average, the fuzzer took less than one hour to discover a vulnerability and crash.

While preparing the fuzzing setup for wolfSSL, we also discovered a severe memory leak that was caused by misuse of the wolfSSL API. This issue was reported to the wolfSSL team, [changed their documentation](https://github.com/wolfSSL/wolfssl/pull/5483) to help users avoid the leak. Additionally, several other code-quality issues have been reported to wolfSSL, and their team fixed all of our findings within one week of disclosure. If a “best coordinated disclosure” award existed, the wolfSSL team would definitely win it.

The following sections will focus on two of the vulnerabilities because of their higher impact and expressive attack traces.

### **DOSC:** Denial of service against clients

In wolfSSL 5.3.0, MiTM attackers or malicious servers can crash TLS clients. The bug lives in the `AddSessionToCache` function, which is called when the client receives a new session ticket from the server.

Let’s assume that each bucket of the session cache of wolfSSL contains at least one entry. As soon as a new session ticket arrives, the client will reuse a previously stored cache entry to try to cache it in the session cache. Additionally, because the new session ticket is quite large at 700 bytes, it will be allocated on the heap using `XMALLOC`.

In the following example, `SESSION_TICKET_LEN` is 256:

```
if (ticLen > SESSION_TICKET_LEN) {
    ticBuff = (byte*)XMALLOC(ticLen, NULL,
            DYNAMIC_TYPE_SESSION_TICK);
    …
}
```

[ssl.c:13442](https://github.com/wolfSSL/wolfssl/blob/e722c15be860794179082a05d09e6a90dc77ccf0/src/ssl.c)

This allocation leads to the initialization of `cacheTicBuff`, as `ticBuff` is already initialized, `cacheSession->ticketLenAlloc` is 0, and `ticLen` is 700:

```
if (ticBuff != NULL && cacheSession->ticketLenAlloc < ticLen) {
    cacheTicBuff = cacheSession->ticket;
    …
}
```

[ssl.c:13500](https://github.com/wolfSSL/wolfssl/blob/e722c15be860794179082a05d09e6a90dc77ccf0/src/ssl.c)

The `cacheTicBuff` is set to the ticket of a previous session, `cacheSession->ticket`. The memory to which `cacheTicBuff` points is not allocated on the heap; in fact, `cacheTicBuff` points to `cacheSession->_staticTicket`. This is problematic because the `cacheTicBuff` is later freed if it is not null.

```
if (cacheTicBuff != NULL)
     XFREE(cacheTicBuff, NULL, DYNAMIC_TYPE_SESSION_TICK);
```

[ssl.c:13557](https://github.com/wolfSSL/wolfssl/blob/e722c15be860794179082a05d09e6a90dc77ccf0/src/ssl.c)

The process terminates by executing the `XFREE` function, as the passed pointer is not allocated on the heap.

Note that the ticket length in itself is not the cause of the crash. This vulnerability is quite different to [Heartbleed](https://heartbleed.com/), the buffer over-read vulnerability discovered in OpenSSL. With wolfSSL, a crash is caused not by overflowing buffers but by a logical bug.

### Finding weird states

The fuzzer discovered the vulnerability in about one hour. The fuzzer modified the `NewSessionTicket` (`new_message_ticket`) message by replacing an actual ticket with a large array of 700 bytes (`large_bytes_vec`). This mutation of an otherwise-sane trace leads to a call of `XFREE` on a non-allocated value. This eventually leads to a crash of the client that receives such a large ticket.

[![](/img/wpdump/bb5626a93f5689ac1228a6a3d3169522.png)](/img/wpdump/bb5626a93f5689ac1228a6a3d3169522.png)

Visualized exploit for DOSC ([CVE-2022-38153](https://www.cve.org...