---
title: A “proof” of Fermat’s Last Theorem that fits the margin
url: https://blog.trailofbits.com/2026/09/09/a-proof-of-fermats-last-theorem-that-fits-the-margin/
source: The Trail of Bits Blog
date: 2026-09-09
fetch_date: 2026-09-10T06:51:20.078816
---

# A “proof” of Fermat’s Last Theorem that fits the margin

[The Trail of Bits Blog

Blog](/ "The Trail of Bits Blog")

[![Trail of Bits Logo](/img/tob.png)](https://trailofbits.com "Trail of Bits")

# A “proof” of Fermat’s Last Theorem that fits the margin

[Marc Ilunga](/authors/marc-ilunga/)

September 09, 2026

[vulnerability-disclosure](/categories/vulnerability-disclosure/), [memory-safety](/categories/memory-safety/), [open-source](/categories/open-source/)

Fermat famously claimed to have a “truly marvelous proof” of his [Last Theorem](https://en.wikipedia.org/wiki/Fermat%27s_Last_Theorem), but he never wrote it down, insisting the margin of his page was too narrow to contain it. A few centuries later, Anthropic announced a complete [formalization of Fermat’s Last Theorem using 13 million lines](https://www.anthropic.com/research/formalizing-fermats-last-theorem) of Lean code (clearly not what Fermat intended). Luckily, we found a wonderfully cursed [Lean bug](https://github.com/leanprover/lean4/issues/14684), shown below, that suggests the proof may have fit the margin after all. The issue affects all stable versions of Lean up to 4.33.1, and the patch is incorporated in v4.34.0-rc1.

![“Figure showing a “checked” proof of Fermat’s Last Theorem using Lean 4.33.1”](/2026/09/09/a-proof-of-fermats-last-theorem-that-fits-the-margin/proof-fermat-image_hu_f4c2a5f3789324fb.webp)

A “checked” proof of Fermat’s Last Theorem using Lean 4.33.1

The blue checkmarks in the screenshot above would suggest that Lean considers this proof correct. This seems odd given the amount of work Sir Andrew Wiles put into this problem and the vast size of Claude’s proof. So what is going on?

The “proof” clearly doesn’t make any sense and exploits an issue in Lean. We found the issue while using GPT-5.6 to experiment with a new skill for code review. We want to clarify up front that the issue is not a kernel [soundness issue](https://github.com/leanprover/lean4/pull/14806), but it happens to nicely fit any discussion of strings, lengths, and substrings.

The issue affects `String.Pos.Raw.extract`, Lean’s low-level string-slicing function. When asked to extract a one-byte slice at an [astronomically large position](https://github.com/leanprover/lean4/blob/f3b06c705e6c85f5314019d5d3baab0fec5b580c/src/runtime/object.cpp#L2221-L2232), Lean’s [logical definition](https://github.com/leanprover/lean4/blob/f3b06c705e6c85f5314019d5d3baab0fec5b580c/src/Init/Data/String/Basic.lean#L3012-L3014) returns [the empty string](https://github.com/leanprover/lean4/blob/f3b06c705e6c85f5314019d5d3baab0fec5b580c/src/Init/Data/String/Basic.lean#L3017). But the [compiled native code](https://github.com/leanprover/lean4/blob/f3b06c705e6c85f5314019d5d3baab0fec5b580c/src/runtime/object.cpp#L2374) returns [the entire original string](https://github.com/leanprover/lean4/blob/f3b06c705e6c85f5314019d5d3baab0fec5b580c/src/runtime/object.cpp#L2376). That disagreement is enough to manufacture a contradiction. Lean’s ordinary evaluator “proves” that the tiny slice was empty, while native evaluation “proves” that the very same slice contained “a truly marvelous proof.” Put those together, and Lean concludes that the empty string equals a non-empty string. And once you have a contradiction, you can prove anything, including Fermat’s Last Theorem.

On the bright side, the Lean team was considerably faster than mathematical history. About 90 minutes after we reported the issue, hargoniX opened a fix for the [memory-safety problem](https://github.com/leanprover/lean4/pull/14687), and it was merged roughly three hours after filing. The [remaining semantic mismatch](https://github.com/leanprover/lean4/pull/14717) was fixed by Rob23oba five days after the report, closing the issue. We’d like to give a huge shoutout to hargoniX, Rob23oba, and the Lean team for the fast turnaround.

As a reminder, when dealing with external proofs, follow Lean’s guidance for [validating a Lean proof](https://lean-lang.org/doc/reference/latest/ValidatingProofs/). In our proof-of-concept code above, `#print axioms flt` shows `'flt' depends on axioms: [propext, Classical.choice, Quot.sound, flt._native.native_decide.ax_1_1]`. The extra axiom `native_decide` adds the compiler to the trusted boundary, and therefore needs to be used with care. Machine-checked proofs will increasingly enable an unprecedented level of trust in mathematical results and critical software. However, more work is needed (e.g., [lean4lean](https://github.com/digama0/lean4lean) and [alternative kernel implementations](https://arena.lean-lang.org/)) to ensure that proofs aren’t deemed correct through exploitation of issues in theorem provers.

Fermat’s theorem took 350+ years to prove. If you don’t want to wait that long for your code to be audited, [contact us](https://trailofbits.com/contact/).

#### If you enjoyed this post, share it:

[X](https://x.com/trailofbits "X")

[LinkedIn](https://linkedin.com/company/trail-of-bits "LinkedIn")

[GitHub](https://github.com/trailofbits "GitHub")

[Mastodon](https://infosec.exchange/%40trailofbits "Mastodon")

[Hacker News](https://news.ycombinator.com/from?site=trailofbits.com "Hacker News")

## Related Posts

[### How CISA can improve OSS security

November 20, 2023

The US government recently issued a request for information (RFI) about open-source software (OSS) security. In this …](/2023/11/20/how-cisa-can-improve-oss-security/)

[### VMs won't contain cyber-capable agents

August 26, 2026

You can no longer assume a mere VM will contain a sufficiently advanced AI agent.](/2026/08/26/vms-wont-contain-cyber-capable-agents/)

[### How Trail of Bits helps verify the integrity of your Signal chats

August 11, 2026

Signal recently launched Automatic Key Verification, a feature that helps validate that your chats are secure without …](/2026/08/11/how-trail-of-bits-helps-verify-the-integrity-of-your-signal-chats/)

Subscribe

#### Page content

#### Recent Posts

* [A “proof” of Fermat’s Last Theorem that fits the margin](/2026/09/09/a-proof-of-fermats-last-theorem-that-fits-the-margin/)
* [VMs won't contain cyber-capable agents](/2026/08/26/vms-wont-contain-cyber-capable-agents/)
* [State divergence enables unauthorized access](/2026/08/25/state-divergence-enables-unauthorized-access/)
* [How Trail of Bits helps verify the integrity of your Signal chats](/2026/08/11/how-trail-of-bits-helps-verify-the-integrity-of-your-signal-chats/)
* [A few notes on AWS Nitro Enclaves: KMS integration](/2026/08/05/a-few-notes-on-aws-nitro-enclaves-kms-integration/)

© 2026 Trail of Bits.
Generated with [Hugo](https://gohugo.io/) and [Roadster](https://github.com/mansoorbarri/roadster/) theme.