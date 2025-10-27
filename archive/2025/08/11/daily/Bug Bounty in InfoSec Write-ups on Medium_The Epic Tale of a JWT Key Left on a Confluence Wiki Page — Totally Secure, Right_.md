---
title: The Epic Tale of a JWT Key Left on a Confluence Wiki Page — Totally Secure, Right?
url: https://infosecwriteups.com/the-epic-tale-of-a-jwt-key-left-on-a-confluence-wiki-page-totally-secure-right-141189f1d9c3?source=rss----7b722bfd1b8d--bug_bounty
source: Bug Bounty in InfoSec Write-ups on Medium
date: 2025-08-11
fetch_date: 2025-10-07T00:17:01.207472
---

# The Epic Tale of a JWT Key Left on a Confluence Wiki Page — Totally Secure, Right?

[Sitemap](/sitemap/sitemap.xml)

[Open in app](https://rsci.app.link/?%24canonical_url=https%3A%2F%2Fmedium.com%2Fp%2F141189f1d9c3&%7Efeature=LoOpenInAppButton&%7Echannel=ShowPostUnderCollection&%7Estage=mobileNavBar&source=post_page---top_nav_layout_nav-----------------------------------------)

Sign up

[Sign in](https://medium.com/m/signin?operation=login&redirect=https%3A%2F%2Finfosecwriteups.com%2Fthe-epic-tale-of-a-jwt-key-left-on-a-confluence-wiki-page-totally-secure-right-141189f1d9c3&source=post_page---top_nav_layout_nav-----------------------global_nav------------------)

[Medium Logo](https://medium.com/?source=post_page---top_nav_layout_nav-----------------------------------------)

[Write](https://medium.com/m/signin?operation=register&redirect=https%3A%2F%2Fmedium.com%2Fnew-story&source=---top_nav_layout_nav-----------------------new_post_topnav------------------)

[Search](https://medium.com/search?source=post_page---top_nav_layout_nav-----------------------------------------)

Sign up

[Sign in](https://medium.com/m/signin?operation=login&redirect=https%3A%2F%2Finfosecwriteups.com%2Fthe-epic-tale-of-a-jwt-key-left-on-a-confluence-wiki-page-totally-secure-right-141189f1d9c3&source=post_page---top_nav_layout_nav-----------------------global_nav------------------)

![](https://miro.medium.com/v2/resize:fill:64:64/1*dmbNkD5D-u45r44go_cf0g.png)

[## InfoSec Write-ups](https://infosecwriteups.com/?source=post_page---publication_nav-7b722bfd1b8d-141189f1d9c3---------------------------------------)

·

Follow publication

[![InfoSec Write-ups](https://miro.medium.com/v2/resize:fill:76:76/1*SWJxYWGZzgmBP1D0Qg_3zQ.png)](https://infosecwriteups.com/?source=post_page---post_publication_sidebar-7b722bfd1b8d-141189f1d9c3---------------------------------------)

A collection of write-ups from the best hackers in the world on topics ranging from bug bounties and CTFs to vulnhub machines, hardware challenges and real life encounters. Subscribe to our weekly newsletter for the coolest infosec updates: <https://weekly.infosecwriteups.com/>

Follow publication

Member-only story

# 📜 **The Epic Tale of a JWT Key Left on a Confluence Wiki Page — Totally Secure, Right? 🙄🔐**

[![Devansh Patel](https://miro.medium.com/v2/resize:fill:64:64/1*UbOj48VcY7qPnQSGWQhuaA.jpeg)](https://medium.com/%40devanshpatel930?source=post_page---byline--141189f1d9c3---------------------------------------)

[Devansh Patel](https://medium.com/%40devanshpatel930?source=post_page---byline--141189f1d9c3---------------------------------------)

3 min read

·

Aug 1, 2025

--

Share

**The story of where to hid JWT key 🔑… and from all places they found 🕵️‍♂️ was in the public 🌐.**

Press enter or click to view image in full size

![]()

This very evening with casual hunting on a target which was on bugbounty platform i tried a lot on it and was almost 2–3 hours and it was 1 hour past midnight, i was about to close my lappy but i thought to just try out google dorks on it so i started with the dorks………

If you can’t read furthur here is a [FREE LINK](https://medium.com/%40devanshpatel930/the-epic-tale-of-a-jwt-key-left-on-a-confluence-wiki-page-totally-secure-right-141189f1d9c3?sk=b2a9fb994fdac4f3eec5a63fa4db5c80) brother….

BTW you can check the Google dork blog

[## Dorks For Sensitive Information Disclosure Part-2

### Oh Look, Your Secrets Are on Google (Again)

medium.com](https://medium.com/%40devanshpatel930/dorks-for-sensitive-information-disclosure-part-2-4355b479d2aa?source=post_page-----141189f1d9c3---------------------------------------)

[## Dorks For Sensitive Information Disclosure

### Hello everyone, This is my 6th Blog first about Bugs and Bug bounty

medium.com](https://medium.com/%40devanshpatel930/dorks-for-sensitive-information-disclosure-31fb90ad6f21?source=post_page-----141189f1d9c3---------------------------------------)

………and it was also going for a failed attempted but then i tried a dork which was for finding Atlassian dashboards for the target but instead of that i found a dashboard which was having some text related to the target but was not of the…

--

--

[![InfoSec Write-ups](https://miro.medium.com/v2/resize:fill:96:96/1*SWJxYWGZzgmBP1D0Qg_3zQ.png)](https://infosecwriteups.com/?source=post_page---post_publication_info--141189f1d9c3---------------------------------------)

[![InfoSec Write-ups](https://miro.medium.com/v2/resize:fill:128:128/1*SWJxYWGZzgmBP1D0Qg_3zQ.png)](https://infosecwriteups.com/?source=post_page---post_publication_info--141189f1d9c3---------------------------------------)

Follow

[## Published in InfoSec Write-ups](https://infosecwriteups.com/?source=post_page---post_publication_info--141189f1d9c3---------------------------------------)

[71K followers](/followers?source=post_page---post_publication_info--141189f1d9c3---------------------------------------)

·[Last published 3 hours ago](/actuator-unleashed-a-guide-to-finding-and-exploiting-spring-boot-actuator-endpoints-29252dcd9d79?source=post_page---post_publication_info--141189f1d9c3---------------------------------------)

A collection of write-ups from the best hackers in the world on topics ranging from bug bounties and CTFs to vulnhub machines, hardware challenges and real life encounters. Subscribe to our weekly newsletter for the coolest infosec updates: <https://weekly.infosecwriteups.com/>

Follow

[![Devansh Patel](https://miro.medium.com/v2/resize:fill:96:96/1*UbOj48VcY7qPnQSGWQhuaA.jpeg)](https://medium.com/%40devanshpatel930?source=post_page---post_author_info--141189f1d9c3---------------------------------------)

[![Devansh Patel](https://miro.medium.com/v2/resize:fill:128:128/1*UbOj48VcY7qPnQSGWQhuaA.jpeg)](https://medium.com/%40devanshpatel930?source=post_page---post_author_info--141189f1d9c3---------------------------------------)

[## Written by Devansh Patel](https://medium.com/%40devanshpatel930?source=post_page---post_author_info--141189f1d9c3---------------------------------------)

[78 followers](https://medium.com/%40devanshpatel930/followers?source=post_page---post_author_info--141189f1d9c3---------------------------------------)

·[9 following](https://medium.com/%40devanshpatel930/following?source=post_page---post_author_info--141189f1d9c3---------------------------------------)

Hacking legally so companies don’t get hacked illegally. Cybersecurity analyst | Bug bounty hunter | Breaking things so others can call it ‘secure’

## No responses yet

[Help](https://help.medium.com/hc/en-us?source=post_page-----141189f1d9c3---------------------------------------)

[Status](https://status.medium.com/?source=post_page-----141189f1d9c3---------------------------------------)

[About](https://medium.com/about?autoplay=1&source=post_page-----141189f1d9c3---------------------------------------)

[Careers](https://medium.com/jobs-at-medium/work-at-medium-959d1a85284e?source=post_page-----141189f1d9c3---------------------------------------)

Press

[Blog](https://blog.medium.com/?source=post_page-----141189f1d9c3---------------------------------------)

[Privacy](https://policy.medium.com/medium-privacy-policy-f03bf92035c9?source=post_page-----141189f1d9c3---------------------------------------)

[Rules](https://policy.medium.com/medium-rules-30e5502c4eb4?source=post_page-----141189f1d9c3---------------------------------------)

[Terms](https://policy.medium.com/medium-terms-of-service-9db0094a1e0f?source=post_page-----141189f1d9c3---------------------------------------)

[Text to speech](https://speechify.com/medium?source=post_page-----141189f1d9c3---------------------------------------)