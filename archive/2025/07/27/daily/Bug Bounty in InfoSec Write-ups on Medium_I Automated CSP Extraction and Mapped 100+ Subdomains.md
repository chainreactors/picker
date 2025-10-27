---
title: I Automated CSP Extraction and Mapped 100+ Subdomains
url: https://infosecwriteups.com/i-automated-csp-extraction-and-mapped-100-subdomains-adf04880ea5d?source=rss----7b722bfd1b8d--bug_bounty
source: Bug Bounty in InfoSec Write-ups on Medium
date: 2025-07-27
fetch_date: 2025-10-06T23:17:22.658059
---

# I Automated CSP Extraction and Mapped 100+ Subdomains

[Sitemap](/sitemap/sitemap.xml)

[Open in app](https://rsci.app.link/?%24canonical_url=https%3A%2F%2Fmedium.com%2Fp%2Fadf04880ea5d&%7Efeature=LoOpenInAppButton&%7Echannel=ShowPostUnderCollection&%7Estage=mobileNavBar&source=post_page---top_nav_layout_nav-----------------------------------------)

Sign up

[Sign in](https://medium.com/m/signin?operation=login&redirect=https%3A%2F%2Finfosecwriteups.com%2Fi-automated-csp-extraction-and-mapped-100-subdomains-adf04880ea5d&source=post_page---top_nav_layout_nav-----------------------global_nav------------------)

[Medium Logo](https://medium.com/?source=post_page---top_nav_layout_nav-----------------------------------------)

[Write](https://medium.com/m/signin?operation=register&redirect=https%3A%2F%2Fmedium.com%2Fnew-story&source=---top_nav_layout_nav-----------------------new_post_topnav------------------)

[Search](https://medium.com/search?source=post_page---top_nav_layout_nav-----------------------------------------)

Sign up

[Sign in](https://medium.com/m/signin?operation=login&redirect=https%3A%2F%2Finfosecwriteups.com%2Fi-automated-csp-extraction-and-mapped-100-subdomains-adf04880ea5d&source=post_page---top_nav_layout_nav-----------------------global_nav------------------)

![](https://miro.medium.com/v2/resize:fill:64:64/1*dmbNkD5D-u45r44go_cf0g.png)

[## InfoSec Write-ups](https://infosecwriteups.com/?source=post_page---publication_nav-7b722bfd1b8d-adf04880ea5d---------------------------------------)

·

Follow publication

[![InfoSec Write-ups](https://miro.medium.com/v2/resize:fill:76:76/1*SWJxYWGZzgmBP1D0Qg_3zQ.png)](https://infosecwriteups.com/?source=post_page---post_publication_sidebar-7b722bfd1b8d-adf04880ea5d---------------------------------------)

A collection of write-ups from the best hackers in the world on topics ranging from bug bounties and CTFs to vulnhub machines, hardware challenges and real life encounters. Subscribe to our weekly newsletter for the coolest infosec updates: <https://weekly.infosecwriteups.com/>

Follow publication

Member-only story

# I Automated CSP Extraction and Mapped 100+ Subdomains

## *How I used CSP headers to automate subdomain discovery at scale — and how you can too.*

[![Ibtissam hammadi](https://miro.medium.com/v2/resize:fill:64:64/1*UlSONScgC0yYgoSEJfzq_A.jpeg)](https://medium.com/%40ibtissamhammadi1?source=post_page---byline--adf04880ea5d---------------------------------------)

[Ibtissam hammadi](https://medium.com/%40ibtissamhammadi1?source=post_page---byline--adf04880ea5d---------------------------------------)

4 min read

·

Jul 26, 2025

--

3

Share

W**ithin 24 hours, my tool parsed 500+ CSP headers and revealed 100+ forgotten subdomains — including admin panels and API gateways.**

Press enter or click to view image in full size

![Content Security Policy (CSP)]()

Photo by [Philipp Tükenmez](https://unsplash.com/%40philippvincent?utm_source=medium&utm_medium=referral) on [Unsplash](https://unsplash.com/?utm_source=medium&utm_medium=referral)

Most bug hunters rely on brute-forcing subdomains, but I found a **hidden goldmine** — **CSP headers**.

While everyone was hammering DNS servers, I was quietly collecting subdomains **without sending a single packet**.

And the best part? **It’s all passive, ethical, and shockingly effective.**

Let me show you how.

### Subdomain Enumeration is Noisy and Overused

If you’ve ever done **bug bounty recon**, you know the struggle:

* Brute-forcing (like with `massdns` or `altdns`) is slow and gets you blocked.
* **Certificate Transparency logs** are useful but miss internal domains.
* **DNS scraping** is hit or miss.

But what if I told you there’s a **passive, low-noise method** that most hunters ignore?

**CSP headers.**

### What Are CSP Headers? (And Why Should You Care?)

--

--

3

[![InfoSec Write-ups](https://miro.medium.com/v2/resize:fill:96:96/1*SWJxYWGZzgmBP1D0Qg_3zQ.png)](https://infosecwriteups.com/?source=post_page---post_publication_info--adf04880ea5d---------------------------------------)

[![InfoSec Write-ups](https://miro.medium.com/v2/resize:fill:128:128/1*SWJxYWGZzgmBP1D0Qg_3zQ.png)](https://infosecwriteups.com/?source=post_page---post_publication_info--adf04880ea5d---------------------------------------)

Follow

[## Published in InfoSec Write-ups](https://infosecwriteups.com/?source=post_page---post_publication_info--adf04880ea5d---------------------------------------)

[71K followers](/followers?source=post_page---post_publication_info--adf04880ea5d---------------------------------------)

·[Last published 2 hours ago](/actuator-unleashed-a-guide-to-finding-and-exploiting-spring-boot-actuator-endpoints-29252dcd9d79?source=post_page---post_publication_info--adf04880ea5d---------------------------------------)

A collection of write-ups from the best hackers in the world on topics ranging from bug bounties and CTFs to vulnhub machines, hardware challenges and real life encounters. Subscribe to our weekly newsletter for the coolest infosec updates: <https://weekly.infosecwriteups.com/>

Follow

[![Ibtissam hammadi](https://miro.medium.com/v2/resize:fill:96:96/1*UlSONScgC0yYgoSEJfzq_A.jpeg)](https://medium.com/%40ibtissamhammadi1?source=post_page---post_author_info--adf04880ea5d---------------------------------------)

[![Ibtissam hammadi](https://miro.medium.com/v2/resize:fill:128:128/1*UlSONScgC0yYgoSEJfzq_A.jpeg)](https://medium.com/%40ibtissamhammadi1?source=post_page---post_author_info--adf04880ea5d---------------------------------------)

[## Written by Ibtissam hammadi](https://medium.com/%40ibtissamhammadi1?source=post_page---post_author_info--adf04880ea5d---------------------------------------)

[4.2K followers](https://medium.com/%40ibtissamhammadi1/followers?source=post_page---post_author_info--adf04880ea5d---------------------------------------)

·[102 following](https://medium.com/%40ibtissamhammadi1/following?source=post_page---post_author_info--adf04880ea5d---------------------------------------)

I am a Senior Data Scientist exploring Cybersecurity, Infosec, Programming, and AI technologies.

## Responses (3)

See all responses

[Help](https://help.medium.com/hc/en-us?source=post_page-----adf04880ea5d---------------------------------------)

[Status](https://status.medium.com/?source=post_page-----adf04880ea5d---------------------------------------)

[About](https://medium.com/about?autoplay=1&source=post_page-----adf04880ea5d---------------------------------------)

[Careers](https://medium.com/jobs-at-medium/work-at-medium-959d1a85284e?source=post_page-----adf04880ea5d---------------------------------------)

Press

[Blog](https://blog.medium.com/?source=post_page-----adf04880ea5d---------------------------------------)

[Privacy](https://policy.medium.com/medium-privacy-policy-f03bf92035c9?source=post_page-----adf04880ea5d---------------------------------------)

[Rules](https://policy.medium.com/medium-rules-30e5502c4eb4?source=post_page-----adf04880ea5d---------------------------------------)

[Terms](https://policy.medium.com/medium-terms-of-service-9db0094a1e0f?source=post_page-----adf04880ea5d---------------------------------------)

[Text to speech](https://speechify.com/medium?source=post_page-----adf04880ea5d---------------------------------------)