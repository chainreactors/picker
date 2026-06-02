---
title: 1,000 Data Breaches Later, the Disclosure Lag is Worse Than Ever
url: https://www.troyhunt.com/1000-data-breaches-later-the-disclosure-lag-is-worse-than-ever/
source: Troy Hunt's Blog
date: 2026-06-01
fetch_date: 2026-06-02T06:33:15.673145
---

# 1,000 Data Breaches Later, the Disclosure Lag is Worse Than Ever

* [Home](https://www.troyhunt.com/)
* [Workshops](https://www.troyhunt.com/workshops/)
* [Speaking](https://www.troyhunt.com/speaking/)
* [Media](https://www.troyhunt.com/media/)
* [About](https://www.troyhunt.com/about/)
* [Contact](https://www.troyhunt.com/contact/)
* [Sponsor](https://www.troyhunt.com/sponsorship/)

**Sponsored by:**

# 1,000 Data Breaches Later, the Disclosure Lag is Worse Than Ever

01 June 2026

Today, I loaded the 1,000th data breach into [Have I Been Pwned](https://haveibeenpwned.com/?ref=troyhunt.com). Reflecting on that milestone number, I pondered how to mark the occasion in writing, and what immediately came to mind was a very simple question: why is it still needed? Especially considering the emergence of privacy regulations such as GDPR and CCPA in the 12 and a half years since I started HIBP, what possible purpose does it still serve? The title kinda gives the answer away, and the big number we hit today coincided with another pattern that makes everything worse: increasingly long lag times for disclosure.

This is all going to be anecdotal, and as far as I know, there are no hard numbers for me to cite, but the evidence is everywhere. Here's what I mean:

> New breach: Cruise operator Carnival was targeted in a ShinyHunters “pay or leak” attack last week. 8.7M records with 7.5M email addresses and loyalty program data were published yesterday. 85% were already in [@haveibeenpwned](https://x.com/haveibeenpwned?ref_src=twsrc%5Etfw&ref=troyhunt.com). Read more: [https://t.co/QhqNt0WucV](https://t.co/QhqNt0WucV?ref=troyhunt.com)
>
> — Have I Been Pwned (@haveibeenpwned) [April 24, 2026](https://x.com/haveibeenpwned/status/2047497445383528908?ref_src=twsrc%5Etfw&ref=troyhunt.com)

That was the 24th of April, five days after [news of the incident had broken](https://cyberinsider.com/carnival-corporation-probes-data-breach-after-claims-of-8-7m-records-theft/?ref=troyhunt.com). Given ShinyHunters' MO, Carnival would have known about the breach many days before they ratcheted up extortion pressure by announcing the impending leak on their website. The subsequent leak on the 24th was very public: an announcement was posted to the group's dark-web site, the data itself was published to their *clear-web* site, and industry commentary followed:

> 🚨 Massive Data Breach
>
> Carnival Corporation ([https://t.co/pGlchZ1yFy](https://t.co/pGlchZ1yFy?ref=troyhunt.com)) reportedly impacted — 8.7M+ customer records exposed
>
> 📊 Alleged data includes:
> • Full names & email addresses
> • Dates of birth & gender
> • Location data & loyalty program details
>
> 🎯 Linked to ShinyHunters… [pic.twitter.com/Fd8tNFPqpd](https://t.co/Fd8tNFPqpd?ref=troyhunt.com)
>
> — Intel and Breaches (@IBreaches) [April 24, 2026](https://x.com/IBreaches/status/2047764076785463722?ref_src=twsrc%5Etfw&ref=troyhunt.com)

Per that last post, the data was then reposted to all sorts of other places: hacking forums, Telegram channels, and who knows how many other, more private locations. The point is that it spread quickly, extensively, and, without any shadow of a doubt, Carnival were aware of this. [They then told people about it on the 27th... of May](https://www.maine.gov/agviewer/content/ag/985235c7-cb95-4be2-8792-a1252b4f8318/d6729ef2-7bb3-42d3-abdd-99a1dd8f2415.html?ref=troyhunt.com). According to [their press release that same day](https://api.kscope.io/ks-doc-view?key=fde6d8e0-6260-46ee-9286-9578b2baf99c&content=benznews&docid=146ca2a0b6b2c9132af22b2efdfcee546d60ba59&allow_back=true&ref=troyhunt.com), this was 43 days after learning about the incident. For more than 6 weeks, data breach victims whose names, dates of birth, email addresses, loyalty program details and, of course, their association with Carnival leaked to the public en masse had absolutely no idea of their exposure. And if they asked Carnival about it? Well:

> As recently as four days ago, we heard “I’m in the breach per HIBP, but Carnival is telling me there’s no breach!” [pic.twitter.com/YYmGm3NzEY](https://t.co/YYmGm3NzEY?ref=troyhunt.com)
>
> — Troy Hunt (@troyhunt) [May 28, 2026](https://x.com/troyhunt/status/2060082594818224480?ref_src=twsrc%5Etfw&ref=troyhunt.com)

So, why the delay? [Last week's press coverage](https://www.theregister.com/cyber-crime/2026/05/28/carnival-shinyhunters-cruised-off-with-6m-customer-records/5247808?ref=troyhunt.com) may give some insight:

> thorough and time-consuming analysis of the impacted data

Often, the reason I hear for disclosure lag is "we needed to fully assess the scope of exposed data before notifying people". The issue I have with this position is that it implies that even an early heads-up can't happen until there's a very comprehensive understanding of the impact. There are many things that take time to establish after a data breach: the jurisdiction each individual sits in, the precise data that was exposed about them and additional information that may be buried in terabytes of exfiltrated data in all sorts of different formats. But pulling out email addresses and sending early notification is *very* easy - I've literally done it a thousand times now.

This isn't just a Carnival issue; in fact, it was off the back of this next one only a few days later that I was prompted to write this post:

![](https://storage.ghost.io/c/fb/33/fb3391dc-723d-4e74-b95a-d641b5feb38e/content/images/2026/05/image-1.png)

FFS. 45 days. Even worse than Carnival. And like Carnival, *very* broadly distributed and easily accessible by the masses, including HIBP:

> New breach: Zara was named as a ShinyHunters victim last month, after which data containing 197k unique email addresses was published. Impacted data included customer support records, product SKUs and order IDs. 60% were already in [@haveibeenpwned](https://x.com/haveibeenpwned?ref_src=twsrc%5Etfw&ref=troyhunt.com). More: [https://t.co/0hIQbqoBCk](https://t.co/0hIQbqoBCk?ref=troyhunt.com)
>
> — Have I Been Pwned (@haveibeenpwned) [May 8, 2026](https://x.com/haveibeenpwned/status/2052650516304609420?ref_src=twsrc%5Etfw&ref=troyhunt.com)

I have a working theory that the disclosure lag is worsening in part due to the proliferation of class actions *immediately* following a breach. In my live stream last weekend, I did a quick search for the DentaQuest breach:

![](https://storage.ghost.io/c/fb/33/fb3391dc-723d-4e74-b95a-d641b5feb38e/content/images/2026/05/image-2.png)

Three of the first four results are all for class actions related to the breach, and there are two more class action results a little further down the page. [I've been raising concerns about the adverse impact of class actions for many years now](https://www.troyhunt.com/data-breaches-class-actions-and-ambulance-chasing/), and it's worse than I've ever seen. By a big margin, too.

It's not just me observing how the behaviour of these orgs appears to be influenced by how lawyers will respond, either. Have a read of this post from [Roby Joyce](https://en.wikipedia.org/wiki/Rob_Joyce?ref=troyhunt.com) (check out his bio if you don't already know why he's worth paying attention to) after he learned about his exposure in the ZenBusiness breach via HIBP:

What especially caught my eye was this sentence:

> That is not a customer-protection posture. That is a litigation posture.

This isn't about prioritising the customer, it's about protecting the organisation. I don't think most people understand that organisational accountability really lies with their shareholders, first and foremost. All the pleasantries around "customers are our number one priority" and "we take security seriously" are all secondary to shareholder happiness, and minimising the chances of getting their arses sued into oblivion is a big part of that.

Rob's quoted comment above came immediately after the response he received from ZenBusiness after asking them about the incident:

> If we determine that an incident resulted in the exposure of your protected PII, we will provid...