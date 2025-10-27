---
title: Introducing Alacrity to Federated Cryptography
url: https://soatok.blog/2024/08/28/introducing-alacrity-to-federated-cryptography/
source: Dhole Moments
date: 2024-08-29
fetch_date: 2025-10-06T18:04:45.150506
---

# Introducing Alacrity to Federated Cryptography

[Skip to the content](#site-content)

Search

[Dhole Moments](https://soatok.blog/)

Software, Security, Cryptography, and Furries

Menu

* [Home](https://soatok.blog/)
* [Blog](https://soatok.blog/b/)
* [Explore](https://soatok.blog/explore/)
* [About](https://soatok.blog/about/)

Search

Search for:

Close search

Close Menu

* [Home](https://soatok.blog/)
* [Blog](https://soatok.blog/b/)
* [Explore](https://soatok.blog/explore/)
* [About](https://soatok.blog/about/)

Categories

[Cryptography](https://soatok.blog/category/cryptography/) [Fediverse E2EE Project](https://soatok.blog/category/technology/open-source/fediverse-e2ee-project/) [Open Source](https://soatok.blog/category/technology/open-source/) [Security Community](https://soatok.blog/category/technology/software-security/security-community/)

# Introducing Alacrity to Federated Cryptography

* Post author

  By [Soatok](https://soatok.blog/author/soatok/)
* Post date

  [August 28, 2024](https://soatok.blog/2024/08/28/introducing-alacrity-to-federated-cryptography/)

![Introducing Alacrity to Federated Cryptography](https://i0.wp.com/soatok.blog/wp-content/uploads/2024/08/BlogHeader-2024-Alacrity.png?fit=1200%2C675&ssl=1)

There are two mental models for designing a cryptosystem that offers end-to-end encryption to all of its users.

The first is the Signal model.

Predicated on Moxie’s notion that [the ecosystem is moving](https://signal.org/blog/the-ecosystem-is-moving/), Signal (and similar apps) maintain some modicum of centralized control over the infrastructure and deployment of their app. While there are obvious downsides to this approach, it allows them to quickly roll out ecosystem-wide changes to their encryption protocols without having to deal with third-party clients falling behind.

The other is the federated model, which is embraced by [Matrix](https://soatok.blog/2024/08/14/security-issues-in-matrixs-olm-library/), [XMPP with OMEMO](https://soatok.blog/2024/08/04/against-xmppomemo/), and other encrypted chat apps and protocols.

This model can be attractive to a lot of people whose primary concern is data sovereignty rather than cryptographic protections. (Most security experts care about both aspects, but we differ in how they rank the two priorities relative to each other.)

As I examined in my criticisms of Matrix and XMPP+OMEMO, they kind of prove Moxie’s point about the ecosystem:

* Two years after the Matrix team deprecated their C implementation of Olm in favor of a Rust library, virtually all of the clients that actually switched (as of the time of my blog post disclosing vulnerabilities in their C library) were either Element, or forks of Element. The rest were still wrapping libolm.
* Most OMEMO libraries are [still stuck on version 0.3.0](https://xmpp.org/extensions/#xep-0384-implementations) of the specification, and cannot communicate with XMPP+OMEMO implementations that are on [newer versions of the specification](https://xmpp.org/extensions/attic/xep-0384-0.8.3.html).

And this is personally a vexing observation, for two reasons:

1. I don’t *like* that Moxie’s opinion is evidently more correct when you look at the consequences of each model.
2. I’m planning to develop [end-to-end encryption for direct messages on the Fediverse](https://github.com/soatok/mastodon-e2ee-specification), and don’t want to repeat the mistakes of Matrix and OMEMO.

   (Aside from them mistakenly claiming to be [Signal competitors](https://soatok.blog/2024/07/31/what-does-it-mean-to-be-a-signal-competitor/), which I am not doing with my E2EE proposal or any implementations thereof.)

Fortunately, I have a solution to both annoyances that I intend to implement in my end-to-end encryption proposal.

Thus, I’d like to introduce **Cryptographic Alacrity** to the discussion.

> **Note:** The term “crypto agility” was already coined by people who never learned from [the alg=none vulnerability of JSON Web Tokens](https://www.howmanydayssinceajwtalgnonevuln.com/) and think it’s A-okay to negotiate cryptographic primitives at run-time based on attacker-controllable inputs.
>
> Because they got their foolish stink all over that term, I discarded it in favor of coining a new one. I apologize for the marginal increase in cognitive load this decision may cause in the future.

## Cryptographic Alacrity

For readers who aren’t already familiar with the word “alacrity” from playing *Dungeons & Dragons* once upon a time, the Merriam-Webster dictionary defines Alacrity as:

> promptness in response **:**cheerful readiness
>
> [Alacrity Definition & Meaning – Merriam Webster](https://www.merriam-webster.com/dictionary/alacrity)

When I describe a cryptography protocol as having “cryptographic alacrity”, I mean there is a built-in mechanism to enforce protocol upgrades in a timely manner, and stragglers (read: non-compliant implementations) will lose the ability to communicate with up-to-date software.

Alacrity must be incorporated into a protocol at its design phase, specified clearly, and then enforced by the community through its protocol library implementations.

The primary difference between Alacrity and Agility is that Alacrity is implemented through protocol versions and a cryptographic mechanism for enforcing implementation freshness across the ecosystem, whereas Agility is about being able to hot-swap cryptographic primitives in response to novel cryptanalysis.

This probably still sounds a bit abstract to some of you.

![Soatok drinking coffee](https://i0.wp.com/soatok.blog/wp-content/uploads/2024/07/SoatokTelegrams2020-15.png?resize=512%2C512&ssl=1)

[CMYKat](https://cmykatgraphics.carrd.co/)

To best explain what I mean, let’s look at a concrete example. Namely, how I plan on introducing Alacrity to my Fediverse E2EE design, and then enforcing it henceforth.

### Alacrity in E2EE for the Fediverse

One level higher in the protocol than bulk message and/or media attachment encryption will be a Key Derivation Function. (Probably HKDF, probably as part of a Double Ratchet protocol or similar. I haven’t specified that layer just yet.)

Each invocation of HKDF will have a hard-coded 256-bit salt particular to the protocol version that is currently being used.

(What most people would think to pass as the salt in HKDF will [instead be appended to the info parameter](https://soatok.blog/2021/11/17/understanding-hkdf/).)

The protocol version will additionally be used in a lot of other places (i.e., domain separation constants), but those are going to be predictable string values.

The salt will not be predictable until the new version is specified. I will likely tie it to the SHA256 hash of a Merkle root of a [Federated Public Key Directory instance](https://github.com/fedi-e2ee/public-key-directory-specification) and the nickname for each protocol version.

Each library will have a small window (probably no more than 3 versions at any time) of acceptable protocol versions.

A new version will be specified, with a brand new KDF salt, every time we need to improve the protocol to address a security risk. Additionally, we will upgrade the protocol version at least once a year, even if no security risks have been found in the latest version of the protocol.

If your favorite client depends on a 4 year old version of the E2EE protocol library, you won’t be able to silently downgrade security for all of your conversation participants. Instead, you will be prevented from talking to most users, due to incompatible cryptography.

#### Version Deprecation Schedule

Let’s pretend, for the sake of argument, that we launch the first protocol version on January 1, 2025. And that’s when the first clients start to be built atop the libraries that speak the protocols.

Assuming no emergencies occur, after 9 months (i.e., by October 1, 2025), version 2 of the protocol will be specified. Libraries will be updated to support **reading** (but not sending) messages encrypted with protocol v2.

Then, on January ...