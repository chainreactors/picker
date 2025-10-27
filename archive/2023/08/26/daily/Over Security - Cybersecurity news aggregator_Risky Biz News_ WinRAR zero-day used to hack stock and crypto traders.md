---
title: Risky Biz News: WinRAR zero-day used to hack stock and crypto traders
url: https://riskybiznews.substack.com/p/winrar-zero-day-hacked-crypto-trader-accounts
source: Over Security - Cybersecurity news aggregator
date: 2023-08-26
fetch_date: 2025-10-04T12:03:03.575283
---

# Risky Biz News: WinRAR zero-day used to hack stock and crypto traders

[![!!! Do not subscribe! We have moved!](https://substackcdn.com/image/fetch/$s_!dl-9!,w_80,h_80,c_fill,f_auto,q_auto:good,fl_progressive:steep,g_auto/https%3A%2F%2Fbucketeer-e05bbc84-baa3-437e-9518-adb32be77984.s3.amazonaws.com%2Fpublic%2Fimages%2F472a6618-0312-430d-8238-49e88cf01b91_1280x1280.png)](/)

# [!!! Do not subscribe! We have moved!](/)

SubscribeSign in

# Risky Biz News: WinRAR zero-day used to hack stock and crypto traders

### In other news: China's Barracuda hacking campaign still going strong; Brazilian Telegram hacker gets 20 years in prison; and ransomware gangs prefer night-time attacks.

[![Catalin Cimpanu's avatar](https://substackcdn.com/image/fetch/$s_!nOnN!,w_36,h_36,c_fill,f_auto,q_auto:good,fl_progressive:steep/https%3A%2F%2Fbucketeer-e05bbc84-baa3-437e-9518-adb32be77984.s3.amazonaws.com%2Fpublic%2Fimages%2Fe393d520-317c-4283-bbb0-64aaaa65bf19_460x460.jpeg)](https://substack.com/%40campuscodi)

[Catalin Cimpanu](https://substack.com/%40campuscodi)

Aug 25, 2023

Share

***This newsletter is brought to you by [Trail of Bits](https://www.trailofbits.com/). You can subscribe to an audio version of this newsletter as a podcast by searching for "Risky Business News" in your podcatcher or subscribing via [this RSS feed](https://risky.biz/feeds/risky-business-news/). On Apple Podcasts:***

Hackers have used a zero-day vulnerability in the WinRAR file compression utility to install malware on user devices and steal funds from stock and cryptocurrency trading accounts.

The zero-day was discovered by security researchers from *[Group-IB](https://www.group-ib.com/blog/cve-2023-38831-winrar-zero-day/),*who spotted the attacks while investigating a DarkMe malware campaign.

Researchers tracked the earliest exploits to April this year.

All the attacks appear to have been focused on the brokerage and crypto-trading communities, with booby-trapped ZIP files uploaded on eight popular forums.

The zero-day allowed threat actors to modify how files were shown inside the WinRAR window when users wanted to decompress a file. It allowed attackers to run malicious batch or CMD scripts as benign files with innocuous JPEG or PDF file extensions.

When users executed any of these files, they were infected with malware.

Group-IB says it has tracked at least 130 users who got infected this way.

In most cases, the final payload was malware such as DarkMe, GuLoader, and Remcos RAT, which allowed threat actors to connect to infected devices and then siphon money from brokerage or cryptocurrency accounts.

Researchers say they can't tell how much money has been stolen with the zero-day.

A [patch](https://www.win-rar.com/singlenewsview.html?&L=0&tx_ttnews%5Btt_news%5D=232&cHash=c5bf79590657e32554c6683296a8e8aa) for this vulnerability was released earlier this week.

The zero-day is tracked as CVE-2023-38831 and should not be confused with [CVE-2023-40477,](https://www.zerodayinitiative.com/advisories/ZDI-23-1152/) another vulnerability that was also patched this week.

[![](https://substackcdn.com/image/fetch/$s_!Js-k!,w_1456,c_limit,f_auto,q_auto:good,fl_progressive:steep/https%3A%2F%2Fsubstack-post-media.s3.amazonaws.com%2Fpublic%2Fimages%2F238a5827-6884-40c2-a892-f4268c0b2376_896x736.png)](https://substackcdn.com/image/fetch/%24s_%21Js-k%21%2Cf_auto%2Cq_auto%3Agood%2Cfl_progressive%3Asteep/https%3A//substack-post-media.s3.amazonaws.com/public/images/238a5827-6884-40c2-a892-f4268c0b2376_896x736.png)

### **Breaches, hacks, and security incidents**

**FBI's TraderTraitor cash-out warning:** The FBI has [warned](https://www.fbi.gov/news/press-releases/fbi-identifies-cryptocurrency-funds-stolen-by-dprk) that a North Korean hacking group known as TraderTraitor may attempt to launder more than $40 million worth of crypto-assets it stole in hacks earlier this year. The agency published six cryptocurrency addresses where hackers moved some of the stolen funds and asked cryptocurrency platforms not to honor any transactions. The TraderTraitor group is believed to have stolen more than $60 million worth of assets from Alphapo, $37 million from CoinsPaid, and $100 million from Atomic Wallet users.

**SIM swap incident:** Blockchain Capital co-founder Bart Stephens has lost $6.3 million worth of cryptocurrency in a SIM swap incident earlier this year. Stephens says the hackers posed as his brother to gain control over his mobile operator account, from where they transferred his number to a new device. The exec says he learned of the SIM swap when the hackers tried to withdraw money from his company, where his employees received notifications of the withdrawal attempt. [*Additional coverage in [Blockworks](https://blockworks.co/news/stephens-blockchain-capital-hack)*]

**Venus Protocol 2022 hack:** DeFi platform Venus Protocol has invalidated $63 million worth of assets from the accounts of a hacker. The funds represent 10% of the roughly $600 million that were stolen from the company's systems in [October 2022](https://www.theblock.co/post/176511/bnb-chain-executes-hard-fork-to-secure-network-after-100-million-hack). The platform also lost [another $200 million](https://quillhashteam.medium.com/200-m-venus-protocol-hack-analysis-b044af76a1ae) in May 2021. [*Additional coverage in [CryptoPotato](https://cryptopotato.com/bnb-chain-exploiter-loses-63m-on-venus-protocol-to-liquidation-amid-market-crash/)*]

**Clop's MOVEit hacks:**The number of companies who disclosed a security breach in connection to Clop's MOVEit hacks has now reached 963, according to [Resecurity](https://www.resecurity.com/blog/article/cl0p-ups-the-ante-with-massive-moveit-transfer-supply-chain-exploit).

**Fatal Model leak:** A security researcher has found a cloud database containing sensitive information from [Fatal Model](https://www.websiteplanet.com/news/fatalmodel-leak-report/), a website that claims to be the largest escort service in Brazil. Exposed data included more than 14 million records containing information about escorts, customers, and the company's backend infrastructure. The most sensitive information was ID scans and photos for 33,900 escorts who verified their identity on the site. Discovered by Jeremiah Fowler, the database has now been secured.

**CloudNordic ransomware incident:** Danish cloud hosting company CloudNordic [says](http://web.archive.org/web/20230824095447/https%3A//cloudnordic.com/) it lost all customer data in the aftermath of a ransomware attack that hit its systems last week. The company says that hackers have encrypted its backups, which prevents it from restoring customer data. CloudNordic says it does not intend to pay the hackers, meaning customers will have to rebuild infrastructure and websites from local backups or from scratch.

**DEA gets scammed:** Forbes' Thomas Brewster has a [story](https://www.forbes.com/sites/thomasbrewster/2023/08/24/dea-accidentally-sends-50000-in-drug-proceeds-to-crypto-scammer/) on how the DEA fell for a scam and sent crypto seized from a narcotics bust to a scammer.

**Tehtrans incident:** A pro-Ukraine hacktivist group named Nebula [claims](https://archive.ph/mGjmW) to have breached and destroyed the website and internal network of Russian railway company TehTrans. The hackers also claim to have stolen 3.5TB of data, which they plan to release in the coming days. The group says it conducted the attack because TehTrans transported weapons and military equipment for Russia's war effort in Ukraine. [*Additional coverage in the [Kyiv Post](https://www.kyivpost.com/post/20862)*]

[![](https://substackcdn.com/image/fetch/$s_!AEEQ!,w_1456,c_limit,f_auto,q_auto:good,fl_progressive:steep/https%3A%2F%2Fsubstack-post-media.s3.amazonaws.com%2Fpublic%2Fimages%2F81b83897-bda0-4717-a786-161fcf3157a9_1033x774.jpeg)](https://substackcdn.com/image/fetch/%24s_%21AEEQ%21%2Cf_auto%2Cq_auto%3Agood%2Cfl_progressive%3Asteep/https%3A//substack-post-media.s3.amazonaws.com/public/images/81b83897-bda0-4717-a786-161fcf3157a9_1033x774.jpeg)

...