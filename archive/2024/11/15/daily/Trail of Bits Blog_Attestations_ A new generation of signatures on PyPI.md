---
title: Attestations: A new generation of signatures on PyPI
url: https://blog.trailofbits.com/2024/11/14/attestations-a-new-generation-of-signatures-on-pypi/
source: Trail of Bits Blog
date: 2024-11-15
fetch_date: 2025-10-06T19:18:42.625984
---

# Attestations: A new generation of signatures on PyPI

[The Trail of Bits Blog](/ "The Trail of Bits Blog")

[![Trail of Bits Logo](/img/tob.png)](https://trailofbits.com "Trail of Bits")

# Attestations: A new generation of signatures on PyPI

[William Woodruff](https://infosec.exchange/%40yossarian)

November 14, 2024

[open-source](/categories/open-source/), [supply-chain](/categories/supply-chain/), [ecosystem-security](/categories/ecosystem-security/), [engineering-practice](/categories/engineering-practice/)

For the past year, we’ve worked with the Python Package Index (PyPI) on a new security feature for the Python ecosystem: index-hosted digital attestations, as specified in [PEP 740](https://peps.python.org/pep-0740/).

These attestations improve on traditional PGP signatures (which [have been disabled on PyPI](https://blog.pypi.org/posts/2023-05-23-removing-pgp/)) by providing *key usability*, *index verifiability*, *cryptographic strength*, and *provenance* properties that bring us one step closer to *holistic*, cryptographically verifiable provenance for our software supply chains.

![](/img/wpdump/0ab9cff513d5311416598bfdc6682eaf.png)

The good news: if you already publish packages to PyPI using [Trusted Publishing](https://docs.pypi.org/trusted-publishers/), ***you likely won’t have to change a single thing***: the [official PyPI publishing workflow](https://github.com/marketplace/actions/pypi-publish) has attestation support built right in, enabled by default as of [v1.11.0 and newer](https://github.com/pypa/gh-action-pypi-publish/releases/tag/v1.11.0). In other words, so long as you already use (or upgrade to) `pypa/gh-action-pypi-publish@v1.11.0` or newer and with a Trusted Publisher, your packages will get build provenance by default!

Enablement by default was a key design constraint of ours: we wanted an attestation feature that could integrate with existing publishing identities, sidestepping the challenges of key and identity management that recur in traditional digital signature designs. [Sigstore](https://www.sigstore.dev/) afforded itself as the solution to these challenges: its support for identity-based [keyless signing](https://docs.sigstore.dev/cosign/signing/overview/) provides the *publicly verifiable* link between PyPI’s support for Trusted Publishing and package provenance.

Check out the [official PyPI documentation](https://docs.pypi.org/attestations/) for practical information about how to create and use index-hosted attestations, and read on here for our technical summary of how these attestations work and where we see them going in the future!

Read the [official announcement on the PyPI blog](https://blog.pypi.org/posts/2024-11-14-pypi-now-supports-digital-attestations/) as well!

## Background: Trusted Publishing

Last year, [we worked](https://blog.trailofbits.com/2023/05/23/trusted-publishing-a-new-benchmark-for-packaging-security/) with [PyPI](https://pypi.org/) to design and implement [Trusted Publishing](https://docs.pypi.org/trusted-publishers/), a new, more convenient, and more secure way to upload packages to PyPI. Thanks to its usability wins, we’ve seen Trusted Publishing become a *huge* success over the intervening 18 months: over 19,000 individual projects have registered a Trusted Publisher, and those projects have collectively published almost half a million files to PyPI using Trusted Publishing:

![](/img/wpdump/f121b36d7a615b7a69a0fe121c89c44c.png)

We have an entire separate [blog post on Trusted Publishing and PyPI](https://blog.trailofbits.com/2023/05/23/trusted-publishing-a-new-benchmark-for-packaging-security/), but to briefly summarize:

* Trusted Publishing *removes the need for a manually configured and scoped API token*.
* Projects declare approved Trusted Publisher (GitHub, GitLab, Google Cloud Build, ActiveState, etc.) identities that can upload new releases.
* To ensure the *authenticity* of requests from those identities (i.e., the CI/CD workflows purporting to be them), Trusted Publishing uses *public key cryptography* via [OpenID Connect](https://openid.net/connect/) (OIDC).
* The OIDC flow allows the Trusted Publisher to automatically obtain a PyPI API token without user intervention, reducing the opportunity for user errors like credential leaks and accidental over-scoping.
* The resulting tokens issued via this OIDC flow are *short-lived* and *minimally-scoped*, reducing an attacker’s ability to hoard them for future use or pivot between different projects with a single credential.

Trusted Publishing’s success on PyPI has garnered interest from other ecosystems as well: [RubyGems implemented it](https://guides.rubygems.org/trusted-publishing/) just a few months later, and Rust’s crates.io [has an open RFC](https://github.com/rust-lang/rfcs/pull/3691) for it!

## From Trusted Publishing to Sigstore

Trusted Publishing connects PyPI-hosted projects to *cryptographically verifiable machine identities* (such as `release.yml @ github.com/example/example`) that handle publishing.

This is fantastic for eliminating manual API token flows, but it *also* gives us something *much more* fundamental: provenance!

In particular, in the context of a GitHub (or GitLab, etc.) packaging workflow, the machine identity found in an OIDC credential gives us something resembling “publish provenance”: a set of claims about repository and workflow state corresponding to the time at which a package was published to PyPI.

However, in the form of an OIDC credential, this provenance isn’t immediately valuable to external users:

* PyPI can’t share the credential *itself*, since it’s fundamentally secret material. Even with appropriate controls (expiry and a fixed audience), there’s simply too much risk of PII disclosure and misbehaving JWT verifiers to risk disclosure for external (meaning non-PyPI) verification.
* PyPI *could* disclose the claims within the credential, such as by publishing metadata to the effect of “project `sampleproject` was published by a GitHub workflow `pypi-publish.yml` that ran from `pypa/sampleproject`.” This would result in a model where downstream users are forced to trust that PyPI honestly serves those claims.

This is where [Sigstore](https://www.sigstore.dev/) comes in. We have *another* entire separate [blog post on Sigstore and how it works](https://blog.trailofbits.com/2022/11/08/sigstore-code-signing-verification-software-supply-chain/), but the key part for our purpose is that Sigstore binds *short-lived signing keys to machine identities* via a free, publicly accessible, auditable certificate authority ([Fulcio](https://docs.sigstore.dev/certificate_authority/overview/)).

Fulcio accepts machine identities in the form of OIDC credentials, meaning that PyPI’s Trusted Publishing flow is *implicitly compatible* with Sigstore signing: all that the Trusted Publisher needs to do is submit a Certificate Signing Request to Fulcio with the OIDC credential and receive a signing certificate for subsequent use.

Fulcio will embed the appropriate claims from the OIDC credential into the public certificate, giving us a *publicly verifiable* source of provenance that doesn’t require disclosing the credential itself *or* unilaterally trusting PyPI to serve it correctly!

The steps involved in this can be a little hard to follow, so let’s visualize them. Here’s the “traditional” Trusted Publishing flow, before any involvement from Sigstore:

![](/img/wpdump/0390063b46a2ff61347896086f70f3dd.png)

And then, with Sigstore in the loop:

![](/img/wpdump/8a8997986668d5ba8a6b8811985de630.png)

Observe that, while there’s one more entity in the flow (Sigstore), *nothing changes from the user’s perspective*: all that’s needed from them is their one-time Trusted Publisher configuration, which comes from the original flow.

## From Sigstore to attestations and provenance

Sigstore narrows the gap between Trusted Publishing and provenance by giving us a *public*, *verifiable* credential (in the form of an X.509 certificate) that binds an ephem...