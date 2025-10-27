---
title: Announcing a stable release of sigstore-python
url: https://blog.trailofbits.com/2023/01/13/sigstore-python/
source: Trail of Bits Blog
date: 2023-01-14
fetch_date: 2025-10-04T03:53:00.644047
---

# Announcing a stable release of sigstore-python

[The Trail of Bits Blog](/ "The Trail of Bits Blog")

[![Trail of Bits Logo](/img/tob.png)](https://trailofbits.com "Trail of Bits")

# Announcing a stable release of sigstore-python

[William Woodruff](https://infosec.exchange/%40yossarian)

January 13, 2023

[open-source](/categories/open-source/), [supply-chain](/categories/supply-chain/), [ecosystem-security](/categories/ecosystem-security/), [engineering-practice](/categories/engineering-practice/), [cryptography](/categories/cryptography/)

*Read [the official announcement](https://blog.sigstore.dev/announcing-the-1-0-release-of-sigstore-python-4f5d718b468d) on the Sigstore blog as well!*

Trail of Bits is thrilled to announce the [first stable release](https://github.com/sigstore/sigstore-python/releases/tag/v1.0.0) of [sigstore-python](https://github.com/sigstore/sigstore-python), a client implementation of [Sigstore](https://www.sigstore.dev/) that we’ve been developing for nearly a year! This work has been graciously funded by Google’s Open Source Security Team (GOSST), who we’ve also worked with to develop [`pip-audit`](https://github.com/pypa/pip-audit) and its [associated GitHub Actions workflow](https://github.com/pypa/gh-action-pip-audit).

If you aren’t already familiar with Sigstore, we’ve [written an explainer](https://blog.trailofbits.com/2022/11/08/sigstore-code-signing-verification-software-supply-chain/), including an explanation of *what* Sigstore is, *how* you can use it on your own projects, and how tools like sigstore-python fit into the overall codesigning ecosystem.

If you want to get started, it’s a single `pip install` away:

```
$ echo 'hello sigstore' > hello.txt
$ python -m pip install sigstore
$ sigstore sign hello.txt
$ sigstore verify identity hello.txt \
    --cert-identity 'foo@example.com' \
    --cert-oidc-issuer 'https://example.com'
```

## A usable, reference-quality Sigstore client implementation

Our goals with sigstore-python are two-fold:

* **Usability:** sigstore-python should provide an **extremely intuitive** CLI and API, with 100 percent documentation coverage and practical examples for both.
* **Reference-quality:** sigstore-python is just one of many Sigstore clients being developed, including for ecosystems like [Go](https://github.com/sigstore/sigstore-go), [Ruby](https://github.com/sigstore/sigstore-ruby), [Java](https://github.com/sigstore/sigstore-java), [Rust](https://github.com/sigstore/sigstore-rs), and [JavaScript](https://github.com/sigstore/sigstore-js/). We’re not the oldest implementation, but we’re aiming to be one of the **most authoritative** in terms of succinctly and correctly implementing the intricacies of Sigstore’s security model.

We believe we’ve achieved both of these goals with this release. The rest of this post will show off demonstrate how we did so!

## Usability: sigstore-python is for everybody

### The sigstore CLI

One of the Sigstore project’s mottos is “[Software Signing for Everybody](https://dl.acm.org/doi/10.1145/3548606.3560596),” and we want to stay true to that with sigstore-python. To that end, we’ve designed a public Python API and `sigstore CLI` that abstract the murkier cryptographic bits away, leaving the two primitives that nearly every developer is already familiar with: signing and verifying.

To get started, we can install sigstore-python from PyPI, where it’s available as sigstore:

```
$ python -m pip install sigstore
$ sigstore --version
sigstore 1.0.0
```

From there, we can create an input to sign, and use `sigstore sign` to perform the actual signing operation:

```
$ echo "hello, i'm signing this!" > hello.txt
$ sigstore sign hello.txt

Waiting for browser interaction...
Using ephemeral certificate:
-----BEGIN CERTIFICATE-----
MIICwDCCAkagAwIBAgIUOZ3vPindiCHATxvCRQk/TC5WAd0wCgYIKoZIzj0EAwMw
NzEVMBMGA1UEChMMc2lnc3RvcmUuZGV2MR4wHAYDVQQDExVzaWdzdG9yZS1pbnRl
cm1lZGlhdGUwHhcNMjMwMTEwMTkzNDI5WhcNMjMwMTEwMTk0NDI5WjAAMHYwEAYH
KoZIzj0CAQYFK4EEACIDYgAETb8dcUgXs31y6tjgsVy8KwfMEzVvhUVs7jlzcwkN
MLICjVvblYtWfFReYMEN8rM8mfglyAwcW+qY/I3klMnMcf/bna/yazzP7Mnnh1g1
dzlOXh14C9iZMDPIV0KHH5u2o4IBSDCCAUQwDgYDVR0PAQH/BAQDAgeAMBMGA1Ud
JQQMMAoGCCsGAQUFBwMDMB0GA1UdDgQWBBQdX9zi1TPEHw2uAkqaCE2ecWMLTDAf
BgNVHSMEGDAWgBTf0+nPViQRlvmo2OkoVaLGLhhkPzAjBgNVHREBAf8EGTAXgRV3
aWxsaWFtQHlvc3Nhcmlhbi5uZXQwLAYKKwYBBAGDvzABAQQeaHR0cHM6Ly9naXRo
dWIuY29tL2xvZ2luL29hdXRoMIGJBgorBgEEAdZ5AgQCBHsEeQB3AHUA3T0wasbH
ETJjGR4cmWc3AqJKXrjePK3/h4pygC8p7o4AAAGFnS1KGwAABAMARjBEAiAns85i
YPmlq9RWfJOUwCRN4y5Lwvk3/Y1cWB9wNW4XMwIgBRfib3YbotTgGpB16F/5uf7r
mO2Jc7e0yElimghFFmkwCgYIKoZIzj0EAwMDaAAwZQIxAOh0Ob8Mi2lENgRNjMRe
L8r8rBoVRSi8BzJHcKAe+eTwLsjvsdryJ0yKg5HVHc2erQIwNpdUXD71OPqs3QQ4
Ka+Q2Pjcs+GV5TvaecGzJuQGbm2J5ZW5raPJrXngEGUldt0U
-----END CERTIFICATE-----

Transparency log entry created at index: 10892071
Signature written to hello.txt.sig
Certificate written to hello.txt.crt
Rekor bundle written to hello.txt.rekor
```

On your desktop this will produce an [OAuth2](https://oauth.net/2/) flow that prompts you for authentication, while on [supported CI providers](https://github.com/sigstore/sigstore-python#signing-with-ambient-credentials) it’ll intelligently select an ambient OpenID Connect identity!

[![](/img/wpdump/124dd0d6eb1e02d5fb79e080d5be7fe4.png)](/img/wpdump/124dd0d6eb1e02d5fb79e080d5be7fe4.png)

This will produce three outputs:

* `hello.txt.sig`: the signature for `hello.txt` itself
* `hello.txt.crt`: a certificate for the signature, containing the public key needed to verify the signature
* `hello.txt.rekor`: an **optional** “offline Rekor bundle” that can be used during verification instead of accessing an online transparency log

Verification looks almost identical to signing, since the `sigstore` CLI intelligently locates the signature, certificate, and optional Rekor bundle based on the input’s filename. To actually perform the verification, we use the `sigstore verify identity` subcommand:

```
$ # finds hello.txt.sig, hello.txt.crt, hello.txt.rekor
$ sigstore verify identity hello.txt \
    --cert-identity foo@example.com \
    --cert-oidc-issuer https://github.com/login/oauth
OK: hello.txt
```

(What’s with the extra flags? Without them, we’d just be verifying the signature and certificate, and *anybody* can get a valid signature for any public input in Sigstore. To make sure that we’re actually verifying something meaningful, the `sigstore` CLI **forces** you to assert which identity the signature is expected to be bound to, which is then checked during certificate verification!)

However, that’s not all! Sigstore is not just for email identities; it also supports URI identities, which can correspond to a particular GitHub Actions workflow run, or some other machine identity. We can do more in-depth verifications of these signatures using the `sigstore verify github` subcommand, which allows us to check specific attestations made by the GitHub Actions runner environment:

```
$ # change this to any version!
$ v=0.10.0
$ repo=https://github.com/sigstore/sigstore-python
$ release="${repo}/release/download"
$ sha=66581529803929c3ccc45334632ccd90f06e0de4

$ # download a distribution + certificate and signature
$ wget ${release}/v${v}/sigstore-${v}.tar.gz{,.crt,.sig}

$ # verify extended claims
$ sigstore verify github sigstore-${v}.tar.gz \
    --cert-identity \
      "${repo}/.github/workflows/release.yml@refs/tags/v${v}" \
    --sha ${sha} \
    --trigger release
```

This goes well beyond what we can prove with just a bare `sigstore verify identity` command: we’re now asserting that the signature was created by a release-triggered workflow run against commit `[66581529803929c3ccc45334632ccd90f06e0de4](https://github.com/sigstore/sigstore-python/commit/66581529803929c3ccc45334632ccd90f06e0de4)`, meaning that even if an attacker somehow managed to compromise our repository’s actions and sign for new inputs, they still couldn’t fool us into accepting the wrong signature for this release!

(`--sha` and `--trigger` are just a small samp...