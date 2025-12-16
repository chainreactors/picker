---
title: Announcing Key Transparency for the Fediverse
url: https://soatok.blog/2025/12/15/announcing-key-transparency-fediverse/
source: Dhole Moments
date: 2025-12-15
fetch_date: 2025-12-16T03:23:11.657089
---

# Announcing Key Transparency for the Fediverse

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

# Announcing Key Transparency for the Fediverse

* Post author

  By [Soatok](https://soatok.blog/author/soatok/)
* Post date

  [December 15, 2025](https://soatok.blog/2025/12/15/announcing-key-transparency-fediverse/)

![Announcing Key Transparency for the Fediverse](https://i0.wp.com/soatok.blog/wp-content/uploads/2025/11/BlogHeader-2025-FediE2EE-Update.png?fit=1200%2C675&ssl=1)

I’m pleased to announce the immediate availability of a **reference implementation** for the Public Key Directory server.

This software implements [the Key Transparency specification](https://github.com/fedi-e2ee/public-key-directory-specification) I’ve been working on [since last year](https://soatok.blog/2024/06/06/towards-federated-key-transparency/), and is an important stepping stone towards secure end-to-end encryption for the Fediverse.

You can find the software publicly available on GitHub:

* PHP Server software:
  [**http://github.com/fedi-e2ee/pkd-server-php**](http://github.com/fedi-e2ee/pkd-server-php)
* PHP SDK (client-side):
  <https://github.com/fedi-e2ee/pkd-client-php>

To get started with the project, start with the pkd-server-php repository (linked above). Some quick commands:

```
# Clone the source code
git clone https://github.com/fedi-e2ee/pkd-server-php.git

# Install dependencies
cd pkd-server-php
composer install --no-dev

# Setup and configure
cp config/database.php config/local/database.php
vim config/local/database.php # or your favorite editor
cp config/params.php config/local/params.php
vim config/local/params.php # or your favorite editor

# Setup SQL tables
php cmd/init-database.php

# Run locally for dev purposes:
php -S localhost:8080 -t public
```

This represents an important milestone in the overall project!

![Soatok Yay Sticker](https://i0.wp.com/soatok.blog/wp-content/uploads/2024/07/SoatokCheer.png?resize=512%2C379&ssl=1)

Art by [AJ](https://ajlovesdinos.bsky.social)

However, there remains *a lot* of work left to do.

(We’re [only on v0.1.0](https://semver.org/#semantic-versioning-specification-semver) for both projects, after all.)

So, I’d like to outline the road between where we are today, and when you can easily use end-to-end encryption to communicate with your friends on Mastodon and other ActivityPub-enabled software.

But before we get into the technical stuff, the most important question to answer is why anyone should care about any of this.

### Important

**What was released today is still not production-ready.** We’re still on v0.x for all of the software in scope.

There will be bugs!

Some features may need to be reconsidered (which will require future revisions to the specification).

Do not count on any of this software being secure or stable until we tag v1.0.0.

![Soatok heart sticker](https://i0.wp.com/soatok.blog/wp-content/uploads/2020/04/soatok_stickerpack-heart.png?resize=512%2C512&ssl=1)

Art: [CMYKat](https://cmykatgraphics.carrd.co/)

## Why Should I Care About This?

As I’ve discussed [in a previous blog post](https://soatok.blog/2025/09/16/are-you-under-the-influence-the-tail-that-wags-the-dog/), a lot of social media toxicity and online services getting shittier over time share a root cause:

They’re direct consequences of centralized platforms with access to *fuckloads* of sensitive data about people.

Whenever a techie figures this out, they’re quick to embrace decentralized technologies, but these actually have a [pretty awful privacy track record](https://cups.cs.cmu.edu/soups/2006/posters/sheng-poster_abstract.pdf).

I like to pick on [PGP](https://www.latacora.com/blog/2019/07/16/the-pgp-problem/) and [Matrix](https://soatok.blog/2024/08/14/security-issues-in-matrixs-olm-library/), but the Fediverse (including Mastodon) is a good example that doesn’t require technical expertise to grok:

On the Fediverse, DMs (“direct messages”) are not end-to-end encrypted. This means that your instance admin can snoop on your messages if they want. (In fairness, this was also true of DMs for Twitter and BlueSky for [most of](https://web.archive.org/web/20250908122143/https%3A//techcrunch.com/2025/09/05/x-is-now-offering-me-end-to-end-encrypted-chat-you-probably-shouldnt-trust-it-yet/) their history.)

Last year, the W3C decided to [investigate E2EE for ActivityPub](https://github.com/swicg/activitypub-e2ee), which would create a standard for solving this privacy foot-gun for Mastodon and other Fediverse software.

However, key management for the Fediverse was still a very difficult problem to solve.

Until today.

![High Paw (high five) sticker](https://i0.wp.com/soatok.blog/wp-content/uploads/2020/09/soatoktelegrams2020-08.png?resize=512%2C512&ssl=1)

Art: [CMYKat](https://cmykatgraphics.carrd.co/)

## What is Key Transparency?

To understand that, you need to know a *little* bit of cryptography concepts.

Don’t worry, I won’t be throwing any crazy math at you today.

### Public Keys

There’s a special type of cryptography that involves two different numbers (called “keys”): One public, one secret.

Every “secret key” (which, as its name implies, should be kept secret) has a corresponding “public key” (which can be freely shared with the world). The two have some mathematical relationship that lets us do cool things.

If you’re hoping for an intuitive, easy-to-understand explanation for how any of this “secret/public key” magic works without any mathematics, the best I’ve found online uses colors.

<https://www.youtube.com/watch?v=YEBfamv-_do>

(If you need a deeper explanation, I’ll try to come up with one. But for now, just know that “public keys” are intended to be shared publicly, and can be used for lots of things in cryptography.)

Some things that are nice to know about public keys:

* Some algorithms allow you to encrypt a message such that, even if you publish the encrypted message publicly, only the person holding the secret key can ever hope to decrypt it.
* Others allow you to use your secret key produce a “signature” of a message. Then, someone can take your public key, the signature, and your exact message, and prove that you signed it. But (and this is critical) they cannot easily forge new messages and convince others that you signed them.
* You can also do complicated things like build [authenticated key exchanges](https://soatok.blog/2020/04/21/authenticated-key-exchanges/), [asynchronous ratchet trees](https://www.rfc-editor.org/rfc/rfc9420.html), or zero-knowledge proofs.

However, these systems are only secure if **you know which public key to use**, especially if you have an intended recipient in mind.

Knowing which public key is trustworthy turns out to be a much harder problem than even most technologists appreciate.

![Soatok glitching out](https://i0.wp.com/soatok.blog/wp-content/uploads/2023/10/SoatokGlitch.png?resize=512%2C445&ssl=1)

Art by [AJ](https://ajlovesdinos.bsky.social)

### [Public] Key Transparency

Key Transparency is a way to ensure that, given a public key to use for cool cryptography purposes, you can be reasonably sure that it’s related to the specific secret key held by the person you want to communicate with.

How Key Transparency works is simple in concept: Build a protocol that lets everyone publish their public keys to an immutable, append-only ledger called a “transparency log”.

If you want to find the public keys that belong to your friend, you can simply query the trans...