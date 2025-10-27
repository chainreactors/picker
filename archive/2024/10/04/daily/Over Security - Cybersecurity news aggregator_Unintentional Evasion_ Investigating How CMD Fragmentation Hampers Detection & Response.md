---
title: Unintentional Evasion: Investigating How CMD Fragmentation Hampers Detection & Response
url: https://kostas-ts.medium.com/unintentional-evasion-investigating-how-cmd-fragmentation-hampers-detection-response-e5d7b465758e
source: Over Security - Cybersecurity news aggregator
date: 2024-10-04
fetch_date: 2025-10-06T18:52:01.748340
---

# Unintentional Evasion: Investigating How CMD Fragmentation Hampers Detection & Response

[Sitemap](/sitemap/sitemap.xml)

[Open in app](https://rsci.app.link/?%24canonical_url=https%3A%2F%2Fmedium.com%2Fp%2Fe5d7b465758e&%7Efeature=LoOpenInAppButton&%7Echannel=ShowPostUnderCollection&%7Estage=mobileNavBar&source=post_page---top_nav_layout_nav-----------------------------------------)

Sign up

[Sign in](https://medium.com/m/signin?operation=login&redirect=https%3A%2F%2Fdetect.fyi%2Funintentional-evasion-investigating-how-cmd-fragmentation-hampers-detection-response-e5d7b465758e&source=post_page---top_nav_layout_nav-----------------------global_nav------------------)

[Medium Logo](https://medium.com/?source=post_page---top_nav_layout_nav-----------------------------------------)

[Write](https://medium.com/m/signin?operation=register&redirect=https%3A%2F%2Fmedium.com%2Fnew-story&source=---top_nav_layout_nav-----------------------new_post_topnav------------------)

[Search](https://medium.com/search?source=post_page---top_nav_layout_nav-----------------------------------------)

Sign up

[Sign in](https://medium.com/m/signin?operation=login&redirect=https%3A%2F%2Fdetect.fyi%2Funintentional-evasion-investigating-how-cmd-fragmentation-hampers-detection-response-e5d7b465758e&source=post_page---top_nav_layout_nav-----------------------global_nav------------------)

![](https://miro.medium.com/v2/resize:fill:64:64/1*dmbNkD5D-u45r44go_cf0g.png)

[## Detect FYI](https://detect.fyi/?source=post_page---publication_nav-d5fd8f494f6a-e5d7b465758e---------------------------------------)

·

Follow publication

[![Detect FYI](https://miro.medium.com/v2/resize:fill:76:76/1*ayMhoNccbO0IxQ1UPFv0SA.png)](https://detect.fyi/?source=post_page---post_publication_sidebar-d5fd8f494f6a-e5d7b465758e---------------------------------------)

Threat Detection Engineering and DFIR Insights

Follow publication

Member-only story

# Unintentional Evasion: Investigating Command Line Logging Gaps

## How CMD Fragmentation Hampers Detection & Response

[![Kostas](https://miro.medium.com/v2/resize:fill:64:64/1*BtTfw89t0Sfap1SKrF3hvA.jpeg)](https://kostas-ts.medium.com/?source=post_page---byline--e5d7b465758e---------------------------------------)

[Kostas](https://kostas-ts.medium.com/?source=post_page---byline--e5d7b465758e---------------------------------------)

7 min read

·

Oct 3, 2024

--

Share

In a recent investigation, I came across a subtle yet significant issue that can hinder forensic analysis and threat detection: command line omission and fragmentation in Windows process execution logs. This isn’t my first time encountering such nuances, so I felt it was worth sharing my insights through this article.

While examining commands executed by a threat actor who had gained GUI interactive access to compromised hosts, I noticed that many commands were either fragmented or missing entirely from the logs. This was especially apparent when the attacker used built-in commands in conjunction with special characters.

Attackers often use RMM software to access the victims’ hosts, enabling them to create interactive sessions and run commands directly through CMD. This can significantly affect command logging — or the absence of logs altogether — due to command line omission and fragmentation.

Understanding how special characters and built-in commands affect logging is important for threat detection and intrusion analysis. In this post, I will discuss the issues with command line fragmentation and how it can lead to the loss of critical data in investigations.

Press enter or click to view image in full size

![]()

--

--

[![Detect FYI](https://miro.medium.com/v2/resize:fill:96:96/1*ayMhoNccbO0IxQ1UPFv0SA.png)](https://detect.fyi/?source=post_page---post_publication_info--e5d7b465758e---------------------------------------)

[![Detect FYI](https://miro.medium.com/v2/resize:fill:128:128/1*ayMhoNccbO0IxQ1UPFv0SA.png)](https://detect.fyi/?source=post_page---post_publication_info--e5d7b465758e---------------------------------------)

Follow

[## Published in Detect FYI](https://detect.fyi/?source=post_page---post_publication_info--e5d7b465758e---------------------------------------)

[2.1K followers](/followers?source=post_page---post_publication_info--e5d7b465758e---------------------------------------)

·[Last published 3 days ago](/the-missing-link-in-mdr-spoiler-it-starts-with-a-detection-engineering-framework-5f836347c92f?source=post_page---post_publication_info--e5d7b465758e---------------------------------------)

Threat Detection Engineering and DFIR Insights

Follow

[![Kostas](https://miro.medium.com/v2/resize:fill:96:96/1*BtTfw89t0Sfap1SKrF3hvA.jpeg)](https://kostas-ts.medium.com/?source=post_page---post_author_info--e5d7b465758e---------------------------------------)

[![Kostas](https://miro.medium.com/v2/resize:fill:128:128/1*BtTfw89t0Sfap1SKrF3hvA.jpeg)](https://kostas-ts.medium.com/?source=post_page---post_author_info--e5d7b465758e---------------------------------------)

[## Written by Kostas](https://kostas-ts.medium.com/?source=post_page---post_author_info--e5d7b465758e---------------------------------------)

[1.2K followers](https://kostas-ts.medium.com/followers?source=post_page---post_author_info--e5d7b465758e---------------------------------------)

·[21 following](https://medium.com/%40kostas-ts/following?source=post_page---post_author_info--e5d7b465758e---------------------------------------)

I am a security researcher. My interests lie in #ThreatIntel, #malware, #IR & #Threat\_Hunting. I either post here or at <http://thedfirreport.com/>

## No responses yet

[Help](https://help.medium.com/hc/en-us?source=post_page-----e5d7b465758e---------------------------------------)

[Status](https://status.medium.com/?source=post_page-----e5d7b465758e---------------------------------------)

[About](https://medium.com/about?autoplay=1&source=post_page-----e5d7b465758e---------------------------------------)

[Careers](https://medium.com/jobs-at-medium/work-at-medium-959d1a85284e?source=post_page-----e5d7b465758e---------------------------------------)

Press

[Blog](https://blog.medium.com/?source=post_page-----e5d7b465758e---------------------------------------)

[Privacy](https://policy.medium.com/medium-privacy-policy-f03bf92035c9?source=post_page-----e5d7b465758e---------------------------------------)

[Rules](https://policy.medium.com/medium-rules-30e5502c4eb4?source=post_page-----e5d7b465758e---------------------------------------)

[Terms](https://policy.medium.com/medium-terms-of-service-9db0094a1e0f?source=post_page-----e5d7b465758e---------------------------------------)

[Text to speech](https://speechify.com/medium?source=post_page-----e5d7b465758e---------------------------------------)