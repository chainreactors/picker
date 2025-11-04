---
title: Understanding JSON Web Token (JWT) Security
url: https://infosecwriteups.com/understanding-json-web-token-jwt-security-48c3a9cc96f2?source=rss----7b722bfd1b8d--bug_bounty
source: Bug Bounty in InfoSec Write-ups on Medium
date: 2025-11-03
fetch_date: 2025-11-04T03:09:41.028293
---

# Understanding JSON Web Token (JWT) Security

[Sitemap](/sitemap/sitemap.xml)

[Open in app](https://rsci.app.link/?%24canonical_url=https%3A%2F%2Fmedium.com%2Fp%2F48c3a9cc96f2&%7Efeature=LoOpenInAppButton&%7Echannel=ShowPostUnderCollection&%7Estage=mobileNavBar&source=post_page---top_nav_layout_nav-----------------------------------------)

Sign up

[Sign in](https://medium.com/m/signin?operation=login&redirect=https%3A%2F%2Finfosecwriteups.com%2Funderstanding-json-web-token-jwt-security-48c3a9cc96f2&source=post_page---top_nav_layout_nav-----------------------global_nav------------------)

[Medium Logo](https://medium.com/?source=post_page---top_nav_layout_nav-----------------------------------------)

[Write](https://medium.com/m/signin?operation=register&redirect=https%3A%2F%2Fmedium.com%2Fnew-story&source=---top_nav_layout_nav-----------------------new_post_topnav------------------)

[Search](https://medium.com/search?source=post_page---top_nav_layout_nav-----------------------------------------)

Sign up

[Sign in](https://medium.com/m/signin?operation=login&redirect=https%3A%2F%2Finfosecwriteups.com%2Funderstanding-json-web-token-jwt-security-48c3a9cc96f2&source=post_page---top_nav_layout_nav-----------------------global_nav------------------)

![](https://miro.medium.com/v2/resize:fill:64:64/1*dmbNkD5D-u45r44go_cf0g.png)

[## InfoSec Write-ups](https://infosecwriteups.com/?source=post_page---publication_nav-7b722bfd1b8d-48c3a9cc96f2---------------------------------------)

·

Follow publication

[![InfoSec Write-ups](https://miro.medium.com/v2/resize:fill:76:76/1*SWJxYWGZzgmBP1D0Qg_3zQ.png)](https://infosecwriteups.com/?source=post_page---post_publication_sidebar-7b722bfd1b8d-48c3a9cc96f2---------------------------------------)

A collection of write-ups from the best hackers in the world on topics ranging from bug bounties and CTFs to vulnhub machines, hardware challenges and real life encounters. Subscribe to our weekly newsletter for the coolest infosec updates: <https://weekly.infosecwriteups.com/>

Follow publication

Member-only story

# Understanding JSON Web Token (JWT) Security

[![hackerdevil](https://miro.medium.com/v2/resize:fill:64:64/1*sVg7V08AyUPzAzA_Hx-UYg.png)](https://devilwrites.medium.com/?source=post_page---byline--48c3a9cc96f2---------------------------------------)

[hackerdevil](https://devilwrites.medium.com/?source=post_page---byline--48c3a9cc96f2---------------------------------------)

6 min read

·

Oct 22, 2025

--

Share

From Basics to Breaking Authentication

JSON Web Tokens (JWTs) have become the backbone of modern authentication systems. If you’re a penetration tester or bug bounty hunter, understanding JWT vulnerabilities isn’t just useful; it’s essential. This blog will walk you through the very basics that you need to know about JWT security testing.

Press enter or click to view image in full size

![]()

JWT Security

## **What is JWT? A quick refresher**

**JWT is a standard** as specified in RFC 7519, which can be implemented in either of three ways: **JSON Web Signature (JWS)** or **JSON Web Encryption (JWE),** or **Unsecured JWT**. **JWS** is widely and majorly used where it preserves the **integrity** of the claims made by using the **signature,** while in **JWE**, it ensures **confidentiality** by **encrypting** the entire content, which is only accessible to parties with the decryption keys. In an **unsecured JWT** implementation, ‘alg’ is set to none.

JSON Web Token (JWT) consists of 3 parts: JOSE (JSON Object Signing and Encryption) header, Payload, and Signature.

A JWT = `HEADER.PAYLOAD.SIGNATURE` (base64url parts).

**> Header:** tells alg (HS256, RS256), typ, kid.

**> Payload:** claims (sub, iss, aud, exp, role…). Not encrypted-anyone can read it. The payload of a JSON Web Token (JWT) contains **claims**, which store information…

--

--

[![InfoSec Write-ups](https://miro.medium.com/v2/resize:fill:96:96/1*SWJxYWGZzgmBP1D0Qg_3zQ.png)](https://infosecwriteups.com/?source=post_page---post_publication_info--48c3a9cc96f2---------------------------------------)

[![InfoSec Write-ups](https://miro.medium.com/v2/resize:fill:128:128/1*SWJxYWGZzgmBP1D0Qg_3zQ.png)](https://infosecwriteups.com/?source=post_page---post_publication_info--48c3a9cc96f2---------------------------------------)

Follow

[## Published in InfoSec Write-ups](https://infosecwriteups.com/?source=post_page---post_publication_info--48c3a9cc96f2---------------------------------------)

[73K followers](/followers?source=post_page---post_publication_info--48c3a9cc96f2---------------------------------------)

·[Last published 2 days ago](/how-i-cracked-the-ejpt-exam-in-just-3-hours-with-a-score-of-85-badc569e68ba?source=post_page---post_publication_info--48c3a9cc96f2---------------------------------------)

A collection of write-ups from the best hackers in the world on topics ranging from bug bounties and CTFs to vulnhub machines, hardware challenges and real life encounters. Subscribe to our weekly newsletter for the coolest infosec updates: <https://weekly.infosecwriteups.com/>

Follow

[![hackerdevil](https://miro.medium.com/v2/resize:fill:96:96/1*sVg7V08AyUPzAzA_Hx-UYg.png)](https://devilwrites.medium.com/?source=post_page---post_author_info--48c3a9cc96f2---------------------------------------)

[![hackerdevil](https://miro.medium.com/v2/resize:fill:128:128/1*sVg7V08AyUPzAzA_Hx-UYg.png)](https://devilwrites.medium.com/?source=post_page---post_author_info--48c3a9cc96f2---------------------------------------)

[## Written by hackerdevil](https://devilwrites.medium.com/?source=post_page---post_author_info--48c3a9cc96f2---------------------------------------)

[194 followers](https://devilwrites.medium.com/followers?source=post_page---post_author_info--48c3a9cc96f2---------------------------------------)

·[52 following](https://medium.com/%40devilwrites/following?source=post_page---post_author_info--48c3a9cc96f2---------------------------------------)

CRTP • CEH • VAPT • Foodie • Infosec Writer

## No responses yet

[Help](https://help.medium.com/hc/en-us?source=post_page-----48c3a9cc96f2---------------------------------------)

[Status](https://status.medium.com/?source=post_page-----48c3a9cc96f2---------------------------------------)

[About](https://medium.com/about?autoplay=1&source=post_page-----48c3a9cc96f2---------------------------------------)

[Careers](https://medium.com/jobs-at-medium/work-at-medium-959d1a85284e?source=post_page-----48c3a9cc96f2---------------------------------------)

Press

[Blog](https://blog.medium.com/?source=post_page-----48c3a9cc96f2---------------------------------------)

[Privacy](https://policy.medium.com/medium-privacy-policy-f03bf92035c9?source=post_page-----48c3a9cc96f2---------------------------------------)

[Rules](https://policy.medium.com/medium-rules-30e5502c4eb4?source=post_page-----48c3a9cc96f2---------------------------------------)

[Terms](https://policy.medium.com/medium-terms-of-service-9db0094a1e0f?source=post_page-----48c3a9cc96f2---------------------------------------)

[Text to speech](https://speechify.com/medium?source=post_page-----48c3a9cc96f2---------------------------------------)