---
title: Electron JS Application Penetration Testing
url: https://infosecwriteups.com/electron-js-application-penetration-testing-b0809af324f6?source=rss----7b722bfd1b8d--bug_bounty
source: Bug Bounty in InfoSec Write-ups on Medium
date: 2024-10-28
fetch_date: 2025-10-06T18:48:06.952943
---

# Electron JS Application Penetration Testing

[Sitemap](/sitemap/sitemap.xml)

[Open in app](https://rsci.app.link/?%24canonical_url=https%3A%2F%2Fmedium.com%2Fp%2Fb0809af324f6&%7Efeature=LoOpenInAppButton&%7Echannel=ShowPostUnderCollection&%7Estage=mobileNavBar&source=post_page---top_nav_layout_nav-----------------------------------------)

Sign up

[Sign in](https://medium.com/m/signin?operation=login&redirect=https%3A%2F%2Finfosecwriteups.com%2Felectron-js-application-penetration-testing-b0809af324f6&source=post_page---top_nav_layout_nav-----------------------global_nav------------------)

[Medium Logo](https://medium.com/?source=post_page---top_nav_layout_nav-----------------------------------------)

[Write](https://medium.com/m/signin?operation=register&redirect=https%3A%2F%2Fmedium.com%2Fnew-story&source=---top_nav_layout_nav-----------------------new_post_topnav------------------)

[Search](https://medium.com/search?source=post_page---top_nav_layout_nav-----------------------------------------)

Sign up

[Sign in](https://medium.com/m/signin?operation=login&redirect=https%3A%2F%2Finfosecwriteups.com%2Felectron-js-application-penetration-testing-b0809af324f6&source=post_page---top_nav_layout_nav-----------------------global_nav------------------)

![](https://miro.medium.com/v2/resize:fill:64:64/1*dmbNkD5D-u45r44go_cf0g.png)

[## InfoSec Write-ups](https://infosecwriteups.com/?source=post_page---publication_nav-7b722bfd1b8d-b0809af324f6---------------------------------------)

·

Follow publication

[![InfoSec Write-ups](https://miro.medium.com/v2/resize:fill:76:76/1*SWJxYWGZzgmBP1D0Qg_3zQ.png)](https://infosecwriteups.com/?source=post_page---post_publication_sidebar-7b722bfd1b8d-b0809af324f6---------------------------------------)

A collection of write-ups from the best hackers in the world on topics ranging from bug bounties and CTFs to vulnhub machines, hardware challenges and real life encounters. Subscribe to our weekly newsletter for the coolest infosec updates: <https://weekly.infosecwriteups.com/>

Follow publication

Member-only story

# Electron JS Application Penetration Testing

[![Ajay Naik](https://miro.medium.com/v2/resize:fill:64:64/1*_IX9-hF0QxJXhyR65v8Fww.jpeg)](https://medium.com/%40ajaynaikhack?source=post_page---byline--b0809af324f6---------------------------------------)

[Ajay Naik](https://medium.com/%40ajaynaikhack?source=post_page---byline--b0809af324f6---------------------------------------)

9 min read

·

Oct 17, 2024

--

Share

Press enter or click to view image in full size

![]()

## Overview of Electron JS

Electron is an open-source framework for building cross-platform desktop applications using web technologies such as JavaScript, HTML, and CSS. It combines the power of Node.js for backend functionality with Chromium for rendering. Due to its hybrid nature, Electron applications can present unique security challenges.

For more on Electron, you can visit [Electron JS](https://www.electronjs.org/).

## Reversing Electron Applications

Reversing is a critical step in Electron application penetration testing as it allows security professionals to extract the source code of Electron applications. This enables them to analyze the code for security flaws that might expose vulnerabilities in the application.

## Test Case 1: Reversing .exe Files

Reversing an Electron application in Windows can be simple using an `.exe` file. Here are the steps for reversing an Electron-based application:

1. **Download the application**: Use the link [**Notable App**](https://github.com/notable/notable/releases/download/v1.5.1/Notable.1.5.1.exe)**.**
2. **Install and locate the executable**: Right-click the installed application and select “Open File Location.”

--

--

[![InfoSec Write-ups](https://miro.medium.com/v2/resize:fill:96:96/1*SWJxYWGZzgmBP1D0Qg_3zQ.png)](https://infosecwriteups.com/?source=post_page---post_publication_info--b0809af324f6---------------------------------------)

[![InfoSec Write-ups](https://miro.medium.com/v2/resize:fill:128:128/1*SWJxYWGZzgmBP1D0Qg_3zQ.png)](https://infosecwriteups.com/?source=post_page---post_publication_info--b0809af324f6---------------------------------------)

Follow

[## Published in InfoSec Write-ups](https://infosecwriteups.com/?source=post_page---post_publication_info--b0809af324f6---------------------------------------)

[71K followers](/followers?source=post_page---post_publication_info--b0809af324f6---------------------------------------)

·[Last published 3 hours ago](/baby-dfc2547dc387?source=post_page---post_publication_info--b0809af324f6---------------------------------------)

A collection of write-ups from the best hackers in the world on topics ranging from bug bounties and CTFs to vulnhub machines, hardware challenges and real life encounters. Subscribe to our weekly newsletter for the coolest infosec updates: <https://weekly.infosecwriteups.com/>

Follow

[![Ajay Naik](https://miro.medium.com/v2/resize:fill:96:96/1*_IX9-hF0QxJXhyR65v8Fww.jpeg)](https://medium.com/%40ajaynaikhack?source=post_page---post_author_info--b0809af324f6---------------------------------------)

[![Ajay Naik](https://miro.medium.com/v2/resize:fill:128:128/1*_IX9-hF0QxJXhyR65v8Fww.jpeg)](https://medium.com/%40ajaynaikhack?source=post_page---post_author_info--b0809af324f6---------------------------------------)

[## Written by Ajay Naik](https://medium.com/%40ajaynaikhack?source=post_page---post_author_info--b0809af324f6---------------------------------------)

[313 followers](https://medium.com/%40ajaynaikhack/followers?source=post_page---post_author_info--b0809af324f6---------------------------------------)

·[276 following](https://medium.com/%40ajaynaikhack/following?source=post_page---post_author_info--b0809af324f6---------------------------------------)

Cyber security Expert with a Strong Focus on Penetration Testing, Threat Intelligence, and Bug Bounty Hunting.

## No responses yet

[Help](https://help.medium.com/hc/en-us?source=post_page-----b0809af324f6---------------------------------------)

[Status](https://status.medium.com/?source=post_page-----b0809af324f6---------------------------------------)

[About](https://medium.com/about?autoplay=1&source=post_page-----b0809af324f6---------------------------------------)

[Careers](https://medium.com/jobs-at-medium/work-at-medium-959d1a85284e?source=post_page-----b0809af324f6---------------------------------------)

Press

[Blog](https://blog.medium.com/?source=post_page-----b0809af324f6---------------------------------------)

[Privacy](https://policy.medium.com/medium-privacy-policy-f03bf92035c9?source=post_page-----b0809af324f6---------------------------------------)

[Rules](https://policy.medium.com/medium-rules-30e5502c4eb4?source=post_page-----b0809af324f6---------------------------------------)

[Terms](https://policy.medium.com/medium-terms-of-service-9db0094a1e0f?source=post_page-----b0809af324f6---------------------------------------)

[Text to speech](https://speechify.com/medium?source=post_page-----b0809af324f6---------------------------------------)