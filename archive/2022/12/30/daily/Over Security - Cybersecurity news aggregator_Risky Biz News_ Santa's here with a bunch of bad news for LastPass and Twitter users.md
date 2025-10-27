---
title: Risky Biz News: Santa's here with a bunch of bad news for LastPass and Twitter users
url: https://riskybiznews.substack.com/p/risky-biz-news-santas-here-with-a
source: Over Security - Cybersecurity news aggregator
date: 2022-12-30
fetch_date: 2025-10-04T02:46:19.102601
---

# Risky Biz News: Santa's here with a bunch of bad news for LastPass and Twitter users

[![!!! Do not subscribe! We have moved!](https://substackcdn.com/image/fetch/$s_!dl-9!,w_80,h_80,c_fill,f_auto,q_auto:good,fl_progressive:steep,g_auto/https%3A%2F%2Fbucketeer-e05bbc84-baa3-437e-9518-adb32be77984.s3.amazonaws.com%2Fpublic%2Fimages%2F472a6618-0312-430d-8238-49e88cf01b91_1280x1280.png)](/)

# [!!! Do not subscribe! We have moved!](/)

SubscribeSign in

# Risky Biz News: Santa's here with a bunch of bad news for LastPass and Twitter users

### In other news: AT&T exonerates itself from any responsibility in SIM-swapping attacks; BitKeep wallets drained in supply chain attack; TikTok banned on federal networks and lawmakers' devices.

[![Catalin Cimpanu's avatar](https://substackcdn.com/image/fetch/$s_!nOnN!,w_36,h_36,c_fill,f_auto,q_auto:good,fl_progressive:steep/https%3A%2F%2Fbucketeer-e05bbc84-baa3-437e-9518-adb32be77984.s3.amazonaws.com%2Fpublic%2Fimages%2Fe393d520-317c-4283-bbb0-64aaaa65bf19_460x460.jpeg)](https://substack.com/%40campuscodi)

[Catalin Cimpanu](https://substack.com/%40campuscodi)

Dec 29, 2022

Share

***This newsletter is brought to you by [Airlock Digital](https://www.airlockdigital.com/), [Proofpoint](https://www.proofpoint.com/), [runZero](https://www.runzero.com/), and [Thinkst Canary](https://canary.tools/). You can subscribe to an audio version of this newsletter as a podcast by searching for "Risky Business News" in your podcatcher or subscribing via [this RSS feed](https://risky.biz/feeds/risky-business-news/).***

The Risky Business team is still on its holiday break, but we thought to put out this weekly edition with some of the past week's biggest infosec stories.

Happy holidays!

### Breaches and hacks

**LastPass breach:** The day after our last newsletter and just ahead of the Christmas holiday, LastPass updated the [blog post](https://blog.lastpass.com/2022/12/notice-of-recent-security-incident/) about its August security breach to add a bunch of bad news. The new text is [full of PR misdirections](https://palant.info/2022/12/26/whats-in-a-pr-statement-lastpass-breach-explained/), but translated, the company effectively admits it didn't contain the August intrusion, and since then, the threat actor moved laterally across its network and managed to gain access to a cloud server where the company was storing its users' encrypted password vaults. Yes, your LastPass password vaults are gone, and it's apparently pretty easy to brute-force them if your master password is weak. Sigh! Lots of this is [LastPass'](https://mastodon.social/%40WPalant%40infosec.exchange/109590750726241142) [fault](https://mastodon.social/%40sawaba%40infosec.exchange/109564824303979172), btw.

**Twitter breach:** But that wasn't all of it. On Christmas day, news emerged that a threat actor was selling the personal details of [more than 400 million Twitter users](https://www.linkedin.com/posts/alon-gal-utb_data-gdpr-database-activity-7012389466937913344-zpMO/). The threat actor said the data was compiled earlier this year [by scraping the Twitter API](https://mastodon.social/%40briankrebs%40infosec.exchange/109569534086173092) for private account information, such as account stats and phone numbers. Twitter has [refused](https://twitter.com/briankrebs/status/1607848771777630209) to acknowledge the incident, and the company has applied "context notes" on some of the more popular tweets sharing the bad news, claiming the data comes from [an incident it confirmed last month](https://www.bleepingcomputer.com/news/security/54-million-twitter-users-stolen-data-leaked-online-more-shared-privately/) and which only affected 5.4 million users. In the meantime, several people have come out to say that the data sold on Breached is legitimate and that big. A friendly piece of advice is to either change your Twitter-associated phone number or disable SMS-based 2FA and use an authenticator app only for logging into Twitter (if you still use that ring-wing, QAnon, and Kremlin propaganda cesspool).

[![](https://substackcdn.com/image/fetch/$s_!JmZN!,w_1456,c_limit,f_auto,q_auto:good,fl_progressive:steep/https%3A%2F%2Fbucketeer-e05bbc84-baa3-437e-9518-adb32be77984.s3.amazonaws.com%2Fpublic%2Fimages%2F96f8750b-ec7d-4a59-913f-6ebb5be0f47d_1125x596.png)](https://substackcdn.com/image/fetch/%24s_%21JmZN%21%2Cf_auto%2Cq_auto%3Agood%2Cfl_progressive%3Asteep/https%3A//bucketeer-e05bbc84-baa3-437e-9518-adb32be77984.s3.amazonaws.com/public/images/96f8750b-ec7d-4a59-913f-6ebb5be0f47d_1125x596.png)

**BitKeep wallet crypto-heists:** Cryptocurrency wallet app [BitKeep confirmed](https://t.me/bitkeep/780791) that hackers modified some of its Android APK files and deployed malicious code on the devices of some of its customers. Losses from this incident are [estimated](https://archive.ph/hxc8V) at around $8 million worth of crypto assets.

**BTC.com crypto-heist:** Cryptocurrency mining pool [BTC.com said](https://btcm.group/news-detail?id=52667) it was the victim of a cyber-attack that took place at the start of the month.

> "In the cyberattack, certain digital assets were stolen, including approximately US$700,000 in asset value owned by BTC.com's clients, and approximately US$2.3 million in asset value owned by the Company."

**Defrost Finance crypto-heist:** DeFi platform Defrost Finance was the victim of a flash-loan attack. Losses are estimated at $12 million, but the hacker [returned the funds](https://medium.com/%40Defrost_Finance/details-concerning-the-refunding-process-78d48e18031b) after three days.

**Rubic crypto-heist:** Cross-chain cryptocurrency platform Rubic was also hacked and [lost $1.41 million](https://archive.ph/0Xdhe) worth of crypto assets. The company [confirmed](https://archive.ph/2zGYF) the incident and promised to refund affected users.

**Comcast Xfinity account hacks:** Several Comcast Xfinity customers said they had their accounts hacked. The accounts were then used to reset passwords and bypass 2FA accounts on cryptocurrency portals like Gemini and Coinbase. [*Coverage in [BleepingComputer](https://www.bleepingcomputer.com/news/security/comcast-xfinity-accounts-hacked-in-widespread-2fa-bypass-attacks/)*]

**RansomHouse claims Vanuatu:** The RansomHouse ransomware cartel has [claimed](https://www.databreaches.net/vanuatu-ransomware-attack-claimed-by-ransomhouse/) the ransomware attack that crippled the network of the Vanuatu government for the past few weeks.

**49ers CLA:** The San Francisco 49ers NFL team has been [sued](https://www.courtlistener.com/docket/66678990/sampson-v-49ers-enterprises-llc/) in a class-action lawsuit for not properly disclosing in a breach notification that they suffered a [ransomware attack](https://therecord.media/san-francisco-49ers-confirm-ransomware-attack/) and that some of their employee and customer PII data might have been exposed and leaked online on the dark web.

### General tech and privacy

**AWS S3 new defaults:**After a quatrabazillion incidents where customers accidentally left S3 buckets exposed on the internet and leaked their companies' sensitive data online, the super-geniuses at AWS have finally decided to [change the S3 defaults](https://aws.amazon.com/about-aws/whats-new/2022/12/amazon-s3-automatically-enable-block-public-access-disable-access-control-lists-buckets-april-2023/) from open to "block public access." This will become the default policy for all new S3 buckets in April 2023, meaning that if you want the content of your S3 bucket to be publicly accessible, you will have to deploy an ACL rule to make it so.

**TikTok spied on journalists:** Chinese social media giant TikTok has [confirmed](https://www.forbes.com/sites/emilybaker-white/2022/12/22/tiktok-tracks-forbes-journalists-bytedance/) that it spied on the real-time location of Forbes journalists who reported on the company in the hopes of identifying some of their sources. [*Non-paywall version [here](https://archive.ph/WTupJ)*]

**AT&T legal shenanigans:** AT&T has [updated](https://mastodon.social/%40briankrebs%40...