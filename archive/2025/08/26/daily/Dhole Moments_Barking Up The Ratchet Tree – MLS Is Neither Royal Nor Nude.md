---
title: Barking Up The Ratchet Tree – MLS Is Neither Royal Nor Nude
url: https://soatok.blog/2025/08/25/barking-up-the-ratchet-tree-mls-is-neither-royal-nor-nude/
source: Dhole Moments
date: 2025-08-26
fetch_date: 2025-10-07T00:48:27.143533
---

# Barking Up The Ratchet Tree – MLS Is Neither Royal Nor Nude

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

[Cryptography](https://soatok.blog/category/cryptography/) [Security Community](https://soatok.blog/category/technology/software-security/security-community/)

# Barking Up The Ratchet Tree – MLS Is Neither Royal Nor Nude

* Post author

  By [Soatok](https://soatok.blog/author/soatok/)
* Post date

  [August 25, 2025](https://soatok.blog/2025/08/25/barking-up-the-ratchet-tree-mls-is-neither-royal-nor-nude/)

![Barking Up The Ratchet Tree - MLS Is Neither Royal Nor Nude](https://i0.wp.com/soatok.blog/wp-content/uploads/2025/08/BlogHeader-2025-MLS-Naked.png?fit=1200%2C675&ssl=1)

One of the first rules you learn about technical writing is, “Know your audience.” But often, this sort of advice is given without sufficient weight or practical examples. Instead, you’re ushered quickly onto the actual tactile aspects of writing–with the hope that some seed was planted that will sprout later in your education.

**Science communication is famously a hard problem.**

The formal scientific literature is often written with an intended audience of other scientists. In the past few decades, an industry of popular science publications sought to bridge the gap between the cool things scientists were doing and us mere mortals who completely lack the intuition necessary to wrap our heads around the intricacies and nuances of what the eggheads figured out in their pursuit of higher-quality ignorance. The few science communicators who excelled in not only informing, but also exciting, a young audience would be celebrated for decades to come.

We all remember Mythbusters, right?

One of the things that exacerbates the difficulty of effective science communication is when you cannot know, let alone choose, who your audience is. Deprived of the ability to work backwards from what the intended recipient already knows and believes, you have to make tough choices about how to articulate your ideas.

When the Internet Engineering Task Force publishes an RFC, their bar is community rough consensus. RFCs are, inherently, the result of a design-by-committee writing process; usually intended for engineers to read. Especially with cryptography, they err on the side of technical specification rather than introductory blog post.

When someone misinterprets an IETF RFC, [it can have devastating security implications](https://web.archive.org/web/20250722114544/https%3A//paragonie.com/blog/2017/03/jwt-json-web-tokens-is-bad-standard-that-everyone-should-avoid). So, in recent years, RFC authors have demonstrated a tendency to err on the side of overcommunicating security risks. However, this is a delicate balance to strike: If you go too far, you risk confusing or scaring the reader. This is especially risky since RFCs are often read by non-engineers, making the specter of science communication difficulty continue to haunt us.

With all that in mind, several people have asked me in recent weeks for my thoughts on a blog post published earlier this month titled, *[MLS: The Naked King of End-to-End Encryption](https://ghostarchive.org/archive/LBbj6)*.

So let’s get into that.

![Clipboard Sticker](https://i0.wp.com/soatok.blog/wp-content/uploads/2021/04/soatok-telegrams-wave-3-commission-11.png?resize=512%2C512&ssl=1)

[CMYKat](https://cmykatgraphics.carrd.co/)

## What is MLS, anyway?

MLS (Messaging Layer Security, [RFC 9420](https://www.rfc-editor.org/rfc/rfc9420.html)) is a protocol for establishing a shared key for a group of users and maintaining it as users join, leave, or rotate their own private credentials. The relevant concept here is called **Continuous Group Key Agreement**.

MLS is not a complete end-to-end encryption software protocol, in the way that TLS (Transport Layer Security) owns virtually the entire communication stack for communicating over networks. (You’re using TLS right now, and whenever you access a website over HTTPS.)

MLS is a building block; a well-designed tool whose designers made specific trade-offs in order to satisfy their understanding of the threat model for group private messaging.

In the hands of practical engineers and architects, MLS is an excellent starting point for building a complete end-to-end encryption system.

MLS is currently being considered by the W3C [for end-to-end encryption for the Fediverse](https://github.com/swicg/activitypub-e2ee). My own initiative, which was not tethered to any standards organization, was [also likely to settle on MLS](https://github.com/soatok/mastodon-e2ee-specification/issues/3).

### Contextualizing MLS

MLS is very limited in its scope.

It’s chiefly a group key agreement protocol built atop a binary tree of key encapsulation mechanisms, with some other features thoughtfully attached to make it easy to securely integrate into messaging software.

MLS doesn’t boil the ocean on *what you actually use those keys for*. Why would it? That’s not MLS’s job to figure out.

MLS excludes a lot of other things from its scope, because it really wouldn’t make architectural sense for MLS to cover them.

You can deploy MLS in a closed-source, centralized, enshittified, corporate messaging app, without needing to change any of the cryptographic properties.

You can also deploy MLS in an open source, federated protocol with multiple independent clients. Once again, the cryptography used by MLS doesn’t need to change.

But these are two very different types of applications, with different concepts of what a user’s “identity” even is, vastly different trust and threat models, and vastly different networking topologies.

#### Okay, what gives?

In order to integrate MLS in your software, you need to decide on two “Services” (from a loose architectural sense).

1. The **Delivery Service** is responsible for yeeting ciphertext from one party to another. It isn’t responsible for much else.

   It’s important that the Delivery Service provides availability for the entire network.
2. The **Authentication Service** is responsible for vending identity keys and proofs of possession to the clients.

   MLS doesn’t delve into the Authentication Service in great detail, because this is very specific to where MLS is being deployed.

   Some deployments may want a private Certificate Authority with some attestations bound to a FIDO key or even government-issued ID. More open and anonymous systems may benefit from Key Transparency. The MLS RFC even calls out CONIKS.

Ultimately, what the Authentication Service actually means or looks like is an architectural decision that *you* have to make when you deploy MLS in your application. MLS doesn’t make the decision for you.

#### Why are you telling me all this?

This is important context to know up front before we dive into the claims made by [Poberezkin’s blog post](https://ghostarchive.org/archive/LBbj6).

![A protogen with purple and green fur sits cross-legged, typing on a wireless keyboard.](https://i0.wp.com/soatok.blog/wp-content/uploads/2021/07/neophyte-sitting.png?resize=422%2C512&ssl=1)

Art by [Harubaki](https://harubaki.carrd.co/)

## Claims Made By Evgeny Poberezkin

Poberezkin’s blog post starts off strong, but then makes a sharp turn shortly after introducing the subject matter.

> **Does MLS Work for End-to-End Encryption?**
>
> *TL;DR: Yes, if you accept “Trust Me Bro” security model*.
>
> [MLS: The Naked King of End-to-End Encryption](https://www.poberezkin.com/posts/2025-08-12-mls-the-naked-king-of-end-to-end-encryption.html)

How flippant. But let’s read on.

They describe the Double Ratchet...