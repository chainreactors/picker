---
title: Inside the Massive Crime Industry That’s Hacking Billion-Dollar Companies
url: https://www.wired.com/story/inside-the-massive-crime-industry-thats-hacking-billion-dollar-companies/
source: Instapaper: Unread
date: 2024-11-06
fetch_date: 2025-10-06T19:23:31.298330
---

# Inside the Massive Crime Industry That’s Hacking Billion-Dollar Companies

[Skip to main content](#main-content)

Menu

[![Wired](/verso/static/wired-us/assets/logo.svg)](/)

[SECURITY](/category/security/)

[POLITICS](/category/politics/)

[THE BIG STORY](/category/big-story/)

[BUSINESS](/category/business/)

[SCIENCE](/category/science/)

[CULTURE](/category/culture/)

[REVIEWS](/category/gear/)

Menu

[![Wired](/verso/static/wired-us/assets/logo.svg)](/)

Account

Account

[Newsletters](/newsletter?sourceCode=navbar)

[Security](/category/security/)

[Politics](/category/politics/)

[The Big Story](/category/big-story/)

[Business](/category/business/)

[Science](/category/science/)

[Culture](/category/culture/)

[ReviewsChevron](/category/gear/)

MoreExpand

[The Big Interview](/the-big-interview/)[Magazine](/magazine/)[Events](/tag/wired-events/)[WIRED Insider](/collection/wiredinsider/)[WIRED Consulting](/tag/wired-consulting/)

[Newsletters](/newsletter?sourceCode=navbar)

[Podcasts](/podcasts/)

[Video](/video/)

[Merch](https://shop.wired.com/)

[SearchSearch](/search/)

[Sign In](/auth/initiate?redirectURL=%2Fstory%2Finside-the-massive-crime-industry-thats-hacking-billion-dollar-companies%2F&source=VERSO_NAVIGATION)

[Sign In](/auth/initiate?redirectURL=%2Fstory%2Finside-the-massive-crime-industry-thats-hacking-billion-dollar-companies%2F&source=VERSO_NAVIGATION)

[Joseph Cox](/author/joseph-cox/)

[Security](/category/security)

Nov 4, 2024 6:00 AM

# Inside the Massive Crime Industry That’s Hacking Billion-Dollar Companies

When you download a piece of pirated software, you might also be getting a piece of infostealer malware, and entering a highly complex hacking ecosystem that’s fueling some of the biggest breaches on the planet.

![Adult Person Collage Accessories Bag Handbag Clothing Finger Print Dollar Bill Map and Code](https://media.wired.com/photos/6723b2ccb2d0f9dc9309d32b/3:2/w_2560%2Cc_limit/Security_404_Getty-Images.jpg)

Photo Illustration: Skye Battles; Getty Images

Save StorySave this story

Save StorySave this story

On October 20, a hacker who calls themselves Dark X said they logged in to a server and stole the personal data of 350 million Hot Topic customers. The following day, Dark X listed the data, including alleged emails, addresses, phone numbers, and partial credit card numbers, for sale on an underground forum. The day after that, Dark X said Hot Topic kicked them out.

*This article is copublished in partnership with [404 Media](https://www.404media.co/).*

Dark X told me that the apparent breach, which is possibly the largest hack of a consumer retailer ever, was partly due to luck. They just happened to get login credentials from a developer who had access to Hot Topic’s crown jewels. To prove it, Dark X sent me the developer’s login credentials for Snowflake, a data warehousing tool that hackers have repeatedly targeted recently. Alon Gal from cybersecurity firm Hudson Rock, [which first found the link](https://www.infostealers.com/article/largest-retail-breach-in-history-350-million-hot-topic-customers-personal-and-payment-data-exposed-as-a-result-of-infostealer-infection/) between infostealers and the Hot Topic breach, said he was sent the same set of credentials by the hacker.

The luck part is true. But the claimed Hot Topic hack is also the latest breach directly connected to a sprawling underground industry that has made hacking some of the most important companies in the world child’s play.

[AT&T](https://www.404media.co/hackers-steal-text-and-call-records-of-nearly-all-at-t-customers/). [Ticketmaster](https://www.404media.co/the-ticketmaster-hack-is-becoming-a-logistical-nightmare-for-fans-and-brokers/). [Santander Bank](https://www.404media.co/the-walls-are-closing-in-on-the-snowflake-hacker/). [Neiman Marcus](https://www.bleepingcomputer.com/news/security/neiman-marcus-confirms-data-breach-after-snowflake-account-hack/). [Electronic Arts](https://www.vice.com/en/article/hackers-steal-data-electronic-arts-ea-fifa-source-code/). These were not entirely isolated incidents. Instead, they were all hacked thanks to “infostealers,” a type of malware that is designed to pillage passwords and cookies stored in the victim’s browser. In turn, infostealers have given birth to a complex ecosystem that has been allowed to grow in the shadows and where criminals fulfill different roles. There are Russian malware coders continually updating their code; teams of professionals who use glitzy advertising to hire contractors to spread the malware across YouTube, TikTok, or GitHub; and English-speaking teenagers on the other side of the world who then use the harvested credentials to break into corporations. At the end of October, a collaboration of law enforcement agencies [announced an operation](https://www.operation-magnus.com/) against two of the world’s most prevalent stealers. But the market has been able to grow and mature so much that now law enforcement action against even one part of it is unlikely to make any lasting dent in the spread of infostealers.

Based on interviews with malware developers, hackers who use the stolen credentials, and a review of manuals that tell new recruits how to spread the malware, 404 Media has mapped out this industry. Its end result is that a download of an innocent-looking piece of software by a single person can lead to a data breach at a multibillion-dollar company, putting Google and other tech giants in an ever-escalating cat-and-mouse game with the malware developers to keep people and companies safe.

“We are professionals in our field and will continue to work on bypassing future Google updates,” an administrator for LummaC2, one of the most popular pieces of infostealer malware, told me in an online chat. “It takes some time, but we have all the resources and knowledge to continue the fight against Chrome.”

## The Stealers

The infostealer ecosystem starts with the malware itself. Dozens of these exist, with names like Nexus, Aurora, META, and Raccoon. The most widespread infostealer at the moment is one called RedLine, according to cybersecurity firm Recorded Future. Having a prepackaged piece of malware also dramatically lowers the barrier to entry for a budding new hacker. The administrator of LummaC2, which Recorded Future says is in the top 10 of infostealers, said it welcomes both beginner and experienced hackers.

Initially, many of these developers were interested in stealing credentials or keys related to cryptocurrency wallets. Armed with those, hackers could empty a victim’s digital wallets and make a quick buck. Many today still market their tools as being able to steal bitcoin and have [even introduced OCR](https://x.com/RecordedFuture/status/1839310003431448946) to detect seed phrases in images. But recently those same developers and their associates figured out that all of the other stuff stored in a browser—passwords to the victim’s place of work, for example—could generate a secondary stream of revenue.

“Malware developers and their clients have realized that personal and corporate credentials, such as login details for online accounts, financial data, and other sensitive information, hold substantial value on the black market,” RussianPanda, an independent security researcher who follows infostealers closely, told 404 Media. Infostealer creators pivoted to capture this information too, she said. In essence, the exhaust from cryptocurrency-focused heists has created an entire new industry in its own right that is causing even more destruction across healthcare, tech, and other industries.

Some stealers then sell these collected credentials and cookies, or logs, themselves via bots on Telegram. Telegram, rather than acting as simply a messaging app, provides critical infrastructure for these teams. The entire process from buying to selling stolen logs is automated through Telegram bots. Telegram did not respond to a request for comment.

Infostealers are not especially hard to write, but the malware developers constant...