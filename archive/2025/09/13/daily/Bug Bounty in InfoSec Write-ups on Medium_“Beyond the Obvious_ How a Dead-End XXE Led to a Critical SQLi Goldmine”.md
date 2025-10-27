---
title: “Beyond the Obvious: How a Dead-End XXE Led to a Critical SQLi Goldmine”
url: https://infosecwriteups.com/beyond-the-obvious-how-a-dead-end-xxe-led-to-a-critical-sqli-goldmine-d368f5ddaadc?source=rss----7b722bfd1b8d--bug_bounty
source: Bug Bounty in InfoSec Write-ups on Medium
date: 2025-09-13
fetch_date: 2025-10-02T20:05:30.464998
---

# “Beyond the Obvious: How a Dead-End XXE Led to a Critical SQLi Goldmine”

[Sitemap](/sitemap/sitemap.xml)

[Open in app](https://rsci.app.link/?%24canonical_url=https%3A%2F%2Fmedium.com%2Fp%2Fd368f5ddaadc&%7Efeature=LoOpenInAppButton&%7Echannel=ShowPostUnderCollection&%7Estage=mobileNavBar&source=post_page---top_nav_layout_nav-----------------------------------------)

Sign up

[Sign in](https://medium.com/m/signin?operation=login&redirect=https%3A%2F%2Finfosecwriteups.com%2Fbeyond-the-obvious-how-a-dead-end-xxe-led-to-a-critical-sqli-goldmine-d368f5ddaadc&source=post_page---top_nav_layout_nav-----------------------global_nav------------------)

[Medium Logo](https://medium.com/?source=post_page---top_nav_layout_nav-----------------------------------------)

[Write](https://medium.com/m/signin?operation=register&redirect=https%3A%2F%2Fmedium.com%2Fnew-story&source=---top_nav_layout_nav-----------------------new_post_topnav------------------)

[Search](https://medium.com/search?source=post_page---top_nav_layout_nav-----------------------------------------)

Sign up

[Sign in](https://medium.com/m/signin?operation=login&redirect=https%3A%2F%2Finfosecwriteups.com%2Fbeyond-the-obvious-how-a-dead-end-xxe-led-to-a-critical-sqli-goldmine-d368f5ddaadc&source=post_page---top_nav_layout_nav-----------------------global_nav------------------)

![](https://miro.medium.com/v2/resize:fill:64:64/1*dmbNkD5D-u45r44go_cf0g.png)

[## InfoSec Write-ups](https://infosecwriteups.com/?source=post_page---publication_nav-7b722bfd1b8d-d368f5ddaadc---------------------------------------)

·

Follow publication

[![InfoSec Write-ups](https://miro.medium.com/v2/resize:fill:76:76/1*SWJxYWGZzgmBP1D0Qg_3zQ.png)](https://infosecwriteups.com/?source=post_page---post_publication_sidebar-7b722bfd1b8d-d368f5ddaadc---------------------------------------)

A collection of write-ups from the best hackers in the world on topics ranging from bug bounties and CTFs to vulnhub machines, hardware challenges and real life encounters. Subscribe to our weekly newsletter for the coolest infosec updates: <https://weekly.infosecwriteups.com/>

Follow publication

Member-only story

# “Beyond the Obvious: How a Dead-End XXE Led to a Critical SQLi Goldmine”

## From a frustrating file upload to a database of a million records, the path to a critical bug is rarely a straight line.

[![Aman Sharma](https://miro.medium.com/v2/da:true/resize:fill:64:64/0*gTsmBWudIxLcZoel)](https://amannsharmaa.medium.com/?source=post_page---byline--d368f5ddaadc---------------------------------------)

[Aman Sharma](https://amannsharmaa.medium.com/?source=post_page---byline--d368f5ddaadc---------------------------------------)

5 min read

·

Sep 11, 2025

--

2

Share

We’ve all been there. You find an endpoint that makes your hacker senses tingle. A file upload form. Your mind races with possibilities — PHP shells, malicious PDFs, the works. You fire up Burp Suite, eager to claim your bounty, only to hit a wall. The error messages are clear: it’s not a file upload. It’s something else entirely.

[FREE LINK](https://amannsharmaa.medium.com/beyond-the-obvious-how-a-dead-end-xxe-led-to-a-critical-sqli-goldmine-d368f5ddaadc?sk=6895345c5774605c7f272320121bf25e)

Press enter or click to view image in full size

![]()

This is the story of one such target. It’s a masterclass in persistence, adaptability, and why you should never, ever delete a tab in Burp.

### The First Look: A Promising Door That Slammed Shut

My journey started like many others: with subdomain enumeration. Amass, Subfinder, the usual tools. One subdomain stood out: `invoices.corp-target.com`. It hosted a single, sleek HTML form for uploading files. Jackpot, right?

I started with the classic tests. Uploading a `shell.php`. The server responded, not with a generic error, but with a verbose one: "Error: File processed as XML. Root element is missing."

--

--

2

[![InfoSec Write-ups](https://miro.medium.com/v2/resize:fill:96:96/1*SWJxYWGZzgmBP1D0Qg_3zQ.png)](https://infosecwriteups.com/?source=post_page---post_publication_info--d368f5ddaadc---------------------------------------)

[![InfoSec Write-ups](https://miro.medium.com/v2/resize:fill:128:128/1*SWJxYWGZzgmBP1D0Qg_3zQ.png)](https://infosecwriteups.com/?source=post_page---post_publication_info--d368f5ddaadc---------------------------------------)

Follow

[## Published in InfoSec Write-ups](https://infosecwriteups.com/?source=post_page---post_publication_info--d368f5ddaadc---------------------------------------)

[71K followers](/followers?source=post_page---post_publication_info--d368f5ddaadc---------------------------------------)

·[Last published 4 days ago](/how-to-find-p1-bugs-using-google-in-your-target-part-1-e37455324dc1?source=post_page---post_publication_info--d368f5ddaadc---------------------------------------)

A collection of write-ups from the best hackers in the world on topics ranging from bug bounties and CTFs to vulnhub machines, hardware challenges and real life encounters. Subscribe to our weekly newsletter for the coolest infosec updates: <https://weekly.infosecwriteups.com/>

Follow

[![Aman Sharma](https://miro.medium.com/v2/resize:fill:96:96/0*gTsmBWudIxLcZoel)](https://amannsharmaa.medium.com/?source=post_page---post_author_info--d368f5ddaadc---------------------------------------)

[![Aman Sharma](https://miro.medium.com/v2/resize:fill:128:128/0*gTsmBWudIxLcZoel)](https://amannsharmaa.medium.com/?source=post_page---post_author_info--d368f5ddaadc---------------------------------------)

[## Written by Aman Sharma](https://amannsharmaa.medium.com/?source=post_page---post_author_info--d368f5ddaadc---------------------------------------)

[739 followers](https://amannsharmaa.medium.com/followers?source=post_page---post_author_info--d368f5ddaadc---------------------------------------)

·[14 following](https://medium.com/%40amannsharmaa/following?source=post_page---post_author_info--d368f5ddaadc---------------------------------------)

| Data Enthusiast | SQL | Python | Power BI | ML | Exploring Cybersecurity & Bug Bounty | Sharing real-world analytics, dashboards & security insights.

## Responses (2)

See all responses

[Help](https://help.medium.com/hc/en-us?source=post_page-----d368f5ddaadc---------------------------------------)

[Status](https://status.medium.com/?source=post_page-----d368f5ddaadc---------------------------------------)

[About](https://medium.com/about?autoplay=1&source=post_page-----d368f5ddaadc---------------------------------------)

[Careers](https://medium.com/jobs-at-medium/work-at-medium-959d1a85284e?source=post_page-----d368f5ddaadc---------------------------------------)

Press

[Blog](https://blog.medium.com/?source=post_page-----d368f5ddaadc---------------------------------------)

[Privacy](https://policy.medium.com/medium-privacy-policy-f03bf92035c9?source=post_page-----d368f5ddaadc---------------------------------------)

[Rules](https://policy.medium.com/medium-rules-30e5502c4eb4?source=post_page-----d368f5ddaadc---------------------------------------)

[Terms](https://policy.medium.com/medium-terms-of-service-9db0094a1e0f?source=post_page-----d368f5ddaadc---------------------------------------)

[Text to speech](https://speechify.com/medium?source=post_page-----d368f5ddaadc---------------------------------------)