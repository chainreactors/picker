---
title: Risky Biz News: Disgruntled member doxes and extorts URSNIF gang
url: https://riskybiznews.substack.com/p/risky-biz-news-disgruntled-member
source: Over Security - Cybersecurity news aggregator
date: 2022-12-13
fetch_date: 2025-10-04T01:19:54.900469
---

# Risky Biz News: Disgruntled member doxes and extorts URSNIF gang

[![!!! Do not subscribe! We have moved!](https://substackcdn.com/image/fetch/$s_!dl-9!,w_80,h_80,c_fill,f_auto,q_auto:good,fl_progressive:steep,g_auto/https%3A%2F%2Fbucketeer-e05bbc84-baa3-437e-9518-adb32be77984.s3.amazonaws.com%2Fpublic%2Fimages%2F472a6618-0312-430d-8238-49e88cf01b91_1280x1280.png)](/)

# [!!! Do not subscribe! We have moved!](/)

SubscribeSign in

# Risky Biz News: Disgruntled member doxes and extorts URSNIF gang

### In other news: PyPI and npm packages deploy ransomware; Japan wants to carry out preemptive cyber-attacks; Pwn2Own Toronto hacking contest results.

[![Catalin Cimpanu's avatar](https://substackcdn.com/image/fetch/$s_!nOnN!,w_36,h_36,c_fill,f_auto,q_auto:good,fl_progressive:steep/https%3A%2F%2Fbucketeer-e05bbc84-baa3-437e-9518-adb32be77984.s3.amazonaws.com%2Fpublic%2Fimages%2Fe393d520-317c-4283-bbb0-64aaaa65bf19_460x460.jpeg)](https://substack.com/%40campuscodi)

[Catalin Cimpanu](https://substack.com/%40campuscodi)

Dec 12, 2022

Share

***This newsletter is brought to you by [Airlock Digital](https://www.airlockdigital.com/), [Proofpoint](https://www.proofpoint.com/), [runZero](https://www.runzero.com/), and [Thinkst Canary](https://canary.tools/). You can subscribe to an audio version of this newsletter as a podcast by searching for "Risky Business News" in your podcatcher or subscribing via [this RSS feed](https://risky.biz/feeds/risky-business-news/).***

An individual claiming to be a former member of the URSNIF malware operation has leaked the real-world identities of three of the gang's members in a series of tweets last week.

The account, going by the name of [URSNIFleak](https://twitter.com/URSNIFleak), has also released snippets from the gang's [internal chats](https://archive.ph/KqvhA), along with [screenshots](https://archive.ph/cp7jA) of some of the URSNIF malware's source code and [private](https://archive.ph/IFkfN) [messages](https://archive.ph/PXXkE) sent via an [underground](https://archive.ph/3wytF) [malware forum](https://archive.ph/RKyhG), discussing topics like money laundering and the war in Ukraine.

The incident marks the fourth major doxing of a cybercrime operation this year after similar leaks exposed crucial and very sensitive information about the operations of [the Conti ransomware](https://www.trellix.com/en-gb/about/newsroom/stories/research/conti-leaks-examining-the-panama-papers-of-ransomware.html), the [TrickBot trojan](https://www.cyjax.com/2022/07/15/who-is-trickbot/), and [the Yanluowang ransomware gang](https://riskybiznews.substack.com/p/risky-biz-news-internal-chats-for).

The first two leaks were driven by an anti-Russian sentiment as the Conti gang (which also managed the TrickBot botnet) showed their support for Russia's brutal invasion of Ukraine. The reasons for the Yanluowang leak are still unknown.

However, the reason behind the URSNIF leak is much more mundane—and it's revenge and your [run-of-the-mill extortion](https://archive.ph/cp7jA).

The leak was teased over several days (*on a first now-suspended Twitter account*); they first leaked details of low-level members to show they were serious ([1](https://archive.ph/GGE5i), [2](https://archive.ph/wZYUH), [3](https://archive.ph/KRi74)); and the URSNIFleak account stopped posting new content after the leader of the URSNIF gang (*an individual named CAP*) [paid them off](https://archive.ph/xnEQu) to keep quiet.

"I just made more money in a single week than I have made in years. Pay workers right and they wont have a reason to leak s\*\*\*," URSNIFleak [wrote](https://archive.ph/obIt4) in their last tweet before allegedly closing the account.

In another tweet, URSNIFleak said they decided to go through with the leak and extortion after reading statements made by the URSNIF leader in a recent [interview](https://papers.vx-underground.org/papers/Other/Interviews/Interviewing%20the%20organizer%20for%20URSNIF%20banking%20trojan.html) with the VX-Underground project. What particular part, they did not say.

"The interview angered me," URSNIFleak [said](https://archive.ph/6HFqr). "He has been a bad boss for a long time. I have been waiting for the right time to release."

Compared to the Conti, TrickBot, and Yanluowang leaks, less information was released in the URSNif dox, but despite this, nobody in infosec is complaining. More cybercrime leaks, plz! Especially leaks like these that show how [URSNIF's recent pivot to a ransomware operation](https://www.mandiant.com/resources/blog/rm3-ldr4-ursnif-banking-fraud) was [not as successful](https://archive.ph/iRKzI) as the gang was hoping.

[![](https://substackcdn.com/image/fetch/$s_!wVQw!,w_1456,c_limit,f_auto,q_auto:good,fl_progressive:steep/https%3A%2F%2Fbucketeer-e05bbc84-baa3-437e-9518-adb32be77984.s3.amazonaws.com%2Fpublic%2Fimages%2F81d45347-7cca-420a-a4ab-06f774a530a2_1000x1533.png)](https://substackcdn.com/image/fetch/%24s_%21wVQw%21%2Cf_auto%2Cq_auto%3Agood%2Cfl_progressive%3Asteep/https%3A//bucketeer-e05bbc84-baa3-437e-9518-adb32be77984.s3.amazonaws.com/public/images/81d45347-7cca-420a-a4ab-06f774a530a2_1000x1533.png)

### Breaches and hacks

**Rackspace faces three CALs:** Cloud hosting provider Rackspace will have to defend [at least three different class-action lawsuits](https://www.expressnews.com/business/article/Another-class-action-lawsuit-filed-over-Rackspace-17640869.php) related to a ransomware attack that hit a part of its server infrastructure and has left countless companies without access to their email servers. In an [interview](https://www.barrons.com/articles/rackspace-ransomware-attack-update-2022-fbi-51670634273) last week, Rackspace suggested they might not be able to recover all their customers' data, which they referred to as "legacy data." The company also appears to have given up on hosting Exchange email servers in its cloud and said it was migrating all its existing customers to Microsoft 365. Migrating its Exchange customers to a rival will cost the company $30 million, according to [documents](https://www.sec.gov/ix?doc=/Archives/edgar/data/0001810019/000119312522298940/d388117d8k.htm#:~:text=Although%20we%20are,to%20the%20incident.) Rackspace filed with the SEC.

**Lodestar Finance crypto-heist:** A threat actor has [abused an exploit](https://blog.lodestarfinance.io/post-mortem-summary-13f5fe0bb336) in the smart contract of the Lodestar Finance DeFi platform and has stolen more than $5.8 million worth of cryptocurrency. The platform [said](https://twitter.com/CertiKAlert/status/1601855745905115136) it already recovered $2.4 million of the stolen funds and is still working to secure the rest. Just like most cryptocurrency platforms that get popped these days, Lodestar has offered to let the hacker keep some of the stolen funds and hide the intrusion under a "[white-hat agreement](https://archive.ph/KyjJk)."

### General tech and privacy

**Edge support on Windows 7/8:** Microsoft plans to end support for its Edge web browser on Windows 7 and Windows 8/8.1 versions next year, [on January 10, 2023](https://blogs.windows.com/msedgedev/2022/12/09/microsoft-edge-and-webview2-ending-support-for-windows-7-and-windows-8-8-1/). This is the same date when both [Windows 7](https://learn.microsoft.com/en-us/lifecycle/products/windows-7) and [Windows 8/8.1](https://learn.microsoft.com/en-us/lifecycle/products/windows-81) will reach End-Of-Life (EOL) after their extended support periods expire. Google also [announced](https://support.google.com/chrome/thread/185534985/sunsetting-support-for-windows-7-8-1-in-early-2023?hl=en) earlier this fall that Chrome version 110 would be the last to support both Windows 7 and Windows 8/8.1. Chrome 110 is scheduled for release in February 2023.

**Chrome passkeys support:** Google has [added formal support](https://blog.chromium.org/2022/12/introducing-passkeys-in-chrome.html) for the passkeys authentication mechanism to its Chrome web browser through an [update](https://chromereleases.googleblog.com/2022/12/stab...