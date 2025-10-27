---
title: What To Use Instead of PGP
url: https://soatok.blog/2024/11/15/what-to-use-instead-of-pgp/
source: Dhole Moments
date: 2024-11-16
fetch_date: 2025-10-06T19:17:19.121324
---

# What To Use Instead of PGP

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

[Cryptography](https://soatok.blog/category/cryptography/) [Open Source](https://soatok.blog/category/technology/open-source/)

# What To Use Instead of PGP

* Post author

  By [Soatok](https://soatok.blog/author/soatok/)
* Post date

  [November 15, 2024](https://soatok.blog/2024/11/15/what-to-use-instead-of-pgp/)

![What To Use Instead of PGP](https://i0.wp.com/soatok.blog/wp-content/uploads/2024/11/BlogHeader-2024-PGP.png?fit=1200%2C675&ssl=1)

It’s been more than five years since [The PGP Problem](https://www.latacora.com/blog/2019/07/16/the-pgp-problem/) was published, and I still hear from people who believe that using PGP (whether GnuPG or another OpenPGP implementation) is a thing they should be doing.

**It isn’t.**

I don’t blame individual Internet users for this confusion. There is a lot of cargo-culting around communication tools in the software community, and the evangelists for the various projects muddy the waters for the rest of us.

![](https://i0.wp.com/soatok.blog/wp-content/uploads/2021/07/neophyte-confused.png?resize=409%2C512&ssl=1)

[Harubaki](https://harubaki.carrd.co/)

The part of the free and open source software community that thinks PGP is just dandy, and therefore evangelize the hell out of it to unsuspecting people, are the same kind of people that happily use [XMPP+OMEMO](https://soatok.blog/2024/08/04/against-xmppomemo/), [Matrix](https://soatok.blog/2024/08/14/security-issues-in-matrixs-olm-library/), or weird Signal forks that [remove forward secrecy](https://web.archive.org/web/20240405190353/https%3A//getsession.org/session-protocol-explained#:~:text=First%20things%20first%2C%20let%E2%80%99s%20talk%20about%20what%20we%E2%80%99re%20leaving%20behind%3A%20Perfect%20Forward%20Secrecy%20(PFS)) and think it’s fine.

Not to mince words: The same people who believe PGP is good are also famously not great at cryptography engineering.

If you’re going to outsource your opinions on privacy technology to someone else, make sure it’s someone who has [actually found vulnerabilities in cryptographic software](https://soatok.blog/tag/vulnerability/) before. Most evangelists have not.

![](https://i0.wp.com/soatok.blog/wp-content/uploads/2020/08/soatok_stickerpack_ind_cca2.png?resize=512%2C512&ssl=1)

[CMYKat](https://cmykatgraphics.carrd.co/)

**I’m not here to litigate the demerits of PGP.** The Latacora article I linked above makes the same arguments I would make today, and is a more entertaining read.

It is of my opinion as a security engineer that specializes in applied cryptography that nobody should use PGP, because there’s virtually always a better tool for the job you want to use PGP for.

(And for the uncommon use cases, offering a secure, purpose-built replacement is a work-in-progress.)

> Note: I’m deliberately being blunt in this post because literally more than a decade of softspokenness from cryptography experts has done nothing to talk users off the PGP cliff. Being direct seems more effective than being tactful.
>
> If you want a gentler touch, ask your cryptographer. If you don’t have a cryptographer, hire one.

If you can accept that [every billionaire is the result of a failed system](https://papers.ssrn.com/sol3/papers.cfm?abstract_id=4442029), that’s how cryptographers feel about people using PGP.

Instead, let’s examine the “use cases” of PGP and what you should be using instead. (Some of this is redundant with the Latacora article, but I’m also writing it 5 years later, so some things have changed.)

![Clipboard Sticker](https://i0.wp.com/soatok.blog/wp-content/uploads/2021/04/soatok-telegrams-wave-3-commission-11.png?resize=512%2C512&ssl=1)

[CMYKat](https://cmykatgraphics.carrd.co/)

> I’m focusing on the “what” in this post, not the “why”. If you want to know the why, read [the Latacora blog](https://www.latacora.com/blog/2019/07/16/the-pgp-problem/), or [the Matthew Green blog](https://blog.cryptographyengineering.com/2014/08/13/whats-matter-with-pgp/).
>
> If you’re curious about the credibility of my recommendations, read my other blog posts or ask your cryptographer.

## Instead of PGP, Use This

This section contains specific tools to solve the same problems that PGP tries to solve, but better.

*What makes these recommendations better than PGP?*

Simply, they don’t make cryptographers want to run the other way screaming when they look under the hood. PGP does.

Some people are forced to use PGP because they work for a government that legally requires them to use PGP. In that corner case, your hands are tied by lawyers, so you don’t need to bother with what cryptographers recommend.

![OwO sticker](https://i0.wp.com/soatok.blog/wp-content/uploads/2020/09/soatoktelegrams2020-06.png?resize=512%2C512&ssl=1)

[CMYKat](https://cmykatgraphics.carrd.co/)

### Signing Software Distributions

**Use [Sigstore](https://www.sigstore.dev/)**.

Note that this is an ecosystem-wide consideration, not something that specific individuals must manually opt into for each of their hobby projects. The only downside to Sigstore is it hasn’t been widely adopted yet.

> If you’re a Python developer, you can just use [PEP 740](https://trailofbits.github.io/are-we-pep740-yet/) to get attestations with Trusted Publishers, which gives you Sigstore for free. For most developers, this is as simple as setting up a [GitHub Action](https://github.com/pypa/gh-action-pypi-publish) to publish to PyPI.
>
> This is a developing trend: Other programming language and package management ecosystems are following suit. I expect to see Sigstore attestations baked into NPM and Maven before the next US presidential election. With any luck, your favorite programming language could be on this list too.

Sigstore doesn’t just give you a signature that you check with a long-lived public key, nor does it require you to do the Web Of Trust rigamarole.

Rather, [Sigstore gives you a lot for free](https://blog.trailofbits.com/2022/11/08/sigstore-code-signing-verification-software-supply-chain/). Sigstore was designed around ephemeral signing certificates rather than a long-lived private key. It was purpose-built for preventing supply-chain attacks against open source software.

Combined with [Reproducible Builds](https://reproducible-builds.org/), Sigstore solves the [triangle of secure code delivery](https://defuse.ca/triangle-of-secure-code-delivery.htm).

**Alternatively, use [minisign](https://jedisct1.github.io/minisign/).** If your package ecosystem doesn’t support Sigstore yet, you can get by with minisign (which is [signify](https://man.openbsd.org/signify)-compatible) until they modernize.

You can also use SSH signatures, if you’d prefer. (More on that below.)

![Drakeposting Yes Sticker](https://i0.wp.com/soatok.blog/wp-content/uploads/2021/04/soatoktelegramswave3-08.png?resize=512%2C512&ssl=1)

[CMYKat](https://cmykatgraphics.carrd.co/)

### Signing Git Tags/Commits

**Use [SSH Signatures](https://docs.gitlab.com/ee/user/project/repository/signed_commits/ssh.html)**, not PGP signatures.

With Ed25519. [Stop using RSA](https://blog.trailofbits.com/2019/07/08/fuck-rsa/).

![](https://i0.wp.com/soatok.blog/wp-content/uploads/2021/07/neophyte-happy.png?resize=350%2C512&ssl=1)

Art by [Harubaki](https://harubaki.carrd.co)

### Sending Files Between Computers

**Use [Magic Wormhole](https://github.com/magic-wormhole/magic-wormhole).**

You could also use SSH + rsync to do this job. That’s fine too.

![](https://i0.wp.com/soatok.blog/wp-content/uploads/2020/04/soat...