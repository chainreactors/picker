---
title: Moving Beyond the NPM elliptic Package
url: https://soatok.blog/2025/11/19/moving-beyond-the-npm-elliptic-package/
source: Dhole Moments
date: 2025-11-19
fetch_date: 2025-11-20T03:08:44.241774
---

# Moving Beyond the NPM elliptic Package

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

[Open Source](https://soatok.blog/category/technology/open-source/)

# Moving Beyond the NPM elliptic Package

* Post author

  By [Soatok](https://soatok.blog/author/soatok/)
* Post date

  [November 19, 2025](https://soatok.blog/2025/11/19/moving-beyond-the-npm-elliptic-package/)

![Moving Beyond the NPM elliptic Package](https://i0.wp.com/soatok.blog/wp-content/uploads/2025/11/BlogHeader-2025-Elliptic-JavaScript.png?fit=1200%2C675&ssl=1)

> **If you’re in a hurry,** head on over to [soatok/elliptic-to-noble](https://github.com/soatok/elliptic-to-noble) and follow the instructions in the README in order to remove the elliptic package from your project **and all dependencies in node\_modules**.
>
> ![High Paw (high five) sticker](https://i0.wp.com/soatok.blog/wp-content/uploads/2020/09/soatoktelegrams2020-08.png?resize=512%2C512&ssl=1)
>
> Art: [CMYKat](https://cmykatgraphics.carrd.co/)

## Why replace the elliptic package?

Yesterday, the *Trail of Bits* blog published [a post about finding cryptographic bugs in the elliptic library](https://blog.trailofbits.com/2025/11/18/we-found-cryptography-bugs-in-the-elliptic-library-using-wycheproof/) (a Javascript package on NPM) by using the Wycheproof. This blog post was accompanied by [a new chapter in their Testing Handbook about using Wycheproof](https://appsec.guide/docs/crypto/wycheproof/) as well as two CVEs.

It’s pretty cool work, especially to applied cryptography nerds (and C2SP contributors [like myself](https://github.com/C2SP/C2SP/pull/164)).

But one can’t help but notice [all the dates in the disclosure timeline](https://blog.trailofbits.com/2025/11/18/we-found-cryptography-bugs-in-the-elliptic-library-using-wycheproof/#coordinated-disclosure-timeline) are from **2024**, which was last year.

![Soatok thinking sticker](https://i0.wp.com/soatok.blog/wp-content/uploads/2025/11/SoatokTelegrams2020-12.png?resize=512%2C512&ssl=1)

Art: [CMYKat](https://cmykatgraphics.carrd.co/)

If you were to take a look at [the elliptic project’s issue tracker](https://github.com/indutny/elliptic/issues), you would be greeted by this:

![A bunch of open issues, stretching back to August 2024, detailing security issues in this pacakge.](https://i0.wp.com/soatok.blog/wp-content/uploads/2025/11/image.png?resize=618%2C1024&ssl=1)

Yeah, that’s not great.

Some of these issues are unrelated, and some are duplicates (referencing the vulnerabilities disclosed in the aforementioned blog post), and [one’s a false positive](https://github.com/indutny/elliptic/issues/341#issuecomment-3550036418).

Nonetheless, there’s a general lack of responsiveness from the elliptic maintainer on these security issues.

But it’s not like it’s **widely used** or anything, *right*?

![elliptic has 3056 dependent packages on npm](https://i0.wp.com/soatok.blog/wp-content/uploads/2025/11/image-1.png?resize=497%2C224&ssl=1)

![elliptic has 12,389,598 weekly downloads](https://i0.wp.com/soatok.blog/wp-content/uploads/2025/11/image-2.png?resize=464%2C232&ssl=1)

Oh, motherfucker!

### On Burnout and Open Source Software

I don’t blame anyone for getting burned out by maintaining open source software. Especially if you’re not being paid for it. If your open source software is popular enough, it doesn’t necessarily guarantee you an income. Rather, it just means more people with more problems demanding more of your time and emotional bandwidth. The outcome is as common as it is unfortunate.

To be clear: That the elliptic maintainer is largely unresponsive doesn’t necessarily mean that they’re experiencing burnout (they could just be really busy with things that don’t involve computers–who knows?), but I think we as a community should be mindful of this possibility.

### Deciding A Path Forward

So, to recap:

* The `elliptic` package has several public vulnerabilities that remain unfixed, including some that were made public **last year**.
* The package maintainer has largely been unresponsive.
* There are over 3000 dependent packages on NPM.

Thus, the most important question in my mind is: **How do we mitigate the security risk to the NPM ecosystem** without adding pressure to, or punishing, a possibly burned-out unpaid software developer?

After pondering it for a few hours, I decided to find a suitable replacement library and create a shim that replaces elliptic with a better implementation.

Without falling back to native dependencies, the best bet for the Node.js ecosystem is [noble-curves](https://github.com/paulmillr/noble-curves).

![Soatok Yay Sticker](https://i0.wp.com/soatok.blog/wp-content/uploads/2024/07/SoatokCheer.png?resize=512%2C379&ssl=1)

Art: [AJ](https://ajlovesdinos.bsky.social)

## Introducing, elliptic-to-noble

With all this background in mind, I’ve published the initial release of a package called [elliptic-to-noble](https://github.com/soatok/elliptic-to-noble) that provides a shim layer for noble-curves that imitates the elliptic package’s API.

Additionally, if you install it according to the instructions in the README, then NPM will **replace elliptic with my shim layer in all dependencies as well**.

![Grin Sticker](https://i0.wp.com/soatok.blog/wp-content/uploads/2021/03/soatoktelegramswave3-01.png?resize=512%2C512&ssl=1)

[CMYKat](https://cmykatgraphics.carrd.co/)

### Why this approach and not a different one?

This shim layer approach allows production code to quickly migrate towards a more secure implementation of elliptic curve cryptography in a pinch without introducing a lot of breaking changes to their source code.

It also doesn’t involve NPM security wresting control of the elliptic package away from its maintainer (as is possible if they aren’t responding to security issues) or putting yet-even-more pressure on them (as is always the case when security issues are reported). Additionally, if fewer packages end up depending on `elliptic` in the long-run, it might even be a relief to its author.

I think this strikes a balance between being humane to someone that isn’t communicating while still allowing the ecosystem to remain secure, and not requiring thousands of package maintainers to *drop everything and replace a dependency*.

#### Why should we trust you?

You don’t have to trust me. I have no official standing in the NPM ecosystem.

The elliptic-to-noble shim library is a quick way to get off elliptic’s vulnerable implementations while you plan a longer migration to noble-curves.

If you would rather do that work now than trust an Internet furry’s code to lurk in your node\_modules directory? Great. I’m glad you’re proactive.

But the fact remains that elliptic is vulnerable today. My shim library is one way to mitigate the risk while you replace your dependency.

---

Happy hacking!

Header art by [AJ](https://ajlovesdinos.bsky.social).

* Tags

  [ecosystem](https://soatok.blog/tag/ecosystem/), [elliptic](https://soatok.blog/tag/elliptic/), [elliptic curve cryptography](https://soatok.blog/tag/elliptic-curve-cryptography/), [JavaScript](https://soatok.blog/tag/javascript/), [mitigation](https://soatok.blog/tag/mitigation/), [NPM](https://soatok.blog/tag/npm/), [shim library](https://soatok.blog/tag/shim-library/), [software security](https://soatok.blog/tag/software-security/), [vulnerability](https://soatok.blog/tag/vulnerability-2/)

![](https://secure.gravatar.com/avatar/62964206396b67fb3a8985b19dc274f74b1a9232374e189577c0f1388fdc73f2?s=160&d=identicon&r=g)

## By Soatok

Security engineer with a fursona. Ask me ab...