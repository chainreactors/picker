---
title: Practical Collision Attack Against Long Key IDs in PGP
url: https://soatok.blog/2026/01/07/practical-collision-attack-against-long-key-ids-in-pgp/
source: Dhole Moments
date: 2026-01-07
fetch_date: 2026-01-08T03:29:17.624004
---

# Practical Collision Attack Against Long Key IDs in PGP

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

[(Anti-)Social Media](https://soatok.blog/category/social-media/) [Cryptography](https://soatok.blog/category/cryptography/) [Vulnerability](https://soatok.blog/category/technology/software-security/vulnerability/)

# Practical Collision Attack Against Long Key IDs in PGP

* Post author

  By [Soatok](https://soatok.blog/author/soatok/)
* Post date

  [January 7, 2026](https://soatok.blog/2026/01/07/practical-collision-attack-against-long-key-ids-in-pgp/)

![Practical Collision Attack Against Long Key IDs in PGP](https://i0.wp.com/soatok.blog/wp-content/uploads/2026/01/BlogHeader-2026-PGP-LongKeyIDs.png?fit=1200%2C675&ssl=1)

In response to the GPG.Fail attacks, a Hacker News user made this claim about the 64-bit “Long Key IDs” used by OpenPGP and GnuPG, while responding to an answer I gave to someone else’s question:

> OK, to be clear, I am specifically contending that a key fingerprint does *not* include collisions. My proof is empirical, that **no one has come up with an attack on 64 bit PGP key fingerprints.**
>
> [Hacker News Thread](https://news.ycombinator.com/item?id=46415279#46419711)

This was a stupid thing to say to me, of all people.

![Blep Tongue Sticker](https://i0.wp.com/soatok.blog/wp-content/uploads/2020/09/soatoktelegrams2020-13.png?resize=512%2C512&ssl=1)

[CMYKat](https://cmykatgraphics.carrd.co/)

And thus:

## Proof of Concept

Save this file as pubkey1.asc:

```
-----BEGIN PGP PUBLIC KEY BLOCK-----

xjQEZVQvDBYKCSsGAQQB2kcPAQEHQPlChumZ771BEWmLgtsrm2QUf3YE4xSbpiRr
wGelIDITzShDb2xsaXNpb24gS2V5IDEgPGtleTFAY29sbGlzaW9uLmV4YW1wbGU+
=8+QC
-----END PGP PUBLIC KEY BLOCK-----
```

Save this file as pubkey2.asc:

```
-----BEGIN PGP PUBLIC KEY BLOCK-----

xjQEZVRJOxYKCSsGAQQB2kcPAQEHQE5YOa8jzfZ1IAUmqaxKvrGdq3RJWQ1QBfh4
9ffaD/S3zShDb2xsaXNpb24gS2V5IDIgPGtleTJAY29sbGlzaW9uLmV4YW1wbGU+
=Ah4C
-----END PGP PUBLIC KEY BLOCK-----
```

Run the following commands, and despair:

```
gpg --list-packets pubkey1.asc | grep keyid
gpg --list-packets pubkey2.asc | grep keyid
```

You will observe the following:

```
$ gpg --list-packets pubkey1.asc | grep keyid
        keyid: 948F9326DD647C78
$ gpg --list-packets pubkey2.asc | grep keyid
        keyid: 948F9326DD647C78
```

However, the public keys and full fingerprints are different for each public key.

![galaxy brain sticker](https://i0.wp.com/soatok.blog/wp-content/uploads/2020/08/soatoktelegrams2020-01.png?resize=512%2C512&ssl=1)

[CMYKat](https://cmykatgraphics.carrd.co/)

## What Is Actually Happening?

This was the result of a Birthday attack against the 64-bit size of the “Long Key ID” feature of OpenPGP.

I’ve written about [the Birthday Bound](https://soatok.blog/2024/07/01/blowing-out-the-candles-on-the-birthday-bound/) before. But generally:

* If you have ![2^{n}](https://s0.wp.com/latex.php?latex=2%5E%7Bn%7D&bg=0a0a0a&fg=f0f0f0&s=3&c=20201002) possible outputs from a function…
* And the input domain is larger than the output domain…
* And you want to generate two distinct inputs that produce the same output (a collision attack)…

…then you only need about ![\sqrt{2^{n}}](https://s0.wp.com/latex.php?latex=%5Csqrt%7B2%5E%7Bn%7D%7D&bg=0a0a0a&fg=f0f0f0&s=3&c=20201002) or ![2^{n/2}](https://s0.wp.com/latex.php?latex=2%5E%7Bn%2F2%7D&bg=0a0a0a&fg=f0f0f0&s=3&c=20201002) inputs before your collision probability approaches 50%.

Since the output space of a Long Key ID is 64 bits, there are ![2^{64}](https://s0.wp.com/latex.php?latex=2%5E%7B64%7D&bg=0a0a0a&fg=f0f0f0&s=3&c=20201002) possible Long Key IDs. However, you expect a collision with about 50% probability after only ![2^{32}](https://s0.wp.com/latex.php?latex=2%5E%7B32%7D&bg=0a0a0a&fg=f0f0f0&s=3&c=20201002) Long Key IDs are generated.

This is a widely known fact about cryptography, and the crux of the attack.

EDIT: Apparently it was also done before. [In 2019](https://nullprogram.com/blog/2019/07/22/).

![Drakeposting Yes Sticker](https://i0.wp.com/soatok.blog/wp-content/uploads/2021/04/soatoktelegramswave3-08.png?resize=512%2C512&ssl=1)

[CMYKat](https://cmykatgraphics.carrd.co/)

### Methodology

The full attack took about 3 days on a laptop, running in the background while I was doing other work.

This is within an order of magnitude of the same runtime [needed to break Rainbow](https://eprint.iacr.org/2022/214), for comparison.

Because it was a memory-constrained device, the strategy looked roughly like this:

1. Generate ![2^{16}](https://s0.wp.com/latex.php?latex=2%5E%7B16%7D&bg=0a0a0a&fg=f0f0f0&s=3&c=20201002) keypairs. (~2 seconds)
2. For each keypair, iterate over a range of ![2^{17}](https://s0.wp.com/latex.php?latex=2%5E%7B17%7D&bg=0a0a0a&fg=f0f0f0&s=3&c=20201002) UNIX timestamps.
3. Compute the Key ID for each (public key, timestamp).
4. Write the Key IDs, index pointing to which keypair, and timestamps to a file (~15 hours).
5. Use the `sort` command on this enormous file (~57 hours).
   * This probably took so long because my laptop goes into sleep mode when I’m not using it, so at least 20 hours of that can be written off as “nap time for my computer”.
6. Read through this file from start to until a colliding key ID was found (~30 minutes).

I could have done it faster if I felt like using a cloud provider, but I didn’t want to put too much work into this.

Virtually no cryptography expert worth listening to will be surprised by this.

#### “What impact does colliding Key IDs give an attacker?”

To head off any questions like this, we need to be clear that a successful collision *is, in and of itself, a successful attack*. This is cryptography. None of us can weasel-word our way out of that fact.

But it’s still worth entertaining: what can you do with such a colliding keypair in practice?

Let’s say I was the maintainer of a popular open source package and got a bunch of Linux kernel devs to sign pubkey1.asc instead of publishing it here.

If I decided to go rogue in the future, I could replace the public key that other people will download with pubkey2.asc. Especially if I secretly control the PGP key server they’re using.

Users following instructions that mean to verify the Long Key ID instead of the full fingerprint will see that pubkey2.asc checks out, and then install backdoored software. [All their apes, gone](https://www.vice.com/en/article/all-my-apes-gone-nft-theft-victims-beg-for-centralized-saviors/)!

If I’m ever confronted about it (especially by the folks that signed my actual public key), I could point out that my private key was never compromised, and claim the attacker *clearly* did a “preimage” attack on my Long Key ID. Thus, there’s plausible deniability in the absence of other forensics.

Especially since PGP users [advise each other to check the Long Key ID](https://web.archive.org/web/20250427164953/https%3A//security.stackexchange.com/questions/74009/what-is-an-openpgp-key-id-collision/74010#74010). ([Alternative archive](https://archive.is/IFMvz).)

This kind of attack has to be setup in advance. Collision attacks aren’t preimage attacks. But it’s a realistic exploit scenario.

![Soatok typing on a laptlop like a stereotypical hacker](https://i0.wp.com/soatok.blog/wp-content/uploads/2020/04/soatok_stickerpack-hacker-1.png?resize=512%2C512&ssl=1)

[CMYKat](https://cmykatgraphics.carrd.co/)

### Bonus: The Private Keys

private1.asc

```
-----BEGIN PGP PRIVATE KEY BLOCK-----
xVkEZVQvDBYKCSsGAQQB2kcPAQEHQPlChumZ771BEWmLgtsrm2QUf3YE4xSbpiRr
wGelIDITAAEAX7B7GVQBGE9VxroU6ilaSYp7D0QrZFRgbLDBM+uVTxEMis0dVGVz
dCBLZXkgMSA8a2V5M...