---
title: Risky Biz News: Zero-day alert for GoAnywhere file transfer servers
url: https://riskybiznews.substack.com/p/risky-biz-news-zero-day-alert-for
source: Over Security - Cybersecurity news aggregator
date: 2023-02-04
fetch_date: 2025-10-04T05:42:26.067765
---

# Risky Biz News: Zero-day alert for GoAnywhere file transfer servers

[![!!! Do not subscribe! We have moved!](https://substackcdn.com/image/fetch/$s_!dl-9!,w_80,h_80,c_fill,f_auto,q_auto:good,fl_progressive:steep,g_auto/https%3A%2F%2Fbucketeer-e05bbc84-baa3-437e-9518-adb32be77984.s3.amazonaws.com%2Fpublic%2Fimages%2F472a6618-0312-430d-8238-49e88cf01b91_1280x1280.png)](/)

# [!!! Do not subscribe! We have moved!](/)

SubscribeSign in

# Risky Biz News: Zero-day alert for GoAnywhere file transfer servers

### In other news: BonqDAO hacked for $120 million; new Nevada RaaS; HeadCrab infects 1,200 Redis servers.

[![Catalin Cimpanu's avatar](https://substackcdn.com/image/fetch/$s_!nOnN!,w_36,h_36,c_fill,f_auto,q_auto:good,fl_progressive:steep/https%3A%2F%2Fbucketeer-e05bbc84-baa3-437e-9518-adb32be77984.s3.amazonaws.com%2Fpublic%2Fimages%2Fe393d520-317c-4283-bbb0-64aaaa65bf19_460x460.jpeg)](https://substack.com/%40campuscodi)

[Catalin Cimpanu](https://substack.com/%40campuscodi)

Feb 03, 2023

Share

***This newsletter is brought to you by [Airlock Digital](https://www.airlockdigital.com/), [Proofpoint](https://www.proofpoint.com/), [runZero](https://www.runzero.com/), and [Thinkst Canary](https://canary.tools/). You can subscribe to an audio version of this newsletter as a podcast by searching for "Risky Business News" in your podcatcher or subscribing via [this RSS feed](https://risky.biz/feeds/risky-business-news/).***

Hackers are exploiting a zero-day vulnerability in [GoAnywhere MFT](https://www.goanywhere.com/), a web-based file transfer application typically used in corporate environments.

Fortra, the company behind GoAnywhere MFT, says that only the app's administrative panel is exploitable and not the public web client typically used by a company's normal users.

The company is warning customers to secure their admin panels from unauthorized access, such as taking panels off the public internet and restricting them to intranets or behind firewall IP allowlists.

No patch is currently available. Some mitigations exist, and they are available in a copy of Fortra's security alert [shared](https://mastodon.social/%40briankrebs%40infosec.exchange/109795711331882434) by infosec reporter Brian Krebs on Mastodon on Thursday.

According to security researcher [Kevin Beaumont](https://mastodon.social/%40GossiTheDog%40cyberplace.social/109795921470330685), there are currently [roughly 1,000](https://www.shodan.io/search?query=http.favicon.hash%3A1484947000) internet-accessible GoAnywhere MFT servers listed on Shodan, although most of these appear to expose their web client. Unclear how many have admin panels exposed as well.

Enterprise-ready file transfer solutions like GoAnywhere are often in the crosshair of both cybercrime and APT groups alike. In the past, [Accelion's FTA](https://www.zdnet.com/article/accellion-to-retire-product-at-the-heart-of-recent-hacks/) and [Soliton's FileZen](https://therecord.media/hacking-campaign-targets-filezen-file-sharing-network-appliances/) file-sharing and file-transfer products have been targeted in attacks.

### **Breaches and hacks**

**BonqDAO crypto-heist:** The BonqDAO cryptocurrency lending platform has [confirmed](http://web.archive.org/web/20230202184319/https%3A//twitter.com/BonqDAO/status/1620908233761378304) that a threat actor used an Oracle attack to exploit a vulnerability in its Bonq protocol and manipulate the price of AllianceBlock (ALBT) tokens. The company is still investigating the impact of the hack, but blockchain security firm PeckShield has [estimated](http://web.archive.org/web/20230202184322/https%3A//twitter.com/peckshield/status/1620926816868499458) the losses from the attack to be a whopping $120 million worth of funds. The attacker is currently trying to launder the stolen funds into more stable/mainstream coins. The incident is this year's largest cryptocurrency heist so far. [*Media coverage in the [CoinTelegraph](https://cointelegraph.com/news/bonqdao-protocol-suffers-120m-loss-after-oracle-hack), technical analysis via [Numen Cyber Labs](https://mp.weixin.qq.com/s/uhxAbHt7HAPcDbBkZeynsw) and [SlowMist](https://mp.weixin.qq.com/s/RG8daNwU_d9QUSmiTwtroA)*]

**Ransomware impacts the stock market:** A ransomware attack on ION Trading, a UK-based company that makes trading software, is impacting the activity of several major European and US banks. The company's software is used to process derivatives trades across stock, bond, and commodities markets. *[Bloomberg News](https://www.bloomberg.com/news/articles/2023-02-01/cyberattack-hits-derivatives-unit-of-trading-software-firm-ion)* says the outage has impacted at least 42 customers, some of which are having problems with regulatory reporting and are processing trades manually. In a [statement](https://iongroup.com/press-release/markets/cleared-derivatives-cyber-event/) on its website, ION Trading confirmed the incident but said the attack only hit one of its software environments and that all affected servers have now been disconnected. Most of the issues have been reported across Europe. Bloomberg has identified the ransomware gang behind the attack as LockBit.

**Vice Media breach:** US news agency Vice Media says a hacker gained access to an internal email account and has stolen information on 1,724 of the company's employees. Vice Media, whose news outlets have criticized companies for being slow in disclosing data breaches, took ten months to [disclose the incident](https://apps.web.maine.gov/online/aeviewer/ME/40/74ca2ed9-e08b-43be-a6a9-34bd892a9c72.shtml), which took place in March last year and was discovered a week later in early April.

**Electrify America boo-boo:** Apparently, you can use TeamViewer to take over the DC fast-charging stations of Electrify America and access their backend, which looks to be some sort of old Windows 10 install still running Internet Explorer. Several instances of abuse have been reported already. [*More in [InsideEVs](https://insideevs.com/news/642914/electrify-america-charging-station-bugs-easy-hacking/)*]

**Mastodon DDoS attacks:** Several Mastodon instances have been the targets of DDoS attacks lately, including [Mastodon.social](https://mastodon.social/%40feditips%40mstdn.social/109781538119002791), the largest Mastodon instance, and [JoinMastodon.org](https://mastodon.social/%40feditips%40mstdn.social/109788799622782423), the service's official website. No major downtime was recorded, though.

**Best2Pay leak:** Hackers have leaked the data of more than 1 million customers of Russian online payment service Best2Pay.net. The leaked data contains customer names, mobile phone numbers, payment details, and people's last four card digits. The company has not confirmed the leak, but the Telegram channel where the data was leaked has a very long history of sharing authentic leaks from Russian companies.

[![](https://substackcdn.com/image/fetch/$s_!EMjW!,w_1456,c_limit,f_auto,q_auto:good,fl_progressive:steep/https%3A%2F%2Fsubstack-post-media.s3.amazonaws.com%2Fpublic%2Fimages%2Fce8a1e48-8b7b-4a16-927f-5da59eb80a52_651x793.png)](https://substackcdn.com/image/fetch/%24s_%21EMjW%21%2Cf_auto%2Cq_auto%3Agood%2Cfl_progressive%3Asteep/https%3A//substack-post-media.s3.amazonaws.com/public/images/ce8a1e48-8b7b-4a16-927f-5da59eb80a52_651x793.png)

### **General tech and privacy**

**GoodRx fine:** The US Federal Trade Commission has [fined GoodRx](https://www.ftc.gov/news-events/news/press-releases/2023/02/ftc-enforcement-action-bar-goodrx-sharing-consumers-sensitive-health-info-advertising), a telehealth and prescription drug discount provider, $1.5 million for sharing the personal and health information of its customers with online advertisers. The FTC says that in 2019, GoodRx compiled lists of its users who used their apps or visited their site to purchase particular medications, such as those used to treat heart disease and blood pressure. These lists included a buyer's email address, phone number, and mobile advertising ID. The FTC says GoodRx uploaded these lists...