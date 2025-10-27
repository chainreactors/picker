---
title: Avoid The Randomness From The Sky
url: https://words.filippo.io/dispatches/avoid-the-randomness-from-the-sky/
source: Filippo Valsorda
date: 2023-03-04
fetch_date: 2025-10-04T08:36:29.758964
---

# Avoid The Randomness From The Sky

[![Filippo Valsorda](https://assets.buttondown.email/images/1e8b4251-b3e2-4de1-9b95-9f5d0447644d.png)](https://filippo.io)

3 Mar 2023

# Avoid The Randomness From The Sky

This is a plea for cryptography specification authors. If your protocol uses randomness, please **make it a deterministic function that takes a fixed-size string of random bytes**, and publish known-answer tests for it.

This whole issue could really be just the paragraph above, but I feel like I need to at least explain the title. A cryptographer I respect and I had a bit of a running joke: *the randomness from the sky*. That’s how we called random sampling from arbitrary distributions dropped halfway through a cryptography algorithm, with no concern for how it should be implemented, where the entropy is coming from, what properties it needs to have, the failure modes, and how it will be tested. “It’s… you know, random!” Magic perfect randomness.

That might be ok for theoretical papers that focus on security proofs[1](#fn:isit), but it is very very much not enough for a spec.

The first reason is that the kernel doesn’t give us implementers a “random integer modulo q” API, or a “random point on P-256” API, it gives us a CSPRNG that produces bytes, at best. It’s then up to us to turn those random bytes into a random element of whatever the protocol needs. Trust me, that’s not a job you want to leave to us. Selecting uniform elements is subtle: even for the simplest case of an integer in a range whether you can just reduce a larger value depends on *the specific modulo and how larger the value is*.[2](#fn:bias)

You might argue that it’s tedious to re-specify how to get a random group element from bytes in every higher-level specification, and I agree! That’s why I think that building blocks such as prime order groups should include as part of the abstraction a map from a fixed number of uniform bytes to a uniform element in the group. [That’s what ristretto255 does.](https://www.ietf.org/archive/id/draft-irtf-cfrg-ristretto255-decaf448-06.html#name-element-derivation)

The second, more important reason is testability. Specifying randomness as just another fixed-size input of a deterministic function makes it possible to provide “known answer” test cases. Even if the spec doesn’t include vectors—which it should—other projects like [Wycheproof](https://github.com/google/wycheproof) or [CCTV](https://c2sp.org/CCTV) can fill the gap over time. Good, shared test vectors can cover edge cases[4](#fn:edge) implementors would not have otherwise thought about or tested, stopping bugs from making it into the wild. Instead, we have [scary algorithms like ECDSA signing](https://cs.opensource.google/go/go/%2B/refs/tags/go1.20%3Asrc/crypto/ecdsa/ecdsa.go;l=206) (where nonce selection needs to be 100% perfectly uniform, or the private key is leaked) that have no off-the-shelf test vectors because they are poorly randomized.[3](#fn:6979)

It’s tempting to say “just seed a stream cipher and use that as the CSPRNG” but that adopts the internals of the stream cipher, of how it’s instantiated, and how it’s used as a CSPRNG into your protocol, which might be a much worse outcome than a deliberate design. For example, the ZCash Powers of Tau MPC ceremony needed to generate a number of elliptic curve points from a seed, so they just called `ChaChaRng::from_seed`, got a Rust `Rand` trait implementation, and passed it down to `Fq::Rand`. Then they asked me to reimplement the protocol in Go. The result was… [fun](https://github.com/FiloSottile/powersoftau/blob/e2af113817477d26e6155f1aae478d3cb58d62c5/powersoftau/hash_to_g2.go#L13-L55).

Depending on your protocol, you can probably adopt simpler options than a deterministic CSPRNG anyway. If you need variable but short amounts of randomness, a XOF (extendable-output functions) or HKDF will do. If you need to retry a process, like to do rejection sampling, I like the pattern of hashing (with proper domain separation!) the previous randomness to generate a new candidate. For example, you take a fixed-size random string `r`, check if `truncate(H(r))` is in range, if not try `truncate(H(H(r)))`, and so on.

I saw a neat trick on top of this in the Classic McEliece design: its very large private keys are expanded from a short fixed-size random byte string, but the process has a chance of failure; if the process fails, the string is hashed into a new string, and the process starts over. What’s neat is that only the final string is written to disk to store the private key, removing the need to repeat the whole process next time, but without introducing the need for separate key loading and key generation functions.

## The picture

For those of you who follow this not for the cryptography or the open source journey but for the Rome photoblogging, here’s a picture of the Tevere at dawn. In other completely unrelated news, I am officially past the age where I can dance ‘til morning. Anyway, pretty sky.

![A river in the center of the frame, leading to a bridge. The sky is pink and orange and is reflecting off the water. A seagull silhouette in the sky.](https://assets.buttondown.email/images/d57025ea-a83d-41c3-85b6-228543fa03b5.jpeg)

As you might know, [I am now a full-time professional maintainer](https://words.filippo.io/full-time-maintainer/) and my awesome clients—Sigsum, Protocol Labs, Latacora, Interchain, Smallstep, and Tailscale—have me on retainer, funding all this work and getting unlimited access to advice.

Here are a few words from some of them!

Protocol Labs — Did you like today’s topic, randomness? Don’t miss our free event in Tokyo, the [Randomness Summit 2023](https://lu.ma/randomness-summit-tokyo) on March 30th. Learn more about randomness beacons, PRNG, VDF, and their fun applications such as timelock encryption[5](#fn:timelock) if you’re around!

Smallstep — [Access your homelab from anywhere securely using a YubiKey.](https://u.step.sm/yubikey-access-your-homelab-FV-newsletter) At Smallstep, we have an Offroad Engineer named Carl Tashian who keeps his ear to the ground for new ways to encrypt everything. He’s currently on a mission to use hardware-bound keys anywhere and everywhere - including in your homelab. [Join us (and get a free YubiKey 5 NFC)](https://u.step.sm/yubikey-access-your-homelab-FV-newsletter) as we take the journey to accessing your homelab securely, all with open source software.

Latacora — [Latacora](https://www.latacora.com/) bootstraps security practices for startups. Instead of wasting your time trying to hire a security person who is good at everything from Android security to AWS IAM strategies to SOC2 and apparently has the time to answer all your security questionnaires plus never gets sick or takes a day off, you hire us. We provide a crack team of professionals prepped with processes and power tools, coupling individual security capabilities with strategic program management and tactical project management.[6](#fn:latacora)

---

1. I think even papers ought to get into details about randomness, for example by telling us if the thing needs to be just non-repeating, or also unpredictable, or also secret, or also uniform… sometimes all that matters in the security proof! But today let’s focus on specifications. [↩](#fnref:isit "Jump back to footnote 1 in the text")
2. Here’s an example: if you want a number modulo 200, you might be tempted to reduce a random byte which starts uniformly between 0 and 255. What you get is a biased distribution where 0 to 55 are twice as likely as the other values. If you reduce a 16 bytes value though the difference in probability becomes a comfortable 2⁻¹²⁰. The closer the modulo is to a power of two, the less margin is necessary. The math is annoying to do. [↩](#fnref:bias "Jump back to footnote 2 in the text")
3. [RFC 6979](https://www.rfc-editor.org/rfc/rfc6979) improves the situation by defining a deterministic ECDSA signing algorithm, and indeed it includes vectors. Unfortunat...