---
title: Dom-Based Xss
url: https://infosecwriteups.com/dom-based-xss-fa913b66b09b?source=rss----7b722bfd1b8d--bug_bounty
source: Bug Bounty in InfoSec Write-ups on Medium
date: 2025-07-25
fetch_date: 2025-10-06T23:28:09.668300
---

# Dom-Based Xss

[Sitemap](/sitemap/sitemap.xml)

[Open in app](https://rsci.app.link/?%24canonical_url=https%3A%2F%2Fmedium.com%2Fp%2Ffa913b66b09b&%7Efeature=LoOpenInAppButton&%7Echannel=ShowPostUnderCollection&%7Estage=mobileNavBar&source=post_page---top_nav_layout_nav-----------------------------------------)

Sign up

[Sign in](https://medium.com/m/signin?operation=login&redirect=https%3A%2F%2Finfosecwriteups.com%2Fdom-based-xss-fa913b66b09b&source=post_page---top_nav_layout_nav-----------------------global_nav------------------)

[Medium Logo](https://medium.com/?source=post_page---top_nav_layout_nav-----------------------------------------)

[Write](https://medium.com/m/signin?operation=register&redirect=https%3A%2F%2Fmedium.com%2Fnew-story&source=---top_nav_layout_nav-----------------------new_post_topnav------------------)

[Search](https://medium.com/search?source=post_page---top_nav_layout_nav-----------------------------------------)

Sign up

[Sign in](https://medium.com/m/signin?operation=login&redirect=https%3A%2F%2Finfosecwriteups.com%2Fdom-based-xss-fa913b66b09b&source=post_page---top_nav_layout_nav-----------------------global_nav------------------)

![](https://miro.medium.com/v2/resize:fill:64:64/1*dmbNkD5D-u45r44go_cf0g.png)

[## InfoSec Write-ups](https://infosecwriteups.com/?source=post_page---publication_nav-7b722bfd1b8d-fa913b66b09b---------------------------------------)

·

Follow publication

[![InfoSec Write-ups](https://miro.medium.com/v2/resize:fill:76:76/1*SWJxYWGZzgmBP1D0Qg_3zQ.png)](https://infosecwriteups.com/?source=post_page---post_publication_sidebar-7b722bfd1b8d-fa913b66b09b---------------------------------------)

A collection of write-ups from the best hackers in the world on topics ranging from bug bounties and CTFs to vulnhub machines, hardware challenges and real life encounters. Subscribe to our weekly newsletter for the coolest infosec updates: <https://weekly.infosecwriteups.com/>

Follow publication

Member-only story

# Dom Based Xss

[![Monika sharma](https://miro.medium.com/v2/da:true/resize:fill:64:64/0*Tv4b4p5mb6J3IJwD)](https://medium.com/%40commanak46?source=post_page---byline--fa913b66b09b---------------------------------------)

[Monika sharma](https://medium.com/%40commanak46?source=post_page---byline--fa913b66b09b---------------------------------------)

3 min read

·

Jul 24, 2025

--

Share

An overlooked JavaScript plugin led to a dangerous DOM-based Cross-Site Scripting flaw exploitable across major browsers

Press enter or click to view image in full size

![]()

## Introduction

Uber has been at the forefront of tech innovation for years, but even giants can stumble. In 2016, security researcher e3xpl0it reported a DOM-based Cross-Site Scripting (XSS) vulnerability on Uber’s `eng.uber.com` subdomain. The culprit? A popular jQuery plugin called `prettyPhoto`, widely used for creating image lightboxes — but also known for its outdated and unsafe code handling.

This bug was not only functional across Chrome, Firefox, and Internet Explorer, but also triggered instantly with a single malicious link. Let’s walk through the vulnerability, the vectors used, and how this simple bug could have led to a serious security impact.

### Vulnerable Component: prettyPhoto

The `prettyPhoto` plugin had known vulnerabilities — particularly due to unsafe handling of URL hash fragments. This plugin parsed the fragment portion of the URL (i.e., after the `#`) and failed to sanitize input properly before dynamically injecting it into the DOM.

Uber’s engineering blog (`eng.uber.com`) was using this plugin, making it an open target for DOM-based attacks.

## The Attack Vectors

--

--

[![InfoSec Write-ups](https://miro.medium.com/v2/resize:fill:96:96/1*SWJxYWGZzgmBP1D0Qg_3zQ.png)](https://infosecwriteups.com/?source=post_page---post_publication_info--fa913b66b09b---------------------------------------)

[![InfoSec Write-ups](https://miro.medium.com/v2/resize:fill:128:128/1*SWJxYWGZzgmBP1D0Qg_3zQ.png)](https://infosecwriteups.com/?source=post_page---post_publication_info--fa913b66b09b---------------------------------------)

Follow

[## Published in InfoSec Write-ups](https://infosecwriteups.com/?source=post_page---post_publication_info--fa913b66b09b---------------------------------------)

[71K followers](/followers?source=post_page---post_publication_info--fa913b66b09b---------------------------------------)

·[Last published 3 hours ago](/actuator-unleashed-a-guide-to-finding-and-exploiting-spring-boot-actuator-endpoints-29252dcd9d79?source=post_page---post_publication_info--fa913b66b09b---------------------------------------)

A collection of write-ups from the best hackers in the world on topics ranging from bug bounties and CTFs to vulnhub machines, hardware challenges and real life encounters. Subscribe to our weekly newsletter for the coolest infosec updates: <https://weekly.infosecwriteups.com/>

Follow

[![Monika sharma](https://miro.medium.com/v2/resize:fill:96:96/0*Tv4b4p5mb6J3IJwD)](https://medium.com/%40commanak46?source=post_page---post_author_info--fa913b66b09b---------------------------------------)

[![Monika sharma](https://miro.medium.com/v2/resize:fill:128:128/0*Tv4b4p5mb6J3IJwD)](https://medium.com/%40commanak46?source=post_page---post_author_info--fa913b66b09b---------------------------------------)

[## Written by Monika sharma](https://medium.com/%40commanak46?source=post_page---post_author_info--fa913b66b09b---------------------------------------)

[2K followers](https://medium.com/%40commanak46/followers?source=post_page---post_author_info--fa913b66b09b---------------------------------------)

·[7 following](https://medium.com/%40commanak46/following?source=post_page---post_author_info--fa913b66b09b---------------------------------------)

## No responses yet

[Help](https://help.medium.com/hc/en-us?source=post_page-----fa913b66b09b---------------------------------------)

[Status](https://status.medium.com/?source=post_page-----fa913b66b09b---------------------------------------)

[About](https://medium.com/about?autoplay=1&source=post_page-----fa913b66b09b---------------------------------------)

[Careers](https://medium.com/jobs-at-medium/work-at-medium-959d1a85284e?source=post_page-----fa913b66b09b---------------------------------------)

Press

[Blog](https://blog.medium.com/?source=post_page-----fa913b66b09b---------------------------------------)

[Privacy](https://policy.medium.com/medium-privacy-policy-f03bf92035c9?source=post_page-----fa913b66b09b---------------------------------------)

[Rules](https://policy.medium.com/medium-rules-30e5502c4eb4?source=post_page-----fa913b66b09b---------------------------------------)

[Terms](https://policy.medium.com/medium-terms-of-service-9db0094a1e0f?source=post_page-----fa913b66b09b---------------------------------------)

[Text to speech](https://speechify.com/medium?source=post_page-----fa913b66b09b---------------------------------------)