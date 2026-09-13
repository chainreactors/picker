---
title: The V8 JavaScript Runtime Undermined My Constant-Time JavaScript Library
url: https://soatok.blog/2026/09/12/the-v8-javascript-runtime-undermined-my-constant-time-javascript-library/
source: Dhole Moments
date: 2026-09-12
fetch_date: 2026-09-13T07:01:40.573276
---

# The V8 JavaScript Runtime Undermined My Constant-Time JavaScript Library

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

[Cryptography](https://soatok.blog/category/cryptography/) [Vulnerability](https://soatok.blog/category/technology/software-security/vulnerability/)

# The V8 JavaScript Runtime Undermined My Constant-Time JavaScript Library

* Post author

  By [Soatok](https://soatok.blog/author/soatok/)
* Post date

  [September 12, 2026](https://soatok.blog/2026/09/12/the-v8-javascript-runtime-undermined-my-constant-time-javascript-library/)

![The V8 JavaScript Runtime Undermined My Constant-Time JavaScript Library](https://i0.wp.com/soatok.blog/wp-content/uploads/2026/09/BlogHeader-2026-ConstantTimeJS050.png?fit=1200%2C675&ssl=1)

Six years ago, I wrote a blog post titled *[Soatok’s Guide to Side-Channel Attacks](https://soatok.blog/2020/08/27/soatoks-guide-to-side-channel-attacks/)* in which I discussed the general topic of side-channels in cryptographic applications, and how to avoid them, with example code in PHP. I had called out that the algorithms discussed on the page cannot rule out compiler or runtime optimizations that undermine your security goals: You can achieve *algorithmic constant-time*, but any higher assurance was [outside the scope of the work being done](https://soatok.blog/2020/08/27/soatoks-guide-to-side-channel-attacks/#malicious-environments-and-algorithmic-constant-time).

> For that reason, we’re going to assume that **algorithmic constant-time is adequate** for the duration of this blog post.
>
> If your threat model prevents you from accepting this assumption, feel free to put in the extra effort yourself and tell me how it goes. After all, as a furry who writes blog posts in my spare time for fun, I don’t exactly have the budget for massive research projects in formal verification.
>
> Soatok’s Guide to Side-Channel Attacks (Aug. 2020)

To make it easier to see in action, I also wrote a separate TypeScript / JavaScript library called [constant-time-js](https://github.com/soatok/constant-time-js) for demonstration purposes.

Over the years, this demo code has been adopted by **precisely zero dependent packages**, [according to NPM](https://www.npmjs.com/package/constant-time-js?activeTab=dependents) (at least, as of this writing).

![Soatok Yay Sticker](https://i0.wp.com/soatok.blog/wp-content/uploads/2024/07/SoatokCheer.png?resize=512%2C379&ssl=1)

My warnings to not rely on this in production worked!
Art: AJ\_LovesDinos

However, that only covers open source dependencies; I have no idea if some proprietary software decided to build on my designs.

While at a furry convention last month, I received an email from a Ph.D student named [Yayu Wang](https://yayuwang.org/) which [disclosed a side-channel in constant-time-js](https://github.com/soatok/constant-time-js/pull/9). I have since released [version 0.5.0](https://github.com/soatok/constant-time-js/releases/tag/v0.5.0) of the library, which fixes the issue reported, and used [GitHub’s security advisories feature](https://github.com/soatok/constant-time-js/security/advisories/GHSA-pgf9-4q65-hrqj) to request a CVE.

> The full credits are as follows:
>
> Vulnerability discovered and reported by [Yayu Wang](https://yayuwang.org/). Research done by [Yayu Wang](https://yayuwang.org/), [Kjell Dankert](https://www.linkedin.com/in/kdankert/), [Duy Kha Dinh](https://kha-dinh.github.io/), and [Aastha Mehta](https://aasthakm.github.io/), University of British Columbia.

My reason for posting an advisory and requesting a CVE is simple: If anyone is *actually* using this code (e.g., in a proprietary software system I have no visibility into), then either `npm audit` or a CVE being assigned is likely to trigger internal security mechanisms and prompt them to upgrade to the latest version as soon as possible.

Since the urgent stuff (advisory, patch, etc.) has already been handled elsewhere, I thought I’d write a blog post that dives deeper into the more interesting parts of this finding and its remediation.

Because, let’s be real, if you read my blog you’re either a nerd or part of [a nerdy subculture](https://en.wikipedia.org/wiki/Furry_fandom), so why not nerd out a bit?

![Coffee Sip Sticker](https://i0.wp.com/soatok.blog/wp-content/uploads/2020/09/soatoktelegrams2020-15.png?resize=512%2C512&ssl=1)

Art: [CMYKat](https://cmykatgraphics.carrd.co/)

## Contents

* [Timeline](#timeline)
* [Verifying The Report](#verifying-the-report)
* [Writing The Patch](#writing-the-patch)
* [Verifying The Fix](#verifying-the-fix)
* [What Would Higher Assurance Look Like?](#higher-assurance)

## Timeline

* **2026-08-21:** Disclosure email received at 4:51 PM. I reply only to Yayu at 4:54 PM to say “Hey, I [got] your email. I’m currently traveling and will not be at a keyboard until Tuesday. I’ll follow up as soon as I can.”
* **2026-08-25:** I verify the report and then write a patch.
* **2026-08-26:** I reply-all to the disclosure email with a locally-tested proposed patch.
* **2026-09-09**: Yayu responds that they tested the patch and confirmed it removed the leakage.
* **2026-09-10**: Public disclosure and new version tagged.
* **2026-09-11**: This blog post is written.
  + Though I didn’t post it until a little after 3 AM. Oops.

## Verifying The Report

In the age of AI-driven vulnerability hunting–punctuated by severity inflation and frequent hallucinations–the proportion of bogus reports to legitimate ones has increased significantly. Verifying that the bug actually exists and is as severe as the researcher claims has always been important for maintainers, but it invites much more emphasis when you’re drowning in slop.

The initial report email was shared in [the pull request description](https://github.com/soatok/constant-time-js/pull/9) for the fix, if you want to read it in full. The relevant excerpt from the description tells us enough to figure out where to start looking:

> The conditional-selection functions in constant-time-js use branchless JavaScript expressions to construct selection masks. We found that `select`, `select_alt`, and `select_ints` nevertheless produce secret-dependent instruction- and data-cache behavior in V8. The leakage arises from V8’s `ToBoolean` mechanism, its different handling of `-0` and `-1`, and direct accesses to the raw `true` and `false` Oddball objects on different cache lines. The resulting cache-access patterns can reveal the value of the selection condition.
>
> Yayu’s disclosure email

So, obviously, the first thing to check is V8’s ToBoolean mechanism. Which looks like [this](https://github.com/v8/v8/blob/9c09e7876ff830e1f9a731aa930040d1028ff5a1/src/interpreter/interpreter-generator.cc#L1267-L1288):

```
// ToString
//
// Convert the accumulator to a String.
IGNITION_HANDLER(ToBoolean, InterpreterAssembler) {
  TNode<Object> value = GetAccumulator();
  TVARIABLE(Boolean, result);
  Label if_true(this), if_false(this), end(this);
  BranchIfToBooleanIsTrue(value, &if_true, &if_false);
  BIND(&if_true);
  {
    result = TrueConstant();
    Goto(&end);
  }
  BIND(&if_false);
  {
    result = FalseConstant();
    Goto(&end);
  }
  BIND(&end);
  SetAccumulator(result.value());
  Dispatch();
}
```

Oh, hey, `BranchIfToBooleanIsTrue()`. That name sure sounds like [a branching side-channel](https://github.com/veorq/cryptocoding#avoid-branchings-controlled-by-secret-data) would be exposed. And, indeed, that is [what we observe](https://github.com/v8/v8/blob/9c09e7876ff830e1f9a731aa930040d1028ff5a1/src/codegen/code-stub-assembler.cc#L1641-L1724).

Next, we need to look at converting *fro...