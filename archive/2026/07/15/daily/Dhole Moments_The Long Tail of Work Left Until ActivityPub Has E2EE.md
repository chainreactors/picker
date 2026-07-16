---
title: The Long Tail of Work Left Until ActivityPub Has E2EE
url: https://soatok.blog/2026/07/15/the-long-tail-of-work-left-until-activitypub-has-e2ee/
source: Dhole Moments
date: 2026-07-15
fetch_date: 2026-07-16T04:57:57.854287
---

# The Long Tail of Work Left Until ActivityPub Has E2EE

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

[Fediverse E2EE Project](https://soatok.blog/category/technology/open-source/fediverse-e2ee-project/)

# The Long Tail of Work Left Until ActivityPub Has E2EE

* Post author

  By [Soatok](https://soatok.blog/author/soatok/)
* Post date

  [July 15, 2026](https://soatok.blog/2026/07/15/the-long-tail-of-work-left-until-activitypub-has-e2ee/)

!["The Long Tail of Work Left Until ActivityPub Has E2EE" written above art of Soatok's fursona with an extremely big fluffy tail.](https://i0.wp.com/soatok.blog/wp-content/uploads/2026/07/BlogHeader-2026-LongTail.png?fit=1200%2C675&ssl=1)

Separate from my proposal for [key transparency for the Fediverse](https://publickey.directory/) (which I’ve certainly blogged about a lot), the W3C has been [working on building out end-to-end encryption (E2EE) for ActivityPub](https://github.com/swicg/activitypub-e2ee).

The two projects are mostly being developed independent of each other, though connecting the two [should be straightforward](https://github.com/swicg/activitypub-e2ee/issues/35#issuecomment-3738855995).

As I prepare to tie up the loose ends and call my side of the work “feature complete” and consider tagging a major version 1.0.0 for the specification and reference implementations, I thought it would be useful to lay out the work that needs to be done in order to get this over the finish line–in part, because this is where **most technical folks can begin to meaningfully contribute without needing security or cryptography expertise**.

Unlike most of my blog posts (which are intended to be what some bloggers call “evergreen”), I fully intend for this one to be less useful over time, as the work gets done.

To make the most sense, I’m going to work backwards from the desired end state, delving recursively into prerequisites of each unit of work necessary, and then follow it up with a roadmap that should have no surprises if you read the preceding prose.

![Soatok thinking sticker](https://i0.wp.com/soatok.blog/wp-content/uploads/2025/11/SoatokTelegrams2020-12.png?resize=512%2C512&ssl=1)

Art: [CMYKat](https://cmykatgraphics.carrd.co/)

## Working Backwards

This is a complicated effort, so I think it’s best to start by distilling the desired end state into three distinct goals.

**Fundamental Goal**: Fediverse users should be able to send each other end-to-end encrypted messages, which may include attachments. This must efficiently support group messages, not just 1:1 messaging. This is currently being implemented with [Emissary and Bonfire](https://socialwebfoundation.org/2025/12/19/implementing-encrypted-messaging-over-activitypub/), built on a protocol called [Messaging Layer Security (MLS, RFC 9420)](https://www.rfc-editor.org/rfc/rfc9420.html).

**Security Goal:** Users should be able to know that the end-to-end encryption is being performed correctly, and with the correct encapsulation keys.

To that end, Each encapsulation key (which is shipped in what MLS calls [KeyPackages](https://www.rfc-editor.org/rfc/rfc9420.html#name-key-packages)) *must* be signed, client-side, by the user (using an asymmetric digital signature algorithm).

**Authenticity Goal**: The signing keys must be verifiably controlled by the user, and anyone must be able to verify this property. This verification must not rely on a central authority.

The Authenticity Goal is where key transparency comes in. By providing an append-only cryptographic transparency log of which Actor (in ActivityPub parlance) controls which signing keys, you can build a decentralized root of trust. This is where [my focus has been](https://soatok.blog/category/technology/open-source/fediverse-e2ee-project/) for the past several years.

These goals build on each other:

* Without satisfying the Fundamental Goal, none of this work has any real pay-off to end users.
* Without satisfying the Security Goal, the end-to-end encryption must come with a giant fucking asterisk that nobody wants.
* Without satisfying the Authenticity Goal, Fediverse clients that wish to support E2EE will resort to Safety Numbers of Key Fingerprinting–techniques that even professional cryptographers I respect do not bother themselves with, and therefore not a realistic expectation for most people either.

Let’s first discuss each of these three work streams as separately as possible.

![Clipboard Sticker](https://i0.wp.com/soatok.blog/wp-content/uploads/2021/04/soatok-telegrams-wave-3-commission-11.png?resize=512%2C512&ssl=1)

[CMYKat](https://cmykatgraphics.carrd.co/)

#### Why Do Something Rather Than Nothing?

> **Note:** This was added after the blog post was initially published because it’s important context.

The status quo is as follows:

* Direct Messages today do not use end-to-end encryption
* Regardless of [jurisdiction](https://soatok.blog/2025/07/09/jurisdiction-is-nearly-irrelevant-to-the-security-of-encrypted-messaging-apps/), storing sensitive messages and attachments as plaintext is [legally perilous for Fediverse instance hosts](https://www.eff.org/deeplinks/2023/07/fbi-seizure-mastodon-server-wakeup-call-fediverse-users-and-hosts-protect-their)
  + The EU codifying ChatControl 1.0 into law is also noteworthy here

This may come as a surprise to some folks, but sending nude images or videos is kind of a normal thing that many adults want to do (hopefully with consenting recipients).

But if you have a large repository of such content, suddenly these instances becomes a juicy target for sextortion or revenge porn. This is also a risk if one of your instance administrators goes rogue, or is secretly evil to begin with.

End-to-end encryption mitigates most of this risk by virtue of *not having any plaintext stored on any Fediverse instance servers to begin with*.

For more on threat modeling, see [my previous blog post](https://soatok.blog/2026/06/30/soatoks-informal-guide-to-threat-models/).

![Soatok maximizing the use of rainbows](https://i0.wp.com/soatok.blog/wp-content/uploads/2023/07/soatok-stickers4.png?resize=512%2C512&ssl=1)

Art: [MarleyTanuki](https://sfw.furaffinity.net/user/marleytanuki)

### E2EE with ActivityPub

The Fundamental Goal (as I defined above) is being worked on by [the SWICG’s ActivityPub E2EE project team](https://github.com/swicg/activitypub-e2ee) (part of W3C). Most of their work can be surmised by reading [the draft specification](https://swicg.github.io/activitypub-e2ee/mls) and [the issue tracker on GitHub](https://github.com/swicg/activitypub-e2ee/issues).

In order to achieve this goal, they (obviously) need MLS implementations in each of the programming languages relevant to end user Fediverse clients.

For example, [ts-mls](https://github.com/LukaJCB/ts-mls) is a TypeScript implementation of MLS that supports post-quantum cryptography, and [OpenMLS](https://openmls.tech/) is a Rust implementation that ts-mls is being tested against for interoperability.

There is currently [an Internet Draft for post-quantum MLS](https://www.ietf.org/archive/id/draft-ietf-mls-pq-ciphersuites-05.html) being discussed [on the IETF MLS mailing list](https://mailarchive.ietf.org/arch/browse/mls/). The latest draft includes a registration for [a ciphersuite that I requested](https://mailarchive.ietf.org/arch/msg/mls/goy5Lzp4Sqht5fUSQTXJuzpR9hU/) (and recommended to [the ActivityPub E2EE project](https://github.com/swicg/activitypub-e2ee/issues/59)).

As I noted [in my previous blog post](https://soatok.blog/2026/06/30/soatoks-informal-guide-to-threat-models/#distributed-e2e...