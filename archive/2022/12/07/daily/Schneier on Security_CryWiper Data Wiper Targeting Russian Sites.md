---
title: CryWiper Data Wiper Targeting Russian Sites
url: https://www.schneier.com/blog/archives/2022/12/crywiper-data-wiper-targeting-russian-sites.html
source: Schneier on Security
date: 2022-12-07
fetch_date: 2025-10-04T00:50:27.517176
---

# CryWiper Data Wiper Targeting Russian Sites

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

## CryWiper Data Wiper Targeting Russian Sites

Kaspersky is [reporting](https://www.kaspersky.com/blog/crywiper-pseudo-ransomware/46480/) on a data wiper masquerading as ransomware that is targeting local Russian government networks.

> The Trojan corrupts any data that’s not vital for the functioning of the operating system. It doesn’t affect files with extensions .exe, .dll, .lnk, .sys or .msi, and ignores several system folders in the C:\Windows directory. The malware focuses on databases, archives, and user documents.
>
> So far, our experts have seen only pinpoint attacks on targets in the Russian Federation. However, as usual, no one can guarantee that the same code won’t be used against other targets.

Nothing leading to an attribution.

News [article](https://arstechnica.com/information-technology/2022/12/never-before-seen-malware-is-nuking-data-in-russias-courts-and-mayors-offices/).

Slashdot [thread](https://it.slashdot.org/story/22/12/03/0044234/new-crywiper-data-wiper-targets-russian-courts-mayors-offices).

Tags: [data destruction](https://www.schneier.com/tag/data-destruction/), [malware](https://www.schneier.com/tag/malware/), [ransomware](https://www.schneier.com/tag/ransomware/), [Russia](https://www.schneier.com/tag/russia/)

[Posted on December 6, 2022 at 7:04 AM](https://www.schneier.com/blog/archives/2022/12/crywiper-data-wiper-targeting-russian-sites.html) •
[13 Comments](https://www.schneier.com/blog/archives/2022/12/crywiper-data-wiper-targeting-russian-sites.html#comments)

### Comments

Jan Doggen •
[December 6, 2022 11:07 AM](https://www.schneier.com/blog/archives/2022/12/crywiper-data-wiper-targeting-russian-sites.html/#comment-413442)

Dilemma. On the one hand, malware is simply bad, and innocent people may be hit by the consequences, but OTOH given the atrocities of Russia in Ukraine (and earlier, in other countries) I’m tempted to think ‘Hit Russia with everything available’ until they pull out.

Clive Robinson •
[December 6, 2022 11:34 AM](https://www.schneier.com/blog/archives/2022/12/crywiper-data-wiper-targeting-russian-sites.html/#comment-413445)

@ Bruce, ALL,

There is a bit of a contoversy comming out over this to do with the Random Number Generator CryWiper uses.

It’s refered to as the “Mersenne Vortex”, not “Mersenne Twister” and it’s claimed it’s usage is somehow both unusual thus indicative enough for “attribution”.

From the ARS article,

> *“The name of the algorithm is the Mersenne Vortex PRNG. The algorithm is rarely used, so the commonality stuck out.”*

Howrver a little search on “Mersenne Vortex” indicates the algorithm is in the standard librarirs from C++11 onwards. It’s also in GCC, and many other “standard libraries”.

Now some may wonder if the algorithms are somehow different as they have slightly different names?

Simple answer is we don’t know…

The original Mersenne Twister algorithm was found to have some deficiencies thus got a couple of little upgrades but people followed habit with names, so yes there is more than one Mersenne Twister algorithm…

So unless someone who actually has the CryWiper code digging out the PRNG via debug/reverse\_engineer etc and checking, I guess we will have to wait and see.

&ers •
[December 6, 2022 12:08 PM](https://www.schneier.com/blog/archives/2022/12/crywiper-data-wiper-targeting-russian-sites.html/#comment-413448)

I don’t understand why on earth should anyone quote

hxxps://www.nytimes.com/2017/10/10/technology/kaspersky-lab-israel-russia-hacking.html

Just ignoring them is the best we can do. Anything they say is biased.

Ray Dillinger •
[December 6, 2022 12:21 PM](https://www.schneier.com/blog/archives/2022/12/crywiper-data-wiper-targeting-russian-sites.html/#comment-413449)

‘Mersenne Vortex’ in the Linux libraries is a correction of some perceived flaws with the Mersenne Twister. I don’t remember exactly what flaws. Nor have I a copy of this malware to dig through and see which binary matches.

That said, I dispute the claim that Mersenne Vortex is sufficiently uncommon to base attribution on. As Clive pointed out, standard libraries on a couple of standard platforms puts it well in the range of common tools.

Based on no special evidence beyond the daily news, however, I would suspect a Ukrainian, a member of the Ukrainian Diaspora, or Ukrainian sympathizer, likely acting without the knowledge or approval of any government.

There’s also a chance that it’s an act of cyber warfare undertaken specifically by the Ukrainian government.

And the latter case is in very murky territory as far as whether or not to condemn it.

On one hand, it’s clearly targeted at Russia, and with reasonable care to prevent damage in other countries. That makes it quasi-legitimate as an act of war.

On the other hand, it’s not specifically deployed against military targets; it’s much more general, and closer to being an attack on general infrastructure. And that makes it less legitimate as an act of war.

And on one foot, it’s targeted against the infrastructure of a nation that has routinely been committing atrocities against civilians and war crimes against the general infrastructure of Ukraine, so it’s turnabout. Which is not really okay under the Geneva Suggestions, but as long as Ukraine’s civilian population is manifestly suffering more under Russian attacks than any discomfort this brings to Russians, I don’t think I’d condemn it.

And on the other foot, it releases malware with a damaging payload out into the wild where in the hands of crooks and miscreants it will most assuredly be used in many other ways, most of which have nothing to do with any war whether the military use can be justified or not. So beyond being an immediate attack on Russia, it becomes a secondary attack against the general infrastructure of the world at large. And that’s not okay.

All told? Complicated. If it’s an act of war then it’s not one that would comply with the Geneva Convention. But considering the enormous scale of war crimes of the nation it’s being used against, and the fact that any damage it may do is drastically smaller than the damage Ukraine has suffered, and its likely short-term effect until the bugs it exploits are fixed, I am not terribly upset by its use.

Andy •
[December 6, 2022 1:05 PM](https://www.schneier.com/blog/archives/2022/12/crywiper-data-wiper-targeting-russian-sites.html/#comment-413451)

@Jan Doggen be careful what you’re wishing for. The virus is not hitting Russian military, just any computer in Russia… It may be holding your bank account, medication, and more

Clive Robinson •
[December 6, 2022 4:46 PM](https://www.schneier.com/blog/archives/2022/12/crywiper-data-wiper-targeting-russian-sites.html/#comment-413453)

@ Andy, Ray Dillinger, Jan Doggen,

Re : Who benifits the most?

> “The virus is not hitting Russian military, just any computer in Russia… “

Actually not “any computer in Russia...