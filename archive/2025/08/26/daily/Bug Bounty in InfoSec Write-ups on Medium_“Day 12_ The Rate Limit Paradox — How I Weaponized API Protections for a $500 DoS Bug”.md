---
title: “Day 12: The Rate Limit Paradox — How I Weaponized API Protections for a $500 DoS Bug”
url: https://infosecwriteups.com/day-12-the-rate-limit-paradox-how-i-weaponized-api-protections-for-a-500-dos-bug-497fa5f8fe45?source=rss----7b722bfd1b8d--bug_bounty
source: Bug Bounty in InfoSec Write-ups on Medium
date: 2025-08-26
fetch_date: 2025-10-07T00:47:40.908856
---

# “Day 12: The Rate Limit Paradox — How I Weaponized API Protections for a $500 DoS Bug”

[Sitemap](/sitemap/sitemap.xml)

[Open in app](https://rsci.app.link/?%24canonical_url=https%3A%2F%2Fmedium.com%2Fp%2F497fa5f8fe45&%7Efeature=LoOpenInAppButton&%7Echannel=ShowPostUnderCollection&%7Estage=mobileNavBar&source=post_page---top_nav_layout_nav-----------------------------------------)

Sign up

[Sign in](https://medium.com/m/signin?operation=login&redirect=https%3A%2F%2Finfosecwriteups.com%2Fday-12-the-rate-limit-paradox-how-i-weaponized-api-protections-for-a-500-dos-bug-497fa5f8fe45&source=post_page---top_nav_layout_nav-----------------------global_nav------------------)

[Medium Logo](https://medium.com/?source=post_page---top_nav_layout_nav-----------------------------------------)

[Write](https://medium.com/m/signin?operation=register&redirect=https%3A%2F%2Fmedium.com%2Fnew-story&source=---top_nav_layout_nav-----------------------new_post_topnav------------------)

[Search](https://medium.com/search?source=post_page---top_nav_layout_nav-----------------------------------------)

Sign up

[Sign in](https://medium.com/m/signin?operation=login&redirect=https%3A%2F%2Finfosecwriteups.com%2Fday-12-the-rate-limit-paradox-how-i-weaponized-api-protections-for-a-500-dos-bug-497fa5f8fe45&source=post_page---top_nav_layout_nav-----------------------global_nav------------------)

![](https://miro.medium.com/v2/resize:fill:64:64/1*dmbNkD5D-u45r44go_cf0g.png)

[## InfoSec Write-ups](https://infosecwriteups.com/?source=post_page---publication_nav-7b722bfd1b8d-497fa5f8fe45---------------------------------------)

·

Follow publication

[![InfoSec Write-ups](https://miro.medium.com/v2/resize:fill:76:76/1*SWJxYWGZzgmBP1D0Qg_3zQ.png)](https://infosecwriteups.com/?source=post_page---post_publication_sidebar-7b722bfd1b8d-497fa5f8fe45---------------------------------------)

A collection of write-ups from the best hackers in the world on topics ranging from bug bounties and CTFs to vulnhub machines, hardware challenges and real life encounters. Subscribe to our weekly newsletter for the coolest infosec updates: <https://weekly.infosecwriteups.com/>

Follow publication

Member-only story

# “Day 12: The Rate Limit Paradox — How I Weaponized API Protections for a $500 DoS Bug”

## Turning Security Features Into Attack Vectors Through Creative Abuse

[![Aman Sharma](https://miro.medium.com/v2/da:true/resize:fill:64:64/0*gTsmBWudIxLcZoel)](https://amannsharmaa.medium.com/?source=post_page---byline--497fa5f8fe45---------------------------------------)

[Aman Sharma](https://amannsharmaa.medium.com/?source=post_page---byline--497fa5f8fe45---------------------------------------)

3 min read

·

Aug 15, 2025

--

Share

While testing a fintech API last month, I discovered their “robust” rate limiting system had a fatal flaw — it could be tricked into locking every user account for 24 hours. What the developers intended as brute-force protection became a denial-of-service weapon, earning me a $500 bounty. Here’s how API safeguards can backfire spectacularly.

[free link](https://amannsharmaa.medium.com/day-12-the-rate-limit-paradox-how-i-weaponized-api-protections-for-a-500-dos-bug-497fa5f8fe45?sk=8b20fdfcb1f5dae634d58675cc8bdef3)

Press enter or click to view image in full size

![]()

## The Rate Limit Arms Race

Modern APIs implement protections like:

* IP-based throttling (100 requests/minute)
* Account lockouts (5 failed logins → 15min freeze)
* CAPTCHAs after suspicious activity

The Irony:

> *68% of these controls introduce new vulnerabilities when misconfigured (*2024 Cloud Security Report*)*

## The $500 Exploit Chain

### Phase 1: Normal Testing Hit a Wall

```
curl -X POST https://api.bank.com/login -d '{"user":"test"}'
# Response: 429 Too Many Requests
```

--

--

[![InfoSec Write-ups](https://miro.medium.com/v2/resize:fill:96:96/1*SWJxYWGZzgmBP1D0Qg_3zQ.png)](https://infosecwriteups.com/?source=post_page---post_publication_info--497fa5f8fe45---------------------------------------)

[![InfoSec Write-ups](https://miro.medium.com/v2/resize:fill:128:128/1*SWJxYWGZzgmBP1D0Qg_3zQ.png)](https://infosecwriteups.com/?source=post_page---post_publication_info--497fa5f8fe45---------------------------------------)

Follow

[## Published in InfoSec Write-ups](https://infosecwriteups.com/?source=post_page---post_publication_info--497fa5f8fe45---------------------------------------)

[71K followers](/followers?source=post_page---post_publication_info--497fa5f8fe45---------------------------------------)

·[Last published 4 hours ago](/actuator-unleashed-a-guide-to-finding-and-exploiting-spring-boot-actuator-endpoints-29252dcd9d79?source=post_page---post_publication_info--497fa5f8fe45---------------------------------------)

A collection of write-ups from the best hackers in the world on topics ranging from bug bounties and CTFs to vulnhub machines, hardware challenges and real life encounters. Subscribe to our weekly newsletter for the coolest infosec updates: <https://weekly.infosecwriteups.com/>

Follow

[![Aman Sharma](https://miro.medium.com/v2/resize:fill:96:96/0*gTsmBWudIxLcZoel)](https://amannsharmaa.medium.com/?source=post_page---post_author_info--497fa5f8fe45---------------------------------------)

[![Aman Sharma](https://miro.medium.com/v2/resize:fill:128:128/0*gTsmBWudIxLcZoel)](https://amannsharmaa.medium.com/?source=post_page---post_author_info--497fa5f8fe45---------------------------------------)

[## Written by Aman Sharma](https://amannsharmaa.medium.com/?source=post_page---post_author_info--497fa5f8fe45---------------------------------------)

[779 followers](https://amannsharmaa.medium.com/followers?source=post_page---post_author_info--497fa5f8fe45---------------------------------------)

·[14 following](https://medium.com/%40amannsharmaa/following?source=post_page---post_author_info--497fa5f8fe45---------------------------------------)

| Data Enthusiast | SQL | Python | Power BI | ML | Exploring Cybersecurity & Bug Bounty | Sharing real-world analytics, dashboards & security insights.

## No responses yet

[Help](https://help.medium.com/hc/en-us?source=post_page-----497fa5f8fe45---------------------------------------)

[Status](https://status.medium.com/?source=post_page-----497fa5f8fe45---------------------------------------)

[About](https://medium.com/about?autoplay=1&source=post_page-----497fa5f8fe45---------------------------------------)

[Careers](https://medium.com/jobs-at-medium/work-at-medium-959d1a85284e?source=post_page-----497fa5f8fe45---------------------------------------)

Press

[Blog](https://blog.medium.com/?source=post_page-----497fa5f8fe45---------------------------------------)

[Privacy](https://policy.medium.com/medium-privacy-policy-f03bf92035c9?source=post_page-----497fa5f8fe45---------------------------------------)

[Rules](https://policy.medium.com/medium-rules-30e5502c4eb4?source=post_page-----497fa5f8fe45---------------------------------------)

[Terms](https://policy.medium.com/medium-terms-of-service-9db0094a1e0f?source=post_page-----497fa5f8fe45---------------------------------------)

[Text to speech](https://speechify.com/medium?source=post_page-----497fa5f8fe45---------------------------------------)