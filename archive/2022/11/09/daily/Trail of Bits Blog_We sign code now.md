---
title: We sign code now
url: https://blog.trailofbits.com/2022/11/08/sigstore-code-signing-verification-software-supply-chain/
source: Trail of Bits Blog
date: 2022-11-09
fetch_date: 2025-10-03T22:04:37.116712
---

# We sign code now

[The Trail of Bits Blog](/ "The Trail of Bits Blog")

[![Trail of Bits Logo](/img/tob.png)](https://trailofbits.com "Trail of Bits")

# We sign code now

[William Woodruff](https://infosec.exchange/%40yossarian)

November 08, 2022

[open-source](/categories/open-source/), [supply-chain](/categories/supply-chain/), [ecosystem-security](/categories/ecosystem-security/), [cryptography](/categories/cryptography/)

Sigstore announced the [general availability](https://www.prnewswire.com/news-releases/sigstore-announces-general-availability-at-sigstorecon-301657741.html) of its free and ecosystem-agnostic software signing service two weeks ago, giving developers a way to sign, verify and protect their software projects and the dependencies they rely on. Trail of Bits is absolutely thrilled to be a part of the project, and we spoke about our work at the [inaugural SigstoreCon](https://events.linuxfoundation.org/sigstorecon-north-america/).

While the opportunity to speak about Sigstore is amazing, we don’t want to stop there. We think Sigstore is a critical and much-needed step towards accessible software signing, which has become a key component of software supply chain management and security.

Here are some of the ways Trail of Bits has contributed (and will continue to contribute!) to the overall growth of the Sigstore ecosystem. Strap in!

## What exactly is Sigstore?

[![](/img/wpdump/d07c0b734cd5077271b6ec30763c0ff2.png)](/img/wpdump/d07c0b734cd5077271b6ec30763c0ff2.png)

For those unfamiliar: [Sigstore](https://www.sigstore.dev/) is a [Linux Foundation](https://www.linuxfoundation.org/) project, with contributions from big tech companies and well-regarded academic institutions, focused on a simple mission: to enable code signing and verification for everyone.

How it goes about doing that is a little more complicated. Sigstore is composed of two core services:

* [Fulcio](https://github.com/sigstore/fulcio), a public root [certificate authority](https://en.wikipedia.org/wiki/Certificate_authority) that issues short-lived signing certificates for authorized identities and commits those certificates to a Certificate Transparency log;
* [Rekor](https://github.com/sigstore/rekor), a transparency and timestamping service for signed artifacts, with strong integrity guarantees.

Together, Fulcio and Rekor allow programmers to mint short-lived signing certificates, commit to those certificates publicly (making it harder for an attacker to surreptitiously obtain a valid certificate), sign artifacts against those certificates, and then publicly commit to the resulting signatures (again, making it harder for a surreptitious attacker).

The two services use standard formats and protocols ([x509v3](https://datatracker.ietf.org/doc/html/rfc5280) and [CT](https://www.rfc-editor.org/rfc/rfc6962)) in order to be interoperable with pre-existing verification schemes and machinery. Because of this, Sigstore is already being slotted into pre-existing workflows: you can use [gitsign](https://github.com/sigstore/gitsign) today to sign git commits using Sigstore, without any modifications to `git` itself!

## What makes Sigstore special?

Sigstore is basically a [PKI ecosystem](https://en.wikipedia.org/wiki/Public_key_infrastructure), but specialized for short-term signing certificates.

But what gives Sigstore its special sauce is **identity**: Fulcio is a root CA, but only for *developer or machine identities*. More precisely, Fulcio won’t let just any certificate signing request go through: requests must be accompanied by an [OpenID Connect](https://openid.net/connect/) (OIDC) token, which attests to an intended identity. That identity is then baked into the signing certificate, allowing anybody to confirm that signature against that certificate.

When Fulcio receives an OIDC token (which is really just a [JSON Web Token](https://jwt.io/)), it verifies it against the service it claims to be from using OIDC’s `.well-known` lookup protocol. A handful of services (with known-high-quality IdPs) are currently supported, among them:

* **GitHub**: Individual email identities (corresponding to GitHub accounts) can be attested to, as can machine identities for workflow actions.
* **Google and Microsoft**: Individual email identities are supported, including for non-service accounts. In other words: as long as you have a Google or Microsoft account you can attest to the email that’s been linked to it, even if that email is not controlled by Google or Microsoft.
* **Kubernetes**: Cloud-based Kubernetes instances (e.g. those provided by AWS, Azure, and Google Cloud) can attest to their cluster identities.

This identity-first approach turns code-signing on its head: rather than manually establishing trust in the identity behind a public key (which is the norm with PGP-based code signing), a verifier takes a public identity that they trust and simply asks the public signing log whether that identity has signed for the artifact they’d like to use. The end result: strong cryptographic primitives by default, no more brittle key management (on either end), no more [broken webs of trust](https://gist.github.com/rjhansen/f716c3ff4a7068b50f2d8896e54e4b7e), and a publicly-accessible transparency log that keeps all signing parties honest.

This model *additionally* enables powerful misuse-resistant techniques, like “keyless” signing: rather than holding onto long-lived signing keys, users can create a short-lived key, request a certificate for it from Fulcio, and discard it once all signing operations are done. The key never leaves memory and is never reused, drastically reducing the threat (and blast radius) of key theft.

## How do I use Sigstore?

In the abstract, Sigstore’s “identity-first” model can be a little mind-bending. Here’s an example of how it’s used:

To get started, we’ll install [`sigstore-python`](https://github.com/sigstore/sigstore-python), the official (and Trail of Bits maintained!) Python implementation of Sigstore:

```
$ python -m pip install sigstore
```

Once we have it installed, we can use it to sign a local file (you can sign anything, including Python packages or distributions for any language!):

```
$ python -m sigstore sign README.md
Waiting for browser interaction...
Using ephemeral certificate:
-----BEGIN CERTIFICATE-----
MIICwTCCAkegAwIBAgIUZr4/MflYaUb/SSw0CgNj+qLZDhMwCgYIKoZIzj0EAwMw
NzEVMBMGA1UEChMMc2lnc3RvcmUuZGV2MR4wHAYDVQQDExVzaWdzdG9yZS1pbnRl
cm1lZGlhdGUwHhcNMjIxMDI4MTYzMjQzWhcNMjIxMDI4MTY0MjQzWjAAMHYwEAYH
KoZIzj0CAQYFK4EEACIDYgAEVBG9SWAO0pkbhrsKtDUN4Il5OK115yp+Ai5GiDYW
V1obpF1Ih+/NrtTDN+tdkop0T6Z8eotVjpnyrFpc4TbA6okIZ2eo6oFwRD3tn/mG
4BFPgm4O4Nvgih+f75M845c1o4IBSTCCAUUwDgYDVR0PAQH/BAQDAgeAMBMGA1Ud
JQQMMAoGCCsGAQUFBwMDMB0GA1UdDgQWBBRE3hH5uBNf4l/EDxedz0aNNAZX+zAf
BgNVHSMEGDAWgBTf0+nPViQRlvmo2OkoVaLGLhhkPzAjBgNVHREBAf8EGTAXgRV3
aWxsaWFtQHlvc3Nhcmlhbi5uZXQwLAYKKwYBBAGDvzABAQQeaHR0cHM6Ly9naXRo
dWIuY29tL2xvZ2luL29hdXRoMIGKBgorBgEEAdZ5AgQCBHwEegB4AHYACGCS8ChS
/2hF0dFrJ4ScRWcYrBY9wzjSbea8IgY2b3IAAAGEH3BI7gAABAMARzBFAiEAnrGB
RDQMHW26GT4H/nCvTBQ7RzBI3ix8rRewG6Bii10CIBnjNsSYBhNB77nNmAheoxxj
XQWJuQ4n2iQu9FB4AGeKMAoGCCqGSM49BAMDA2gAMGUCMQDaV/a8myBO5yKDBTvS
fM9ziqC1zOiDrXXg+k4lVg02idTHeukbUZTKsROzOsPSRfUCMCsp30CTXrJPBUfN
dCxmp44zCE7/yGkNCu+5waxPhOI7mXrfQ7FqzmZ0Z5cs9H/CiA==
-----END CERTIFICATE-----

Transparency log entry created at index: 6052228
Signature written to file README.md.sig
Certificate written to file README.md.crt
```

This just works™. Behind the scenes, Sigstore is:

**1**. Creating a new local ephemeral keypair;

**2**. Retrieving the OIDC identity token, either via an interactive OAuth2 flow or [ambient credential detection](https://github.com/sigstore/sigstore-python#signing-with-ambient-credentials);

**3**. Submitting a [Certificate Signing Request](https://en.wikipedia.org/wiki/Certificate_signing_request) to Fulcio, combined with the OIDC token and a proof of possession for the private half of the ephemeral keypair;

**4**. Receiving the...