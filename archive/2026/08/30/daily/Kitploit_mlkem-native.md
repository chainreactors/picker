---
title: mlkem-native
url: https://kitploit.com/en/tools/github/pq-code-package/mlkem-native
source: Kitploit
date: 2026-08-30
fetch_date: 2026-08-31T07:53:06.216258
---

# mlkem-native

[Skip to content](#main-content)

[![Kitploit](/_next/image?url=%2Flogo.png&w=64&q=75)KITPLOIT](/en)[Tools](/en/tools)[Blog](/en/blog)Categories

EN

[Submit](/en/submit)

[Tools](/en/tools)[Blog](/en/blog)Categories

[Submit](/en/submit)

EN

Hacking, PenTest, and Cybersecurity Tools for Your Security Arsenal!

Kitploit is a directory of hacking, cybersecurity, and pentesting tools. Discover the latest project updates to find vulnerabilities, analyze systems, automate testing, and strengthen your security.

·Analytics preferences·[Feeds](/en/feeds)·[Contact](/en/contact)·[Privacy](/en/privacy)·© 2026 Kitploit

Tool Directory

## Categories

[View all categories](/en/categories)

Loading categories

mlkem-native — Secure, fast, and portable C90 implementation of ML-KEM / FIPS 203 | Kitploit

[Tools](/en/tools)/![GitHub](/providers/github.png)GitHub/pq-code-package/mlkem-native

![](https://assets.kitploit.com/production/public/tools/53526/50116e5b529c28565ac8d2ee9b9499e7fa0f97187628ab9af3c97d71da963273-display-v1.webp)

[Embedded Systems Security](/en/categories/embedded-systems-security)[Static Analysis](/en/categories/static-analysis)[Cryptography](/en/categories/cryptography)[Hardware Security](/en/categories/hardware-security)

![GitHub](/providers/github.png)pq-code-package/mlkem-native

# mlkem-native

Secure, fast, and portable C90 implementation of ML-KEM / FIPS 203

[View Repository](https://github.com/pq-code-package/mlkem-native)

22365432 days ago![Reviewed by Kitploit](/_next/image?url=%2Fbadges%2Fkitploit_badge_reviewed_full.png&w=48&q=75)

### Most Popular

[View all →](/en/tools)

Discover the most used tools by our community.

Last 7 DaysLast 30 Days

Explore all tools

Browse our collection of tools

[View all tools →](/en/tools)

Share

[Website](https://pq-code-package.github.io/mlkem-native/dev/bench/)

# mlkem-native

![CI](https://github.com/pq-code-package/mlkem-native/actions/workflows/all.yml/badge.svg)
![Benchmarks](https://github.com/pq-code-package/mlkem-native/actions/workflows/bench.yml/badge.svg)
![C90](https://img.shields.io/badge/language-C90-blue.svg)

[![License: Apache](https://img.shields.io/badge/license-Apache--2.0-green.svg)](https://www.apache.org/licenses/LICENSE-2.0)
[![License: ISC](https://img.shields.io/badge/License-ISC-blue.svg)](https://opensource.org/licenses/ISC)
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)

mlkem-native is a secure, fast, and portable C90[1](#user-content-fn-c90) implementation of ML-KEM[2](#user-content-fn-fips203).
It is a fork of the ML-KEM reference implementation[3](#user-content-fn-ref).

All C code in [mlkem/src/\*](https://github.com/pq-code-package/mlkem-native/blob/HEAD/mlkem) and [mlkem/src/fips202/\*](https://github.com/pq-code-package/mlkem-native/blob/HEAD/mlkem/src/fips202) is proved memory-safe (no memory overflow) and type-safe (no integer overflow)
using CBMC[4](#user-content-fn-cbmc). All AArch64 and x86\_64 assembly is proved to be functionally correct,
memory-safe, and of secret-independent timing (constant-time), using HOL-Light[5](#user-content-fn-hol-light).

mlkem-native includes native backends for Arm (64-bit, Neon), Intel/AMD (64-bit, AVX2), RISC-V (64-bit, RVV), and POWER (ppc64le, VSX). See [benchmarks](https://pq-code-package.github.io/mlkem-native/dev/bench/) for performance data.

mlkem-native is supported by the [Post-Quantum Cryptography Alliance](https://pqca.org/) as part of the [Linux Foundation](https://linuxfoundation.org/).

## Quickstart for Ubuntu

root@kitploit:~

```
# Install base packages
sudo apt-get update
sudo apt-get install make gcc python3 git

# Clone mlkem-native
git clone https://github.com/pq-code-package/mlkem-native.git
cd mlkem-native

# Build and run tests
make build
make test

# The same using `tests`, a convenience wrapper around `make`
./scripts/tests all
# Show all options
./scripts/tests --help
```

See [BUILDING.md](https://github.com/pq-code-package/mlkem-native/blob/HEAD/BUILDING.md) for more information.

## Applications

mlkem-native is used in

* [libOQS](https://github.com/open-quantum-safe/liboqs/) of the Open Quantum Safe project since [0.13.0](https://github.com/open-quantum-safe/liboqs/releases/tag/0.13.0) (as the default ML-KEM implementation)
* AWS' Cryptography library [AWS-LC](https://github.com/aws/aws-lc/) since [v1.50.0](https://github.com/aws/aws-lc/releases/tag/v1.50.0)
* The [rustls](https://github.com/rustls/rustls) TLS library written in Rust since [0.23.28](https://github.com/rustls/rustls/releases/tag/v/0.23.28) (through AWS-LC as the default cryptography provider)
* [Pavona](https://github.com/pavona/pavona) - a library of modular, tapeout-proven, and secure-by-default open silicon blocks

## Formal Verification

All C code in [mlkem/src/\*](https://github.com/pq-code-package/mlkem-native/blob/HEAD/mlkem) and [mlkem/src/fips202/\*](https://github.com/pq-code-package/mlkem-native/blob/HEAD/mlkem/src/fips202) is proved memory-safe (no memory overflow) and type-safe (no integer overflow).
This uses the [C Bounded Model Checker (CBMC)](https://github.com/diffblue/cbmc) and builds on function contracts and loop invariant annotations
in the source code. See [proofs/cbmc](https://github.com/pq-code-package/mlkem-native/blob/HEAD/proofs/cbmc) for details.

All AArch64 and x86\_64 assembly is proved functionally correct, memory-safe, and to have secret-independent timing
(constant-time), at the object-code level. This uses the [HOL-Light](https://github.com/jrh13/hol-light) interactive theorem prover and the
[s2n-bignum](https://github.com/awslabs/s2n-bignum/) verification infrastructure (which includes models of the
relevant parts of the Arm and x86 architectures). See [proofs/hol\_light](https://github.com/pq-code-package/mlkem-native/blob/HEAD/proofs/hol_light) for details.

**NOTE:** Formal Verification is never absolute. See [SOUNDNESS.md](https://github.com/pq-code-package/mlkem-native/blob/HEAD/SOUNDNESS.md) for a detailed analysis of the scope, assumptions and risks of the formal verification
efforts around mlkem-native.

## Security

All AArch64 and x86\_64 assembly in mlkem-native is formally proved in [HOL Light](https://github.com/jrh13/hol-light) to be free of secret-dependent control flow,
memory access patterns, and variable-latency instructions, thwarting most timing side channels
(see [proofs/hol\_light](https://github.com/pq-code-package/mlkem-native/blob/HEAD/proofs/hol_light) for details). C code is hardened against
compiler-introduced timing side channels (such as KyberSlash[6](#user-content-fn-kyberslash) or clangover[7](#user-content-fn-clangover))
through suitable barriers and constant-time patterns.

Absence of secret-dependent branches, memory-access patterns and variable-latency instructions is also tested using `valgrind`
with various combinations of compilers and compilation options.

**Other attacks.** mlkem-native targets resistance against timing side-channels only. Other attack classes, such as power and electromagnetic side-channels, microarchitectural side-channels (e.g. speculative execution), or fault-injection attacks, are currently out of scope.

## Design

mlkem-native is split into a *frontend* and two *backends* for arithmetic and FIPS202 / SHA3. The frontend is
fixed, written in C, and covers all routines that are not critical to performance. The backends are flexible, take care of
performance-sensitive routines, and can be implemented in C or native code (assembly/intrinsics); see
[mlkem/src/native/api.h](https://github.com/pq-code-package/mlkem-native/blob/HEAD/mlkem/src/native/api.h) for the arithmetic backend and
[mlkem/src/fips202/native/api.h](https://github.com/pq-code-package/mlkem-native/blob/HEAD/mlkem/src/fips202/native/api.h) for the FIPS-202 backend.

mlkem-native currently offers the following backends:

* Default portable C backend
* 64-bit Arm backend (using Neon)
* 64-bit Intel...