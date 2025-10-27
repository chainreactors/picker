---
title: US Disrupts Massive Cell Phone Array in New York
url: https://www.schneier.com/blog/archives/2025/09/us-disrupts-massive-cell-phone-array-in-new-york.html
source: Schneier on Security
date: 2025-09-25
fetch_date: 2025-10-02T20:40:49.589753
---

# US Disrupts Massive Cell Phone Array in New York

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

## US Disrupts Massive Cell Phone Array in New York

This is a [weird story](https://www.bbc.com/news/articles/cn4w0d8zz22o):

> The US Secret Service disrupted a network of telecommunications devices that could have shut down cellular systems as leaders gather for the United Nations General Assembly in New York City.
>
> The agency said on Tuesday that last month it found more than 300 SIM servers and 100,000 SIM cards that could have been used for telecom attacks within the area encompassing parts of New York, New Jersey and Connecticut.
>
> “This network had the power to disable cell phone towers and essentially shut down the cellular network in New York City,” said special agent in charge Matt McCool.
>
> The devices were discovered within 35 miles (56km) of the UN, where leaders are meeting this week.
>
> McCool said the “well-organised and well-funded” scheme involved “nation-state threat actors and individuals that are known to federal law enforcement.”
>
> The unidentified nation-state actors were sending encrypted messages to organised crime groups, cartels and terrorist organisations, he added.
>
> The equipment was capable of texting the entire population of the US within 12 minutes, officials say. It could also have disabled mobile phone towers and launched distributed denial of service attacks that might have blocked emergency dispatch communications.
>
> The devices were seized from SIM farms at abandoned apartment buildings across more than five sites. Officials did not specify the locations.

Wait; seriously? “Special agent in charge Matt McCool”? If I wanted to pick a fake-sounding name, I couldn’t do better than that.

*Wired* has [some more](https://www.wired.com/story/sim-farm-new-york-threatened-us-infrastructure-feds-say/) information and a lot more speculation:

> The phenomenon of SIM farms, even at the scale found in this instance around New York, is far from new. Cybercriminals have long used the massive collections of centrally operated SIM cards for everything from spam to swatting to fake account creation and fraudulent engagement with social media or advertising campaigns.
>
> […]
>
> SIM farms allow “bulk messaging at a speed and volume that would be impossible for an individual user,” one telecoms industry source, who asked not to be named due to the sensitivity of the Secret Service’s investigation, told WIRED. “The technology behind these farms makes them highly flexible—SIMs can be rotated to bypass detection systems, traffic can be geographically masked, and accounts can be made to look like they’re coming from genuine users.”

Tags: [cell phones](https://www.schneier.com/tag/cell-phones/), [cyberattack](https://www.schneier.com/tag/cyberattack/), [denial of service](https://www.schneier.com/tag/denial-of-service/), [infrastructure](https://www.schneier.com/tag/infrastructure/), [telecom](https://www.schneier.com/tag/telecom/)

[Posted on September 24, 2025 at 7:09 AM](https://www.schneier.com/blog/archives/2025/09/us-disrupts-massive-cell-phone-array-in-new-york.html) •
[21 Comments](https://www.schneier.com/blog/archives/2025/09/us-disrupts-massive-cell-phone-array-in-new-york.html#comments)

### Comments

Jason Sewell •
[September 24, 2025 7:25 AM](https://www.schneier.com/blog/archives/2025/09/us-disrupts-massive-cell-phone-array-in-new-york.html/#comment-448195)

How do farms like this work around the fact that they’re adding the pressure of thousands of devices to a single (or maybe a small handful) of cell towers? Seems like that would either be easily detected and blocked or that it would disable that single tower or backhaul. I don’t quite understand how this would cause widespread failures unless it was exploiting a flaw of some kind.

Winter •
[September 24, 2025 7:39 AM](https://www.schneier.com/blog/archives/2025/09/us-disrupts-massive-cell-phone-array-in-new-york.html/#comment-448196)

The most explosive subject in the United Nations General Assembly would be the plight of the Palestinians in Gaza and the West-Bank. In the General Assembly, the suffering of the Palestinians were expected to get a lot of attention.

The current administration of the US has block entrance to the US to all Palestinians, even to those carry non-Palestinian or Israeli passports.

This plot might very well linked to this subject.

Alan •
[September 24, 2025 7:59 AM](https://www.schneier.com/blog/archives/2025/09/us-disrupts-massive-cell-phone-array-in-new-york.html/#comment-448197)

The story is weird because it appears to be sensationalized. The key sentence is this:

“Following multiple telecommunications-related imminent threats directed towards senior U.S. government officials this spring, the U.S. Secret Service began a protective intelligence investigation to determine the extent and impact these threats could have on protective operations,” he said.

From that sentence, it looks like this is what actually happened:

1. An SMS/telecom provider set up a SIM farm to rent to clients.
2. One of the clients used the SIM farm to send threats to US officials.
3. The Secret Service got involved and tracked down the SIM farm.
4. The Secret Service closed the SIM farm down, seized the equipment, and then published an over-sensationalized story with lots of movie-plot scenarios about the huge threat that it averted.

Stephen •
[September 24, 2025 8:08 AM](https://www.schneier.com/blog/archives/2025/09/us-disrupts-massive-cell-phone-array-in-new-york.html/#comment-448199)

Have seen comments in other forums to the effect that these are effectively rental cloned or falsified phones that can be used in any number of scams. Essentially a turnkey solution when part of the opening of a short con requires SMS. Might this be a self-financing way to build dual-purpose infrastructure that can flex into DoS attacks by saturating available bandwidth? Sure, I guess so, but very doubtful that was the primary purpose.

One would hope that carriers have mitigation tactics to kick misbehaving endpoints off the network or at least throttle them. If that requires some cooperation or at least orderly behavior from the rogue device, there are very likely multiple ways to subvert expectations and jam up the network.

Again, that’s a side hustle. People deploy capital to make a return. The capacity to push out a lot of SMS traffic, seemingly from multiple points of origin is the most obvious application for this relatively unsophisticated setup. The carriers may turn a blind eye because each of the fake SIMs that route scammy traffic through that tower comes with a monthly check.

The new Maslow’s hierarchy for cybersecurity bad actors seems to be greed > sloth > stupidity > malice.

Vesselin Bontchev •
[September 24, 2025 8:13 AM](https://www.schneier.com/blog/archives/2025/09/us-disrupts-massive-cell-phone-array-in-new-york.html/#comment-448200)

> “This network had the power to disable cel...