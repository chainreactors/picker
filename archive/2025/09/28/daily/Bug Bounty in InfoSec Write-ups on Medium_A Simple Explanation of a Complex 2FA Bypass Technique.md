---
title: A Simple Explanation of a Complex 2FA Bypass Technique
url: https://infosecwriteups.com/a-simple-explanation-of-a-complex-2fa-bypass-technique-de8b1db064a0?source=rss----7b722bfd1b8d--bug_bounty
source: Bug Bounty in InfoSec Write-ups on Medium
date: 2025-09-28
fetch_date: 2025-10-02T20:49:17.550843
---

# A Simple Explanation of a Complex 2FA Bypass Technique

[Sitemap](/sitemap/sitemap.xml)

[Open in app](https://rsci.app.link/?%24canonical_url=https%3A%2F%2Fmedium.com%2Fp%2Fde8b1db064a0&%7Efeature=LoOpenInAppButton&%7Echannel=ShowPostUnderCollection&%7Estage=mobileNavBar&source=post_page---top_nav_layout_nav-----------------------------------------)

Sign up

[Sign in](https://medium.com/m/signin?operation=login&redirect=https%3A%2F%2Finfosecwriteups.com%2Fa-simple-explanation-of-a-complex-2fa-bypass-technique-de8b1db064a0&source=post_page---top_nav_layout_nav-----------------------global_nav------------------)

[Medium Logo](https://medium.com/?source=post_page---top_nav_layout_nav-----------------------------------------)

[Write](https://medium.com/m/signin?operation=register&redirect=https%3A%2F%2Fmedium.com%2Fnew-story&source=---top_nav_layout_nav-----------------------new_post_topnav------------------)

[Search](https://medium.com/search?source=post_page---top_nav_layout_nav-----------------------------------------)

Sign up

[Sign in](https://medium.com/m/signin?operation=login&redirect=https%3A%2F%2Finfosecwriteups.com%2Fa-simple-explanation-of-a-complex-2fa-bypass-technique-de8b1db064a0&source=post_page---top_nav_layout_nav-----------------------global_nav------------------)

![](https://miro.medium.com/v2/resize:fill:64:64/1*dmbNkD5D-u45r44go_cf0g.png)

[## InfoSec Write-ups](https://infosecwriteups.com/?source=post_page---publication_nav-7b722bfd1b8d-de8b1db064a0---------------------------------------)

·

Follow publication

[![InfoSec Write-ups](https://miro.medium.com/v2/resize:fill:76:76/1*SWJxYWGZzgmBP1D0Qg_3zQ.png)](https://infosecwriteups.com/?source=post_page---post_publication_sidebar-7b722bfd1b8d-de8b1db064a0---------------------------------------)

A collection of write-ups from the best hackers in the world on topics ranging from bug bounties and CTFs to vulnhub machines, hardware challenges and real life encounters. Subscribe to our weekly newsletter for the coolest infosec updates: <https://weekly.infosecwriteups.com/>

Follow publication

Member-only story

# A Simple Explanation of a Complex 2FA Bypass Technique

[![Ibtissam hammadi](https://miro.medium.com/v2/resize:fill:64:64/1*UlSONScgC0yYgoSEJfzq_A.jpeg)](https://medium.com/%40ibtissamhammadi1?source=post_page---byline--de8b1db064a0---------------------------------------)

[Ibtissam hammadi](https://medium.com/%40ibtissamhammadi1?source=post_page---byline--de8b1db064a0---------------------------------------)

3 min read

·

5 days ago

--

Share

I once found a hidden door in a fortress. It wasn’t meant to be there. Today, I’ll show you how a tiny timing issue, known as a **Race Condition Vulnerability**, can be the key to a major security flaw.

Press enter or click to view image in full size

![A Simple Explanation of a Complex 2FA Bypass Technique]()

Image generated

**Why should you care?**
If you use two-factor authentication (2FA) to protect your accounts, you trust it to be a solid wall.

This story matters because it demonstrates how that wall can sometimes have a secret passage.

Understanding these flaws is how we make the digital world safer for everyone.

### When Two Requests Have a Race

The main concept is surprisingly simple. Imagine two lines at a coffee shop, both leading to the same barista.

1. You get in the first line and hand over your loyalty card to get a stamp (this is like starting the 2FA login process).
2. Very quickly, you jump into the second line *before the barista has finished stamping your card*.
3. You ask for a free coffee (this is like asking to access your account).
4. If the barista is too busy and just hands you the coffee without checking if the stamping in the first line is done, you’ve won the race.

--

--

[![InfoSec Write-ups](https://miro.medium.com/v2/resize:fill:96:96/1*SWJxYWGZzgmBP1D0Qg_3zQ.png)](https://infosecwriteups.com/?source=post_page---post_publication_info--de8b1db064a0---------------------------------------)

[![InfoSec Write-ups](https://miro.medium.com/v2/resize:fill:128:128/1*SWJxYWGZzgmBP1D0Qg_3zQ.png)](https://infosecwriteups.com/?source=post_page---post_publication_info--de8b1db064a0---------------------------------------)

Follow

[## Published in InfoSec Write-ups](https://infosecwriteups.com/?source=post_page---post_publication_info--de8b1db064a0---------------------------------------)

[71K followers](/followers?source=post_page---post_publication_info--de8b1db064a0---------------------------------------)

·[Last published 4 days ago](/how-to-find-p1-bugs-using-google-in-your-target-part-1-e37455324dc1?source=post_page---post_publication_info--de8b1db064a0---------------------------------------)

A collection of write-ups from the best hackers in the world on topics ranging from bug bounties and CTFs to vulnhub machines, hardware challenges and real life encounters. Subscribe to our weekly newsletter for the coolest infosec updates: <https://weekly.infosecwriteups.com/>

Follow

[![Ibtissam hammadi](https://miro.medium.com/v2/resize:fill:96:96/1*UlSONScgC0yYgoSEJfzq_A.jpeg)](https://medium.com/%40ibtissamhammadi1?source=post_page---post_author_info--de8b1db064a0---------------------------------------)

[![Ibtissam hammadi](https://miro.medium.com/v2/resize:fill:128:128/1*UlSONScgC0yYgoSEJfzq_A.jpeg)](https://medium.com/%40ibtissamhammadi1?source=post_page---post_author_info--de8b1db064a0---------------------------------------)

[## Written by Ibtissam hammadi](https://medium.com/%40ibtissamhammadi1?source=post_page---post_author_info--de8b1db064a0---------------------------------------)

[4.2K followers](https://medium.com/%40ibtissamhammadi1/followers?source=post_page---post_author_info--de8b1db064a0---------------------------------------)

·[98 following](https://medium.com/%40ibtissamhammadi1/following?source=post_page---post_author_info--de8b1db064a0---------------------------------------)

I am a Senior Data Scientist exploring Cybersecurity, Infosec, Programming, and AI technologies.

## No responses yet

[Help](https://help.medium.com/hc/en-us?source=post_page-----de8b1db064a0---------------------------------------)

[Status](https://status.medium.com/?source=post_page-----de8b1db064a0---------------------------------------)

[About](https://medium.com/about?autoplay=1&source=post_page-----de8b1db064a0---------------------------------------)

[Careers](https://medium.com/jobs-at-medium/work-at-medium-959d1a85284e?source=post_page-----de8b1db064a0---------------------------------------)

Press

[Blog](https://blog.medium.com/?source=post_page-----de8b1db064a0---------------------------------------)

[Privacy](https://policy.medium.com/medium-privacy-policy-f03bf92035c9?source=post_page-----de8b1db064a0---------------------------------------)

[Rules](https://policy.medium.com/medium-rules-30e5502c4eb4?source=post_page-----de8b1db064a0---------------------------------------)

[Terms](https://policy.medium.com/medium-terms-of-service-9db0094a1e0f?source=post_page-----de8b1db064a0---------------------------------------)

[Text to speech](https://speechify.com/medium?source=post_page-----de8b1db064a0---------------------------------------)