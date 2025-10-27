---
title: Ambition, The Fediverse, and Technology Freedom
url: https://soatok.blog/2024/10/12/ambition-the-fediverse-and-technology-freedom/
source: Dhole Moments
date: 2024-10-13
fetch_date: 2025-10-06T18:49:54.935320
---

# Ambition, The Fediverse, and Technology Freedom

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

[Fediverse E2EE Project](https://soatok.blog/category/technology/open-source/fediverse-e2ee-project/) [Open Source](https://soatok.blog/category/technology/open-source/)

# Ambition, The Fediverse, and Technology Freedom

* Post author

  By [Soatok](https://soatok.blog/author/soatok/)
* Post date

  [October 12, 2024](https://soatok.blog/2024/10/12/ambition-the-fediverse-and-technology-freedom/)

![Ambition, The Fediverse, and Technology Freedom](https://i0.wp.com/soatok.blog/wp-content/uploads/2024/10/BlogHeader-2024-Ambition.png?fit=1200%2C675&ssl=1)

If you’re new to reading this blog, you might not already be aware of my efforts to [develop end-to-end encryption for ActivityPub-based software](https://soatok.blog/2024/09/13/e2ee-for-the-fediverse-update-were-going-post-quantum/). It’s worth being aware of before you continue to read this blog post.

> To be very, very clear, this is work I’m doing **independent of the W3C** or any other standards organization and/or funding source (and they have [their own ideas about how to approach it](https://forum.summerofprotocols.com/t/pig-end-to-end-encryption-in-activitypub/440)).
>
> Really, I’m doing my own thing and releasing my designs under a public domain-equivalent license so anyone (including the W3C grant awardees) can pick it up and use it, if they see fit.
>
> But the work I’m doing has no official standing and is not representative of anyone (except maybe a lot of other furries interested in technology). They have, emphatically, never endorsed anything I’m doing. I have not talked with any of them about my ideas, nor has my name come up in any of their meeting notes.
>
> My background is in applied cryptography and software security assessments, so I have strong opinions about how such software should be developed.
>
> I’m being very up-front about this because I don’t want anyone to mistake my ideas for anything “official”.

## Why spend your time on that?

My end goal is pretty straightforward.

Before Musk took it over, Twitter was wonderful for queer people. I’ve even heard it described as the most successful dating platform for the LGBTQIA+ community.

These days, it’s full of Nazis and people who think the ideal version of “free speech” means not being allowed to say the word “cisgender.” But I repeat myself.

The typical threat model for Twitter was: You have to trust the person you’re talking with, and the Twitter corporation, to keep your conversations (or nudes, if we’re being frank about it) private.

With the Fediverse, things are a little more complicated. Instance operators also have access to the plaintext versions of any Direct Messages between you and other participants.

And maybe you trust your instance operator… but do you trust your friends’? And do they trust yours?

If implemented securely, end-to-end encryption saves you from having to care about this injection of additional threat actors to consider.

If not implemented securely, it’s little more than security theater and should be ridiculed loudly.

So it’s natural and obvious for a person with my particular interests and skills to want to solve this problem.

## Technological Decisions

When I started this project, I separated the end goal into 4 separate components:

1. Client-side secret key management.
2. Federated public-key infrastructure.
3. Shared key agreement for group messaging.
4. The actual bulk encryption techniques.

A lot of hobbyist projects over-index on the fourth component, rather than the actual hard problems. This is why so many doomed projects start with PGP, or implement weird “cipher cascades” to hedge against AES getting broken.

In reality, every component matters for the security of the whole system, but the bulk encryption is boring. It’s the well-tread path of any cryptosystem. The significantly harder parts are key management.

### Political Decisions

Let’s not mince words: How you implement key management is inherently a political decision.

If that sounds counter-intuitive, meditate on this bit of wisdom for a while:

> Repeat after me: all technical problems of sufficient scope or impact are actually political problems first.
>
> [Eleanor Saitta](https://infosec.exchange/%40dymaxion/109344795644687902)

Many projects, when confronted with the complexity of key management, are perfectly happy with “just write private keys to disk” or “put blind trust in AWS KMS.”

Or, more directly: “YOLO.”

With my Fediverse E2EE project, I wanted to minimize the amount of trust you have to place in others. (Especially, minimize the trust needed in Soatok!)

### How Decisions Flow

Client-side secrets are the most visible area of risk to end users. Backing up and managing their own credentials, recovering from failure modes, [the Mud Puddle test](https://blog.cryptographyengineering.com/2012/04/05/icloud-who-holds-key/), etc.

Once each participant has secret keys managed (1), they can provide public keys to each other.

Public-key infrastructure (2) is how you decide trust relationships between parties. We’re operating in a federated environment, and want to minimize the amount of unchecked “authority” anyone has, so that complicates matters. But, if it wasn’t challenging, it would already be solved.

Once you’ve figured out a trust mechanism to tie a public key to an identity, you can try to agree on a shared symmetric key securely, even over an untrusted channel.

Key agreement for group messaging (3) is how you decide which shared key to use, and when, and who has access to this key and for how long.

And from there, you can actually encrypt shit (4).

It doesn’t really matter [how much you boil the ocean on mitigating hypothetical weaknesses in AES](https://github.com/keybase/triplesec) if an adversary can muck with your key management.

Thus, it should hopefully be reasonable to divide the work up in this fashion.

But there is a fifth component; one that I am not qualified to comment on:

**User experience.**

The final deliverable for my participation in this project will be software libraries (and any necessary patches to server software) to facilitate secure end-to-end encryption between Fediverse users.

As for what that experience looks like? How it’s presented visually? What accessibility features are used, and how? How elements are organized and in what order they are displayed? Any quality-of-life design decisions that delight users and avoid dark patterns?

Yeah, sorry, I’m totally out of my depth here. That’s not my domain.

I will do my damnedest to not make security decisions that are inherently onerous towards making usable software.

(After all, [security at the cost of usability comes at the cost of security](https://security.stackexchange.com/a/6116).)

But I can’t promise that the experience will be totally seamless for everyone, all the time.

## Lacking Ambition?

One of the things that’s been bothering me, as I work on out the finer details about this end-to-end encryption project, is that it seems to lack ambition.

Sure, I can talk your ear off for hours about the ins and outs of implementing end-to-end encryption securely, but we already have end-to-end encryption apps. [So](https://soatok.blog/2024/08/14/security-issues-in-matrixs-olm-library/) [many](https://soatok.blog/2021/11/05/threema-three-strikes-youre-out/) [private](https://soatok.blog/2024/08/04/against-xmppomemo/) [messengers](https://soatok.blog/2024/07/31/what-does-it-mean-to-be-a-signal-competitor/).

How does “you can now ha...