---
title: Risky Biz News: North Korean hackers behind supply chain attack on 3CX
url: https://riskybiznews.substack.com/p/risky-biz-news-north-korean-hackers
source: Over Security - Cybersecurity news aggregator
date: 2023-04-01
fetch_date: 2025-10-04T11:24:07.794932
---

# Risky Biz News: North Korean hackers behind supply chain attack on 3CX

[![!!! Do not subscribe! We have moved!](https://substackcdn.com/image/fetch/$s_!dl-9!,w_80,h_80,c_fill,f_auto,q_auto:good,fl_progressive:steep,g_auto/https%3A%2F%2Fbucketeer-e05bbc84-baa3-437e-9518-adb32be77984.s3.amazonaws.com%2Fpublic%2Fimages%2F472a6618-0312-430d-8238-49e88cf01b91_1280x1280.png)](/)

# [!!! Do not subscribe! We have moved!](/)

SubscribeSign in

# Risky Biz News: North Korean hackers behind supply chain attack on 3CX

### In other news: Lumen discloses two security breaches; UAE users targeted with zero-days from Spanish vendor; VulkanFiles leak exposes Russian military hacking tools.

[![Catalin Cimpanu's avatar](https://substackcdn.com/image/fetch/$s_!nOnN!,w_36,h_36,c_fill,f_auto,q_auto:good,fl_progressive:steep/https%3A%2F%2Fbucketeer-e05bbc84-baa3-437e-9518-adb32be77984.s3.amazonaws.com%2Fpublic%2Fimages%2Fe393d520-317c-4283-bbb0-64aaaa65bf19_460x460.jpeg)](https://substack.com/%40campuscodi)

[Catalin Cimpanu](https://substack.com/%40campuscodi)

Mar 31, 2023

Share

***This newsletter is brought to you by [Airlock Digital](https://www.airlockdigital.com/), [Proofpoint](https://www.proofpoint.com/), [runZero](https://www.runzero.com/), and [Thinkst Canary](https://canary.tools/). You can subscribe to an audio version of this newsletter as a podcast by searching for "Risky Business News" in your podcatcher or subscribing via [this RSS feed](https://risky.biz/feeds/risky-business-news/).***

A threat actor has compromised VoIP software development company 3CX and has trojanized its macOS and Windows desktop clients with malware.

The incident was discovered by cybersecurity firm [CrowdStrike](https://www.crowdstrike.com/blog/crowdstrike-detects-and-prevents-active-intrusion-campaign-targeting-3cxdesktopapp-customers/), and the company believes this may be the work of a North Korean state actor tracked as [Labyrinth Chollima](https://www.crowdstrike.com/adversaries/labyrinth-chollima/), also known as the Lazarus Group or Hidden Cobra.

Current evidence suggests the group infiltrated the company months before and hid malware in the company's macOS and Windows desktop clients around the start of the month. Customers who downloaded the apps were infected. The malware was also installed on some systems via the app's built-in updating feature—if this was enabled.

Security researchers who investigated the incident following Crowdstrike's initial disclosure say the malware went under the radar for weeks until the past few days when it started aggressively reaching out to a number of domains suspected of being controlled by the Labyrinth Chollima group.

The current thinking is that the North Korean operators saw recent posts on the 3CX forum from customers complaining about the trojanized Windows client triggering antivirus warnings and decided to exploit their access while they still had it and before security vendors realized what was actually happening.

In addition to beaconing activity, CrowdStrike says that in some cases, its security tools also detected the deployment of second and third-stage payloads and, in a small number of cases, even "hands-on-keyboard activity"—where the hackers connected to the compromised systems and ran malicious commands manually.

[SentinelOne](https://www.sentinelone.com/blog/smoothoperator-ongoing-campaign-trojanizes-3cx-software-in-software-supply-chain-attack/) says the final payload is "a previously unknown infostealer meant to interface with browser data." Stealing passwords from 3CX customer networks to enable future intrusions seems to be the end goal here.

macOS security researcher Patrick Wardle [confirmed](https://objective-see.org/blog/blog_0x73.html) the compromise of the 3CX macOS desktop client, although he was unable to find what payloads were being dropped on macOS systems. Probably something similar.

Both SentinelOne and Sophos confirmed the supply chain attack, but only CrowdStrike attributed the operation to North Korea. [Volexity](https://www.volexity.com/blog/2023/03/30/3cx-supply-chain-compromise-leads-to-iconic-incident/), [Sophos,](https://news.sophos.com/en-us/2023/03/29/3cx-dll-sideloading-attack/) [Trend Micro](https://www.trendmicro.com/de_de/research/23/c/information-on-attacks-involving-3cx-desktop-app.html), and [Huntress](https://www.huntress.com/blog/3cx-voip-software-compromise-supply-chain-threats) also have technical reports on the incident and the malware.

The incident is as bad as it gets, primarily because of the popularity of 3CX solutions.

The company's products include hosted and on-premise telephony VoIP IPBX servers. Employees in companies with 3CX VoIP IPBX servers can either use a VoIP phone or install the 3CX softphone on their devices to make and receive calls or host video conferences via a desktop or mobile app. It's these macOS and Windows desktop apps that were trojanized.

It's unclear how many users downloaded the trojanized desktop clients or how many received the malicious update for existing clients, but 3CX's customer base is huge. The company claims on its website to serve more than 600,000 companies and more than 12 million daily users. Per its [website](https://www.3cx.com/company/customers/), 3CX serves some of today's largest corporations.

[![](https://substackcdn.com/image/fetch/$s_!BR-e!,w_1456,c_limit,f_auto,q_auto:good,fl_progressive:steep/https%3A%2F%2Fsubstack-post-media.s3.amazonaws.com%2Fpublic%2Fimages%2F611b509e-46d3-4c5d-b985-2fd68ce7641f_1315x866.png)](https://substackcdn.com/image/fetch/%24s_%21BR-e%21%2Cf_auto%2Cq_auto%3Agood%2Cfl_progressive%3Asteep/https%3A//substack-post-media.s3.amazonaws.com/public/images/611b509e-46d3-4c5d-b985-2fd68ce7641f_1315x866.png)

A [Shodan search](https://www.shodan.io/search?query=http.favicon.hash%3A970132176) returns more than 245,000 3CX VoIP IPBX servers, just to give you an idea of how popular the 3CX system is.

As for 3CX, well, it's not good. At all. First, they didn't detect the intrusion for months. Second, when several antivirus products started detecting their clients as malicious, they repeatedly claimed it was just false positives, over and over again, without investigating further. When 4-5 different vendors see the same thing, it's probably a indicator you should look at your app. Third, some customers said that when they went to 3CX's customer support with CrowdStrike's findings, they were asked to "[open a support ticket at £75 per incident](https://archive.ph/DkWSh#selection-2579.99-2579.140)." That's just... not what people wanted to hear.

The company did eventually confirm the incident in a [blog post](https://www.3cx.com/blog/news/desktopapp-security-alert/) and promised to release new clean desktop client versions. Until then, 3CX recommended that customers use its web-based PWA app instead.

### **Breaches and hacks**

**Lumen discloses two security breaches:** Lumen Technologies, one of the largest US telcos and infrastructure providers, has disclosed in [an SEC filing](https://www.sec.gov/ix?doc=/Archives/edgar/data/18926/000119312523079847/d467138d8k.htm) that it suffered not one but two security breaches. The first was a ransomware attack that hit servers part of the company's hosting infrastructure. Lumen says the incident is degrading the operations of a small number of enterprise customers. The second incident is more severe. Lumen described the attacker as "a separate sophisticated intruder" that managed to gain access to some of its internal systems, where it conducted reconnaissance, installed malware, and extracted "a relatively limited amount of data."

**Russian pilots doxxed:** Pro-Ukraine hacktivist group Cyber Resistance has hacked into the personal accounts of the Russian pilots who bombed civilian infrastructure in the city of Mariupol at the start of the Ukrainian war. The hackers [publicly identified](https://informnapalm.org/ua/zlam-75387-960-aviapolku/) the commander of the unit responsible for the bombings and leaked his inbox. They a...