---
title: YubiKey Side-Channel Attack
url: https://www.schneier.com/blog/archives/2024/09/yubikey-side-channel-attack.html
source: Schneier on Security
date: 2024-09-07
fetch_date: 2025-10-06T18:30:42.541539
---

# YubiKey Side-Channel Attack

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

## YubiKey Side-Channel Attack

There is a side-channel attack against YubiKey access tokens that allows someone to clone a device. It’s a [complicated attack](https://ninjalab.io/wp-content/uploads/2024/09/20240903_eucleak.pdf), requiring the victim’s username and password, and physical access to their YubiKey—as well as some technical expertise and equipment.

Still, nice piece of security analysis.

Tags: [academic papers](https://www.schneier.com/tag/academic-papers/), [cloning](https://www.schneier.com/tag/cloning/), [security analysis](https://www.schneier.com/tag/security-analysis/), [security tokens](https://www.schneier.com/tag/security-tokens/), [side-channel attacks](https://www.schneier.com/tag/side-channel-attacks/)

[Posted on September 6, 2024 at 11:16 AM](https://www.schneier.com/blog/archives/2024/09/yubikey-side-channel-attack.html) •
[17 Comments](https://www.schneier.com/blog/archives/2024/09/yubikey-side-channel-attack.html#comments)

### Comments

ZN •
[September 6, 2024 12:27 PM](https://www.schneier.com/blog/archives/2024/09/yubikey-side-channel-attack.html/#comment-440375)

To fix it yubikey reportedly replaced the Infineon upstream library for ECC with their own in the keys’ firmware.

Az •
[September 6, 2024 1:04 PM](https://www.schneier.com/blog/archives/2024/09/yubikey-side-channel-attack.html/#comment-440376)

In fact all products relying on the ECDSA of Infineon
cryptographic library running on an Infineon security microcontroller are affected by the attack.
We estimate that the vulnerability exists for more than 14 years in Infineon top secure chips.
These chips and the vulnerable part of the cryptographic library went through about 80 CC
certification evaluations of level AVA VAN 4 (for TPMs) or AVA VAN 5 (for the others) from 2010
to 2024 (and a bit less than 30 certificate maintenances)

This looks to me like a rather big deal. It doesn’t just undermine trust in Infineon, but IMO also in the certification evaluation process.

Clive Robinson •
[September 6, 2024 2:37 PM](https://www.schneier.com/blog/archives/2024/09/yubikey-side-channel-attack.html/#comment-440377)

Well as has been noted in the past,

“Attacks only get better with time”

And I suspect that some did not realise that “time” is what some “side channel” attacks are all about.

For those who’ve not downloaded the paper, it’s 88pages and quite a read…

So you might want to wait for the “Students Notes” version…

The question that many will have to ponder is,

“Is there any single security system that is secure?”

To which the answer these days appears to be “No” for a multitude of reasons.

Thus the second question that will come to mind is,

“Can layering up security with systems that work on entirely different principles work?”

To which I suspect the answer will be “No” due to two reasons,

Firstly, the fact that the independent system layers will have to in effect “reduce down to a single channel” at some point where vulnerabilities will probably appear due to amongst other things “increasing complexity / attack surface”.

Secondly, the laws of nature. That is “all work” requires an energy differential and has losses.

The second point is important because such losses get modulated / imprinted with “information” that can carry other “sensitive information” with it.

I’ve talked about this off and on since the 1990’s and the issues which came to general view with “Smart Cards” and the various side channel attacks such as “Simple Power Analysis”(SPA) and “Differential Power Analysis”(DPA) that could be used on EM radiation (I also noted that Paul Kocher patenting the general attack methodology that had been known since the 1980’s would have detrimental effects on security…).

Any way I shall read more into the “attack methodology” and mull over what further risks it will “bring to the game” as such things never work in isolation.

[Axon](https://www.h-i-r.net) •
[September 6, 2024 3:09 PM](https://www.schneier.com/blog/archives/2024/09/yubikey-side-channel-attack.html/#comment-440379)

I’ve been recommending these to friends and family for years, and of course, now the question is coming up “are these still safe?” and “do I need to replace mine?”

So far, my advice is to treat your physical YubiKey just like you’d treat any other physical key that could potentially be stolen, or copied by a bad actor with a few minutes of covert access. Don’t leave it unattended in a public place, in your car, or likewise.

I’m curious what others think about this, though.

Matt Thompson •
[September 6, 2024 3:47 PM](https://www.schneier.com/blog/archives/2024/09/yubikey-side-channel-attack.html/#comment-440380)

I was at first concerned thinking “I have to buy new Yubikeys?!” when I saw the news. But then I read about the attack and, frankly, if someone wants to do all that for anything I have in my life protected by my Yubikeys, I think they deserve to get it.

Heck, I’d sort of feel honored.

Jack •
[September 6, 2024 4:22 PM](https://www.schneier.com/blog/archives/2024/09/yubikey-side-channel-attack.html/#comment-440381)

In light of this, is there any “quality” analysis of the pros/cons of some of the “open source” alternatives to Yubikey eg Soma Solokey Nitrokey Onlykeys etc.

I only ask as I’m acutely aware that open-source != secure

Clive Robinson •
[September 6, 2024 6:12 PM](https://www.schneier.com/blog/archives/2024/09/yubikey-side-channel-attack.html/#comment-440384)

When it comes to EM signals used in Power Analysis, one of the suggestions almost always made is,

“Make the ‘Signal to noise ratio’ worse by ‘randomly adding noise’.”

Whilst in theory it appears like a good idea, in practice for various reasons it’s nowhere near as effective as it is thought to be.

Part of that is the ‘Async vs Sync’ issue. It is assumed that the observer is using time based synchronisation to align waveforms to average the noise out. So if you make your signal asynchronous to time the attacker can not average out the noise by averaging up the signal.

In practice all the attacker needs is some form of synchronising signal to re-aline time so they can average up the signal.

There are a number of ways to do this “Fourier Transforms”(FTs), that in effect are a frequency based “matched filter” similar to those used to synchronize “Spread Spectrum”(SS) “Low Probability of Intercept”(LPI) systems. A variation on FTs using sequency rather than frequency known as “Walsh Transforms”(WT) and more recently the use of “Wavelets”.

There is a paper (PDF) that is reasonably readable,

[https://web.archive.org/web/20160304061330/http://csrc.nist.gov/groups/STM/cmvp/documents/fips140-3/physec/papers/physecpaper14.pdf](https://web.archive.org/web/20160304061330/http%3A//csrc.nist.gov/groups/STM/cmvp/documents/fips140-3/physec/papers/physecpaper14.pdf)

That explains using both Wavelets and ‘Simulated Annealing” to pull the sign...