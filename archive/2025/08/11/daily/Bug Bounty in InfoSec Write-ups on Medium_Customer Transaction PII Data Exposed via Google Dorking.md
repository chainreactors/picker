---
title: Customer Transaction PII Data Exposed via Google Dorking
url: https://infosecwriteups.com/third-party-google-dorking-e90c2126a3dc?source=rss----7b722bfd1b8d--bug_bounty
source: Bug Bounty in InfoSec Write-ups on Medium
date: 2025-08-11
fetch_date: 2025-10-07T00:17:04.781804
---

# Customer Transaction PII Data Exposed via Google Dorking

[Sitemap](/sitemap/sitemap.xml)

[Open in app](https://rsci.app.link/?%24canonical_url=https%3A%2F%2Fmedium.com%2Fp%2Fe90c2126a3dc&%7Efeature=LoOpenInAppButton&%7Echannel=ShowPostUnderCollection&%7Estage=mobileNavBar&source=post_page---top_nav_layout_nav-----------------------------------------)

Sign up

[Sign in](https://medium.com/m/signin?operation=login&redirect=https%3A%2F%2Finfosecwriteups.com%2Fthird-party-google-dorking-e90c2126a3dc&source=post_page---top_nav_layout_nav-----------------------global_nav------------------)

[Medium Logo](https://medium.com/?source=post_page---top_nav_layout_nav-----------------------------------------)

[Write](https://medium.com/m/signin?operation=register&redirect=https%3A%2F%2Fmedium.com%2Fnew-story&source=---top_nav_layout_nav-----------------------new_post_topnav------------------)

[Search](https://medium.com/search?source=post_page---top_nav_layout_nav-----------------------------------------)

Sign up

[Sign in](https://medium.com/m/signin?operation=login&redirect=https%3A%2F%2Finfosecwriteups.com%2Fthird-party-google-dorking-e90c2126a3dc&source=post_page---top_nav_layout_nav-----------------------global_nav------------------)

![](https://miro.medium.com/v2/resize:fill:64:64/1*dmbNkD5D-u45r44go_cf0g.png)

[## InfoSec Write-ups](https://infosecwriteups.com/?source=post_page---publication_nav-7b722bfd1b8d-e90c2126a3dc---------------------------------------)

·

Follow publication

[![InfoSec Write-ups](https://miro.medium.com/v2/resize:fill:76:76/1*SWJxYWGZzgmBP1D0Qg_3zQ.png)](https://infosecwriteups.com/?source=post_page---post_publication_sidebar-7b722bfd1b8d-e90c2126a3dc---------------------------------------)

A collection of write-ups from the best hackers in the world on topics ranging from bug bounties and CTFs to vulnhub machines, hardware challenges and real life encounters. Subscribe to our weekly newsletter for the coolest infosec updates: <https://weekly.infosecwriteups.com/>

Follow publication

Member-only story

# Customer Transaction PII Data Exposed via Google Dorking

## Simple dorking exposes customer transaction data.

[![SIDDHANT SHUKLA](https://miro.medium.com/v2/resize:fill:64:64/1*8ZQ4ust4pThkatOZK2KniQ.jpeg)](https://ghostman01.medium.com/?source=post_page---byline--e90c2126a3dc---------------------------------------)

[SIDDHANT SHUKLA](https://ghostman01.medium.com/?source=post_page---byline--e90c2126a3dc---------------------------------------)

2 min read

·

Aug 10, 2025

--

6

Share

Press enter or click to view image in full size

![]()

Kakashi

### [Read for Freee.ee.e..](https://ghostman01.medium.com/e90c2126a3dc?sk=72195c0dc86b61e8d517a950a572befc)👈

## 🐺Hunters,

I hope you are learning and applying the knowledge to get bugs. There are many write-ups from that you can learn they are all free to read and beginner friendly writeups.

[## Access Denied Subdomain Bypass

### How manual recon led to unexpected access.

infosecwriteups.com](/access-denied-subdomain-bypass-178c2717fad9?source=post_page-----e90c2126a3dc---------------------------------------)

## My Usual Dorking

First of Not a Big Fan of Google Dorking, I do it randomly whenver I don’t get anything to do.

So, I was hunting this primary target of mine for a very long time and getting Swagger-UI XSS, .git, Admin Token and other kind of bugs till now and made some bounties as well.

If you read my previous write-ups, I did some very basic kind of Google Dorking.

### Finding Login Panels

```
site:*<*.target.com intext:"login" | intitle:"login" | inurl:"login" | intext:"username" | intitle:"username" | inurl:"username" | intext:"password" | intitle:"password" |…
```

--

--

6

[![InfoSec Write-ups](https://miro.medium.com/v2/resize:fill:96:96/1*SWJxYWGZzgmBP1D0Qg_3zQ.png)](https://infosecwriteups.com/?source=post_page---post_publication_info--e90c2126a3dc---------------------------------------)

[![InfoSec Write-ups](https://miro.medium.com/v2/resize:fill:128:128/1*SWJxYWGZzgmBP1D0Qg_3zQ.png)](https://infosecwriteups.com/?source=post_page---post_publication_info--e90c2126a3dc---------------------------------------)

Follow

[## Published in InfoSec Write-ups](https://infosecwriteups.com/?source=post_page---post_publication_info--e90c2126a3dc---------------------------------------)

[71K followers](/followers?source=post_page---post_publication_info--e90c2126a3dc---------------------------------------)

·[Last published 3 hours ago](/actuator-unleashed-a-guide-to-finding-and-exploiting-spring-boot-actuator-endpoints-29252dcd9d79?source=post_page---post_publication_info--e90c2126a3dc---------------------------------------)

A collection of write-ups from the best hackers in the world on topics ranging from bug bounties and CTFs to vulnhub machines, hardware challenges and real life encounters. Subscribe to our weekly newsletter for the coolest infosec updates: <https://weekly.infosecwriteups.com/>

Follow

[![SIDDHANT SHUKLA](https://miro.medium.com/v2/resize:fill:96:96/1*8ZQ4ust4pThkatOZK2KniQ.jpeg)](https://ghostman01.medium.com/?source=post_page---post_author_info--e90c2126a3dc---------------------------------------)

[![SIDDHANT SHUKLA](https://miro.medium.com/v2/resize:fill:128:128/1*8ZQ4ust4pThkatOZK2KniQ.jpeg)](https://ghostman01.medium.com/?source=post_page---post_author_info--e90c2126a3dc---------------------------------------)

[## Written by SIDDHANT SHUKLA](https://ghostman01.medium.com/?source=post_page---post_author_info--e90c2126a3dc---------------------------------------)

[855 followers](https://ghostman01.medium.com/followers?source=post_page---post_author_info--e90c2126a3dc---------------------------------------)

·[424 following](https://medium.com/%40ghostman01/following?source=post_page---post_author_info--e90c2126a3dc---------------------------------------)

just a lazy hunter.

## Responses (6)

See all responses

[Help](https://help.medium.com/hc/en-us?source=post_page-----e90c2126a3dc---------------------------------------)

[Status](https://status.medium.com/?source=post_page-----e90c2126a3dc---------------------------------------)

[About](https://medium.com/about?autoplay=1&source=post_page-----e90c2126a3dc---------------------------------------)

[Careers](https://medium.com/jobs-at-medium/work-at-medium-959d1a85284e?source=post_page-----e90c2126a3dc---------------------------------------)

Press

[Blog](https://blog.medium.com/?source=post_page-----e90c2126a3dc---------------------------------------)

[Privacy](https://policy.medium.com/medium-privacy-policy-f03bf92035c9?source=post_page-----e90c2126a3dc---------------------------------------)

[Rules](https://policy.medium.com/medium-rules-30e5502c4eb4?source=post_page-----e90c2126a3dc---------------------------------------)

[Terms](https://policy.medium.com/medium-terms-of-service-9db0094a1e0f?source=post_page-----e90c2126a3dc---------------------------------------)

[Text to speech](https://speechify.com/medium?source=post_page-----e90c2126a3dc---------------------------------------)