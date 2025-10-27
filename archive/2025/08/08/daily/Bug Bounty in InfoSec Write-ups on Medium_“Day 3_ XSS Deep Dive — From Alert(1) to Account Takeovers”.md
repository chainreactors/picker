---
title: “Day 3: XSS Deep Dive — From Alert(1) to Account Takeovers”
url: https://infosecwriteups.com/day-3-xss-deep-dive-from-alert-1-to-account-takeovers-cf422ec57def?source=rss----7b722bfd1b8d--bug_bounty
source: Bug Bounty in InfoSec Write-ups on Medium
date: 2025-08-08
fetch_date: 2025-10-07T00:16:50.316188
---

# “Day 3: XSS Deep Dive — From Alert(1) to Account Takeovers”

[Sitemap](/sitemap/sitemap.xml)

[Open in app](https://rsci.app.link/?%24canonical_url=https%3A%2F%2Fmedium.com%2Fp%2Fcf422ec57def&%7Efeature=LoOpenInAppButton&%7Echannel=ShowPostUnderCollection&%7Estage=mobileNavBar&source=post_page---top_nav_layout_nav-----------------------------------------)

Sign up

[Sign in](https://medium.com/m/signin?operation=login&redirect=https%3A%2F%2Finfosecwriteups.com%2Fday-3-xss-deep-dive-from-alert-1-to-account-takeovers-cf422ec57def&source=post_page---top_nav_layout_nav-----------------------global_nav------------------)

[Medium Logo](https://medium.com/?source=post_page---top_nav_layout_nav-----------------------------------------)

[Write](https://medium.com/m/signin?operation=register&redirect=https%3A%2F%2Fmedium.com%2Fnew-story&source=---top_nav_layout_nav-----------------------new_post_topnav------------------)

[Search](https://medium.com/search?source=post_page---top_nav_layout_nav-----------------------------------------)

Sign up

[Sign in](https://medium.com/m/signin?operation=login&redirect=https%3A%2F%2Finfosecwriteups.com%2Fday-3-xss-deep-dive-from-alert-1-to-account-takeovers-cf422ec57def&source=post_page---top_nav_layout_nav-----------------------global_nav------------------)

![](https://miro.medium.com/v2/resize:fill:64:64/1*dmbNkD5D-u45r44go_cf0g.png)

[## InfoSec Write-ups](https://infosecwriteups.com/?source=post_page---publication_nav-7b722bfd1b8d-cf422ec57def---------------------------------------)

·

Follow publication

[![InfoSec Write-ups](https://miro.medium.com/v2/resize:fill:76:76/1*SWJxYWGZzgmBP1D0Qg_3zQ.png)](https://infosecwriteups.com/?source=post_page---post_publication_sidebar-7b722bfd1b8d-cf422ec57def---------------------------------------)

A collection of write-ups from the best hackers in the world on topics ranging from bug bounties and CTFs to vulnhub machines, hardware challenges and real life encounters. Subscribe to our weekly newsletter for the coolest infosec updates: <https://weekly.infosecwriteups.com/>

Follow publication

Member-only story

# Day 3: XSS Deep Dive — From Alert(1) to Account Takeovers”

[![Aman Sharma](https://miro.medium.com/v2/da:true/resize:fill:64:64/0*gTsmBWudIxLcZoel)](https://amannsharmaa.medium.com/?source=post_page---byline--cf422ec57def---------------------------------------)

[Aman Sharma](https://amannsharmaa.medium.com/?source=post_page---byline--cf422ec57def---------------------------------------)

3 min read

·

Aug 6, 2025

--

1

Share

Two months ago, I found a reflected XSS in a startup’s contact form. “Big deal,” I thought — until I turned it into a full account takeover chain that paid $5,000. Today, I’m breaking down my entire XSS playbook — from basic alerts to stealing sessions and bypassing WAFs.

[free link](https://amannsharmaa.medium.com/day-3-xss-deep-dive-from-alert-1-to-account-takeovers-cf422ec57def?sk=07cddf0d86f41614e252372531e63f4c)

Press enter or click to view image in full size

![]()

## Part 1: XSS Hunting — Where to Actually Look

Most tutorials tell you to “test all inputs.” That’s lazy. Here’s where I consistently find XSS in 2024:

### 1. Forgotten Inputs Everyone Misses

* HTTP Headers (Yes, really)
* Try:

```
GET / HTTP/1.1
Host: target.com
User-Agent: <script>alert(1)</script>
Referer: javascript:alert(1)
```

* Real Find: A fintech app reflected the `User-Agent` in their admin panel. $2,500.
* PDF Generators
* Upload a PDF with:

```
/Title ("><script>alert(1)</script>)
```

* Why It Works: Many sites parse PDF metadata unsafely.

### 2. The API Blindspot

APIs that return user-controlled data in JSON responses often get overlooked:

```
GET…
```

--

--

1

[![InfoSec Write-ups](https://miro.medium.com/v2/resize:fill:96:96/1*SWJxYWGZzgmBP1D0Qg_3zQ.png)](https://infosecwriteups.com/?source=post_page---post_publication_info--cf422ec57def---------------------------------------)

[![InfoSec Write-ups](https://miro.medium.com/v2/resize:fill:128:128/1*SWJxYWGZzgmBP1D0Qg_3zQ.png)](https://infosecwriteups.com/?source=post_page---post_publication_info--cf422ec57def---------------------------------------)

Follow

[## Published in InfoSec Write-ups](https://infosecwriteups.com/?source=post_page---post_publication_info--cf422ec57def---------------------------------------)

[71K followers](/followers?source=post_page---post_publication_info--cf422ec57def---------------------------------------)

·[Last published 3 hours ago](/actuator-unleashed-a-guide-to-finding-and-exploiting-spring-boot-actuator-endpoints-29252dcd9d79?source=post_page---post_publication_info--cf422ec57def---------------------------------------)

A collection of write-ups from the best hackers in the world on topics ranging from bug bounties and CTFs to vulnhub machines, hardware challenges and real life encounters. Subscribe to our weekly newsletter for the coolest infosec updates: <https://weekly.infosecwriteups.com/>

Follow

[![Aman Sharma](https://miro.medium.com/v2/resize:fill:96:96/0*gTsmBWudIxLcZoel)](https://amannsharmaa.medium.com/?source=post_page---post_author_info--cf422ec57def---------------------------------------)

[![Aman Sharma](https://miro.medium.com/v2/resize:fill:128:128/0*gTsmBWudIxLcZoel)](https://amannsharmaa.medium.com/?source=post_page---post_author_info--cf422ec57def---------------------------------------)

[## Written by Aman Sharma](https://amannsharmaa.medium.com/?source=post_page---post_author_info--cf422ec57def---------------------------------------)

[779 followers](https://amannsharmaa.medium.com/followers?source=post_page---post_author_info--cf422ec57def---------------------------------------)

·[14 following](https://medium.com/%40amannsharmaa/following?source=post_page---post_author_info--cf422ec57def---------------------------------------)

| Data Enthusiast | SQL | Python | Power BI | ML | Exploring Cybersecurity & Bug Bounty | Sharing real-world analytics, dashboards & security insights.

## Responses (1)

See all responses

[Help](https://help.medium.com/hc/en-us?source=post_page-----cf422ec57def---------------------------------------)

[Status](https://status.medium.com/?source=post_page-----cf422ec57def---------------------------------------)

[About](https://medium.com/about?autoplay=1&source=post_page-----cf422ec57def---------------------------------------)

[Careers](https://medium.com/jobs-at-medium/work-at-medium-959d1a85284e?source=post_page-----cf422ec57def---------------------------------------)

Press

[Blog](https://blog.medium.com/?source=post_page-----cf422ec57def---------------------------------------)

[Privacy](https://policy.medium.com/medium-privacy-policy-f03bf92035c9?source=post_page-----cf422ec57def---------------------------------------)

[Rules](https://policy.medium.com/medium-rules-30e5502c4eb4?source=post_page-----cf422ec57def---------------------------------------)

[Terms](https://policy.medium.com/medium-terms-of-service-9db0094a1e0f?source=post_page-----cf422ec57def---------------------------------------)

[Text to speech](https://speechify.com/medium?source=post_page-----cf422ec57def---------------------------------------)