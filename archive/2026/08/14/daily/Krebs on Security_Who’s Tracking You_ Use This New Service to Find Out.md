---
title: Who’s Tracking You? Use This New Service to Find Out
url: https://krebsonsecurity.com/2026/08/whos-tracking-you-use-this-new-service-to-find-out/
source: Krebs on Security
date: 2026-08-14
fetch_date: 2026-08-15T02:50:02.923973
---

# Who’s Tracking You? Use This New Service to Find Out

Advertisement

[![](/b-doppel/17.png)](https://www.doppel.com/?utm_source=krebsonsecurity&utm_medium=display&utm_campaign=fy27brandcampaign&utm_content=detectdisrupt)

Advertisement

[![](/b-gartner/16.png)](https://www.gartner.com/en/conferences/na/symposium-us/conference-resources/security?utm_medium=display&utm_campaign=EVT_NA_2026_SYM36_PD_BN1_CYBERINSIGHTS&utm_term=krebs)

[![Krebs on Security](https://krebsonsecurity.com/wp-content/uploads/2021/03/kos-27-03-2021.jpg)](https://krebsonsecurity.com/ "Krebs on Security")

[Skip to content](#content "Skip to content")

* [Home](https://krebsonsecurity.com/)
* [About the Author](https://krebsonsecurity.com/about/)
* [Advertising/Speaking](https://krebsonsecurity.com/cpm/)

# Who’s Tracking You? Use This New Service to Find Out

August 14, 2026

[14 Comments](https://krebsonsecurity.com/2026/08/whos-tracking-you-use-this-new-service-to-find-out/#comments)

It can be daunting to determine who’s responsible for showing ads on the websites we visit, or who’s harvesting data from the mobile apps we use every day. That information is already semi-public, but it is not easily parsed and traditionally much of it has remained walled away in the hands of large advertising platforms. Not anymore: A powerful and free new service called **DecryptAds** scrapes and correlates this adtech data and makes it simple to quickly learn a great deal about the entities that are tracking you.

[![](https://krebsonsecurity.com/wp-content/uploads/2026/08/decryptads-ESPN.png)](https://krebsonsecurity.com/wp-content/uploads/2026/08/decryptads-ESPN.png)

A Decryptads summary of the advertising partnerships declared by espn.com.

The [newly launched](https://decryptads.com/blog/posts/ad-tech-transparency-launch.html) **decryptads.com** says it is constantly scraping the files that websites and apps make publicly available to disclose the companies that are permitted to run ads or collect user data. These files include:

–**ads.txt**: all of the adtech companies and data brokers that may run ads or harvest data from the site;
–**app-ads.txt**: entities that can harvest data from or display ads on mobile and smart TV apps;
–**buyers.json/sellers.json**: the entities buying, selling or reselling ad inventory for a given site or app.

**Zach Edwards** is chief research officer for DecryptAds and a threat researcher at the security company **Infoblox**. Edwards said he and two other founders decided the service was needed because the adtech data in these files is generally only useful when it can be cross-referenced to build a more complete picture of the advertising ecosystem for each website or app.

“It’s an adtech tool but we’re trying to approach adtech from a security perspective,” Edwards said. “It’s really built for a lot of privacy and security use cases that have been dramatically underserved.”

Those use cases, he said, include tracking down the source of malicious ads that try to foist malware on targeted users, identifying ad networks located in adversarial nations, and detecting the fast growing swarms of AI-generated slop websites and apps. And as decryptads.com demonstrates, these potential security and privacy threats are near impossible to detect just by viewing a single apps.txt or app-ads.txt file.

“Supply-chain integrity issues rarely live in a single file,” the site [explains](https://decryptads.com/blog/posts/analytical-features.html). “They show up as broken cross-references between ads.txt, app-ads.txt, and sellers.json files; as cloned declaration sets across unrelated domains; as seller removals that only make sense when viewed across exchanges; and even as supply paths in bid logs that never actually appear in any given publisher’s authorized-seller list.”

A search in DecryptAds for the hugely popular sports network **espn.com** reveals 143 ad partners and 19 registered data broker domains are listed within its [ads.txt](https://www.espn.com/ads.txt) and [app-ads.txt](https://www.espn.com/app-ads.txt) files. That data broker information is gradually becoming available because four states — California, Oregon, Texas and Vermont — have recently passed laws requiring data brokers to register if they buy or sell data on consumers from those states. DecryptAds reports that almost half of those data brokers are collecting geolocation data from espn.com visitors who aren’t blocking ads, while another three disclose that they collect device fingerprints and sensitive personal information.

[![](https://krebsonsecurity.com/wp-content/uploads/2026/08/espn-supplychain.png)](https://krebsonsecurity.com/wp-content/uploads/2026/08/espn-supplychain.png)

A visual representation of the complex ad supply chain declared by espn.com. Image: decryptads.com.

## HIGH-RISK AD PARTNERS

DecryptAds also makes it easy to learn the beneficiaries and national origins of the advertising firms lurking in apps and websites, displaying a conspicuous warning when adtech partners of an app or website are based in [“geo-risk”](https://decryptads.com/geo_risk) areas like China and Russia, or in countries with strong financial and political ties to both — such as Cyprus and the United Arab Emirates (UAE).

According to DecryptAds, espn.com works with four different advertising entities that are based in either Russia, China or the UAE, including the adtech firm **Between Digital**, which lists a New York address. However, the [dossier on Between Digital](https://decryptads.com/ad_system/betweendigital.com) flags them as a Russian firm, showing that [their publisher offers](https://cp.betweendigital.com/files/PublisherOffer.pdf) (PDF) are processed through **Alfa Bank**, Russia’s largest private commercial bank and one of several financial institutions placed under U.S. sanctions in 2022 after Russia invaded Ukraine. KrebsOnSecurity sought comment from both Between Digital and the company’s founder, and will update this story in the event that either replies.

A search for several top U.S. military news websites — including [armytimes.com](https://decryptads.com/search/publisher/armytimes.com), [airforcetimes.com](https://decryptads.com/publisher/airforcetimes.com), [defensenews.com](https://decryptads.com/publisher/defensenews.com), [navytimes.com](https://decryptads.com/publisher/navytimes.com), [marinecorpstimes.com](https://decryptads.com/publisher/marinecorpstimes.com) and [federaltimes.com](https://decryptads.com/publisher/federaltimes.com) — shows they all allow Between Digital to serve ads and track users, as well as two entities in the UAE and another in the ownership secrecy haven of Panama. DecryptAds reports that Between Digital is collecting ad data on approximately 55,000 partner websites.

[![](https://krebsonsecurity.com/wp-content/uploads/2026/08/decryptads-georisk.png)](https://krebsonsecurity.com/?attachment_id=74140)

The “Geo Risk” section of decryptads.com.

Pivoting on Between Digital’s [app-ads.txt file](https://decryptads.com/ad_system_sites/betweendigital.com/app_ads_txt/all) reveals hundreds of domains featuring simple web-based games that are frequently interrupted by ads. Edwards said Between Digital’s own declarations show the company is listed as both a publisher and a reseller on approximately two-thirds of their portfolio.

“It means they are basically playing both sides of the bidding equation, which creates opportunities to direct client spend at your owned and operated properties or client infrastructure, essentially creating opportunities for conflicts of interest,” Edwards told KrebsOnSecurity. “The problem we have right now is that for years we’ve had almost no one policing these ads.txt and app-ads.txt files.”

The **Opera** Web browser remains quite popular, and probably many users are unaware that since 2016 it has been majority owned and controlled by the Chinese company Kunlun Tech (the operational headquarters of Opera remain in Oslo, Norway).

Opera.com’s [profile at DecryptAds](https://decrypta...