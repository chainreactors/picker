---
title: BTMOB Exposed: Inside a Fraud-as-a-Service Platform with 1400+ live servers
url: https://blog.quimerax.com/btmob-exposed-inside-a-fraud-as-a-service-platform-with-1400-live-servers/
source: Over Security
date: 2026-08-20
fetch_date: 2026-08-21T03:05:01.407828
---

# BTMOB Exposed: Inside a Fraud-as-a-Service Platform with 1400+ live servers

[![QuimeraX Intelligence | Blog](https://blog.quimerax.com/content/images/2025/05/logo-amarelo-clean.dQE0sSac-1.png)](https://blog.quimerax.com)

* [Home](https://blog.quimerax.com/)
* [About](https://quimerax.com)

# BTMOB Exposed: Inside a Fraud-as-a-Service Platform with 1400+ live servers

[![QuimeraX Team](https://blog.quimerax.com/content/images/2025/05/logo-amarelo-clean.dQE0sSac-2.png)](/author/quimerax-team/)

#### [QuimeraX Team](/author/quimerax-team/)

17 ago 2026

18 min

![BTMOB Exposed: Inside a Fraud-as-a-Service Platform with 1400+ live servers](/content/images/size/w1200/2026/08/btmob-2-.png)

From the Middle East to Brazil: how BTMOB became a franchised Android banking threat.

## The Trail

In February 2023, cryptocurrency payment processor **Freewallet** froze roughly $75,000 in accumulated earnings from a customer in Syria. The company demanded KYC verification. That moment of financial friction cracked the operational security that a threat actor known as **EVLF** had maintained for approximately eight years, and gave cybersecurity firm **[CYFIRMA](https://www.cyfirma.com/research/unmasking-evlf-dev-the-creator-of-cypherrat-and-craxsrat/?ref=blog.quimerax.com)** the thread they needed to unravel one of the most prolific Android RAT operations on the market.

**EVLF** (also known as **EvilWolf**, or **"EVLF DEV"**) had been building and selling Android remote access trojans from Syria since roughly 2015. His first publicly tracked products were **CypherRAT** and **CraxsRAT**, distributed through a surface-web shop and a Telegram channel (**`@craxso`**) that accumulated over 10,000 subscribers. Over three years, an estimated 100 or more threat actors purchased lifetime licenses. The ecosystem eventually fractured when buyers began releasing cracked versions for free, a pattern that would repeat, almost identically, with BTMOB.

The lineage from CraxsRAT to BTMOB runs through an intermediate family called **SpySolr**. Multiple independent analyses (Cyble, ESET, ANY.RUN, Mallory.ai) confirm that BTMOB is an evolution of SpySolr, itself derived from the CraxsRAT codebase. The architectural "DNA" is unmistakable: the same Accessibility Service abuse patterns, similar WebSocket-based C2 communication, overlapping command structures. But BTMOB represented a leap in ambition: from a general-purpose RAT to a purpose-built banking fraud platform with a professional operator experience.

When **[Cyble Research](https://cyble.com/blog/btmob-rat-newly-discovered-android-malware?ref=blog.quimerax.com)** and **Intelligence Labs (CRIL)** published the first public analysis on February 12, 2025 (based on a sample discovered January 31), the malware was at version **BT-v2.5.** It was distributed as **`lnat-tv-pro.apk`** through a phishing site impersonating iNat TV, a Turkish streaming platform.

![](https://blog.quimerax.com/content/images/2026/08/figure1.png)
*Figure 1: BTMOB distributed via a fake iNat TV site. Source: Cyble.*

The C2 server resolved to **`hxxp://server[.]yaarsa[.]com/con`**. That domain, **yaarsa**, persists as the name of the backend directory in every leaked source package we analyzed. The entire C2 backend still lives under **`/yaarsa/private/`**, the database is still called **`clients`**, and every PHP handler still follows the **`yarsap_NNNNN.php`** naming convention established when **`yaarsa[.]com`** was the canonical server.
**The infrastructure moved on. The code remembers.**

![](https://blog.quimerax.com/content/images/2026/08/figure2-2.png)
*Figure 2: The **yaarsa** directory from the leaked source, the backend structure that persists across every analyzed package.*

Since then, BTMOB has continued to evolve. We obtained the source code packages for versions **4.5.7** and **4.6**, which together comprise the full operator kit: the **VB.NET operator panel** (80 `.vb` files), the **server-side APK builder pipeline** (SolrStarter/SolrWorker .NET executables), the **complete Android source tree** (101 Java files: genuine development source, not a decompile), **the dropper**, and the **entire C2 backend.**

What the source code reveals goes beyond feature additions. It reveals a structural transformation from a centralized operation into a self-service criminal franchise, complete with a reseller API, whitelabel branding, automated APK generation, and capabilities that extend far beyond banking fraud into DDoS, cryptomining, and network exploitation.

This report traces BTMOB from its roots in a Syrian developer's earlier malware projects to its current form as a full-featured Android attack platform, and documents what the leaked source code reveals.

## The Developer Speaks

EVLF operates the official Telegram account **`@CRAXSO`** and maintains a surface-web storefront at **`btmobrat[.]net`.** This storefront funnels visitors straight to Telegram: a "Join us on Telegram" button links to the operation's community of three group chats.

![](https://blog.quimerax.com/content/images/2026/08/figure4.png)
*Figure 3: The BTMOB Telegram community: three group chats linked directly from the **btmobrat[.]net** storefront*

The FAQ message in one of the Telegram groups states that the developer of BTMOB is "EVLF (EvilWolf), owner and administrator of the official Telegram channel @CRAXSO" and that he is "exclusively present in this channel."

The FAQ also addresses a drama that speaks directly to the platform's fragmentation: an impersonator using the handle **`@btmobadmin`** reportedly bought the source code and began releasing customized versions while claiming to be the original developer. According to the FAQ, this has been ongoing for over two years. This is not an isolated incident; it's the inevitable consequence of selling source code access for a tool with an established reputation.

![](https://blog.quimerax.com/content/images/2026/08/figure5.png)
*Figure 4: BTMOB's official Telegram FAQ addressing impersonation. Evidence of the platform's fragmentation, straight from the operator.*

![](https://blog.quimerax.com/content/images/2026/08/figure3.png)
*Figure 5: EVLF **(@CRAXSO)** Telegram account on August 12, 2026.*

## The Real Price of Source Code

BTMOB's pricing history reads like a startup's pivot narrative, except the product is a banking trojan.

| Date | Product | Price |
| --- | --- | --- |
| Jan 2025 | Monthly subscription | $700/mo |
| Jan 2025 | Lifetime license | $3,000 |
| Jan 2025 | Private infra + support | $5,000 + $300/mo |
| May 2025 | Full source code | $20,000 |
| Dec 2025 | Source code (reduced) | $10,000 |
| Apr 2026 (V4.5) | Lifetime account | $1,200 |
| Apr 2026 (V4.5) | Private server (multi-acct) | $3,000 |
| Apr 2026 (V4.5) | Server source code | $7,000 |
| Aug 2026 (current) | Lifetime | $700 |
| Aug 2026 (current) | Source code | $2,000 |
| Secondary market | Lifetime access | $500 |
| Secondary market | Source code | $1,500 |
| Secondary market | Lifetime + custom branding | $800 |

The price trajectory tells a story of market pressure. As cracked and leaked versions proliferated, official prices plummeted. Multiple leak events accelerated the fragmentation: source packages began circulating on underground forums and Telegram channels in mid-2025, and in January 2026 BTMOB v3.6.3 source code appeared on a dark web forum. Around the same time, the v4.x packages we analyzed (containing the full backend and the complete operator kit) became available through secondary distribution channels.

## From Product to Franchise

The source code reveals the exact moment the business model changed.

In **`btlogin.php`**, the **HWID (Hardware ID)** enforcement that once locked each operator account to a single machine is commented out. Not deleted. Commented out. The V3.2 changelog from April 13, 2025 makes it explicit: "Disabled BTMOB device hardware lock, you can now change your PC anytime."

![](https://blog.quimerax.com/content/images/2026/08/figure6-1.png)
*Figure 6: Operator changelog extract...