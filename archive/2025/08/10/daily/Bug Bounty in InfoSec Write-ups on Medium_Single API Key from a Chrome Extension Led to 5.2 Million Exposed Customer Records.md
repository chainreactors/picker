---
title: Single API Key from a Chrome Extension Led to 5.2 Million Exposed Customer Records
url: https://infosecwriteups.com/single-api-key-from-a-chrome-extension-led-to-5-2-million-exposed-customer-records-0cc81545a7a8?source=rss----7b722bfd1b8d--bug_bounty
source: Bug Bounty in InfoSec Write-ups on Medium
date: 2025-08-10
fetch_date: 2025-10-07T00:17:43.740477
---

# Single API Key from a Chrome Extension Led to 5.2 Million Exposed Customer Records

[Sitemap](/sitemap/sitemap.xml)

[Open in app](https://rsci.app.link/?%24canonical_url=https%3A%2F%2Fmedium.com%2Fp%2F0cc81545a7a8&%7Efeature=LoOpenInAppButton&%7Echannel=ShowPostUnderCollection&%7Estage=mobileNavBar&source=post_page---top_nav_layout_nav-----------------------------------------)

Sign up

[Sign in](https://medium.com/m/signin?operation=login&redirect=https%3A%2F%2Finfosecwriteups.com%2Fsingle-api-key-from-a-chrome-extension-led-to-5-2-million-exposed-customer-records-0cc81545a7a8&source=post_page---top_nav_layout_nav-----------------------global_nav------------------)

[Medium Logo](https://medium.com/?source=post_page---top_nav_layout_nav-----------------------------------------)

[Write](https://medium.com/m/signin?operation=register&redirect=https%3A%2F%2Fmedium.com%2Fnew-story&source=---top_nav_layout_nav-----------------------new_post_topnav------------------)

[Search](https://medium.com/search?source=post_page---top_nav_layout_nav-----------------------------------------)

Sign up

[Sign in](https://medium.com/m/signin?operation=login&redirect=https%3A%2F%2Finfosecwriteups.com%2Fsingle-api-key-from-a-chrome-extension-led-to-5-2-million-exposed-customer-records-0cc81545a7a8&source=post_page---top_nav_layout_nav-----------------------global_nav------------------)

![](https://miro.medium.com/v2/resize:fill:64:64/1*dmbNkD5D-u45r44go_cf0g.png)

[## InfoSec Write-ups](https://infosecwriteups.com/?source=post_page---publication_nav-7b722bfd1b8d-0cc81545a7a8---------------------------------------)

·

Follow publication

[![InfoSec Write-ups](https://miro.medium.com/v2/resize:fill:76:76/1*SWJxYWGZzgmBP1D0Qg_3zQ.png)](https://infosecwriteups.com/?source=post_page---post_publication_sidebar-7b722bfd1b8d-0cc81545a7a8---------------------------------------)

A collection of write-ups from the best hackers in the world on topics ranging from bug bounties and CTFs to vulnhub machines, hardware challenges and real life encounters. Subscribe to our weekly newsletter for the coolest infosec updates: <https://weekly.infosecwriteups.com/>

Follow publication

Member-only story

# Single API Key from a Chrome Extension Led to 5.2 Million Exposed Customer Records

[![Erkan Kavas](https://miro.medium.com/v2/resize:fill:64:64/1*wcG-Gq6DQdotbzUlkwr0ig.jpeg)](https://medium.com/%40erkankavas?source=post_page---byline--0cc81545a7a8---------------------------------------)

[Erkan Kavas](https://medium.com/%40erkankavas?source=post_page---byline--0cc81545a7a8---------------------------------------)

3 min read

·

Aug 9, 2025

--

1

Share

> Story of an IDOR with insecure API but **responsible** **disclosure** that saved millions of users data. (Lovely 5k$)

During one of my routine explorations of public Chrome extensions, I stumbled upon a chain-owned extension belonging to a popular **Asian coffee delivery platform**. The extension, designed for quick order access, included preconfigured API endpoints and a hardcoded authorization key.

Press enter or click to view image in full size

![]()

secret coffee chain in asia. @ spoonuniversity . com

Most developers assume Chrome extensions are harmless. But once installed, they’re just ZIP archives — any resource, including JavaScript and config files, is easily accessible.

According to Google’s Chrome Web Store Developer Program Policies, extensions **must not expose sensitive credentials** or grant unauthorized access to user data. This incident clearly violated those rules, and the extension was voluntarily taken down within days of the report.

Cases like this may also highlight why Google has been moving away from Chrome Apps entirely — the end of support for Chrome Apps has been gradually rolling out, with full deprecation planned across all platforms. You can read more about that in [Google’s official announcement](https://support.google.com/chrome/a/answer/15950395?hl=en). 🥹

## Details of Incident

--

--

1

[![InfoSec Write-ups](https://miro.medium.com/v2/resize:fill:96:96/1*SWJxYWGZzgmBP1D0Qg_3zQ.png)](https://infosecwriteups.com/?source=post_page---post_publication_info--0cc81545a7a8---------------------------------------)

[![InfoSec Write-ups](https://miro.medium.com/v2/resize:fill:128:128/1*SWJxYWGZzgmBP1D0Qg_3zQ.png)](https://infosecwriteups.com/?source=post_page---post_publication_info--0cc81545a7a8---------------------------------------)

Follow

[## Published in InfoSec Write-ups](https://infosecwriteups.com/?source=post_page---post_publication_info--0cc81545a7a8---------------------------------------)

[71K followers](/followers?source=post_page---post_publication_info--0cc81545a7a8---------------------------------------)

·[Last published 3 hours ago](/actuator-unleashed-a-guide-to-finding-and-exploiting-spring-boot-actuator-endpoints-29252dcd9d79?source=post_page---post_publication_info--0cc81545a7a8---------------------------------------)

A collection of write-ups from the best hackers in the world on topics ranging from bug bounties and CTFs to vulnhub machines, hardware challenges and real life encounters. Subscribe to our weekly newsletter for the coolest infosec updates: <https://weekly.infosecwriteups.com/>

Follow

[![Erkan Kavas](https://miro.medium.com/v2/resize:fill:96:96/1*wcG-Gq6DQdotbzUlkwr0ig.jpeg)](https://medium.com/%40erkankavas?source=post_page---post_author_info--0cc81545a7a8---------------------------------------)

[![Erkan Kavas](https://miro.medium.com/v2/resize:fill:128:128/1*wcG-Gq6DQdotbzUlkwr0ig.jpeg)](https://medium.com/%40erkankavas?source=post_page---post_author_info--0cc81545a7a8---------------------------------------)

[## Written by Erkan Kavas](https://medium.com/%40erkankavas?source=post_page---post_author_info--0cc81545a7a8---------------------------------------)

[626 followers](https://medium.com/%40erkankavas/followers?source=post_page---post_author_info--0cc81545a7a8---------------------------------------)

·[685 following](https://medium.com/%40erkankavas/following?source=post_page---post_author_info--0cc81545a7a8---------------------------------------)

Cybersecurity Analyst

## Responses (1)

See all responses

[Help](https://help.medium.com/hc/en-us?source=post_page-----0cc81545a7a8---------------------------------------)

[Status](https://status.medium.com/?source=post_page-----0cc81545a7a8---------------------------------------)

[About](https://medium.com/about?autoplay=1&source=post_page-----0cc81545a7a8---------------------------------------)

[Careers](https://medium.com/jobs-at-medium/work-at-medium-959d1a85284e?source=post_page-----0cc81545a7a8---------------------------------------)

Press

[Blog](https://blog.medium.com/?source=post_page-----0cc81545a7a8---------------------------------------)

[Privacy](https://policy.medium.com/medium-privacy-policy-f03bf92035c9?source=post_page-----0cc81545a7a8---------------------------------------)

[Rules](https://policy.medium.com/medium-rules-30e5502c4eb4?source=post_page-----0cc81545a7a8---------------------------------------)

[Terms](https://policy.medium.com/medium-terms-of-service-9db0094a1e0f?source=post_page-----0cc81545a7a8---------------------------------------)

[Text to speech](https://speechify.com/medium?source=post_page-----0cc81545a7a8---------------------------------------)