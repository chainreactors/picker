---
title: Risky Biz News: Move aside RowHammer, the RowPress attack is here
url: https://riskybiznews.substack.com/p/risky-biz-news-move-aside-rowhammer
source: Over Security - Cybersecurity news aggregator
date: 2023-06-29
fetch_date: 2025-10-04T11:50:16.501053
---

# Risky Biz News: Move aside RowHammer, the RowPress attack is here

[![!!! Do not subscribe! We have moved!](https://substackcdn.com/image/fetch/$s_!dl-9!,w_80,h_80,c_fill,f_auto,q_auto:good,fl_progressive:steep,g_auto/https%3A%2F%2Fbucketeer-e05bbc84-baa3-437e-9518-adb32be77984.s3.amazonaws.com%2Fpublic%2Fimages%2F472a6618-0312-430d-8238-49e88cf01b91_1280x1280.png)](/)

# [!!! Do not subscribe! We have moved!](/)

SubscribeSign in

# Risky Biz News: Move aside RowHammer, the RowPress attack is here

### In other news: Volt Typhoon observed exploiting Zoho ManageEngine systems; Polish stalkerware company gets hacked; and encrypted messaging apps are often very confusing.

[![Catalin Cimpanu's avatar](https://substackcdn.com/image/fetch/$s_!nOnN!,w_36,h_36,c_fill,f_auto,q_auto:good,fl_progressive:steep/https%3A%2F%2Fbucketeer-e05bbc84-baa3-437e-9518-adb32be77984.s3.amazonaws.com%2Fpublic%2Fimages%2Fe393d520-317c-4283-bbb0-64aaaa65bf19_460x460.jpeg)](https://substack.com/%40campuscodi)

[Catalin Cimpanu](https://substack.com/%40campuscodi)

Jun 28, 2023

Share

***This newsletter is brought to you by application allowlisting software maker [Airlock Digital](https://www.airlockdigital.com/). You can subscribe to an audio version of this newsletter as a podcast by searching for "Risky Business News" in your podcatcher or subscribing via [this RSS feed](https://risky.biz/feeds/risky-business-news/). On Apple Podcasts:***

Back in 2014, a new attack named RowHammer upended the memory market and forced chip makers to rethink how they were manufacturing and what type of security features they were baking into DRAM chips.

The RowHammer attack—and all its variations—used super-fast read-write operations directed at a row of memory cells inside a DRAM chip to generate electrical disturbances that altered or corrupted data in nearby rows.

Throughout the years, chip vendors started placing memory rows at larger distances between each other and added software-level protections to detect when apps were accessing memory rows at super-high rates.

This would have been all fine and dandy, but in new research published earlier this month, a team of academics from Swiss university ETH Zurich has described an alternative to RowHammer—a new attack they named **RowPress**.

Unlike RowHammer, this attack works by accessing a row of memory cells and then just keeping it open for a long period of time.

[![](https://substackcdn.com/image/fetch/$s_!mrcw!,w_1456,c_limit,f_auto,q_auto:good,fl_progressive:steep/https%3A%2F%2Fsubstack-post-media.s3.amazonaws.com%2Fpublic%2Fimages%2Fe0f40561-1be9-41f9-9f4d-4807c939538d_965x473.png)](https://substackcdn.com/image/fetch/%24s_%21mrcw%21%2Cf_auto%2Cq_auto%3Agood%2Cfl_progressive%3Asteep/https%3A//substack-post-media.s3.amazonaws.com/public/images/e0f40561-1be9-41f9-9f4d-4807c939538d_965x473.png)

The research team says this is unnatural behavior for the memory cells, which end up causing bit-flips in nearby cells, just like in a classic RowHammer attack. There are also some extreme cases where bit-flips occur in a DRAM row just after one activation.

Because RowPress doesn't need to execute super-fast read-write operations, RowHammer software protections don't apply.

The attack also becomes more efficient as the chip's temperature increases.

Researchers say they tested the new RowPress attack with 164 DDR4 DRAM chips from all three major vendors—Samsung, SK Hynix, and Micron—and all were vulnerable.

Although the research sounds grim, the team says the attack can be easily mitigated at the software level by limiting the amount of time a memory row can stay open.

The full RowHammer paper is available here [*[PDF](https://people.inf.ethz.ch/omutlu/pub/RowPress_isca23.pdf)*], and the code to reproduce the attack is available on [GitHub](https://github.com/CMU-SAFARI/RowPress).

### **Breaches, hacks, and security incidents**

**Petro-Canada incident:** Canadian energy company [Suncor says](https://www.sec.gov/Archives/edgar/data/311337/000110465923074667/tm2318006d2_ex99-1.htm) a cyber-attack has hit the systems of its gas station chain Petro-Canada. The incident took place on Friday, June 25, and has impacted the company's website and mobile apps. It also impacted its payment systems, and customers have had to pay cash since the attack. The incident is suspected to be a ransomware attack. Suncor was ranked as the 48th-largest public company in the world in 2020. [*Additional coverage in [CBC](https://www.cbc.ca/news/business/petro-canada-suncor-cybersecurity-1.6888723)*]

**University of Hawaii ransomware attack:** The University of Hawaii has [confirmed](https://www.hawaii.edu/news/2023/06/20/uh-investigating-ransomware-incident/) that its Community College was the target of a ransomware attack.

**Medibank hack:** Australia's financial regulator [APRA has told](https://www.apra.gov.au/news-and-publications/apra-takes-action-against-medibank-private-relation-to-cyber-incident) private insurance provider Medibank to add an extra AUD$250 million (US$167 million) to its capital in the aftermath of the company's October 2022 security breach. The new capital will have to be established by July 1, 2023. It will serve as an operational risk charge and will have to remain in place until APRA deems Medibank has taken steps to strengthen its security environment and data management. The personal and healthcare data of more than 9.7 million Australians was stolen by the REvil ransomware group in an attack last year, marking one of the largest security breaches in Australia's history.

**Chibi Finance crypto-heist:** The operators of the Chibi Finance crypto platform appear to have deployed a malicious smart contract that stole more than $1 million worth of tokens from their users. Commonly referred to as a "rug pull," the incident led to the CHIBI token losing 98% of its value. According to *[CoinDesk](https://www.coindesk.com/tech/2023/06/27/chibi-finance-rug-pulls-users-for-1m-chibi-falls-98/)*, the stolen funds were quickly laundered over the weekend through several exchanges.

**LetMeSpy hack:** Polish stalkerware company LetMeSpy has been hacked, and its data published online. The company makes an Android app that can be side-loaded on modern smartphones and track calls, SMS messages, and the phone's location and movement. The incident exposed information on all LetMeSpy customers, such as names and email addresses. It also exposed data each customer had collected from infected devices. The contents of the dumped SMS messages reveals the typical spying in abusive relationships, but also drug trades and credentials for various online accounts. Based on the leaked data, the company had more than 26,000 paying customers. [*Additional coverage in [Niebezpiecznik](https://niebezpiecznik.pl/post/letmespy-android-wyciek-hacked/)/English coverage in [TechCrunch](https://techcrunch.com/2023/06/27/letmespy-hacked-spyware-thousands/)*]

**RFID scanners in Formula E:** The DS Penske Formula E team has been caught using an RFID scanner that grabbed live car and tire data from rival teams. The scanner was installed at the pitlane entry during a free practice session ahead of the Portland E-Prix that took place over the weekend. The team was fined €25,000—a record for the Formula E championship. Its two pilots were also forced to start from the pitlane in for the race. RFID scanners are commonly used in stores and other industries but are considered illegal in modern motor racing, where usage of such devices is considered cheating and hacking. [*Additional coverage in [The Race](https://the-race.com/formula-e/ds-penske-gets-record-formula-e-punishment-for-pitlane-scanner/)*]

**MOVEit hacks:** The victim count has now gone over 100 with the addition of Siemens Energy, Schneider Electric, Calpers, Genworth, and UCLA.

### **General tech and privacy**

**Passkeys support in Windows 11:** Microsoft is working on [adding a new section](https://blogs.windows.com/windows-insider/2023/06/22/announcing-windows-11-insider-pre...