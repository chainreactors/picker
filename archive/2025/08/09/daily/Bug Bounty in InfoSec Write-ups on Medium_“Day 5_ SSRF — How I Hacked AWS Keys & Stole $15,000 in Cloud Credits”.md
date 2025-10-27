---
title: “Day 5: SSRF — How I Hacked AWS Keys & Stole $15,000 in Cloud Credits”
url: https://infosecwriteups.com/day-5-ssrf-how-i-hacked-aws-keys-stole-15-000-in-cloud-credits-ed521d7525f9?source=rss----7b722bfd1b8d--bug_bounty
source: Bug Bounty in InfoSec Write-ups on Medium
date: 2025-08-09
fetch_date: 2025-10-07T00:47:36.922849
---

# “Day 5: SSRF — How I Hacked AWS Keys & Stole $15,000 in Cloud Credits”

[Sitemap](/sitemap/sitemap.xml)

[Open in app](https://rsci.app.link/?%24canonical_url=https%3A%2F%2Fmedium.com%2Fp%2Fed521d7525f9&%7Efeature=LoOpenInAppButton&%7Echannel=ShowPostUnderCollection&%7Estage=mobileNavBar&source=post_page---top_nav_layout_nav-----------------------------------------)

Sign up

[Sign in](https://medium.com/m/signin?operation=login&redirect=https%3A%2F%2Finfosecwriteups.com%2Fday-5-ssrf-how-i-hacked-aws-keys-stole-15-000-in-cloud-credits-ed521d7525f9&source=post_page---top_nav_layout_nav-----------------------global_nav------------------)

[Medium Logo](https://medium.com/?source=post_page---top_nav_layout_nav-----------------------------------------)

[Write](https://medium.com/m/signin?operation=register&redirect=https%3A%2F%2Fmedium.com%2Fnew-story&source=---top_nav_layout_nav-----------------------new_post_topnav------------------)

[Search](https://medium.com/search?source=post_page---top_nav_layout_nav-----------------------------------------)

Sign up

[Sign in](https://medium.com/m/signin?operation=login&redirect=https%3A%2F%2Finfosecwriteups.com%2Fday-5-ssrf-how-i-hacked-aws-keys-stole-15-000-in-cloud-credits-ed521d7525f9&source=post_page---top_nav_layout_nav-----------------------global_nav------------------)

![](https://miro.medium.com/v2/resize:fill:64:64/1*dmbNkD5D-u45r44go_cf0g.png)

[## InfoSec Write-ups](https://infosecwriteups.com/?source=post_page---publication_nav-7b722bfd1b8d-ed521d7525f9---------------------------------------)

·

Follow publication

[![InfoSec Write-ups](https://miro.medium.com/v2/resize:fill:76:76/1*SWJxYWGZzgmBP1D0Qg_3zQ.png)](https://infosecwriteups.com/?source=post_page---post_publication_sidebar-7b722bfd1b8d-ed521d7525f9---------------------------------------)

A collection of write-ups from the best hackers in the world on topics ranging from bug bounties and CTFs to vulnhub machines, hardware challenges and real life encounters. Subscribe to our weekly newsletter for the coolest infosec updates: <https://weekly.infosecwriteups.com/>

Follow publication

Member-only story

# “Day 5: SSRF — How I Hacked AWS Keys & Stole $15,000 in Cloud Credits”

[![Aman Sharma](https://miro.medium.com/v2/da:true/resize:fill:64:64/0*gTsmBWudIxLcZoel)](https://amannsharmaa.medium.com/?source=post_page---byline--ed521d7525f9---------------------------------------)

[Aman Sharma](https://amannsharmaa.medium.com/?source=post_page---byline--ed521d7525f9---------------------------------------)

4 min read

·

Aug 7, 2025

--

2

Share

Three months ago, I found a “low-severity” SSRF (Server-Side Request Forgery) in a SaaS company’s API. What started as a simple internal port scan turned into full AWS access, stolen credentials, and $15,000 in free cloud credits. Today, I’m revealing the full exploit chain — exactly how I did it, with code snippets you can use right now.

[free link](https://amannsharmaa.medium.com/day-5-ssrf-how-i-hacked-aws-keys-stole-15-000-in-cloud-credits-ed521d7525f9?sk=b4f25b2f48adfc991e34b1a7adcbb9da)

![]()

## What is SSRF? (The $500,000 Vulnerability)

SSRF lets attackers trick a server into making unauthorized requests (e.g., accessing internal systems, cloud metadata).

### Real-World Analogy:

Imagine a hotel concierge who will fetch anything you ask for — even if you request “the master key to every room.” That’s SSRF.

## How I Found the SSRF (Step-by-Step Exploit)

### Step 1: Found a Vulnerable API Endpoint

While testing a document converter SaaS, I noticed:

```
POST /api/convert
{ "url": "https://example.com/resume.pdf" }
```

Hypothesis: What if I change the URL to something internal?

### Step 2: Tested for Basic SSRF

--

--

2

[![InfoSec Write-ups](https://miro.medium.com/v2/resize:fill:96:96/1*SWJxYWGZzgmBP1D0Qg_3zQ.png)](https://infosecwriteups.com/?source=post_page---post_publication_info--ed521d7525f9---------------------------------------)

[![InfoSec Write-ups](https://miro.medium.com/v2/resize:fill:128:128/1*SWJxYWGZzgmBP1D0Qg_3zQ.png)](https://infosecwriteups.com/?source=post_page---post_publication_info--ed521d7525f9---------------------------------------)

Follow

[## Published in InfoSec Write-ups](https://infosecwriteups.com/?source=post_page---post_publication_info--ed521d7525f9---------------------------------------)

[71K followers](/followers?source=post_page---post_publication_info--ed521d7525f9---------------------------------------)

·[Last published 4 hours ago](/actuator-unleashed-a-guide-to-finding-and-exploiting-spring-boot-actuator-endpoints-29252dcd9d79?source=post_page---post_publication_info--ed521d7525f9---------------------------------------)

A collection of write-ups from the best hackers in the world on topics ranging from bug bounties and CTFs to vulnhub machines, hardware challenges and real life encounters. Subscribe to our weekly newsletter for the coolest infosec updates: <https://weekly.infosecwriteups.com/>

Follow

[![Aman Sharma](https://miro.medium.com/v2/resize:fill:96:96/0*gTsmBWudIxLcZoel)](https://amannsharmaa.medium.com/?source=post_page---post_author_info--ed521d7525f9---------------------------------------)

[![Aman Sharma](https://miro.medium.com/v2/resize:fill:128:128/0*gTsmBWudIxLcZoel)](https://amannsharmaa.medium.com/?source=post_page---post_author_info--ed521d7525f9---------------------------------------)

[## Written by Aman Sharma](https://amannsharmaa.medium.com/?source=post_page---post_author_info--ed521d7525f9---------------------------------------)

[779 followers](https://amannsharmaa.medium.com/followers?source=post_page---post_author_info--ed521d7525f9---------------------------------------)

·[14 following](https://medium.com/%40amannsharmaa/following?source=post_page---post_author_info--ed521d7525f9---------------------------------------)

| Data Enthusiast | SQL | Python | Power BI | ML | Exploring Cybersecurity & Bug Bounty | Sharing real-world analytics, dashboards & security insights.

## Responses (2)

See all responses

[Help](https://help.medium.com/hc/en-us?source=post_page-----ed521d7525f9---------------------------------------)

[Status](https://status.medium.com/?source=post_page-----ed521d7525f9---------------------------------------)

[About](https://medium.com/about?autoplay=1&source=post_page-----ed521d7525f9---------------------------------------)

[Careers](https://medium.com/jobs-at-medium/work-at-medium-959d1a85284e?source=post_page-----ed521d7525f9---------------------------------------)

Press

[Blog](https://blog.medium.com/?source=post_page-----ed521d7525f9---------------------------------------)

[Privacy](https://policy.medium.com/medium-privacy-policy-f03bf92035c9?source=post_page-----ed521d7525f9---------------------------------------)

[Rules](https://policy.medium.com/medium-rules-30e5502c4eb4?source=post_page-----ed521d7525f9---------------------------------------)

[Terms](https://policy.medium.com/medium-terms-of-service-9db0094a1e0f?source=post_page-----ed521d7525f9---------------------------------------)

[Text to speech](https://speechify.com/medium?source=post_page-----ed521d7525f9---------------------------------------)