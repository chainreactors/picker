---
title: Finding SSRF BY Full Automation
url: https://infosecwriteups.com/finding-ssrf-by-full-automation-7d2680091d68?source=rss----7b722bfd1b8d--bug_bounty
source: Bug Bounty in InfoSec Write-ups on Medium
date: 2024-08-27
fetch_date: 2025-10-06T18:03:34.464674
---

# Finding SSRF BY Full Automation

[Sitemap](/sitemap/sitemap.xml)

[Open in app](https://rsci.app.link/?%24canonical_url=https%3A%2F%2Fmedium.com%2Fp%2F7d2680091d68&%7Efeature=LoOpenInAppButton&%7Echannel=ShowPostUnderCollection&%7Estage=mobileNavBar&source=post_page---top_nav_layout_nav-----------------------------------------)

Sign up

[Sign in](https://medium.com/m/signin?operation=login&redirect=https%3A%2F%2Finfosecwriteups.com%2Ffinding-ssrf-by-full-automation-7d2680091d68&source=post_page---top_nav_layout_nav-----------------------global_nav------------------)

[Medium Logo](https://medium.com/?source=post_page---top_nav_layout_nav-----------------------------------------)

[Write](https://medium.com/m/signin?operation=register&redirect=https%3A%2F%2Fmedium.com%2Fnew-story&source=---top_nav_layout_nav-----------------------new_post_topnav------------------)

[Search](https://medium.com/search?source=post_page---top_nav_layout_nav-----------------------------------------)

Sign up

[Sign in](https://medium.com/m/signin?operation=login&redirect=https%3A%2F%2Finfosecwriteups.com%2Ffinding-ssrf-by-full-automation-7d2680091d68&source=post_page---top_nav_layout_nav-----------------------global_nav------------------)

![](https://miro.medium.com/v2/resize:fill:64:64/1*dmbNkD5D-u45r44go_cf0g.png)

[## InfoSec Write-ups](https://infosecwriteups.com/?source=post_page---publication_nav-7b722bfd1b8d-7d2680091d68---------------------------------------)

·

Follow publication

[![InfoSec Write-ups](https://miro.medium.com/v2/resize:fill:76:76/1*SWJxYWGZzgmBP1D0Qg_3zQ.png)](https://infosecwriteups.com/?source=post_page---post_publication_sidebar-7b722bfd1b8d-7d2680091d68---------------------------------------)

A collection of write-ups from the best hackers in the world on topics ranging from bug bounties and CTFs to vulnhub machines, hardware challenges and real life encounters. Subscribe to our weekly newsletter for the coolest infosec updates: <https://weekly.infosecwriteups.com/>

Follow publication

Member-only story

# Finding SSRF BY Full Automation

[![Santosh Kumar Sha(@killmongar1996)](https://miro.medium.com/v2/resize:fill:64:64/1*FtRTo_W_7X1N2zp6furWSA.jpeg)](https://notifybugme.medium.com/?source=post_page---byline--7d2680091d68---------------------------------------)

[Santosh Kumar Sha(@killmongar1996)](https://notifybugme.medium.com/?source=post_page---byline--7d2680091d68---------------------------------------)

3 min read

·

Jan 27, 2021

--

5

Share

Hi, everyone

My name is Santosh Kumar Sha, I’m a security researcher from India(Assam). In this article, I will be describing how I was able to Find SSRF vulnerability by by automating it and leak private information amazon metadata, ec2 and cloud services.

> **I am now offering 1:1 sessions to share my knowledge and expertise:**
>
> [**topmate.io/santosh\_kumar\_sha**](https://topmate.io/santosh_kumar_sha)

## TIP For looking for SSRF bug with automation:

**Tools Requried:**

1. gf (tomnomnom) — <https://github.com/tomnomnom/gf>
2. qsreplace(tomnomnom) — <https://github.com/tomnomnom/qsreplace>
3. ffuf — <https://github.com/ffuf/ffuf>
4. gau(Corben) — <https://github.com/lc/gau>
5. waybackurls(tomnomnom) — <https://github.com/tomnomnom/waybackurls>

## Case#1 — — Accessing SSRF metadata with automation by just using curl and bash

Here get access to internal metadata by ssrf we will collect all URL from way-back machine and look for access the internal data by ssrf

Suppose the the target is targetme.com

Now here process the process for find the ssrf to access internal metadata

**Command for getting the URL:**

waybackurl targetme.com >> blindssrftesturl.txt

--

--

5

[![InfoSec Write-ups](https://miro.medium.com/v2/resize:fill:96:96/1*SWJxYWGZzgmBP1D0Qg_3zQ.png)](https://infosecwriteups.com/?source=post_page---post_publication_info--7d2680091d68---------------------------------------)

[![InfoSec Write-ups](https://miro.medium.com/v2/resize:fill:128:128/1*SWJxYWGZzgmBP1D0Qg_3zQ.png)](https://infosecwriteups.com/?source=post_page---post_publication_info--7d2680091d68---------------------------------------)

Follow

[## Published in InfoSec Write-ups](https://infosecwriteups.com/?source=post_page---post_publication_info--7d2680091d68---------------------------------------)

[71K followers](/followers?source=post_page---post_publication_info--7d2680091d68---------------------------------------)

·[Last published 2 hours ago](/baby-dfc2547dc387?source=post_page---post_publication_info--7d2680091d68---------------------------------------)

A collection of write-ups from the best hackers in the world on topics ranging from bug bounties and CTFs to vulnhub machines, hardware challenges and real life encounters. Subscribe to our weekly newsletter for the coolest infosec updates: <https://weekly.infosecwriteups.com/>

Follow

[![Santosh Kumar Sha(@killmongar1996)](https://miro.medium.com/v2/resize:fill:96:96/1*FtRTo_W_7X1N2zp6furWSA.jpeg)](https://notifybugme.medium.com/?source=post_page---post_author_info--7d2680091d68---------------------------------------)

[![Santosh Kumar Sha(@killmongar1996)](https://miro.medium.com/v2/resize:fill:128:128/1*FtRTo_W_7X1N2zp6furWSA.jpeg)](https://notifybugme.medium.com/?source=post_page---post_author_info--7d2680091d68---------------------------------------)

[## Written by Santosh Kumar Sha(@killmongar1996)](https://notifybugme.medium.com/?source=post_page---post_author_info--7d2680091d68---------------------------------------)

[2.2K followers](https://notifybugme.medium.com/followers?source=post_page---post_author_info--7d2680091d68---------------------------------------)

·[6 following](https://medium.com/%40notifybugme/following?source=post_page---post_author_info--7d2680091d68---------------------------------------)

Cloud Security |Security Researcher |Pentester | Bugbounty hunter|VAPT | Pentration tester | CTF player | [topmate.io/santosh\_kumar\_sha](http://topmate.io/santosh_kumar_sha)

## Responses (5)

See all responses

[Help](https://help.medium.com/hc/en-us?source=post_page-----7d2680091d68---------------------------------------)

[Status](https://status.medium.com/?source=post_page-----7d2680091d68---------------------------------------)

[About](https://medium.com/about?autoplay=1&source=post_page-----7d2680091d68---------------------------------------)

[Careers](https://medium.com/jobs-at-medium/work-at-medium-959d1a85284e?source=post_page-----7d2680091d68---------------------------------------)

Press

[Blog](https://blog.medium.com/?source=post_page-----7d2680091d68---------------------------------------)

[Privacy](https://policy.medium.com/medium-privacy-policy-f03bf92035c9?source=post_page-----7d2680091d68---------------------------------------)

[Rules](https://policy.medium.com/medium-rules-30e5502c4eb4?source=post_page-----7d2680091d68---------------------------------------)

[Terms](https://policy.medium.com/medium-terms-of-service-9db0094a1e0f?source=post_page-----7d2680091d68---------------------------------------)

[Text to speech](https://speechify.com/medium?source=post_page-----7d2680091d68---------------------------------------)