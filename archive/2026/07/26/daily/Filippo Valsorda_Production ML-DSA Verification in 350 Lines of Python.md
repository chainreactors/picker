---
title: Production ML-DSA Verification in 350 Lines of Python
url: https://words.filippo.io/mldsa-py/
source: Filippo Valsorda
date: 2026-07-26
fetch_date: 2026-07-27T05:39:02.342696
---

# Production ML-DSA Verification in 350 Lines of Python

[![Filippo Valsorda](https://assets.buttondown.email/images/1e8b4251-b3e2-4de1-9b95-9f5d0447644d.png)](https://filippo.io)

26 Jul 2026

# Production ML-DSA Verification in 350 Lines of Python

I don’t do a lot of Python, at least not in my most recent life.[1](#fn:ytdl) However, I happen to have just written [a production ML-DSA verifier in pure Python](https://github.com/FiloSottile/mldsa-py). It’s [350 lines of code](https://github.com/FiloSottile/mldsa-py/blob/main/src/mldsa/mldsa.py) (plus many more of tests), it supports all parameter sets, and I am pretty satisfied with it.

You can fetch it as [`mldsa` from PyPI](https://pypi.org/project/mldsa/), [thanks to William Woodruff](https://github.com/pypi/support/issues/9843), or you can copy-paste it: it’s a single file without dependencies and it’s dual-licensed CC0 and 0BSD. It works with Python 3.8 and later. The API is modeled after the excellent [pyca/cryptography](https://github.com/pyca/cryptography).

```
import mldsa

vk = mldsa.VerificationKey(verification_key_bytes)

try:
    vk.verify(signature, message)
except mldsa.VerificationError:
    print("invalid signature!")
```

I hope this will make it easier for some projects to migrate to post-quantum authentication, which [has suddenly become more urgent than we all anticipated](https://words.filippo.io/crqc-timeline/). In particular, I hope it will unblock some client applications that can’t use C extensions for portability reasons.

Modern Python [package management](https://docs.astral.sh/uv/), [typing](https://docs.astral.sh/ty/), and [linting](https://docs.astral.sh/ruff/) are also a lot more powerful[2](#fn:minigame) than in the early Python 3 days, and the result is a pretty readable ML-DSA verifier.

ML-DSA is actually very simple to implement with its 23-bit base field: we use Python integers (without even needing Python’s big integer support) and SHA-3 from hashlib. There are 86 lines of throat clearing, 27 lines of base field (arithmetic, `centered_mod`, `decompose`), 28 lines of sampling (`sample_ntt`, `sample_in_ball`), 39 of polynomials (`Poly`, `NTTPoly`), 25 of NTT, 30 of parsing and packing (`pack`, `unpack`, `unpack_signed`), 35 of key expansion (`VerificationKey.__init__`, `public_key_hash`), and 80 of actual signature verification (`VerificationKey.verify`, `message_hash`, `use_hint`).

![A minimap showing the code layout with colorized areas](https://assets.buttondown.email/images/3f31264f-fd5c-4919-b109-7c727a5964bb.png)

Performance is… decent? 230 ML-DSA-44 verifications per second without precomputation. That’s 60x slower than Go, but not 1000x. The only optimization change I made was [using integers instead of field elements in the NTT hot loop](https://github.com/FiloSottile/mldsa-py/commit/954880c364cd99519964413aabe742a0197f91b1).

```
                             │   sec/op    │
Verify/ML-DSA-44/Whole         4.296m ± 2%
Verify/ML-DSA-65/Whole         6.509m ± 1%
Verify/ML-DSA-87/Whole         9.885m ± 3%
Verify/ML-DSA-44/Precomputed   2.635m ± 3%
Verify/ML-DSA-65/Precomputed   3.712m ± 4%
Verify/ML-DSA-87/Precomputed   5.363m ± 1%
```

The implementation is tested with the full reusable ML-DSA testing stack: [Wycheproof test vectors](https://github.com/C2SP/wycheproof/blob/main/doc/mldsa.md) and [CCTV accumulated vectors](https://github.com/C2SP/CCTV/tree/main/ML-DSA/accumulated), using pytest and [muzoo](https://github.com/FiloSottile/mostly-harmless/tree/main/muzoo) for mutation testing. It has 96% branch coverage, and more importantly it kills every mutation I (and Claude) could think of. (ML-DSA testing techniques deserve their own article.)

## Why Python?

The project started as a way to double-check the tests *of the tests* of my Go crypto/mldsa implementation. How do you know your tests are good and comprehensive? You add bugs (“mutations”) and you check that the tests fail. What if you skipped a check though? There won’t be any code to introduce a bug in! The *obvious* solution is to write a different implementation from scratch, then introduce bugs there, check that the tests catch the bugs, and then port the tests back. Duh.

Anyway, pure Python might not be particularly well-suited for cryptography that involves secrets because producing constant-time code could be difficult. However, a signature *verifier* involves no secrets, and Python is expressive and, most importantly, different from Go, making shared mistakes less likely.

You might want to follow me on Bluesky at [@filippo.abyssdomain.expert](https://bsky.app/profile/filippo.abyssdomain.expert) or on Mastodon at [@filippo@abyssdomain.expert](https://abyssdomain.expert/%40filippo), but I can’t promise any more Python.

## The picture

The [CENTOPASSI](https://centopassi.net/) is not all smooth riding, that’s part of the point. However, I am *a little* annoyed at the local who I had called and who said this road was closed but totally doable on a motorcycle.

![A collapsed country road, its asphalt cracked and sliding down towards the valley. Green bushes line the very narrow and gravelly intact left edge. In the distance, rolling hills with wind turbines under a bright blue sky.](https://assets.buttondown.email/images/e3cf617e-3ec0-4b63-b48b-171644262153.jpeg)

My work is made possible by [Geomys](https://geomys.org), an organization of professional Go maintainers, which is funded by [Ava Labs](https://www.avalabs.org/), [Teleport](https://goteleport.com/), [Datadog](https://www.datadoghq.com/), [Tailscale](https://tailscale.com/), and [Sentry](https://sentry.io/). Through our retainer contracts they ensure the sustainability and reliability of our open source maintenance work and get a direct line to my expertise and that of the other Geomys maintainers. (Learn more in the [Geomys announcement](https://words.filippo.io/geomys).)
Here are a few words from some of them!

Teleport — For the past five years, attacks and compromises have been shifting from traditional malware and security breaches to identifying and compromising valid user accounts and credentials with social engineering, credential theft, or phishing. [Teleport Identity](https://goteleport.com/platform/identity/?utm=filippo) is designed to eliminate weak access patterns through access monitoring, minimize attack surface with access requests, and purge unused permissions via mandatory access reviews.

Ava Labs — We at [Ava Labs](https://www.avalabs.org), maintainer of [AvalancheGo](https://github.com/ava-labs/avalanchego) (the most widely used client for interacting with the [Avalanche Network](https://www.avax.network)), believe the sustainable maintenance and development of open source cryptographic protocols is critical to the broad adoption of blockchain technology. We are proud to support this necessary and impactful work through our ongoing sponsorship of Filippo and his team.

---

1. Fun fact, I got started in open source as a maintainer of youtube-dl. [↩](#fnref:ytdl "Jump back to footnote 1 in the text")
2. I feel the same about the TypeScript ecosystem. It’s fun for a week or two every once in a while, but I wouldn’t want to daily drive any of these ecosystems: it’s too easy to spend a whole day updating dev dependencies and fixing linter errors and get the mistaken impression of having gotten anything done. [↩](#fnref:minigame "Jump back to footnote 2 in the text")

Subscribe

[Feed](https://words.filippo.io/rss/) 📡 | [Bluesky](https://bsky.app/profile/filippo.abyssdomain.expert) 🦋 | [Mastodon](https://abyssdomain.expert/%40filippo) 🐘

[![](https://cdn.bsky.app/img/avatar/plain/did:plc:x2nsupeeo52oznrmplwapppl/bafkreifth4anopszp3maih7b3ople7tj77tirmpgmiu2vinou4pjhnewo4)

Filippo Valsorda

@filippo.abyssdomain.expert](https://bsky.app/profile/filippo.abyssdomain.expert)

It's not my usual beat, but I wrote a pure-Python ML-DSA verifier.
pip install mldsa
It's 350 lines, CC0/0BSD, single-file, no dependencies, and thoroughly tested.
Signature verification handles no...