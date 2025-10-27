---
title: SSRF Symphony: How I Turned a PDF Generator Into an Internal Network Spy
url: https://infosecwriteups.com/ssrf-symphony-how-i-turned-a-pdf-generator-into-an-internal-network-spy-0d085a9c1c9e?source=rss----7b722bfd1b8d--bug_bounty
source: Bug Bounty in InfoSec Write-ups on Medium
date: 2025-09-19
fetch_date: 2025-10-02T20:21:42.580324
---

# SSRF Symphony: How I Turned a PDF Generator Into an Internal Network Spy

[Sitemap](/sitemap/sitemap.xml)

[Open in app](https://rsci.app.link/?%24canonical_url=https%3A%2F%2Fmedium.com%2Fp%2F0d085a9c1c9e&%7Efeature=LoOpenInAppButton&%7Echannel=ShowPostUnderCollection&%7Estage=mobileNavBar&source=post_page---top_nav_layout_nav-----------------------------------------)

Sign up

[Sign in](https://medium.com/m/signin?operation=login&redirect=https%3A%2F%2Finfosecwriteups.com%2Fssrf-symphony-how-i-turned-a-pdf-generator-into-an-internal-network-spy-0d085a9c1c9e&source=post_page---top_nav_layout_nav-----------------------global_nav------------------)

[Medium Logo](https://medium.com/?source=post_page---top_nav_layout_nav-----------------------------------------)

[Write](https://medium.com/m/signin?operation=register&redirect=https%3A%2F%2Fmedium.com%2Fnew-story&source=---top_nav_layout_nav-----------------------new_post_topnav------------------)

[Search](https://medium.com/search?source=post_page---top_nav_layout_nav-----------------------------------------)

Sign up

[Sign in](https://medium.com/m/signin?operation=login&redirect=https%3A%2F%2Finfosecwriteups.com%2Fssrf-symphony-how-i-turned-a-pdf-generator-into-an-internal-network-spy-0d085a9c1c9e&source=post_page---top_nav_layout_nav-----------------------global_nav------------------)

![](https://miro.medium.com/v2/resize:fill:64:64/1*dmbNkD5D-u45r44go_cf0g.png)

[## InfoSec Write-ups](https://infosecwriteups.com/?source=post_page---publication_nav-7b722bfd1b8d-0d085a9c1c9e---------------------------------------)

·

Follow publication

[![InfoSec Write-ups](https://miro.medium.com/v2/resize:fill:76:76/1*SWJxYWGZzgmBP1D0Qg_3zQ.png)](https://infosecwriteups.com/?source=post_page---post_publication_sidebar-7b722bfd1b8d-0d085a9c1c9e---------------------------------------)

A collection of write-ups from the best hackers in the world on topics ranging from bug bounties and CTFs to vulnhub machines, hardware challenges and real life encounters. Subscribe to our weekly newsletter for the coolest infosec updates: <https://weekly.infosecwriteups.com/>

Follow publication

Member-only story

# 🌍 SSRF Symphony: How I Turned a PDF Generator Into an Internal Network Spy

[![Iski](https://miro.medium.com/v2/resize:fill:64:64/1*PpvkjPQ1lY6aTYHT9kDX5w.png)](https://medium.com/%40iski?source=post_page---byline--0d085a9c1c9e---------------------------------------)

[Iski](https://medium.com/%40iski?source=post_page---byline--0d085a9c1c9e---------------------------------------)

5 min read

·

Sep 14, 2025

--

1

Share

Free [Link](https://medium.com/%40iski/ssrf-symphony-how-i-turned-a-pdf-generator-into-an-internal-network-spy-0d085a9c1c9e?sk=45a8864e57be864d6289f5d7aff6b81b) 🎈

Hey there!😁

Press enter or click to view image in full size

![]()

Image by AI

From exporting reports to accessing AWS metadata, internal APIs, and cloud secrets. Join my deep dive into exploiting a blind SSRF in a PDF service, chaining vulnerabilities into a critical infrastructure breach. Full PoC included. 🎻

You know that feeling when you’re trying to print a document and the printer jams, but then you accidentally discover the secret admin menu that lets you print free copies for life? 🖨️ That was me — but instead of a printer, it was a multi-million dollar company’s PDF export service, and instead of free copies, I got full access to their internal cloud. My roommate thought I was having too much coffee when I started laughing maniacally at a loading bar.

It all started on a lazy Wednesday. Coffee in hand ☕, I was testing a fancy financial web application — let’s call them `wealthsecure.com`. They had this sleek "Export to PDF" feature on every report page. I'd click it, and a few seconds later, a beautiful PDF would download. Pretty normal, right?

But then I noticed something odd in the network tab…

--

--

1

[![InfoSec Write-ups](https://miro.medium.com/v2/resize:fill:96:96/1*SWJxYWGZzgmBP1D0Qg_3zQ.png)](https://infosecwriteups.com/?source=post_page---post_publication_info--0d085a9c1c9e---------------------------------------)

[![InfoSec Write-ups](https://miro.medium.com/v2/resize:fill:128:128/1*SWJxYWGZzgmBP1D0Qg_3zQ.png)](https://infosecwriteups.com/?source=post_page---post_publication_info--0d085a9c1c9e---------------------------------------)

Follow

[## Published in InfoSec Write-ups](https://infosecwriteups.com/?source=post_page---post_publication_info--0d085a9c1c9e---------------------------------------)

[71K followers](/followers?source=post_page---post_publication_info--0d085a9c1c9e---------------------------------------)

·[Last published 4 days ago](/how-to-find-p1-bugs-using-google-in-your-target-part-1-e37455324dc1?source=post_page---post_publication_info--0d085a9c1c9e---------------------------------------)

A collection of write-ups from the best hackers in the world on topics ranging from bug bounties and CTFs to vulnhub machines, hardware challenges and real life encounters. Subscribe to our weekly newsletter for the coolest infosec updates: <https://weekly.infosecwriteups.com/>

Follow

[![Iski](https://miro.medium.com/v2/resize:fill:96:96/1*PpvkjPQ1lY6aTYHT9kDX5w.png)](https://medium.com/%40iski?source=post_page---post_author_info--0d085a9c1c9e---------------------------------------)

[![Iski](https://miro.medium.com/v2/resize:fill:128:128/1*PpvkjPQ1lY6aTYHT9kDX5w.png)](https://medium.com/%40iski?source=post_page---post_author_info--0d085a9c1c9e---------------------------------------)

[## Written by Iski](https://medium.com/%40iski?source=post_page---post_author_info--0d085a9c1c9e---------------------------------------)

[1.8K followers](https://medium.com/%40iski/followers?source=post_page---post_author_info--0d085a9c1c9e---------------------------------------)

·[7 following](https://medium.com/%40iski/following?source=post_page---post_author_info--0d085a9c1c9e---------------------------------------)

Cybersecurity Researcher | Penetration Tester | Bug Bounty Hunter | Web security| Passionate about cyber security, security automation

## Responses (1)

See all responses

[Help](https://help.medium.com/hc/en-us?source=post_page-----0d085a9c1c9e---------------------------------------)

[Status](https://status.medium.com/?source=post_page-----0d085a9c1c9e---------------------------------------)

[About](https://medium.com/about?autoplay=1&source=post_page-----0d085a9c1c9e---------------------------------------)

[Careers](https://medium.com/jobs-at-medium/work-at-medium-959d1a85284e?source=post_page-----0d085a9c1c9e---------------------------------------)

Press

[Blog](https://blog.medium.com/?source=post_page-----0d085a9c1c9e---------------------------------------)

[Privacy](https://policy.medium.com/medium-privacy-policy-f03bf92035c9?source=post_page-----0d085a9c1c9e---------------------------------------)

[Rules](https://policy.medium.com/medium-rules-30e5502c4eb4?source=post_page-----0d085a9c1c9e---------------------------------------)

[Terms](https://policy.medium.com/medium-terms-of-service-9db0094a1e0f?source=post_page-----0d085a9c1c9e---------------------------------------)

[Text to speech](https://speechify.com/medium?source=post_page-----0d085a9c1c9e---------------------------------------)