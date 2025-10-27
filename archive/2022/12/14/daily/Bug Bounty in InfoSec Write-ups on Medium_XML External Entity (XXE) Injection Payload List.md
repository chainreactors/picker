---
title: XML External Entity (XXE) Injection Payload List
url: https://infosecwriteups.com/xml-external-entity-xxe-injection-payload-list-937d33e5e116?source=rss----7b722bfd1b8d--bug_bounty
source: Bug Bounty in InfoSec Write-ups on Medium
date: 2022-12-14
fetch_date: 2025-10-04T01:23:33.672877
---

# XML External Entity (XXE) Injection Payload List

[Sitemap](/sitemap/sitemap.xml)

[Open in app](https://rsci.app.link/?%24canonical_url=https%3A%2F%2Fmedium.com%2Fp%2F937d33e5e116&%7Efeature=LoOpenInAppButton&%7Echannel=ShowPostUnderCollection&%7Estage=mobileNavBar&source=post_page---top_nav_layout_nav-----------------------------------------)

Sign up

[Sign in](https://medium.com/m/signin?operation=login&redirect=https%3A%2F%2Finfosecwriteups.com%2Fxml-external-entity-xxe-injection-payload-list-937d33e5e116&source=post_page---top_nav_layout_nav-----------------------global_nav------------------)

[Medium Logo](https://medium.com/?source=post_page---top_nav_layout_nav-----------------------------------------)

[Write](https://medium.com/m/signin?operation=register&redirect=https%3A%2F%2Fmedium.com%2Fnew-story&source=---top_nav_layout_nav-----------------------new_post_topnav------------------)

[Search](https://medium.com/search?source=post_page---top_nav_layout_nav-----------------------------------------)

Sign up

[Sign in](https://medium.com/m/signin?operation=login&redirect=https%3A%2F%2Finfosecwriteups.com%2Fxml-external-entity-xxe-injection-payload-list-937d33e5e116&source=post_page---top_nav_layout_nav-----------------------global_nav------------------)

![](https://miro.medium.com/v2/resize:fill:64:64/1*dmbNkD5D-u45r44go_cf0g.png)

[Mastodon](https://me.dm/%40ismailtasdelen)

[## InfoSec Write-ups](https://infosecwriteups.com/?source=post_page---publication_nav-7b722bfd1b8d-937d33e5e116---------------------------------------)

·

Follow publication

[![InfoSec Write-ups](https://miro.medium.com/v2/resize:fill:76:76/1*SWJxYWGZzgmBP1D0Qg_3zQ.png)](https://infosecwriteups.com/?source=post_page---post_publication_sidebar-7b722bfd1b8d-937d33e5e116---------------------------------------)

A collection of write-ups from the best hackers in the world on topics ranging from bug bounties and CTFs to vulnhub machines, hardware challenges and real life encounters. Subscribe to our weekly newsletter for the coolest infosec updates: <https://weekly.infosecwriteups.com/>

Follow publication

Member-only story

# XML External Entity (XXE) Injection Payload List

[![Ismail Tasdelen](https://miro.medium.com/v2/resize:fill:64:64/1*36RW_Tye9fK_Am4h2A5M3g.jpeg)](https://ismailtasdelen.medium.com/?source=post_page---byline--937d33e5e116---------------------------------------)

[Ismail Tasdelen](https://ismailtasdelen.medium.com/?source=post_page---byline--937d33e5e116---------------------------------------)

3 min read

·

Nov 23, 2019

--

2

Share

In this section, we’ll explain what XML external entity injection is, describe some common examples, explain how to find and exploit various kinds of XXE injection, and summarize how to prevent XXE injection attacks.

### What is XML external entity injection?

XML external entity injection (also known as XXE) is a web security vulnerability that allows an attacker to interfere with an application’s processing of XML data. It often allows an attacker to view files on the application server filesystem, and to interact with any backend or external systems that the application itself can access.

In some situations, an attacker can escalate an XXE attack to compromise the underlying server or other backend infrastructure, by leveraging the XXE vulnerability to perform server-side request forgery (SSRF) attacks.

![]()

There are various types of XXE attacks:

XML External Entity (XXE) Injection [Payloads](https://www.peerlyst.com/tags/payloads)

XXE: Basic XML Example

```
<!--?xml version="1.0" ?-->
<userInfo>
 <firstName>John</firstName>
 <lastName>Doe</lastName>
</userInfo>
```

XXE: Entity Example

```
<!--?xml version="1.0" ?-->
<!DOCTYPE replace [<!ENTITY example "Doe"> ]>
 <userInfo>…
```

--

--

2

[![InfoSec Write-ups](https://miro.medium.com/v2/resize:fill:96:96/1*SWJxYWGZzgmBP1D0Qg_3zQ.png)](https://infosecwriteups.com/?source=post_page---post_publication_info--937d33e5e116---------------------------------------)

[![InfoSec Write-ups](https://miro.medium.com/v2/resize:fill:128:128/1*SWJxYWGZzgmBP1D0Qg_3zQ.png)](https://infosecwriteups.com/?source=post_page---post_publication_info--937d33e5e116---------------------------------------)

Follow

[## Published in InfoSec Write-ups](https://infosecwriteups.com/?source=post_page---post_publication_info--937d33e5e116---------------------------------------)

[71K followers](/followers?source=post_page---post_publication_info--937d33e5e116---------------------------------------)

·[Last published 5 days ago](/how-to-find-p1-bugs-using-google-in-your-target-part-1-e37455324dc1?source=post_page---post_publication_info--937d33e5e116---------------------------------------)

A collection of write-ups from the best hackers in the world on topics ranging from bug bounties and CTFs to vulnhub machines, hardware challenges and real life encounters. Subscribe to our weekly newsletter for the coolest infosec updates: <https://weekly.infosecwriteups.com/>

Follow

[![Ismail Tasdelen](https://miro.medium.com/v2/resize:fill:96:96/1*36RW_Tye9fK_Am4h2A5M3g.jpeg)](https://ismailtasdelen.medium.com/?source=post_page---post_author_info--937d33e5e116---------------------------------------)

[![Ismail Tasdelen](https://miro.medium.com/v2/resize:fill:128:128/1*36RW_Tye9fK_Am4h2A5M3g.jpeg)](https://ismailtasdelen.medium.com/?source=post_page---post_author_info--937d33e5e116---------------------------------------)

[## Written by Ismail Tasdelen](https://ismailtasdelen.medium.com/?source=post_page---post_author_info--937d33e5e116---------------------------------------)

[2.6K followers](https://ismailtasdelen.medium.com/followers?source=post_page---post_author_info--937d33e5e116---------------------------------------)

·[434 following](https://medium.com/%40ismailtasdelen/following?source=post_page---post_author_info--937d33e5e116---------------------------------------)

I'm Ismail Tasdelen. I have been working in the cyber security industry for +8 years. Don't forget to follow and applaud to support my content.

## Responses (2)

See all responses

[Help](https://help.medium.com/hc/en-us?source=post_page-----937d33e5e116---------------------------------------)

[Status](https://status.medium.com/?source=post_page-----937d33e5e116---------------------------------------)

[About](https://medium.com/about?autoplay=1&source=post_page-----937d33e5e116---------------------------------------)

[Careers](https://medium.com/jobs-at-medium/work-at-medium-959d1a85284e?source=post_page-----937d33e5e116---------------------------------------)

Press

[Blog](https://blog.medium.com/?source=post_page-----937d33e5e116---------------------------------------)

[Privacy](https://policy.medium.com/medium-privacy-policy-f03bf92035c9?source=post_page-----937d33e5e116---------------------------------------)

[Rules](https://policy.medium.com/medium-rules-30e5502c4eb4?source=post_page-----937d33e5e116---------------------------------------)

[Terms](https://policy.medium.com/medium-terms-of-service-9db0094a1e0f?source=post_page-----937d33e5e116---------------------------------------)

[Text to speech](https://speechify.com/medium?source=post_page-----937d33e5e116---------------------------------------)