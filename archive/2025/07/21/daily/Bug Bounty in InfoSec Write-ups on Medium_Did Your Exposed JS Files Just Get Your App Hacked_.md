---
title: Did Your Exposed JS Files Just Get Your App Hacked?
url: https://infosecwriteups.com/did-your-exposed-js-files-just-get-your-app-hacked-2f8c43789091?source=rss----7b722bfd1b8d--bug_bounty
source: Bug Bounty in InfoSec Write-ups on Medium
date: 2025-07-21
fetch_date: 2025-10-06T23:21:41.932905
---

# Did Your Exposed JS Files Just Get Your App Hacked?

[Sitemap](/sitemap/sitemap.xml)

[Open in app](https://rsci.app.link/?%24canonical_url=https%3A%2F%2Fmedium.com%2Fp%2F2f8c43789091&%7Efeature=LoOpenInAppButton&%7Echannel=ShowPostUnderCollection&%7Estage=mobileNavBar&source=post_page---top_nav_layout_nav-----------------------------------------)

Sign up

[Sign in](https://medium.com/m/signin?operation=login&redirect=https%3A%2F%2Finfosecwriteups.com%2Fdid-your-exposed-js-files-just-get-your-app-hacked-2f8c43789091&source=post_page---top_nav_layout_nav-----------------------global_nav------------------)

[Medium Logo](https://medium.com/?source=post_page---top_nav_layout_nav-----------------------------------------)

[Write](https://medium.com/m/signin?operation=register&redirect=https%3A%2F%2Fmedium.com%2Fnew-story&source=---top_nav_layout_nav-----------------------new_post_topnav------------------)

[Search](https://medium.com/search?source=post_page---top_nav_layout_nav-----------------------------------------)

Sign up

[Sign in](https://medium.com/m/signin?operation=login&redirect=https%3A%2F%2Finfosecwriteups.com%2Fdid-your-exposed-js-files-just-get-your-app-hacked-2f8c43789091&source=post_page---top_nav_layout_nav-----------------------global_nav------------------)

![](https://miro.medium.com/v2/resize:fill:64:64/1*dmbNkD5D-u45r44go_cf0g.png)

[## InfoSec Write-ups](https://infosecwriteups.com/?source=post_page---publication_nav-7b722bfd1b8d-2f8c43789091---------------------------------------)

·

Follow publication

[![InfoSec Write-ups](https://miro.medium.com/v2/resize:fill:76:76/1*SWJxYWGZzgmBP1D0Qg_3zQ.png)](https://infosecwriteups.com/?source=post_page---post_publication_sidebar-7b722bfd1b8d-2f8c43789091---------------------------------------)

A collection of write-ups from the best hackers in the world on topics ranging from bug bounties and CTFs to vulnhub machines, hardware challenges and real life encounters. Subscribe to our weekly newsletter for the coolest infosec updates: <https://weekly.infosecwriteups.com/>

Follow publication

Member-only story

# Did Your Exposed JS Files Just Get Your App Hacked?

## How I Found a Company’s API Keys in a Public JavaScript File (And Why Your App Could Be Next)

[![Ibtissam hammadi](https://miro.medium.com/v2/resize:fill:64:64/1*UlSONScgC0yYgoSEJfzq_A.jpeg)](https://medium.com/%40ibtissamhammadi1?source=post_page---byline--2f8c43789091---------------------------------------)

[Ibtissam hammadi](https://medium.com/%40ibtissamhammadi1?source=post_page---byline--2f8c43789091---------------------------------------)

5 min read

·

Jul 20, 2025

--

1

Share

I was browsing a popular website when I accidentally uncovered their **AWS credentials** — wide open in a JavaScript file. And if I found them, so could hackers.s

This wasn’t a **bug bounty hunt**. I wasn’t even **penetration testing**. I was inspecting the page out of curiosity.

Press enter or click to view image in full size

![js file]()

Photo by [MJH SHIKDER](https://unsplash.com/%40mjh_shikder?utm_source=medium&utm_medium=referral) on [Unsplash](https://unsplash.com/?utm_source=medium&utm_medium=referral)

But what I discovered was shocking: **Exposed JS files** containing **API keys, database URLs, and even admin panel paths**.

And the worst part? **Most developers don’t realize they’re making this mistake.**

### The Hidden Dangers of Exposed JavaScript Files

When we think of **app security**, we imagine **firewalls, encryption, and secure authentication**. But sometimes, the biggest risks come from something as simple as a **misconfigured JavaScript file**.

**What’s Inside These Files?**

* **Hardcoded API keys** (Stripe, AWS, Firebase)
* **Database credentials** (MongoDB, PostgreSQL connection strings)
* **Internal endpoints** (Admin panels, unreleased features)
* **Encryption secrets** (JWT tokens, private keys)

--

--

1

[![InfoSec Write-ups](https://miro.medium.com/v2/resize:fill:96:96/1*SWJxYWGZzgmBP1D0Qg_3zQ.png)](https://infosecwriteups.com/?source=post_page---post_publication_info--2f8c43789091---------------------------------------)

[![InfoSec Write-ups](https://miro.medium.com/v2/resize:fill:128:128/1*SWJxYWGZzgmBP1D0Qg_3zQ.png)](https://infosecwriteups.com/?source=post_page---post_publication_info--2f8c43789091---------------------------------------)

Follow

[## Published in InfoSec Write-ups](https://infosecwriteups.com/?source=post_page---post_publication_info--2f8c43789091---------------------------------------)

[71K followers](/followers?source=post_page---post_publication_info--2f8c43789091---------------------------------------)

·[Last published 2 hours ago](/actuator-unleashed-a-guide-to-finding-and-exploiting-spring-boot-actuator-endpoints-29252dcd9d79?source=post_page---post_publication_info--2f8c43789091---------------------------------------)

A collection of write-ups from the best hackers in the world on topics ranging from bug bounties and CTFs to vulnhub machines, hardware challenges and real life encounters. Subscribe to our weekly newsletter for the coolest infosec updates: <https://weekly.infosecwriteups.com/>

Follow

[![Ibtissam hammadi](https://miro.medium.com/v2/resize:fill:96:96/1*UlSONScgC0yYgoSEJfzq_A.jpeg)](https://medium.com/%40ibtissamhammadi1?source=post_page---post_author_info--2f8c43789091---------------------------------------)

[![Ibtissam hammadi](https://miro.medium.com/v2/resize:fill:128:128/1*UlSONScgC0yYgoSEJfzq_A.jpeg)](https://medium.com/%40ibtissamhammadi1?source=post_page---post_author_info--2f8c43789091---------------------------------------)

[## Written by Ibtissam hammadi](https://medium.com/%40ibtissamhammadi1?source=post_page---post_author_info--2f8c43789091---------------------------------------)

[4.2K followers](https://medium.com/%40ibtissamhammadi1/followers?source=post_page---post_author_info--2f8c43789091---------------------------------------)

·[102 following](https://medium.com/%40ibtissamhammadi1/following?source=post_page---post_author_info--2f8c43789091---------------------------------------)

I am a Senior Data Scientist exploring Cybersecurity, Infosec, Programming, and AI technologies.

## Responses (1)

See all responses

[Help](https://help.medium.com/hc/en-us?source=post_page-----2f8c43789091---------------------------------------)

[Status](https://status.medium.com/?source=post_page-----2f8c43789091---------------------------------------)

[About](https://medium.com/about?autoplay=1&source=post_page-----2f8c43789091---------------------------------------)

[Careers](https://medium.com/jobs-at-medium/work-at-medium-959d1a85284e?source=post_page-----2f8c43789091---------------------------------------)

Press

[Blog](https://blog.medium.com/?source=post_page-----2f8c43789091---------------------------------------)

[Privacy](https://policy.medium.com/medium-privacy-policy-f03bf92035c9?source=post_page-----2f8c43789091---------------------------------------)

[Rules](https://policy.medium.com/medium-rules-30e5502c4eb4?source=post_page-----2f8c43789091---------------------------------------)

[Terms](https://policy.medium.com/medium-terms-of-service-9db0094a1e0f?source=post_page-----2f8c43789091---------------------------------------)

[Text to speech](https://speechify.com/medium?source=post_page-----2f8c43789091---------------------------------------)