---
title: Tech Firms Dismantle Botnet That Turned 1.3M TV Boxes Into Proxies
url: https://krebsonsecurity.com/2026/11/tech-firms-dismantle-botnet-that-turned-1-3m-tv-boxes-into-proxies/
source: Krebs on Security
date: 2026-11-03
fetch_date: 2026-11-04T08:19:36.252613
---

# Tech Firms Dismantle Botnet That Turned 1.3M TV Boxes Into Proxies

Advertisement

[![](/b-flashpoint/1.png)](https://flashpoint.io/ignite/vulnerability-intelligence/?utm_source=krebsonsecurity&utm_medium=display&utm_campaign=brand-vuln&utm_content=vuln-a)

Advertisement

[![](/b-flashpoint/6.png)](https://flashpoint.io/ignite/?utm_source=krebsonsecurity&utm_medium=display&utm_campaign=brand-ignite&utm_content=noise-a)

[![Krebs on Security](https://krebsonsecurity.com/wp-content/uploads/2021/03/kos-27-03-2021.jpg)](https://krebsonsecurity.com/ "Krebs on Security")

[Skip to content](#content "Skip to content")

* [Home](https://krebsonsecurity.com/)
* [About the Author](https://krebsonsecurity.com/about/)
* [Advertising/Speaking](https://krebsonsecurity.com/cpm/)

# Tech Firms Dismantle Botnet That Turned 1.3M TV Boxes Into Proxies

November 2, 2026

[7 Comments](https://krebsonsecurity.com/2026/11/tech-firms-dismantle-botnet-that-turned-1-3m-tv-boxes-into-proxies/#comments)

**Google** said today it worked with industry partners to dismantle a botnet made up of more than 1.3 million **Android** TV set-top boxes that ship with malicious software which secretly rents the user’s Internet connection out to strangers and conducts advertising fraud. Experts involved in the takedown say the action is likely to sever the botnet’s access to more than 10 million additional compromised systems, including other Internet of Things (IoT) products such as Android-based healthcare devices and karaoke machines.

A report from the **Google Threat Intelligence Group** (GTIG) said Google has severed ties with **Videostrong Technology Co.**, a TV box manufacturer in China that GTIG and other industry experts concluded was responsible for including malware that enrolled more than 1.3 million set-top boxes in a botnet dubbed “**XCPE**” (named after one of the malware’s core code components).

![](https://krebsonsecurity.com/wp-content/uploads/2026/11/xcpe-map.png)

The global distribution of XCPE botnet infections. Image: Google Threat Intelligence Group.

The report said the XCPE botnet loaded the user’s device with software that makes their Internet address available for resale by multiple “residential proxy” services, which allow customers to rent Internet addresses as a way to anonymize their web traffic or spoof their true location. As detailed in [several stories here over the past year](https://krebsonsecurity.com/tag/residential-proxy/), residential proxy services are a major source of unwanted and often malicious traffic, including account takeover activity, advertising fraud, and mass content scraping for AI projects.

“Videostrong monetized the backdoor by selling access to criminal affiliates and loading those affiliates’ malware modules onto infected devices,” the [GTIG post](https://cloud.google.com/blog/topics/threat-intelligence/shutting-the-door-on-the-xcpe-botnet) reads, noting that Google took legal action to take down the domains and servers Videostrong used to control the botnet and install additional malware. “A device manufacturer intentionally infecting their users with malware is an unacceptable breach of trust, and represents a serious risk to those users. Without users’ knowledge or consent, infected devices were offered as a distribution mechanism for a wide array of criminal actors.”

The report notes that while TV boxes made up the the majority of the botnet, *the same XCPE malware was found in other Android-based IoT products, including telehealth devices, karaoke machines, and even digital signage systems*.

Google said it requires all Android device makers to pass compatibility and security tests to ensure their products don’t harm users, but that Videostrong nevertheless found a way to load their malicious software immediately after a user boots up one of these devices for the first time (Google says it has since addressed that weakness).

The GTIG report calls out a number of residential proxy providers whose software development kits were routinely downloaded by devices infected by the XCPE botnet. Those include **AppSalt**, also known as **Honeygain**, which is owned by the Vilnius, Lithuania-based **Oxylabs**. In October 2026, Oxylabs was relaunched under a new brand called **Source**, after receiving $130 million in funding from private equity firm Warburg Pincus that [reportedly](https://app.dealroom.co/news/note/oxylabs-parent-launches-as-source-at-3-6b-valuation) valued the business at $3.6 billion. Oxylabs did not respond to a request for comment.

Another provider linked to the botnet was **NetNut**, a once sprawling residential proxy company operated by the publicly-traded Israeli company **Alarum Technologies**. In July 2026, the FBI worked with industry partners [to seize hundreds of domains associated with NetNut](https://krebsonsecurity.com/2026/06/popa-botnet-linked-to-publicly-traded-israeli-firm/), saying the company was responsible for operating a separate botnet called **Popa** that enslaved TV boxes as residential proxies. Other proxy providers named in the GTIG report include **EarnFM**, **Traffmonetizer**, **Jaguar**, **LINKFOG**, **BMW/IPWeb** and **GaGaNode**.

Google’s announcement credits a number of industry partners, including **Synthient**, a startup that tracks proxy providers. In January 2026, Synthient [published research](https://krebsonsecurity.com/2026/01/the-kimwolf-botnet-is-stalking-your-local-network/) into the rapid spread of the **Kimwolf** botnet, which at the time was hammering networks worldwide with [record-smashing DDoS attacks](https://krebsonsecurity.com/2025/10/ddos-botnet-aisuru-blankets-us-isps-in-record-ddos/). Synthient documented how Kimwolf infected millions of Android set-top boxes virtually overnight, using a widespread vulnerability in these residential proxy services to compromise other Android-based devices inside the local networks of unsuspecting TV box users.

Synthient’s research caused dozens of residential proxy providers to patch their networks, which helped to fragment the Kimwolf botnet into much smaller pieces that made its [incessant and disruptive DDoS attacks](https://krebsonsecurity.com/?s=kimwolf) far easier for network operators to manage. It also attracted the attention of the **Motion Picture Association** (MPA), a trade group representing the major Hollywood studios, which partnered with Synthient to purchase and tear apart a number of popular Android TV set-top boxes — including some that were being infected by Kimwolf and other IoT botnets.

In [a report](https://synthient.com/blog/the-internals-of-a-badbox-operation) published today, Synthient examined a popular, pre-infected TV box sold under the brand **MECOOL** by a publicly traded company in China called **Skyworth Technology**, concluding that MECOOL also bundled the malware from Videostrong Technology Co. and likewise installed AppSalt/Honeygain and other proxy components.

![](https://krebsonsecurity.com/wp-content/uploads/2026/11/mecoolboxes.png)

The MECOOL storefront and marketing. Image: Synthient.com.

Synthient founder **Ben Brundage** told KrebsOnSecurity that Videostrong’s malware also distributed software for the proxy service **Grass**. In our November 2025 story, “[Is Your Android TV Streaming Box Part of a Botnet?](http://krebsonsecurity.com/2025/11/is-your-android-tv-streaming-box-part-of-a-botnet/)” we quoted a researcher from **Censys** who found the popular **Superbox** TV streaming device bundled Grass’s residential proxy software. We also quoted the Grass founder, who denied any affiliation with the TV box maker.

That November 2025 story noted that Superbox and similar Android TV set-top boxes gain new customers primarily by engaging influencers on Tiktok and other social networks who praise the product’s ability to offer hundreds of (pirated) pay TV streaming services for a one-time fee.

Likewise, Synthient’s report observes that the MECOOL set-top boxes exploded in popularity after the product was mentioned in 2023 by the Youtube channel Linu...