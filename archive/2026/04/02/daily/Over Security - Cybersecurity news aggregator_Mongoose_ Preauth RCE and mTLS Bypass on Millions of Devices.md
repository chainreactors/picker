---
title: Mongoose: Preauth RCE and mTLS Bypass on Millions of Devices
url: https://www.evilsocket.net/2026/04/02/Mongoose-Preauth-Remote-Code-Execution-and-mTLS-Bypass/
source: Over Security - Cybersecurity news aggregator
date: 2026-04-02
fetch_date: 2026-04-03T04:29:08.691352
---

# Mongoose: Preauth RCE and mTLS Bypass on Millions of Devices

[![evilsocket](/images/glider.png)

evilsocket
Preoccupied with a single leaf, you won't see the tree. Preoccupied with a single tree... you'll miss the entire forest.](/)

[HOME](/)
[RSS](/atom.xml)

# Mongoose: Preauth RCE and mTLS Bypass on Millions of Devices

BY Simone Margaritelli
— 2 Apr 2026
— [rce](/tags/rce/), [exploit](/tags/exploit/), [responsible disclosure](/tags/responsible-disclosure/), [vulnerability research](/tags/vulnerability-research/), [cve](/tags/cve/), [tls](/tags/tls/), [embedded devices](/tags/embedded-devices/), [iot security](/tags/iot-security/), [security](/tags/security/), [iot](/tags/iot/), [mongoose](/tags/mongoose/), [cesanta](/tags/cesanta/), [embedded](/tags/embedded/), [mips](/tags/mips/), [mtls](/tags/mtls/), [mdns](/tags/mdns/), [buffer overflow](/tags/buffer-overflow/), [heap overflow](/tags/heap-overflow/), [stack overflow](/tags/stack-overflow/), [authentication bypass](/tags/authentication-bypass/), [industrial control](/tags/industrial-control/), [CVE-2026-5244](/tags/CVE-2026-5244/), [CVE-2026-5245](/tags/CVE-2026-5245/), [CVE-2026-5246](/tags/CVE-2026-5246/)

[Follow me on X](https://twitter.com/evilsocket)

![cesanta](/images/2026/mongoose/cesanta_logo.png)

So, [Mongoose](https://github.com/cesanta/mongoose). If you’ve never heard of it, you’ve almost certainly used a device that runs it. It’s a single-file, cross-platform embedded network library written in C by [Cesanta](https://cesanta.com/) that provides HTTP/HTTPS, WebSocket, MQTT, mDNS and more, designed specifically for embedded systems and IoT devices where something like OpenSSL would be way too heavy. Their own website claims deployment on **hundreds of millions of devices** by companies like Siemens, Schneider Electric, Broadcom, Bosch, Google, Samsung, Qualcomm and Caterpillar. They even claim it runs on the **International Space Station**. We’re talking everything from smart home gateways and IP cameras to industrial PLCs, SCADA systems and, apparently, space.

![mongoose web server](/images/2026/mongoose/iss_mongoose.png)

One of Mongoose’s key selling points is its **built-in TLS 1.3 implementation** (`MG_TLS_BUILTIN`). Instead of linking against OpenSSL or mbedTLS, you get TLS right out of the box, including mutual TLS (mTLS) for client certificate authentication. This is particularly appealing for embedded devices where every kilobyte of firmware matters and cross-compiling OpenSSL for some obscure MIPS or ARM SoC is a pain. Sounds great, right?

![one does not simply roll their own crypto](/images/2026/mongoose/one-does-not-simply.jpg)

During one of the usual weekend fun projects, I found three vulnerabilities in Mongoose v7.20, each independently exploitable: **complete bypass of mTLS authentication**, **preauth RCE as root** via a heap overflow in the client public key parsing logic, and **preauth RCE via a single UDP packet** through mDNS. No authentication required for any of them. Not that authentication can’t be bypassed anyway :D

## [#](#Disclosure-Timeline)Disclosure Timeline

* **2026-02-17** - Vulnerabilities reported, [as per project README, via email to `[email protected]`](https://github.com/cesanta/mongoose/blob/eefec28b50bd9b2f08efd2477d033907f27cd837/README.md?plain=1#L203) with full technical details, weaponized exploits and proposed fixes.
* **2026-02-26** - Created GitHub issue [#3453](https://github.com/cesanta/mongoose/issues/3453) to get any sort of ACK.
* **2026-02-26** - Maintainer response: *“Please do not discuss security stuff here. You will receive a response in due time.”* Issue closed as **“not planned.”**
* **2026-02-26** - Cesanta finally realizes they wrote the wrong email address in the project README, and the conversation actually starts …
* **2026-03-02** - VulDB is involved for coordination and CVE assignment.
* **2026-03-31** - CVE-2026-5244, CVE-2026-5245 and CVE-2026-5246 assigned.
* **2026-04-01** - Mongoose v7.21 is released, including the patches.
* **2026-04-02** - Public disclosure from yours truly

## [#](#Summary)Summary

* [CVE-2026-5246](https://vuldb.com/vuln/354827) | **mg\_tls\_verify\_cert\_signature()** returns success without checking the signature when the CA uses a P-384 key. Any client certificate from any CA is accepted. Complete mTLS bypass. (CVSS 5.6 Medium, CWE-295 Improper Certificate Validation)
* [CVE-2026-5244](https://vuldb.com/vuln/354825) | **mg\_tls\_recv\_cert()** copies an attacker-controlled RSA public key into a fixed 528-byte heap buffer with no bounds check. Heap overflow overwrites `mg_connection->fn` function pointer → shellcode execution as root. (CVSS 7.3 High, CWE-122 Heap-based Buffer Overflow)
* [CVE-2026-5245](https://vuldb.com/vuln/354826) | **handle\_mdns\_record()** packs four DNS records into a 282-byte stack buffer without bounds checking. A single UDP packet overflows the stack by 386 bytes, corrupting saved registers and the return address. On MIPS with executable stack, this is exploitable for preauth RCE. (CVSS 5.6 Medium, CWE-121 Stack-based Buffer Overflow)

All three affect Mongoose versions 7.0 through 7.20. Fixed in version 7.21.

### [#](#Impact)Impact

A remote unauthenticated attacker can:

* **Bypass mTLS authentication entirely** on any Mongoose server using a P-384 CA certificate, gaining unauthorized access to management interfaces on critical infrastructure.
* **Achieve remote code execution as root** during the TLS handshake, before any HTTP request is processed, via a heap buffer overflow triggered by a crafted client certificate.
* **Achieve remote code execution via mDNS** with a single 34-byte UDP packet on IoT gateways, industrial controllers, and embedded systems (when the mDNS TXT buffer is configured larger than default).

### [#](#Affected-Systems)Affected Systems

Mongoose is deployed on hundreds of millions of devices by companies including Siemens, Schneider Electric, Broadcom, Bosch, Google, Samsung, Qualcomm, and Caterpillar. Any device using `MG_TLS_BUILTIN` or mDNS is potentially affected:

* Industrial PLCs and SCADA gateways
* Smart home hubs and IP cameras
* Building automation controllers
* Medical devices
* Automotive infotainment systems
* Any embedded device running Mongoose 7.0-7.20

### [#](#Remediation)Remediation

* **Update to Mongoose 7.21** which contains fixes for all three vulnerabilities.
* If you can’t update, **switch from `MG_TLS_BUILTIN` to OpenSSL or mbedTLS** for your TLS implementation.
* If you’re using mDNS, **disable it** if you don’t need it.
* **Do not use P-384 CA certificates** with Mongoose’s built-in TLS on any version prior to 7.21.
* If running on embedded devices with no hardening (no ASLR, no PIE, executable heap - which is most of them), **treat this as critical priority**.

## [#](#Bug-1-“ignore-secp386-for-now”-mTLS-Authentication-Bypass-CVE-2026-5246)Bug 1: “ignore secp386 for now” - mTLS Authentication Bypass (CVE-2026-5246)

Let’s start with the fun one, the one that made me literally say “no way” out loud. Mutual TLS (mTLS) is the gold standard for device-to-device authentication in IoT deployments. Instead of passwords or API keys, both the server and the client present X.509 certificates signed by a trusted Certificate Authority. The server verifies the client’s certificate against its CA, and only if the signature checks out does the client get access.

In Mongoose’s built-in TLS implementation, this verification happens in `mg_tls_verify_cert_signature()`. Here’s the relevant code path from [`tls_builtin.c` line 1527](https://github.com/cesanta/mongoose/blob/eefec28b50bd9b2f08efd2477d033907f27cd837/src/tls_builtin.c#L1527):

|  |  |
| --- | --- |
| ``` 1 2 3 4 5 6 7 8 9 10 ``` | ``` if (issuer->pubkey.len == 64) {   // secp256r1 (P-256) verification - actually checks the signature   return mg_uecc_verify(...); } else if (issuer->pubkey.len == 96) {   MG_VERBOSE(("ignore secp386 for now"));  // <--- LMAO   return 1;                                 // <--- ALWAYS S...