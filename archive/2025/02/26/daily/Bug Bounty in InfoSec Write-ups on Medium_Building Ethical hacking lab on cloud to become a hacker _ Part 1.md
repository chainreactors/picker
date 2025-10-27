---
title: Building Ethical hacking lab on cloud to become a hacker | Part 1
url: https://infosecwriteups.com/building-ethical-hacking-lab-on-cloud-to-become-a-hacker-part-1-d410aede27fa?source=rss----7b722bfd1b8d--bug_bounty
source: Bug Bounty in InfoSec Write-ups on Medium
date: 2025-02-26
fetch_date: 2025-10-06T20:34:34.307611
---

# Building Ethical hacking lab on cloud to become a hacker | Part 1

[Sitemap](/sitemap/sitemap.xml)

[Open in app](https://rsci.app.link/?%24canonical_url=https%3A%2F%2Fmedium.com%2Fp%2Fd410aede27fa&%7Efeature=LoOpenInAppButton&%7Echannel=ShowPostUnderCollection&%7Estage=mobileNavBar&source=post_page---top_nav_layout_nav-----------------------------------------)

Sign up

[Sign in](https://medium.com/m/signin?operation=login&redirect=https%3A%2F%2Finfosecwriteups.com%2Fbuilding-ethical-hacking-lab-on-cloud-to-become-a-hacker-part-1-d410aede27fa&source=post_page---top_nav_layout_nav-----------------------global_nav------------------)

[Medium Logo](https://medium.com/?source=post_page---top_nav_layout_nav-----------------------------------------)

[Write](https://medium.com/m/signin?operation=register&redirect=https%3A%2F%2Fmedium.com%2Fnew-story&source=---top_nav_layout_nav-----------------------new_post_topnav------------------)

[Search](https://medium.com/search?source=post_page---top_nav_layout_nav-----------------------------------------)

Sign up

[Sign in](https://medium.com/m/signin?operation=login&redirect=https%3A%2F%2Finfosecwriteups.com%2Fbuilding-ethical-hacking-lab-on-cloud-to-become-a-hacker-part-1-d410aede27fa&source=post_page---top_nav_layout_nav-----------------------global_nav------------------)

![](https://miro.medium.com/v2/resize:fill:64:64/1*dmbNkD5D-u45r44go_cf0g.png)

[Mastodon](https://me.dm/%40theartificialthinker)

[## InfoSec Write-ups](https://infosecwriteups.com/?source=post_page---publication_nav-7b722bfd1b8d-d410aede27fa---------------------------------------)

·

Follow publication

[![InfoSec Write-ups](https://miro.medium.com/v2/resize:fill:76:76/1*SWJxYWGZzgmBP1D0Qg_3zQ.png)](https://infosecwriteups.com/?source=post_page---post_publication_sidebar-7b722bfd1b8d-d410aede27fa---------------------------------------)

A collection of write-ups from the best hackers in the world on topics ranging from bug bounties and CTFs to vulnhub machines, hardware challenges and real life encounters. Subscribe to our weekly newsletter for the coolest infosec updates: <https://weekly.infosecwriteups.com/>

Follow publication

Member-only story

# Build a Hacking lab on cloud (to become a hacker ) 2025 | Part 1

[![Abhishek pawar](https://miro.medium.com/v2/resize:fill:64:64/1*sk-Tu_TV2OgjK9rnAP0G_g.jpeg)](https://theartificialthinker.medium.com/?source=post_page---byline--d410aede27fa---------------------------------------)

[Abhishek pawar](https://theartificialthinker.medium.com/?source=post_page---byline--d410aede27fa---------------------------------------)

6 min read

·

Jan 1, 2025

--

1

Share

To practice my hacking skills, I need a target. Instead of using a virtual machine, I would choose Cloud. Here’s why: [*Friend Link*](https://theartificialthinker.medium.com/d410aede27fa?sk=5fbce9f1852e6ff3960d24e2e3badc46)

Press enter or click to view image in full size

![]()

made by author 😎

![]()

author rocks

My friend was talking about his **New Year’s resolution, LOL!** to start practicing hacking skills. He planned to install bWAPP, OWASP Juice Shop, and other target systems on a virtual machine on his laptop. But after messing around for a bit, he figured out it didn’t really give him that real-world vibe since it was missing stuff like **hacking a public IP, internal networks, and SIEM tools.**

After brief research, I came up with the idea of using an Azure cloud VM, which is essentially a physical computer like a laptop, smartphone, or server located on their premises. We can use them whenever needed.

In this section, I will demonstrate how to create a vulnerable machine and install **target systems like OWASP Juice Shop, DVWA and bWAPP.** We will also explore some Azure topics that will help in your cybersecurity path.

### Requirements

1. If you don’t have an Azure student account yet, just check out this blog to set one up. 👉…

--

--

1

[![InfoSec Write-ups](https://miro.medium.com/v2/resize:fill:96:96/1*SWJxYWGZzgmBP1D0Qg_3zQ.png)](https://infosecwriteups.com/?source=post_page---post_publication_info--d410aede27fa---------------------------------------)

[![InfoSec Write-ups](https://miro.medium.com/v2/resize:fill:128:128/1*SWJxYWGZzgmBP1D0Qg_3zQ.png)](https://infosecwriteups.com/?source=post_page---post_publication_info--d410aede27fa---------------------------------------)

Follow

[## Published in InfoSec Write-ups](https://infosecwriteups.com/?source=post_page---post_publication_info--d410aede27fa---------------------------------------)

[71K followers](/followers?source=post_page---post_publication_info--d410aede27fa---------------------------------------)

·[Last published just now](/actuator-unleashed-a-guide-to-finding-and-exploiting-spring-boot-actuator-endpoints-29252dcd9d79?source=post_page---post_publication_info--d410aede27fa---------------------------------------)

A collection of write-ups from the best hackers in the world on topics ranging from bug bounties and CTFs to vulnhub machines, hardware challenges and real life encounters. Subscribe to our weekly newsletter for the coolest infosec updates: <https://weekly.infosecwriteups.com/>

Follow

[![Abhishek pawar](https://miro.medium.com/v2/resize:fill:96:96/1*sk-Tu_TV2OgjK9rnAP0G_g.jpeg)](https://theartificialthinker.medium.com/?source=post_page---post_author_info--d410aede27fa---------------------------------------)

[![Abhishek pawar](https://miro.medium.com/v2/resize:fill:128:128/1*sk-Tu_TV2OgjK9rnAP0G_g.jpeg)](https://theartificialthinker.medium.com/?source=post_page---post_author_info--d410aede27fa---------------------------------------)

[## Written by Abhishek pawar](https://theartificialthinker.medium.com/?source=post_page---post_author_info--d410aede27fa---------------------------------------)

[161 followers](https://theartificialthinker.medium.com/followers?source=post_page---post_author_info--d410aede27fa---------------------------------------)

·[101 following](https://medium.com/%40theartificialthinker/following?source=post_page---post_author_info--d410aede27fa---------------------------------------)

Entrepreneur, Cybersecurity Enthusiast and engineer

## Responses (1)

See all responses

[Help](https://help.medium.com/hc/en-us?source=post_page-----d410aede27fa---------------------------------------)

[Status](https://status.medium.com/?source=post_page-----d410aede27fa---------------------------------------)

[About](https://medium.com/about?autoplay=1&source=post_page-----d410aede27fa---------------------------------------)

[Careers](https://medium.com/jobs-at-medium/work-at-medium-959d1a85284e?source=post_page-----d410aede27fa---------------------------------------)

Press

[Blog](https://blog.medium.com/?source=post_page-----d410aede27fa---------------------------------------)

[Privacy](https://policy.medium.com/medium-privacy-policy-f03bf92035c9?source=post_page-----d410aede27fa---------------------------------------)

[Rules](https://policy.medium.com/medium-rules-30e5502c4eb4?source=post_page-----d410aede27fa---------------------------------------)

[Terms](https://policy.medium.com/medium-terms-of-service-9db0094a1e0f?source=post_page-----d410aede27fa---------------------------------------)

[Text to speech](https://speechify.com/medium?source=post_page-----d410aede27fa---------------------------------------)