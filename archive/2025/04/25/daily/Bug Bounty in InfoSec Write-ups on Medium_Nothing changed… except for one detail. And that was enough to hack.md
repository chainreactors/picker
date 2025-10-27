---
title: Nothing changed… except for one detail. And that was enough to hack
url: https://infosecwriteups.com/nothing-changed-except-for-one-detail-and-that-was-enough-to-hack-791f0f8bc8cb?source=rss----7b722bfd1b8d--bug_bounty
source: Bug Bounty in InfoSec Write-ups on Medium
date: 2025-04-25
fetch_date: 2025-10-06T22:04:45.304302
---

# Nothing changed… except for one detail. And that was enough to hack

[Sitemap](/sitemap/sitemap.xml)

[Open in app](https://rsci.app.link/?%24canonical_url=https%3A%2F%2Fmedium.com%2Fp%2F791f0f8bc8cb&%7Efeature=LoOpenInAppButton&%7Echannel=ShowPostUnderCollection&%7Estage=mobileNavBar&source=post_page---top_nav_layout_nav-----------------------------------------)

Sign up

[Sign in](https://medium.com/m/signin?operation=login&redirect=https%3A%2F%2Finfosecwriteups.com%2Fnothing-changed-except-for-one-detail-and-that-was-enough-to-hack-791f0f8bc8cb&source=post_page---top_nav_layout_nav-----------------------global_nav------------------)

[Medium Logo](https://medium.com/?source=post_page---top_nav_layout_nav-----------------------------------------)

[Write](https://medium.com/m/signin?operation=register&redirect=https%3A%2F%2Fmedium.com%2Fnew-story&source=---top_nav_layout_nav-----------------------new_post_topnav------------------)

[Search](https://medium.com/search?source=post_page---top_nav_layout_nav-----------------------------------------)

Sign up

[Sign in](https://medium.com/m/signin?operation=login&redirect=https%3A%2F%2Finfosecwriteups.com%2Fnothing-changed-except-for-one-detail-and-that-was-enough-to-hack-791f0f8bc8cb&source=post_page---top_nav_layout_nav-----------------------global_nav------------------)

![](https://miro.medium.com/v2/resize:fill:64:64/1*dmbNkD5D-u45r44go_cf0g.png)

[Mastodon](https://me.dm/%40phoenixcatalan)

[## InfoSec Write-ups](https://infosecwriteups.com/?source=post_page---publication_nav-7b722bfd1b8d-791f0f8bc8cb---------------------------------------)

·

Follow publication

[![InfoSec Write-ups](https://miro.medium.com/v2/resize:fill:76:76/1*SWJxYWGZzgmBP1D0Qg_3zQ.png)](https://infosecwriteups.com/?source=post_page---post_publication_sidebar-7b722bfd1b8d-791f0f8bc8cb---------------------------------------)

A collection of write-ups from the best hackers in the world on topics ranging from bug bounties and CTFs to vulnhub machines, hardware challenges and real life encounters. Subscribe to our weekly newsletter for the coolest infosec updates: <https://weekly.infosecwriteups.com/>

Follow publication

Member-only story

# Nothing changed… except for one detail. And that was enough to hack

[![phoenixcatalan](https://miro.medium.com/v2/resize:fill:64:64/1*vyxgJnHAeNgHofU2nyukJA.jpeg)](https://medium.com/%40phoenixcatalan?source=post_page---byline--791f0f8bc8cb---------------------------------------)

[phoenixcatalan](https://medium.com/%40phoenixcatalan?source=post_page---byline--791f0f8bc8cb---------------------------------------)

6 min read

·

Apr 20, 2025

--

Share

Sometimes, hacking doesn’t require any exploit… just **good observation.**

Press enter or click to view image in full size

![]()

**Every detail counts.**

### 🔐 Introduction — Authentication: An Overlooked But Critical Battleground

Some hackers tend to overlook authentication, even though it sits at the very heart of an application’s defense against malicious attacks.

It’s quite literally the front line against unauthorized access.

And yet…

A simple authentication lab from [*Portswigger*](https://portswigger.net/web-security/authentication/password-based/lab-username-enumeration-via-subtly-different-responses) took me three full hours to solve. Yes, three whole hours… for something that, in hindsight, seems painfully obvious.

That’s exactly what I want to share with you.

Because behind its seemingly simple surface, this lab taught me a **valuable lesson** :

> 🔎 *Observe before acting. Be patient. Never overlook subtle details.*

🧠 **Here’s what you’ll learn from this article:**

* 📌 **How I approached the lab**, step by step
* 🧩 **How I think through logic**, explained in detail — because **that’s what separates average hackers from the top 1%**
* 🔁 **The thought process I extracted**, which you can **apply to other authentication-related**…

--

--

[![InfoSec Write-ups](https://miro.medium.com/v2/resize:fill:96:96/1*SWJxYWGZzgmBP1D0Qg_3zQ.png)](https://infosecwriteups.com/?source=post_page---post_publication_info--791f0f8bc8cb---------------------------------------)

[![InfoSec Write-ups](https://miro.medium.com/v2/resize:fill:128:128/1*SWJxYWGZzgmBP1D0Qg_3zQ.png)](https://infosecwriteups.com/?source=post_page---post_publication_info--791f0f8bc8cb---------------------------------------)

Follow

[## Published in InfoSec Write-ups](https://infosecwriteups.com/?source=post_page---post_publication_info--791f0f8bc8cb---------------------------------------)

[71K followers](/followers?source=post_page---post_publication_info--791f0f8bc8cb---------------------------------------)

·[Last published 1 hour ago](/actuator-unleashed-a-guide-to-finding-and-exploiting-spring-boot-actuator-endpoints-29252dcd9d79?source=post_page---post_publication_info--791f0f8bc8cb---------------------------------------)

A collection of write-ups from the best hackers in the world on topics ranging from bug bounties and CTFs to vulnhub machines, hardware challenges and real life encounters. Subscribe to our weekly newsletter for the coolest infosec updates: <https://weekly.infosecwriteups.com/>

Follow

[![phoenixcatalan](https://miro.medium.com/v2/resize:fill:96:96/1*vyxgJnHAeNgHofU2nyukJA.jpeg)](https://medium.com/%40phoenixcatalan?source=post_page---post_author_info--791f0f8bc8cb---------------------------------------)

[![phoenixcatalan](https://miro.medium.com/v2/resize:fill:128:128/1*vyxgJnHAeNgHofU2nyukJA.jpeg)](https://medium.com/%40phoenixcatalan?source=post_page---post_author_info--791f0f8bc8cb---------------------------------------)

[## Written by phoenixcatalan](https://medium.com/%40phoenixcatalan?source=post_page---post_author_info--791f0f8bc8cb---------------------------------------)

[106 followers](https://medium.com/%40phoenixcatalan/followers?source=post_page---post_author_info--791f0f8bc8cb---------------------------------------)

·[5 following](https://medium.com/%40phoenixcatalan/following?source=post_page---post_author_info--791f0f8bc8cb---------------------------------------)

🎯 Developer with a passion for Angular & cybersecurity Guardian of web applications thanks to cybersecurity 🛡️.

## No responses yet

[Help](https://help.medium.com/hc/en-us?source=post_page-----791f0f8bc8cb---------------------------------------)

[Status](https://status.medium.com/?source=post_page-----791f0f8bc8cb---------------------------------------)

[About](https://medium.com/about?autoplay=1&source=post_page-----791f0f8bc8cb---------------------------------------)

[Careers](https://medium.com/jobs-at-medium/work-at-medium-959d1a85284e?source=post_page-----791f0f8bc8cb---------------------------------------)

Press

[Blog](https://blog.medium.com/?source=post_page-----791f0f8bc8cb---------------------------------------)

[Privacy](https://policy.medium.com/medium-privacy-policy-f03bf92035c9?source=post_page-----791f0f8bc8cb---------------------------------------)

[Rules](https://policy.medium.com/medium-rules-30e5502c4eb4?source=post_page-----791f0f8bc8cb---------------------------------------)

[Terms](https://policy.medium.com/medium-terms-of-service-9db0094a1e0f?source=post_page-----791f0f8bc8cb---------------------------------------)

[Text to speech](https://speechify.com/medium?source=post_page-----791f0f8bc8cb---------------------------------------)