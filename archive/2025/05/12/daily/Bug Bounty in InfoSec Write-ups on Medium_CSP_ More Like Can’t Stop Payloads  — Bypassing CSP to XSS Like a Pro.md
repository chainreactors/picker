---
title: CSP? More Like Can’t Stop Payloads  — Bypassing CSP to XSS Like a Pro
url: https://infosecwriteups.com/csp-more-like-cant-stop-payloads-bypassing-csp-to-xss-like-a-pro-90d27c2c3a40?source=rss----7b722bfd1b8d--bug_bounty
source: Bug Bounty in InfoSec Write-ups on Medium
date: 2025-05-12
fetch_date: 2025-10-06T22:25:03.843812
---

# CSP? More Like Can’t Stop Payloads  — Bypassing CSP to XSS Like a Pro

[Sitemap](/sitemap/sitemap.xml)

[Open in app](https://rsci.app.link/?%24canonical_url=https%3A%2F%2Fmedium.com%2Fp%2F90d27c2c3a40&%7Efeature=LoOpenInAppButton&%7Echannel=ShowPostUnderCollection&%7Estage=mobileNavBar&source=post_page---top_nav_layout_nav-----------------------------------------)

Sign up

[Sign in](https://medium.com/m/signin?operation=login&redirect=https%3A%2F%2Finfosecwriteups.com%2Fcsp-more-like-cant-stop-payloads-bypassing-csp-to-xss-like-a-pro-90d27c2c3a40&source=post_page---top_nav_layout_nav-----------------------global_nav------------------)

[Medium Logo](https://medium.com/?source=post_page---top_nav_layout_nav-----------------------------------------)

[Write](https://medium.com/m/signin?operation=register&redirect=https%3A%2F%2Fmedium.com%2Fnew-story&source=---top_nav_layout_nav-----------------------new_post_topnav------------------)

[Search](https://medium.com/search?source=post_page---top_nav_layout_nav-----------------------------------------)

Sign up

[Sign in](https://medium.com/m/signin?operation=login&redirect=https%3A%2F%2Finfosecwriteups.com%2Fcsp-more-like-cant-stop-payloads-bypassing-csp-to-xss-like-a-pro-90d27c2c3a40&source=post_page---top_nav_layout_nav-----------------------global_nav------------------)

![](https://miro.medium.com/v2/resize:fill:64:64/1*dmbNkD5D-u45r44go_cf0g.png)

[## InfoSec Write-ups](https://infosecwriteups.com/?source=post_page---publication_nav-7b722bfd1b8d-90d27c2c3a40---------------------------------------)

·

Follow publication

[![InfoSec Write-ups](https://miro.medium.com/v2/resize:fill:76:76/1*SWJxYWGZzgmBP1D0Qg_3zQ.png)](https://infosecwriteups.com/?source=post_page---post_publication_sidebar-7b722bfd1b8d-90d27c2c3a40---------------------------------------)

A collection of write-ups from the best hackers in the world on topics ranging from bug bounties and CTFs to vulnhub machines, hardware challenges and real life encounters. Subscribe to our weekly newsletter for the coolest infosec updates: <https://weekly.infosecwriteups.com/>

Follow publication

Member-only story

# 🚧 CSP? More Like Can’t Stop Payloads 🫸🧠 — Bypassing CSP to XSS Like a Pro

[![Iski](https://miro.medium.com/v2/resize:fill:64:64/1*PpvkjPQ1lY6aTYHT9kDX5w.png)](https://medium.com/%40iski?source=post_page---byline--90d27c2c3a40---------------------------------------)

[Iski](https://medium.com/%40iski?source=post_page---byline--90d27c2c3a40---------------------------------------)

3 min read

·

May 9, 2025

--

1

Share

Free [Link](https://medium.com/%40iski/csp-more-like-cant-stop-payloads-bypassing-csp-to-xss-like-a-pro-90d27c2c3a40?sk=6e6f48289bd8fef8e2b6878afdb3353d) 🎈

Hey there!😁

Press enter or click to view image in full size

![]()

Image by Ai

> “I only wanted to test some subdomains… but instead, I ended up karate-chopping CSP into submission and walked away with an XSS that paid for my entire caffeine addiction.”

## 😅 When Life Gives You Headers, Inject Some Payloads

It started like every lazy Sunday: hoodie on, hoodie off, tabs full of Shodan, and a caffeine-fueled terminal session that could fry a data center. I wasn’t even *trying* to find an XSS.

I was running my usual recon script:

```
subfinder -d target.com -silent > subs.txt
httpx -l subs.txt -mc 200,403 -title -tech-detect -x GET > live.txt
gau target.com >> all_urls.txt
waybackurls target.com >> all_urls.txt
```

Then I stumbled upon this juicy endpoint:

```
https://admin-assets.target.com/config/app.viewer?theme=<user-defined>
```

At first glance, it screamed: *“Hi, I reflect parameters, maybe I’m dangerous, maybe I’m not.”* So I poked it.

--

--

1

[![InfoSec Write-ups](https://miro.medium.com/v2/resize:fill:96:96/1*SWJxYWGZzgmBP1D0Qg_3zQ.png)](https://infosecwriteups.com/?source=post_page---post_publication_info--90d27c2c3a40---------------------------------------)

[![InfoSec Write-ups](https://miro.medium.com/v2/resize:fill:128:128/1*SWJxYWGZzgmBP1D0Qg_3zQ.png)](https://infosecwriteups.com/?source=post_page---post_publication_info--90d27c2c3a40---------------------------------------)

Follow

[## Published in InfoSec Write-ups](https://infosecwriteups.com/?source=post_page---post_publication_info--90d27c2c3a40---------------------------------------)

[71K followers](/followers?source=post_page---post_publication_info--90d27c2c3a40---------------------------------------)

·[Last published 2 hours ago](/actuator-unleashed-a-guide-to-finding-and-exploiting-spring-boot-actuator-endpoints-29252dcd9d79?source=post_page---post_publication_info--90d27c2c3a40---------------------------------------)

A collection of write-ups from the best hackers in the world on topics ranging from bug bounties and CTFs to vulnhub machines, hardware challenges and real life encounters. Subscribe to our weekly newsletter for the coolest infosec updates: <https://weekly.infosecwriteups.com/>

Follow

[![Iski](https://miro.medium.com/v2/resize:fill:96:96/1*PpvkjPQ1lY6aTYHT9kDX5w.png)](https://medium.com/%40iski?source=post_page---post_author_info--90d27c2c3a40---------------------------------------)

[![Iski](https://miro.medium.com/v2/resize:fill:128:128/1*PpvkjPQ1lY6aTYHT9kDX5w.png)](https://medium.com/%40iski?source=post_page---post_author_info--90d27c2c3a40---------------------------------------)

[## Written by Iski](https://medium.com/%40iski?source=post_page---post_author_info--90d27c2c3a40---------------------------------------)

[1.8K followers](https://medium.com/%40iski/followers?source=post_page---post_author_info--90d27c2c3a40---------------------------------------)

·[7 following](https://medium.com/%40iski/following?source=post_page---post_author_info--90d27c2c3a40---------------------------------------)

Cybersecurity Researcher | Penetration Tester | Bug Bounty Hunter | Web security| Passionate about cyber security, security automation

## Responses (1)

See all responses

[Help](https://help.medium.com/hc/en-us?source=post_page-----90d27c2c3a40---------------------------------------)

[Status](https://status.medium.com/?source=post_page-----90d27c2c3a40---------------------------------------)

[About](https://medium.com/about?autoplay=1&source=post_page-----90d27c2c3a40---------------------------------------)

[Careers](https://medium.com/jobs-at-medium/work-at-medium-959d1a85284e?source=post_page-----90d27c2c3a40---------------------------------------)

Press

[Blog](https://blog.medium.com/?source=post_page-----90d27c2c3a40---------------------------------------)

[Privacy](https://policy.medium.com/medium-privacy-policy-f03bf92035c9?source=post_page-----90d27c2c3a40---------------------------------------)

[Rules](https://policy.medium.com/medium-rules-30e5502c4eb4?source=post_page-----90d27c2c3a40---------------------------------------)

[Terms](https://policy.medium.com/medium-terms-of-service-9db0094a1e0f?source=post_page-----90d27c2c3a40---------------------------------------)

[Text to speech](https://speechify.com/medium?source=post_page-----90d27c2c3a40---------------------------------------)