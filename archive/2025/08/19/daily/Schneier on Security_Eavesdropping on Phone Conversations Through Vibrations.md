---
title: Eavesdropping on Phone Conversations Through Vibrations
url: https://www.schneier.com/blog/archives/2025/08/eavesdropping-on-phone-conversations-through-vibrations.html
source: Schneier on Security
date: 2025-08-19
fetch_date: 2025-10-07T00:49:03.222698
---

# Eavesdropping on Phone Conversations Through Vibrations

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

## Eavesdropping on Phone Conversations Through Vibrations

Researchers have managed to [eavesdrop](https://dl.acm.org/doi/abs/10.1145/3734477.3734708) [on](https://www.psu.edu/news/engineering/story/conversations-remotely-detected-cellphone-vibrations-researchers-report) cell phone voice conversations by using radar to detect vibrations. It’s more a proof of concept than anything else. The radar detector is only ten feet away, the setup is stylized, and accuracy is poor. But it’s a start.

Tags: [academic papers](https://www.schneier.com/tag/academic-papers/), [AI](https://www.schneier.com/tag/ai/), [cell phones](https://www.schneier.com/tag/cell-phones/), [eavesdropping](https://www.schneier.com/tag/eavesdropping/)

[Posted on August 18, 2025 at 7:02 AM](https://www.schneier.com/blog/archives/2025/08/eavesdropping-on-phone-conversations-through-vibrations.html) •
[7 Comments](https://www.schneier.com/blog/archives/2025/08/eavesdropping-on-phone-conversations-through-vibrations.html#comments)

### Comments

Clive Robinson •
[August 18, 2025 11:23 AM](https://www.schneier.com/blog/archives/2025/08/eavesdropping-on-phone-conversations-through-vibrations.html/#comment-447243)

@ Bruce, ALL

With regards,

> “It’s more a proof of concept than anything else … But it’s a start”

And it has a long way to go, with a lot of sorrow to happen as we go.

All mechanical vibrations contain energy and that can be used as a side channel.

It’s the reason I don’t use the very out of date expression “air gapping” and now use “Energy Gapping” when talking about “Emissions Security”.

It’s also why I keep warning that more “active transducers” that convert one energy type/source to another are bidirectional than are not.

Think of a DC motor it is actively converting DC current in the windings to a form of AC current but also to mechanical energy. But it is also a generator working in opposition (hence “Back EMF”). And this bidirectionally is essential to them not self destructing when starting up.

Now consider a thin semi-flexible plate like a glass window. It is transparent to some forms of energy but absorbs or transmits to others.

It’s designed to be effectively transparent to visible light as that passes mostly through the glass by transmission with some absorption losses being converted to thermal energy (a sure indicator “that work is being done”). Though some light will be reflected thus a light beam will change it’s reflection angle with any mechanical movement.

Acoustic energy is a form of mechanical energy and it will cause the glass to flex in response to the acoustic energy.

So shine a LASER on the glass at the right angle, and it will get modulated by the mechanical movement of the surface. So the signal you pick up from the reflection makes such a setup work as a long range microphone. This has been known as a “useful surveillance technology” from before the 1980’s

But we know sound can go through solid objects like glass because we hear it happening nearly every day of our lives much of the time.

Importantly though we notice that put a near vacuum between two mechanically isolated glass plates –double glazing– and the level of the sound drops significantly. Not because it is absorbed, but because the vacuum gap breaks the transmission of the mechanical energy. But as the light still goes through the LASER mic can thus be used against any reflective object on the other side of Double Glazed windows.

It’s the same principle at work here. All that is different is the the frequency of the Electromagnetic”(EM) energy is a lot lot lower for a RADAR system than it is for the LASER mic.

But this has consequences the inverse of frequency is wavelength, and there areca number of limitations that arise. Acoustic wave length is the speed of sound divided by the “Acoustic Frequency”(AF). The radio wavelength is the “speed of light” divided by the “Radio Frequency”(RF).

The difference in AF and RF of the same wavelength is ~300/300,000,000 or 1:1,000,000 or one to a million. Thus the minimum RF frequency has to be a million times the maximum AF where the first “null” in the conversion spectrum happens usually you try to work below 1/16th of that so with the maximum AF frequency being around 4kHz the minimum RF frequency would have to be 64,000,000,000 or 64Ghz. With the lowest audio frequency being around 10Hz that would be 160,000,000 or 160MHz.

So as 64GHz is not practical, various tricks would have to be used. The first is use an algorithm to invert the frequency spectrum roll off. Unfortunately that makes high frequency noise have a very significant reduction on signal to boise ratio.

Another trick is to use not the speech frequency, but the speech envelop which would be about 200Hz so 3,200,000,000 or 3.2GHz thus you could use with some loss the “Industrial Scientific and Medical”(ISM) band, so existing WiFi units close to the target, or strip down a microwave oven to get a greater range (with optional “Crispy Fried Critter”(CFC) as a side effect to the system operators, so “TinFoil Hats”(TFH) as “Personal Protective Equipment”(PPE) not an optional extra).

XYZZY •
[August 18, 2025 11:49 AM](https://www.schneier.com/blog/archives/2025/08/eavesdropping-on-phone-conversations-through-vibrations.html/#comment-447244)

Humanity rushes forward towards a time when no utterance and perhaps no thought can be private. All out of some desire to prevent some perceived future threat or desire for monetary profit. Morality all but forgotten. What is this professions responsibility?

René •
[August 18, 2025 12:23 PM](https://www.schneier.com/blog/archives/2025/08/eavesdropping-on-phone-conversations-through-vibrations.html/#comment-447245)

Seems a bit pointless. I assume the State security services eavesdrop on all mobile-phone communications anyway, so why would they need this?

Clive Robinson •
[August 18, 2025 1:26 PM](https://www.schneier.com/blog/archives/2025/08/eavesdropping-on-phone-conversations-through-vibrations.html/#comment-447246)

@ XYZZY,

With regards,

> Humanity rushes forward towards a time when no utterance and perhaps no thought can be private.

Not exactly. Like US Justice you chance of being subject to it’s downsides is inversely proportional to how much money you have.

In theory you could if you own your house and surrounds dig out from the basement down twenty or thirty feet and put in a nuclear bunker that with only minimal extra work on EMP / Shock protection would become a “SCIF” in effect “energy gapped” from the outside world.

You note,

> All out of some desire to prevent some perceived future threat or desire for monetary profit. Morality all but forgotten.

Have you read “The Great American Dream”[1] recently, all you are really saying is the same thing, but from a more realistic view point of it being seen with respect to being in a resource constrained environment. As...