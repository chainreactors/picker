---
title: Russia’s Trident Ursa (aka Gamaredon APT) Cyber Conflict Operations Unwavering Since Invasion of Ukraine
url: https://buaq.net/go-140745.html
source: unSafe.sh - 不安全
date: 2022-12-21
fetch_date: 2025-10-04T02:04:18.816017
---

# Russia’s Trident Ursa (aka Gamaredon APT) Cyber Conflict Operations Unwavering Since Invasion of Ukraine

* [unSafe.sh - 不安全](https://unsafe.sh)
* [我的收藏](/user/collects)
* [今日热榜](/?hot=true)
* [公众号文章](/?gzh=true)
* [导航](/nav/index)
* [Github CVE](/cve)
* [Github Tools](/tools)
* [编码/解码](/encode)
* [文件传输](/share/index)
* [Twitter Bot](https://twitter.com/buaqbot)
* [Telegram Bot](https://t.me/aqinfo)
* [Search](/search/search)

[Rss](/rss.xml)

[ ]
黑夜模式

![](https://8aqnet.cdn.bcebos.com/de3462b93ce53e25e77fbaf913fe2d53.jpg)

Russia’s Trident Ursa (aka Gamaredon APT) Cyber Conflict Operations Unwavering Since Invasion of Ukraine

Executive SummarySince our l
*2022-12-20 19:0:57
Author: [unit42.paloaltonetworks.com(查看原文)](/jump-140745.htm)
阅读量:38
收藏*

---

![A pictorial representation of Trident Ursa showing a purple bear and trident](https://unit42.paloaltonetworks.com/wp-content/uploads/2022/12/PA-Unit42-TAC-Trident-URSA_-Landscape.jpg)

## **Executive Summary**

Since our last blog in early February covering the advanced persistent threat (APT) group [Trident Ursa (aka Gamaredon, UAC-0010, Primitive Bear, Shuckworm)](https://unit42.paloaltonetworks.com/gamaredon-primitive-bear-ukraine-update-2021/), Ukraine and its cyber domain has faced ever-increasing threats from Russia. Trident Ursa is a group [attributed by the Security Service of Ukraine](https://ssu.gov.ua/uploads/files/DKIB/Technical%20report%20Armagedon.pdf) to Russia’s Federal Security Service.

As the conflict has continued on the ground and in cyberspace, Trident Ursa has been operating as a dedicated access creator and intelligence gatherer. Trident Ursa remains one of the most pervasive, intrusive, continuously active and focused APTs targeting Ukraine.

Given the ongoing geopolitical situation and the specific target focus of this APT group, Unit 42 researchers continue to actively monitor for indicators of their operations. In doing so, we have mapped out over 500 new domains, 200 samples and other Indicators of Compromise (IoCs) used within the past 10 months that support Trident Ursa’s different phishing and malware purposes.

We are providing this update along with [known IoCs](https://github.com/pan-unit42/iocs/blob/master/Gamaredon/Gamaredon_IoCs_DEC2022.txt) to highlight and share our current overall understanding of Trident Ursa’s operations.

While monitoring these domains as well as open source intelligence, we have identified multiple items of note:

* An unsuccessful attempt to compromise a large petroleum refining company within a NATO member nation on Aug. 30.
* An individual who appears to be involved with Trident Ursa threatened to harm a Ukraine-based cybersecurity researcher immediately following the initial invasion.
* Multiple shifts in their tactics, techniques and procedures (TTPs).

Palo Alto Networks customers receive protections against the types of threats discussed in this blog by products including [Cortex XDR](https://www.paloaltonetworks.com/cortex/cortex-xdr), [WildFire](https://www.paloaltonetworks.com/network-security/wildfire), [Advanced URL Filtering](https://www.paloaltonetworks.com/network-security/advanced-url-filtering), [Advanced Threat Prevention](https://www.paloaltonetworks.com/network-security/advanced-threat-prevention) and [DNS Security](https://www.paloaltonetworks.com/network-security/dns-security) subscription services for the [Next-Generation Firewall](https://www.paloaltonetworks.com/network-security/next-generation-firewall).

|  |  |
| --- | --- |
| **Related Unit 42 Topics** | [Russia](https://unit42.paloaltonetworks.com/tag/russia/), [Ukraine](https://unit42.paloaltonetworks.com/tag/ukraine/), [Gamaredon](https://unit42.paloaltonetworks.com/tag/gamaredon/) |
| **Trident Ursa APT Group akas** | Gamaredon, UAC-0010, Primitive Bear, Shuckworm |

## **Table of Contents**

[Targeting Beyond Ukraine](#post-126209-_q4yt4t8e060w)

## **Targeting Beyond Ukraine**

Traditionally, Trident Ursa has primarily targeted Ukrainian entities with Ukrainian language lures. While this is still the most common scenario for this group, we saw a few instances of them using English language lures. We assess that these samples indicate that Trident Ursa is attempting to boost their intelligence collection and network access against Ukrainian and NATO allies.

In line with these efforts to target allied governments, during a review of their IoCs we identified an unsuccessful attempt to compromise a large petroleum refining company within a NATO member nation on Aug. 30.

|  |  |
| --- | --- |
| **SHA256** | **Filename** |
| b1bc659006938eb5912832eb8412c609d2d875c001ab411d1b69d343515291b7 | MilitaryassistanceofUkraine.htm |
| 0b63f6e7621421de9968d46de243ef769a343b61597816615222387c45df80ae | Necessary\_military\_assistance.rar |
| 303abc6d8ab41cb00e3e7a2165ecc1e7fb4377ba46a9f4213a05f764567182e5 | List of necessary things for the provision of military humanitarian assistance to Ukraine.lnk (Note: File bundled in above .rar) |

*Table 1. English language samples used by Trident Ursa.*

## **Beyond Just Hacking: Open Threats to Cybersecurity Community**

One of our most surprising observations was when an individual named Anton (in Cyrillic, Антон) who appeared to be tied to Trident Ursa threatened a small group of cybersecurity researchers on Twitter, on the same day Russia invaded Ukraine (Feb. 24, 2022). It appears that Anton chose these researchers based on their tweets highlighting Trident Ursa’s IoCs in the days prior to the invasion.

The first tweets (shown in Figure 1) came from Anton (@Anton15001398) as the invasion was underway, to Ukraine-based threat researcher Mikhail Kasimov (@500mk500). In several tweets, he said, “run, i’m coming for you.” Likely figuring his first tweets to Kasimov were too unnoticeable, his last tweet included the #Gamaredon hashtag so it would be more publicly discoverable by other researchers.

![Image 1 is a series of three tweets made by Twitter user Anton15001398 targeting Ukrainian-based threat researcher Mikhail Kasimov, whose Twitter account is 500mk500. In the tweets the actor uses the hashtag Gamaredon and tells Mikhail to “run, I’m coming for you.” ](https://unit42.paloaltonetworks.com/wp-content/uploads/2022/12/word-image-71.png)

Figure 1. Threatening Mikhail Kasimov.

Later that same day, Anton used a different account (@YumHSh2UdIkz64w) to send Shadow Chaser Group (@ShadowChasing1) and TI Research (@tiresearch1) the ominous message “let's be friends. We do not want to fight, but we do it well!” as shown in Figure 2.

![Image 2 is a screenshot of a tweet made by Twitter user YumHSh2UdIkz64w tagging Shadow Chaser Group’s Twitter account ShadowChasing1) and the TI Research Twitter account tiresearch1 with the message “let's be friends. We do not want to fight, but we do it well!” It uses the hashtag Gamaredon.](https://unit42.paloaltonetworks.com/wp-content/uploads/2022/12/word-image-72.png)

Figure 2. Warning away Shadow Chaser Group and TI Research.

Two days later, on Feb. 26, Anton sent his last and most threatening tweet yet (Figure 3). In it, he provides Mikhail Kasimov’s full name, date of birth and address along with the message, “We are already in the city, there is nowhere to run. You had a chance.”

![ Image 3 is a screenshot of a tweet made by Twitter user YumHSh2UdIkz64w targeting Ukrainian-based threat researcher Mikhail Kasimov. He reveals personal information that has been redacted in the screenshot with the message “We are already in the city, there is nowhere to run. You had a chance.” It uses the hashtag Gamaredon. ](https://unit42.paloaltonetworks.com/wp-content/uploads/2022/12/word-image-73.png)

Figure 3. Doxing and threatening Mikhail Kasimov (full name, date of birth, and address redacted from the original tweet).

We imagine these direct, threatening communications from this purported Trident Ursa associate were unsettling to the recipients (especially Mikhail Kasimov, a researcher operating from within the war zone). To their credit, the targeted researchers were undaunted, and tweeted add...