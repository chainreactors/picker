---
title: Software Assurance & That Warm and Fuzzy Feeling
url: https://soatok.blog/2026/01/15/software-assurance-that-warm-and-fuzzy-feeling/
source: Dhole Moments
date: 2026-01-15
fetch_date: 2026-01-16T03:28:42.842092
---

# Software Assurance & That Warm and Fuzzy Feeling

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

[Fediverse E2EE Project](https://soatok.blog/category/technology/open-source/fediverse-e2ee-project/) [Software Security](https://soatok.blog/category/technology/software-security/)

# Software Assurance & That Warm and Fuzzy Feeling

* Post author

  By [Soatok](https://soatok.blog/author/soatok/)
* Post date

  [January 15, 2026](https://soatok.blog/2026/01/15/software-assurance-that-warm-and-fuzzy-feeling/)

![Software Assurance & That Warm and Fuzzy Feeling](https://i0.wp.com/soatok.blog/wp-content/uploads/2026/01/BlogHeader-2026-SoftwareAssurance.png?fit=1200%2C675&ssl=1)

If I were to recommend you use a piece of cryptography-relevant software that I created, how would you actually know if it was any good?

![A blue dhole scratches his head and looks mildly confused.](https://i0.wp.com/soatok.blog/wp-content/uploads/2020/07/riley-edit.png?resize=580%2C580&ssl=1)

Art: [Wayward Mutt](https://www.waywardmutt.art/)

**Trust is, first and foremost, a social problem.** If I told you a furry designed a core piece of Internet infrastructure, the reception to this would be *mixed*, to say the least.

If you’re familiar with the deep lore about furries and the Internet, this probably wouldn’t surprise you.

![@mmsword:  "Telecommunications as a whole, which also encompasses The Internet, is in a constant state of failure and just in time fixes and functionally all modern communication would collapse if about 50 people, most of which are furries, decided to turn their pager off for a day."  Quote tweet of @mykola:  "Please quote this tweet with a thing that everyone in your field knows and nobody in your industry talks about because it would lead to general chaos."  Nov 28, 2019](https://i0.wp.com/soatok.blog/wp-content/uploads/2026/01/image.png?resize=558%2C451&ssl=1)

Screenshot from this [old tweet](https://fixupx.com/mmsword/status/1200147947331043328).

(We all need hobbies, after all.)

But if you weren’t *in the know*, you might recoil in horror at the thought. “Hell nah, those cringey people on TikTok?”

Software assurance is chiefly concerned with reliability, safety, and security, which is deeply connected to **how trustworthy a piece of software is**.

(Trustworthy doesn’t necessarily mean trust*ed*. Everyone is free to choose what they trust, and what they don’t.)

But if you were to approach my work with an open mind, how might someone make an informed decision about whether or not the software I’m writing is trustworthy enough *for their use cases*?

![Soatok lecturing on a whiteboard](https://i0.wp.com/soatok.blog/wp-content/uploads/2021/02/soatok-by-scruffkerfluff-smol-1.png?resize=768%2C614&ssl=1)

Art by [ScruffKerfluff](https://scruffkerfluff.bsky.social/)

## Cryptography Audits and Other Thought-Terminating Clichés

If you weren’t around for *[Is TrueCrypt Audited Yet?](http://istruecryptauditedyet.com/)*, you might think this subheading is clickbait.

Cryptography audits and penetration testing in general are valuable work. Audits are essential in avoiding worse outcomes for security in multiple domains (network, software, hardware, physical, etc.).

However, they’re not a panacea, and an audit status should not be viewed as a simple binary “YES / NO” matter.

Some “audit reports” are **utterly worthless**.

Unfortunately, you basically have to be *qualified to do the same kind of work* to accurately distinguish between the trash and treasure.

However, this is usually one of the first questions I get from some technologists: “Was it audited? And is the report public?”

Audits are not cheap. Hiring a team of qualified and reputable experts to review the entirety of a nontrivial project can easily run into the six digits.

Let’s be real: I don’t have that kind of money just lying around, and random gay furries aren’t exactly a good fit for a non-profit like [OSTIF](https://ostif.org/).

So, no, I don’t have an audit for any of my projects.

If not having an audit is a dealbreaker for you, that’s fine. I would rather you be disappointed with an unchecked box than go out of my way to pay an unqualified company to give me a rubber stamp audit report just to satisfy your request (an act which I consider dishonest).

Audits aside, I’d like to talk about some of the mechanisms I’m employing to make my projects as trustworthy as any mere mortal can hope to achieve.

![High Paw (high five) sticker](https://i0.wp.com/soatok.blog/wp-content/uploads/2020/09/soatoktelegrams2020-08.png?resize=512%2C512&ssl=1)

Art: [CMYKat](https://cmykatgraphics.carrd.co/)

## Towards Furry-Grade Assurance

Let’s not mince words: The rest of this blog post is me nerding out about software testing methodologies, how I’m applying them, and the gap between practice and theory (i.e., formal methods).

The project in scope for this blog post is my [Public Key Directory](https://soatok.blog/category/technology/open-source/fediverse-e2ee-project/) project, which offers an essential building block for [making E2EE possible on the Fediverse](https://github.com/swicg/activitypub-e2ee/issues/35#issuecomment-3738855995).

If you want more background about this project, I recommend starting [here](https://soatok.blog/2024/06/06/towards-federated-key-transparency/).

### Specification-First Development

Before any code was ever written, I started writing a specification. You can [read it online at `fedi-e2ee/public-key-directory-specification` on GitHub](https://github.com/fedi-e2ee/public-key-directory-specification).

This document covers:

1. The motivation for its own existence
2. Important concepts relevant to the design
3. A threat model which includes:
   * **Assumptions** that must be true in order for the software to be secure. These might seem obvious, but it’s better to be explicit.
   * **Assets** in scope for the threat model.
   * **Actors** with specific roles, privileges, and motivations.
   * **The actual risks being considered**, including many that are not mitigated by design.
4. The actual definitions, algorithms, steps, etc.
5. Security considerations for implementors of the spec

I started writing this in June 2024, and I continue to make revisions as I develop the reference implementations of the specification. This process will continue until the first major version has been tagged.

By starting with a specification, every party can agree on what the software does, what it doesn’t do, what are its security goals, and why specific trade-offs were chosen in favor of others. Unlike source code, specifications do not carry the quirks of particular programming language runtimes or package ecosystems.

However, put a pin in this, because there’s more to talk about later.

### Unit Testing: Table Stakes

Once you have a reference implementation, you need it to pass unit tests in [CI](https://en.wikipedia.org/wiki/Continuous_integration). If you’re writing software in 2026 and don’t have working unit tests, your life is harder than it needs to be.

Whenever you bring up unit testing, the next thing that usually comes up is **code coverage**.

I do not use code coverage reports in any of my projects. To understand why, you should be familiar with [Goodhart’s Law](https://en.wikipedia.org/wiki/Goodhart%27s_law): When a measure becomes a target, it ceases to be a good measure.

Code coverage reports can lie to you with pretty green squares, and this leads to overconfidence.

Instead, I actually rely on two distinct additional testing methodologies.

### Mutation Testing: Code Coverag...