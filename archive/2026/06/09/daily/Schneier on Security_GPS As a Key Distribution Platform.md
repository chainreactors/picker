---
title: GPS As a Key Distribution Platform
url: https://www.schneier.com/blog/archives/2026/06/gps-as-a-key-distribution-platform.html
source: Schneier on Security
date: 2026-06-09
fetch_date: 2026-06-10T06:17:17.272390
---

# GPS As a Key Distribution Platform

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

## GPS As a Key Distribution Platform

[This](https://www.404media.co/the-u-s-military-quietly-turned-gps-into-a-global-numbers-station-evidence-suggests/) is interesting:

> The U.S. military has likely been quietly broadcasting codes for its global encryption network using public GPS for nearly 20 years, turning each satellite into a hidden “numbers station,” according to Steven Murdoch…
>
> That means every device that uses GPS has been receiving hidden government information for years, and nobody outside the military knew it until now.
>
> […]
>
> Murdoch discovered that this particular sentinel was transmitted by all 31 operational satellites within a window of a few hours on May 26, 2011, potentially heralding the activation of a new operational system. He confirmed that this timeline coincided with the rollout of the military’s Over-the-Air Distribution (OTAD) and the Over-the-Air Rekeying (OTAR) by cross-referencing declassified documents, including a 2015 presentation about the dates of the operation.
>
> “There was a perfect match between the timeline and that presentation and the change points that were automatically identified from the data,” Murdoch said. “That was the smoking gun that made me think: This is what it’s for.”
>
> These automated systems replaced the cumbersome manual distribution of cryptographic keying material, allowing military GPS receivers around the world to be rekeyed remotely through satellite broadcasts rather than through onsite procedures.

Tags: [GPS](https://www.schneier.com/tag/gps/), [keys](https://www.schneier.com/tag/keys/), [military](https://www.schneier.com/tag/military/)

[Posted on June 9, 2026 at 11:06 AM](https://www.schneier.com/blog/archives/2026/06/gps-as-a-key-distribution-platform.html) •
[9 Comments](https://www.schneier.com/blog/archives/2026/06/gps-as-a-key-distribution-platform.html#comments)

### Comments

Clive Robinson •
[June 9, 2026 11:37 AM](https://www.schneier.com/blog/archives/2026/06/gps-as-a-key-distribution-platform.html/#comment-455049)

@ Bruce, ALL,

A thought to think on…

The modules that go into military GPS units are supposed to be,

1, Secure.
2, Tamper proof.

But… They are like all embedded systems “finite in capacity.

This means there is only so much Key Material (KeyMat) that can be securely stored within them.

Which means they will eventually either have to “reuse KeyMat”, be “reloaded with KeyMat”, or cease to function as the KeyMat is exhausted.

For various reasons this kind of precludes the use of “Shanon Perfect Secrecy” type systems (one of which is the OTP).

Thus the question arises of when will these secure modules “be beyond their shelf life”.

[John Pritchard](https://www.syntelos.io/) •
[June 9, 2026 12:14 PM](https://www.schneier.com/blog/archives/2026/06/gps-as-a-key-distribution-platform.html/#comment-455052)

See also [GPS OTAD] <https://share.google/Yk9f86cBEC9KWbrsW>

Vesselin Bontchev •
[June 9, 2026 1:16 PM](https://www.schneier.com/blog/archives/2026/06/gps-as-a-key-distribution-platform.html/#comment-455053)

I very much doubt that these are “keys”. More likely, they are ciphertext; a codebook-based one, where one code can mean a whole phrase.

Didier Frick •
[June 9, 2026 1:27 PM](https://www.schneier.com/blog/archives/2026/06/gps-as-a-key-distribution-platform.html/#comment-455054)

@clive robinson

isn’t the whole point of the article about remotely sending key material to those devices ?

Rontea •
[June 9, 2026 1:56 PM](https://www.schneier.com/blog/archives/2026/06/gps-as-a-key-distribution-platform.html/#comment-455056)

Fascinating to see how decades-old GPS signals quietly carried the backbone of military key distribution right over our heads the whole time.

Anonymous •
[June 9, 2026 3:09 PM](https://www.schneier.com/blog/archives/2026/06/gps-as-a-key-distribution-platform.html/#comment-455057)

The natural conclusion here is to use this for an RNG seed (joking of course, but…)

Clive Robinson •
[June 9, 2026 3:18 PM](https://www.schneier.com/blog/archives/2026/06/gps-as-a-key-distribution-platform.html/#comment-455058)

@ Didier Frick, ALL,

With regards your note of,

> “isn’t the whole point of the article about remotely sending key material to those devices”

No it’s actually about “updating of KeyMat in use”.

Which is not quite the same thing.

Look at it this way,

If I was to send you a new AES use-key as a plaintext “broadcast message” –which all GPS transmissions are– it would not be secure.

Further if I was to send the new use-key encrypted, each new use-key would need to be encrypted under the same update-key. So although more secure would not be sufficiently secure for quite a few applications [1].

Thus to be secure the actual use-key would need to be stored in advance in the secure module in a look-up table or similar and what would be sent encrypted would be an ID number or Pointer into the lookup table.

So if the unit is also “tamper proof” which it should be, then the table would be stored in “battery backed up RAM” or equivalent such that any attempt to access the table would cause it to be destroyed, thus keeping all past present and future use-keys secure.

The usual indicator that a crypto-module is tamper resistant / proof is that it has a “fill gun / device” access port (usually a 6-pin connector of the sort used for “green radio” audio ports. It is a serial device where a COMSEC Custodian / Guardian can put new crypto keys into the RAM table.

[1] Whilst not as secure as it could be OTAR is now a NATO standard[2] and also used in civilian emergency networks such as “Project 25″(P25). Implementations used for P25 have unfortunately been quite insecure with one actually capable of sending the use-key in plaintext.

[2] The history behind OTAR is somewhat interesting. It was designed and implemented by “David Winters” in London back nearly 40years ago. The real reason it was widely implemented was not security but cost reduction. Sending out COMSEC Custodians / Guardians or returning equipment under guardianship was eye wateringly expensive during the mid 1980’s. Worse was the cost of Key Management (KeyMan) covering just KeyGen and KeyMat audit. The fact that there was no known KeyMat loss for three decades shows that it at least was better than using some bloke called Walker and family, who apparently had a profitable line in Second Hand KeyMat sales.

Jon (a different Jon) •
[June 9, 2026 4:50 PM](https://www.schneier.com/blog/archives/2026/06/gps-as-a-key-distribution-platform.html/#comment-455059)

@Clive Robinson

I must disagree with you there. See, you’re presuming that everything is in the GPS device, which as you accurately noted is limited in space (but not by that much – NVRAM storage chips are vast these days).

Imagine a side channel, in which the actual encrypted data is transmitted in another way – and then the key to decrypt the data ...