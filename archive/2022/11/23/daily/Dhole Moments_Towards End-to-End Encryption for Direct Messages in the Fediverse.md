---
title: Towards End-to-End Encryption for Direct Messages in the Fediverse
url: https://soatok.blog/2022/11/22/towards-end-to-end-encryption-for-direct-messages-in-the-fediverse/
source: Dhole Moments
date: 2022-11-23
fetch_date: 2025-10-03T23:30:05.438570
---

# Towards End-to-End Encryption for Direct Messages in the Fediverse

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

[(Anti-)Social Media](https://soatok.blog/category/social-media/) [Cryptography](https://soatok.blog/category/cryptography/) [Fediverse E2EE Project](https://soatok.blog/category/technology/open-source/fediverse-e2ee-project/) [Open Source](https://soatok.blog/category/technology/open-source/)

# Towards End-to-End Encryption for Direct Messages in the Fediverse

* Post author

  By [Soatok](https://soatok.blog/author/soatok/)
* Post date

  [November 22, 2022](https://soatok.blog/2022/11/22/towards-end-to-end-encryption-for-direct-messages-in-the-fediverse/)
* [8 Comments on Towards End-to-End Encryption for Direct Messages in the Fediverse](https://soatok.blog/2022/11/22/towards-end-to-end-encryption-for-direct-messages-in-the-fediverse/#comments)

![Towards End-to-End Encryption for Direct Messages in the Fediverse](https://i0.wp.com/soatok.blog/wp-content/uploads/2022/11/BlogHeader-ActivityPub-E2EE.png?fit=1200%2C675&ssl=1)

**Update (2024-06-06):** There is [an update on this project](https://soatok.blog/2024/06/06/towards-federated-key-transparency/).

---

As [Twitter’s new management continues to nosedive the platform directly into the ground](https://soatok.blog/2022/11/07/contemplating-the-future/), many people are migrating to what seem like drop-in alternatives; i.e. Cohost and Mastodon. Some are even considering new platforms that none of us have heard of before (one is called “Hive”).

Needless to say, these are somewhat chaotic times.

One topic that has come up several times in the past few days, to the astonishment of many new Mastodon users, is that Direct Messages between users aren’t end-to-end encrypted.

And while that fact makes Mastodon DMs no less safe than Twitter DMs have been this whole time, there is clearly a lot of value and demand in deploying end-to-end encryption for ActivityPub (the protocol that Mastodon and other Fediverse software uses to communicate).

However, given that Melon Husk apparently wants to hurriedly ship end-to-end encryption (E2EE) in Twitter, in some vain attempt to compete with Signal, I took it upon myself to kickstart the E2EE effort for the Fediverse.

> Twitter DMs should have end to end encryption like Signal, so no one can spy on or hack your messages
>
> — Elon Musk (@elonmusk) [April 28, 2022](https://twitter.com/elonmusk/status/1519469891455234048?ref_src=twsrc%5Etfw)

[Archived](https://web.archive.org/web/20220428001404/https%3A//twitter.com/elonmusk/status/1519469891455234048)

So I’d like to share my thoughts about E2EE, how to design such a system from the ground up, and why the direction Twitter is heading looks to be security theater rather than serious cryptographic engineering.

If you’re not interested in those things, but are interested in what I’m proposing for the Fediverse, head on over to [the GitHub repository hosting my work-in-progress proposal draft](https://github.com/soatok/mastodon-e2ee-specification) as I continue to develop it.

## How to Quickly Build E2EE

If one were feeling particularly cavalier about your E2EE designs, they could just generate then dump public keys through a server they control, pass between users, and have them encrypt client-side. Over and done. Check that box.

Every public key would be ephemeral and implicitly trusted, and the threat model would mostly be, “I don’t want to deal with law enforcement data requests.”

![I pretend I do not see it](https://i0.wp.com/soatok.blog/wp-content/uploads/2022/11/donotseeit.png?resize=680%2C664&ssl=1)

Hell, I’ve previously written [an incremental blog post to teach developers about E2EE](https://soatok.blog/2020/11/14/going-bark-a-furrys-guide-to-end-to-end-encryption/) that begins with this sort of design. Encrypt first, ratchet second, manage trust relationships on public keys last.

If you’re catering to a slightly tech-savvy audience, you might throw in SHA256(pk1 + pk2) -> hex2dec() and call it a fingerprint / safety number / “conversation key” and not think further about this problem.

> Look, technical users can verify out-of-band that they’re not being machine-in-the-middle attacked by our service.
>
> An absolute fool who thinks most people will ever do this

From what I’ve gathered, this appears to be the direction that Twitter is going.

<https://twitter.com/wongmjane/status/1592831263182028800>

[Archived](https://web.archive.org/web/20221122041844/https%3A//twitter.com/wongmjane/status/1592831263182028800)

Now, if you’re building E2EE into a small hobby app that you developed for fun (say: a World of Warcraft addon for erotic roleplay chat), **this is probably good enough**.

If you’re building a private messaging feature that is intended to “superset Signal” for hundreds of millions of people, this is woefully inadequate.

> The goal of Twitter DMs is to superset Signal
>
> — Elon Musk (@elonmusk) [November 9, 2022](https://twitter.com/elonmusk/status/1590426255018848256?ref_src=twsrc%5Etfw)

[Archived](https://web.archive.org/web/20221109231306/https%3A//twitter.com/elonmusk/status/1590426255018848256)

![Facepaw](https://i0.wp.com/soatok.blog/wp-content/uploads/2020/04/soatok_stickerpack-facepaw.png?resize=512%2C512&ssl=1)

Art: [CMYKat](https://cmykatgraphics.carrd.co/)

If this is, indeed, the direction Musk is pushing what’s left of Twitter’s engineering staff, here is a brief list of problems with what they’re doing.

1. **Twitter Web**. How do you access your E2EE DMs after opening Twitter in your web browser on a desktop computer?
   * If you can, how do you know twitter.com isn’t including malicious JavaScript to snarf up your secret keys on behalf of law enforcement or a nation state with a poor human rights record?
   * If you can, how are secret keys managed across devices?
   * If you use a password to derive a secret key, how do you prevent weak, guessable, or reused passwords from weakening the security of the users’ keys?
   * If you cannot, how do users decide which is their primary device? What if that device gets lost, stolen, or damaged?
2. **Authenticity.** How do you reason about the person you’re talking with?
3. **Forward Secrecy**. If your secret key is compromised today, can you recover from this situation? How will your conversation participants reason about your new Conversation Key?
4. **Multi-Party E2EE**. If a user wants to have a three-way E2EE DM with the other members of their long-distance polycule, does Twitter enable that?
   * How are media files encrypted in a group setting? If you fuck this up, you [end up like Threema](https://soatok.blog/2021/11/05/threema-three-strikes-youre-out/).
   * Is your group key agreement protocol vulnerable to [insider attacks](https://eprint.iacr.org/2020/752)?
5. **Cryptography Implementations**.
   * What does the KEM look like? If you’re using ECC, which curve? Is a common library being used in all devices?
   * How are you deriving keys? Are you just [using the result of an elliptic curve (scalar x point) multiplication directly without hashing first](https://crypto.stackexchange.com/a/67609)?
6. **Independent Third-Party Review.**
   * Who is reviewing your protocol designs?
   * Who is reviewing your cryptographic primitives?
   * Who is reviewing the code that interacts with E2EE?
   * Is there even a penetration test before the feature launches?

As more details about Twitter’s approach to E2EE DMs come out, I’m sure the above list will be expanded with even more questions and concerns.

My hunch is that they’ll reuse [liblithium...