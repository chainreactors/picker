---
title: Imagining Private Airspaces for Bluesky
url: https://soatok.blog/2024/11/29/imagining-private-airspaces-for-bluesky/
source: Dhole Moments
date: 2024-11-30
fetch_date: 2025-10-06T19:15:57.178927
---

# Imagining Private Airspaces for Bluesky

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

[(Anti-)Social Media](https://soatok.blog/category/social-media/) [Cryptography](https://soatok.blog/category/cryptography/)

# Imagining Private Airspaces for Bluesky

* Post author

  By [Soatok](https://soatok.blog/author/soatok/)
* Post date

  [November 29, 2024](https://soatok.blog/2024/11/29/imagining-private-airspaces-for-bluesky/)

![Imagining Private Airspaces for Bluesky](https://i0.wp.com/soatok.blog/wp-content/uploads/2024/11/BlogHeader-2024-Bluesky-Private-Airspace.png?fit=1200%2C675&ssl=1)

Recently, I shared [my thoughts on the Twitter Exodus](https://soatok.blog/2024/11/19/some-thoughts-on-the-twitter-mass-exodus/). The short of that post is: Even though I’m quite happy on the Fediverse, I think the best outcome is for Bluesky to “win” the popularity contest today. It’s also in a good position to do so: People yearning for “old Twitter” find Bluesky comfortable. (Read the linked post if you’re curious *why* I think these things.)

Everything posted on Bluesky is public, due to architectural decisions they made early in their design. Bluesky is [currently centralized, though a “credible exit” is possible](https://dustycloud.org/blog/how-decentralized-is-bluesky/). I highly recommend reading the linked article before continuing to read my thoughts here.

Earlier this year, Bluesky announced [several possible items on their Protocol Roadmap](https://docs.bsky.app/blog/2024-protocol-roadmap#on-the-horizon). Today, I’d like to look at two of the items on the horizon (Protocol-Native DMs; Limited Audience (Non-Public) Content) and explore ways the Bluesky developers could implement these without significantly changing their architecture.

Instead, we can use cryptography to satisfy both use cases (although they will almost certainly have different key management requirements). If that sounds surprising to you, I promise I will explain my reasoning for this statement.

The organization of this blog post will be as follows: First, I’ll briefly [recap some of my prior and ongoing work](#author-work) to build end-to-end encryption for direct messages on the Fediverse. Then, I’ll introduce [the cryptographic algorithms and protocols relevant to our discussion](#basics). With the basics settled, we can explore [how these protocols can be used to satisfy the use cases for Bluesky users](#private-airspaces). Finally, I’ll discuss a few considerations for [building atop this work to enable use cases and small business opportunities](#wild-blue-yonder) for the Bluesky community.

## The Author and His Work

Due to the nature of what I’m discussing today, it’s highly likely that this post will be many people’s first introduction to my blog, and to me. So I feel a brief introduction is warranted.

> Feel free to [skip this section](#basics) if you don’t care.

**Soatok Dreamseeker** is the name of my fursona, and my pen name for this blog, *Dhole Moments* (the first word being pronounced like “dole”, which refers to [a species of wild canid](https://en.wikipedia.org/wiki/Dhole)).

Most of my blog posts include some furry art between large sections of text, as this website is a furry blog first and foremost. Sometimes I write about technical topics (mostly software security and applied cryptography), which inspires people to share my writing on message boards and leads to some downright exhausting comment threads.

I’m only going to include one piece of furry art in this post (aside from the header image), but if you read anything else on my blog, be prepared to see much more.

(None of the art on this website is adult-oriented or not-safe-for-work by any reasonable person’s measure.)

Behold!

![OwO sticker](https://i0.wp.com/soatok.blog/wp-content/uploads/2020/09/soatoktelegrams2020-06.png?resize=512%2C512&ssl=1)

[CMYKat](https://cmykatgraphics.carrd.co/)

### Relevant Prior and Ongoing Work

In 2022, after Elon Musk bought Twitter, I moved to the Fediverse and was [unimpressed with the lack of progress on building end-to-end encryption (E2EE) for direct messages](https://soatok.blog/2022/11/22/towards-end-to-end-encryption-for-direct-messages-in-the-fediverse/), so decided to take matters into my own paws.

The biggest challenge for deploying E2EE in such an environment is a mix of key management and trust. After puzzling over this for a while, I decided to focus on a tangential concern: [Federated Key Transparency](https://soatok.blog/2024/06/06/towards-federated-key-transparency).

In the coming months, I plan to tag v0.1.0 of my proposed [specification for Public Key Directory software](https://github.com/fedi-e2ee/public-key-directory-specification), build a reference implementation, and then shift gears back to E2EE for the Fediverse (for which I have also [decided to use post-quantum KEMs](https://soatok.blog/2024/09/13/e2ee-for-the-fediverse-update-were-going-post-quantum/) in the initial version, rather than a later update).

Separate from all this, I have written [a lot about applied cryptography](https://soatok.blog/category/cryptography/) over the years. Nearly half of the posts on this website involve it at some point.

I don’t really like talking about my professional life (and, barring [one exception](https://soatok.blog/2023/10/02/return-to-office-is-bullshit-and-everyone-knows-it/) in this blog’s history, I haven’t). The main purpose of this blog is for me to have fun. Sometimes my writing helps people understand new or complex ideas, and I’m always delighted to hear when it does.

This is all to say: I’m deeply familiar with the relevant problem space and have been involved in it for years now.

However, like all mortals, I do occasionally make mistakes; sometimes, very embarrassing ones. You should always ask your favorite security experts to fact-check anything I write before you trust my word on any topic.

I also have no official standing or relationship with Bluesky, the Fediverse, or any other project of note.

## Cryptography Basics

This section is intended to make the overall blog post more accessible to a wider and less technical audience.

If you’re already familiar with the basic cryptographic algorithms and protocols, the next section about [how Bluesky could use them](#private-airspaces) is where the juicy stuff begins.

If you’d like to go further in learning cryptography, I recommend *[So you want to be a cryptographer?](https://gotchas.salusa.dev/GettingStarted.html)* to begin your journey.

### Algorithms

#### Hash Functions

Hash functions transform arbitrary-length input messages into a fixed-length output. They are a handy building block for cryptography designs, but programmers [often use them poorly](https://soatok.blog/2021/08/24/programmers-dont-understand-hash-functions/).

A good, secure cryptographic hash function, such as BLAKE3, has a few important properties:

**It’s a trapdoor.** If you know the input, it is trivial to calculate the output of a hash function. Conversely, if you only know the output, it should be computationally infeasible to find an input that produces the same value. (Succeeding at this is called a “preimage attack”.)

**It’s collision-resistant**. Finding two different inputs that produce the same hash should be [quantifiably difficult](https://soatok.blog/2024/07/01/blowing-out-the-candles-on-the-birthday-bound/). The emphasis here on “two different inputs” cannot be understated: If you can produce [the same input from multiple code paths](https://soatok.blog/2021/07/30/canonicalization-attacks-again...