---
title: How My Name Crashed a Welcome Party: SSI to RCE Surprise! with $$$$
url: https://infosecwriteups.com/how-my-name-crashed-a-welcome-party-ssi-to-rce-surprise-with-f9b8a05ad138?source=rss----7b722bfd1b8d--bug_bounty
source: Bug Bounty in InfoSec Write-ups on Medium
date: 2025-04-14
fetch_date: 2025-10-06T22:03:50.387524
---

# How My Name Crashed a Welcome Party: SSI to RCE Surprise! with $$$$

[Sitemap](/sitemap/sitemap.xml)

[Open in app](https://rsci.app.link/?%24canonical_url=https%3A%2F%2Fmedium.com%2Fp%2Ff9b8a05ad138&%7Efeature=LoOpenInAppButton&%7Echannel=ShowPostUnderCollection&%7Estage=mobileNavBar&source=post_page---top_nav_layout_nav-----------------------------------------)

Sign up

[Sign in](https://medium.com/m/signin?operation=login&redirect=https%3A%2F%2Finfosecwriteups.com%2Fhow-my-name-crashed-a-welcome-party-ssi-to-rce-surprise-with-f9b8a05ad138&source=post_page---top_nav_layout_nav-----------------------global_nav------------------)

[Medium Logo](https://medium.com/?source=post_page---top_nav_layout_nav-----------------------------------------)

[Write](https://medium.com/m/signin?operation=register&redirect=https%3A%2F%2Fmedium.com%2Fnew-story&source=---top_nav_layout_nav-----------------------new_post_topnav------------------)

[Search](https://medium.com/search?source=post_page---top_nav_layout_nav-----------------------------------------)

Sign up

[Sign in](https://medium.com/m/signin?operation=login&redirect=https%3A%2F%2Finfosecwriteups.com%2Fhow-my-name-crashed-a-welcome-party-ssi-to-rce-surprise-with-f9b8a05ad138&source=post_page---top_nav_layout_nav-----------------------global_nav------------------)

![](https://miro.medium.com/v2/resize:fill:64:64/1*dmbNkD5D-u45r44go_cf0g.png)

[## InfoSec Write-ups](https://infosecwriteups.com/?source=post_page---publication_nav-7b722bfd1b8d-f9b8a05ad138---------------------------------------)

·

Follow publication

[![InfoSec Write-ups](https://miro.medium.com/v2/resize:fill:76:76/1*SWJxYWGZzgmBP1D0Qg_3zQ.png)](https://infosecwriteups.com/?source=post_page---post_publication_sidebar-7b722bfd1b8d-f9b8a05ad138---------------------------------------)

A collection of write-ups from the best hackers in the world on topics ranging from bug bounties and CTFs to vulnhub machines, hardware challenges and real life encounters. Subscribe to our weekly newsletter for the coolest infosec updates: <https://weekly.infosecwriteups.com/>

Follow publication

Member-only story

# How My Name Crashed a Welcome Party: SSI to RCE Surprise! with $$$$🎉

[![Iski](https://miro.medium.com/v2/resize:fill:64:64/1*PpvkjPQ1lY6aTYHT9kDX5w.png)](https://medium.com/%40iski?source=post_page---byline--f9b8a05ad138---------------------------------------)

[Iski](https://medium.com/%40iski?source=post_page---byline--f9b8a05ad138---------------------------------------)

3 min read

·

Apr 1, 2025

--

1

Share

Free [Link](https://medium.com/%40iski/how-my-name-crashed-a-welcome-party-ssi-to-rce-surprise-with-f9b8a05ad138?sk=2671fe8019fcedb255246fe02d82f2f4)🎈

Hey there!

Press enter or click to view image in full size

![]()

Image by ChatGpt

Life lesson number 237: If they don’t remember your name, just break the system until they do! 😎

Hi, I’m Iski, and today I bring you a wild ride from a friendly registration form to a full-blown **Server-Side Template Injection (SSTI)** leading to **Remote Code Execution (RCE)**. Yup, it’s one of those stories where my name quite literally broke the system.

## Recon and Discovery

[## How Recon → SQLi Made €€€€ Bounty

### Hi there…!

infosecwriteups.com](/how-recon-sqli-made-bounty-425fc0fa2e92?source=post_page-----f9b8a05ad138---------------------------------------)

## The “Hello There” Gone Wrong 🚪

It all started with good ol’ recon. After sifting through endpoints like a detective with a magnifying glass, I came across a sign-up page. While most people enter their names without a second thought, I saw an opportunity.

Here’s where the fun began. Like every responsible bug hunter, I thought, why not see how they handle my name? Instead of using the boring ol’ “Iski,”, I went with the classic test payload:

```
{{7*7}}
```

--

--

1

[![InfoSec Write-ups](https://miro.medium.com/v2/resize:fill:96:96/1*SWJxYWGZzgmBP1D0Qg_3zQ.png)](https://infosecwriteups.com/?source=post_page---post_publication_info--f9b8a05ad138---------------------------------------)

[![InfoSec Write-ups](https://miro.medium.com/v2/resize:fill:128:128/1*SWJxYWGZzgmBP1D0Qg_3zQ.png)](https://infosecwriteups.com/?source=post_page---post_publication_info--f9b8a05ad138---------------------------------------)

Follow

[## Published in InfoSec Write-ups](https://infosecwriteups.com/?source=post_page---post_publication_info--f9b8a05ad138---------------------------------------)

[71K followers](/followers?source=post_page---post_publication_info--f9b8a05ad138---------------------------------------)

·[Last published 1 hour ago](/actuator-unleashed-a-guide-to-finding-and-exploiting-spring-boot-actuator-endpoints-29252dcd9d79?source=post_page---post_publication_info--f9b8a05ad138---------------------------------------)

A collection of write-ups from the best hackers in the world on topics ranging from bug bounties and CTFs to vulnhub machines, hardware challenges and real life encounters. Subscribe to our weekly newsletter for the coolest infosec updates: <https://weekly.infosecwriteups.com/>

Follow

[![Iski](https://miro.medium.com/v2/resize:fill:96:96/1*PpvkjPQ1lY6aTYHT9kDX5w.png)](https://medium.com/%40iski?source=post_page---post_author_info--f9b8a05ad138---------------------------------------)

[![Iski](https://miro.medium.com/v2/resize:fill:128:128/1*PpvkjPQ1lY6aTYHT9kDX5w.png)](https://medium.com/%40iski?source=post_page---post_author_info--f9b8a05ad138---------------------------------------)

[## Written by Iski](https://medium.com/%40iski?source=post_page---post_author_info--f9b8a05ad138---------------------------------------)

[1.8K followers](https://medium.com/%40iski/followers?source=post_page---post_author_info--f9b8a05ad138---------------------------------------)

·[7 following](https://medium.com/%40iski/following?source=post_page---post_author_info--f9b8a05ad138---------------------------------------)

Cybersecurity Researcher | Penetration Tester | Bug Bounty Hunter | Web security| Passionate about cyber security, security automation

## Responses (1)

See all responses

[Help](https://help.medium.com/hc/en-us?source=post_page-----f9b8a05ad138---------------------------------------)

[Status](https://status.medium.com/?source=post_page-----f9b8a05ad138---------------------------------------)

[About](https://medium.com/about?autoplay=1&source=post_page-----f9b8a05ad138---------------------------------------)

[Careers](https://medium.com/jobs-at-medium/work-at-medium-959d1a85284e?source=post_page-----f9b8a05ad138---------------------------------------)

Press

[Blog](https://blog.medium.com/?source=post_page-----f9b8a05ad138---------------------------------------)

[Privacy](https://policy.medium.com/medium-privacy-policy-f03bf92035c9?source=post_page-----f9b8a05ad138---------------------------------------)

[Rules](https://policy.medium.com/medium-rules-30e5502c4eb4?source=post_page-----f9b8a05ad138---------------------------------------)

[Terms](https://policy.medium.com/medium-terms-of-service-9db0094a1e0f?source=post_page-----f9b8a05ad138---------------------------------------)

[Text to speech](https://speechify.com/medium?source=post_page-----f9b8a05ad138---------------------------------------)