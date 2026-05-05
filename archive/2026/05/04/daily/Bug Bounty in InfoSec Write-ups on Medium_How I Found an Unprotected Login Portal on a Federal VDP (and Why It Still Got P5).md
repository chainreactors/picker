---
title: How I Found an Unprotected Login Portal on a Federal VDP (and Why It Still Got P5)
url: https://infosecwriteups.com/how-i-found-an-unprotected-login-portal-on-a-federal-vdp-and-why-it-still-got-p5-e93dbed192b0?source=rss----7b722bfd1b8d--bug_bounty
source: Bug Bounty in InfoSec Write-ups on Medium
date: 2026-05-04
fetch_date: 2026-05-05T05:03:29.262235
---

# How I Found an Unprotected Login Portal on a Federal VDP (and Why It Still Got P5)

[Sitemap](/sitemap/sitemap.xml)

[Open in app](https://play.google.com/store/apps/details?id=com.medium.reader&referrer=utm_source%3DmobileNavBar&source=post_page---top_nav_layout_nav-----------------------------------------)

Sign up

[Sign in](https://medium.com/m/signin?operation=login&redirect=https%3A%2F%2Finfosecwriteups.com%2Fhow-i-found-an-unprotected-login-portal-on-a-federal-vdp-and-why-it-still-got-p5-e93dbed192b0&source=post_page---top_nav_layout_nav-----------------------global_nav------------------)

[Medium Logo](https://medium.com/?source=post_page---top_nav_layout_nav-----------------------------------------)

Get app

[Write](https://medium.com/m/signin?operation=register&redirect=https%3A%2F%2Fmedium.com%2Fnew-story&source=---top_nav_layout_nav-----------------------new_post_topnav------------------)

[Search](https://medium.com/search?source=post_page---top_nav_layout_nav-----------------------------------------)

Sign up

[Sign in](https://medium.com/m/signin?operation=login&redirect=https%3A%2F%2Finfosecwriteups.com%2Fhow-i-found-an-unprotected-login-portal-on-a-federal-vdp-and-why-it-still-got-p5-e93dbed192b0&source=post_page---top_nav_layout_nav-----------------------global_nav------------------)

![](https://miro.medium.com/v2/resize:fill:64:64/1*dmbNkD5D-u45r44go_cf0g.png)

[## InfoSec Write-ups](https://infosecwriteups.com/?source=post_page---publication_nav-7b722bfd1b8d-e93dbed192b0---------------------------------------)

·

[![InfoSec Write-ups](https://miro.medium.com/v2/resize:fill:76:76/1*SWJxYWGZzgmBP1D0Qg_3zQ.png)](https://infosecwriteups.com/?source=post_page---post_publication_sidebar-7b722bfd1b8d-e93dbed192b0---------------------------------------)

A collection of write-ups from the best hackers in the world on topics ranging from bug bounties and CTFs to vulnhub machines, hardware challenges and real life encounters. Subscribe to our weekly newsletter for the coolest infosec updates: <https://weekly.infosecwriteups.com/>

Member-only story

# How I Found an Unprotected Login Portal on a Federal VDP (and Why It Still Got P5)

[![Nicholas Mullenski](https://miro.medium.com/v2/resize:fill:64:64/1*x38eR9tlaUgh7Kj7M1NL2w.jpeg)](https://nicholasmullenski.medium.com/?source=post_page---byline--e93dbed192b0---------------------------------------)

[Nicholas Mullenski](https://nicholasmullenski.medium.com/?source=post_page---byline--e93dbed192b0---------------------------------------)

8 min read

·

15 hours ago

--

[Listen](https://medium.com/m/signin?actionUrl=https%3A%2F%2Fmedium.com%2Fplans%3Fdimension%3Dpost_audio_button%26postId%3De93dbed192b0&operation=register&redirect=https%3A%2F%2Finfosecwriteups.com%2Fhow-i-found-an-unprotected-login-portal-on-a-federal-vdp-and-why-it-still-got-p5-e93dbed192b0&source=---header_actions--e93dbed192b0---------------------post_audio_button------------------)

Share

So I want to walk you through this one because I think the lessons matter more than the finding itself. I’m under NDA on the actual program, vendor, and target — so I’ve swapped in documentation IPs (`203.0.113.x`) and generalized the product. Everything else is real. The methodology, the commands, the reasoning, the mistakes, and the triage outcome; all of it is exactly how it went down.

If you’re newer to bug bounty and you’re hunting on VDPs (Vulnerability Disclosure Programs; the no-bounty ones agencies and companies use to legally accept vuln reports), this is the kind of bug you’ll trip over constantly. Knowing what to do with it is what separates a P5 from a P3.

## The Setup

I was working through a federal VDP that had a handful of IP ranges explicitly listed in scope. Three of those IPs caught my eye because they all responded to HTTPS on 443, and the TLS cert hinted they were the same gateway. When I pulled them up in a browser, I got a login page titled “Please Login” generic enough that it could have been anything, but the form was clearly tied to a real backend.

That’s step one of the methodology I want you to internalize: **don’t move on from a login page until you know what’s behind it.** Half the people doing recon screenshot a login portal and skip it. The other half stop and figure out if it’s a static page or a real authentication surface. The second group finds the bugs.

--

--

[![InfoSec Write-ups](https://miro.medium.com/v2/resize:fill:96:96/1*SWJxYWGZzgmBP1D0Qg_3zQ.png)](https://infosecwriteups.com/?source=post_page---post_publication_info--e93dbed192b0---------------------------------------)

[![InfoSec Write-ups](https://miro.medium.com/v2/resize:fill:128:128/1*SWJxYWGZzgmBP1D0Qg_3zQ.png)](https://infosecwriteups.com/?source=post_page---post_publication_info--e93dbed192b0---------------------------------------)

[## Published in InfoSec Write-ups](https://infosecwriteups.com/?source=post_page---post_publication_info--e93dbed192b0---------------------------------------)

[85K followers](/followers?source=post_page---post_publication_info--e93dbed192b0---------------------------------------)

·[Last published 15 hours ago](/reading-responses-status-codes-headers-and-body-forensics-76c2da93335f?source=post_page---post_publication_info--e93dbed192b0---------------------------------------)

A collection of write-ups from the best hackers in the world on topics ranging from bug bounties and CTFs to vulnhub machines, hardware challenges and real life encounters. Subscribe to our weekly newsletter for the coolest infosec updates: <https://weekly.infosecwriteups.com/>

[![Nicholas Mullenski](https://miro.medium.com/v2/resize:fill:96:96/1*x38eR9tlaUgh7Kj7M1NL2w.jpeg)](https://nicholasmullenski.medium.com/?source=post_page---post_author_info--e93dbed192b0---------------------------------------)

[![Nicholas Mullenski](https://miro.medium.com/v2/resize:fill:128:128/1*x38eR9tlaUgh7Kj7M1NL2w.jpeg)](https://nicholasmullenski.medium.com/?source=post_page---post_author_info--e93dbed192b0---------------------------------------)

[## Written by Nicholas Mullenski](https://nicholasmullenski.medium.com/?source=post_page---post_author_info--e93dbed192b0---------------------------------------)

[110 followers](https://nicholasmullenski.medium.com/followers?source=post_page---post_author_info--e93dbed192b0---------------------------------------)

·[35 following](https://medium.com/%40nicholasmullenski/following?source=post_page---post_author_info--e93dbed192b0---------------------------------------)

Offensive security researcher specializing in web exploitation and vulnerability disclosure. NASA Hall of Fame. HTB Pro Hacker, #677 globally.

[Help](https://help.medium.com/hc/en-us?source=post_page-----e93dbed192b0---------------------------------------)

[Status](https://status.medium.com/?source=post_page-----e93dbed192b0---------------------------------------)

[About](https://medium.com/about?autoplay=1&source=post_page-----e93dbed192b0---------------------------------------)

[Careers](https://medium.com/jobs-at-medium/work-at-medium-959d1a85284e?source=post_page-----e93dbed192b0---------------------------------------)

Press

[Blog](https://blog.medium.com/?source=post_page-----e93dbed192b0---------------------------------------)

[Privacy](https://policy.medium.com/medium-privacy-policy-f03bf92035c9?source=post_page-----e93dbed192b0---------------------------------------)

[Rules](https://policy.medium.com/medium-rules-30e5502c4eb4?source=post_page-----e93dbed192b0---------------------------------------)

[Terms](https://policy.medium.com/medium-terms-of-service-9db0094a1e0f?source=post_page-----e93dbed192b0---------------------------------------)

[Text to speech](https://speechify.com/medium?source=post_page-----e93dbed192b0---------------------------------------)