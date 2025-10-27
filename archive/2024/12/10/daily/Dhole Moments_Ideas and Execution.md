---
title: Ideas and Execution
url: https://soatok.blog/2024/12/09/ideas-and-execution/
source: Dhole Moments
date: 2024-12-10
fetch_date: 2025-10-06T19:39:50.624409
---

# Ideas and Execution

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

[Open Source](https://soatok.blog/category/technology/open-source/)

# Ideas and Execution

4 free ideas that Soatok doesn’t have the time or energy to execute on.

* Post author

  By [Soatok](https://soatok.blog/author/soatok/)
* Post date

  [December 9, 2024](https://soatok.blog/2024/12/09/ideas-and-execution/)

![Ideas and Execution](https://i0.wp.com/soatok.blog/wp-content/uploads/2024/12/BlogHeader-2024-Ideas-Execution.png?fit=1200%2C675&ssl=1)

I’ve been known to blog about ideas that I don’t have the time or energy to build myself–from using asynchronous ratcheting trees to [support multicast networking in WireGuard (and other Noise-based protocols)](https://soatok.blog/2023/10/10/a-plan-for-multicast-support-in-noise-based-protocols/) to [how Bluesky could introduce private accounts (or limited audiences) without changing their current architecture](https://soatok.blog/2024/11/29/imagining-private-airspaces-for-bluesky/)–in the hopes that someone might read them and be inspired to build something similar for themselves.

Business types are fond of saying, “Ideas are cheap, execution is everything.”

In their world, that’s probably sage advice. I immediately imagine people that see themselves as the “idea person” but actually have little contribution to the actual work that needs to get done.

Thus, in the “business” world, a person that has ideas is probably seen as a nuisance, unless they’re also able and willing to execute on them.

**But this blog doesn’t exist in their world, now does it?**

![Three panel comic. First panel: Soatok (blue dhole) picks up a red book, confused. Second panel: The cover of the book. It reads "Being a Yes-Man to Yacht Owners" with the subtitle, "The Rat Race Imagined As An Optimization Problem". Third panel: Soatok smiles and tosses the book over his shoulder as if to say, "Don't need that shit!"](https://i0.wp.com/soatok.blog/wp-content/uploads/2024/12/Book-Meme-Yacht-Owners.png?resize=768%2C244&ssl=1)

[Sophie](https://loviesophie.carrd.co/)

For years, I’ve managed to avoid the perverse incentives that come with profit-seeking, though marketers [still contact me all the time requesting I promote their nonsense](https://soatok.blog/2024/07/02/my-furry-blog-is-not-an-opportunity-to-develop-your-brand/).

This blog does not serve ads. In fact, it promotes the use of adblockers through [this WordPress plugin](https://github.com/stefanbohacek/detect-missing-adblocker).

I refuse to engage in so-called native advertising, or to allow other people to write posts here.

It’s not that I hate money. In fact, I’ve shared a link to let folks [buy me a coffee](https://ko-fi.com/soatok) for a while now, and a few people were kind enough to do so.

**Recently, due to popular demand, I even decided [to start offering Critiques](https://soatok.com/critiques).**

Basically, you can pay for up to an hour of my time to give feedback on software, design docs, etc. in preparation for more formal review. The linked webpage has more details.

> It’s there if anyone wants it, but **nobody** should feel obligated or pressured at all to even consider it. I have a full-time job as a security engineer.

Point being: If I’m not playing their game, I also don’t need to play by their rules. So here are a few free ideas that **anyone** can pick up and run with if they want.

Some of them could yield profitable small businesses (or startups, if you really want to play [the venture capitalism / enshittification game](https://www.ycombinator.com/)). Others might make for neat open source software projects. Some might be total wastes of time, or require expertise that none of us have (myself especially).

* [Threshold Single-Sign On](#threshold-sso)
* [Full-text Beacons for Encrypted Databases](#fulltext-encrypted-search)
* [Random-Access AEAD](#random-access-aead)
* [Differential Complexity Fingerprinting](#differential-complexity)

I will describe each in as much details as I’ve envisioned.

![ ](https://i0.wp.com/soatok.blog/wp-content/uploads/2021/02/soatok-by-scruffkerfluff-smol-1.png?resize=768%2C614&ssl=1)

[ScruffKerfluff](https://scruffkerfluff.carrd.co/)

## Free Ideas (Take One)

Each of these ideas is free for the taking, should anyone wish to adopt them, with no strings or stipulations attached.

However, at the end of this post, I do have [one request](#one-request) to anyone that succeeds at implementing any of them.

I was originally going to include a few more ideas, but they’re too similar to ones I’ve heard other people share, and I don’t want to step on friends’ toes.

![A protogen is about to enjoy a delicious cupcake.](https://i0.wp.com/soatok.blog/wp-content/uploads/2021/07/neophyte-cupcake.png?resize=342%2C512&ssl=1)

Art: [Harubaki](https://harubaki.carrd.co/)

### Threshold Single Sign-On

> **Elevator Pitch**: Use Threshold Signature Schemes and hardware tokens to provide SSO with built-in failover.

Threshold Signature Schemes, such as [FROST (RFC 9591)](https://www.rfc-editor.org/rfc/rfc9591.html), enable use-cases where multiple participants must cooperate in order to produce a valid signature.

FROST specifically is attractive here because one of the ciphersuites produces a valid Ed25519 signature.

To date, most of the interest in threshold signatures comes from the cryptocurrency space, where non-custodial wallets are desirable for… reasons.

What I’m proposing is to instead use them for building an identity provider that has a dedicated service component (what Okta and Auth0 satisfy today) along with an on-premise component for enterprise customers.

![galaxy brain sticker](https://i0.wp.com/soatok.blog/wp-content/uploads/2020/08/soatoktelegrams2020-01.png?resize=512%2C512&ssl=1)

[CMYKat](https://cmykatgraphics.carrd.co/)

#### What Threshold SSO Might Look Like

* Either a custom FIDO2-compatible hardware token, or software that uses [the hmac-secret extension](https://docs.yubico.com/yesdk/users-manual/application-fido2/hmac-secret.html) to derive wrapping keys to encrypt the end user’s shares.
* An appropriate threshold where the end user and *either* the service provider or the on-premise component can produce a valid signature.

  For example: A 3-of-4 configuration where 2 of the shares are protected by the hardware token.
* The message being signed, along with the valid signature, produces a valid credential. See also, [OpenID Connect](https://openid.net/developers/how-connect-works/).

#### “What does this get you?”

With threshold signature schemes, if the service is ever compromised, an attacker can *at best* obtain the service’s share. This is insufficient to generate a valid signature and impersonate users.

The same cannot be said of identity providers today.

Additionally, if the service goes offline or experiences some sort of outage (e.g., distributed denial-of-service attack), the types of enterprise customers that want resilience get automatic fail-over to their own authentication infrastructure, and this can be invisible to their end users.

Resilience, uptime, and a harder attack surface. What’s not to love?

#### “Why haven’t you built this yourself?”

I don’t have the time.

I’m already busy with [other projects](https://soatok.blog/category/technology/open-source/fediverse-e2ee-project/) which are taking up a ton of my time, and I have a full-time job to boot.

There might be technical, financial, political, or logistical hurdles that I haven’t anticipated.

For starters, you need a library that implements...