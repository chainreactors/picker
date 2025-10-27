---
title: Risky Biz News: New Scattered Spider group targets telcos for SIM swapping attacks
url: https://riskybiznews.substack.com/p/risky-biz-news-new-scattered-spider
source: Over Security - Cybersecurity news aggregator
date: 2022-12-08
fetch_date: 2025-10-04T00:55:25.316831
---

# Risky Biz News: New Scattered Spider group targets telcos for SIM swapping attacks

[![!!! Do not subscribe! We have moved!](https://substackcdn.com/image/fetch/$s_!dl-9!,w_80,h_80,c_fill,f_auto,q_auto:good,fl_progressive:steep,g_auto/https%3A%2F%2Fbucketeer-e05bbc84-baa3-437e-9518-adb32be77984.s3.amazonaws.com%2Fpublic%2Fimages%2F472a6618-0312-430d-8238-49e88cf01b91_1280x1280.png)](/)

# [!!! Do not subscribe! We have moved!](/)

SubscribeSign in

# Risky Biz News: New Scattered Spider group targets telcos for SIM swapping attacks

### In other news: Amnesty International says it was hacked by China; EU funds Cyber Lab in Ukraine; Callisto APT so hot right now!

[![Catalin Cimpanu's avatar](https://substackcdn.com/image/fetch/$s_!nOnN!,w_36,h_36,c_fill,f_auto,q_auto:good,fl_progressive:steep/https%3A%2F%2Fbucketeer-e05bbc84-baa3-437e-9518-adb32be77984.s3.amazonaws.com%2Fpublic%2Fimages%2Fe393d520-317c-4283-bbb0-64aaaa65bf19_460x460.jpeg)](https://substack.com/%40campuscodi)

[Catalin Cimpanu](https://substack.com/%40campuscodi)

Dec 07, 2022

Share

***This newsletter is brought to you by [Airlock Digital](https://www.airlockdigital.com/), [Proofpoint](https://www.proofpoint.com/), [runZero](https://www.runzero.com/), and [Thinkst Canary](https://canary.tools/). You can subscribe to an audio version of this newsletter as a podcast by searching for "Risky Business News" in your podcatcher or subscribing via [this RSS feed](https://risky.biz/feeds/risky-business-news/).***

> *Please be aware that due to a certificate rotation on our main website and audio distribution server, our podcast’s Spotify feed is currently down and won’t show any new episodes. Until this issue is resolved on Spotify’s side, you can subscribe via the RSS feed above or via any other podcatcher to get new episodes.*

A new financially-motivated threat actor tracked as Scattered Spider has been on a rampage over the past few months, hacking into the networks of telcos and outsourcing companies in order to gain access to customer information and, in some cases, carry out SIM-swapping attacks.

The attacks have been taking place since June this year and follow a model previously made popular by the Lapsus$ gang.

The initial stages start with phone calls and text or Telegram messages to a company's employees, posing as its IT department. The calls and messages ask employees to visit a phishing site or instruct them to download a boobytrapped application.

Phished credentials and compromised systems are then used to establish a foothold inside a company's network, with the group quickly acting to move laterally across the network and create multiple persistence methods for future access.

Security firm CrowdStrike—which detailed Scattered Spider's modus operandi in a [report](https://www.crowdstrike.com/blog/analysis-of-intrusion-campaign-targeting-telecom-and-bpo-companies/) published last Friday—described the group and its actions as "extremely persistent and brazen."

They operate using many open-source tools and across Windows, Linux, Google Workspace, AzureAD, Microsoft 365, and AWS environments, sometimes in a very noisy way.

If their intrusions are detected, Scattered Spider operators will re-access a victim's network through their backdoors and use their access to roll back security mitigations put in place by the targeted organisation. If they lose access to a network, CrowdStrike says the group immediately moves to a new target as if nothing happened.

CrowdStrike said that "swift and bold" security measures to isolate compromised environments had the best results in kicking the group out of a victim's network and making it move to a new target.

[![](https://substackcdn.com/image/fetch/$s_!FrDM!,w_1456,c_limit,f_auto,q_auto:good,fl_progressive:steep/https%3A%2F%2Fbucketeer-e05bbc84-baa3-437e-9518-adb32be77984.s3.amazonaws.com%2Fpublic%2Fimages%2F348ecb6b-b975-4e9f-943f-bec622aba405_1714x674.png)](https://substackcdn.com/image/fetch/%24s_%21FrDM%21%2Cf_auto%2Cq_auto%3Agood%2Cfl_progressive%3Asteep/https%3A//bucketeer-e05bbc84-baa3-437e-9518-adb32be77984.s3.amazonaws.com/public/images/348ecb6b-b975-4e9f-943f-bec622aba405_1714x674.png)

### Breaches and hacks

**Amnesty International hack:** A Chinese APT group has breached the network of the Canadian branch of Amnesty International, [the organization said on Monday](https://amnesty.ca/news/news-releases/cyber-breach-statement/). The breach was discovered in early October and was investigated and confirmed with the help of cybersecurity firm Secureworks. [Speaking to reporters](https://www.abc.net.au/news/2022-12-06/amnesty-international-canada-says-it-was-hacked-by-china/101740268), Amnesty International said the hackers searched for information on China, Hong Kong, and prominent Chinese activists. The organization said there found no evidence to suggest that Chinese hackers stole information on its donors and members. In August, threat intelligence firm [Recorded Future warned](https://www.recordedfuture.com/redalpha-credential-theft-campaign-targeting-humanitarian-thinktank) that a Chinese APT named RedAlpha was registering lookalike domain names impersonating various human rights organizations, including Amnesty International.

**It was ransomware:** Rackspace has [confirmed](https://www.rackspace.com/newsroom/rackspace-technology-hosted-exchange-environment-update) that the [major outage](https://status.apps.rackspace.com/index/viewincidents?group=2) of its Exchange email server infrastructure that took place over the weekend was caused by ransomware.

**Mercury IT ransomware incident:** The New Zealand government [said](https://www.privacy.org.nz/publications/statements-media-releases/new-news-page-5/) that a ransomware attack on Mercury IT, a major local MSP, has impacted the services of several private and public institutions. The attack took place last week on November 30. According to the [NZ Herald](https://www.nzherald.co.nz/business/spreading-cyberattacks-privacy-commissioner-opening-investigation-into-wellingtons-mercury-it/SL5KSANTGBHCNEWC7G77VKU3XU/), the incident has impacted and compromised the data of the Ministry of Justice, the Ministry of Health, the NZ National Nurses Association, health insurer Accuro, and private industry group BusinessNZ.

**Helio crypto-heist:** In our [last newsletter](https://riskybiznews.substack.com/p/risky-biz-news-samsung-mediatek-and), we featured a bit about the Ankr DeFi platform being exploited to steal $5 million. Apparently, as Binance was working with Ankr to prevent the hacker from stealing BNB coins, this left the door open for another attacker to exploit the Helio platform and steal $15 million. See [CoinDesk's explanation](https://www.coindesk.com/tech/2022/12/02/how-attackers-made-15m-from-staking-platform-helio-after-ankr-exploit/) for what happened. It's hard to keep track of the card castle that cryptocurrency protocols are starting to look like.

### General tech and privacy

**Threema's new Ibex protocol:** E2EE instant messaging service Threema has launched a new cryptographic protocol suite named [Ibex](https://threema.ch/en/blog/posts/ibex). The new protocol supports [Perfect Forward Secrecy](https://en.wikipedia.org/wiki/Forward_secrecy), and Threema said it worked with external cryptographers for more than 18 months to make the protocol "future proof." In addition to deploying Ibex, Threema said it also added E2EE support for group calls, something that very few secure messaging services currently support.

### Government, politics, and policy

**EU funds Cyber Lab in Ukraine:** The EU has [financed and delivered](https://www.eeas.europa.eu/eeas/ukraine-eu-sets-cyber-lab-ukrainian-armed-forces_en) software and hardware equipment for the creation of a cyber lab inside the Ukrainian Armed Forces. The lab will allow Ukraine to train military cyber defense professionals in a virtual environment using real-time simulations. The lab was formally unveiled in Kyiv last week, and EU officials hope it will help Ukraine's military detect and r...