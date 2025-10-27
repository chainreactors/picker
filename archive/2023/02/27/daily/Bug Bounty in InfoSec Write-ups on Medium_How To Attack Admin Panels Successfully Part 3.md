---
title: How To Attack Admin Panels Successfully Part 3
url: https://infosecwriteups.com/how-to-attack-admin-panels-successfully-part-3-ccf36cbc1c57?source=rss----7b722bfd1b8d--bug_bounty
source: Bug Bounty in InfoSec Write-ups on Medium
date: 2023-02-27
fetch_date: 2025-10-04T08:10:36.975601
---

# How To Attack Admin Panels Successfully Part 3

[Sitemap](/sitemap/sitemap.xml)

[Open in app](https://rsci.app.link/?%24canonical_url=https%3A%2F%2Fmedium.com%2Fp%2Fccf36cbc1c57&%7Efeature=LoOpenInAppButton&%7Echannel=ShowPostUnderCollection&%7Estage=mobileNavBar&source=post_page---top_nav_layout_nav-----------------------------------------)

Sign up

[Sign in](https://medium.com/m/signin?operation=login&redirect=https%3A%2F%2Finfosecwriteups.com%2Fhow-to-attack-admin-panels-successfully-part-3-ccf36cbc1c57&source=post_page---top_nav_layout_nav-----------------------global_nav------------------)

[Medium Logo](https://medium.com/?source=post_page---top_nav_layout_nav-----------------------------------------)

[Write](https://medium.com/m/signin?operation=register&redirect=https%3A%2F%2Fmedium.com%2Fnew-story&source=---top_nav_layout_nav-----------------------new_post_topnav------------------)

[Search](https://medium.com/search?source=post_page---top_nav_layout_nav-----------------------------------------)

Sign up

[Sign in](https://medium.com/m/signin?operation=login&redirect=https%3A%2F%2Finfosecwriteups.com%2Fhow-to-attack-admin-panels-successfully-part-3-ccf36cbc1c57&source=post_page---top_nav_layout_nav-----------------------global_nav------------------)

![](https://miro.medium.com/v2/resize:fill:64:64/1*dmbNkD5D-u45r44go_cf0g.png)

[## InfoSec Write-ups](https://infosecwriteups.com/?source=post_page---publication_nav-7b722bfd1b8d-ccf36cbc1c57---------------------------------------)

·

Follow publication

[![InfoSec Write-ups](https://miro.medium.com/v2/resize:fill:76:76/1*SWJxYWGZzgmBP1D0Qg_3zQ.png)](https://infosecwriteups.com/?source=post_page---post_publication_sidebar-7b722bfd1b8d-ccf36cbc1c57---------------------------------------)

A collection of write-ups from the best hackers in the world on topics ranging from bug bounties and CTFs to vulnhub machines, hardware challenges and real life encounters. Subscribe to our weekly newsletter for the coolest infosec updates: <https://weekly.infosecwriteups.com/>

Follow publication

Member-only story

# How To Attack Admin Panels Successfully Part 3

## Are you Attacking Web Apps Admin Panels The Right Way?

[![c0d3x27](https://miro.medium.com/v2/resize:fill:64:64/1*Kj6QOt5K6dTAPyZ9xrbcbA.png)](https://c0d3x27.medium.com/?source=post_page---byline--ccf36cbc1c57---------------------------------------)

[c0d3x27](https://c0d3x27.medium.com/?source=post_page---byline--ccf36cbc1c57---------------------------------------)

4 min read

·

Feb 26, 2023

--

Share

Press enter or click to view image in full size

![]()

Photo by [Ed Hardie](https://unsplash.com/%40impelling?utm_source=medium&utm_medium=referral) on [Unsplash](https://unsplash.com/?utm_source=medium&utm_medium=referral)

**You should start here:** [**Part\_1**](/how-to-attack-admin-panels-successfully-72c90eeb818c)

## Intro

Picking up from where we left off in part two. This time, we are on a Windows Server. Personally, I’m not a big fan of Windows Servers, and once you try to become a professional Red Teamer, you will understand why. Today, we will learn about *a very basic and simple* ***Active Directory*** attack, a topic not much talked about in the Bug Bounty community since most reports involve just web application vulnerabilities.

### Tree

* Hashcat
* Service Principal Name(SPN)
* *Powershell*
* [Invoke-Kerberoast.ps1](https://github.com/EmpireProject/Empire/blob/master/data/module_source/credentials/Invoke-Kerberoast.ps1)

## Attack Scenario

Unlike Linux servers, because of the complexity of the Windows ecosystem, they are too many different directions to go from here, which is why I will go for the simplest path. Everything will depend on the group policies that were given to the server. Your best bet will be to enumerate everything. We want to be as stealthy as possible, which is why we are going to do everything manually, without using tools like **Mimikatz** that can trigger alerts and get you caught. You will land in **CMD**, and many…

--

--

[![InfoSec Write-ups](https://miro.medium.com/v2/resize:fill:96:96/1*SWJxYWGZzgmBP1D0Qg_3zQ.png)](https://infosecwriteups.com/?source=post_page---post_publication_info--ccf36cbc1c57---------------------------------------)

[![InfoSec Write-ups](https://miro.medium.com/v2/resize:fill:128:128/1*SWJxYWGZzgmBP1D0Qg_3zQ.png)](https://infosecwriteups.com/?source=post_page---post_publication_info--ccf36cbc1c57---------------------------------------)

Follow

[## Published in InfoSec Write-ups](https://infosecwriteups.com/?source=post_page---post_publication_info--ccf36cbc1c57---------------------------------------)

[71K followers](/followers?source=post_page---post_publication_info--ccf36cbc1c57---------------------------------------)

·[Last published 5 days ago](/how-to-find-p1-bugs-using-google-in-your-target-part-1-e37455324dc1?source=post_page---post_publication_info--ccf36cbc1c57---------------------------------------)

A collection of write-ups from the best hackers in the world on topics ranging from bug bounties and CTFs to vulnhub machines, hardware challenges and real life encounters. Subscribe to our weekly newsletter for the coolest infosec updates: <https://weekly.infosecwriteups.com/>

Follow

[![c0d3x27](https://miro.medium.com/v2/resize:fill:96:96/1*Kj6QOt5K6dTAPyZ9xrbcbA.png)](https://c0d3x27.medium.com/?source=post_page---post_author_info--ccf36cbc1c57---------------------------------------)

[![c0d3x27](https://miro.medium.com/v2/resize:fill:128:128/1*Kj6QOt5K6dTAPyZ9xrbcbA.png)](https://c0d3x27.medium.com/?source=post_page---post_author_info--ccf36cbc1c57---------------------------------------)

[## Written by c0d3x27](https://c0d3x27.medium.com/?source=post_page---post_author_info--ccf36cbc1c57---------------------------------------)

[1.8K followers](https://c0d3x27.medium.com/followers?source=post_page---post_author_info--ccf36cbc1c57---------------------------------------)

·[15 following](https://medium.com/%40c0d3x27/following?source=post_page---post_author_info--ccf36cbc1c57---------------------------------------)

OSCP || OSWE || eMAPT || CompTIA CYSA+, Sec+, A+, ITF+, CSAP | | 0-day Researcher | | Security Consultant

## No responses yet

[Help](https://help.medium.com/hc/en-us?source=post_page-----ccf36cbc1c57---------------------------------------)

[Status](https://status.medium.com/?source=post_page-----ccf36cbc1c57---------------------------------------)

[About](https://medium.com/about?autoplay=1&source=post_page-----ccf36cbc1c57---------------------------------------)

[Careers](https://medium.com/jobs-at-medium/work-at-medium-959d1a85284e?source=post_page-----ccf36cbc1c57---------------------------------------)

Press

[Blog](https://blog.medium.com/?source=post_page-----ccf36cbc1c57---------------------------------------)

[Privacy](https://policy.medium.com/medium-privacy-policy-f03bf92035c9?source=post_page-----ccf36cbc1c57---------------------------------------)

[Rules](https://policy.medium.com/medium-rules-30e5502c4eb4?source=post_page-----ccf36cbc1c57---------------------------------------)

[Terms](https://policy.medium.com/medium-terms-of-service-9db0094a1e0f?source=post_page-----ccf36cbc1c57---------------------------------------)

[Text to speech](https://speechify.com/medium?source=post_page-----ccf36cbc1c57---------------------------------------)