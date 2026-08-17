---
title: Researchers Hunt Telegram Pirates with AI Tool, Flag Hundreds of Channels
url: https://torrentfreak.com/researchers-hunt-telegram-pirates-with-ai-tool-flag-hundreds-of-channels/
source: TorrentFreak
date: 2026-08-16
fetch_date: 2026-08-17T02:54:42.986430
---

# Researchers Hunt Telegram Pirates with AI Tool, Flag Hundreds of Channels

[![](https://torrentfreak.com/wp-content/themes/tf-theme-v2/build/assets/img/logo.svg)](/)

![](https://torrentfreak.com/wp-content/themes/tf-theme-v2/build/assets/img/search.svg)

* News ▼
  + [Piracy](https://torrentfreak.com/category/piracy/)
  + [Piracy Research](https://torrentfreak.com/category/research/)
  + [Law and Politics](https://torrentfreak.com/category/law-politics/)
  + [Lawsuits](https://torrentfreak.com/category/lawsuits/)
  + [Anti-Piracy](https://torrentfreak.com/category/anti-piracy/)
  + [Technology](https://torrentfreak.com/category/technology/)
* [Contact](https://torrentfreak.com/contact/)
* [Subscribe](https://torrentfreak.com/subscriptions/)

![](https://torrentfreak.com/wp-content/themes/tf-theme-v2/build/assets/img/x.svg)

# Researchers Hunt Telegram Pirates with AI Tool, Flag Hundreds of Channels

today by
[Ernesto Van der Sar](https://torrentfreak.com/author/ernesto/)

[Home](https://torrentfreak.com "Go to TorrentFreak.") > [Piracy Research](https://torrentfreak.com/category/research/ "Go to the Piracy Research category archives.") >

A new academic study offers a detailed look inside Telegram's video piracy ecosystem, spotting more than 19,000 pirated titles linked in posts that were viewed more than 4 billion times. The researchers built an AI-powered tool that can spot pirate channels and bots, which were reported to Telegram and shared with major rightsholders. The takedown effort produced results but was far from flawless.

![telegram logo](https://torrentfreak.com/images/telelogo.png)
Like many other public communication services, Telegram can be abused to facilitate illegal activities.

While much of this occurs beyond the company’s purview, pirates appear to be drawn to the platform, sharing links to pirated movies, TV-shows and other content in dedicated channels.

Despite this reputation, the platform’s piracy ecosystem has rarely been mapped in any detail. A new academic paper sets out to fill that gap, while also trying to offer a potential AI-powered solution to the problem.

Researchers from Louisiana State University and the University of Texas at Arlington examined 1,057 channels that shared roughly 209,000 posts between December 2023 and January 2026. They describe it as the first large-scale study of video piracy on the platform.

The results are detailed in the paper titled “Binge, Bot, Repeat: Unpacking the Ecosystem of Video Piracy on Telegram,” which provides some interesting new insights.

*The paper*

![bbr paper](https://torrentfreak.com/images/bbr.png)

The findings reveal that piracy is certainly not a fringe activity on Telegram. On the contrary, it is massively popular.

## 4.85 billion post views for 19,033 titles

To map the ecosystem, the researchers relied on a locally run large language model to label posts. This helped them to identify 19,033 unique pirated titles across various Telegram channels, including 14,632 movies and 4,401 TV shows produced by 3,941 companies.

As on regular pirate sites, anime is rather popular. The most pirated rightsholder is Japan’s Toei Company, home to One Piece and Dragon Ball, which accounted for 17% of the titles. As shown below, Netflix is in second place with 15%, followed by Warner Bros. at 12.4%.

*Top Rightsholders*

![top rightsholders](https://torrentfreak.com/images/toppirated1.png)

These numbers get more context when looking at the total views. According to the researchers, the ‘pirate’ posts were found on 983 channels where they amassed 4.85 billion views.

The views are not per title, as a single post can include more titles. Nonetheless, the researchers estimate a total loss of $17.49 billion, with United States content accounting for $8.17 billion and Japanese content $3.72 billion.

This is a loose estimate, assuming that 1% of the views translate into lost sales, based on the cheapest legal option available. Also, the researchers capped lost sales at a single subscription cost when multiple titles from one service were linked.

## Built to Survive Takedowns

One of the most noteworthy findings is that piracy channels use a wide variety of distribution techniques, with content scattered across interconnected channels, bots, and backup accounts.

Roughly 94% of the AI-mapped channels were connected to at least one other and many of these were unfindable using traditional searches.

“We also find that this ecosystem is deliberately engineered to be resilient against takedown efforts, frequently redirecting users through chains of intermediary channels and automated bots that collectively handle hosting, access control, monetization, and channel discovery.”

*Telegram piracy chain*

![telegram piracy](https://torrentfreak.com/images/teleexample.png)

Most pirate links pointed to external hosting platforms such as TeraBox, Terashare, and GoFile. Torrents and magnet links, meanwhile, were a rarity, and the researchers only spotted nine of these links in their research.

In addition to posting links to pirated content, some channels also shared compromised Netflix, Hulu, Disney+, and Crunchyroll logins, and VPN tutorials to help people bypass blocking measures.

## Anti-RIP: AI Powered Channel Hunting

The researchers went beyond simply mapping the ecosystem. Their findings also motivated the development of “Anti-RIP,” a real-time AI-powered tool that can detect video piracy on Telegram.

To catch channels before they grow, the researchers generated candidate Telegram handles and probed them to see which ones were linked to piracy communities. Between February 3 and April 10, 2026, the tool scanned 249,133 newly discovered channels.

*The Anti-RIP framework*

![anti-RIP](https://torrentfreak.com/images/antiripframework1.png)

From that sweep, Anti-RIP flagged 802 piracy channels with a median age of less than 5 days, along with 299 connected channels and 108 bots.

Rather than sending bare links, the team compiled the findings into evidence reports that paired each flagged channel with contextual labels describing what it was doing, from hosting and redirecting to monetizing content. These reports were sent to Telegram’s abuse department as well as 17 major U.S. rightsholders.

The research notes that 14 of the 17 US studios acknowledged the reports, and 4 explicitly stated that the contextual labels helped them assess and prioritize the notices.

“Over a 61-day period, the framework facilitated the takedown of 524 previously unknown piracy channels and 71 bots,” the paper reads. Additionally, Telegram removed many flagged posts.

## AI Tool Isn’t Flawless

Anti-RIP’s reports produced measurable results. Within two weeks, 524 of the 1,101 reported channels had become inaccessible, and Telegram removed many individual flagged posts on top of that.

The AI tool is far from perfect, and the researchers acknowledge that it produces false positives. When two coders reviewed a random sample of 1,000 posts used to validate the system, they found that the model had wrongly flagged 4 legitimate posts as piracy.

The detection model built for the live tool is reported to be 98% accurate in testing. That figure comes from a controlled test set, however, and the paper does not publish a verified error rate for the channels that were flagged during its real-world run.

The researchers have open-sourced Anti-RIP and released the dataset publicly [through GitHub](https://github.com/Scalable-Security-Research-Lab/BingeBotRepeat). This means that Telegram and rightsholders can put it to use, if they like. Similarly, pirates will likely use AI tools to evade detection, triggering an AI-driven game of cat-and-mouse.

*—*

A copy of the paper, “Binge, Bot, Repeat: Unpacking the Ecosystem of Video Piracy on Telegram,” is available [here](https://arxiv.org/abs/2605.08418). It is a preprint that hasn’t been peer-reviewed yet.

* [Previous Post![](https://torrentfreak.com/wp-content/themes/tf-theme-v2/build/assets/img/arrow-right.svg)](https://torrentfreak.com/cou...