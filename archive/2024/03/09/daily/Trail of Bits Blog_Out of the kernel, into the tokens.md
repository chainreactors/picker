---
title: Out of the kernel, into the tokens
url: https://blog.trailofbits.com/2024/03/08/out-of-the-kernel-into-the-tokens/
source: Trail of Bits Blog
date: 2024-03-09
fetch_date: 2025-10-04T12:09:42.733433
---

# Out of the kernel, into the tokens

[The Trail of Bits Blog](/ "The Trail of Bits Blog")

[![Trail of Bits Logo](/img/tob.png)](https://trailofbits.com "Trail of Bits")

# Out of the kernel, into the tokens

Emilio López, Max Ammann

March 08, 2024

[application-security](/categories/application-security/), [linux](/categories/linux/), [vulnerability-disclosure](/categories/vulnerability-disclosure/)

We’re digging up the archives of vulnerabilities that Trail of Bits has reported over the years. This post shares the story of two such issues: a denial-of-service (DoS) vulnerability hidden in JSON Web Tokens (JWTs), and an oversight in the Linux kernel that could enable circumvention of critical kernel security mechanisms (KASLR).

### Unraveling a DoS vulnerability in JOSE libraries

JWT and JSON Object Signing and Encoding (JOSE) are expansive standards that describe the creation and use of encrypted and/or signed JSON-based tokens. While these standards are widely used and represent a significant improvement over previous solutions for identity claims, they are not without drawbacks, and have several well-known footguns, like [the JWT “none” signature algorithm](https://auth0.com/blog/critical-vulnerabilities-in-json-web-token-libraries/).

Our finding concerns an attack that was part of a lineup of new JWT attacks presented by Tom Tervoort at BlackHat USA 2023: [“Three New Attacks Against JSON Web Tokens.”](https://i.blackhat.com/BH-US-23/Presentations/US-23-Tervoort-Three-New-Attacks-Against-JSON-Web-Tokens.pdf) The “billion hashes attack”, which results in denial-of-service due to a lack of validation in JWT key encryption, caught our colleague Matt Schwager’s attention. Upon further examination, he discovered it applied to several more libraries in the Go and Rust ecosystems: go-jose, jose2go, square/go-jose, and josekit-rs.

These libraries all support [key encryption with PBES2](https://datatracker.ietf.org/doc/html/rfc7518#section-4.8), a feature meant to allow for password-based encryption of the Content Encryption Key (CEK) in [JSON Web Encryption (JWE)](https://datatracker.ietf.org/doc/html/rfc7516). A key is first derived from a password by using PBES2 schemes, which execute a number of PBKDF2 iterations. Then that key is used to encrypt and decrypt the token contents.

This wouldn’t normally be an issue, but unfortunately, the number of iterations is contained as part of the token, on the p2c header parameter, which an attacker can easily manipulate. Consider, for example, the token header shown below:

![](/img/wpdump/7ef769fd39cc683e28673b4faaa959b4.png)

Figure 1: A JWE token header indicating PBES2 key encryption with a large number of iterations

By using a very large iteration count in the p2c field, an attacker can cause a DoS on any application that attempts to process this token. Whoever receives and attempts to verify this token will first need to perform 2,147,483,647 PBKDF2 iterations to derive the CEK before they can even verify if the token is valid, costing significant amounts of compute time.

We reported the issue to the [go-jose](https://github.com/go-jose/go-jose/issues/64), [jose2go](https://github.com/dvsekhvalnov/jose2go/issues/31), and [josekit-rs](https://github.com/hidekatsu-izuno/josekit-rs/issues/29) library maintainers, and it has been fixed by limiting the maximum value usable for p2c in `go-jose/go-jose` on version 3.0.1 (commit [65351c27657d](https://github.com/go-jose/go-jose/commit/65351c27657d58960c2e6c9fbb2b00f818e50568)); on `dvsekhvalnov/jose2go` on version 1.6.0 (commits [a4584e9dd712](https://github.com/dvsekhvalnov/jose2go/commit/a4584e9dd7128608fedbc67892eba9697f0d5317) and [8e9e0d1c6b39](https://github.com/dvsekhvalnov/jose2go/commit/8e9e0d1c6b39ac448a6042ed1275efa70a81c7b7)); and on `hidekatsu-izuno/josekit-rs` on version 0.8.5 (commits [1f3278a33f0e](https://github.com/hidekatsu-izuno/josekit-rs/commit/1f3278a33f0e9ef938091538b4bbc4fcf6da07ee), [8b60bd0ea8ce](https://github.com/hidekatsu-izuno/josekit-rs/commit/8b60bd0ea8cea9ad2256a56ec20b809cbcbef0f2), and [7e448ce66c1c](https://github.com/hidekatsu-izuno/josekit-rs/commit/7e448ce66c1c5f02204212033ee686f3f5272351)). `square/go-jose` remains unfixed, as the library is deprecated, and users are encouraged to migrate to `go-jose/go-jose`.

Alternatively, the risk can also be mitigated by not relying purely on the token’s `alg` parameter. After all, if your application does not expect to receive a token using PBES2 or any lesser-used algorithm, there is no reason to try to process one. [jose2go](https://github.com/dvsekhvalnov/jose2go?tab=readme-ov-file#customizing-library-for-security) allows implementing opt-in stricter validation of `alg` and `enc` parameters today, and [go-jose’s next major version](https://github.com/go-jose/go-jose/commit/9b5800e95c2ab569ec52f9d41b37a8c07be5ea8e) will require passing a list of acceptable algorithms when processing a token, allowing developers to explicitly list a set of expected algorithms.

### KASLR bypass in privilege-less containers

Next is a vulnerability that has been fixed since 2020, but never got a CVE assigned by the Linux kernel maintainers. In the following paragraphs, we’ll go into the details of a previously unknown but fixed KASLR bypass.

Back in 2020, Trail of Bits engineer Dominik Czarnota (aka [disconnect3d](https://twitter.com/disconnect3d_pl)) discovered a vulnerability in the Linux kernel that could expose internal pointer addresses within unprivileged Docker containers, allowing a malicious actor to bypass Kernel Address Space Layout Randomization (KASLR) for [kernel modules](https://wiki.archlinux.org/title/Kernel_module).

KASLR is an important defense mechanism in operating systems, primarily used to deter exploit attempts. It is a security technique that randomizes the kernel memory address locations between reboots. On top of that, kernel addresses must be hidden from userspace; otherwise, the mitigation would make no sense, as such kernel address disclosure would effectively bypass the KASLR mitigation.

While there are places where kernel addresses are shown to userspace programs, on many systems they should be available only when the user has the `CAP_SYSLOG` Linux capability. (Capabilities split root user privileges so it is possible to be the root user, or a user with uid 0, while having a limited set of privileges.) In particular, the [manual page](https://man7.org/linux/man-pages/man7/capabilities.7.html) for the `CAP_SYSLOG` capability reads: “View kernel addresses exposed via /proc and other interfaces when `/proc/sys/kernel/kptr_restrict` has the value 1.” This means that only processes that are executed with the capability `CAP_SYSLOG` should be able to read kernel addresses.

However, Dominik discovered that this was not the case from within a Docker container where processes that are run from the root user without `CAP_SYSLOG` were able to observe kernel addresses. By default, Docker containers are [unprivileged](https://docs.docker.com/engine/reference/run/#runtime-privilege-and-linux-capabilities), which means that root users are restricted in what they can do (e.g., they cannot perform actions that require `CAP_SYSLOG`). This can also be demonstrated without Docker by using the capsh tool run from the root user to remove the `CAP_SYSLOG` capability:

![](/img/wpdump/5bf03009e9bce37522709d0e5fa7a6a4.png)

The underlying cause of the issue was that the credentials were checked incorrectly. The sysctl toggle `kernel.kptr_restrict` indicates whether restrictions are placed on exposing kernel addresses: the value “2” means that the addresses are always hidden; “1” means that they are shown only if the user has `CAP_SYSLOG`; and “0” means that they are always shown. Instead of ensuring that the user had the `CAP_SYSLOG` capability before showing the addresses, only the value of kptr\_restrict was being considered to decide whether to show or hide the addresses. The addresses were always exposed if `kpt...