---
title: Hell Is Overconfident Developers Writing Encryption Code
url: https://soatok.blog/2025/01/31/hell-is-overconfident-developers-writing-encryption-code/
source: Dhole Moments
date: 2025-02-02
fetch_date: 2025-10-06T20:37:51.290882
---

# Hell Is Overconfident Developers Writing Encryption Code

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

[Cryptography](https://soatok.blog/category/cryptography/) [Open Source](https://soatok.blog/category/technology/open-source/) [Security Community](https://soatok.blog/category/technology/software-security/security-community/) [Security Industry](https://soatok.blog/category/technology/software-security/security-industry/)

# Hell Is Overconfident Developers Writing Encryption Code

* Post author

  By [Soatok](https://soatok.blog/author/soatok/)
* Post date

  [January 31, 2025](https://soatok.blog/2025/01/31/hell-is-overconfident-developers-writing-encryption-code/)

![Hell Is Overconfident Developers Writing Encryption Code](https://i0.wp.com/soatok.blog/wp-content/uploads/2025/01/BlogHeader-2025-Hell.png?fit=1200%2C675&ssl=1)

Overconfident developers that choose to write their own cryptography code have plagued the information security industry since before it was *even an industry*.

This in and of itself isn’t inherently a bad thing, despite the infosec truisms about *never doing exactly that*. Writing crypto code (but not deploying or publishing it!) is [an important first step to understanding the algorithms](https://www.cryptofails.com/post/75204435608/write-crypto-code-dont-publish-it).

> **EDIT:** If you haven’t already read the article I linked just now, please stop and do so before continuing.
>
> Quite a few people have posted angry responses to a different argument I’m *not even making here* because they seem to have missed this prominently placed hyperlink, and consequently assumed a different stance than the one I’m actually taking.

One trend I’ve noticed (as I [recently noted about Session](https://soatok.blog/2025/01/20/session-round-2/#:~:text=On%20their%20FAQs%20page%2C%20Session%E2%80%99s%20response%20to%20%E2%80%9Care%20you%20rolling%20your%20own%20cryptography%3F%E2%80%9D%20can%20be%20abbreviated%20to%2C%20%E2%80%9CNo%2C%20we%20use%20libsodium!%E2%80%9D)) is developers incorrectly insisting that they aren’t rolling their own crypto because they use a lower-level cryptography library.

> “If you want a picture of the future, imagine developers rolling their own crypto–forever.”
>
> –if George Orwell was an applied cryptography expert

This misdeed isn’t limited to dubious apps that fork end-to-end encrypted messengers to strip off forward secrecy.

## Startup-Grade Cryptography

Feast your eyes on, *[How we share secrets at a fully-remote startup](https://ghostarchive.org/archive/taW5z)*–a January 2025 reprint of [an earlier 2024 blog post](https://web.archive.org/web/20240716164008/https%3A//www.getgrist.com/blog/how-we-share-secrets-at-a-fully-remote-startup/) about the same cryptography code that originally [fell victim to Bleichenbacher’s 1998 Padding Oracle Attack](https://ghostarchive.org/archive/h8Ylr) (which is possibly the oldest pitfall in real-world cryptography, and one of the reasons why cryptographers say to [stop using RSA](https://blog.trailofbits.com/2019/07/08/fuck-rsa/)).

And, **let me be very clear on this**, the reason I want you to feast your eyes on this is ***NOT*** put this person on blast.

They are by far not the first person to roll their own cryptography. They aren’t even the first one I’ve seen *this week*.

But they *were* kind enough to walk through their code and share their thoughts about what they wrote, and I think that sheds a lot of insight into how people think about cryptographic code.

The blog post in question starts off with a bit of humility and echoes the common refrain you’ll hear from security experts:

> **Don’t roll your own security**
>
> Like many hard areas of human knowledge, security/cryptography is one where the more you know, the more you realize you don’t know.
>
> [How we share secrets at a fully-remote startup](https://ghostarchive.org/archive/taW5z)

And that’s good advice!

But if you scroll down a bit further, past the code and explanation, you’ll see this too:

> **Did we roll our own security?**
>
> No, not really. Our solution uses and trusts a lot of cryptography code from good sources: Node.js, its crypto module, and the [OpenSSL](https://www.openssl.org/) library it’s based on. These are respected, well-maintained, commonly-used open-source tools, which get plenty of attention from security researchers.
>
> [How we share secrets at a fully-remote startup](https://ghostarchive.org/archive/taW5z)

Hey, this argument has [a very familiar structure](https://web.archive.org/web/20250102225433/https%3A//getsession.org/faq#libsodium), doesn’t it?

Despite the author’s awareness of “rolling your own” being undesirable, they somehow managed to convince themselves that they weren’t doing exactly that.

And that’s what I find so *interesting* about this blog post in particular.

The code in question is [just about what you’d expect](https://github.com/gristlabs/secrets.js/issues/2) from a blog post with this sort of cognitive dissonance:

* It first tries to [encrypt keys directly with RSA](https://soatok.blog/2021/01/20/please-stop-encrypting-with-rsa-directly/).
* If it fails, it falls back to encrypting a *random symmetric key* with RSA, and then using that key to encrypt the message… with [unauthenticated AES-CBC](https://www.nccgroup.com/us/research-blog/cryptopals-exploiting-cbc-padding-oracles/).

Oh, and did I mention that other folks tried to talk the author down from rolling their own implementation [the first time around](https://lobste.rs/s/1nj3wf/how_we_share_secrets_at_fully_remote) (i.e., six months ago)?

> **Update (2025-02-02):** The author has [updated their code to only use RSA for key-wrapping and switch to AES-GCM](https://github.com/gristlabs/secrets.js/pull/4).
>
> This is a material improvement over what they were doing before, so this particular example does have a happy ending.

## Countless Stories Untold

As tempting as it may be to dunk on this code or the accompanying blog post, at least they’re being open and transparent.

> Care to wager how many people make similar design mistakes and ship them to production every week, without *any* oversight from the security community?

This is the part of the blog post where I could tell any of a dozen stories that would fit very elegantly as a complementary example to that blog post from a startup co-CEO.

Unfortunately, all of my best work is done under NDA.

![Contemplating, Thinking Sticker](https://i0.wp.com/soatok.blog/wp-content/uploads/2020/09/soatoktelegrams2020-12.png?resize=512%2C512&ssl=1)

Art: [CMYKat](https://cmykatgraphics.carrd.co/)

So, I can’t actually give you any specifics, even if I wanted to. The conversations I’ve experienced over the years would give most infosec neophytes *chills*. The only silver lining is that I, and my peers, were successful in convincing the developers in question to correct their course.

Here are a few highlights to chew on:

* I’ve seen people use `md5($password)` as their key derivation function for libsodium.
* I’ve seen people encrypt fields in a database, and then store the decryption key right next to the ciphertext. And then, in a stunning display of brilliance, they wrote decryption logic in SQL so they could query their database over encrypted fields.
* At least once, when reviewing an end-to-end encryption project that implemented cryptography in JavaScript intended to run in the web browser, my question of “how do you know which public key to trust?” was answered with something shaped like, “Oh, we just store those in MySQL and fetch them from the server.”

T...