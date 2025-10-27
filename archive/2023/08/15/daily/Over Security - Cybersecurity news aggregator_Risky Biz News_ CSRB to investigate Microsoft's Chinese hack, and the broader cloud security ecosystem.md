---
title: Risky Biz News: CSRB to investigate Microsoft's Chinese hack, and the broader cloud security ecosystem
url: https://riskybiznews.substack.com/p/csrb-to-investigate-microsoft-hack
source: Over Security - Cybersecurity news aggregator
date: 2023-08-15
fetch_date: 2025-10-04T12:03:25.780667
---

# Risky Biz News: CSRB to investigate Microsoft's Chinese hack, and the broader cloud security ecosystem

[![!!! Do not subscribe! We have moved!](https://substackcdn.com/image/fetch/$s_!dl-9!,w_80,h_80,c_fill,f_auto,q_auto:good,fl_progressive:steep,g_auto/https%3A%2F%2Fbucketeer-e05bbc84-baa3-437e-9518-adb32be77984.s3.amazonaws.com%2Fpublic%2Fimages%2F472a6618-0312-430d-8238-49e88cf01b91_1280x1280.png)](/)

# [!!! Do not subscribe! We have moved!](/)

SubscribeSign in

# Risky Biz News: CSRB to investigate Microsoft's Chinese hack, and the broader cloud security ecosystem

### In other news: UK Foreign Office hacked twice in 2021; Japan to build Indo-Pacific cyberdefense network; and Zyxel routers under attack.

[![Catalin Cimpanu's avatar](https://substackcdn.com/image/fetch/$s_!nOnN!,w_36,h_36,c_fill,f_auto,q_auto:good,fl_progressive:steep/https%3A%2F%2Fbucketeer-e05bbc84-baa3-437e-9518-adb32be77984.s3.amazonaws.com%2Fpublic%2Fimages%2Fe393d520-317c-4283-bbb0-64aaaa65bf19_460x460.jpeg)](https://substack.com/%40campuscodi)

[Catalin Cimpanu](https://substack.com/%40campuscodi)

Aug 14, 2023

Share

***This newsletter is brought to you by [Thinkst](https://thinkst.com/), the makers of the much-loved [Thinkst Canary](https://canary.tools/). You can subscribe to an audio version of this newsletter as a podcast by searching for "Risky Business News" in your podcatcher or subscribing via [this RSS feed](https://risky.biz/feeds/risky-business-news/). On Apple Podcasts:***

The DHS Cyber Safety Review Board (CSRB) has picked up the unenviable task of investigating the security practices of US cloud service providers and plans to use the [recent breach](https://www.microsoft.com/en-us/security/blog/2023/07/14/analysis-of-storm-0558-techniques-for-unauthorized-email-access/) of Microsoft email systems as the figurehead of an upcoming report.

The CSRB may have couched its [press release](https://www.dhs.gov/news/2023/08/11/department-homeland-securitys-cyber-safety-review-board-conduct-review-cloud) as a generic investigation of cloud security providers, but it is, without a doubt, an investigation into Microsoft's carelessness when it comes to its cloud infrastructure, which underpins a vast section of the US government's IT systems.

The CSRB investigation was announced two weeks after Sen. Ron Wyden [asked](https://www.wyden.senate.gov/news/press-releases/wyden-requests-federal-agencies-investigate-lax-cybersecurity-practices-by-microsoft-that-reportedly-enabled-chinese-espionage) the DHS—together with the FTC and DOJ—to investigate Microsoft's "lax cybersecurity practices" that led to the breach in the first place.

Of the three agencies that Wyden asked, the CSRB is the one with fewer teeth and the one whose investigation might give Microsoft a slap on the cheek but then allow the US government to kiss the boo-boo later without having to impose any heavy fines.

[Established](https://www.whitehouse.gov/briefing-room/presidential-actions/2021/05/12/executive-order-on-improving-the-nations-cybersecurity/) by the White House in 2021, the [CSRB](https://www.cisa.gov/resources-tools/groups/cyber-safety-review-board-csrb) is tasked with reviewing major cybersecurity incidents impacting the US. It has no subpoena powers, and its investigations are completely at the mercy of the cooperation they get from other government agencies and private sector companies—which was [painfully obvious](https://mastodon.social/%40arekfurt%40infosec.exchange/110870927757718138) in its recent Lapsus$ report. A [bill](https://therecord.media/csrb-legislation-congress-white-house-rob-silvers-rsac) is currently in the works to grant the CSRB subpoena powers, but the bill has not passed yet.

So far, the CSRB has investigated just two incidents and issued two reports—on the [Log4Shell](https://www.cisa.gov/resources-tools/resources/csrb-review-december-2021-log4j-event) vulnerability and the operations of the [Lapsus$](https://www.cisa.gov/resources-tools/resources/review-attacks-associated-lapsus-and-related-threat-groups-report) APT, where APT stands for advanced persistent teens.

This is the first time the CSRB will be investigating an entity that can fight back in meetings and has more lobbyists than the board has members.

About the only thing the board has going is that Microsoft knows it has egg on its face. Its Exchange servers were widely hacked across the world with the [ProxyShell](https://en.wikipedia.org/wiki/2021_Microsoft_Exchange_Server_data_breach) vulnerability in 2021, the company got not [one](https://www.linkedin.com/pulse/microsofts-vulnerability-practices-put-customers-risk-amit-yoran/) but [two](https://www.linkedin.com/pulse/microsoftthe-truth-even-worse-than-you-think-amit-yoran/) public tongue-lashings from the Tenable CEO for basically ignoring major Azure vulnerabilities, and then the [Storm-0558](https://www.microsoft.com/en-us/security/blog/2023/07/14/analysis-of-storm-0558-techniques-for-unauthorized-email-access/) hacks happened in July.

These latter intrusions were particularly bad for Microsoft. Not only did Chinese hackers access the email systems of at least four US government agencies, but the technical details of how they did it squarely point the finger at Microsoft's negligence. My colleague Tom Uren went over all of these technical slip-ups in his [newsletter](https://srslyriskybiz.substack.com/p/on-microsoft-wydens-bark-may-have) two weeks ago, right after Sen. Wyden asked for a CSRB review.

He pointed out back then that a "*CSRB review might not result in many new specific technical recommendations"* since Microsoft was clearly breaking many basic rules when it came to the storage of privileged access skeleton keys and the separation of internal services and systems.

As Tom, Tenable CEO Amit Yoran, and many other infosec and gov-tech experts have pointed out is that "***Microsoft isn't prioritising security as much as it should***."

By couching its report as a general review of cybersecurity practices of cloud service providers, we hope the board will establish an unofficial set of rules and requirements that cloud providers will have to adhere to, if they hope to serve secure government systems going forward.

The CSRB's latest report on the Lapsus$ operations clearly showed that US telcos run on extremely insecure infrastructure and that tech companies, even if they use them, they often fail to properly configure their Identity Access Management (IAM) and Multi-Factor Authentication (MFA) solutions.

Believe it or not, the CSRB Lapsus$ report, which is a bore for incident responders—because they know all of Lapsus$'s shenanigans by now— is a gold mine for defenders and CISOs, who now have a set of recommendations and examples on how to use or not-use your IAM/MFA. There is something to learn from reading all of it.

But if you're using some of today's biggest cybersecurity experts and policymakers to issue recommendations and best practices, then what's the point of NIST and standards bodies?

There's a reason why the DHS is looking for subpoena powers for the CSRB. How Microsoft responds to this investigation will most likely determine if the CSRB project implodes or if Congress sees the issue and grants it the legal power it needs to become the cyber NTSB [the DHS wants](https://www.dhs.gov/news/2023/04/24/statement-secretary-mayorkas-cyber-safety-review-boards-review-inaugural) to make into so much.

I'll just end this newsletter with a [Mastodon post](https://mastodon.social/%40arekfurt%40infosec.exchange/110871358996858471) from an infosec commentator whose opinion I always treasure and find extremely to the point.

> "Anyway, it seems likely to be make or break for what remains of CSRB's credibility in policy circles. It may not want to act as a kind Cyber NTSB, but that's exactly what the situation calls for and that's basically what people are going to expect."

[![](https://substackcdn.com/image/fetch/$s_!tpq-!,w_1456,c_limit,f_auto,q_auto:good,fl_progressive:steep/https%3A%2F%2Fsubstack-post-media.s3.amazonaws.com%2Fpublic%...