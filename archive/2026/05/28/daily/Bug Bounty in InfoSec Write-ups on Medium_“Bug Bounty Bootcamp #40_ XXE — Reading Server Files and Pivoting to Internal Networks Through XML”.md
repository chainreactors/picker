---
title: “Bug Bounty Bootcamp #40: XXE — Reading Server Files and Pivoting to Internal Networks Through XML”
url: https://infosecwriteups.com/bug-bounty-bootcamp-40-xxe-reading-server-files-and-pivoting-to-internal-networks-through-xml-17708cf6029b?source=rss----7b722bfd1b8d--bug_bounty
source: Bug Bounty in InfoSec Write-ups on Medium
date: 2026-05-28
fetch_date: 2026-05-29T06:04:50.244885
---

# “Bug Bounty Bootcamp #40: XXE — Reading Server Files and Pivoting to Internal Networks Through XML”

[Sitemap](/sitemap/sitemap.xml)

[Open in app](https://play.google.com/store/apps/details?id=com.medium.reader&referrer=utm_source%3DmobileNavBar&source=post_page---top_nav_layout_nav-----------------------------------------)

Sign up

[Sign in](https://medium.com/m/signin?operation=login&redirect=https%3A%2F%2Finfosecwriteups.com%2Fbug-bounty-bootcamp-40-xxe-reading-server-files-and-pivoting-to-internal-networks-through-xml-17708cf6029b&source=post_page---top_nav_layout_nav-----------------------global_nav------------------)

[Medium Logo](https://medium.com/?source=post_page---top_nav_layout_nav-----------------------------------------)

Get app

[Write](https://medium.com/m/signin?operation=register&redirect=https%3A%2F%2Fmedium.com%2Fnew-story&source=---top_nav_layout_nav-----------------------new_post_topnav------------------)

[Search](https://medium.com/search?source=post_page---top_nav_layout_nav-----------------------------------------)

Sign up

[Sign in](https://medium.com/m/signin?operation=login&redirect=https%3A%2F%2Finfosecwriteups.com%2Fbug-bounty-bootcamp-40-xxe-reading-server-files-and-pivoting-to-internal-networks-through-xml-17708cf6029b&source=post_page---top_nav_layout_nav-----------------------global_nav------------------)

![Unknown user](https://miro.medium.com/v2/resize:fill:64:64/1*dmbNkD5D-u45r44go_cf0g.png)

[## InfoSec Write-ups](https://infosecwriteups.com/?source=post_page---publication_nav-7b722bfd1b8d-17708cf6029b---------------------------------------)

·

[![InfoSec Write-ups](https://miro.medium.com/v2/resize:fill:76:76/1*SWJxYWGZzgmBP1D0Qg_3zQ.png)](https://infosecwriteups.com/?source=post_page---post_publication_sidebar-7b722bfd1b8d-17708cf6029b---------------------------------------)

A collection of write-ups from the best hackers in the world on topics ranging from bug bounties and CTFs to vulnhub machines, hardware challenges and real life encounters. Subscribe to our weekly newsletter for the coolest infosec updates: <https://weekly.infosecwriteups.com/>

Member-only story

# “Bug Bounty Bootcamp #40: XXE — Reading Server Files and Pivoting to Internal Networks Through XML”

## That innocent XML import feature could be a direct line to your `/etc/passwd` and internal cloud metadata. Learn to spot XML parsing vulnerabilities and weaponize external entities for file disclosure and SSRF.

[![Aman Sharma](https://miro.medium.com/v2/da:true/resize:fill:64:64/0*gTsmBWudIxLcZoel)](https://amannsharmaa.medium.com/?source=post_page---byline--17708cf6029b---------------------------------------)

[Aman Sharma](https://amannsharmaa.medium.com/?source=post_page---byline--17708cf6029b---------------------------------------)

5 min read

·

1 day ago

--

[Listen](https://medium.com/m/signin?actionUrl=https%3A%2F%2Fmedium.com%2Fplans%3Fdimension%3Dpost_audio_button%26postId%3D17708cf6029b&operation=register&redirect=https%3A%2F%2Finfosecwriteups.com%2Fbug-bounty-bootcamp-40-xxe-reading-server-files-and-pivoting-to-internal-networks-through-xml-17708cf6029b&source=---header_actions--17708cf6029b---------------------post_audio_button------------------)

Share

[*Friend link*](https://amannsharmaa.medium.com/bug-bounty-bootcamp-40-xxe-reading-server-files-and-pivoting-to-internal-networks-through-xml-17708cf6029b?sk=e6c6fd36d0cfd0abbbb48972cd5f46ad)

Press enter or click to view image in full size

![]()

Welcome back. You’ve mastered SSRF and chaining. Now we turn to a vulnerability that often flies under the radar: XML External Entity (XXE) injection. When an application parses user‑supplied XML without disabling external entities, an attacker can read local files, perform SSRF, and in some cases achieve remote code execution. Even when the response is blind — no data reflected — you can exfiltrate files via an external DTD and a remote server. This lesson covers the full XXE arsenal: from basic file read to blind exfiltration using base64 encoding.

## What Is XXE? The XML Parser’s Fatal Feature

XML, like HTML, supports entities — placeholders that get replaced with content. An external entity pulls data from a file, URL, or other resource using a `SYSTEM` identifier. If the parser resolves it without restrictions, an…

--

--

[![InfoSec Write-ups](https://miro.medium.com/v2/resize:fill:96:96/1*SWJxYWGZzgmBP1D0Qg_3zQ.png)](https://infosecwriteups.com/?source=post_page---post_publication_info--17708cf6029b---------------------------------------)

[![InfoSec Write-ups](https://miro.medium.com/v2/resize:fill:128:128/1*SWJxYWGZzgmBP1D0Qg_3zQ.png)](https://infosecwriteups.com/?source=post_page---post_publication_info--17708cf6029b---------------------------------------)

[## Published in InfoSec Write-ups](https://infosecwriteups.com/?source=post_page---post_publication_info--17708cf6029b---------------------------------------)

[86K followers](/followers?source=post_page---post_publication_info--17708cf6029b---------------------------------------)

·[Last published 17 hours ago](/built-pentest-environment-on-your-mac-using-docker-bc37c3dcb7ac?source=post_page---post_publication_info--17708cf6029b---------------------------------------)

A collection of write-ups from the best hackers in the world on topics ranging from bug bounties and CTFs to vulnhub machines, hardware challenges and real life encounters. Subscribe to our weekly newsletter for the coolest infosec updates: <https://weekly.infosecwriteups.com/>

[![Aman Sharma](https://miro.medium.com/v2/resize:fill:96:96/0*gTsmBWudIxLcZoel)](https://amannsharmaa.medium.com/?source=post_page---post_author_info--17708cf6029b---------------------------------------)

[![Aman Sharma](https://miro.medium.com/v2/resize:fill:128:128/0*gTsmBWudIxLcZoel)](https://amannsharmaa.medium.com/?source=post_page---post_author_info--17708cf6029b---------------------------------------)

[## Written by Aman Sharma](https://amannsharmaa.medium.com/?source=post_page---post_author_info--17708cf6029b---------------------------------------)

[1.5K followers](https://amannsharmaa.medium.com/followers?source=post_page---post_author_info--17708cf6029b---------------------------------------)

·[22 following](https://medium.com/%40amannsharmaa/following?source=post_page---post_author_info--17708cf6029b---------------------------------------)

| Data Enthusiast | SQL | Python | Power BI | ML | Exploring Cybersecurity & Bug Bounty | Sharing real-world analytics, dashboards & security insights.

[Help](https://help.medium.com/hc/en-us?source=post_page-----17708cf6029b---------------------------------------)

[Status](https://status.medium.com/?source=post_page-----17708cf6029b---------------------------------------)

[About](https://medium.com/about?autoplay=1&source=post_page-----17708cf6029b---------------------------------------)

[Careers](https://medium.com/jobs-at-medium/work-at-medium-959d1a85284e?source=post_page-----17708cf6029b---------------------------------------)

Press

[Blog](https://blog.medium.com/?source=post_page-----17708cf6029b---------------------------------------)

[Privacy](https://policy.medium.com/medium-privacy-policy-f03bf92035c9?source=post_page-----17708cf6029b---------------------------------------)

[Rules](https://policy.medium.com/medium-rules-30e5502c4eb4?source=post_page-----17708cf6029b---------------------------------------)

[Terms](https://policy.medium.com/medium-terms-of-service-9db0094a1e0f?source=post_page-----17708cf6029b---------------------------------------)

[Text to speech](https://speechify.com/medium?source=post_page-----17708cf6029b---------------------------------------)