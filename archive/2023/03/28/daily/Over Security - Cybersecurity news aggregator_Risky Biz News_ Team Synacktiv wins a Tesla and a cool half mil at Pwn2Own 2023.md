---
title: Risky Biz News: Team Synacktiv wins a Tesla and a cool half mil at Pwn2Own 2023
url: https://riskybiznews.substack.com/p/risky-biz-news-team-synacktiv-wins
source: Over Security - Cybersecurity news aggregator
date: 2023-03-28
fetch_date: 2025-10-04T10:54:59.207846
---

# Risky Biz News: Team Synacktiv wins a Tesla and a cool half mil at Pwn2Own 2023

[![!!! Do not subscribe! We have moved!](https://substackcdn.com/image/fetch/$s_!dl-9!,w_80,h_80,c_fill,f_auto,q_auto:good,fl_progressive:steep,g_auto/https%3A%2F%2Fbucketeer-e05bbc84-baa3-437e-9518-adb32be77984.s3.amazonaws.com%2Fpublic%2Fimages%2F472a6618-0312-430d-8238-49e88cf01b91_1280x1280.png)](/)

# [!!! Do not subscribe! We have moved!](/)

SubscribeSign in

# Risky Biz News: Team Synacktiv wins a Tesla and a cool half mil at Pwn2Own 2023

### In other news: CISA rolls out pre-ransomware notification system; NCA runs fake DDoS-for-hire websites; GitHub leaks private RSA key.

[![Catalin Cimpanu's avatar](https://substackcdn.com/image/fetch/$s_!nOnN!,w_36,h_36,c_fill,f_auto,q_auto:good,fl_progressive:steep/https%3A%2F%2Fbucketeer-e05bbc84-baa3-437e-9518-adb32be77984.s3.amazonaws.com%2Fpublic%2Fimages%2Fe393d520-317c-4283-bbb0-64aaaa65bf19_460x460.jpeg)](https://substack.com/%40campuscodi)

[Catalin Cimpanu](https://substack.com/%40campuscodi)

Mar 27, 2023

Share

***This newsletter is brought to you by [Airlock Digital](https://www.airlockdigital.com/), [Proofpoint](https://www.proofpoint.com/), [runZero](https://www.runzero.com/), and [Thinkst Canary](https://canary.tools/). You can subscribe to an audio version of this newsletter as a podcast by searching for "Risky Business News" in your podcatcher or subscribing via [this RSS feed](https://risky.biz/feeds/risky-business-news/).***

French cybersecurity firm [Synacktiv](https://www.synacktiv.com/) has won this year's Pwn2Own hacking contest after dominating the competition with six successful exploits that brought its researchers a cool half mil ($530,000), the biggest award ever raked in by one contestant in Pwn2Own's history.

There are three Pwn2Own hacking contests that take place during a year: one dedicated to smartphones and IoT devices, one dedicated to industrial equipment, and one dedicated to desktops, servers, and smart cars.

Synacktiv won the latter—considered the most prestigious of all hacking contests today. This year's edition took place during the CanSecWest security conference, which wrapped up on Friday last week.

This marks the second time Synacktiv has won Pwn2Own after it also won the [2021 edition](https://archive.ph/dQEhi) as well.

During this year's three-day contest [[1](https://www.zerodayinitiative.com/blog/2023/3/22/pwn2own-vancouver-2023-day-one-results), [2](https://www.zerodayinitiative.com/blog/2023/3/23/pwn2own-vancouver-2023-day-two-results), [3](https://www.zerodayinitiative.com/blog/2023/3/24/pwn2own-vancouver-2023-day)], Synacktiv brought down some notable targets:

* **$250,000** - heap overflow and an OOB write to exploit a **Tesla Model 3**'s infotainment system for unconfined root access
* **$100,000** - TOCTOU attack against a **Tesla Model 3**
* **$80,000** - three-bug chain against **Oracle VirtualBox** with a Host EoP
* **$40,000** - TOCTOU bug to escalate privileges on **Apple macOS**
* **$30,000** - incorrect pointer scaling leading to privilege escalation on **Ubuntu Desktop**
* **$30,000**- UAF against **Microsoft Windows 11**

[![](https://substackcdn.com/image/fetch/$s_!7Q5X!,w_1456,c_limit,f_auto,q_auto:good,fl_progressive:steep/https%3A%2F%2Fsubstack-post-media.s3.amazonaws.com%2Fpublic%2Fimages%2Ff1405479-eed1-47db-9092-82a7751e3e11_750x423.png)](https://substackcdn.com/image/fetch/%24s_%217Q5X%21%2Cf_auto%2Cq_auto%3Agood%2Cfl_progressive%3Asteep/https%3A//substack-post-media.s3.amazonaws.com/public/images/f1405479-eed1-47db-9092-82a7751e3e11_750x423.png)

Synacktiv's team members for this year's contest included Eloi Benoist-Vanderbeken, David Berard, Vincent Dehors, Tanguy Dubroca, Thomas Bouzerar, and Thomas Imbert.

Besides the $530,000 and the Master of Pwn trophy, Synacktiv will also receive a Tesla Model 3 car—as part of an agreement between the contest organizers (the Zero-Day Initiative) and Tesla.

All in all, Synacktiv went home with more than half of the prizes awarded at Pwn2Own this year—$1,035,000 and a car.

### **Breaches and hacks**

**Euler hacker returns funds:** The hacker who stole $197 million worth of cryptocurrency from the Euler Finance platform has returned more than half to the beleaguered company. More than $107 million have been returned so far across three separate transactions. The returns come following negotiations between the two sides. [*Press coverage in [The Block](https://www.theblock.co/post/222810/euler-hacker-returns-51000-ether-worth-about-89-million)*]

**GitHub private key leak:** Code-hosting repository GitHub has rotated its RSA private key that the company uses to secure Git operations sent over SSH on the GitHub.com domain. [GitHub says](https://github.blog/2023-03-23-we-updated-our-rsa-ssh-host-key/) it rotated the key after it was accidentally exposed in a public repository earlier in the week. The change does not affect browser traffic to the GitHub website nor Git operations performed on GitHub via HTTPS. Affected users will get a warning in their SSH interface (see below).

[![](https://substackcdn.com/image/fetch/$s_!UjpS!,w_1456,c_limit,f_auto,q_auto:good,fl_progressive:steep/https%3A%2F%2Fsubstack-post-media.s3.amazonaws.com%2Fpublic%2Fimages%2Fe29b90bd-5adb-41d7-8a2a-2fa193532ebf_688x264.png)](https://substackcdn.com/image/fetch/%24s_%21UjpS%21%2Cf_auto%2Cq_auto%3Agood%2Cfl_progressive%3Asteep/https%3A//substack-post-media.s3.amazonaws.com/public/images/e29b90bd-5adb-41d7-8a2a-2fa193532ebf_688x264.png)

### **General tech and privacy**

**Microsoft to block emails from outdated Exchange servers:** Microsoft plans to block emails on its Exchange Online infrastructure that are coming from on-premise Exchange email servers running outdated software. The block will not be enforced right away. Microsoft says it plans to notify Exchange server owners about their insecure server and gradually throttle email traffic from unpatched servers. If servers aren't patched after 90 days, Microsoft says it will block traffic from outdated servers. Microsoft says that once servers are patched, any throttling or block will be lifted immediately. The block is part of a new security feature named [Transport-based Enforcement System](https://techcommunity.microsoft.com/t5/exchange-team-blog/throttling-and-blocking-email-from-persistently-vulnerable/ba-p/3762078) and will apply to all on-premise Exchange servers that have formally reached end-of-life. The list includes Exchange 2007, Exchange 2010, and soon, Exchange 2013.

[![](https://substackcdn.com/image/fetch/$s_!ioMA!,w_1456,c_limit,f_auto,q_auto:good,fl_progressive:steep/https%3A%2F%2Fsubstack-post-media.s3.amazonaws.com%2Fpublic%2Fimages%2F66ec1392-4059-4f2c-89a3-4eaf06a315d6_999x502.jpeg)](https://substackcdn.com/image/fetch/%24s_%21ioMA%21%2Cf_auto%2Cq_auto%3Agood%2Cfl_progressive%3Asteep/https%3A//substack-post-media.s3.amazonaws.com/public/images/66ec1392-4059-4f2c-89a3-4eaf06a315d6_999x502.jpeg)

### **Government, politics, and policy**

**Dutch intelligence overview report:** TIB, a committee that supervises the use of telecommunications interception powers by Dutch intelligence services, has published its [yearly report](https://www.tib-ivd.nl/actueel/nieuws/2023/03/24/jaarverslag-tib-2022) for 2022. TIB says that last year, Dutch intelligence services AIVD and MIVD used their hacking capabilities exclusively on "strategic grounds." The report noted that while, in some cases, the intelligence services started operations before the TIB approval—a breach of protocol—the operations themselves were not illegal. TIB officials were [annoyed](https://archive.ph/Pnvga) they had to redact some parts of their report, though.

**UA mandatory security audits:** The Ukrainian government [approved](https://cip.gov.ua/en/news/kabmin-ukhvaliv-postanovu-yaka-unormovuye-vprovadzhennya-nezalezhnogo-auditu-sistem-informaciinoyi-bezpeki-na-ob-yektakh-kritichnoyi-infrastrukturi) a resolution requiring mandatory security audits at critical infrastructur...