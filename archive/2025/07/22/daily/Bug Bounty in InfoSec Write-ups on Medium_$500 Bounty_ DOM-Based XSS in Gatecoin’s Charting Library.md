---
title: $500 Bounty: DOM-Based XSS in Gatecoin’s Charting Library
url: https://infosecwriteups.com/500-bounty-dom-based-xss-in-gatecoins-charting-library-e21e40c4f270?source=rss----7b722bfd1b8d--bug_bounty
source: Bug Bounty in InfoSec Write-ups on Medium
date: 2025-07-22
fetch_date: 2025-10-06T23:26:57.488453
---

# $500 Bounty: DOM-Based XSS in Gatecoin’s Charting Library

[Sitemap](/sitemap/sitemap.xml)

[Open in app](https://rsci.app.link/?%24canonical_url=https%3A%2F%2Fmedium.com%2Fp%2Fe21e40c4f270&%7Efeature=LoOpenInAppButton&%7Echannel=ShowPostUnderCollection&%7Estage=mobileNavBar&source=post_page---top_nav_layout_nav-----------------------------------------)

Sign up

[Sign in](https://medium.com/m/signin?operation=login&redirect=https%3A%2F%2Finfosecwriteups.com%2F500-bounty-dom-based-xss-in-gatecoins-charting-library-e21e40c4f270&source=post_page---top_nav_layout_nav-----------------------global_nav------------------)

[Medium Logo](https://medium.com/?source=post_page---top_nav_layout_nav-----------------------------------------)

[Write](https://medium.com/m/signin?operation=register&redirect=https%3A%2F%2Fmedium.com%2Fnew-story&source=---top_nav_layout_nav-----------------------new_post_topnav------------------)

[Search](https://medium.com/search?source=post_page---top_nav_layout_nav-----------------------------------------)

Sign up

[Sign in](https://medium.com/m/signin?operation=login&redirect=https%3A%2F%2Finfosecwriteups.com%2F500-bounty-dom-based-xss-in-gatecoins-charting-library-e21e40c4f270&source=post_page---top_nav_layout_nav-----------------------global_nav------------------)

![](https://miro.medium.com/v2/resize:fill:64:64/1*dmbNkD5D-u45r44go_cf0g.png)

[## InfoSec Write-ups](https://infosecwriteups.com/?source=post_page---publication_nav-7b722bfd1b8d-e21e40c4f270---------------------------------------)

·

Follow publication

[![InfoSec Write-ups](https://miro.medium.com/v2/resize:fill:76:76/1*SWJxYWGZzgmBP1D0Qg_3zQ.png)](https://infosecwriteups.com/?source=post_page---post_publication_sidebar-7b722bfd1b8d-e21e40c4f270---------------------------------------)

A collection of write-ups from the best hackers in the world on topics ranging from bug bounties and CTFs to vulnhub machines, hardware challenges and real life encounters. Subscribe to our weekly newsletter for the coolest infosec updates: <https://weekly.infosecwriteups.com/>

Follow publication

Member-only story

# **$500 Bounty: DOM-Based XSS in Gatecoin’s Charting Library**

## A critical oversight in dynamically loaded JavaScript enabled a $500 DOM XSS attack — here’s how it worked and how you can find similar issues.

[![Monika sharma](https://miro.medium.com/v2/da:true/resize:fill:64:64/0*Tv4b4p5mb6J3IJwD)](https://medium.com/%40commanak46?source=post_page---byline--e21e40c4f270---------------------------------------)

[Monika sharma](https://medium.com/%40commanak46?source=post_page---byline--e21e40c4f270---------------------------------------)

3 min read

·

Jul 21, 2025

--

Share

Press enter or click to view image in full size

![]()

## Introduction

In the world of client-side vulnerabilities, few bugs are as silently powerful as DOM-based Cross-Site Scripting (XSS). Unlike traditional reflected or stored XSS, DOM XSS resides entirely in the client’s browser, exploiting the way JavaScript handles untrusted input — often bypassing WAFs, CSPs, and even bug bounty scanners.

In this report, we’ll explore how a critical DOM XSS flaw in Gatecoin’s `charting_library` allowed an attacker to inject and execute arbitrary JavaScript code by manipulating a URL fragment. The bug was awarded $500, and it perfectly showcases how improper handling of dynamic script imports can lead to full account compromise.

## The Vulnerability Explained

The vulnerable endpoint was located at:

```
<https://gatecoin.com/widget-trade/assets/charting_library/static/tv-chart.html>
```

This page took a URL fragment parameter called `indicatorsFile` and directly passed it into `$.getScript()`, a jQuery method that loads…

--

--

[![InfoSec Write-ups](https://miro.medium.com/v2/resize:fill:96:96/1*SWJxYWGZzgmBP1D0Qg_3zQ.png)](https://infosecwriteups.com/?source=post_page---post_publication_info--e21e40c4f270---------------------------------------)

[![InfoSec Write-ups](https://miro.medium.com/v2/resize:fill:128:128/1*SWJxYWGZzgmBP1D0Qg_3zQ.png)](https://infosecwriteups.com/?source=post_page---post_publication_info--e21e40c4f270---------------------------------------)

Follow

[## Published in InfoSec Write-ups](https://infosecwriteups.com/?source=post_page---post_publication_info--e21e40c4f270---------------------------------------)

[71K followers](/followers?source=post_page---post_publication_info--e21e40c4f270---------------------------------------)

·[Last published 3 hours ago](/actuator-unleashed-a-guide-to-finding-and-exploiting-spring-boot-actuator-endpoints-29252dcd9d79?source=post_page---post_publication_info--e21e40c4f270---------------------------------------)

A collection of write-ups from the best hackers in the world on topics ranging from bug bounties and CTFs to vulnhub machines, hardware challenges and real life encounters. Subscribe to our weekly newsletter for the coolest infosec updates: <https://weekly.infosecwriteups.com/>

Follow

[![Monika sharma](https://miro.medium.com/v2/resize:fill:96:96/0*Tv4b4p5mb6J3IJwD)](https://medium.com/%40commanak46?source=post_page---post_author_info--e21e40c4f270---------------------------------------)

[![Monika sharma](https://miro.medium.com/v2/resize:fill:128:128/0*Tv4b4p5mb6J3IJwD)](https://medium.com/%40commanak46?source=post_page---post_author_info--e21e40c4f270---------------------------------------)

[## Written by Monika sharma](https://medium.com/%40commanak46?source=post_page---post_author_info--e21e40c4f270---------------------------------------)

[2K followers](https://medium.com/%40commanak46/followers?source=post_page---post_author_info--e21e40c4f270---------------------------------------)

·[7 following](https://medium.com/%40commanak46/following?source=post_page---post_author_info--e21e40c4f270---------------------------------------)

## No responses yet

[Help](https://help.medium.com/hc/en-us?source=post_page-----e21e40c4f270---------------------------------------)

[Status](https://status.medium.com/?source=post_page-----e21e40c4f270---------------------------------------)

[About](https://medium.com/about?autoplay=1&source=post_page-----e21e40c4f270---------------------------------------)

[Careers](https://medium.com/jobs-at-medium/work-at-medium-959d1a85284e?source=post_page-----e21e40c4f270---------------------------------------)

Press

[Blog](https://blog.medium.com/?source=post_page-----e21e40c4f270---------------------------------------)

[Privacy](https://policy.medium.com/medium-privacy-policy-f03bf92035c9?source=post_page-----e21e40c4f270---------------------------------------)

[Rules](https://policy.medium.com/medium-rules-30e5502c4eb4?source=post_page-----e21e40c4f270---------------------------------------)

[Terms](https://policy.medium.com/medium-terms-of-service-9db0094a1e0f?source=post_page-----e21e40c4f270---------------------------------------)

[Text to speech](https://speechify.com/medium?source=post_page-----e21e40c4f270---------------------------------------)