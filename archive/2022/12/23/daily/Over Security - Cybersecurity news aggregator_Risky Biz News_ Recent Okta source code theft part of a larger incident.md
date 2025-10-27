---
title: Risky Biz News: Recent Okta source code theft part of a larger incident
url: https://riskybiznews.substack.com/p/risky-biz-news-recent-okta-source
source: Over Security - Cybersecurity news aggregator
date: 2022-12-23
fetch_date: 2025-10-04T02:21:57.997516
---

# Risky Biz News: Recent Okta source code theft part of a larger incident

[![!!! Do not subscribe! We have moved!](https://substackcdn.com/image/fetch/$s_!dl-9!,w_80,h_80,c_fill,f_auto,q_auto:good,fl_progressive:steep,g_auto/https%3A%2F%2Fbucketeer-e05bbc84-baa3-437e-9518-adb32be77984.s3.amazonaws.com%2Fpublic%2Fimages%2F472a6618-0312-430d-8238-49e88cf01b91_1280x1280.png)](/)

# [!!! Do not subscribe! We have moved!](/)

SubscribeSign in

# Risky Biz News: Recent Okta source code theft part of a larger incident

### In other news: Smart home wall pad hacker detained in South Korea; The Guardian newspaper hit by ransomware; E2EE coming to enterprise Gmail.

[![Catalin Cimpanu's avatar](https://substackcdn.com/image/fetch/$s_!nOnN!,w_36,h_36,c_fill,f_auto,q_auto:good,fl_progressive:steep/https%3A%2F%2Fbucketeer-e05bbc84-baa3-437e-9518-adb32be77984.s3.amazonaws.com%2Fpublic%2Fimages%2Fe393d520-317c-4283-bbb0-64aaaa65bf19_460x460.jpeg)](https://substack.com/%40campuscodi)

[Catalin Cimpanu](https://substack.com/%40campuscodi)

Dec 22, 2022

Share

***This newsletter is brought to you by [Airlock Digital](https://www.airlockdigital.com/), [Proofpoint](https://www.proofpoint.com/), [runZero](https://www.runzero.com/), and [Thinkst Canary](https://canary.tools/). You can subscribe to an audio version of this newsletter as a podcast by searching for "Risky Business News" in your podcatcher or subscribing via [this RSS feed](https://risky.biz/feeds/risky-business-news/).***

The Risky Business team is still on its December holiday break, but we thought to put out this weekly edition with some of the past week's biggest infosec stories.

Happy holidays!

### Breaches and hacks

**The Guardian ransomware attack:** Some parts of The Guardian's IT infrastructure went down this week, with the paper tentatively calling the incident [a ransomware attack](https://www.theguardian.com/media/2022/dec/21/guardian-hit-by-serious-it-incident-believed-to-be-ransomware-attack). The UK news org has told staff to work from home until it sorts things out. The incident appears to have impacted their entire data center network, [per researchers](https://mastodon.social/%40GossiTheDog%40cyberplace.social/109551855895723300).

**Raydium cyber-heist:** Solana-based DeFi platform Raydium was hacked for $5.5 million. [According to CertiK](https://twitter.com/CertiKAlert/status/1603877927078313984), "the attack appears to be the result of a trojan attack & private key compromise."

**Nio extortion:** Chinese EV maker Nio said it was being [blackmailed](https://ir.nio.com/news-events/news-releases/news-release-details/nio-inc-promptly-responds-data-leakage/) by hackers. According to [Bloomberg](https://www.bnnbloomberg.ca/nio-blackmailed-for-millions-in-bitcoin-by-data-stealing-hackers-1.1861672), hackers are asking $2.25 million in Bitcoin from the company to not leak sensitive information they stole from the company in August 2021. Nio said this data contains "information of users and vehicle sales in China before August 2021."

**Thyssenkrupp hacked again:** German industrial engineering and steel production giant Thyssenkrupp has [confirmed](https://www.securityweek.com/industrial-giant-thyssenkrupp-again-targeted-cybercriminals) that it was the victim of a new cybersecurity breach. The company was previously the victim of several ransomware attacks, and even APT intrusions.

**GitHub/Heroku/TravisCI security incident:** [Okta told customers](https://www.bleepingcomputer.com/news/security/oktas-source-code-stolen-after-github-repositories-hacked/) that a threat actor gained access to its GitHub repositories and stole some of its source code. *RiskyBizNews*understands this incident is actually part of a larger set of GitHub account intrusions that took place earlier in December. At the time, threat actors used [Heroku](https://mastodon.social/%40kurtseifried/109474509351487448) and [TravisCI](https://twitter.com/guewenb/status/1600751900114100225) [integrations](https://twitter.com/peter_szilagyi/status/1600591604280360961) to access GitHub accounts in an incident similar to one that happened earlier in the year, [in April](https://github.blog/2022-04-15-security-alert-stolen-oauth-user-tokens/). GitHub has not returned a request for comment.

[![](https://substackcdn.com/image/fetch/$s_!0h_I!,w_1456,c_limit,f_auto,q_auto:good,fl_progressive:steep/https%3A%2F%2Fbucketeer-e05bbc84-baa3-437e-9518-adb32be77984.s3.amazonaws.com%2Fpublic%2Fimages%2Fcc22f267-e23b-4d6c-9259-874f75b0c689_590x484.png)](https://substackcdn.com/image/fetch/%24s_%210h_I%21%2Cf_auto%2Cq_auto%3Agood%2Cfl_progressive%3Asteep/https%3A//bucketeer-e05bbc84-baa3-437e-9518-adb32be77984.s3.amazonaws.com/public/images/cc22f267-e23b-4d6c-9259-874f75b0c689_590x484.png)

### General tech and privacy

**Client-side encryption for Gmail:** Google is [adding E2EE support](https://workspaceupdates.googleblog.com/2022/12/client-side-encryption-for-gmail-beta.html) for Gmail's web client. The feature is currently available for Google Workspace users via a beta program. Users allowed in the beta trial will be able to send and receive encrypted emails within and outside their email domain. It's unclear when this will become available for regular Gmail personal accounts.

**IE update:** Microsoft says that an Edge browser update that will be released on February 14, 2023, will [permanently disable Internet Explorer](https://learn.microsoft.com/en-us/deployedge/edge-ie-disable-ie11) 11 on Windows 10. Talk about the perfect Valentine's Day gift! Lovely!

**Epic Games settlement:** The US FTC has settled with Epic Games, and the gaming company has agreed to pay [a $520 million fine](https://www.ftc.gov/news-events/news/press-releases/2022/12/fortnite-video-game-maker-epic-games-pay-more-half-billion-dollars-over-ftc-allegations) in two lawsuits that accused the company of (1) breaching COPPA and collecting data on small children, (2) and employing dark patterns to trick customers into making unintentional purchases.

**Mozilla to launch Mastodon instance:** The Mozilla Foundation [announced](https://blog.mozilla.org/en/mozilla/mozilla-launch-fediverse-instance-social-media-alternative/) plans to launch its own Mastodon server instance next year in early 2023.

**Mastodon job:** Joyent and Mozilla technologist Mark Mayo [wants to hire](https://mastodon.social/%40mmayo%40hachyderm.io/109530486547174648) a developer for the next three months to improve the authentication mechanism used by the Mastodon open-source project.

**Twitter dumb stuff:** Right-wing QAnon-friendly social network Twitter (yeah, I said it) has [removed the feature](https://twitter.com/PubityIG/status/1604200614711287808) that lets you see the source of a tweet. Famous hardware hacker George Hotz has also [quit the company](https://twitter.com/goldman/status/1605348785898811392) after realizing he won't be able to improve the company's search feature, something he bragged about last month. Journalists who have been suspended last week have had accounts reinstated, however, they said they have [not been granted access](https://www.techmeme.com/221220/p41#a221220p41) to their Twitter profiles, with the company imposing the condition that they deleted tweets commenting or correcting Musk. In addition, Musk's fake journalists have also published part 7 of the Twitter Files "revelations," where they claim the FBI was paying Twitter to censor content. Alex Stamos, the former Facebook CISO, has corrected their absolutely unprofessional and skewed reporting on the topic in this [Mastodon thread](https://cybervillains.com/%40alex/109547284671459064). Also, over the weekend, Twitter banned links to any other social network ([except the right-wing ones](https://twitter.com/MeanwhileinCana/status/1604553729029586944)) and then changed their mind when they realized they could face some serious antitrust investigations. [*We’ve removed an entry about Musk’s stalker from this section since we misunderstood the reporting. Apologies for the error!*]

### ...