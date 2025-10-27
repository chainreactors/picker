---
title: Reflected XSS with Some SVG Markup Allowed
url: https://infosecwriteups.com/reflected-xss-with-some-svg-markup-allowed-65e24224d819?source=rss----7b722bfd1b8d--bug_bounty
source: Bug Bounty in InfoSec Write-ups on Medium
date: 2025-08-05
fetch_date: 2025-10-07T00:47:37.210582
---

# Reflected XSS with Some SVG Markup Allowed

[Sitemap](/sitemap/sitemap.xml)

[Open in app](https://rsci.app.link/?%24canonical_url=https%3A%2F%2Fmedium.com%2Fp%2F65e24224d819&%7Efeature=LoOpenInAppButton&%7Echannel=ShowPostUnderCollection&%7Estage=mobileNavBar&source=post_page---top_nav_layout_nav-----------------------------------------)

Sign up

[Sign in](https://medium.com/m/signin?operation=login&redirect=https%3A%2F%2Finfosecwriteups.com%2Freflected-xss-with-some-svg-markup-allowed-65e24224d819&source=post_page---top_nav_layout_nav-----------------------global_nav------------------)

[Medium Logo](https://medium.com/?source=post_page---top_nav_layout_nav-----------------------------------------)

[Write](https://medium.com/m/signin?operation=register&redirect=https%3A%2F%2Fmedium.com%2Fnew-story&source=---top_nav_layout_nav-----------------------new_post_topnav------------------)

[Search](https://medium.com/search?source=post_page---top_nav_layout_nav-----------------------------------------)

Sign up

[Sign in](https://medium.com/m/signin?operation=login&redirect=https%3A%2F%2Finfosecwriteups.com%2Freflected-xss-with-some-svg-markup-allowed-65e24224d819&source=post_page---top_nav_layout_nav-----------------------global_nav------------------)

![](https://miro.medium.com/v2/resize:fill:64:64/1*dmbNkD5D-u45r44go_cf0g.png)

[## InfoSec Write-ups](https://infosecwriteups.com/?source=post_page---publication_nav-7b722bfd1b8d-65e24224d819---------------------------------------)

·

Follow publication

[![InfoSec Write-ups](https://miro.medium.com/v2/resize:fill:76:76/1*SWJxYWGZzgmBP1D0Qg_3zQ.png)](https://infosecwriteups.com/?source=post_page---post_publication_sidebar-7b722bfd1b8d-65e24224d819---------------------------------------)

A collection of write-ups from the best hackers in the world on topics ranging from bug bounties and CTFs to vulnhub machines, hardware challenges and real life encounters. Subscribe to our weekly newsletter for the coolest infosec updates: <https://weekly.infosecwriteups.com/>

Follow publication

Member-only story

# Reflected XSS with Some SVG Markup Allowed

[![Bash Overflow](https://miro.medium.com/v2/resize:fill:64:64/1*JoM8_WC11wsYSOwkJ1oqxQ.png)](https://bashoverflow.com/?source=post_page---byline--65e24224d819---------------------------------------)

[Bash Overflow](https://bashoverflow.com/?source=post_page---byline--65e24224d819---------------------------------------)

4 min read

·

Aug 4, 2025

--

Share

**Learn how reflected cross-site scripting (XSS) vulnerabilities still succeed in filtered environments using SVG tags**.

🔓 [**Free Link**](https://bashoverflow.com/65e24224d819?sk=cf2f7866571fea3bd5d5d23c1f41be0a)

Press enter or click to view image in full size

![Reflected XSS with Some SVG Markup Allowed — Bashoverflow Medium]()

Reflected XSS with Some SVG Markup Allowed

> **Disclaimer:**
> The techniques described in this document are intended solely for ethical use and educational purposes. Unauthorized use of these methods outside approved environments is strictly prohibited, as it is illegal, unethical, and may lead to severe consequences.
>
> It is crucial to act responsibly, comply with all applicable laws, and adhere to established ethical guidelines. Any activity that exploits security vulnerabilities or compromises the safety, privacy, or integrity of others is strictly forbidden.

## Table of Contents

1. [**Summary of the Vulnerability**](#af5f)
2. [**Steps to Reproduce & Proof of Concept (PoC)**](#c672)
3. [**Impact**](#9036)

## Summary of the Vulnerability

In this scenario, the web application is vulnerable to Reflected XSS, where untrusted input is reflected directly in the response without proper sanitization. The key twist? The application tries to block common HTML tags like `<script>`, `<img>`, and `<iframe>`, but some SVG markup is still allowed.

--

--

[![InfoSec Write-ups](https://miro.medium.com/v2/resize:fill:96:96/1*SWJxYWGZzgmBP1D0Qg_3zQ.png)](https://infosecwriteups.com/?source=post_page---post_publication_info--65e24224d819---------------------------------------)

[![InfoSec Write-ups](https://miro.medium.com/v2/resize:fill:128:128/1*SWJxYWGZzgmBP1D0Qg_3zQ.png)](https://infosecwriteups.com/?source=post_page---post_publication_info--65e24224d819---------------------------------------)

Follow

[## Published in InfoSec Write-ups](https://infosecwriteups.com/?source=post_page---post_publication_info--65e24224d819---------------------------------------)

[71K followers](/followers?source=post_page---post_publication_info--65e24224d819---------------------------------------)

·[Last published 4 hours ago](/actuator-unleashed-a-guide-to-finding-and-exploiting-spring-boot-actuator-endpoints-29252dcd9d79?source=post_page---post_publication_info--65e24224d819---------------------------------------)

A collection of write-ups from the best hackers in the world on topics ranging from bug bounties and CTFs to vulnhub machines, hardware challenges and real life encounters. Subscribe to our weekly newsletter for the coolest infosec updates: <https://weekly.infosecwriteups.com/>

Follow

[![Bash Overflow](https://miro.medium.com/v2/resize:fill:96:96/1*JoM8_WC11wsYSOwkJ1oqxQ.png)](https://bashoverflow.com/?source=post_page---post_author_info--65e24224d819---------------------------------------)

[![Bash Overflow](https://miro.medium.com/v2/resize:fill:128:128/1*JoM8_WC11wsYSOwkJ1oqxQ.png)](https://bashoverflow.com/?source=post_page---post_author_info--65e24224d819---------------------------------------)

[## Written by Bash Overflow](https://bashoverflow.com/?source=post_page---post_author_info--65e24224d819---------------------------------------)

[150 followers](https://bashoverflow.com/followers?source=post_page---post_author_info--65e24224d819---------------------------------------)

·[11 following](https://medium.com/%40bashoverflow/following?source=post_page---post_author_info--65e24224d819---------------------------------------)

Cybersecurity Enthusiast | Sharing insights through some writeups | Passionate about advancing knowledge in the field of cybersecurity

## No responses yet

[Help](https://help.medium.com/hc/en-us?source=post_page-----65e24224d819---------------------------------------)

[Status](https://status.medium.com/?source=post_page-----65e24224d819---------------------------------------)

[About](https://medium.com/about?autoplay=1&source=post_page-----65e24224d819---------------------------------------)

[Careers](https://medium.com/jobs-at-medium/work-at-medium-959d1a85284e?source=post_page-----65e24224d819---------------------------------------)

Press

[Blog](https://blog.medium.com/?source=post_page-----65e24224d819---------------------------------------)

[Privacy](https://policy.medium.com/medium-privacy-policy-f03bf92035c9?source=post_page-----65e24224d819---------------------------------------)

[Rules](https://policy.medium.com/medium-rules-30e5502c4eb4?source=post_page-----65e24224d819---------------------------------------)

[Terms](https://policy.medium.com/medium-terms-of-service-9db0094a1e0f?source=post_page-----65e24224d819---------------------------------------)

[Text to speech](https://speechify.com/medium?source=post_page-----65e24224d819---------------------------------------)