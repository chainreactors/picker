---
title: Improving Geographical Resilience For Distributed Open Source Teams with FREON
url: https://soatok.blog/2025/08/09/improving-geographical-resilience-for-distributed-open-source-teams-with-freon/
source: Dhole Moments
date: 2025-08-10
fetch_date: 2025-10-07T00:17:52.691431
---

# Improving Geographical Resilience For Distributed Open Source Teams with FREON

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

# Improving Geographical Resilience For Distributed Open Source Teams with FREEON

* Post author

  By [Soatok](https://soatok.blog/author/soatok/)
* Post date

  [August 9, 2025](https://soatok.blog/2025/08/09/improving-geographical-resilience-for-distributed-open-source-teams-with-freeon/)

![Improving Geographical Resilience For Distributed Open Source Teams with FREON](https://i0.wp.com/soatok.blog/wp-content/uploads/2025/08/BlogHeader-2025-FREON.png?fit=1200%2C675&ssl=1)

In a recent blog post, I laid out the argument that, if you have securely implemented end-to-end encryption in your software, then [the jurisdiction where your ciphertext is stored is almost irrelevant](https://soatok.blog/2025/07/09/jurisdiction-is-nearly-irrelevant-to-the-security-of-encrypted-messaging-apps/).

Where jurisdiction *does* come into play, unfortunately, is where your software is developed and whether or not the local government will employ rubber-hose cryptanalysis to backdoor your software.

![The XKCD Security comic.  [Cueball is holding a laptop up in two hands, showing it to his Cueball-like friend who is examining it while holding a hand up to his head. Above the top of the panels frame, there is a box with a caption:] A Crypto nerd's imagination: Cueball: His laptop's encrypted. Let's build a million-dollar cluster to crack it. Friend: No good! It's 4096-bit RSA! Cueball: Blast! Our evil plan is foiled! [Cueball is holding a closed laptop down in one hand while giving his Cueball-like friend a wrench with the other. The friend reaches out for it. Above the top of the panels frame, there is a box with a caption:] What would actually happen: Cueball: His laptop's encrypted. Drug him and hit him with this $5 wrench until he tells us the password. Friend : Got it.  (Transcript from ExplainXKCD)](https://i0.wp.com/soatok.blog/wp-content/uploads/2025/08/xkcd-538-dark.png?resize=448%2C274&ssl=1)

[XKCD: Security](https://xkcd.com/538/)

If you’re a European, you probably already assumed this sort of attack is inevitable in America under the Trump administration.

Unfortunately, this isn’t a new threat.

The [U.S.A. P.A.T.R.I.O.T. Act](https://www.eff.org/issues/patriot-act)–which Congress keeps re-authorizing despite how much it shits all over the Constitution and human rights–has emboldened government agents to [flagrantly disregard the 4th Amendment](https://www.aclu.org/know-your-rights/border-zone) for years already. The CLOUD Act, passed in 2018, adds [further legal backdoors to data privacy](https://www.eff.org/deeplinks/2018/03/new-backdoor-around-fourth-amendment-cloud-act).

## Well-Tread Paths

There are multiple layers of mitigations that open source teams can adopt to make this sort of attack less attractive for human right violators.

Commonly discussed mitigations include:

* Releasing your software publicly under an free or open source license allows your users to inspect the software, modify it, or fork it entirely if you’re totally compromised.
* Reproducible builds allow you to assert that the software you’re installing matches the version you expect from the open source repository. This introduces a mechanism that makes attacks significantly less stealthy.
* Digital signatures and attestations published to SigStore (or some other binary transparency technology) provide a notion of supply-chain security between the provider of a software package and its users.

  See also: [PEP 740](https://peps.python.org/pep-0740/).

  In the context of end-to-end encrypted messaging apps, you also have the congruent notion of key transparency for preventing key substitution attacks.

Nothing in the above list is new. If you cannot publish reproducible artifacts to SigStore (or equivalent) today, your developer ecosystem should already be planning or developing this capability.

> If they aren’t, kick ’em into gear, maybe?
>
> ![Soatok is _TOTALLY_ innocent](https://i0.wp.com/soatok.blog/wp-content/uploads/2020/04/soatok_stickerpack-innocent.png?resize=512%2C512&ssl=1)
>
> Art: [CMYKat](https://cmykatgraphics.carrd.co/)

## Humans: The Weak Link

Any software that implements all three layers of protection is doing a remarkable job.

There is, however, one additional mitigation layer we can introduce to dissuade rubber-hose cryptanalysis by rendering it largely ineffective.

Today, software releases are signed with an asymmetric keypair. The `signing key` can produce signatures (and therefore must be secret), while the `verifying key` is released publicly to allow anyone to verify signatures.

There are some approaches that implement so-called “multi-sig” approaches, where multiple signatures must be present before a payload is considered valid, but this is not a universal strategy.

Therefore, **the publisher** of software that controls the signing key is the weak link, even in today’s state of the art security software.

## Stay FROSTy

So what if we removed this single point of failure by not having a single signing key?

**[FROST (RFC 9591)](https://datatracker.ietf.org/doc/rfc9591/)** is a technique for implementing Threshold Signatures. One of the FROST ciphersuites is backwards compatible with Ed25519.

### Threshold Signatures

Building an intuition for threshold signatures is easy.

Imagine for a moment, instead of having 1 secret key, you have 7 secret keys, of which 4 are required to cooperate in the FROST protocol to produce a signature for a given message. You can replace these numbers with some integer `t` (instead of 4) out of `n` (instead of 7).

This signature is valid for a single public key.

If fewer than `t` participants are dishonest, the entire protocol is secure.

![A flowchart sketching out the basic idea of threshold cryptography for digital signatures.](https://i0.wp.com/soatok.blog/wp-content/uploads/2025/08/Threshold-Cryptography.png?resize=768%2C523&ssl=1)

The basic idea of threshold signatures.

#### Okay But How?

Welp, that’s where things get tricky, because threshold cryptography is different depending on the algorithm you use.

If you’re trying to generate ECDSA-compatible threshold signatures, [good luck](https://blog.trailofbits.com/2023/09/20/dont-overextend-your-oblivious-transfer/). The complexity involved, [even with recent advancements](https://eprint.iacr.org/2025/910), makes it only generally worth it for non-custodial cryptocurrency wallets. This mess is unavoidable because ECDSA requires computing the modular inverse of a secret value.

Schnorr signatures, such as Ed25519, use a different construction that’s more amenable to threshold cryptography.

FROST is a protocol that implements Schnorr signatures in two rounds, once the initial key setup has concluded.

You can think of it as a variation of [Shamir’s Secret Sharing](https://www.zkdocs.com/docs/zkdocs/protocol-primitives/shamir/) that doesn’t require actually reconstructing the secret to actually use it to calculate signatures.

In FROST, the first round commits to the message (and therefore to the nonces), and the second creates the shares of the final signature. The shares are then validated by the Coordinator and aggregated into a final signature.

If you want to understand in more detail, [RFC 9591](https://www.rfc-editor.org/rfc/rfc9591.html#name-two-round-frost-signing-pro) is the best document to refer to.

![](https://i0.wp.com/soatok.blog/wp-co...