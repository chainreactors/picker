---
title: Parameter Pollution: How to Hunt Silent Access Bugs
url: https://infosecwriteups.com/parameter-pollution-how-to-hunt-silent-access-bugs-922863d0498e?source=rss----7b722bfd1b8d--bug_bounty
source: Bug Bounty in InfoSec Write-ups on Medium
date: 2025-06-12
fetch_date: 2025-10-06T22:51:39.716597
---

# Parameter Pollution: How to Hunt Silent Access Bugs

[Sitemap](/sitemap/sitemap.xml)

[Open in app](https://rsci.app.link/?%24canonical_url=https%3A%2F%2Fmedium.com%2Fp%2F922863d0498e&%7Efeature=LoOpenInAppButton&%7Echannel=ShowPostUnderCollection&%7Estage=mobileNavBar&source=post_page---top_nav_layout_nav-----------------------------------------)

Sign up

[Sign in](https://medium.com/m/signin?operation=login&redirect=https%3A%2F%2Finfosecwriteups.com%2Fparameter-pollution-how-to-hunt-silent-access-bugs-922863d0498e&source=post_page---top_nav_layout_nav-----------------------global_nav------------------)

[Medium Logo](https://medium.com/?source=post_page---top_nav_layout_nav-----------------------------------------)

[Write](https://medium.com/m/signin?operation=register&redirect=https%3A%2F%2Fmedium.com%2Fnew-story&source=---top_nav_layout_nav-----------------------new_post_topnav------------------)

[Search](https://medium.com/search?source=post_page---top_nav_layout_nav-----------------------------------------)

Sign up

[Sign in](https://medium.com/m/signin?operation=login&redirect=https%3A%2F%2Finfosecwriteups.com%2Fparameter-pollution-how-to-hunt-silent-access-bugs-922863d0498e&source=post_page---top_nav_layout_nav-----------------------global_nav------------------)

![](https://miro.medium.com/v2/resize:fill:64:64/1*dmbNkD5D-u45r44go_cf0g.png)

[## InfoSec Write-ups](https://infosecwriteups.com/?source=post_page---publication_nav-7b722bfd1b8d-922863d0498e---------------------------------------)

·

Follow publication

[![InfoSec Write-ups](https://miro.medium.com/v2/resize:fill:76:76/1*SWJxYWGZzgmBP1D0Qg_3zQ.png)](https://infosecwriteups.com/?source=post_page---post_publication_sidebar-7b722bfd1b8d-922863d0498e---------------------------------------)

A collection of write-ups from the best hackers in the world on topics ranging from bug bounties and CTFs to vulnhub machines, hardware challenges and real life encounters. Subscribe to our weekly newsletter for the coolest infosec updates: <https://weekly.infosecwriteups.com/>

Follow publication

Member-only story

# Parameter Pollution: How to Hunt Silent Access Bugs

[![Monika sharma](https://miro.medium.com/v2/da:true/resize:fill:64:64/0*Tv4b4p5mb6J3IJwD)](https://medium.com/%40commanak46?source=post_page---byline--922863d0498e---------------------------------------)

[Monika sharma](https://medium.com/%40commanak46?source=post_page---byline--922863d0498e---------------------------------------)

3 min read

·

Jun 11, 2025

--

1

Share

How Overlooked URL Tricks Can Lead to Access Control Bypasses, Info Leaks, and Full Exploitation

Press enter or click to view image in full size

![]()

In the world of web application security, the smallest things often cause the biggest problems. One such subtle but dangerous vulnerability is HTTP Parameter Pollution (HPP). While XSS and SQLi often steal the spotlight, parameter pollution silently creeps into production environments, enabling privilege escalation, logic bypasses, and even critical data leaks.

Let’s dive into what parameter pollution is, how it works, real-world cases, PoCs, and how bug bounty hunters can catch this bug in the wild.

> **What Is Parameter Pollution?**

Parameter Pollution occurs when multiple HTTP parameters with the same name are sent in a request, and the server or backend handles them unexpectedly.

> **Example**

```
GET /user?role=user&role=admin
```

Depending on how the backend handles repeated parameters, the application may:

* Take the first value (user)
* Take the last value (admin)
* Concatenate them (user,admin)
* Or mishandle them entirely

This behavior is undefined by RFCs, which makes different languages, frameworks…

--

--

1

[![InfoSec Write-ups](https://miro.medium.com/v2/resize:fill:96:96/1*SWJxYWGZzgmBP1D0Qg_3zQ.png)](https://infosecwriteups.com/?source=post_page---post_publication_info--922863d0498e---------------------------------------)

[![InfoSec Write-ups](https://miro.medium.com/v2/resize:fill:128:128/1*SWJxYWGZzgmBP1D0Qg_3zQ.png)](https://infosecwriteups.com/?source=post_page---post_publication_info--922863d0498e---------------------------------------)

Follow

[## Published in InfoSec Write-ups](https://infosecwriteups.com/?source=post_page---post_publication_info--922863d0498e---------------------------------------)

[71K followers](/followers?source=post_page---post_publication_info--922863d0498e---------------------------------------)

·[Last published 2 hours ago](/actuator-unleashed-a-guide-to-finding-and-exploiting-spring-boot-actuator-endpoints-29252dcd9d79?source=post_page---post_publication_info--922863d0498e---------------------------------------)

A collection of write-ups from the best hackers in the world on topics ranging from bug bounties and CTFs to vulnhub machines, hardware challenges and real life encounters. Subscribe to our weekly newsletter for the coolest infosec updates: <https://weekly.infosecwriteups.com/>

Follow

[![Monika sharma](https://miro.medium.com/v2/resize:fill:96:96/0*Tv4b4p5mb6J3IJwD)](https://medium.com/%40commanak46?source=post_page---post_author_info--922863d0498e---------------------------------------)

[![Monika sharma](https://miro.medium.com/v2/resize:fill:128:128/0*Tv4b4p5mb6J3IJwD)](https://medium.com/%40commanak46?source=post_page---post_author_info--922863d0498e---------------------------------------)

[## Written by Monika sharma](https://medium.com/%40commanak46?source=post_page---post_author_info--922863d0498e---------------------------------------)

[2K followers](https://medium.com/%40commanak46/followers?source=post_page---post_author_info--922863d0498e---------------------------------------)

·[7 following](https://medium.com/%40commanak46/following?source=post_page---post_author_info--922863d0498e---------------------------------------)

## Responses (1)

See all responses

[Help](https://help.medium.com/hc/en-us?source=post_page-----922863d0498e---------------------------------------)

[Status](https://status.medium.com/?source=post_page-----922863d0498e---------------------------------------)

[About](https://medium.com/about?autoplay=1&source=post_page-----922863d0498e---------------------------------------)

[Careers](https://medium.com/jobs-at-medium/work-at-medium-959d1a85284e?source=post_page-----922863d0498e---------------------------------------)

Press

[Blog](https://blog.medium.com/?source=post_page-----922863d0498e---------------------------------------)

[Privacy](https://policy.medium.com/medium-privacy-policy-f03bf92035c9?source=post_page-----922863d0498e---------------------------------------)

[Rules](https://policy.medium.com/medium-rules-30e5502c4eb4?source=post_page-----922863d0498e---------------------------------------)

[Terms](https://policy.medium.com/medium-terms-of-service-9db0094a1e0f?source=post_page-----922863d0498e---------------------------------------)

[Text to speech](https://speechify.com/medium?source=post_page-----922863d0498e---------------------------------------)