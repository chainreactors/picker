---
title: Accessing Employee GitHub SSH Key
url: https://infosecwriteups.com/accessing-employee-github-ssh-key-4e125faba413?source=rss----7b722bfd1b8d--bug_bounty
source: Bug Bounty in InfoSec Write-ups on Medium
date: 2025-09-21
fetch_date: 2025-10-02T20:28:40.799827
---

# Accessing Employee GitHub SSH Key

[Sitemap](/sitemap/sitemap.xml)

[Open in app](https://rsci.app.link/?%24canonical_url=https%3A%2F%2Fmedium.com%2Fp%2F4e125faba413&%7Efeature=LoOpenInAppButton&%7Echannel=ShowPostUnderCollection&%7Estage=mobileNavBar&source=post_page---top_nav_layout_nav-----------------------------------------)

Sign up

[Sign in](https://medium.com/m/signin?operation=login&redirect=https%3A%2F%2Finfosecwriteups.com%2Faccessing-employee-github-ssh-key-4e125faba413&source=post_page---top_nav_layout_nav-----------------------global_nav------------------)

[Medium Logo](https://medium.com/?source=post_page---top_nav_layout_nav-----------------------------------------)

[Write](https://medium.com/m/signin?operation=register&redirect=https%3A%2F%2Fmedium.com%2Fnew-story&source=---top_nav_layout_nav-----------------------new_post_topnav------------------)

[Search](https://medium.com/search?source=post_page---top_nav_layout_nav-----------------------------------------)

Sign up

[Sign in](https://medium.com/m/signin?operation=login&redirect=https%3A%2F%2Finfosecwriteups.com%2Faccessing-employee-github-ssh-key-4e125faba413&source=post_page---top_nav_layout_nav-----------------------global_nav------------------)

![](https://miro.medium.com/v2/resize:fill:64:64/1*dmbNkD5D-u45r44go_cf0g.png)

[## InfoSec Write-ups](https://infosecwriteups.com/?source=post_page---publication_nav-7b722bfd1b8d-4e125faba413---------------------------------------)

·

Follow publication

[![InfoSec Write-ups](https://miro.medium.com/v2/resize:fill:76:76/1*SWJxYWGZzgmBP1D0Qg_3zQ.png)](https://infosecwriteups.com/?source=post_page---post_publication_sidebar-7b722bfd1b8d-4e125faba413---------------------------------------)

A collection of write-ups from the best hackers in the world on topics ranging from bug bounties and CTFs to vulnhub machines, hardware challenges and real life encounters. Subscribe to our weekly newsletter for the coolest infosec updates: <https://weekly.infosecwriteups.com/>

Follow publication

Member-only story

# Accessing Employee GitHub SSH Key

## Recon to Critical Finding

[![SIDDHANT SHUKLA](https://miro.medium.com/v2/resize:fill:64:64/1*8ZQ4ust4pThkatOZK2KniQ.jpeg)](https://ghostman01.medium.com/?source=post_page---byline--4e125faba413---------------------------------------)

[SIDDHANT SHUKLA](https://ghostman01.medium.com/?source=post_page---byline--4e125faba413---------------------------------------)

5 min read

·

Aug 24, 2025

--

8

Share

### [Read for Freee.ee.e](https://ghostman01.medium.com/4e125faba413?sk=ee611807a02905b468935a0a8c6549a7)

![]()

Gear Second

### 🐺Hunters,

Hope my article are simple and understandable for you, even if you’re a beginner. The title has already let you know what’s the finding of the write-up. So let’s get started :)

### Subdomain Selection

One day, I was bored and just looking at my primary target’s recon findings like what I have got any interesting directories and files or any random intersting subdomain.

But nothing interesting, so I thought why not to take a look on my previous reports and if you read my previous blogs, you already knew I love going back to my target, you can read this read article:

[## Revisiting the Past, Hacking the Future

### From Invalid Reports to Real Vulnerabilities: The Path to Growth in Hacking

infosecwriteups.com](/invalid-bug-c3cae222858c?source=post_page-----4e125faba413---------------------------------------)

So I opened my all previous reports and Notion side by side so that I get a quick look if there is something intersting on a particular subdomain previously and forgot to hunt. As I am moving forward with reports I started getting many interesting things but one of my favourite report which was my first **Access**…

--

--

8

[![InfoSec Write-ups](https://miro.medium.com/v2/resize:fill:96:96/1*SWJxYWGZzgmBP1D0Qg_3zQ.png)](https://infosecwriteups.com/?source=post_page---post_publication_info--4e125faba413---------------------------------------)

[![InfoSec Write-ups](https://miro.medium.com/v2/resize:fill:128:128/1*SWJxYWGZzgmBP1D0Qg_3zQ.png)](https://infosecwriteups.com/?source=post_page---post_publication_info--4e125faba413---------------------------------------)

Follow

[## Published in InfoSec Write-ups](https://infosecwriteups.com/?source=post_page---post_publication_info--4e125faba413---------------------------------------)

[71K followers](/followers?source=post_page---post_publication_info--4e125faba413---------------------------------------)

·[Last published 4 days ago](/how-to-find-p1-bugs-using-google-in-your-target-part-1-e37455324dc1?source=post_page---post_publication_info--4e125faba413---------------------------------------)

A collection of write-ups from the best hackers in the world on topics ranging from bug bounties and CTFs to vulnhub machines, hardware challenges and real life encounters. Subscribe to our weekly newsletter for the coolest infosec updates: <https://weekly.infosecwriteups.com/>

Follow

[![SIDDHANT SHUKLA](https://miro.medium.com/v2/resize:fill:96:96/1*8ZQ4ust4pThkatOZK2KniQ.jpeg)](https://ghostman01.medium.com/?source=post_page---post_author_info--4e125faba413---------------------------------------)

[![SIDDHANT SHUKLA](https://miro.medium.com/v2/resize:fill:128:128/1*8ZQ4ust4pThkatOZK2KniQ.jpeg)](https://ghostman01.medium.com/?source=post_page---post_author_info--4e125faba413---------------------------------------)

[## Written by SIDDHANT SHUKLA](https://ghostman01.medium.com/?source=post_page---post_author_info--4e125faba413---------------------------------------)

[825 followers](https://ghostman01.medium.com/followers?source=post_page---post_author_info--4e125faba413---------------------------------------)

·[423 following](https://medium.com/%40ghostman01/following?source=post_page---post_author_info--4e125faba413---------------------------------------)

just a lazy hunter.

## Responses (8)

See all responses

[Help](https://help.medium.com/hc/en-us?source=post_page-----4e125faba413---------------------------------------)

[Status](https://status.medium.com/?source=post_page-----4e125faba413---------------------------------------)

[About](https://medium.com/about?autoplay=1&source=post_page-----4e125faba413---------------------------------------)

[Careers](https://medium.com/jobs-at-medium/work-at-medium-959d1a85284e?source=post_page-----4e125faba413---------------------------------------)

Press

[Blog](https://blog.medium.com/?source=post_page-----4e125faba413---------------------------------------)

[Privacy](https://policy.medium.com/medium-privacy-policy-f03bf92035c9?source=post_page-----4e125faba413---------------------------------------)

[Rules](https://policy.medium.com/medium-rules-30e5502c4eb4?source=post_page-----4e125faba413---------------------------------------)

[Terms](https://policy.medium.com/medium-terms-of-service-9db0094a1e0f?source=post_page-----4e125faba413---------------------------------------)

[Text to speech](https://speechify.com/medium?source=post_page-----4e125faba413---------------------------------------)