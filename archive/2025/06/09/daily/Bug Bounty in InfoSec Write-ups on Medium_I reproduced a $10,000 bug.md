---
title: I reproduced a $10,000 bug
url: https://infosecwriteups.com/i-reproduced-a-10-000-bug-28466603e45e?source=rss----7b722bfd1b8d--bug_bounty
source: Bug Bounty in InfoSec Write-ups on Medium
date: 2025-06-09
fetch_date: 2025-10-06T22:51:43.419104
---

# I reproduced a $10,000 bug

[Sitemap](/sitemap/sitemap.xml)

[Open in app](https://rsci.app.link/?%24canonical_url=https%3A%2F%2Fmedium.com%2Fp%2F28466603e45e&%7Efeature=LoOpenInAppButton&%7Echannel=ShowPostUnderCollection&%7Estage=mobileNavBar&source=post_page---top_nav_layout_nav-----------------------------------------)

Sign up

[Sign in](https://medium.com/m/signin?operation=login&redirect=https%3A%2F%2Finfosecwriteups.com%2Fi-reproduced-a-10-000-bug-28466603e45e&source=post_page---top_nav_layout_nav-----------------------global_nav------------------)

[Medium Logo](https://medium.com/?source=post_page---top_nav_layout_nav-----------------------------------------)

[Write](https://medium.com/m/signin?operation=register&redirect=https%3A%2F%2Fmedium.com%2Fnew-story&source=---top_nav_layout_nav-----------------------new_post_topnav------------------)

[Search](https://medium.com/search?source=post_page---top_nav_layout_nav-----------------------------------------)

Sign up

[Sign in](https://medium.com/m/signin?operation=login&redirect=https%3A%2F%2Finfosecwriteups.com%2Fi-reproduced-a-10-000-bug-28466603e45e&source=post_page---top_nav_layout_nav-----------------------global_nav------------------)

![](https://miro.medium.com/v2/resize:fill:64:64/1*dmbNkD5D-u45r44go_cf0g.png)

[Mastodon](https://me.dm/%40phoenixcatalan)

[## InfoSec Write-ups](https://infosecwriteups.com/?source=post_page---publication_nav-7b722bfd1b8d-28466603e45e---------------------------------------)

·

Follow publication

[![InfoSec Write-ups](https://miro.medium.com/v2/resize:fill:76:76/1*SWJxYWGZzgmBP1D0Qg_3zQ.png)](https://infosecwriteups.com/?source=post_page---post_publication_sidebar-7b722bfd1b8d-28466603e45e---------------------------------------)

A collection of write-ups from the best hackers in the world on topics ranging from bug bounties and CTFs to vulnhub machines, hardware challenges and real life encounters. Subscribe to our weekly newsletter for the coolest infosec updates: <https://weekly.infosecwriteups.com/>

Follow publication

Member-only story

# I reproduced a $10,000 bug

[![phoenixcatalan](https://miro.medium.com/v2/resize:fill:64:64/1*vyxgJnHAeNgHofU2nyukJA.jpeg)](https://medium.com/%40phoenixcatalan?source=post_page---byline--28466603e45e---------------------------------------)

[phoenixcatalan](https://medium.com/%40phoenixcatalan?source=post_page---byline--28466603e45e---------------------------------------)

3 min read

·

Jun 8, 2025

--

2

Share

🎭 “I wasn’t an admin… until I became one with just a JSON object.”

Press enter or click to view image in full size

![]()

*An Express server. An innocent* `isAdmin` *field. And a hacker who hijacks it through a simple* `__proto__`*. Welcome to the world of Prototype Pollution.*

### 🎬 The Setup

It all starts with a small, seemingly harmless Node.js application. Users can update their profiles via a POST request to `/update-profile`.

Under pressure, the developer uses a popular module to merge objects: `[deep-extend](https://www.npmjs.com/package/deep-extend)`. A classic choice.

But by using an **outdated, vulnerable version**, they unknowingly opened a dangerous backdoor.

### 🧨 The Vulnerability: Prototype Pollution

Here’s the issue: some JavaScript libraries allow you to inject properties into the **global object prototype**, impacting every object in the application.

To successfully exploit prototype pollution, an attacker typically needs three things:

1. **A pollution source** — Input that lets them inject arbitrary properties into prototypes (e.g., `__proto__`, `constructor`, `prototype`).
2. **A sink** — A function or behavior in the app that uses those polluted properties (like `eval`, DOM manipulation, or access checks).
3. **An exploitable gadget** — A…

--

--

2

[![InfoSec Write-ups](https://miro.medium.com/v2/resize:fill:96:96/1*SWJxYWGZzgmBP1D0Qg_3zQ.png)](https://infosecwriteups.com/?source=post_page---post_publication_info--28466603e45e---------------------------------------)

[![InfoSec Write-ups](https://miro.medium.com/v2/resize:fill:128:128/1*SWJxYWGZzgmBP1D0Qg_3zQ.png)](https://infosecwriteups.com/?source=post_page---post_publication_info--28466603e45e---------------------------------------)

Follow

[## Published in InfoSec Write-ups](https://infosecwriteups.com/?source=post_page---post_publication_info--28466603e45e---------------------------------------)

[71K followers](/followers?source=post_page---post_publication_info--28466603e45e---------------------------------------)

·[Last published 2 hours ago](/actuator-unleashed-a-guide-to-finding-and-exploiting-spring-boot-actuator-endpoints-29252dcd9d79?source=post_page---post_publication_info--28466603e45e---------------------------------------)

A collection of write-ups from the best hackers in the world on topics ranging from bug bounties and CTFs to vulnhub machines, hardware challenges and real life encounters. Subscribe to our weekly newsletter for the coolest infosec updates: <https://weekly.infosecwriteups.com/>

Follow

[![phoenixcatalan](https://miro.medium.com/v2/resize:fill:96:96/1*vyxgJnHAeNgHofU2nyukJA.jpeg)](https://medium.com/%40phoenixcatalan?source=post_page---post_author_info--28466603e45e---------------------------------------)

[![phoenixcatalan](https://miro.medium.com/v2/resize:fill:128:128/1*vyxgJnHAeNgHofU2nyukJA.jpeg)](https://medium.com/%40phoenixcatalan?source=post_page---post_author_info--28466603e45e---------------------------------------)

[## Written by phoenixcatalan](https://medium.com/%40phoenixcatalan?source=post_page---post_author_info--28466603e45e---------------------------------------)

[106 followers](https://medium.com/%40phoenixcatalan/followers?source=post_page---post_author_info--28466603e45e---------------------------------------)

·[5 following](https://medium.com/%40phoenixcatalan/following?source=post_page---post_author_info--28466603e45e---------------------------------------)

🎯 Developer with a passion for Angular & cybersecurity Guardian of web applications thanks to cybersecurity 🛡️.

## Responses (2)

See all responses

[Help](https://help.medium.com/hc/en-us?source=post_page-----28466603e45e---------------------------------------)

[Status](https://status.medium.com/?source=post_page-----28466603e45e---------------------------------------)

[About](https://medium.com/about?autoplay=1&source=post_page-----28466603e45e---------------------------------------)

[Careers](https://medium.com/jobs-at-medium/work-at-medium-959d1a85284e?source=post_page-----28466603e45e---------------------------------------)

Press

[Blog](https://blog.medium.com/?source=post_page-----28466603e45e---------------------------------------)

[Privacy](https://policy.medium.com/medium-privacy-policy-f03bf92035c9?source=post_page-----28466603e45e---------------------------------------)

[Rules](https://policy.medium.com/medium-rules-30e5502c4eb4?source=post_page-----28466603e45e---------------------------------------)

[Terms](https://policy.medium.com/medium-terms-of-service-9db0094a1e0f?source=post_page-----28466603e45e---------------------------------------)

[Text to speech](https://speechify.com/medium?source=post_page-----28466603e45e---------------------------------------)