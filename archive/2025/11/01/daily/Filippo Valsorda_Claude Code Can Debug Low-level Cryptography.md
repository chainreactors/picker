---
title: Claude Code Can Debug Low-level Cryptography
url: https://words.filippo.io/claude-debugging/
source: Filippo Valsorda
date: 2025-11-01
fetch_date: 2025-11-02T03:15:13.336027
---

# Claude Code Can Debug Low-level Cryptography

[![Filippo Valsorda](https://assets.buttondown.email/images/1e8b4251-b3e2-4de1-9b95-9f5d0447644d.png)](https://filippo.io)

1 Nov 2025

# Claude Code Can Debug Low-level Cryptography

Over the past few days I wrote a new Go implementation of ML-DSA, a post-quantum signature algorithm specified by NIST last summer. I [livecoded](https://twitch.tv/filosottile) it all over four days, finishing it on Thursday evening. Except… Verify was always rejecting valid signatures.

```
$ bin/go test crypto/internal/fips140/mldsa
--- FAIL: TestVector (0.00s)
    mldsa_test.go:47: Verify: mldsa: invalid signature
    mldsa_test.go:84: Verify: mldsa: invalid signature
    mldsa_test.go:121: Verify: mldsa: invalid signature
FAIL
FAIL     crypto/internal/fips140/mldsa   2.142s
FAIL
```

I was exhausted, so I tried debugging for half an hour and then gave up, with the intention of coming back to it the next day with a fresh mind.

On a whim, I figured I would let Claude Code take a shot while I read emails and resurfaced from hyperfocus. I mostly expected it to flail in some maybe-interesting way, or rule out some issues.

Instead, it rapidly figured out a fairly complex low-level bug in my implementation of a relatively novel cryptography algorithm. I am sharing this because it made me realize I still don’t have a good intuition for when to invoke AI tools, and because I think it’s a fantastic case study for anyone who’s still skeptical about their usefulness.

> Full disclosure: Anthropic gave me a few months of Claude Max for free. They reached out one day and told me they were giving it away to some open source maintainers. Maybe it’s a ploy to get me hooked so I’ll pay for it when the free coupon expires. Maybe they hoped I’d write something like this. Maybe they are just nice. Anyway, they made no request or suggestion to write anything public about Claude Code. Now you know.

## Finding the bug

I started Claude Code v2.0.28 with Opus 4.1 and no system prompts, and gave it the following prompt (typos included):

> I implemented ML-DSA in the Go standard library, and it all works except that verification always rejects the signatures. I know the signatures are right because they match the test vector.
>
> YOu can run the tests with “bin/go test crypto/internal/fips140/mldsa”
>
> You can find the code in src/crypto/internal/fips140/mldsa
>
> Look for potential reasons the signatures don’t verify. ultrathink
>
> I spot-checked and w1 is different from the signing one.

To my surprise, it pinged me a few minutes later with [a complete fix](https://go-review.googlesource.com/c/go/%2B/716540/1..2).

Maybe I shouldn’t be surprised! Maybe it would have been clear to anyone more familiar with AI tools that this was a good AI task: a well-scoped issue with failing tests. On the other hand, this is a low-level issue in a fresh implementation of a complex, *relatively novel* algorithm.

It figured out that I had merged `HighBits` and `w1Encode` into a single function for using it from Sign, and then reused it from Verify where `UseHint` already produces the high bits, effectively taking the high bits of w1 twice in Verify.

Looking at [the log](https://gist.github.com/FiloSottile/d019f68db7143493c6a7e9c5fd08e872), it loaded the implementation into the context and then *immediately* figured it out, without any exploratory tool use! After that it wrote itself a cute little test that reimplemented half of verification to confirm the hypothesis, wrote a mediocre fix, and checked the tests pass.

I [threw the fix away](https://go-review.googlesource.com/c/go/%2B/716540/2..3) and refactored `w1Encode` to take high bits as input, and changed the type of the high bits, which is both clearer and saves a round-trip through Montgomery representation. Still, this 100% saved me a bunch of debugging time.

## A second synthetic experiment

On Monday, I had also finished implementing signing with failing tests. There were two bugs, which I fixed in the following couple evenings.

The first one was due to [somehow computing a couple hardcoded constants (1 and -1 in the Montgomery domain) wrong](https://go-review.googlesource.com/c/go/%2B/716240/1..2). It was very hard to find, requiring a lot of deep printfs and guesswork. Took me maybe an hour or two.

The second one was easier: [a value that ends up encoded in the signature was too short (32 bits instead of 32 bytes)](https://go-review.googlesource.com/c/go/%2B/716240/2..3). It was relatively easy to tell because only the first four bytes of the signature were the same, and then the signature lengths were different.

I figured these would be an interesting way to validate Claude’s ability to help find bugs in low-level cryptography code, so I checked out the old version of the change with the bugs (yay Jujutsu!) and kicked off a fresh Claude Code session with this prompt:

> I am implementing ML-DSA in the Go standard library, and I just finished implementing signing, but running the tests against a known good test vector it looks like it goes into an infinite loop, probably because it always rejects in the Fiat-Shamir with Aborts loop.
>
> You can run the tests with “bin/go test crypto/internal/fips140/mldsa”
>
> You can find the code in src/crypto/internal/fips140/mldsa
>
> Figure out why it loops forever, and get the tests to pass. ultrathink

It spent [some time doing printf debugging and chasing down incorrect values very similarly to how I did it, and then figured out and fixed the wrong constants](https://gist.github.com/FiloSottile/d16c37b2fada56875a894cdd2670a860). Took Claude definitely less than it took me. Impressive.

It gave up after fixing that bug even if the tests still failed, so I started a fresh session (on the assumption that the context on the wrong constants would do more harm than good investigating an independent bug), and gave it this prompt:

> I am implementing ML-DSA in the Go standard library, and I just finished implementing signing, but running the tests against a known good test vector they don’t match.
>
> You can run the tests with “bin/go test crypto/internal/fips140/mldsa”
>
> You can find the code in src/crypto/internal/fips140/mldsa
>
> Figure out what is going on. ultrathink

[It took a couple wrong paths, thought for quite a bit longer, and then found this one too](https://gist.github.com/FiloSottile/b184888663c5d57078dc90b1a019981b). I honestly expected it to fail initially.

It’s interesting how Claude found the “easier” bug more difficult. My guess is that maybe the large random-looking outputs of the failing tests did not play well with its attention.

The fix it proposed was updating only the allocation’s length and not its capacity, but whatever, the point is finding the bug, and I’ll usually want to throw away the fix and rewrite it myself anyway.

Three out of three one-shot debugging hits with no help is *extremely impressive*. Importantly, there is no need to trust the LLM or review its output when its job is just saving me an hour or two by telling me where the bug is, for me to reason about it and fix it.

As ever, I wish we had better tooling for using LLMs which didn’t look like chat or autocomplete or “make me a PR.” For example, how nice would it be if every time tests fail, an LLM agent was kicked off with the task of figuring out why, and only notified us if it did before we fixed it?

![An image of Clippy, the paperclip with eyes from Microsoft Office, with a speech bubble saying 'FYI, your tests are failing because you are taking the HighBits of w1 in w1Encode, but w1 in Verify is already the high bits output of UseHint.'](https://assets.buttondown.email/images/fdf79d45-0e03-4a52-b2d1-6c9c645aa773.png?w=800&fit=max)

For more low-level cryptography ~~bugs~~ implementations, follow me on Bluesky at [@filippo.abyssdomain.expert](https://bsky.app/profile/filippo.abyssdomain.expert) or on Mastodon at [@filippo@abyssdomain.expert](https://abyssdomain.expert/%40filippo). I promise I...