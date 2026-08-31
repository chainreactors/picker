---
title: liboqs
url: https://kitploit.com/en/tools/github/open-quantum-safe/liboqs
source: Kitploit
date: 2026-08-30
fetch_date: 2026-08-31T07:53:04.585086
---

# liboqs

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

liboqs — C library for prototyping and experimenting with quantum-resistant cryptography | Kitploit

[Tools](/en/tools)/![GitHub](/providers/github.png)GitHub/open-quantum-safe/liboqs

![](https://assets.kitploit.com/production/public/tools/53525/8f55e877443936bb16b04ead56c9790a9baba0c15c3928b68ea8080a43c6f77e-display-v1.webp)

[Encryption/Decryption Tools](/en/categories/encryption-decryption-tools)[Cryptography](/en/categories/cryptography)[Utilities & Frameworks](/en/categories/utilities-frameworks)

![GitHub](/providers/github.png)open-quantum-safe/liboqs

# liboqs

C library for prototyping and experimenting with quantum-resistant cryptography

[View Repository](https://github.com/open-quantum-safe/liboqs)[Website](https://openquantumsafe.org/)

3.0k765444 days ago![Reviewed by Kitploit](/_next/image?url=%2Fbadges%2Fkitploit_badge_reviewed_full.png&w=48&q=75)

### Most Popular

[View all →](/en/tools)

Discover the most used tools by our community.

Last 7 DaysLast 30 Days

Explore all tools

Browse our collection of tools

[View all tools →](/en/tools)

Share

# liboqs

[![Main Branch Tests](https://github.com/open-quantum-safe/liboqs/actions/workflows/commit-to-main.yml/badge.svg)](https://github.com/open-quantum-safe/liboqs/actions/workflows/commit-to-main.yml)
[![Weekly Tests](https://github.com/open-quantum-safe/liboqs/actions/workflows/weekly.yml/badge.svg)](https://github.com/open-quantum-safe/liboqs/actions/workflows/weekly.yml)
[![Coverage Status](https://coveralls.io/repos/github/open-quantum-safe/liboqs/badge.svg?branch=main)](https://coveralls.io/github/open-quantum-safe/liboqs?branch=main)

liboqs is an open source C library for quantum-safe cryptographic algorithms.

* [liboqs](#liboqs)
  + [Overview](#overview)
  + [Status](#status)
    - [Supported Algorithms](#supported-algorithms)
      * [Key encapsulation mechanisms](#key-encapsulation-mechanisms)
      * [Signature schemes](#signature-schemes)
      * [Stateful signature schemes](#stateful-signature-schemes)
    - [Limitations and Security](#limitations-and-security)
      * [Platform limitations](#platform-limitations)
      * [Support limitations](#support-limitations)
  + [Quickstart](#quickstart)
    - [Linux and Mac](#linux-and-mac)
    - [Windows](#windows)
    - [Cross compilation](#cross-compilation)
  + [Documentation](#documentation)
  + [Contributing](#contributing)
  + [License](#license)
  + [Acknowledgements](#acknowledgements)

## Overview

liboqs provides:

* a collection of open source implementations of quantum-safe key encapsulation mechanisms (KEMs) and digital signature algorithms; the full list can be found [below](#supported-algorithms)
* a common API for these algorithms
* a test harness and benchmarking routines

liboqs is part of the **Open Quantum Safe (OQS)** project, which aims to develop and integrate into applications quantum-safe cryptography to facilitate deployment and testing in real world contexts. In particular, OQS provides prototype integrations of liboqs into protocols like TLS, X.509, and S/MIME, through our [OpenSSL 3 Provider](https://github.com/open-quantum-safe/oqs-provider) and we provide a variety of other [post-quantum-enabled demos](https://github.com/open-quantum-safe/oqs-demos).

The OQS project is supported by the [Post-Quantum Cryptography Alliance](https://pqca.org/) as part of the [Linux Foundation](https://linuxfoundation.org/). More information about the Open Quantum Safe project can be found at [openquantumsafe.org](https://openquantumsafe.org/).

OQS is running a survey to better understand our community. We would like to hear from organizations and individuals about their interest in and use of the Open Quantum Safe project. Please take a few minutes to fill out the survey: <https://linuxfoundation.surveymonkey.com/r/oqssurvey>

## Status

### Supported Algorithms

The table below summarizes every algorithm family currently integrated into liboqs. For per-variant detail (including NIST level, constant-time status, formal verification, and available optimizations), see [ALGORITHMS.md](https://github.com/open-quantum-safe/liboqs/blob/main/ALGORITHMS.md); for upstream sources and advisories, see the per-algorithm pages under [docs/algorithms](https://github.com/open-quantum-safe/liboqs/tree/main/docs/algorithms).

Names of algorithms standardized by NIST — [`ML-KEM`](https://csrc.nist.gov/pubs/fips/203/final), [`ML-DSA`](https://csrc.nist.gov/pubs/fips/204/final), and [`SLH-DSA`](https://csrc.nist.gov/pubs/fips/205/final) — are stable; if NIST changes the implementation details, `liboqs` will adjust so that users are protected from such changes. All other names are subject to change. Which algorithms are built can be controlled via [`OQS_ALGS_ENABLED`](https://github.com/open-quantum-safe/liboqs/blob/HEAD/CONFIGURE.md#oQS_ALGS_ENABLED); by default, `liboqs` is built supporting every algorithm in the table, including experimental ones.

#### Key encapsulation mechanisms

#### Signature schemes

#### Stateful signature schemes

### Limitations and Security

While at the time of this writing there are no vulnerabilities known in any of the quantum-safe algorithms used in this library, caution is advised when deploying quantum-safe algorithms as most of the algorithms and software have not been subject to the same degree of scrutiny as for currently deployed algorithms. Particular attention should be paid to guidance provided by the standards community, especially from the NIST [Post-Quantum Cryptography Standardization](https://csrc.nist.gov/Projects/Post-Quantum-Cryptography/Post-Quantum-Cryptography-Standardization) project. As research advances, the supported algorithms may see rapid changes in their security, and may even prove insecure against both classical and quantum computers. Moreover, note that the `sntrup761` is only included for interop testing.

liboqs does not intend to "pick winners": algorithm support is informed by the NIST PQC standardization project. We strongly recommend that applications and protocols rely on the outcomes of this effort when deploying post-quantum cryptography.

We realize some parties may want to deploy quantum-safe cryptography prior to the conclusion of the NIST PQC standardization project. We strongly recommend such attempts make use of so-called **hybrid cryptography**, in which quantum-safe public-key algorithms are used alongside traditional public key algorithms (like RSA or elliptic curves) so that the solution is at least no less secure than existing traditional cryptography.

**WE DO NOT CURRENTLY RECOMMEND RELYING ON THIS LIBRARY IN A PRODUCTION ENVIRONMENT OR TO PROTECT ANY SENSITIVE DATA.** This library is meant to help with research and prototyping. While we make a best-effort approach to avoid security bugs, this library has not received the level of auditing and analysis that would be necessary to rely on it for high security use.

Please see [SECURITY.md](https://github.com/open-quantum-safe/liboqs/blob/HEAD/SECURITY.md#security-policy) for details on how to report a vulnerability and the OQS vulnerability response process.

#### Platform limitations

In order to optimize support effort,

* not all algorithms are equally well supported on all platforms. In case of ques...