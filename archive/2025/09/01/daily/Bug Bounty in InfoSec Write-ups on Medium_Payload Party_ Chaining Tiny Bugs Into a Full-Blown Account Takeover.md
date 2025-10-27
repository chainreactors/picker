---
title: Payload Party: Chaining Tiny Bugs Into a Full-Blown Account Takeover
url: https://infosecwriteups.com/payload-party-chaining-tiny-bugs-into-a-full-blown-account-takeover-f85d646f3666?source=rss----7b722bfd1b8d--bug_bounty
source: Bug Bounty in InfoSec Write-ups on Medium
date: 2025-09-01
fetch_date: 2025-10-02T19:29:10.160026
---

# Payload Party: Chaining Tiny Bugs Into a Full-Blown Account Takeover

[Sitemap](/sitemap/sitemap.xml)

[Open in app](https://rsci.app.link/?%24canonical_url=https%3A%2F%2Fmedium.com%2Fp%2Ff85d646f3666&%7Efeature=LoOpenInAppButton&%7Echannel=ShowPostUnderCollection&%7Estage=mobileNavBar&source=post_page---top_nav_layout_nav-----------------------------------------)

Sign up

[Sign in](https://medium.com/m/signin?operation=login&redirect=https%3A%2F%2Finfosecwriteups.com%2Fpayload-party-chaining-tiny-bugs-into-a-full-blown-account-takeover-f85d646f3666&source=post_page---top_nav_layout_nav-----------------------global_nav------------------)

[Medium Logo](https://medium.com/?source=post_page---top_nav_layout_nav-----------------------------------------)

[Write](https://medium.com/m/signin?operation=register&redirect=https%3A%2F%2Fmedium.com%2Fnew-story&source=---top_nav_layout_nav-----------------------new_post_topnav------------------)

[Search](https://medium.com/search?source=post_page---top_nav_layout_nav-----------------------------------------)

Sign up

[Sign in](https://medium.com/m/signin?operation=login&redirect=https%3A%2F%2Finfosecwriteups.com%2Fpayload-party-chaining-tiny-bugs-into-a-full-blown-account-takeover-f85d646f3666&source=post_page---top_nav_layout_nav-----------------------global_nav------------------)

![](https://miro.medium.com/v2/resize:fill:64:64/1*dmbNkD5D-u45r44go_cf0g.png)

[## InfoSec Write-ups](https://infosecwriteups.com/?source=post_page---publication_nav-7b722bfd1b8d-f85d646f3666---------------------------------------)

·

Follow publication

[![InfoSec Write-ups](https://miro.medium.com/v2/resize:fill:76:76/1*SWJxYWGZzgmBP1D0Qg_3zQ.png)](https://infosecwriteups.com/?source=post_page---post_publication_sidebar-7b722bfd1b8d-f85d646f3666---------------------------------------)

A collection of write-ups from the best hackers in the world on topics ranging from bug bounties and CTFs to vulnhub machines, hardware challenges and real life encounters. Subscribe to our weekly newsletter for the coolest infosec updates: <https://weekly.infosecwriteups.com/>

Follow publication

Member-only story

# 📦 Payload Party: Chaining Tiny Bugs Into a Full-Blown Account Takeover

[![Iski](https://miro.medium.com/v2/resize:fill:64:64/1*PpvkjPQ1lY6aTYHT9kDX5w.png)](https://medium.com/%40iski?source=post_page---byline--f85d646f3666---------------------------------------)

[Iski](https://medium.com/%40iski?source=post_page---byline--f85d646f3666---------------------------------------)

3 min read

·

Aug 31, 2025

--

1

Share

Free [link](https://medium.com/%40iski/payload-party-chaining-tiny-bugs-into-a-full-blown-account-takeover-f85d646f3666?sk=8db8e93465f0e3af53f5dd6be03e8be4) 🎈

Hey there!😁

Press enter or click to view image in full size

![]()

Image by AI

**Ever have one of those days where you’re cleaning your desk and find ₹500 you didn’t know existed?** That was my bug bounty: small, forgotten bugs that led to a sweet, unexpected payday.

This is my real story — the *Payload Party*: how I chained micro-flaws, each boring in isolation, into a **full account takeover**. Grab your favorite drink (coffee recommended ☕) and let’s dive in!

[## 🎉 Parameter Swap Party: When Flipping POST to GET Broke the App 🔁💥

### Hey there!😁

infosecwriteups.com](/parameter-swap-party-when-flipping-post-to-get-broke-the-app-9d4cf3d2de6c?source=post_page-----f85d646f3666---------------------------------------)

## 1. Recon Roulette: Gathering the Bug Bits

I began with classic recon tools:

```
subfinder -d target.com -o subs.txt
amass enum -d target.com -o amass.txt
waybackurls target.com | tee endpoints.txt
```

These scans turned up:

* A **forgotten subdomain**: `beta.api.target.com`
* A dusty **open redirect** param: `?next=` in `/login/redirect`
* A `POST /user/update` endpoint that **accepted JSON** without CSRF protection

--

--

1

[![InfoSec Write-ups](https://miro.medium.com/v2/resize:fill:96:96/1*SWJxYWGZzgmBP1D0Qg_3zQ.png)](https://infosecwriteups.com/?source=post_page---post_publication_info--f85d646f3666---------------------------------------)

[![InfoSec Write-ups](https://miro.medium.com/v2/resize:fill:128:128/1*SWJxYWGZzgmBP1D0Qg_3zQ.png)](https://infosecwriteups.com/?source=post_page---post_publication_info--f85d646f3666---------------------------------------)

Follow

[## Published in InfoSec Write-ups](https://infosecwriteups.com/?source=post_page---post_publication_info--f85d646f3666---------------------------------------)

[71K followers](/followers?source=post_page---post_publication_info--f85d646f3666---------------------------------------)

·[Last published 4 days ago](/how-to-find-p1-bugs-using-google-in-your-target-part-1-e37455324dc1?source=post_page---post_publication_info--f85d646f3666---------------------------------------)

A collection of write-ups from the best hackers in the world on topics ranging from bug bounties and CTFs to vulnhub machines, hardware challenges and real life encounters. Subscribe to our weekly newsletter for the coolest infosec updates: <https://weekly.infosecwriteups.com/>

Follow

[![Iski](https://miro.medium.com/v2/resize:fill:96:96/1*PpvkjPQ1lY6aTYHT9kDX5w.png)](https://medium.com/%40iski?source=post_page---post_author_info--f85d646f3666---------------------------------------)

[![Iski](https://miro.medium.com/v2/resize:fill:128:128/1*PpvkjPQ1lY6aTYHT9kDX5w.png)](https://medium.com/%40iski?source=post_page---post_author_info--f85d646f3666---------------------------------------)

[## Written by Iski](https://medium.com/%40iski?source=post_page---post_author_info--f85d646f3666---------------------------------------)

[1.8K followers](https://medium.com/%40iski/followers?source=post_page---post_author_info--f85d646f3666---------------------------------------)

·[7 following](https://medium.com/%40iski/following?source=post_page---post_author_info--f85d646f3666---------------------------------------)

Cybersecurity Researcher | Penetration Tester | Bug Bounty Hunter | Web security| Passionate about cyber security, security automation

## Responses (1)

See all responses

[Help](https://help.medium.com/hc/en-us?source=post_page-----f85d646f3666---------------------------------------)

[Status](https://status.medium.com/?source=post_page-----f85d646f3666---------------------------------------)

[About](https://medium.com/about?autoplay=1&source=post_page-----f85d646f3666---------------------------------------)

[Careers](https://medium.com/jobs-at-medium/work-at-medium-959d1a85284e?source=post_page-----f85d646f3666---------------------------------------)

Press

[Blog](https://blog.medium.com/?source=post_page-----f85d646f3666---------------------------------------)

[Privacy](https://policy.medium.com/medium-privacy-policy-f03bf92035c9?source=post_page-----f85d646f3666---------------------------------------)

[Rules](https://policy.medium.com/medium-rules-30e5502c4eb4?source=post_page-----f85d646f3666---------------------------------------)

[Terms](https://policy.medium.com/medium-terms-of-service-9db0094a1e0f?source=post_page-----f85d646f3666---------------------------------------)

[Text to speech](https://speechify.com/medium?source=post_page-----f85d646f3666---------------------------------------)