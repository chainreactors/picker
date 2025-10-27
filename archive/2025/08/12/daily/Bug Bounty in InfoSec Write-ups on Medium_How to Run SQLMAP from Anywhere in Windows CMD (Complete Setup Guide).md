---
title: How to Run SQLMAP from Anywhere in Windows CMD (Complete Setup Guide)
url: https://infosecwriteups.com/how-to-run-sqlmap-from-anywhere-in-windows-cmd-complete-setup-guide-eee9d61f6303?source=rss----7b722bfd1b8d--bug_bounty
source: Bug Bounty in InfoSec Write-ups on Medium
date: 2025-08-12
fetch_date: 2025-10-07T00:17:15.321035
---

# How to Run SQLMAP from Anywhere in Windows CMD (Complete Setup Guide)

[Sitemap](/sitemap/sitemap.xml)

[Open in app](https://rsci.app.link/?%24canonical_url=https%3A%2F%2Fmedium.com%2Fp%2Feee9d61f6303&%7Efeature=LoOpenInAppButton&%7Echannel=ShowPostUnderCollection&%7Estage=mobileNavBar&source=post_page---top_nav_layout_nav-----------------------------------------)

Sign up

[Sign in](https://medium.com/m/signin?operation=login&redirect=https%3A%2F%2Finfosecwriteups.com%2Fhow-to-run-sqlmap-from-anywhere-in-windows-cmd-complete-setup-guide-eee9d61f6303&source=post_page---top_nav_layout_nav-----------------------global_nav------------------)

[Medium Logo](https://medium.com/?source=post_page---top_nav_layout_nav-----------------------------------------)

[Write](https://medium.com/m/signin?operation=register&redirect=https%3A%2F%2Fmedium.com%2Fnew-story&source=---top_nav_layout_nav-----------------------new_post_topnav------------------)

[Search](https://medium.com/search?source=post_page---top_nav_layout_nav-----------------------------------------)

Sign up

[Sign in](https://medium.com/m/signin?operation=login&redirect=https%3A%2F%2Finfosecwriteups.com%2Fhow-to-run-sqlmap-from-anywhere-in-windows-cmd-complete-setup-guide-eee9d61f6303&source=post_page---top_nav_layout_nav-----------------------global_nav------------------)

![](https://miro.medium.com/v2/resize:fill:64:64/1*dmbNkD5D-u45r44go_cf0g.png)

[## InfoSec Write-ups](https://infosecwriteups.com/?source=post_page---publication_nav-7b722bfd1b8d-eee9d61f6303---------------------------------------)

·

Follow publication

[![InfoSec Write-ups](https://miro.medium.com/v2/resize:fill:76:76/1*SWJxYWGZzgmBP1D0Qg_3zQ.png)](https://infosecwriteups.com/?source=post_page---post_publication_sidebar-7b722bfd1b8d-eee9d61f6303---------------------------------------)

A collection of write-ups from the best hackers in the world on topics ranging from bug bounties and CTFs to vulnhub machines, hardware challenges and real life encounters. Subscribe to our weekly newsletter for the coolest infosec updates: <https://weekly.infosecwriteups.com/>

Follow publication

Member-only story

# 💻 How to Run SQLMAP from Anywhere in Windows CMD (Complete Setup Guide)

[![Devansh Patel](https://miro.medium.com/v2/resize:fill:64:64/1*UbOj48VcY7qPnQSGWQhuaA.jpeg)](https://medium.com/%40devanshpatel930?source=post_page---byline--eee9d61f6303---------------------------------------)

[Devansh Patel](https://medium.com/%40devanshpatel930?source=post_page---byline--eee9d61f6303---------------------------------------)

2 min read

·

Jun 16, 2025

--

Share

Hey, you. Yeah, you.

Tired of digging into your *Sqlmap* folder like some kind of digital archaeologist just to run a simple command?

Same😭😭😭

If you’re still opening CMD, typing cd fifty times, and then finally running python sqlmap.py, I’m sorry to break it to you – you’re doing it wrong (and wasting precious hacker energy). 😤

But don’t worry – in this blog, I’ll show you how to fix that mess and make sqlmap run from literally anywhere on your Windows CMD.

Because let’s be honest – if you’re pwning databases, the least you deserve is some PATH respect.

Let’s do this. 🧑‍💻💥

⸻

### 🔧 Step 1: Download sqlmap

Head to the official [**GitHub repo**](https://github.com/sqlmapproject/sqlmap)**:**

Click on Code → Download ZIP,

OR

Use Git if you have it installed:

```
git clone --depth 1 https://github.com/sqlmapproject/sqlmap.git
```

`--depth 1` is optional; it clones only the latest commit to save time and space. You can use it without the depth option.

Once downloaded, extract the folder.

⸻

### 🗃️ Step 2: Move SQLMAP to a Permanent Location

--

--

[![InfoSec Write-ups](https://miro.medium.com/v2/resize:fill:96:96/1*SWJxYWGZzgmBP1D0Qg_3zQ.png)](https://infosecwriteups.com/?source=post_page---post_publication_info--eee9d61f6303---------------------------------------)

[![InfoSec Write-ups](https://miro.medium.com/v2/resize:fill:128:128/1*SWJxYWGZzgmBP1D0Qg_3zQ.png)](https://infosecwriteups.com/?source=post_page---post_publication_info--eee9d61f6303---------------------------------------)

Follow

[## Published in InfoSec Write-ups](https://infosecwriteups.com/?source=post_page---post_publication_info--eee9d61f6303---------------------------------------)

[71K followers](/followers?source=post_page---post_publication_info--eee9d61f6303---------------------------------------)

·[Last published 3 hours ago](/actuator-unleashed-a-guide-to-finding-and-exploiting-spring-boot-actuator-endpoints-29252dcd9d79?source=post_page---post_publication_info--eee9d61f6303---------------------------------------)

A collection of write-ups from the best hackers in the world on topics ranging from bug bounties and CTFs to vulnhub machines, hardware challenges and real life encounters. Subscribe to our weekly newsletter for the coolest infosec updates: <https://weekly.infosecwriteups.com/>

Follow

[![Devansh Patel](https://miro.medium.com/v2/resize:fill:96:96/1*UbOj48VcY7qPnQSGWQhuaA.jpeg)](https://medium.com/%40devanshpatel930?source=post_page---post_author_info--eee9d61f6303---------------------------------------)

[![Devansh Patel](https://miro.medium.com/v2/resize:fill:128:128/1*UbOj48VcY7qPnQSGWQhuaA.jpeg)](https://medium.com/%40devanshpatel930?source=post_page---post_author_info--eee9d61f6303---------------------------------------)

[## Written by Devansh Patel](https://medium.com/%40devanshpatel930?source=post_page---post_author_info--eee9d61f6303---------------------------------------)

[78 followers](https://medium.com/%40devanshpatel930/followers?source=post_page---post_author_info--eee9d61f6303---------------------------------------)

·[9 following](https://medium.com/%40devanshpatel930/following?source=post_page---post_author_info--eee9d61f6303---------------------------------------)

Hacking legally so companies don’t get hacked illegally. Cybersecurity analyst | Bug bounty hunter | Breaking things so others can call it ‘secure’

## No responses yet

[Help](https://help.medium.com/hc/en-us?source=post_page-----eee9d61f6303---------------------------------------)

[Status](https://status.medium.com/?source=post_page-----eee9d61f6303---------------------------------------)

[About](https://medium.com/about?autoplay=1&source=post_page-----eee9d61f6303---------------------------------------)

[Careers](https://medium.com/jobs-at-medium/work-at-medium-959d1a85284e?source=post_page-----eee9d61f6303---------------------------------------)

Press

[Blog](https://blog.medium.com/?source=post_page-----eee9d61f6303---------------------------------------)

[Privacy](https://policy.medium.com/medium-privacy-policy-f03bf92035c9?source=post_page-----eee9d61f6303---------------------------------------)

[Rules](https://policy.medium.com/medium-rules-30e5502c4eb4?source=post_page-----eee9d61f6303---------------------------------------)

[Terms](https://policy.medium.com/medium-terms-of-service-9db0094a1e0f?source=post_page-----eee9d61f6303---------------------------------------)

[Text to speech](https://speechify.com/medium?source=post_page-----eee9d61f6303---------------------------------------)