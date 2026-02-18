---
title: Cryptographic Issues in Matrix’s Rust Library Vodozemac
url: https://soatok.blog/2026/02/17/cryptographic-issues-in-matrixs-rust-library-vodozemac/
source: Dhole Moments
date: 2026-02-17
fetch_date: 2026-02-18T04:15:13.796733
---

# Cryptographic Issues in Matrix’s Rust Library Vodozemac

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

[Vulnerability](https://soatok.blog/category/technology/software-security/vulnerability/)

# Cryptographic Issues in Matrix’s Rust Library Vodozemac

* Post author

  By [Soatok](https://soatok.blog/author/soatok/)
* Post date

  [February 17, 2026](https://soatok.blog/2026/02/17/cryptographic-issues-in-matrixs-rust-library-vodozemac/)

![Cryptographic Issues in Matrix's Rust Library Vodozemac](https://i0.wp.com/soatok.blog/wp-content/uploads/2026/02/BlogHeader-2026-Matrix-Vodozemac.png?fit=1200%2C675&ssl=1)

Two years ago, I glanced at Matrix’s Olm library and [immediately found several side-channel vulnerabilities](https://soatok.blog/2024/08/14/security-issues-in-matrixs-olm-library/). After dragging their feet for 90 days, they ended up **not bothering to fix any of it**.

> The Matrix.org security team also failed to notify many of the alternative clients about the impending disclosure–a fact that became more annoying when they complained *to me* about how Matrix.org handled the embargo.

Instead, their response to my disclosure was to slap a deprecated notice on their README (despite allegedly having deprecated it in 2022) and then *publicly insist they knew about the side-channel attacks all along*, [per Matthew Hodgson on Hacker News](https://news.ycombinator.com/item?id=41249371).

Knowingly shipping vulnerable cryptography to millions of people that [happily insist their product is better than Signal](https://web.archive.org/web/20240731062107/https%3A//pawb.social/post/9842375) is a level of irresponsible that borders on grifting.

So, at that point, my public stance on Matrix became, simply:
**Don’t use Matrix.**

![NO sticker](https://i0.wp.com/soatok.blog/wp-content/uploads/2020/08/soatoktelegrams2020-04.png?resize=512%2C512&ssl=1)

[CMYKat](https://cmykatgraphics.carrd.co/)

And I was perfectly content leaving things at that, until my recent blog post about [why there are no good Discord alternatives and what we can do about that](https://soatok.blog/2026/02/11/on-discord-alternatives/) summoned yet more annoying Matrix evangelists.

So I decided to finally take a look at [Vodozemac](https://github.com/matrix-org/vodozemac), the Rust library that the Matrix team is so proud of.

Since you’re reading this, you already know how that turned out.

## Contents

* [Disclosure Timeline](#disclosure-timeline)
* [Cryptographic Issues in Vodozemac](#cryptographic-issues)
  + [Vulnerabilities](#vulnerabilities)
    1. [Olm Diffie-Hellman Accepts the Identity Element](#vuln-1)
    2. [Downgrade Attacks From V2 to V1](#vuln-2)
  + [Miscellaneous Issues](#miscellaneous)
    1. [ECIES CheckCode Has Only 100 Possible Values](#misc-1)
    2. [Message Keys Silently Dropped After MAX\_MESSAGE\_BYTES](#vuln-2)
    3. [Pickle Format Uses Deterministic IV](#misc-3)
    4. [`#[cfg(fuzzing)]` Bypasses MAC and Signature Verification](#vuln-4)
    5. [Strict Ed25519 Verification is Disabled By Default](#vuln-5)
* [What’s the Impact?](#impact)
* [Takeaways](#takeaways)
  + [Will Matrix Do Better Next Time?](#will-matrix-do-better)
* [Closing Thoughts](#closing-thoughts)

## Disclosure Timeline

I’m putting the disclosure timeline front-and-center so everyone has a chance to see it.

* **2026-02-11**: Issues discovered and reported to `security@matrix.org`
* **2026-02-12**: Matrix.org Security replies:

  “Thank you for your report. We’re looking into it and will get back to you shortly.”
* **2026-02-13**: I begin drafting this blog post
* **2026-02-16**: I email Matrix.org security to inform them that I plan to disclose this publicly on 2026-02-18
* **2026-02-17**: Matrix.org Security replies insisting, “there’s no practical security impact on Matrix”
* **2026-02-17**: I respond to Matrix.org with [an additional PoC](https://gist.github.com/soatok/024f80b8377de4bf9d0cb2d7e57b1eed#bonus-round-compromising-a-group-chat-megolm-from-a-single-participant), a patch, and express disagreement with their reasoning
* **2026-02-17**: Public disclosure

An astute observer will notice that this timeline does not cover 90 days. In fact, it only covers a week. There are a few reasons for that.

![Clipboard Sticker](https://i0.wp.com/soatok.blog/wp-content/uploads/2021/04/soatok-telegrams-wave-3-commission-11.png?resize=512%2C512&ssl=1)

[CMYKat](https://cmykatgraphics.carrd.co/)

### Why Avoid Delaying Publication?

Full public disclosure of security vulnerabilities is a damn good idea, [as Bruce Schneier argued in 2007](https://www.schneier.com/essays/archives/2007/01/schneier_full_disclo.html).

Coordinated disclosure is the practice of researchers and vendors working together to practice full disclosure in a timeline that’s minimally disruptive to the vendor’s customers, in a way that maximizes security and safety.

Some fools call that “responsible” disclosure. [They are wrong](https://adamcaudill.com/2015/11/19/responsible-disclosure-is-wrong/). (Matrix, to their credit, does not use the incorrect term on [their security disclosure policy page](https://www.matrix.org/security-disclosure-policy/).)

Google Project Zero established the norm of publishing within 90 days of a vulnerability’s discovery, whether it’s fixed or not. This, however, is a courtesy that independent researchers do not automatically owe the vendor.

I’ve covered a lot of this before in [a previous blog post](https://soatok.blog/2025/01/21/too-many-people-dont-value-the-time-of-security-researchers/) about how many people (including open source software developers) de-value security researchers.

The last time I reported an issue to Matrix, they insisted on the full 90 days and then did jack shit with that time. They didn’t even notify the developers of other Matrix clients that it was coming.

So, in my book, Matrix permanently lost the privilege of having a 90 day courtesy window. I gave them a week.

> I can already feel the message board users typing a storm about this. So to cut the debate off at the pass, I say: You’re free to disagree with this decision **when you disclose your own research findings**.
>
> Your bug, your policy.
>
> My bug, my policy.
>
> The Matrix team is already getting free specialized labor out of this deal. They don’t get to also dictate when, where, and how I criticize their software.
>
> You’re not gonna find a fairer fucking deal than that.

![Whistling Sticker](https://i0.wp.com/soatok.blog/wp-content/uploads/2021/04/soatoktelegramswave3-06.png?resize=512%2C512&ssl=1)

Art: [CMYKat](https://cmykatgraphics.carrd.co/)

## Cryptographic Issues in Vodozemac

These issues were identified in the source code tree at the commit hash, [a4807ce7f8e69e0a512bf6c6904b0d589d06b993](https://github.com/matrix-org/vodozemac/tree/a4807ce7f8e69e0a512bf6c6904b0d589d06b993) (which was also the head of the `main` branch at the time).

Not all of these issues are vulnerabilities, per se, but I will front-load this section with the actual vulnerabilities and then cover the remaining issues.

### Vulnerabilities

#### 1. Olm Diffie-Hellman Accepts the Identity Element

**Severity:** High

To understand this one, I first need to explain how [[Elliptic Curve] Diffie-Hellman](https://keymaterial.net/2025/05/23/there-is-no-diffie-hellman-but-elliptic-curve-diffie-hellman/) works, and the laziest way to do cryptanalysis.

At the risk of oversimplification, you can think of Diffie-Hellman as “just multiplication with exponents”.

(Don’t get intimidated by the math notation; you won’t need advanced math skills for this on...