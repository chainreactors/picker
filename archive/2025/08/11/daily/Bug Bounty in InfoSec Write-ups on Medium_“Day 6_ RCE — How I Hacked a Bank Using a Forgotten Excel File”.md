---
title: “Day 6: RCE — How I Hacked a Bank Using a Forgotten Excel File”
url: https://infosecwriteups.com/day-6-rce-how-i-hacked-a-bank-using-a-forgotten-excel-file-e0eb14758136?source=rss----7b722bfd1b8d--bug_bounty
source: Bug Bounty in InfoSec Write-ups on Medium
date: 2025-08-11
fetch_date: 2025-10-07T00:16:53.349587
---

# “Day 6: RCE — How I Hacked a Bank Using a Forgotten Excel File”

[Sitemap](/sitemap/sitemap.xml)

[Open in app](https://rsci.app.link/?%24canonical_url=https%3A%2F%2Fmedium.com%2Fp%2Fe0eb14758136&%7Efeature=LoOpenInAppButton&%7Echannel=ShowPostUnderCollection&%7Estage=mobileNavBar&source=post_page---top_nav_layout_nav-----------------------------------------)

Sign up

[Sign in](https://medium.com/m/signin?operation=login&redirect=https%3A%2F%2Finfosecwriteups.com%2Fday-6-rce-how-i-hacked-a-bank-using-a-forgotten-excel-file-e0eb14758136&source=post_page---top_nav_layout_nav-----------------------global_nav------------------)

[Medium Logo](https://medium.com/?source=post_page---top_nav_layout_nav-----------------------------------------)

[Write](https://medium.com/m/signin?operation=register&redirect=https%3A%2F%2Fmedium.com%2Fnew-story&source=---top_nav_layout_nav-----------------------new_post_topnav------------------)

[Search](https://medium.com/search?source=post_page---top_nav_layout_nav-----------------------------------------)

Sign up

[Sign in](https://medium.com/m/signin?operation=login&redirect=https%3A%2F%2Finfosecwriteups.com%2Fday-6-rce-how-i-hacked-a-bank-using-a-forgotten-excel-file-e0eb14758136&source=post_page---top_nav_layout_nav-----------------------global_nav------------------)

![](https://miro.medium.com/v2/resize:fill:64:64/1*dmbNkD5D-u45r44go_cf0g.png)

[## InfoSec Write-ups](https://infosecwriteups.com/?source=post_page---publication_nav-7b722bfd1b8d-e0eb14758136---------------------------------------)

·

Follow publication

[![InfoSec Write-ups](https://miro.medium.com/v2/resize:fill:76:76/1*SWJxYWGZzgmBP1D0Qg_3zQ.png)](https://infosecwriteups.com/?source=post_page---post_publication_sidebar-7b722bfd1b8d-e0eb14758136---------------------------------------)

A collection of write-ups from the best hackers in the world on topics ranging from bug bounties and CTFs to vulnhub machines, hardware challenges and real life encounters. Subscribe to our weekly newsletter for the coolest infosec updates: <https://weekly.infosecwriteups.com/>

Follow publication

Member-only story

# “Day 6: RCE — How I Hacked a Bank Using a Forgotten Excel File”

[![Aman Sharma](https://miro.medium.com/v2/da:true/resize:fill:64:64/0*gTsmBWudIxLcZoel)](https://amannsharmaa.medium.com/?source=post_page---byline--e0eb14758136---------------------------------------)

[Aman Sharma](https://amannsharmaa.medium.com/?source=post_page---byline--e0eb14758136---------------------------------------)

3 min read

·

Aug 9, 2025

--

2

Share

I was testing a banking portal when I stumbled upon an “Export to Excel” feature. What looked harmless turned into a full Remote Code Execution (RCE) chain that gave me root access to their internal servers. The bank paid me $200 for this critical find. Today, I’ll break down exactly how I did it, with real code snippets you can test yourself.

[free link](https://amannsharmaa.medium.com/day-6-rce-how-i-hacked-a-bank-using-a-forgotten-excel-file-e0eb14758136?sk=63a93e5a1177fdc8f2cb66383445a0bf)

![]()

## The Forgotten Attack Vector: Malicious Document Generators

Most hackers focus on web inputs. The real goldmine? Document processing (Excel, PDF, Word).

### How the Bank’s System Worked:

1. Users could export transaction logs to Excel.
2. The server used an old Apache POI library (CVE-2021–27568) to generate files.
3. No sandboxing — the parser ran with full system privileges.

## Step-by-Step Exploit (From Excel to Shell)

### Step 1: Found the Vulnerable Endpoint

Intercepted a request with Burp:

```
POST /export_transactions
{ "format": "xlsx", "data": [/* transaction data */] }
```

### Step 2: Crafted a Malicious Excel…

--

--

2

[![InfoSec Write-ups](https://miro.medium.com/v2/resize:fill:96:96/1*SWJxYWGZzgmBP1D0Qg_3zQ.png)](https://infosecwriteups.com/?source=post_page---post_publication_info--e0eb14758136---------------------------------------)

[![InfoSec Write-ups](https://miro.medium.com/v2/resize:fill:128:128/1*SWJxYWGZzgmBP1D0Qg_3zQ.png)](https://infosecwriteups.com/?source=post_page---post_publication_info--e0eb14758136---------------------------------------)

Follow

[## Published in InfoSec Write-ups](https://infosecwriteups.com/?source=post_page---post_publication_info--e0eb14758136---------------------------------------)

[71K followers](/followers?source=post_page---post_publication_info--e0eb14758136---------------------------------------)

·[Last published 3 hours ago](/actuator-unleashed-a-guide-to-finding-and-exploiting-spring-boot-actuator-endpoints-29252dcd9d79?source=post_page---post_publication_info--e0eb14758136---------------------------------------)

A collection of write-ups from the best hackers in the world on topics ranging from bug bounties and CTFs to vulnhub machines, hardware challenges and real life encounters. Subscribe to our weekly newsletter for the coolest infosec updates: <https://weekly.infosecwriteups.com/>

Follow

[![Aman Sharma](https://miro.medium.com/v2/resize:fill:96:96/0*gTsmBWudIxLcZoel)](https://amannsharmaa.medium.com/?source=post_page---post_author_info--e0eb14758136---------------------------------------)

[![Aman Sharma](https://miro.medium.com/v2/resize:fill:128:128/0*gTsmBWudIxLcZoel)](https://amannsharmaa.medium.com/?source=post_page---post_author_info--e0eb14758136---------------------------------------)

[## Written by Aman Sharma](https://amannsharmaa.medium.com/?source=post_page---post_author_info--e0eb14758136---------------------------------------)

[779 followers](https://amannsharmaa.medium.com/followers?source=post_page---post_author_info--e0eb14758136---------------------------------------)

·[14 following](https://medium.com/%40amannsharmaa/following?source=post_page---post_author_info--e0eb14758136---------------------------------------)

| Data Enthusiast | SQL | Python | Power BI | ML | Exploring Cybersecurity & Bug Bounty | Sharing real-world analytics, dashboards & security insights.

## Responses (2)

See all responses

[Help](https://help.medium.com/hc/en-us?source=post_page-----e0eb14758136---------------------------------------)

[Status](https://status.medium.com/?source=post_page-----e0eb14758136---------------------------------------)

[About](https://medium.com/about?autoplay=1&source=post_page-----e0eb14758136---------------------------------------)

[Careers](https://medium.com/jobs-at-medium/work-at-medium-959d1a85284e?source=post_page-----e0eb14758136---------------------------------------)

Press

[Blog](https://blog.medium.com/?source=post_page-----e0eb14758136---------------------------------------)

[Privacy](https://policy.medium.com/medium-privacy-policy-f03bf92035c9?source=post_page-----e0eb14758136---------------------------------------)

[Rules](https://policy.medium.com/medium-rules-30e5502c4eb4?source=post_page-----e0eb14758136---------------------------------------)

[Terms](https://policy.medium.com/medium-terms-of-service-9db0094a1e0f?source=post_page-----e0eb14758136---------------------------------------)

[Text to speech](https://speechify.com/medium?source=post_page-----e0eb14758136---------------------------------------)