---
title: Risky Biz News: URSNIF goes from banking trojan to backdoor, dreaming of ransomware profits
url: https://riskybiznews.substack.com/p/risky-biz-news-ursnif-goes-from-banking
source: Over Security - Cybersecurity news aggregator
date: 2022-10-22
fetch_date: 2025-10-03T20:37:48.906319
---

# Risky Biz News: URSNIF goes from banking trojan to backdoor, dreaming of ransomware profits

[![!!! Do not subscribe! We have moved!](https://substackcdn.com/image/fetch/$s_!dl-9!,w_80,h_80,c_fill,f_auto,q_auto:good,fl_progressive:steep,g_auto/https%3A%2F%2Fbucketeer-e05bbc84-baa3-437e-9518-adb32be77984.s3.amazonaws.com%2Fpublic%2Fimages%2F472a6618-0312-430d-8238-49e88cf01b91_1280x1280.png)](/)

# [!!! Do not subscribe! We have moved!](/)

SubscribeSign in

# Risky Biz News: URSNIF goes from banking trojan to backdoor, dreaming of ransomware profits

### In other news: Microsoft discloses another data breach; Canada's Parliament got hacked; Brazilian police detain Lapsus$ member.

[![Catalin Cimpanu's avatar](https://substackcdn.com/image/fetch/$s_!nOnN!,w_36,h_36,c_fill,f_auto,q_auto:good,fl_progressive:steep/https%3A%2F%2Fbucketeer-e05bbc84-baa3-437e-9518-adb32be77984.s3.amazonaws.com%2Fpublic%2Fimages%2Fe393d520-317c-4283-bbb0-64aaaa65bf19_460x460.jpeg)](https://substack.com/%40campuscodi)

[Catalin Cimpanu](https://substack.com/%40campuscodi)

Oct 21, 2022

Share

***This newsletter is brought to you by [Airlock Digital](https://www.airlockdigital.com/), [Proofpoint](https://www.proofpoint.com/), [runZero](https://www.runzero.com/), and [Thinkst Canary](https://canary.tools/). You can subscribe to an audio version of this newsletter as a podcast by searching for "Risky Business News" in your podcatcher or subscribing via [this RSS feed](https://risky.biz/feeds/risky-business-news/).***

Researchers from security firm Mandiant have reported this week that URSNIF (aka Gozi, or Gozi/IFSB), one of the oldest and last few remaining banking trojan operations that were still active this year, has completely ditched its banking fraud-related features and now appears to operate as a basic backdoor trojan, the type of barebones malware typically used in Access-as-a-Service (AaaS) schemes that rent access to compromised devices.

[According to Mandiant](https://www.mandiant.com/resources/blog/rm3-ldr4-ursnif-banking-fraud), the change took place earlier this year, in June, when URSNIF developers started distributing a new URSNIF version tracked under a codename of LDR4.

[![](https://substackcdn.com/image/fetch/$s_!L-FD!,w_1456,c_limit,f_auto,q_auto:good,fl_progressive:steep/https%3A%2F%2Fbucketeer-e05bbc84-baa3-437e-9518-adb32be77984.s3.amazonaws.com%2Fpublic%2Fimages%2F8b78bfa6-637c-4751-a6b9-bbb2b81a2022_1000x487.png)](https://substackcdn.com/image/fetch/%24s_%21L-FD%21%2Cf_auto%2Cq_auto%3Agood%2Cfl_progressive%3Asteep/https%3A//bucketeer-e05bbc84-baa3-437e-9518-adb32be77984.s3.amazonaws.com/public/images/8b78bfa6-637c-4751-a6b9-bbb2b81a2022_1000x487.png)

Mandiant cites several reasons for URSNIF's new radical redesign. At least two leaks of its codebase, multiple branches of the same codebase that had slowly diverged and were making it harder to support features across different botnets, but also an ancient codebase that had finally reached the end of the road when IE was removed from Windows.

> "In June 2022, with Internet Explorer finally being fully removed from Microsoft Windows, the RM3 variant was officially seen as a "dead" malware from a technical point of view, as RM3 was reliant on this browser for some of its critical network communication."

Honestly, it's a surprise that URSNIF lasted this long still operating on a banking trojan model. It had become obvious in the mid-2010s that the banking malware scene was dying, at least on the desktop.

Banks, tired of a decade of heists from customer accounts, had rolled out advanced multi-factor authentication and transaction verification systems. While not foolproof, these systems did their job and made it more time-consuming for banking malware operators to steal money from compromised accounts.

Today, it's very hard to list a banking trojan off the top of my head and without googling it first.

Emotet and TrickBot converted their codebases from banking trojans to generic modular backdoors back in 2016, being some of the first to do so. Even if they kept their banking modules around, Dridex and Qbot also followed suit in subsequent years.

The driving force behind this shift in malware economics was the rise of ransomware and enterprise network big-game hunting. As ransomware operators realized they could extort an obscene amount of money from companies and government networks, they started to look for ways into these networks.

This initially led to the rise of a market for initial access brokers, smaller threat actors that typically exploited corporate networking and server gear, where they planted backdoors and then sold access to these systems to ransomware gangs and their affiliates.

EvilCorp was the first major botnet operator to realize they could use their banking trojan to drop ransomware inside the thousands of corporate networks they had at their disposal through the Dridex botnet and even launched internal teams to write and deploy their own internal forms of ransomware.

Because Dridex operated on a closed model, providing limited access to their botnet to only a handful of very carefully vetted operators, Emotet, and later TrickBot, cornered the market in MaaS services working with ransomware gangs.

Once law enforcement cracked down on the two, IcedID and Qbot stepped in as handy replacements after years of slowly growing in their shadows.

The world of underground malware is not that hard to understand if we dispel all the CTI mumbo-jumbo and we are really honest. It's all about the minimum amount of work you can perform for the largest profit. Banking/carding is now hard, thanks to banks, and ransomware is easy, thanks to a bazillion reasons.

There are literally no good reasons to run a banking botnet these days, especially one as old and complicated as URSNIF, when you can just manage a simple backdoor, spam bored corporate employees until they infect themselves, and then sell access to ransomware or cryptomining gangs for a cut of the profits.

But enough explaining basic cybercrime economics. What this means going forward for the readers of this newsletter, many of which are most likely tasked with defending networks, is that URSNIF infections now need to be treated with the same urgency as we once used to treat Emotet and Trickbot. Once it's in your network, you need to get it out ASAP, as you never know when that infected system might end up deploying ransomware to your network. If we take stats from previous IR reports, this might be somewhere from 30 minutes and up to an hour. Sure, Mandiant hasn't linked any URSNIF incident with a confirmed ransomware attack, but the writing's on the wall as clear as day.

### Breaches and hacks

**Microsoft breach:** Microsoft [confirmed](https://msrc-blog.microsoft.com/2022/10/19/investigation-regarding-misconfigured-microsoft-storage-location-2/) on Wednesday a report from security firm [SOCRadar](https://socradar.io/sensitive-data-of-65000-entities-in-111-countries-leaked-due-to-a-single-misconfigured-data-bucket/) that the OS maker misconfigured one of its cloud servers that eventually leaked the details of some of its business transactions and prospective customers. SOCRadar claimed the data of more than 65,000 customers was exposed as a result of the leaky server, but Microsoft said that "greatly exaggerated the scope of this issue" and that the number was far smaller, including many duplicates. Microsoft also said it was disappointed that SOCRadar released [BlueBleed](https://socradar.io/labs/bluebleed), a tool for users to search and see if their data was exposed in the incident.

**Defense Health Agency:** The US Defense Health Agency, the agency that provides healthcare services to the US Army, Navy, and Air Force during peace and wartime, has [disclosed a security breach](https://www.fedscoop.com/hhs-office-of-civil-rights-probes-defense-health-headquarters-cyber-incident/) that exposed the details of more than 1,200 individuals.

**Canada Parliament hack:** Canadian Parliament members have been asked to change t...