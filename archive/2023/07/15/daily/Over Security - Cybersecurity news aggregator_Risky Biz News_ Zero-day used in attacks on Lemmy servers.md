---
title: Risky Biz News: Zero-day used in attacks on Lemmy servers
url: https://riskybiznews.substack.com/p/risky-biz-news-zero-day-used-in-attacks
source: Over Security - Cybersecurity news aggregator
date: 2023-07-15
fetch_date: 2025-10-04T11:55:07.472188
---

# Risky Biz News: Zero-day used in attacks on Lemmy servers

[![!!! Do not subscribe! We have moved!](https://substackcdn.com/image/fetch/$s_!dl-9!,w_80,h_80,c_fill,f_auto,q_auto:good,fl_progressive:steep,g_auto/https%3A%2F%2Fbucketeer-e05bbc84-baa3-437e-9518-adb32be77984.s3.amazonaws.com%2Fpublic%2Fimages%2F472a6618-0312-430d-8238-49e88cf01b91_1280x1280.png)](/)

# [!!! Do not subscribe! We have moved!](/)

SubscribeSign in

# Risky Biz News: Zero-day used in attacks on Lemmy servers

### In other news: Chinese hackers breach US government agencies; FCC cracks down on SIM swapping; ransomware on track for another record year.

[![Catalin Cimpanu's avatar](https://substackcdn.com/image/fetch/$s_!nOnN!,w_36,h_36,c_fill,f_auto,q_auto:good,fl_progressive:steep/https%3A%2F%2Fbucketeer-e05bbc84-baa3-437e-9518-adb32be77984.s3.amazonaws.com%2Fpublic%2Fimages%2Fe393d520-317c-4283-bbb0-64aaaa65bf19_460x460.jpeg)](https://substack.com/%40campuscodi)

[Catalin Cimpanu](https://substack.com/%40campuscodi)

Jul 14, 2023

Share

***This newsletter is brought to you by [Kroll](https://www.kroll.com). You can subscribe to an audio version of this newsletter as a podcast by searching for "Risky Business News" in your podcatcher or subscribing via [this RSS feed](https://risky.biz/feeds/risky-business-news/). On Spotify:***

A threat actor has used a zero-day vulnerability in the Lemmy platform to hack and deface multiple Lemmy instances over the weekend.

If the name sounds familiar, [Lemmy](https://en.wikipedia.org/wiki/Lemmy_%28software%29) is to Reddit what Mastodon is to Twitter. It is an open-source news aggregation and discussion forum modeled after the Reddit platform. Lemmy-based websites are where many Reddit communities have moved in the aftermath of the recent [Reddit API controversy](https://en.wikipedia.org/wiki/2023_Reddit_API_controversy) and site-wide protests.

On the night between Sunday to Monday, an attacker used a cross-site scripting (XSS) vulnerability to inject malicious code into the websites of some Lemmy-based communities.

The code was injected into each site's [legal pages and the main sidebar](https://lemmy.ml/post/1896249) and was designed to steal a user's authentication cookies and send it to the attackers.

Admins believe the attack was designed to target their accounts because, within minutes of their accounts being compromised, the attackers abused the authentication cookies to deface Lemmy front pages.

So far, only three websites have formally confirmed they got hacked—[Lemmy[.]world](https://lemmy.world/post/1290412), [Beehaw[.]org](https://beehaw.org/post/1039540), and [Blahaj[.]zone](https://lemmy.blahaj.zone/post/766402)—but the list might grow as admins investigate their code.

LemmyNet, the team that manages the Lemmy source code, has released a [patch](https://github.com/LemmyNet/lemmy-ui/issues/1895) in record time, with [fixes](https://github.com/LemmyNet/lemmy-ui/pull/1897) going live while the attack was still ongoing.

According to an [analysis](https://lemmy.world/post/1293336) of the zero-day, the vulnerability resided in how the Lemmy software was processing custom emojis.

The attack on Lemmy instances comes as its Fediverse brethren Mastodon also released a security patch to address a [major bug](https://github.com/mastodon/mastodon/security/advisories/GHSA-9928-3cp5-93fm) that could have allowed attackers to hijack servers just by posting a toot with a malicious multimedia file attached.

---

### **Breaches, hacks, and security incidents**

**Ventia incident:** Critical infrastructure service provider Ventia has finally contained a [cybersecurity incident](https://www.ventia.com/news-and-insights/cyberincident-3) that has impacted some of its IT services over the past weekend. The company has not shared any information about the mysterious attack.

**NRC attack:** An unidentified threat actor has targeted the online database of the Norwegian Refugee Council (NRC). The [NRC says](https://www.nrc.no/news/2023/july/cyberattack-on-norwegian-refugee-council-online-database/) it took the database offline after detecting the attack to protect the information of refugees and asylum seekers.

**Multichain cyber-heist, part 2:** An additional $103 million in crypto-assets have been moved out of the accounts of the Multichain cryptocurrency exchange. The new transfers come after an initial batch of [$126 million](https://riskybiznews.substack.com/p/risky-biz-news-126-million-go-missing) was mysteriously moved from the company's accounts over the past weekend. The company has not provided any updates after the initial transfers. Many of its users fear the company was either hacked or its staff is executing a rug pull and running away with their funds. [*Additional coverage in [Decrypt](https://decrypt.co/148133/multichain-anyswap-rug-pull-hack-103-million-chainalysis)*]

**Rodeo Finance cyber-heist:** A threat actor has stolen $1.53 million worth of crypto from the Rodeo Finance DeFi platform. The attacker used an [oracle manipulation](https://consensys.github.io/smart-contract-best-practices/attacks/oracle-manipulation/) attack. The company is [now begging](https://medium.com/%40Rodeo_Finance/rodeo-post-mortem-overview-f35635c14101) the hacker to return the funds in exchange for a "bug bounty." [*Additional coverage in [CoinTelegraph](https://cointelegraph.com/news/arbitrum-based-rodeo-finance-exploited-for-1-53m-the-second-time-in-a-week)*]

### **General tech and privacy**

**Tax data shared with Meta and Google:** An [investigation](https://www.warren.senate.gov/oversight/reports/in-new-report-senators-warren-wyden-lawmakers-reveal-massive-likely-illegal-breach-of-taxpayer-privacy-by-tax-prep-companies-with-meta_call-for-agencies-to-investigate-prosecute) by seven US Senators has found that tax preparation and filing services TaxAct, H&R Block, and TaxSlayer have shared the personal data of taxpayers with Google and Meta. The three services used Google Analytics and Meta Pixel to track taxpayers on their sites, inadvertently sharing sensitive information with the two Silicon Valley companies. The senator group, which also includes the Chair of the Senate Finance Committee, Richard Blumenthal, says this behavior violates taxpayer privacy laws.

**Privacy Sandbox requires consent:**French privacy watchdog CNIL has [ruled](https://www.cnil.fr/fr/privacy-sandbox-sur-google-chrome-quelles-consequences-pour-les-utilisateurs) that Google's new Privacy Sandbox tracking technology also requires user consent before tracking users, even if Google says the data it collects on users is far smaller and anonymized.

**VanMoof going under:** Electric bike maker VanMoof has [told customers](https://old.reddit.com/r/vanmoofbicycle/comments/14xj66k/get_your_encryption_keys_now/) to make copies of their Bluetooth encryption keys as this is the only way customers can connect to their bikes. The company has already shut down some online services as it deals with an [impending total shutdown](https://www.theverge.com/2023/7/12/23792143/vanmoof-e-bike-payment-suspension-bankruptcy-sale) and possible bankruptcy.

**Windows 11:** More Rust code has [made it](https://blogs.windows.com/windows-insider/2023/07/12/announcing-windows-11-insider-preview-build-25905/) into the Windows kernel.

**Passkeys on GitHub:** GitHub now [supports](https://github.blog/2023-07-12-introducing-passwordless-authentication-on-github-com/) passkeys.

> "To use passkeys with your GitHub account, navigate to your 'Settings' sidebar, locate the 'Feature Preview' tab, and click 'enable passkeys'. Once you've enabled passkeys, you'll be able to upgrade eligible security keys to passkeys and register new passkeys."

### **Government, politics, and policy**

**FCC cyber-funds for schools:** The FCC plans to allow K-12 schools and libraries to use funds from the E-Rate program to purchase cybersecurity products. E-Rate funding could previously only be used to purchase internet subscriptions and networking devices. The [FCC plans](ht...