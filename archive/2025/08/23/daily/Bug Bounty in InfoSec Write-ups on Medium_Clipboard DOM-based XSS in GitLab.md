---
title: Clipboard DOM-based XSS in GitLab
url: https://infosecwriteups.com/clipboard-dom-based-xss-in-gitlab-2b4768f108cf?source=rss----7b722bfd1b8d--bug_bounty
source: Bug Bounty in InfoSec Write-ups on Medium
date: 2025-08-23
fetch_date: 2025-10-07T00:47:45.245575
---

# Clipboard DOM-based XSS in GitLab

[Sitemap](/sitemap/sitemap.xml)

[Open in app](https://rsci.app.link/?%24canonical_url=https%3A%2F%2Fmedium.com%2Fp%2F2b4768f108cf&%7Efeature=LoOpenInAppButton&%7Echannel=ShowPostUnderCollection&%7Estage=mobileNavBar&source=post_page---top_nav_layout_nav-----------------------------------------)

Sign up

[Sign in](https://medium.com/m/signin?operation=login&redirect=https%3A%2F%2Finfosecwriteups.com%2Fclipboard-dom-based-xss-in-gitlab-2b4768f108cf&source=post_page---top_nav_layout_nav-----------------------global_nav------------------)

[Medium Logo](https://medium.com/?source=post_page---top_nav_layout_nav-----------------------------------------)

[Write](https://medium.com/m/signin?operation=register&redirect=https%3A%2F%2Fmedium.com%2Fnew-story&source=---top_nav_layout_nav-----------------------new_post_topnav------------------)

[Search](https://medium.com/search?source=post_page---top_nav_layout_nav-----------------------------------------)

Sign up

[Sign in](https://medium.com/m/signin?operation=login&redirect=https%3A%2F%2Finfosecwriteups.com%2Fclipboard-dom-based-xss-in-gitlab-2b4768f108cf&source=post_page---top_nav_layout_nav-----------------------global_nav------------------)

![](https://miro.medium.com/v2/resize:fill:64:64/1*dmbNkD5D-u45r44go_cf0g.png)

[## InfoSec Write-ups](https://infosecwriteups.com/?source=post_page---publication_nav-7b722bfd1b8d-2b4768f108cf---------------------------------------)

·

Follow publication

[![InfoSec Write-ups](https://miro.medium.com/v2/resize:fill:76:76/1*SWJxYWGZzgmBP1D0Qg_3zQ.png)](https://infosecwriteups.com/?source=post_page---post_publication_sidebar-7b722bfd1b8d-2b4768f108cf---------------------------------------)

A collection of write-ups from the best hackers in the world on topics ranging from bug bounties and CTFs to vulnhub machines, hardware challenges and real life encounters. Subscribe to our weekly newsletter for the coolest infosec updates: <https://weekly.infosecwriteups.com/>

Follow publication

Member-only story

# Clipboard DOM-based XSS in GitLab

## Unveiling the Hidden Risks of Unsanitized Markdown Fields and Safeguarding Against JavaScript Exploitation

[![Monika sharma](https://miro.medium.com/v2/da:true/resize:fill:64:64/0*Tv4b4p5mb6J3IJwD)](https://medium.com/%40commanak46?source=post_page---byline--2b4768f108cf---------------------------------------)

[Monika sharma](https://medium.com/%40commanak46?source=post_page---byline--2b4768f108cf---------------------------------------)

4 min read

·

Aug 22, 2025

--

Share

Press enter or click to view image in full size

![]()

## Introduction

Cross-site scripting (XSS) vulnerabilities continue to pose significant threats to web applications, with DOM-based XSS presenting a unique challenge due to its reliance on client-side manipulation. A critical vulnerability was identified in GitLab’s Markdown text fields, where a clipboard DOM-based XSS flaw allows attackers to execute arbitrary JavaScript under a user’s credentials. This article provides an in-depth exploration of the vulnerability, its technical underpinnings, reproduction steps, impact, and mitigation strategies, offering valuable insights for developers and security professionals.

## Understanding DOM-based XSS

DOM-based XSS occurs when client-side scripts dynamically manipulate the Document Object Model (DOM) based on unsanitized user input, such as data from the clipboard. Unlike server-side XSS, the attack vector is processed entirely within the browser, making it harder to detect through traditional security measures. In GitLab’s case, the vulnerability leverages the clipboard’s `text/x-gfm-html` MIME type, enabling malicious payloads to be injected into Markdown text fields…

--

--

[![InfoSec Write-ups](https://miro.medium.com/v2/resize:fill:96:96/1*SWJxYWGZzgmBP1D0Qg_3zQ.png)](https://infosecwriteups.com/?source=post_page---post_publication_info--2b4768f108cf---------------------------------------)

[![InfoSec Write-ups](https://miro.medium.com/v2/resize:fill:128:128/1*SWJxYWGZzgmBP1D0Qg_3zQ.png)](https://infosecwriteups.com/?source=post_page---post_publication_info--2b4768f108cf---------------------------------------)

Follow

[## Published in InfoSec Write-ups](https://infosecwriteups.com/?source=post_page---post_publication_info--2b4768f108cf---------------------------------------)

[71K followers](/followers?source=post_page---post_publication_info--2b4768f108cf---------------------------------------)

·[Last published 4 hours ago](/actuator-unleashed-a-guide-to-finding-and-exploiting-spring-boot-actuator-endpoints-29252dcd9d79?source=post_page---post_publication_info--2b4768f108cf---------------------------------------)

A collection of write-ups from the best hackers in the world on topics ranging from bug bounties and CTFs to vulnhub machines, hardware challenges and real life encounters. Subscribe to our weekly newsletter for the coolest infosec updates: <https://weekly.infosecwriteups.com/>

Follow

[![Monika sharma](https://miro.medium.com/v2/resize:fill:96:96/0*Tv4b4p5mb6J3IJwD)](https://medium.com/%40commanak46?source=post_page---post_author_info--2b4768f108cf---------------------------------------)

[![Monika sharma](https://miro.medium.com/v2/resize:fill:128:128/0*Tv4b4p5mb6J3IJwD)](https://medium.com/%40commanak46?source=post_page---post_author_info--2b4768f108cf---------------------------------------)

[## Written by Monika sharma](https://medium.com/%40commanak46?source=post_page---post_author_info--2b4768f108cf---------------------------------------)

[2K followers](https://medium.com/%40commanak46/followers?source=post_page---post_author_info--2b4768f108cf---------------------------------------)

·[7 following](https://medium.com/%40commanak46/following?source=post_page---post_author_info--2b4768f108cf---------------------------------------)

## No responses yet

[Help](https://help.medium.com/hc/en-us?source=post_page-----2b4768f108cf---------------------------------------)

[Status](https://status.medium.com/?source=post_page-----2b4768f108cf---------------------------------------)

[About](https://medium.com/about?autoplay=1&source=post_page-----2b4768f108cf---------------------------------------)

[Careers](https://medium.com/jobs-at-medium/work-at-medium-959d1a85284e?source=post_page-----2b4768f108cf---------------------------------------)

Press

[Blog](https://blog.medium.com/?source=post_page-----2b4768f108cf---------------------------------------)

[Privacy](https://policy.medium.com/medium-privacy-policy-f03bf92035c9?source=post_page-----2b4768f108cf---------------------------------------)

[Rules](https://policy.medium.com/medium-rules-30e5502c4eb4?source=post_page-----2b4768f108cf---------------------------------------)

[Terms](https://policy.medium.com/medium-terms-of-service-9db0094a1e0f?source=post_page-----2b4768f108cf---------------------------------------)

[Text to speech](https://speechify.com/medium?source=post_page-----2b4768f108cf---------------------------------------)