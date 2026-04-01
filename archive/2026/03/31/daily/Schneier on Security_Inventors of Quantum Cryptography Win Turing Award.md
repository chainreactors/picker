---
title: Inventors of Quantum Cryptography Win Turing Award
url: https://www.schneier.com/blog/archives/2026/03/inventors-of-quantum-cryptography-win-turing-award.html
source: Schneier on Security
date: 2026-03-31
fetch_date: 2026-04-01T04:47:46.496536
---

# Inventors of Quantum Cryptography Win Turing Award

# [Schneier on Security](https://www.schneier.com/)

Menu

* [Blog](https://www.schneier.com)
* [Newsletter](https://www.schneier.com/crypto-gram/)
* [Books](https://www.schneier.com/books/)
* [Essays](https://www.schneier.com/essays/)
* [News](https://www.schneier.com/news/)
* [Talks](https://www.schneier.com/talks/)
* [Academic](https://www.schneier.com/academic/)
* [About Me](https://www.schneier.com/blog/about/)

### Search

*Powered by [DuckDuckGo](https://duckduckgo.com/)*

Blog

Essays

Whole site

### Subscribe

[![Atom](https://www.schneier.com/wp-content/uploads/2019/10/rss-32px.png)](https://www.schneier.com/feed/atom/)[![Facebook](https://www.schneier.com/wp-content/uploads/2019/10/facebook-32px.png)](https://www.facebook.com/bruce.schneier)[![Twitter](https://www.schneier.com/wp-content/uploads/2019/10/twitter-32px.png)](https://twitter.com/schneierblog)[![Email](https://www.schneier.com/wp-content/uploads/2019/10/email-32px.png)](https://www.schneier.com/crypto-gram)

[Home](https://www.schneier.com)[Blog](https://www.schneier.com/blog/archives/)

## Inventors of Quantum Cryptography Win Turing Award

Charles Bennett and Gilles Brassard have [won](https://www.nytimes.com/2026/03/18/technology/turing-award-winners-quantum-cryptography.html) the 2026 Turing Award for inventing quantum cryptography.

I am incredibly pleased to see them get this recognition. I have always thought the technology to be fantastic, even though I think it’s largely unnecessary. I wrote up my thoughts back in 2008, in an essay titled “Quantum Cryptography: As Awesome As It Is Pointless.”

Back then, I wrote:

> While I like the science of quantum cryptography—my undergraduate degree was in physics—I don’t see any commercial value in it. I don’t believe it solves any security problem that needs solving. I don’t believe that it’s worth paying for, and I can’t imagine anyone but a few technophiles buying and deploying it. Systems that use it don’t magically become unbreakable, because the quantum part doesn’t address the weak points of the system.
>
> Security is a chain; it’s as strong as the weakest link. Mathematical cryptography, as bad as it sometimes is, is the strongest link in most security chains. Our symmetric and public-key algorithms are pretty good, even though they’re not based on much rigorous mathematical theory. The real problems are elsewhere: computer security, network security, user interface and so on.
>
> Cryptography is the one area of security that we can get right. We already have good encryption algorithms, good authentication algorithms and good key-agreement protocols. Maybe quantum cryptography can make that link stronger, but why would anyone bother? There are far more serious security problems to worry about, and it makes much more sense to spend effort securing those.
>
> As I’ve often said, it’s like defending yourself against an approaching attacker by putting a huge stake in the ground. It’s useless to argue about whether the stake should be 50 feet tall or 100 feet tall, because either way, the attacker is going to go around it. Even quantum cryptography doesn’t “solve” all of cryptography: The keys are exchanged with photons, but a conventional mathematical algorithm takes over for the actual encryption.

What about quantum computation? I’m [not worried](https://www.schneier.com/essays/archives/2018/09/cryptography_after_t.html); the math is ahead of the physics. Reports of progress in that area are [overblown](https://eprint.iacr.org/2025/1237). And if there’s a security crisis because of a quantum computation breakthrough, it’s because our systems aren’t crypto-agile.

Tags: [history of cryptography](https://www.schneier.com/tag/history-of-cryptography/), [quantum computing](https://www.schneier.com/tag/quantum-computing/), [quantum cryptography](https://www.schneier.com/tag/quantum-cryptography/)

[Posted on March 31, 2026 at 7:05 AM](https://www.schneier.com/blog/archives/2026/03/inventors-of-quantum-cryptography-win-turing-award.html) •
[5 Comments](https://www.schneier.com/blog/archives/2026/03/inventors-of-quantum-cryptography-win-turing-award.html#comments)

### Comments

Paul •
[March 31, 2026 7:28 AM](https://www.schneier.com/blog/archives/2026/03/inventors-of-quantum-cryptography-win-turing-award.html/#comment-453257)

Missing a there! 🙂

Who? •
[March 31, 2026 11:00 AM](https://www.schneier.com/blog/archives/2026/03/inventors-of-quantum-cryptography-win-turing-award.html/#comment-453262)

A cryptographically relevant quantum computer (“CRQC”) may not be as good as it sounds for our society. Recently, requirements to break secp256k1 have been lowered to only

Clive Robinson •
[March 31, 2026 12:36 PM](https://www.schneier.com/blog/archives/2026/03/inventors-of-quantum-cryptography-win-turing-award.html/#comment-453263)

@ Bruce,

> “Charles Bennett and Gilles Brassard have won the 2026 Turing Award for inventing quantum cryptography.”

There is an interesting pre-story, in the fact that the work that lead up to it was a thought experiment to invent un-forgable currency using quantum wells which Gilles Brassard has talked about inthe past.

He’s also mentioned it was not secure due to an acoustic side channels due to being able to hear the polarisers changing position, which was a useful diagnostic aid.

But the big issue is the “medium” the photons travel in.

This limited the range to a few tens of meters originally that brings us to,

> “While I like the science of quantum cryptography—my undergraduate degree was in physics—I don’t see any commercial value in it. I don’t believe it solves any security problem that needs solving. I don’t believe that it’s worth paying for, and I can’t imagine anyone but a few technophiles buying and deploying it.”

Nearly all the issues are to do with the channel medium which has improved significantly recently.

But as the Chinese have been proving the use of quantum entangled particles in the medium of “space” can solve many of these and may in fact be the only way we can get Secure Key Distribution between satellites that are going to be up in space for a quarter of a century to work, and they are becoming rather more numerous of late. Not just for military applications but civil as well.

The real issue is “terrestrial internets” unlike space systems that are mostly “point to point” they are “multipoint to multipoint”, hence your,

> “The real problems are elsewhere: computer security, network security, user interface and so on.”

As I’ve mentioned before QKD does not work with “switches” and like “repeaters” they are not currently secure.

The thing is, is this actually something that will always be an issue, or is it something we are working toward a solution for?

I won’t go into details but people are working on solving them in various ways.

Thus the question devolves down to what do we mean by “secure”?

I’m firmly convinced that we can have real security in some areas…

BUT, that we “can not” and more importantly “will not” be allowed to have “full security” in consumer and commercial equipment.

As I’ve pointed out for quite some time it’s in part a question of how you make and manage a system where,

1, The “Security End Point” and what follws is
2, Securely beyond the “communications End Point”.

As can be seen the security success of E2EE has been killed by “Client Side Scanning” that Apple started putting in their products.

But… As I’ve pointed out and proved in the past, you can create a “plaintext” that has a “covert channel” within in it that can not be “proved” to exist and is deniable to any 3rd Party Observer.

But others have recently used the same reasoning to show that Guide Rails on LLM’s irrespective of input, output, or both will always be subject to being “jail broken” by simple “Crypto”.

So we know that there are some things that “observers” can not do, thus actual Shannon “Perfect Security” can be had with appropriate system design.

Ray Dillinger •
...