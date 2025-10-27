---
title: Risky Biz News: Ransomware wave hits thousands of VMWare ESXi servers
url: https://riskybiznews.substack.com/p/risky-biz-news-ransomware-wave-hits
source: Over Security - Cybersecurity news aggregator
date: 2023-02-07
fetch_date: 2025-10-04T05:53:20.221586
---

# Risky Biz News: Ransomware wave hits thousands of VMWare ESXi servers

[![!!! Do not subscribe! We have moved!](https://substackcdn.com/image/fetch/$s_!dl-9!,w_80,h_80,c_fill,f_auto,q_auto:good,fl_progressive:steep,g_auto/https%3A%2F%2Fbucketeer-e05bbc84-baa3-437e-9518-adb32be77984.s3.amazonaws.com%2Fpublic%2Fimages%2F472a6618-0312-430d-8238-49e88cf01b91_1280x1280.png)](/)

# [!!! Do not subscribe! We have moved!](/)

SubscribeSign in

# Risky Biz News: Ransomware wave hits thousands of VMWare ESXi servers

### In other news: Vastaamo hacker arrested; Google lays off 60% of Jigsaw staff; 28% of Microsoft user accounts use MFA.

[![Catalin Cimpanu's avatar](https://substackcdn.com/image/fetch/$s_!nOnN!,w_36,h_36,c_fill,f_auto,q_auto:good,fl_progressive:steep/https%3A%2F%2Fbucketeer-e05bbc84-baa3-437e-9518-adb32be77984.s3.amazonaws.com%2Fpublic%2Fimages%2Fe393d520-317c-4283-bbb0-64aaaa65bf19_460x460.jpeg)](https://substack.com/%40campuscodi)

[Catalin Cimpanu](https://substack.com/%40campuscodi)

Feb 06, 2023

Share

***This newsletter is brought to you by [Airlock Digital](https://www.airlockdigital.com/), [Proofpoint](https://www.proofpoint.com/), [runZero](https://www.runzero.com/), and [Thinkst Canary](https://canary.tools/). You can subscribe to an audio version of this newsletter as a podcast by searching for "Risky Business News" in your podcatcher or subscribing via [this RSS feed](https://risky.biz/feeds/risky-business-news/).***

A massive ransomware wave has hit VMWare servers over the weekend, encrypting thousands of unpatched and internet-exposed ESXi systems.

The attacks are exploiting a two-year-old vulnerability tracked as [CVE-2021-21974](https://www.zerodayinitiative.com/blog/2021/3/1/cve-2020-3992-amp-cve-2021-21974-pre-auth-remote-code-execution-in-vmware-esxi), which allows the threat actors to execute remote commands on unpatched VMWare ESXi servers via their OpenSLP service (on port 427).

Once the attackers get in, they encrypt files on the ESXi server and leave a ransom note behind, asking for $50,000 in bitcoin to decrypt each infected server.

[![](https://substackcdn.com/image/fetch/$s_!-pjs!,w_1456,c_limit,f_auto,q_auto:good,fl_progressive:steep/https%3A%2F%2Fsubstack-post-media.s3.amazonaws.com%2Fpublic%2Fimages%2F59076cd3-bd42-419e-9913-ccec83ea3c71_935x682.png)](https://substackcdn.com/image/fetch/%24s_%21-pjs%21%2Cf_auto%2Cq_auto%3Agood%2Cfl_progressive%3Asteep/https%3A//substack-post-media.s3.amazonaws.com/public/images/59076cd3-bd42-419e-9913-ccec83ea3c71_935x682.png)

An analysis from [OVHcloud's security team](https://blog.ovhcloud.com/ransomware-targeting-vmware-esxi/) initially identified the ransomware as a version of the newly launched [Nevada](https://resecurity.com/blog/article/nevada-ransomware-waiting-for-the-next-dark-web-jackpot) strain. Another report identified it as a [version of the Cheerscrypt ransomware](https://archive.ph/NJJGw)—and based on the leaked Babuk ransomware source code.

In the end, [both](https://archive.ph/UxCXc) [initial](https://archive.ph/VAhXT) assessments proved to be incorrect, and currently, the ransomware strain is tracked as **ESXiArgs**.

All in all, French cloud hosting provider OVH had a front-row seat to the attacks because France hosted most of the affected servers, hence why [France's CERT team](https://www.cert.ssi.gouv.fr/alerte/CERTFR-2023-ALE-015/) was the first agency to spot the outbreak before anyone else.

According to a [Censys search query](https://search.censys.io/search?resource=hosts&virtual_hosts=EXCLUDE&q=%28services.http.response.html_title%3A%22How+to+Restore+Your+Files%22%29+and+services.software.product%3D%60VMware+ESXi+Server%60) for the ransomware note, more than 2,500 servers have been encrypted so far, and more than a third of these are hosted in France.

[![](https://substackcdn.com/image/fetch/$s_!FykZ!,w_1456,c_limit,f_auto,q_auto:good,fl_progressive:steep/https%3A%2F%2Fsubstack-post-media.s3.amazonaws.com%2Fpublic%2Fimages%2F980297c2-b0b3-4cee-b885-70d1514d477c_1071x552.png)](https://substackcdn.com/image/fetch/%24s_%21FykZ%21%2Cf_auto%2Cq_auto%3Agood%2Cfl_progressive%3Asteep/https%3A//substack-post-media.s3.amazonaws.com/public/images/980297c2-b0b3-4cee-b885-70d1514d477c_1071x552.png)

According to replies in a [thread](https://www.bleepingcomputer.com/forums/t/782193/esxi-ransomware-help-and-support-topic-esxiargs-args-extension/) on the attacks hosted on the Bleeping Computer forum, most of the affected organizations were using ESXi servers rented from cloud providers.

As [Kevin Beaumont](https://mastodon.social/%40GossiTheDog%40cyberplace.social/109806939126836286) perfectly summarized it on Mastodon:

> "One lesson learned from this — some cloud providers that offer managed VMware hosting haven't been patching and leave all ports open to the internet on management IPs 🤦‍♀️"

To mitigate attacks, organizations running VMWare servers are advised to patch ESXi servers, move to a version not affected by the attacks (such as v8), or disable the OpenSLP service (*see instructions [here](https://kb.vmware.com/s/article/76372)*).

It is also not recommended paying the attackers. As security researcher [Soufiane Tahiri](https://archive.ph/MS5pE) spotted, the threat actor reused some Bitcoin addresses to collect ransoms, which could cause issues when proving payment and receiving/releasing the proper decryption key.

With this campaign having proved so successful for the attackers, it should be expected that other threat actors will also move in to exploit the same CVE-2021-21974 vulnerability soon. A public [proof-of-concept exploit](https://straightblast.medium.com/my-poc-walkthrough-for-cve-2021-21974-a266bcad14b9) has been available for this bug since March 2021, shortly after the bug was disclosed, so, honestly, we have no idea why companies haven't rushed to patch this back then. Some people like playing with fire, we guess!

### **Breaches and hacks**

**Orion Protocol crypto-heist:** DeFi trading platform Orion Protocol has lost ~$3 million worth of cryptocurrency assets after a hacker [exploited](https://blog.orionprotocol.io/strongfoundations) a re-entry attack vulnerability in one of its smart contracts last week. Following the hack, Orion Protocol CEO [Alexey Koloskov](https://archive.ph/pafCx) went online to reassure users that all their funds were safe. [*Press coverage in [Coindesk](https://www.coindesk.com/business/2023/02/02/orion-protocol-loses-3m-of-crypto-in-trading-pool-exploit/); technical analysis by [Numen Cyber Labs](https://mp.weixin.qq.com/s/CU1OgR9dTygUi_sQWiTliQ)*]

**Canceled surgeries:** The Tallahassee Memorial HealthCare (TMH) hospital says it was forced to cancel all non-emergency surgeries and other medical procedures following what officials described as an "[IT security issue](https://www.tmh.org/news/2023/tallahassee-memorial-managing-it-security-issue)" that crippled its computer systems on Thursday night last week. The hospital says that with the exception of Level 1 traumas and other life-threatening scenarios, it will also divert all incoming emergency patients to other nearby hospitals. The incident is believed to be yet another ransomware attack on US healthcare providers.

**988 cyberattack:** US federal officials say that a cyberattack has caused a nearly daylong outage to the nation's new 988 mental health helpline in an [incident](https://apnews.com/article/health-mental-service-outages-government-and-politics-d39ecadd27541c7c37c71caff95f975e) that took place on December 1, last year. The attack hit the network of Intrado, the company that provides telecommunications services for the helpline, a spokeswoman for the US Substance Abuse and Mental Health Services Administration [told the AP](https://apnews.com/article/technology-health-mental-76f75061bdc4ff3c4ec024f337e9a426) last week.

### **General tech and privacy**

**Microsoft MFA stats:** Microsoft says that [28% of its userbase](https://www.microsoft.com/en-us/security/blog/2023/01/26/2023-identity-security-trend...