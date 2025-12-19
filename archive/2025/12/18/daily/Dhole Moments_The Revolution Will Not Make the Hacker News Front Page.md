---
title: The Revolution Will Not Make the Hacker News Front Page
url: https://soatok.blog/2025/12/17/the-revolution-will-not-make-the-hacker-news-front-page/
source: Dhole Moments
date: 2025-12-18
fetch_date: 2025-12-19T03:22:33.185253
---

# The Revolution Will Not Make the Hacker News Front Page

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

[Meta-blog](https://soatok.blog/category/meta/)

# The Revolution Will Not Make the Hacker News Front Page

* Post author

  By [Soatok](https://soatok.blog/author/soatok/)
* Post date

  [December 17, 2025](https://soatok.blog/2025/12/17/the-revolution-will-not-make-the-hacker-news-front-page/)

![The Revolution Will Not Make the Hacker News Front Page](https://i0.wp.com/soatok.blog/wp-content/uploads/2025/12/BlogHeader-2025-Boring.png?fit=1200%2C675&ssl=1)

*(with apologies to Gil Scott-Heron)*

If you get all of your important technology news from “content aggregators” like Hacker News, Lobste.rs, and most subreddits, you might be totally unaware of the important but boring infrastructure work happening largely on the Fediverse, indie web, and other less-centralized communities.

**This is no accident.**

The rough consensus of these spaces has been strongly in favor of the sort of centralized tech monopolies, venture capitalists, private equity ghouls, and “innovation” that weakens the position of workers against the wealthy (i.e., most use cases for Large Language Models).

Occasionally they sprinkle in a bit of faux resistance–just enough to be able to pretend they’re counterculture, so they can pretend that Silicon Valley spirit hasn’t been thoroughly sold out to Palantir over the past two decades. That’s why a few “anti-AI” rants will occasionally slip through.

If you’re interested in the substance that underpins this mild rant, I’ve written about [technology that causes massive cultural harm](https://soatok.blog/2025/09/16/are-you-under-the-influence-the-tail-that-wags-the-dog/) recently.

Earlier this week, I [announced](https://soatok.blog/2025/12/15/announcing-key-transparency-fediverse/) the immediate availability of a reference implementation for the Public Key Directory–a project I’ve been working on [since June 2024](https://soatok.blog/2024/06/06/towards-federated-key-transparency/). Hundreds of people shared it on Mastodon and BlueSky. Comparatively, [almost nobody on Hacker News ever saw it](https://news.ycombinator.com/item?id=46275460).

Today, the [COCKTAIL-DKG](https://c2sp.org/cocktail-dkg) specification is now live ([previous blog post](https://soatok.blog/2025/08/27/its-a-cold-day-in-developer-hell-so-i-must-roll-my-own-crypto/)). It’s an early version (v0.1.0), and the reference implementations are still a work-in-progress, and there’s still [a lot of work to do](https://furry.engineer/%40soatok/115737586735883369), but it’s a tangible specification. With [test vectors](https://github.com/C2SP/CCTV/pull/23) (from my hacky implementation that isn’t clean enough to publish)!

Two months ago, I wrote a blog post titled *[The Dreamseeker’s Vision of Tomorrow](https://soatok.blog/2025/10/15/the-dreamseekers-vision-of-tomorrow/)*. In the time since, I’ve gotten two of my three current projects to the next stage of maturity (and the third one was blocked by one of those two).

I have no illusions that the larger tech industry will do anything but collectively shrug at this sort of progress. I’m sure you’ve all heard it before.

> This is boring infrastructure work!
>
> There’s no drama; no scandal. There’s nothing sexy. No one is bleeding. Why would anyone want to read about this?
>
> Hell, why are you even *blogging* instead of making **short-form video content**?
>
> Get with the *times*. The attention economy demands tribute.
>
> Don’t you want to [be important](https://soatok.blog/2024/09/09/doesnt-matter/)? Don’t you want [money](https://soatok.blog/2024/07/02/my-furry-blog-is-not-an-opportunity-to-develop-your-brand/)?
>
> While you’re at it, cut the furry crap; [it’s totally unprofessional](https://soatok.blog/2023/11/17/this-would-be-more-professionally-useful-if-not-for-the-furry-art/).

![](https://i0.wp.com/soatok.blog/wp-content/uploads/2024/08/SoatokNerdRage.png?resize=512%2C376&ssl=1)

Art: [AJ](https://ajlovesdinos.bsky.social)

## 2026 Will Be More Boring Infrastructure Work

While the rest of the Internet descends slowly into [AI-induced mass psychosis](https://psychiatryonline.org/doi/10.1176/appi.pn.2025.10.10.5), I’ve got different plans.

1. Push the [Fediverse Key Transparency project](https://github.com/fedi-e2ee/public-key-directory-specification) closer to v1.0.
2. Begin working on a realistic proposal for end-to-end encryption for ActivityPub-enabled software.
   * I plan on building atop MLS. If your opinion of MLS was tainted by [Evgeny’s disingenuous rant](https://ghostarchive.org/archive/LBbj6), I already wrote [a rebuttal](https://soatok.blog/2025/08/25/barking-up-the-ratchet-tree-mls-is-neither-royal-nor-nude/) earlier this year.
   * W3C-affilited folks are [also planning to build atop MLS](https://swicg.github.io/activitypub-e2ee/mls.html). I’m already talking with them [about Key Transparency](https://github.com/swicg/activitypub-e2ee/issues/35).
3. Improve COCKTAIL-DKG and implement it in several popular languages to make Threshold Signing with FROST easier for teams to develop.
4. Build the next version of FREEON with COCKTAIL-DKG, so [FOSS development teams can have geographic resilience](https://soatok.blog/2025/08/09/improving-geographical-resilience-for-distributed-open-source-teams-with-freeon/) even if one of their team members reside in a nation that goes totally authoritarian.
5. Design tooling to integrate FREEON into other workloads that already support single-secret Ed25519 today.
   * Imagine tying this into SigStore and attestations like [PEP-740](https://peps.python.org/pep-0740/).

None of this work will generate much buzz, but I’m building it because I feel strongly that it needs to exist.

* Fediverse users should be able to have private chats with each other, that not even their instance admins can snoop on.
  + This encryption should be accessible to mere mortals, without sophisticated training or discipline.
* Geographically distributed open source software teams should be able to mitigate the $5 wrench problem.

## AuxData is a little exciting

One thing that I feel is underappreciated about the Key Transparency system I designed is that it’s extensible. That is to say, you can push more than just public keys; you can also publish (and revoke) typed blobs of [“auxiliary data”](https://github.com/fedi-e2ee/public-key-directory-specification/blob/main/Specification.md#auxiliary-data).

If you asked a cryptographer how to enable a workflow where strangers can encrypt a file and send it to you, such that only you can decrypt it, they’ll recommend something like [age](https://github.com/FiloSottile/age). (If they recommend [PGP without you specifically adding it as a constraint](https://soatok.blog/2024/11/15/what-to-use-instead-of-pgp/), they’re a clown.)

But, in this scenario, how does anyone know that they’re using **YOUR** age public key and not the NSA’s? Or [Mossad’s](https://www.usenix.org/system/files/1401_08-12_mickens.pdf)?

Well, if you publish your age public key as AuxData via Key Transparency, you can reason about how long it’s been published and how much verification the transparency log offers. This is [a much stronger notion for baseline trust than trust-on-first-use](https://soatok.blog/2025/12/15/announcing-key-transparency-fediverse/#addendum).

I’m not just building a solution for the Fediverse. I’m building a viable way for developers the world over to build federated trust and transparency that **doesn’t involve cryptocurrency** and all the crap that comes with that crowd.

...