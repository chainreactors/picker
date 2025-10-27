---
title: What Does It Mean To Be A Signal Competitor?
url: https://soatok.blog/2024/07/31/what-does-it-mean-to-be-a-signal-competitor/
source: Dhole Moments
date: 2024-08-01
fetch_date: 2025-10-06T18:04:32.489201
---

# What Does It Mean To Be A Signal Competitor?

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

[Software Security](https://soatok.blog/category/technology/software-security/)

# What Does It Mean To Be A Signal Competitor?

* Post author

  By [Soatok](https://soatok.blog/author/soatok/)
* Post date

  [July 31, 2024](https://soatok.blog/2024/07/31/what-does-it-mean-to-be-a-signal-competitor/)
* [13 Comments on What Does It Mean To Be A Signal Competitor?](https://soatok.blog/2024/07/31/what-does-it-mean-to-be-a-signal-competitor/#comments)

A lot of recent (and upcoming) blog posts I’ve written, and Fediverse discussions I’ve participated in, have been about the security of communication products.

My criticism of these products is simply that, from a cryptography and security perspective, they’re not a real competitor to Signal.

For all its other faults, Signal sets the bar for secure private messaging. It’s a solid security tool, even if its user experience and feature set leaves a lot of people disappointed. [I highly recommend it over, say, Telegram](https://soatok.blog/2024/05/14/its-time-for-furries-to-stop-using-telegram/).

In response to my post about jettisoning Telegram, quite a few people have tried to evangelize other products. For example:

> Edit: Oh yeah, DON’T USE SIGNAL. Use [Matrix](https://web.archive.org/web/20240731062107mp_/https%3A//matrix.org) instead, offers the benefits of signal without the drawbacks of lack of sync and phone number requirements and is decentralized. The fact that everyone is going gaga for signal as “the BEST messaging app” should be a big red flag in and of itself, because hype trains like this aren’t organic, just saying.
>
> [Draconic\_NEO on pawb.social](https://web.archive.org/web/20240731062107/https%3A//pawb.social/post/9842375)

So, let me explain what it means for a communication product to qualify as a Signal competitor from the perspective of someone whose job involves auditing cryptography implementations.

## The Minimum Bar to Clear

### Open Source

Every private messaging app must be open source in order to qualify as a Signal competitor.

If it’s not open source, it’s not even worth talking about.

### End-to-End Encryption

Messages MUST be end-to-end encrypted. This means that you encrypt on one participant’s device, decrypt on another’s, and nobody in the middle can observe plaintext.

When I say MUST, I mean the [RFC 2119](https://datatracker.ietf.org/doc/html/rfc2119) keyword.

There must never be a “transmit plaintext” option. No excuses. Secure cryptography is not interoperable with insecure cryptography. If you allow a “transmit plaintext” mode for any reason whatsoever, you have failed to build an encryption product that meets the bar.

This disqualifies Matrix.

This disqualifies Telegram.

This disqualifies XMPP + OMEMO.

This alone disqualifies *a lot of so-called private messaging apps*.

This doesn’t mean your product is *insecure*, or that I’m aware of any specific ways to break it.

It just doesn’t occupy the same mindshare as Signal, which only transmits encrypted data and doesn’t have a plaintext protocol to downgrade to.

Therefore, it’s not a goddamn Signal alternative.

### How You Encrypt Matters

Signal normalized the use of AES-256-CBC with HMAC-SHA256.

Facebook’s “Secret Conversations” feature deviated from this and preferred AES-GCM for attachments, but this bit them when [the Invisible Salamanders attack](https://eprint.iacr.org/2019/016) was discovered.

The way Signal uses AES+HMAC is fine for their use case, but building a secure committing AEAD mode (rather than merely AE) out of these primitives is [nontrivial](https://soatok.blog/2021/07/30/canonicalization-attacks-against-macs-and-signatures/).

If you’re aiming to compete with Signal on security, you should, at minimum, expect to engage with a cryptography auditing firm at least once a year to review and re-review your protocol designs and implementations.

### I Will Heavily Scrutinize Your Group Messaging Protocols

Group messaging is one of those topics that might sound easy if you can do peer-to-peer messaging securely, but is catastrophically difficult once you get into the details.

See also: [My blog post about Threema](https://soatok.blog/2021/11/05/threema-three-strikes-youre-out/#invisible-salamanders-with-group-messaging).

If you want a starting point, look at [RFC 9420](https://datatracker.ietf.org/doc/rfc9420/) (Messaging Layer Security, which is a *group key agreement* protocol for messaging apps).

### How You Manage Keys Matters

Tox attempted to build atop NaCl’s crypto\_box interface, but this is not suitable for a general purpose secure messaging due to [a lack of KCI Security](https://github.com/TokTok/c-toxcore/issues/426).

Key management (which is the focus of an upcoming blog post) is a problem that almost everyone underestimates. It’s also the most user-facing aspect of these messaging applications.

WhatsApp uses [Key Transparency](https://engineering.fb.com/2023/04/13/security/whatsapp-key-transparency/) to scale user trust. I’m proposing [something similar for E2EE for the Fediverse](https://soatok.blog/2022/11/22/towards-end-to-end-encryption-for-direct-messages-in-the-fediverse/).

This is a much better strategy than expecting users to manually verify “fingerprints”.

Don’t look at OpenPGP as a role model when it comes to user experience. Johnny still cannot fucking encrypt.

### Your Feature Should Not Bypass Privacy

Want to add all sorts of frills, like video chat or some dumb bullshit with AI and/or blockchain to secure the attention of venture capitalist investors?

You’d better not implement them in such a way that leaks users’ messages or search queries to your service.

The main reason Signal is “missing” features is because they are thoughtful about how these features are designed and implemented.

Guess what happens if you prioritize shipping features over privacy and cryptography engineering?

That’s right: You stop being a contender for a Signal alternative.

## So What?

If your fave isn’t a viable alternative to Signal, *don’t fucking recommend it to people* in response to me recommending Signal.

That’s all I ask.

![](https://i0.wp.com/soatok.blog/wp-content/uploads/2021/02/soatok-by-scruffkerfluff-smol-1.png?resize=768%2C614&ssl=1)

Art: [Scruff](https://scruffkerfluff.carrd.co/)

### But what about…?

I’m not here to discuss your use cases, or usability, or anything else. I’m also not saying that Signal is perfect!

Signal is a private messaging app that I would feel safe recommending whistleblowers to use. It meets all these requirements.

In order to be a Signal competitor, *no matter how much you like your app*, it needs to meet them too, otherwise it isn’t a Signal competitor. Them’s the rules!

![](https://i0.wp.com/soatok.blog/wp-content/uploads/2023/10/SoatokLecture.png?resize=512%2C402&ssl=1)

[AJ](https://sfw.furaffinity.net/user/ajlovesdinos/)

There may be other requirements that are more important to you, that Signal doesn’t meet. That’s fine! You can like other things.

But unless your favorite widget **also meets all of the things on this page**, it’s not a valid competitor from a security and privacy perspective, and therefore I don’t want to fucking hear about it in response to me saying “use Signal until something better comes along”.

*Capiche?*

## Addendum (2024-08-01)

Since I originally posted this, there have been a lot of opinions expressed and questions asked about messaging apps that have nothing to do with cryptographic security.

Those are...