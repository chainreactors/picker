---
title: US Federal Court Rules Against Geofence Warrants
url: https://www.schneier.com/blog/archives/2024/08/us-federal-court-rules-against-geofence-warrants.html
source: Schneier on Security
date: 2024-08-27
fetch_date: 2025-10-06T18:08:25.834963
---

# US Federal Court Rules Against Geofence Warrants

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

## US Federal Court Rules Against Geofence Warrants

This is a big deal. A US Appeals Court [ruled](https://techcrunch.com/2024/08/13/us-appeals-court-rules-geofence-warrants-are-unconstitutional/) that geofence warrants—these are general warrants demanding information about all people within a geographical boundary—are unconstitutional.

The decision seems obvious to me, but you can’t take anything for granted.

Tags: [courts](https://www.schneier.com/tag/courts/), [data privacy](https://www.schneier.com/tag/data-privacy/), [geolocation](https://www.schneier.com/tag/geolocation/), [laws](https://www.schneier.com/tag/laws/)

[Posted on August 26, 2024 at 7:05 AM](https://www.schneier.com/blog/archives/2024/08/us-federal-court-rules-against-geofence-warrants.html) •
[12 Comments](https://www.schneier.com/blog/archives/2024/08/us-federal-court-rules-against-geofence-warrants.html#comments)

### Comments

R.Cake •
[August 26, 2024 9:13 AM](https://www.schneier.com/blog/archives/2024/08/us-federal-court-rules-against-geofence-warrants.html/#comment-440200)

Why, look at that. I had never realized that there is such a thing as a “geofence warrant”. But then, I do not live in the US either.

yet another bruce •
[August 26, 2024 10:46 AM](https://www.schneier.com/blog/archives/2024/08/us-federal-court-rules-against-geofence-warrants.html/#comment-440201)

I applaud the Fifth Circuit Court decision. The article refers to an opposite decision in a similar case made last month by the Fourth Circuit Court. I would have thought ideally Federal Law would be interpreted consistently across all 50 states. Circuit Courts seem anachronistic in an age where many legal cases are heard by teleconference.

[John Levine](https://jl.ly) •
[August 26, 2024 10:59 AM](https://www.schneier.com/blog/archives/2024/08/us-federal-court-rules-against-geofence-warrants.html/#comment-440202)

It’s worth reading [Orin Kerr’s take on this case](https://reason.com/volokh/2024/08/13/fifth-circuit-shuts-down-geofence-warrants-and-maybe-a-lot-more/).

The Fourth Circuit and the Colorado supreme court both recently decided that geofence warrants are OK, so this is a circuit split headed to the Supreme Court. Both based on Kerr’s analysis, and the fact that the Fifth Circuit has a history of legally extreme decisions, I wouldn’t count on this being upheld.

(I’m not saying the reasoning in this decision is wacky because it’s not, but it is definitely out of step with other courts.)

Victor Serge •
[August 26, 2024 2:17 PM](https://www.schneier.com/blog/archives/2024/08/us-federal-court-rules-against-geofence-warrants.html/#comment-440203)

!!

> seems obvious to me, but you can’t take anything for granted

Gosh, yah. Take Signal for example, you’d think after the “Edwardian Revelations” their users would’ve realized we are ALL targeted endpoints, and yet the only secure way of using it via SEIF airgaps, like JS partially details, [‘https… github…com/johnshearing/PrivateKeyVault], makes Signal completely redundant.

TEXT> PGP> QRCODE PARADE> MP4 Video> XMIT via WIREGAURD or TOR or Signal…> MP4> QRCODE> PGP> TEXT, for example. Land of the free, right? HUH! Fair enuf for your tiny QKI maybe.

But do you really want to stick your poker in that fire? Targeted WITH a huge bullseye painted on your back. Who wins? You heard Jesselyn Radack. ‘https://whisper.exposefacts.org/staff/

You’ll be dripping from their eye teeth for decades, if they LIKE you.

lurker •
[August 26, 2024 7:55 PM](https://www.schneier.com/blog/archives/2024/08/us-federal-court-rules-against-geofence-warrants.html/#comment-440207)

“This is a big deal.”

Yeah, right. The Fourth Circuit says you can, the Fifth Circuit says you can’t. It’ll have to go to the Supremes for a better answer. And Google’s gesture of flicking the data down to the device won’t be so much of an improvement for the perps being sought by the LEAs, because they will never turn Location Services OFF.

Clive Robinson •
[August 28, 2024 11:37 AM](https://www.schneier.com/blog/archives/2024/08/us-federal-court-rules-against-geofence-warrants.html/#comment-440232)

@ Victor Serge,

Re : Air gap solution is insecure and exploitable.

You mention,

<https://github.com/johnshearing/PrivateKeyVault/blob/master/README.md>

And whilst with it’s clear plastic box it looks like it is secure it’s not.

Firstly it talks of swapping the memory card equivalent of “the boot drive” that makes it a faux-HSM with another card to make it Internet-Usable or similar via externally connected communications… That is a very very bad idea.

Because it ignores the fact that the Pi2 has the equivalent of a boot up BIOS ROM that can be over-written as can most SoC chips.

We went through this issue years ago with the ideas behind BadBIOS, and before that the spat between the UK Government and Guardian Newspaper, that resulted in “Tweedle-dee and Tweedle-dum” of GCHQ or similar “on a day trip to London”. The result of which was photographs published “double page” in the Guardian that identified chips on a computer motherboard that provably had Flash-ROM or equivalent that could be subverted by malware etc known to GCHQ or Hanslope Park. The number was quite significant. At the time I did point out that it would be usefull for students of security to learn from.

Also the device as described has no RF or acoustic segregation that is present or reliable. Thus it not just leaks energy into the environment it is susceptable to energy from the environment as well (see EMC training info to get nice easy to understand info on this).

Most if not all communications paths are bi-directional and the are all susceptible to “covert channels” of one form or another (something I’ve warned about with commercial “Data Diodes” pumps and sluices, oft used for security segregation).

All that is actually required is the parts that Claude Shannon and others identified getting on for a century ago that became the “Shannon Channel” model which fundamentally underlies “Information Theory” that “came of age” during the 1960’s. And in turn also is the underlying model that TEMPEST and EmSec is built on, even though what we now call Emission Security” was being exploited during “The Great War” or World War I in 1914-18.

We happen to actually know that these “energy channels” are exploitable with very little equipment these days as the WWI exploits suggest. The use of an old Android phone can when close (say tapped under the table) will pick up enough radiated signal to break both Symmetric and Asymmetric crypto. Grad Students have done this practically and published it.

Further it is known from earlier work done in the UK Cambridge Computer Labs set up by Emeritus Prof Ross J. Anderson that directed EM Radiation can fritz an IBM secure True Random Number Generator, and their paper won a Usenix award. Over on the “Light the blue touch paper” blog, I told ...