---
title: Disallowed but Discoverable: The Hacker’s robots.txt Playbook
url: https://infosecwriteups.com/disallowed-but-discoverable-the-hackers-robots-txt-playbook-73dca570f23e?source=rss----7b722bfd1b8d--bug_bounty
source: Bug Bounty in InfoSec Write-ups on Medium
date: 2024-11-24
fetch_date: 2025-10-06T19:14:53.653572
---

# Disallowed but Discoverable: The Hacker’s robots.txt Playbook

[Sitemap](/sitemap/sitemap.xml)

[Open in app](https://rsci.app.link/?%24canonical_url=https%3A%2F%2Fmedium.com%2Fp%2F73dca570f23e&%7Efeature=LoOpenInAppButton&%7Echannel=ShowPostUnderCollection&%7Estage=mobileNavBar&source=post_page---top_nav_layout_nav-----------------------------------------)

Sign up

[Sign in](https://medium.com/m/signin?operation=login&redirect=https%3A%2F%2Finfosecwriteups.com%2Fdisallowed-but-discoverable-the-hackers-robots-txt-playbook-73dca570f23e&source=post_page---top_nav_layout_nav-----------------------global_nav------------------)

[Medium Logo](https://medium.com/?source=post_page---top_nav_layout_nav-----------------------------------------)

[Write](https://medium.com/m/signin?operation=register&redirect=https%3A%2F%2Fmedium.com%2Fnew-story&source=---top_nav_layout_nav-----------------------new_post_topnav------------------)

[Search](https://medium.com/search?source=post_page---top_nav_layout_nav-----------------------------------------)

Sign up

[Sign in](https://medium.com/m/signin?operation=login&redirect=https%3A%2F%2Finfosecwriteups.com%2Fdisallowed-but-discoverable-the-hackers-robots-txt-playbook-73dca570f23e&source=post_page---top_nav_layout_nav-----------------------global_nav------------------)

![](https://miro.medium.com/v2/resize:fill:64:64/1*dmbNkD5D-u45r44go_cf0g.png)

[Mastodon](https://me.dm/%40myselfakash20)

[## InfoSec Write-ups](https://infosecwriteups.com/?source=post_page---publication_nav-7b722bfd1b8d-73dca570f23e---------------------------------------)

·

Follow publication

[![InfoSec Write-ups](https://miro.medium.com/v2/resize:fill:76:76/1*SWJxYWGZzgmBP1D0Qg_3zQ.png)](https://infosecwriteups.com/?source=post_page---post_publication_sidebar-7b722bfd1b8d-73dca570f23e---------------------------------------)

A collection of write-ups from the best hackers in the world on topics ranging from bug bounties and CTFs to vulnhub machines, hardware challenges and real life encounters. Subscribe to our weekly newsletter for the coolest infosec updates: <https://weekly.infosecwriteups.com/>

Follow publication

Member-only story

# Disallowed but Discoverable: The Hacker’s robots.txt Playbook

[![Akash Ghosh](https://miro.medium.com/v2/resize:fill:64:64/1*xbttpz6vUW1KE6Wd1M2OEg.png)](https://myselfakash20.medium.com/?source=post_page---byline--73dca570f23e---------------------------------------)

[Akash Ghosh](https://myselfakash20.medium.com/?source=post_page---byline--73dca570f23e---------------------------------------)

3 min read

·

Nov 23, 2024

--

Share

Press enter or click to view image in full size

![]()

Let's Gooooooo

***Ever felt like a pirate on the hunt for hidden treasure? 🏴‍☠️ As bug bounty hunters, we’re all about uncovering the secrets others try to bury. But what if I told you the most overlooked and underestimated file on any website — the humble*** `robots.txt`***—could be your treasure map?***

*That’s right! This seemingly innocuous file, designed to guide search engine crawlers, often holds breadcrumbs leading to sensitive directories, confidential endpoints, or even forgotten functionality. While most see it as harmless, seasoned hackers know it can be a goldmine for reconnaissance.*

**In this guide, I’ll show you how to go beyond the basics of** `robots.txt`**, leveraging its full potential to find vulnerabilities, access restricted areas, and report impactful bugs. By the end, you'll have the tools and mindset to turn this unassuming file into a valuable ally in your bug bounty journey.**

> Outline of the Story:

### 1. What is robots.txt?

* A brief explanation of `robots.txt`:

> It’s a plain text file in the root directory of a website that tells search engine bots which parts of the site they can and cannot crawl.

* Examples of typical entries:

```
User-agent: *
Disallow…
```

--

--

[![InfoSec Write-ups](https://miro.medium.com/v2/resize:fill:96:96/1*SWJxYWGZzgmBP1D0Qg_3zQ.png)](https://infosecwriteups.com/?source=post_page---post_publication_info--73dca570f23e---------------------------------------)

[![InfoSec Write-ups](https://miro.medium.com/v2/resize:fill:128:128/1*SWJxYWGZzgmBP1D0Qg_3zQ.png)](https://infosecwriteups.com/?source=post_page---post_publication_info--73dca570f23e---------------------------------------)

Follow

[## Published in InfoSec Write-ups](https://infosecwriteups.com/?source=post_page---post_publication_info--73dca570f23e---------------------------------------)

[71K followers](/followers?source=post_page---post_publication_info--73dca570f23e---------------------------------------)

·[Last published 4 hours ago](/baby-dfc2547dc387?source=post_page---post_publication_info--73dca570f23e---------------------------------------)

A collection of write-ups from the best hackers in the world on topics ranging from bug bounties and CTFs to vulnhub machines, hardware challenges and real life encounters. Subscribe to our weekly newsletter for the coolest infosec updates: <https://weekly.infosecwriteups.com/>

Follow

[![Akash Ghosh](https://miro.medium.com/v2/resize:fill:96:96/1*xbttpz6vUW1KE6Wd1M2OEg.png)](https://myselfakash20.medium.com/?source=post_page---post_author_info--73dca570f23e---------------------------------------)

[![Akash Ghosh](https://miro.medium.com/v2/resize:fill:128:128/1*xbttpz6vUW1KE6Wd1M2OEg.png)](https://myselfakash20.medium.com/?source=post_page---post_author_info--73dca570f23e---------------------------------------)

[## Written by Akash Ghosh](https://myselfakash20.medium.com/?source=post_page---post_author_info--73dca570f23e---------------------------------------)

[658 followers](https://myselfakash20.medium.com/followers?source=post_page---post_author_info--73dca570f23e---------------------------------------)

·[2 following](https://medium.com/%40myselfakash20/following?source=post_page---post_author_info--73dca570f23e---------------------------------------)

Akash Ghosh|Ethical Hacker | Cybersecurity Expert | Web & Mobile Security Expert

## No responses yet

[Help](https://help.medium.com/hc/en-us?source=post_page-----73dca570f23e---------------------------------------)

[Status](https://status.medium.com/?source=post_page-----73dca570f23e---------------------------------------)

[About](https://medium.com/about?autoplay=1&source=post_page-----73dca570f23e---------------------------------------)

[Careers](https://medium.com/jobs-at-medium/work-at-medium-959d1a85284e?source=post_page-----73dca570f23e---------------------------------------)

Press

[Blog](https://blog.medium.com/?source=post_page-----73dca570f23e---------------------------------------)

[Privacy](https://policy.medium.com/medium-privacy-policy-f03bf92035c9?source=post_page-----73dca570f23e---------------------------------------)

[Rules](https://policy.medium.com/medium-rules-30e5502c4eb4?source=post_page-----73dca570f23e---------------------------------------)

[Terms](https://policy.medium.com/medium-terms-of-service-9db0094a1e0f?source=post_page-----73dca570f23e---------------------------------------)

[Text to speech](https://speechify.com/medium?source=post_page-----73dca570f23e---------------------------------------)