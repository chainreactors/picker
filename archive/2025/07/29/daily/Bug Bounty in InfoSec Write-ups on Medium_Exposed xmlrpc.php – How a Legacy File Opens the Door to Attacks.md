---
title: Exposed xmlrpc.php – How a Legacy File Opens the Door to Attacks
url: https://infosecwriteups.com/exposed-xmlrpc-php-how-a-legacy-file-opens-the-door-to-attacks-d99dd0cb9d33?source=rss----7b722bfd1b8d--bug_bounty
source: Bug Bounty in InfoSec Write-ups on Medium
date: 2025-07-29
fetch_date: 2025-10-06T23:51:57.433687
---

# Exposed xmlrpc.php – How a Legacy File Opens the Door to Attacks

[Sitemap](/sitemap/sitemap.xml)

[Open in app](https://rsci.app.link/?%24canonical_url=https%3A%2F%2Fmedium.com%2Fp%2Fd99dd0cb9d33&%7Efeature=LoOpenInAppButton&%7Echannel=ShowPostUnderCollection&%7Estage=mobileNavBar&source=post_page---top_nav_layout_nav-----------------------------------------)

Sign up

[Sign in](https://medium.com/m/signin?operation=login&redirect=https%3A%2F%2Finfosecwriteups.com%2Fexposed-xmlrpc-php-how-a-legacy-file-opens-the-door-to-attacks-d99dd0cb9d33&source=post_page---top_nav_layout_nav-----------------------global_nav------------------)

[Medium Logo](https://medium.com/?source=post_page---top_nav_layout_nav-----------------------------------------)

[Write](https://medium.com/m/signin?operation=register&redirect=https%3A%2F%2Fmedium.com%2Fnew-story&source=---top_nav_layout_nav-----------------------new_post_topnav------------------)

[Search](https://medium.com/search?source=post_page---top_nav_layout_nav-----------------------------------------)

Sign up

[Sign in](https://medium.com/m/signin?operation=login&redirect=https%3A%2F%2Finfosecwriteups.com%2Fexposed-xmlrpc-php-how-a-legacy-file-opens-the-door-to-attacks-d99dd0cb9d33&source=post_page---top_nav_layout_nav-----------------------global_nav------------------)

![](https://miro.medium.com/v2/resize:fill:64:64/1*dmbNkD5D-u45r44go_cf0g.png)

[## InfoSec Write-ups](https://infosecwriteups.com/?source=post_page---publication_nav-7b722bfd1b8d-d99dd0cb9d33---------------------------------------)

·

Follow publication

[![InfoSec Write-ups](https://miro.medium.com/v2/resize:fill:76:76/1*SWJxYWGZzgmBP1D0Qg_3zQ.png)](https://infosecwriteups.com/?source=post_page---post_publication_sidebar-7b722bfd1b8d-d99dd0cb9d33---------------------------------------)

A collection of write-ups from the best hackers in the world on topics ranging from bug bounties and CTFs to vulnhub machines, hardware challenges and real life encounters. Subscribe to our weekly newsletter for the coolest infosec updates: <https://weekly.infosecwriteups.com/>

Follow publication

Member-only story

# Exposed `xmlrpc.php` – How a Legacy File Opens the Door to Attacks

[![Ehtesham Ul Haq](https://miro.medium.com/v2/resize:fill:64:64/1*Ol6i1EKzTepUIEn8uE8KJg.png)](https://ehteshamulhaq198.medium.com/?source=post_page---byline--d99dd0cb9d33---------------------------------------)

[Ehtesham Ul Haq](https://ehteshamulhaq198.medium.com/?source=post_page---byline--d99dd0cb9d33---------------------------------------)

3 min read

·

Jul 27, 2025

--

Share

Free Article Link: [Click for free!](https://ehteshamulhaq198.medium.com/exposed-xmlrpc-php-how-a-legacy-file-opens-the-door-to-attacks-d99dd0cb9d33?sk=b7d1eb752e3a97bd5f48e346e0affdf2)

Press enter or click to view image in full size

![]()

**Hi there,**

Hope you’re doing great. In this article, I’m sharing a real-world vulnerability I discovered that relates to an often-overlooked WordPress feature — `xmlrpc.php`. While it seems harmless at first glance, when left exposed, it opens the door for brute-force attacks and even denial-of-service (DoS) exploitation.

## **Understanding xml-rpc and why it matters**

`xmlrpc.php` is a legacy feature in WordPress that allows remote access and interaction with the site through API-based requests. It was originally designed to help third-party apps or blogging platforms publish content or perform actions on WordPress.

However, if this feature is left enabled without proper restrictions, attackers can misuse it in several ways. Two major risks include:

1. **Brute-force attacks**: Attackers can repeatedly attempt username-password combinations through `xmlrpc.php`, bypassing some security plugins or login attempt limits.
2. **Denial-of-Service (DoS)**: This same endpoint can be used to amplify requests using a method called `pingback`, overwhelming the server and potentially knocking the site offline.

## **vulnerable endpoint**

--

--

[![InfoSec Write-ups](https://miro.medium.com/v2/resize:fill:96:96/1*SWJxYWGZzgmBP1D0Qg_3zQ.png)](https://infosecwriteups.com/?source=post_page---post_publication_info--d99dd0cb9d33---------------------------------------)

[![InfoSec Write-ups](https://miro.medium.com/v2/resize:fill:128:128/1*SWJxYWGZzgmBP1D0Qg_3zQ.png)](https://infosecwriteups.com/?source=post_page---post_publication_info--d99dd0cb9d33---------------------------------------)

Follow

[## Published in InfoSec Write-ups](https://infosecwriteups.com/?source=post_page---post_publication_info--d99dd0cb9d33---------------------------------------)

[71K followers](/followers?source=post_page---post_publication_info--d99dd0cb9d33---------------------------------------)

·[Last published 3 hours ago](/actuator-unleashed-a-guide-to-finding-and-exploiting-spring-boot-actuator-endpoints-29252dcd9d79?source=post_page---post_publication_info--d99dd0cb9d33---------------------------------------)

A collection of write-ups from the best hackers in the world on topics ranging from bug bounties and CTFs to vulnhub machines, hardware challenges and real life encounters. Subscribe to our weekly newsletter for the coolest infosec updates: <https://weekly.infosecwriteups.com/>

Follow

[![Ehtesham Ul Haq](https://miro.medium.com/v2/resize:fill:96:96/1*Ol6i1EKzTepUIEn8uE8KJg.png)](https://ehteshamulhaq198.medium.com/?source=post_page---post_author_info--d99dd0cb9d33---------------------------------------)

[![Ehtesham Ul Haq](https://miro.medium.com/v2/resize:fill:128:128/1*Ol6i1EKzTepUIEn8uE8KJg.png)](https://ehteshamulhaq198.medium.com/?source=post_page---post_author_info--d99dd0cb9d33---------------------------------------)

[## Written by Ehtesham Ul Haq](https://ehteshamulhaq198.medium.com/?source=post_page---post_author_info--d99dd0cb9d33---------------------------------------)

[520 followers](https://ehteshamulhaq198.medium.com/followers?source=post_page---post_author_info--d99dd0cb9d33---------------------------------------)

·[99 following](https://medium.com/%40ehteshamulhaq198/following?source=post_page---post_author_info--d99dd0cb9d33---------------------------------------)

Penetration Tester & Bug Bounty Hunter focused on finding vulnerabilities and helping organizations stay ahead of cyber threats.

## No responses yet

[Help](https://help.medium.com/hc/en-us?source=post_page-----d99dd0cb9d33---------------------------------------)

[Status](https://status.medium.com/?source=post_page-----d99dd0cb9d33---------------------------------------)

[About](https://medium.com/about?autoplay=1&source=post_page-----d99dd0cb9d33---------------------------------------)

[Careers](https://medium.com/jobs-at-medium/work-at-medium-959d1a85284e?source=post_page-----d99dd0cb9d33---------------------------------------)

Press

[Blog](https://blog.medium.com/?source=post_page-----d99dd0cb9d33---------------------------------------)

[Privacy](https://policy.medium.com/medium-privacy-policy-f03bf92035c9?source=post_page-----d99dd0cb9d33---------------------------------------)

[Rules](https://policy.medium.com/medium-rules-30e5502c4eb4?source=post_page-----d99dd0cb9d33---------------------------------------)

[Terms](https://policy.medium.com/medium-terms-of-service-9db0094a1e0f?source=post_page-----d99dd0cb9d33---------------------------------------)

[Text to speech](https://speechify.com/medium?source=post_page-----d99dd0cb9d33---------------------------------------)