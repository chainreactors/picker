---
title: Swimming Pools, Pee, and Trying to Delete Your Data From the Internet
url: https://www.troyhunt.com/swimming-pools-pee-and-trying-to-delete-your-data-from-the-internet/
source: Troy Hunt's Blog
date: 2026-07-03
fetch_date: 2026-07-04T05:49:47.478137
---

# Swimming Pools, Pee, and Trying to Delete Your Data From the Internet

* [Home](https://www.troyhunt.com/)
* [Workshops](https://www.troyhunt.com/workshops/)
* [Speaking](https://www.troyhunt.com/speaking/)
* [Media](https://www.troyhunt.com/media/)
* [About](https://www.troyhunt.com/about/)
* [Contact](https://www.troyhunt.com/contact/)
* [Sponsor](https://www.troyhunt.com/sponsorship/)

**Sponsored by:**

# Swimming Pools, Pee, and Trying to Delete Your Data From the Internet

03 July 2026

I can't recall if someone else originally came up with this saying or if I said it in some off-the-cuff comment and it just propagated, but since [it's often attributed back to me](https://www.standard.co.uk/lifestyle/how-to-delete-yourself-from-the-internet-a4384456.html?ref=troyhunt.com), I'll relay it here regardless:

> Trying to delete yourself from the internet is like trying to take piss out of a swimming pool

Depending on the publication, I'll tailor the saying to be either more broadly palatable or more, uh, "Australian", but the sentiment doesn't change: once data spreads on the internet, you can never put a lid on it. This is important in the context of data breaches because it speaks to the immutability of our exposed personal information. It also speaks to the limited practicality of services that promise to erase your data from the internet, and it's the constant outreach from these organisations looking for marketing opportunities on [Have I Been Pwned](https://haveibeenpwned.com/?ref=troyhunt.com) (HIBP) that's prompted me to write this.

Let's begin with those services, and because there are so many and I don't want to throw any of them under the bus, I won't name names. I also won't name them because whilst they're rather assertive in their marketing outreach, I do believe they're well-intentioned and I don't want to imply otherwise. And they have a role to play; it's just much more limited than is represented. The positioning is often around "data broker removal services", or "protect my data", or "remove my information from the internet". You'll find various companies providing these services by searching for those terms, or you can search for specific organisations... and find others hijacking the search term as they pay to market their brand in front of others. Usual internet marketing shadiness, of course, but IMHO it speaks volumes about the commercialisation of the data removal business.

These services all follow roughly the same marketing handbook:

1. Data brokers have your personal information, which they may obtain via both legitimate and dodgy means
2. It may be used for nefarious purposes such as identity theft, stalking, spam and other privacy violations
3. Pay us, and we'll ask the brokers to remove your data

So let's go through these points one by one, starting with the data broker claim, which is absolutely correct. Your data has value - "data is the new oil" - and there's business in obtaining and selling it. I've dealt with many of them personally over the years, primarily because they've had data breaches. [Master Deeds in South Africa](https://www.troyhunt.com/questions-about-the-massive-south-african-master-deeds-data-breach-answered/) was massive. [National Public data a couple of years ago](https://www.troyhunt.com/inside-the-3-billion-people-national-public-data-breach/) was many times larger. [Exactis](https://haveibeenpwned.com/Breach/Exactis?ref=troyhunt.com), [Adapt](https://haveibeenpwned.com/Breach/Adapt?ref=troyhunt.com), and many others have also been added to HIBP over the years. To the best of my knowledge, they're legally operating services, even if they may exist on the fringe of what most of us would consider "a bit dodgy" as far as respecting our personal information goes.

Which brings us to the second point about nefarious uses. There is a *very* broad spectrum of legitimacy across data brokers. Let's pick two extremes as far as the legality of the service goes. On the "very legally operating" end of things, we have [Experian](https://www.experian.com/?ref=troyhunt.com), and even if you don't like what they do, there's no arguing the fact that they're on the cleaner end of legitimacy and do provide valid services. At the other end, you have the likes of [LeakedSource](https://www.troyhunt.com/thoughts-on-the-leakedsource-take-down/) (and pretty much every other service with the word "Leak" in its name) that... well... just Google them. And there are many, many more at each end and everywhere in between. And a lot of it's very grey: different legal jurisdictions, different means of obtaining data, and different tolerances for adhering to opt-out requests.

But it's the data removal piece that's the real problem. If you pay one of the services in question to scrub you from the internet, I have no doubt they'll have some degree of success with the legally operating services. Those services will comply with legal requests and are adequately equipped to receive and process them. But the LeakedSources of the world? Not so much. And that's where the rub begins:

**Requests to remove personal information are only effective for services that are willing to honour them.**

That should sound profoundly obvious to anyone reading this now, but it doesn't really feature when you read the marketing material on data removal services. But I'm only just warming up...

Imagine trying to remove your data from here:

> 🚨🇺🇸 ShinyHunters has leaked the data of multiple companies...
>
> 🇺🇸 American Tower Corporation
>
> 🇺🇸 JCPenney & subsidiaries under Catalyst Brands & Authentic Brands Group
>
> 🇺🇸 Madison Square Garden Sports Corp.
>
> 🇺🇸 Ralph Lauren
>
> 🇺🇸 [https://t.co/08IaUnp1sx](https://t.co/08IaUnp1sx?ref=troyhunt.com) [pic.twitter.com/TvqanSTO1Y](https://t.co/TvqanSTO1Y?ref=troyhunt.com)
>
> — Dark Web Informer (@DarkWebInformer) [June 16, 2026](https://x.com/DarkWebInformer/status/2066906568101081220?ref_src=twsrc%5Etfw&ref=troyhunt.com)

That's a small snippet of the ShinyHunters website from a couple of weeks ago. At the time of writing, a bunch more data has been dumped, including only about 15 minutes before putting these words down in the draft blog post. These breaches have impacted tens of millions of people, including my wife courtesy of her having previously shopped at [Canada Goose](https://www.troyhunt.com/welcoming-the-philippine-government-to-have-i-been-pwned/). Now, let's see how you go about scrubbing her data from that incident. For all the data broker removal services I'll direct to this post later, how do you do that? Clearly, you can't. The pee is now in the pool, and you're not taking it back out. And it's not just "on the dark web" either, their Tor site links through to a clear web site hosting all the data:

![](https://storage.ghost.io/c/fb/33/fb3391dc-723d-4e74-b95a-d641b5feb38e/content/images/2026/07/image.png)

And that's just the beginning. Because we're talking about digitised data posted publicly, it replicates *like crazy*. There will be tens of thousands of copies of my wife's personal info floating around between personal stashes, Telegram channels and public hacking forums. That genie is *never* going back in the bottle, not unless we're talking about the narrow scope of a legally operating data broker, which raises another issue:

What legally operating broker is enriching their corpus from data breaches?! That's just not where the *legitimate* ones source info from. The data comes from surveys, exchanges with other services where you ticked the box to agree to the terms and conditions for exchanging data with "partners", public business directories, and even arrest records. Legal services, legal sources, legal processes. In one of the emails from a company looking for product placement, they described their plan as follows (bold is mine):

> a plan which allows you to remove your personal information from any URL **(where it's legal)** you find your personal information on

So what we're left with is data removal services being effective for lega...