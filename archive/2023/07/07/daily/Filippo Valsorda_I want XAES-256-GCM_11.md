---
title: I want XAES-256-GCM/11
url: https://words.filippo.io/dispatches/xaes-256-gcm-11/
source: Filippo Valsorda
date: 2023-07-07
fetch_date: 2025-10-04T11:52:44.353075
---

# I want XAES-256-GCM/11

[![Filippo Valsorda](https://assets.buttondown.email/images/1e8b4251-b3e2-4de1-9b95-9f5d0447644d.png)](https://filippo.io)

6 Jul 2023

# I want XAES-256-GCM/11

In 2023, the way to use AES is AES-GCM. Anything else is very unlikely to make sense. We might not like that, we might wish OCB hadn’t been patented, but with hardware support in most processors these days GCM is both faster than the alternatives, ubiquitous, and just tolerable to implement.

Still, I don’t want to use AES-GCM, I want to use XAES-256-GCM/11, which has a number of nice properties and only the annoying defect of not existing.

The problem with AES-GCM is that its nonce is a little too small to comfortably select at random. At 96 bit, the probability of a [birthday bound](https://en.wikipedia.org/wiki/Birthday_attack) collision becomes uncomfortable (2^-32^) after a few billion messages (2^32^), and [the consequences of a collision are catastrophic](https://eprint.iacr.org/2016/475).[1](#fn:distinguish) Some applications know they will never encrypt that many messages under a single key, but those numbers are a little too low and the consequences too dire to make that assumption at the API level, so we’re forced to delegate nonce management to the user.[6](#fn:gcm128)

ChaCha20Poly1305 has the same issue, which is why the *extended-nonce* construction XChaCha20Poly1305 exists. It resolves the issue by taking a 192-bit nonce[2](#fn:xcha), and “hashing” it along with the key into a fresh key.[5](#fn:sivchacha) The key is 256 bits, so there is no need to ever worry about collisions there. (More on that later.) You should *always* use the X variant unless the nonce is fully implicit, like when it’s always zero (like in age), a record counter (like in TLS), or a chunk number (like in STREAM). You can also make nice APIs for the X variant that generate the nonce at random from the system CSPRNG (and we are thinking about how to best do that in the Go standard library).

XChaCha20Poly1305 uses ChaCha20 itself to do the hashing to avoid introducing a new primitive, but this would work just as well using SHA-256 or HKDF to derive a regular key and nonce for ChaCha20Poly1305 from a key and a larger nonce. This means you could do the same for AES-GCM, and some schemes do in fact do just that. Regrettably, we don’t have a name for it, so you can’t just say to people “you should *always* use the X variant” or make a nice interoperable API for it.

Anyway, that’s the X in my ~~pony~~ XAES-256-GCM/11.

I don’t care if it uses HKDF, or SHA-256, or the AES function[3](#fn:care): I want a well-defined scheme that takes a key and 192 bits of nonce and hashes them into a derived key and 96 bits of nonce for use with AES-GCM.

Even with AES-128, the combined 224 bits of space for key and nonce are juuuust enough not to worry about collisions in the derived values. Still, this hints to the second part of the ~~pony~~ problem with AES-GCM: while [actually enough for post-quantum cryptography](https://words.filippo.io/dispatches/post-quantum-age/#128-bits-are-enough), 128-bit keys are still too tight for *multi-user security*. If for example an application encrypts 2^48^ messages under different 128-bit keys, and all messages start with the same few bytes, an attacker can build a lookup table, try and lookup the ciphertext of 2^64^ keys, and [have a 2^-16^ chance](https://www.wolframalpha.com/input?i=log2%281+-+%281+-+2%5E48+%2F+2%5E128%29+%5E+%282%5E64%29%29) to decrypt one message. Not good.

Multi-user attacks can be mitigated by many things—they require fixed nonces and partially known plaintext—but the only way to avoid that complexity escaping the AEAD abstraction and leaking into the rest of the protocol is to use 256-bit keys. For AES-GCM, that means using AES-256. Too bad that AES-256 is slower than AES-128, not because of its bigger key size, but because it was specified with more rounds, presumably under the assumption that users of bigger keys would also want more security margin against cryptanalysis. AES is an iterated cipher, where four core operations are performed multiple times in sequence: AES-128 performs them ten times, while AES-256 performs them fourteen times. AES-256 doesn’t *have to be* slower than AES-128, it was just defined to be slower. That’s regrettable, because it applies an artificial performance tax on the use of longer keys, which are desirable for reasons that have nothing to do with the risk of AES cryptanalysis.

Picking the “right” number of rounds is hard, and it’s kind of an open secret in the community that there is no rigorous and scientific way to do it. “*[Too much crypto](https://eprint.iacr.org/2019/1492)*” by Aumasson is all about this, and suggests eleven rounds for AES-256. I started this aiming for ten, which would have been exactly as fast as AES-128, but AES-256 does need more margin than AES-128 in some rare cases for *reasons*[4](#fn:rounds) and I guess it’d be silly to introduce a different abstraction-leaking edge case while trying to remove two, so AES-256/11 it is.

Summing up, I would like to provide to my users the extended-nonce 256-bit reduced-rounds XAES-256-GCM/11 (or XAES-256/11-GCM?) AEAD. It has infinitely randomizable nonces, a comfortable margin of multi-user security, and nearly the same performance as AES-128-GCM. It would also be a true drop-in replacement for XChaCha20Poly1305. Only issue is that it doesn’t exist.

(I guess it would also not be FIPS 140 compliant. We could make a FIPS version that’s slower but equivalent by using HKDF to derive the key, and the full-rounds AES-256.)

**Edit 2023-07-06**: Soatok has [previously suggested an extended-nonce AES-GCM construction](https://soatok.blog/2022/12/21/extending-the-aes-gcm-nonce-without-nightmare-fuel/). His AES-XGCM uses CBC-MAC for key derivation, which might be a good pick as both primitive-parsimonious and potentially FIPS 140 compliant. @NohatCoder@mastodon.gamedev.place on Mastodon suggests that since we’re KDF’ing, we might as well generate all the subkeys directly, solving the AES-256-specific issues that require the extra rounds (see [4](#fn:rounds)). I’m a bit wary to diverge too much from the well-established primitives, since at that point might as well use something novel (such as [AEGIS](https://datatracker.ietf.org/doc/draft-irtf-cfrg-aegis-aead/), like Soatok says). The point here is that I’d like a thin construction that’s easy to get confidence for if you already trust AES-GCM.

If for some reason you’re curious about what other ponies I want, you might want to follow me [on Bluesky](https://bsky.app/profile/filippo.abyssdomain.expert) or [on Mastodon](https://abyssdomain.expert/%40filippo).

## The picture

Cats! Amongst Roman ruins! What else do you need in life? (Better AEAD modes I guess.)

![A calico cat sleeps in the foreground, another cat is sitting down a step behind it, and behind them and a rail is a archaeological site with trees and columns. Further back, buildings.](https://assets.buttondown.email/images/9f565354-cb87-43c5-8ef8-36289ff73b83.jpeg)

My awesome clients—[Sigsum](https://www.sigsum.org/), [Protocol Labs](https://protocol.ai/), [Latacora](https://www.latacora.com/), [Interchain](https://interchain.io/), [Smallstep](https://smallstep.com/), and [Tailscale](https://tailscale.com/)—are funding all this work and through our retainer contracts they get face time about its direction, as well as unlimited access to advice.

Here are a few words from some of them!

Protocol Labs — [Cryptonet](https://cryptonet.org/) is hosting [Proof of Space days](https://lu.ma/tm8v78rl) in Paris on July 20-21, a gathering of cryptographers, Web3 researchers and engineers to share knowledge on [Proof of Space](http://proofofspace.org/). We’ll have talks and workshops to collaborate, share ideas and onboard new researchers into this exciting field. You’ll also have a chance to meet us (we’re currently looking for a senior cryptography engineer), [regist...