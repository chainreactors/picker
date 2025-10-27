---
title: ⏱️ There were no visible errors, no hints… only the server’s hesitation told me the truth.
url: https://infosecwriteups.com/%EF%B8%8F-there-were-no-visible-errors-no-hints-only-the-servers-hesitation-told-me-the-truth-7b4987f10444?source=rss----7b722bfd1b8d--bug_bounty
source: Bug Bounty in InfoSec Write-ups on Medium
date: 2025-04-27
fetch_date: 2025-10-06T22:03:43.401067
---

# ⏱️ There were no visible errors, no hints… only the server’s hesitation told me the truth.

[Sitemap](/sitemap/sitemap.xml)

[Open in app](https://rsci.app.link/?%24canonical_url=https%3A%2F%2Fmedium.com%2Fp%2F7b4987f10444&%7Efeature=LoOpenInAppButton&%7Echannel=ShowPostUnderCollection&%7Estage=mobileNavBar&source=post_page---top_nav_layout_nav-----------------------------------------)

Sign up

[Sign in](https://medium.com/m/signin?operation=login&redirect=https%3A%2F%2Finfosecwriteups.com%2F%25EF%25B8%258F-there-were-no-visible-errors-no-hints-only-the-servers-hesitation-told-me-the-truth-7b4987f10444&source=post_page---top_nav_layout_nav-----------------------global_nav------------------)

[Medium Logo](https://medium.com/?source=post_page---top_nav_layout_nav-----------------------------------------)

[Write](https://medium.com/m/signin?operation=register&redirect=https%3A%2F%2Fmedium.com%2Fnew-story&source=---top_nav_layout_nav-----------------------new_post_topnav------------------)

[Search](https://medium.com/search?source=post_page---top_nav_layout_nav-----------------------------------------)

Sign up

[Sign in](https://medium.com/m/signin?operation=login&redirect=https%3A%2F%2Finfosecwriteups.com%2F%25EF%25B8%258F-there-were-no-visible-errors-no-hints-only-the-servers-hesitation-told-me-the-truth-7b4987f10444&source=post_page---top_nav_layout_nav-----------------------global_nav------------------)

![](https://miro.medium.com/v2/resize:fill:64:64/1*dmbNkD5D-u45r44go_cf0g.png)

[Mastodon](https://me.dm/%40phoenixcatalan)

[## InfoSec Write-ups](https://infosecwriteups.com/?source=post_page---publication_nav-7b722bfd1b8d-7b4987f10444---------------------------------------)

·

Follow publication

[![InfoSec Write-ups](https://miro.medium.com/v2/resize:fill:76:76/1*SWJxYWGZzgmBP1D0Qg_3zQ.png)](https://infosecwriteups.com/?source=post_page---post_publication_sidebar-7b722bfd1b8d-7b4987f10444---------------------------------------)

A collection of write-ups from the best hackers in the world on topics ranging from bug bounties and CTFs to vulnhub machines, hardware challenges and real life encounters. Subscribe to our weekly newsletter for the coolest infosec updates: <https://weekly.infosecwriteups.com/>

Follow publication

Member-only story

# ⏱️ There were no visible errors, no hints… only the server’s hesitation told me the truth.

[![phoenixcatalan](https://miro.medium.com/v2/resize:fill:64:64/1*vyxgJnHAeNgHofU2nyukJA.jpeg)](https://medium.com/%40phoenixcatalan?source=post_page---byline--7b4987f10444---------------------------------------)

[phoenixcatalan](https://medium.com/%40phoenixcatalan?source=post_page---byline--7b4987f10444---------------------------------------)

7 min read

·

Apr 26, 2025

--

1

Share

It didn’t scream. It whispered… and I heard it.

Press enter or click to view image in full size

![]()

**Username Enumeration**: the server’s hesitation told me the truth.

## 🚀 Introduction

T**hey say silence speaks louder than words …**

And in this lab portswigger, it was silence that broke the system.

**No flashy errors**. **No red flags**. Just a **slight delay** — a *hesitation* — like a nervous tick the server couldn’t hide.
That’s when i knew : something was off.

It didn’t tell me outright. It couldn’t. But it showed me, if I was willing to watch, to wait… to **listen**.

This is the story of how I hacked without an exploit.
Just a **clock** ⏱️. A **hunch**. And a **bit of madness**.

🧠 **Here’s what you’ll learn from this article:**

* 📌 **How I approached the lab**, step by step
* 🧩 **How I think through logic**, explained in detail — because **that’s what separates average hackers from the top 1%**
* 🔁 **The thought process I extracted**, which you can **apply to other authentication-related situations.**

### 🎯 Lab objective

The purpose of the lab is simple :

--

--

1

[![InfoSec Write-ups](https://miro.medium.com/v2/resize:fill:96:96/1*SWJxYWGZzgmBP1D0Qg_3zQ.png)](https://infosecwriteups.com/?source=post_page---post_publication_info--7b4987f10444---------------------------------------)

[![InfoSec Write-ups](https://miro.medium.com/v2/resize:fill:128:128/1*SWJxYWGZzgmBP1D0Qg_3zQ.png)](https://infosecwriteups.com/?source=post_page---post_publication_info--7b4987f10444---------------------------------------)

Follow

[## Published in InfoSec Write-ups](https://infosecwriteups.com/?source=post_page---post_publication_info--7b4987f10444---------------------------------------)

[71K followers](/followers?source=post_page---post_publication_info--7b4987f10444---------------------------------------)

·[Last published 1 hour ago](/actuator-unleashed-a-guide-to-finding-and-exploiting-spring-boot-actuator-endpoints-29252dcd9d79?source=post_page---post_publication_info--7b4987f10444---------------------------------------)

A collection of write-ups from the best hackers in the world on topics ranging from bug bounties and CTFs to vulnhub machines, hardware challenges and real life encounters. Subscribe to our weekly newsletter for the coolest infosec updates: <https://weekly.infosecwriteups.com/>

Follow

[![phoenixcatalan](https://miro.medium.com/v2/resize:fill:96:96/1*vyxgJnHAeNgHofU2nyukJA.jpeg)](https://medium.com/%40phoenixcatalan?source=post_page---post_author_info--7b4987f10444---------------------------------------)

[![phoenixcatalan](https://miro.medium.com/v2/resize:fill:128:128/1*vyxgJnHAeNgHofU2nyukJA.jpeg)](https://medium.com/%40phoenixcatalan?source=post_page---post_author_info--7b4987f10444---------------------------------------)

[## Written by phoenixcatalan](https://medium.com/%40phoenixcatalan?source=post_page---post_author_info--7b4987f10444---------------------------------------)

[106 followers](https://medium.com/%40phoenixcatalan/followers?source=post_page---post_author_info--7b4987f10444---------------------------------------)

·[5 following](https://medium.com/%40phoenixcatalan/following?source=post_page---post_author_info--7b4987f10444---------------------------------------)

🎯 Developer with a passion for Angular & cybersecurity Guardian of web applications thanks to cybersecurity 🛡️.

## Responses (1)

See all responses

[Help](https://help.medium.com/hc/en-us?source=post_page-----7b4987f10444---------------------------------------)

[Status](https://status.medium.com/?source=post_page-----7b4987f10444---------------------------------------)

[About](https://medium.com/about?autoplay=1&source=post_page-----7b4987f10444---------------------------------------)

[Careers](https://medium.com/jobs-at-medium/work-at-medium-959d1a85284e?source=post_page-----7b4987f10444---------------------------------------)

Press

[Blog](https://blog.medium.com/?source=post_page-----7b4987f10444---------------------------------------)

[Privacy](https://policy.medium.com/medium-privacy-policy-f03bf92035c9?source=post_page-----7b4987f10444---------------------------------------)

[Rules](https://policy.medium.com/medium-rules-30e5502c4eb4?source=post_page-----7b4987f10444---------------------------------------)

[Terms](https://policy.medium.com/medium-terms-of-service-9db0094a1e0f?source=post_page-----7b4987f10444---------------------------------------)

[Text to speech](https://speechify.com/medium?source=post_page-----7b4987f10444---------------------------------------)