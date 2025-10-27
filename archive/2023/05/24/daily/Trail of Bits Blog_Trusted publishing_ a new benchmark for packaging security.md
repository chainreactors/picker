---
title: Trusted publishing: a new benchmark for packaging security
url: https://blog.trailofbits.com/2023/05/23/trusted-publishing-a-new-benchmark-for-packaging-security/
source: Trail of Bits Blog
date: 2023-05-24
fetch_date: 2025-10-04T11:38:50.836577
---

# Trusted publishing: a new benchmark for packaging security

[The Trail of Bits Blog](/ "The Trail of Bits Blog")

[![Trail of Bits Logo](/img/tob.png)](https://trailofbits.com "Trail of Bits")

# Trusted publishing: a new benchmark for packaging security

[William Woodruff](https://infosec.exchange/%40yossarian)

May 23, 2023

[ecosystem-security](/categories/ecosystem-security/), [engineering-practice](/categories/engineering-practice/)

*Read the [official announcement on the PyPI blog](https://blog.pypi.org/posts/2023-04-20-introducing-trusted-publishers/) as well!*

For the past year, we’ve worked with the [Python Package Index](https://pypi.org/) to add a new, more secure authentication method called “trusted publishing.” Trusted publishing eliminates the need for long-lived API tokens and passwords, reducing the risk of supply chain attacks and credential leaks while also streamlining release workflows. [Critical](https://pypi.org/project/cryptography/) [packages](https://pypi.org/project/Flask/) [on PyPI](https://pypi.org/project/urllib3/) are already using trusted publishing to make their release processes more secure.

If you publish packages to PyPI, use the official PyPI documentation to set up trusted publishing for your projects today. The rest of this post will introduce the technical how and why of trusted publishing, as well as where we’d like to see similar techniques applied in the future.

We love to help expand trust in language ecosystems. Contact us if you’re involved in a packaging ecosystem (e.g., NPM, Go, Crates, etc) and want to adopt more of these techniques!

### Trusted publishing: a primer

At its core, trusted publishing is “just” another authentication mechanism. In that sense, it’s no different from passwords or long-lived API tokens: you present some kind of proof to the index that states your identity and expected privileges; the index verifies that proof and, if valid, allows you to perform the action associated with those privileges.

What makes trusted publishing interesting is how it achieves that authentication **without requiring a preexisting shared secret**. Let’s get into it!

#### OpenID Connect and “ambient” credentials

Trusted publishing is built on top of [OpenID Connect](https://openid.net/connect/) (OIDC), an open identity attestation and verification standard built on top of [OAuth2](https://oauth.net/2/). OIDC enables identity providers (IdPs) to produce publicly verifiable credentials that attest to a particular identity (like hamilcar@example.com) . These credentials are [JSON Web Tokens](https://jwt.io/) (JWTs) under the hood, meaning that an identity under OIDC is the set of relevant [claims](https://jwt.io/introduction) in the JWT.

To drive that point home, here’s what a (slightly redacted) claim set might look like for a user identity presented by GitHub’s OIDC IdP:

[![](/img/wpdump/ee32d43b8fb013bdefa50f687f9b6040.jpg)](/img/wpdump/ee32d43b8fb013bdefa50f687f9b6040.jpg)

(In an actual JWT, this claim set would be accompanied by a digital signature proving its authenticity for a [trusted signing key](https://auth0.com/docs/secure/tokens/json-web-tokens/json-web-key-sets) held by the IdP. Without that digital signature, we’d have no reason to trust the claims!)

Anybody can be an IdP in an OpenID Connect scheme. Still, a large part of the practical value of OIDC is derived from interactions with large, presumed-to-be-trustworthy-and-well-secured IdPs. There’s value in proving ownership over things like GitHub and Google accounts, particularly for things like [SSO](https://en.wikipedia.org/wiki/Single_sign-on) and service federation.

So far, so good, but none of this is especially relevant to packaging indices like PyPI. PyPI could allow users to sign in with OIDC rather than passwords, but it’s unclear how that would make publishing workflows, particularly CI-based ones, any more convenient.

What makes OIDC useful to package indices like PyPI is the observation that an OIDC identity doesn’t need to be a human: it can be a machine identifier, a source repository, or even a specific instance of a CI run. Moreover, it doesn’t need to be obtained through an interactive OAuth2 flow: it can be offered “ambiently” as an object or resource that only the identity (machine, etc.) can access.

CI providers figured this out not too long ago: GitHub Actions [added support](https://docs.github.com/en/actions/deployment/security-hardening-your-deployments/about-security-hardening-with-openid-connect) for ambient OIDC credentials in [late 2021](https://github.blog/changelog/2021-10-27-github-actions-secure-cloud-deployments-with-openid-connect/), while GitLab added it [just a few months ago](https://docs.gitlab.com/ee/ci/secrets/id_token_authentication.html). Here’s what retrieving one of those credentials looks like on GitHub Actions:

[![](/img/wpdump/ba7af6e8ec461fe80df9591ca646247e.jpg)](/img/wpdump/ba7af6e8ec461fe80df9591ca646247e.jpg)

And here’s what the (again, filtered) claim set for a GitHub Actions workflow run might look like:

[![](/img/wpdump/9996021ec99811184685d70397ce3e6a.jpg)](/img/wpdump/9996021ec99811184685d70397ce3e6a.jpg)

This is *a lot* of context to work with: assuming that we trust the IdP and that the signature checks out, we can verify the identity down to the exact GitHub repository, the workflow that ran, the user that triggered the workflow, and so forth. Each of these can, in turn, become a constraint in an authentication system.

#### Trust is everything

To recap: OpenID Connect gives us the context and machinery we need to verify proofs of identity (in the form of OIDC tokens) originating from an IdP. The identities in these proofs can be anything, including the identity of a GitHub Actions workflow in a particular repository.

Any third-party service (like PyPI) can, in turn, accept OIDC tokens and determine a set of permissions based on them. Because OIDC tokens are cryptographically tied to a particular OIDC IdP’s public key, an attacker cannot spoof an OIDC token, even if they know the claims within it.

But wait a second: how do we get from an OIDC token containing an identity to a specific PyPI project? How do we know which PyPI project(s) should trust which OIDC identity or identities?

This is where a bit of [trusted setup](https://docs.pypi.org/trusted-publishers/adding-a-publisher/) is required: a user (on PyPI) has to log in and configure the trust relationship between each project and the publishers (i.e., the OIDC identities) that are authorized to publish on behalf of the project.

This needs to be done only once, as with a normal API token. Unlike an API token, however, it only involves one party: the CI (and OIDC) provider doesn’t need to be given a token or any other secret material. Moreover, even the trusted setup part is composed of completely public information: it’s just the set of claim values that the user considers trustworthy for publishing purposes. For GitHub Actions publishing to PyPI, the trusted setup would include the following:

1. The GitHub **user/repo** slug
2. The filename of the GitHub Actions workflow that’s doing the publishing (e.g., **release.yml**)
3. Optionally, the name of a [GitHub Actions environment](https://docs.github.com/en/actions/deployment/targeting-different-environments/using-environments-for-deployment) that the workflow uses (e.g., **release**)

Together, these states allow the relying party (e.g., PyPI) to accept OIDC tokens, confirm that they’re signed by a trusted identity provider (e.g., GitHub Actions), and then match the signed claims against one or more PyPI projects that have established trust in those claims.

#### Look ma, no secrets!

At this point, we have everything we need to allow an identity verified via OIDC to publish to PyPI. Here’s what that looks like in the GitHub case:

1. A developer (or automation) triggers a GitHub Actions workflow to release to PyPI.
2. The normal build process (**python -m build** or similar) commences.
3. Automation retrieves ...