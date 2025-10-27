---
title: Pass the Hash Attack
url: https://infosecwriteups.com/pass-the-hash-attack-ddf956cf9551?source=rss----7b722bfd1b8d--bug_bounty
source: Bug Bounty in InfoSec Write-ups on Medium
date: 2022-11-22
fetch_date: 2025-10-03T23:23:09.843762
---

# Pass the Hash Attack

[Sitemap](/sitemap/sitemap.xml)

[Open in app](https://rsci.app.link/?%24canonical_url=https%3A%2F%2Fmedium.com%2Fp%2Fddf956cf9551&%7Efeature=LoOpenInAppButton&%7Echannel=ShowPostUnderCollection&%7Estage=mobileNavBar&source=post_page---top_nav_layout_nav-----------------------------------------)

Sign up

[Sign in](https://medium.com/m/signin?operation=login&redirect=https%3A%2F%2Finfosecwriteups.com%2Fpass-the-hash-attack-ddf956cf9551&source=post_page---top_nav_layout_nav-----------------------global_nav------------------)

[Medium Logo](https://medium.com/?source=post_page---top_nav_layout_nav-----------------------------------------)

[Write](https://medium.com/m/signin?operation=register&redirect=https%3A%2F%2Fmedium.com%2Fnew-story&source=---top_nav_layout_nav-----------------------new_post_topnav------------------)

[Search](https://medium.com/search?source=post_page---top_nav_layout_nav-----------------------------------------)

Sign up

[Sign in](https://medium.com/m/signin?operation=login&redirect=https%3A%2F%2Finfosecwriteups.com%2Fpass-the-hash-attack-ddf956cf9551&source=post_page---top_nav_layout_nav-----------------------global_nav------------------)

![](https://miro.medium.com/v2/resize:fill:64:64/1*dmbNkD5D-u45r44go_cf0g.png)

[## InfoSec Write-ups](https://infosecwriteups.com/?source=post_page---publication_nav-7b722bfd1b8d-ddf956cf9551---------------------------------------)

·

Follow publication

[![InfoSec Write-ups](https://miro.medium.com/v2/resize:fill:76:76/1*SWJxYWGZzgmBP1D0Qg_3zQ.png)](https://infosecwriteups.com/?source=post_page---post_publication_sidebar-7b722bfd1b8d-ddf956cf9551---------------------------------------)

A collection of write-ups from the best hackers in the world on topics ranging from bug bounties and CTFs to vulnhub machines, hardware challenges and real life encounters. Subscribe to our weekly newsletter for the coolest infosec updates: <https://weekly.infosecwriteups.com/>

Follow publication

Member-only story

# Pass the Hash Attack

[![Security Lit Limited](https://miro.medium.com/v2/resize:fill:64:64/1*yrQrISi6PlPkHrHAS2ai3g.png)](https://securitylit.medium.com/?source=post_page---byline--ddf956cf9551---------------------------------------)

[Security Lit Limited](https://securitylit.medium.com/?source=post_page---byline--ddf956cf9551---------------------------------------)

6 min read

·

Nov 21, 2022

--

Share

![]()

Photo by [Gursimrat Ganda](https://unsplash.com/%40gurysimrat?utm_source=unsplash&utm_medium=referral&utm_content=creditCopyText) on [Unsplash](https://unsplash.com/%40gurysimrat?utm_source=unsplash&utm_medium=referral&utm_content=creditCopyText)

We hear about breaches on a daily basis, and sometimes even about system compromises, so what stages does the attacker take and how does he infiltrate the entire system are unknown. Let us be clear about this.

From an attacker’s perspective, there are 5 stages involved in compromising a system/network. They are:

1. **Reconnaissance**: It is used to collect information about the system and can be both active and passive in its operation. As a result, the attacker attempts to gather as much information as possible in order to target the system as effectively as possible.
2. **Scanning and Enumeration**: The scanning is carried out by the attacker in order to identify any vulnerabilities in the system.
3. **Gaining Access:** Once an attacker has discovered the system’s vulnerabilities, he or she can use them to compromise the system.
4. **Maintaining Access / Post Exploitation:** Following exploitation, an attacker either attempts to keep his access to the system or attempts to hack another system on the network in order to obtain additional information.
5. **Clearing your tracks:** The attacker destroys all evidence of his actions so that no one can determine who compromised the system and what information was obtained.

--

--

[![InfoSec Write-ups](https://miro.medium.com/v2/resize:fill:96:96/1*SWJxYWGZzgmBP1D0Qg_3zQ.png)](https://infosecwriteups.com/?source=post_page---post_publication_info--ddf956cf9551---------------------------------------)

[![InfoSec Write-ups](https://miro.medium.com/v2/resize:fill:128:128/1*SWJxYWGZzgmBP1D0Qg_3zQ.png)](https://infosecwriteups.com/?source=post_page---post_publication_info--ddf956cf9551---------------------------------------)

Follow

[## Published in InfoSec Write-ups](https://infosecwriteups.com/?source=post_page---post_publication_info--ddf956cf9551---------------------------------------)

[71K followers](/followers?source=post_page---post_publication_info--ddf956cf9551---------------------------------------)

·[Last published 5 days ago](/how-to-find-p1-bugs-using-google-in-your-target-part-1-e37455324dc1?source=post_page---post_publication_info--ddf956cf9551---------------------------------------)

A collection of write-ups from the best hackers in the world on topics ranging from bug bounties and CTFs to vulnhub machines, hardware challenges and real life encounters. Subscribe to our weekly newsletter for the coolest infosec updates: <https://weekly.infosecwriteups.com/>

Follow

[![Security Lit Limited](https://miro.medium.com/v2/resize:fill:96:96/1*yrQrISi6PlPkHrHAS2ai3g.png)](https://securitylit.medium.com/?source=post_page---post_author_info--ddf956cf9551---------------------------------------)

[![Security Lit Limited](https://miro.medium.com/v2/resize:fill:128:128/1*yrQrISi6PlPkHrHAS2ai3g.png)](https://securitylit.medium.com/?source=post_page---post_author_info--ddf956cf9551---------------------------------------)

[## Written by Security Lit Limited](https://securitylit.medium.com/?source=post_page---post_author_info--ddf956cf9551---------------------------------------)

[2K followers](https://securitylit.medium.com/followers?source=post_page---post_author_info--ddf956cf9551---------------------------------------)

·[150 following](https://medium.com/%40securitylit/following?source=post_page---post_author_info--ddf956cf9551---------------------------------------)

<https://securitylit.com/contact>

## No responses yet

[Help](https://help.medium.com/hc/en-us?source=post_page-----ddf956cf9551---------------------------------------)

[Status](https://status.medium.com/?source=post_page-----ddf956cf9551---------------------------------------)

[About](https://medium.com/about?autoplay=1&source=post_page-----ddf956cf9551---------------------------------------)

[Careers](https://medium.com/jobs-at-medium/work-at-medium-959d1a85284e?source=post_page-----ddf956cf9551---------------------------------------)

Press

[Blog](https://blog.medium.com/?source=post_page-----ddf956cf9551---------------------------------------)

[Privacy](https://policy.medium.com/medium-privacy-policy-f03bf92035c9?source=post_page-----ddf956cf9551---------------------------------------)

[Rules](https://policy.medium.com/medium-rules-30e5502c4eb4?source=post_page-----ddf956cf9551---------------------------------------)

[Terms](https://policy.medium.com/medium-terms-of-service-9db0094a1e0f?source=post_page-----ddf956cf9551---------------------------------------)

[Text to speech](https://speechify.com/medium?source=post_page-----ddf956cf9551---------------------------------------)