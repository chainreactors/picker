---
title: $250 Bounty: Privilege Escalation in Acronis via System Clean-up Directory Junction Trick
url: https://infosecwriteups.com/250-bounty-privilege-escalation-in-acronis-via-system-clean-up-directory-junction-trick-f8ab338a6744?source=rss----7b722bfd1b8d--bug_bounty
source: Bug Bounty in InfoSec Write-ups on Medium
date: 2025-07-01
fetch_date: 2025-10-06T23:51:45.560191
---

# $250 Bounty: Privilege Escalation in Acronis via System Clean-up Directory Junction Trick

[Sitemap](/sitemap/sitemap.xml)

[Open in app](https://rsci.app.link/?%24canonical_url=https%3A%2F%2Fmedium.com%2Fp%2Ff8ab338a6744&%7Efeature=LoOpenInAppButton&%7Echannel=ShowPostUnderCollection&%7Estage=mobileNavBar&source=post_page---top_nav_layout_nav-----------------------------------------)

Sign up

[Sign in](https://medium.com/m/signin?operation=login&redirect=https%3A%2F%2Finfosecwriteups.com%2F250-bounty-privilege-escalation-in-acronis-via-system-clean-up-directory-junction-trick-f8ab338a6744&source=post_page---top_nav_layout_nav-----------------------global_nav------------------)

[Medium Logo](https://medium.com/?source=post_page---top_nav_layout_nav-----------------------------------------)

[Write](https://medium.com/m/signin?operation=register&redirect=https%3A%2F%2Fmedium.com%2Fnew-story&source=---top_nav_layout_nav-----------------------new_post_topnav------------------)

[Search](https://medium.com/search?source=post_page---top_nav_layout_nav-----------------------------------------)

Sign up

[Sign in](https://medium.com/m/signin?operation=login&redirect=https%3A%2F%2Finfosecwriteups.com%2F250-bounty-privilege-escalation-in-acronis-via-system-clean-up-directory-junction-trick-f8ab338a6744&source=post_page---top_nav_layout_nav-----------------------global_nav------------------)

![](https://miro.medium.com/v2/resize:fill:64:64/1*dmbNkD5D-u45r44go_cf0g.png)

[## InfoSec Write-ups](https://infosecwriteups.com/?source=post_page---publication_nav-7b722bfd1b8d-f8ab338a6744---------------------------------------)

·

Follow publication

[![InfoSec Write-ups](https://miro.medium.com/v2/resize:fill:76:76/1*SWJxYWGZzgmBP1D0Qg_3zQ.png)](https://infosecwriteups.com/?source=post_page---post_publication_sidebar-7b722bfd1b8d-f8ab338a6744---------------------------------------)

A collection of write-ups from the best hackers in the world on topics ranging from bug bounties and CTFs to vulnhub machines, hardware challenges and real life encounters. Subscribe to our weekly newsletter for the coolest infosec updates: <https://weekly.infosecwriteups.com/>

Follow publication

Member-only story

# $250 Bounty: Privilege Escalation in Acronis via System Clean-up Directory Junction Trick

## How a Simple Symlink Bypass in Windows Temp Folder Let Me Delete Protected System Files Without Admin Rights

[![Monika sharma](https://miro.medium.com/v2/da:true/resize:fill:64:64/0*Tv4b4p5mb6J3IJwD)](https://medium.com/%40commanak46?source=post_page---byline--f8ab338a6744---------------------------------------)

[Monika sharma](https://medium.com/%40commanak46?source=post_page---byline--f8ab338a6744---------------------------------------)

4 min read

·

Jun 30, 2025

--

Share

Press enter or click to view image in full size

![]()

In the never-ending battle for software security, even trusted utilities like system clean-up tools can become dangerous if they overlook subtle file system tricks. In this write-up, I’ll walk you through how I discovered a **Local Privilege Escalation (LPE)** vulnerability in **Acronis True Image 2021**, which earned me a **$250 bounty**.

Using **Directory Junctions**, I was able to delete sensitive system files like `hosts` from `C:\\Windows\\System32\\drivers\\etc` — all without administrative privileges.

> *Impact Summary:*

*An unprivileged user could leverage the* ***System Clean-up*** *feature to delete protected files and folders, leading to potential system misconfiguration or persistence mechanisms being destroyed.*

## The Vulnerability at a Glance

The **System Clean-up** feature in Acronis True Image allows users to clean temporary files, browser data, history, and more. While symlink-based attacks were protected against, the tool was **vulnerable to Directory Junction attacks**.

--

--

[![InfoSec Write-ups](https://miro.medium.com/v2/resize:fill:96:96/1*SWJxYWGZzgmBP1D0Qg_3zQ.png)](https://infosecwriteups.com/?source=post_page---post_publication_info--f8ab338a6744---------------------------------------)

[![InfoSec Write-ups](https://miro.medium.com/v2/resize:fill:128:128/1*SWJxYWGZzgmBP1D0Qg_3zQ.png)](https://infosecwriteups.com/?source=post_page---post_publication_info--f8ab338a6744---------------------------------------)

Follow

[## Published in InfoSec Write-ups](https://infosecwriteups.com/?source=post_page---post_publication_info--f8ab338a6744---------------------------------------)

[71K followers](/followers?source=post_page---post_publication_info--f8ab338a6744---------------------------------------)

·[Last published 3 hours ago](/actuator-unleashed-a-guide-to-finding-and-exploiting-spring-boot-actuator-endpoints-29252dcd9d79?source=post_page---post_publication_info--f8ab338a6744---------------------------------------)

A collection of write-ups from the best hackers in the world on topics ranging from bug bounties and CTFs to vulnhub machines, hardware challenges and real life encounters. Subscribe to our weekly newsletter for the coolest infosec updates: <https://weekly.infosecwriteups.com/>

Follow

[![Monika sharma](https://miro.medium.com/v2/resize:fill:96:96/0*Tv4b4p5mb6J3IJwD)](https://medium.com/%40commanak46?source=post_page---post_author_info--f8ab338a6744---------------------------------------)

[![Monika sharma](https://miro.medium.com/v2/resize:fill:128:128/0*Tv4b4p5mb6J3IJwD)](https://medium.com/%40commanak46?source=post_page---post_author_info--f8ab338a6744---------------------------------------)

[## Written by Monika sharma](https://medium.com/%40commanak46?source=post_page---post_author_info--f8ab338a6744---------------------------------------)

[2K followers](https://medium.com/%40commanak46/followers?source=post_page---post_author_info--f8ab338a6744---------------------------------------)

·[7 following](https://medium.com/%40commanak46/following?source=post_page---post_author_info--f8ab338a6744---------------------------------------)

## No responses yet

[Help](https://help.medium.com/hc/en-us?source=post_page-----f8ab338a6744---------------------------------------)

[Status](https://status.medium.com/?source=post_page-----f8ab338a6744---------------------------------------)

[About](https://medium.com/about?autoplay=1&source=post_page-----f8ab338a6744---------------------------------------)

[Careers](https://medium.com/jobs-at-medium/work-at-medium-959d1a85284e?source=post_page-----f8ab338a6744---------------------------------------)

Press

[Blog](https://blog.medium.com/?source=post_page-----f8ab338a6744---------------------------------------)

[Privacy](https://policy.medium.com/medium-privacy-policy-f03bf92035c9?source=post_page-----f8ab338a6744---------------------------------------)

[Rules](https://policy.medium.com/medium-rules-30e5502c4eb4?source=post_page-----f8ab338a6744---------------------------------------)

[Terms](https://policy.medium.com/medium-terms-of-service-9db0094a1e0f?source=post_page-----f8ab338a6744---------------------------------------)

[Text to speech](https://speechify.com/medium?source=post_page-----f8ab338a6744---------------------------------------)