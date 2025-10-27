---
title: Hunting OS Command Injection
url: https://infosecwriteups.com/hunting-os-command-injection-039dbb284c7d?source=rss----7b722bfd1b8d--bug_bounty
source: Bug Bounty in InfoSec Write-ups on Medium
date: 2025-09-09
fetch_date: 2025-10-02T19:50:01.800473
---

# Hunting OS Command Injection

[Sitemap](/sitemap/sitemap.xml)

[Open in app](https://rsci.app.link/?%24canonical_url=https%3A%2F%2Fmedium.com%2Fp%2F039dbb284c7d&%7Efeature=LoOpenInAppButton&%7Echannel=ShowPostUnderCollection&%7Estage=mobileNavBar&source=post_page---top_nav_layout_nav-----------------------------------------)

Sign up

[Sign in](https://medium.com/m/signin?operation=login&redirect=https%3A%2F%2Finfosecwriteups.com%2Fhunting-os-command-injection-039dbb284c7d&source=post_page---top_nav_layout_nav-----------------------global_nav------------------)

[Medium Logo](https://medium.com/?source=post_page---top_nav_layout_nav-----------------------------------------)

[Write](https://medium.com/m/signin?operation=register&redirect=https%3A%2F%2Fmedium.com%2Fnew-story&source=---top_nav_layout_nav-----------------------new_post_topnav------------------)

[Search](https://medium.com/search?source=post_page---top_nav_layout_nav-----------------------------------------)

Sign up

[Sign in](https://medium.com/m/signin?operation=login&redirect=https%3A%2F%2Finfosecwriteups.com%2Fhunting-os-command-injection-039dbb284c7d&source=post_page---top_nav_layout_nav-----------------------global_nav------------------)

![](https://miro.medium.com/v2/resize:fill:64:64/1*dmbNkD5D-u45r44go_cf0g.png)

[## InfoSec Write-ups](https://infosecwriteups.com/?source=post_page---publication_nav-7b722bfd1b8d-039dbb284c7d---------------------------------------)

·

Follow publication

[![InfoSec Write-ups](https://miro.medium.com/v2/resize:fill:76:76/1*SWJxYWGZzgmBP1D0Qg_3zQ.png)](https://infosecwriteups.com/?source=post_page---post_publication_sidebar-7b722bfd1b8d-039dbb284c7d---------------------------------------)

A collection of write-ups from the best hackers in the world on topics ranging from bug bounties and CTFs to vulnhub machines, hardware challenges and real life encounters. Subscribe to our weekly newsletter for the coolest infosec updates: <https://weekly.infosecwriteups.com/>

Follow publication

Member-only story

# Hunting OS Command Injection

## Easily Find OS Command Injection Bugs with This Simple Burp Suite Method

[![Monika sharma](https://miro.medium.com/v2/da:true/resize:fill:64:64/0*Tv4b4p5mb6J3IJwD)](https://medium.com/%40commanak46?source=post_page---byline--039dbb284c7d---------------------------------------)

[Monika sharma](https://medium.com/%40commanak46?source=post_page---byline--039dbb284c7d---------------------------------------)

7 min read

·

Sep 8, 2025

--

1

Share

Press enter or click to view image in full size

![]()

OS command injection (also called OS command execution or shell injection) is a serious vulnerability where an attacker can inject malicious commands into a web app, potentially running them on the server’s operating system. This could lead to full server compromise, data theft, or even remote code execution. Finding it manually in Burp Suite is exciting for bug bounty hunters because it often pays big rewards (e.g., $1,000–$10,000 on HackerOne). But you need to be smart about it — don’t just fuzz randomly; start with indicators to see if the site is vulnerable.

In this guide, I’ll explain what I’d look for first on a target website to spot potential OS command injection risks, then walk you through manual steps in Burp Suite to test and exploit it. This is based on real-world bug bounty practices, like those from PortSwigger’s Web Security Academy and HackerOne reports. Remember, always test ethically in scope — use legal targets like labs or bug bounty programs. Let’s break it down step by step.

## Step 1: Initial Recon — What to Look for on the Website to Spot Potential OS Command Injection

--

--

1

[![InfoSec Write-ups](https://miro.medium.com/v2/resize:fill:96:96/1*SWJxYWGZzgmBP1D0Qg_3zQ.png)](https://infosecwriteups.com/?source=post_page---post_publication_info--039dbb284c7d---------------------------------------)

[![InfoSec Write-ups](https://miro.medium.com/v2/resize:fill:128:128/1*SWJxYWGZzgmBP1D0Qg_3zQ.png)](https://infosecwriteups.com/?source=post_page---post_publication_info--039dbb284c7d---------------------------------------)

Follow

[## Published in InfoSec Write-ups](https://infosecwriteups.com/?source=post_page---post_publication_info--039dbb284c7d---------------------------------------)

[71K followers](/followers?source=post_page---post_publication_info--039dbb284c7d---------------------------------------)

·[Last published 4 days ago](/how-to-find-p1-bugs-using-google-in-your-target-part-1-e37455324dc1?source=post_page---post_publication_info--039dbb284c7d---------------------------------------)

A collection of write-ups from the best hackers in the world on topics ranging from bug bounties and CTFs to vulnhub machines, hardware challenges and real life encounters. Subscribe to our weekly newsletter for the coolest infosec updates: <https://weekly.infosecwriteups.com/>

Follow

[![Monika sharma](https://miro.medium.com/v2/resize:fill:96:96/0*Tv4b4p5mb6J3IJwD)](https://medium.com/%40commanak46?source=post_page---post_author_info--039dbb284c7d---------------------------------------)

[![Monika sharma](https://miro.medium.com/v2/resize:fill:128:128/0*Tv4b4p5mb6J3IJwD)](https://medium.com/%40commanak46?source=post_page---post_author_info--039dbb284c7d---------------------------------------)

[## Written by Monika sharma](https://medium.com/%40commanak46?source=post_page---post_author_info--039dbb284c7d---------------------------------------)

[1.99K followers](https://medium.com/%40commanak46/followers?source=post_page---post_author_info--039dbb284c7d---------------------------------------)

·[7 following](https://medium.com/%40commanak46/following?source=post_page---post_author_info--039dbb284c7d---------------------------------------)

## Responses (1)

See all responses

[Help](https://help.medium.com/hc/en-us?source=post_page-----039dbb284c7d---------------------------------------)

[Status](https://status.medium.com/?source=post_page-----039dbb284c7d---------------------------------------)

[About](https://medium.com/about?autoplay=1&source=post_page-----039dbb284c7d---------------------------------------)

[Careers](https://medium.com/jobs-at-medium/work-at-medium-959d1a85284e?source=post_page-----039dbb284c7d---------------------------------------)

Press

[Blog](https://blog.medium.com/?source=post_page-----039dbb284c7d---------------------------------------)

[Privacy](https://policy.medium.com/medium-privacy-policy-f03bf92035c9?source=post_page-----039dbb284c7d---------------------------------------)

[Rules](https://policy.medium.com/medium-rules-30e5502c4eb4?source=post_page-----039dbb284c7d---------------------------------------)

[Terms](https://policy.medium.com/medium-terms-of-service-9db0094a1e0f?source=post_page-----039dbb284c7d---------------------------------------)

[Text to speech](https://speechify.com/medium?source=post_page-----039dbb284c7d---------------------------------------)