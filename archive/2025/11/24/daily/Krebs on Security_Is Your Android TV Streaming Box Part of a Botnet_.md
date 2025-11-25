---
title: Is Your Android TV Streaming Box Part of a Botnet?
url: https://krebsonsecurity.com/2025/11/is-your-android-tv-streaming-box-part-of-a-botnet/
source: Krebs on Security
date: 2025-11-24
fetch_date: 2025-11-25T03:13:32.888169
---

# Is Your Android TV Streaming Box Part of a Botnet?

Advertisement

[![](/b-sysdig/1.png)](https://content.foleon.com/sysdig/sysdig-cloud-defense-report-2025/?utm_source=krebs-on-security&utm_medium=display&utm_campaign=aware_amer_the-right-way_na_ung_display&utm_content=AD000460_1240x110)

Advertisement

[![](/b-gartner/4.jpg)](https://www.gartner.com/en/conferences/na/identity-access-management-us?utm_source=krebs&utm_medium=banner&utm_campaign=EVT_NA_2025_IAM20_PP_MP6_KREBSONSECURITY)

[![Krebs on Security](https://krebsonsecurity.com/wp-content/uploads/2021/03/kos-27-03-2021.jpg)](https://krebsonsecurity.com/ "Krebs on Security")

[Skip to content](#content "Skip to content")

* [Home](https://krebsonsecurity.com/)
* [About the Author](https://krebsonsecurity.com/about/)
* [Advertising/Speaking](https://krebsonsecurity.com/cpm/)

# Is Your Android TV Streaming Box Part of a Botnet?

November 24, 2025

[3 Comments](https://krebsonsecurity.com/2025/11/is-your-android-tv-streaming-box-part-of-a-botnet/#comments)

On the surface, the **Superbox** media streaming devices for sale at retailers like **BestBuy** and **Walmart** may seem like a steal: They offer unlimited access to more than 2,200 pay-per-view and streaming services like **Netflix**, **ESPN** and **Hulu**, all for a one-time fee of around $400. But security experts warn these TV boxes require intrusive software that forces the user’s network to relay Internet traffic for others, traffic that is often tied to cybercrime activity such as advertising fraud and account takeovers.

![](https://krebsonsecurity.com/wp-content/uploads/2025/11/superbox-walmart.png)

Superbox bills itself as an affordable way for households to stream all of the television and movie content they could possibly want, without the hassle of monthly subscription fees — for a one-time payment of nearly $400.

“Tired of confusing cable bills and hidden fees?,” Superbox’s website asks in a recent blog post titled, “Cheap Cable TV for Low Income: Watch TV, No Monthly Bills.”

“Real cheap cable TV for low income solutions does exist,” the blog continues. “This guide breaks down the best alternatives to stop overpaying, from free over-the-air options to one-time purchase devices that eliminate monthly bills.”

Superbox claims that watching a stream of movies, TV shows, and sporting events won’t violate U.S. copyright law.

“SuperBox is just like any other Android TV box on the market, we can not control what software customers will use,” the company’s website maintains. “And you won’t encounter a law issue unless uploading, downloading, or broadcasting content to a large group.”

![](https://krebsonsecurity.com/wp-content/uploads/2025/11/superbox-cheapcable.png)

There is nothing illegal about the sale or use of the Superbox itself, which can be used strictly as a way to stream content at providers where users already have a paid subscription. But that is not why people are shelling out $400 for these machines. The only way to watch those 2,200+ channels for free with a Superbox is to install several apps made for the device that enable them to stream this content.

Superbox’s homepage includes a prominent message stating the company does “not sell access to or preinstall any apps that bypass paywalls or provide access to unauthorized content.” The company explains that they merely provide the hardware, while customers choose which apps to install.

“We only sell the hardware device,” the notice states. “Customers must use official apps and licensed services; unauthorized use may violate copyright law.”

Superbox is technically correct here, except for maybe the part about how customers must use official apps and licensed services: Before the Superbox can stream those thousands of channels, users must configure the device to update itself, and the first step involves ripping out Google’s official Play store and replacing it with something called the “App Store” or “Blue TV Store.”

Superbox does this because the device does not use the official Google-certified Android TV system, and its apps will not load otherwise. Only after the Google Play store has been supplanted by this unofficial App Store do the various movie and video streaming apps that are built specifically for the Superbox appear available for download (again, outside of Google’s app ecosystem).

Experts say while these Android streaming boxes generally do what they advertise — enabling buyers to stream video content that would normally require a paid subscription — the apps that enable the streaming also ensnare the user’s Internet connection in a distributed residential proxy network that uses the devices to relay traffic from others.

**Ashley** is a senior solutions engineer at **Censys**, a cyber intelligence company that indexes Internet-connected devices, services and hosts. Ashley requested that only her first name be used in this story.

In a recent video interview, Ashley showed off several Superbox models that Censys was studying in the malware lab — including one purchased off the shelf at BestBuy.

“I’m sure a lot of people are thinking, ‘Hey, how bad could it be if it’s for sale at the big box stores?'” she said. “But the more I looked, things got weirder and weirder.”

Ashley said she found the Superbox devices immediately contacted a server at the Chinese instant messaging service **Tencent** **QQ**, as well as a residential proxy service called **Grass IO**.

## GET GRASSED

Also known as getgrass[.]io, Grass says it is “a decentralized network that allows users to earn rewards by sharing their unused Internet bandwidth with AI labs and other companies.”

“Buyers seek unused internet bandwidth to access a more diverse range of IP addresses, which enables them to see certain websites from a retail perspective,” the Grass website explains. “By utilizing your unused internet bandwidth, they can conduct market research, or perform tasks like web scraping to train AI.” ![](https://krebsonsecurity.com/wp-content/uploads/2025/11/grassio.png)

Reached via Twitter/X, Grass founder **Andrej Radonjic** told KrebsOnSecurity he’d never heard of a Superbox, and that Grass has no affiliation with the device maker.

“It looks like these boxes are distributing an unethical proxy network which people are using to try to take advantage of Grass,” Radonjic said. “The point of grass is to be an opt-in network. You download the grass app to monetize your unused bandwidth. There are tons of sketchy SDKs out there that hijack people’s bandwidth to help webscraping companies.”

Radonjic said Grass has implemented “a robust system to identify network abusers,” and that if it discovers anyone trying to misuse or circumvent its terms of service, the company takes steps to stop it and prevent those users from earning points or rewards.

Superbox’s parent company, **Super Media Technology Company Ltd.**, lists its street address as a UPS store in Fountain Valley, Calif. The company did not respond to multiple inquiries.

According to [this teardown by behindmlm.com](https://behindmlm.com/mlm-reviews/grass-review-wynd-labs-securities-fraud/), a blog that covers multi-level marketing (MLM) schemes, Grass’s compensation plan is built around “grass points,” which are earned through the use of the Grass app and through app usage by recruited affiliates. Affiliates can earn 5,000 grass points for clocking 100 hours usage of Grass’s app, but they must progress through ten affiliate tiers or ranks before they can redeem their grass points (presumably for some type of cryptocurrency). The 10th or “Titan” tier requires affiliates *to accumulate a whopping 50 million grass points, or recruit at least 221 more affiliates*.

Radonjic said Grass’s system has changed in recent months, and confirmed the company has a referral program where users can earn Grass Uptime Points by contributing their own bandwidth and/or by inviting other users to participate.

“Users are not required to participate in the referral program to earn Grass Uptime P...