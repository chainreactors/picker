---
title: securesystemslib v1.5.1
url: https://kitploit.com/en/posts/github-secure-systems-lab-securesystemslib-v151
source: Kitploit
date: 2026-09-05
fetch_date: 2026-09-06T06:39:22.201759
---

# securesystemslib v1.5.1

[Skip to content](#main-content)

[![Kitploit](/_next/image?url=%2Flogo.png&w=64&q=75)KITPLOIT](/en)[Tools](/en/tools)[Blog](/en/blog)Categories

EN

[Submit](/en/submit)

[Tools](/en/tools)[Blog](/en/blog)Categories

[Submit](/en/submit)

EN

Hacking, PenTest, and Cybersecurity Tools for Your Security Arsenal!

[Back to updates](/en/updates)

![](https://assets.kitploit.com/production/public/tools/50923/5acc199004fe16434551f80f26f759a86e7cd540d9b955e507bc24db6c648354-display-v1.webp)

New releaseSep 5, 2026

# securesystemslib v1.5.1

Cryptographic and general-purpose routines for Secure Systems Lab projects at NYU

Share

# securesystemslib

[![CI](https://github.com/secure-systems-lab/securesystemslib/workflows/Run%20Securesystemslib%20tests/badge.svg)](https://github.com/secure-systems-lab/securesystemslib/actions?query=workflow%3A%22Run+Securesystemslib+tests%22+branch%3Amain)
[![Documentation Status](https://readthedocs.org/projects/python-securesystemslib/badge/?version=latest)](https://python-securesystemslib.readthedocs.io/en/latest/?badge=latest)

Securesystemslib is a cryptography interface for signing and verifying digital
signatures. It is developed for the [TUF](https://theupdateframework.io) and
[in-toto](https://in-toto.io) projects: the key and signature containers are
compatible with metadata formats from those projects.

Under the hood, Securesystemslib can use various digital signing systems
(e.g. [cryptography](https://pypi.org/project/cryptography/), PIV hardware keys
and multiple cloud-based key management systems).

## Installation

The default installation supports [pure-Python `ed25519` signature
verification](https://github.com/pyca/ed25519) only. To enable other schemes and
signature creation, `securesystemslib` can be installed with *extras*. See
[pyproject.toml](https://github.com/secure-systems-lab/securesystemslib/blob/main/pyproject.toml) for available *optional dependencies*.

root@kitploit:~

```
# Install with ed25519, RSA, ECDSA sign and verify support
pip install securesystemslib[crypto]
```

root@kitploit:~

```
# ...or with HSM (e.g. Yubikey) support
pip install securesystemslib[hsm]
```

## Usage

[python-securesystemslib.readthedocs.io](https://python-securesystemslib.readthedocs.io)

## Contact

* Questions and discussions:
  [`#securesystemslib-python`](https://cloud-native.slack.com/archives/C05PF3GA7AL)
  on [CNCF Slack](https://communityinviter.com/apps/cloud-native/cncf)
* Security issues: see [Security policy](https://github.com/secure-systems-lab/securesystemslib/blob/main/docs/SECURITY.md)
* Other issues and requests: [*Open a new
  issue*](https://github.com/secure-systems-lab/securesystemslib/issues/new)

## Contribute

See [Instructions for contributors](https://github.com/secure-systems-lab/securesystemslib/blob/main/docs/CONTRIBUTING.md).

## Legacy key migration

Use
[`migrate_keys`](https://github.com/secure-systems-lab/securesystemslib/blob/v0.31.0/docs/migrate_key.py)
script to convert key pairs generated with legacy `keys` or `interface` modules
to a consistent standard format, which is compatible with
[`CryptoSigner`](https://github.com/secure-systems-lab/securesystemslib/blob/main/docs/CRYPTO_SIGNER.md). The script requires
`securesystemslib~=0.31.0`.

[Read more](/en/tools/github/secure-systems-lab/securesystemslib?expand=1)

## Categories

[Cryptography](/en/categories/cryptography)[Hardware Security](/en/categories/hardware-security)[Supply Chain Security](/en/categories/supply-chain-security)[Authentication](/en/categories/authentication)

### Most Popular

[View all →](/en/tools)

Discover the most used tools by our community.

Last 7 DaysLast 30 Days

Explore all tools

Browse our collection of tools

[View all tools →](/en/tools)

Kitploit is a directory of hacking, cybersecurity, and pentesting tools. Discover the latest project updates to find vulnerabilities, analyze systems, automate testing, and strengthen your security.

·Analytics preferences·[Feeds](/en/feeds)·[Contact](/en/contact)·[Privacy](/en/privacy)·© 2026 Kitploit

Tool Directory

## Categories

[View all categories](/en/categories)

Loading categories