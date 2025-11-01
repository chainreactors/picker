---
title: Exposed API Keys and Secrets with AI
url: https://infosecwriteups.com/exposed-api-keys-and-secrets-d9c08f34ab73?source=rss----7b722bfd1b8d--bug_bounty
source: Bug Bounty in InfoSec Write-ups on Medium
date: 2025-10-31
fetch_date: 2025-11-01T03:11:15.604399
---

# Exposed API Keys and Secrets with AI

[Sitemap](/sitemap/sitemap.xml)

[Open in app](https://rsci.app.link/?%24canonical_url=https%3A%2F%2Fmedium.com%2Fp%2Fd9c08f34ab73&%7Efeature=LoOpenInAppButton&%7Echannel=ShowPostUnderCollection&%7Estage=mobileNavBar&source=post_page---top_nav_layout_nav-----------------------------------------)

Sign up

[Sign in](https://medium.com/m/signin?operation=login&redirect=https%3A%2F%2Finfosecwriteups.com%2Fexposed-api-keys-and-secrets-d9c08f34ab73&source=post_page---top_nav_layout_nav-----------------------global_nav------------------)

[Medium Logo](https://medium.com/?source=post_page---top_nav_layout_nav-----------------------------------------)

[Write](https://medium.com/m/signin?operation=register&redirect=https%3A%2F%2Fmedium.com%2Fnew-story&source=---top_nav_layout_nav-----------------------new_post_topnav------------------)

[Search](https://medium.com/search?source=post_page---top_nav_layout_nav-----------------------------------------)

Sign up

[Sign in](https://medium.com/m/signin?operation=login&redirect=https%3A%2F%2Finfosecwriteups.com%2Fexposed-api-keys-and-secrets-d9c08f34ab73&source=post_page---top_nav_layout_nav-----------------------global_nav------------------)

![](https://miro.medium.com/v2/resize:fill:64:64/1*dmbNkD5D-u45r44go_cf0g.png)

[## InfoSec Write-ups](https://infosecwriteups.com/?source=post_page---publication_nav-7b722bfd1b8d-d9c08f34ab73---------------------------------------)

·

Follow publication

[![InfoSec Write-ups](https://miro.medium.com/v2/resize:fill:76:76/1*SWJxYWGZzgmBP1D0Qg_3zQ.png)](https://infosecwriteups.com/?source=post_page---post_publication_sidebar-7b722bfd1b8d-d9c08f34ab73---------------------------------------)

A collection of write-ups from the best hackers in the world on topics ranging from bug bounties and CTFs to vulnhub machines, hardware challenges and real life encounters. Subscribe to our weekly newsletter for the coolest infosec updates: <https://weekly.infosecwriteups.com/>

Follow publication

Member-only story

# Fiding API Keys and Secrets with AI

## Perplexity’s Comet Browser helps to find this Bug

[![SIDDHANT SHUKLA](https://miro.medium.com/v2/resize:fill:64:64/1*8ZQ4ust4pThkatOZK2KniQ.jpeg)](https://ghostman01.medium.com/?source=post_page---byline--d9c08f34ab73---------------------------------------)

[SIDDHANT SHUKLA](https://ghostman01.medium.com/?source=post_page---byline--d9c08f34ab73---------------------------------------)

3 min read

·

Oct 16, 2025

--

3

Share

### [Read for Freee..ee.e](https://ghostman01.medium.com/d9c08f34ab73?sk=5f99b7131f71b6a8027a29494050a860)

Press enter or click to view image in full size

![]()

sataru gojo

### 🐺Hunters,

Hope my write-ups are beginner understandable. If you find my write-ups helpful in your Bug Hunting journey then **you can send**:

> 50 Claps, comment, share everywhere

### Introduction

This bug was a quick bug discovery a year ago. I started hunting on this target because I get bored on my primary target.

### Quick Bugs

I started with Google Dorking but didn’t get much on this target, and you can read my article **Impactful Google Dorking:**

[## Impactful Google Dorking on your Target

### All the dorks for your target

infosecwriteups.com](/impactful-google-dorking-ce2f68862ae8?source=post_page-----d9c08f34ab73---------------------------------------)

> I didn’t say anything like you will surely 100% got something sensitive with these dorks on your target.

### Subdomains

The first things starts with Subdomain Discovery using my favourite tool called **subdominator**.

```
subdominator -d target.com | anew…
```

--

--

3

[![InfoSec Write-ups](https://miro.medium.com/v2/resize:fill:96:96/1*SWJxYWGZzgmBP1D0Qg_3zQ.png)](https://infosecwriteups.com/?source=post_page---post_publication_info--d9c08f34ab73---------------------------------------)

[![InfoSec Write-ups](https://miro.medium.com/v2/resize:fill:128:128/1*SWJxYWGZzgmBP1D0Qg_3zQ.png)](https://infosecwriteups.com/?source=post_page---post_publication_info--d9c08f34ab73---------------------------------------)

Follow

[## Published in InfoSec Write-ups](https://infosecwriteups.com/?source=post_page---post_publication_info--d9c08f34ab73---------------------------------------)

[73K followers](/followers?source=post_page---post_publication_info--d9c08f34ab73---------------------------------------)

·[Last published 19 hours ago](/everyone-wants-to-hack-no-one-wants-to-think-a6bb8a313501?source=post_page---post_publication_info--d9c08f34ab73---------------------------------------)

A collection of write-ups from the best hackers in the world on topics ranging from bug bounties and CTFs to vulnhub machines, hardware challenges and real life encounters. Subscribe to our weekly newsletter for the coolest infosec updates: <https://weekly.infosecwriteups.com/>

Follow

[![SIDDHANT SHUKLA](https://miro.medium.com/v2/resize:fill:96:96/1*8ZQ4ust4pThkatOZK2KniQ.jpeg)](https://ghostman01.medium.com/?source=post_page---post_author_info--d9c08f34ab73---------------------------------------)

[![SIDDHANT SHUKLA](https://miro.medium.com/v2/resize:fill:128:128/1*8ZQ4ust4pThkatOZK2KniQ.jpeg)](https://ghostman01.medium.com/?source=post_page---post_author_info--d9c08f34ab73---------------------------------------)

[## Written by SIDDHANT SHUKLA](https://ghostman01.medium.com/?source=post_page---post_author_info--d9c08f34ab73---------------------------------------)

[1K followers](https://ghostman01.medium.com/followers?source=post_page---post_author_info--d9c08f34ab73---------------------------------------)

·[434 following](https://medium.com/%40ghostman01/following?source=post_page---post_author_info--d9c08f34ab73---------------------------------------)

just a lazy hunter.

## Responses (3)

See all responses

[Help](https://help.medium.com/hc/en-us?source=post_page-----d9c08f34ab73---------------------------------------)

[Status](https://status.medium.com/?source=post_page-----d9c08f34ab73---------------------------------------)

[About](https://medium.com/about?autoplay=1&source=post_page-----d9c08f34ab73---------------------------------------)

[Careers](https://medium.com/jobs-at-medium/work-at-medium-959d1a85284e?source=post_page-----d9c08f34ab73---------------------------------------)

Press

[Blog](https://blog.medium.com/?source=post_page-----d9c08f34ab73---------------------------------------)

[Privacy](https://policy.medium.com/medium-privacy-policy-f03bf92035c9?source=post_page-----d9c08f34ab73---------------------------------------)

[Rules](https://policy.medium.com/medium-rules-30e5502c4eb4?source=post_page-----d9c08f34ab73---------------------------------------)

[Terms](https://policy.medium.com/medium-terms-of-service-9db0094a1e0f?source=post_page-----d9c08f34ab73---------------------------------------)

[Text to speech](https://speechify.com/medium?source=post_page-----d9c08f34ab73---------------------------------------)