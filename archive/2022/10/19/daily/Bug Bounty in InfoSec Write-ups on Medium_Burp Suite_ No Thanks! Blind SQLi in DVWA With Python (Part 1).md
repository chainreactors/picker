---
title: Burp Suite? No Thanks! Blind SQLi in DVWA With Python (Part 1)
url: https://infosecwriteups.com/how-i-exploited-blind-sqli-without-using-any-tool-stackzero-396e831ecbdf?source=rss----7b722bfd1b8d--bug_bounty
source: Bug Bounty in InfoSec Write-ups on Medium
date: 2022-10-19
fetch_date: 2025-10-03T20:14:35.955540
---

# Burp Suite? No Thanks! Blind SQLi in DVWA With Python (Part 1)

[Sitemap](/sitemap/sitemap.xml)

[Open in app](https://rsci.app.link/?%24canonical_url=https%3A%2F%2Fmedium.com%2Fp%2F396e831ecbdf&%7Efeature=LoOpenInAppButton&%7Echannel=ShowPostUnderCollection&%7Estage=mobileNavBar&source=post_page---top_nav_layout_nav-----------------------------------------)

Sign up

[Sign in](https://medium.com/m/signin?operation=login&redirect=https%3A%2F%2Finfosecwriteups.com%2Fhow-i-exploited-blind-sqli-without-using-any-tool-stackzero-396e831ecbdf&source=post_page---top_nav_layout_nav-----------------------global_nav------------------)

[Medium Logo](https://medium.com/?source=post_page---top_nav_layout_nav-----------------------------------------)

[Write](https://medium.com/m/signin?operation=register&redirect=https%3A%2F%2Fmedium.com%2Fnew-story&source=---top_nav_layout_nav-----------------------new_post_topnav------------------)

[Search](https://medium.com/search?source=post_page---top_nav_layout_nav-----------------------------------------)

Sign up

[Sign in](https://medium.com/m/signin?operation=login&redirect=https%3A%2F%2Finfosecwriteups.com%2Fhow-i-exploited-blind-sqli-without-using-any-tool-stackzero-396e831ecbdf&source=post_page---top_nav_layout_nav-----------------------global_nav------------------)

![](https://miro.medium.com/v2/resize:fill:64:64/1*dmbNkD5D-u45r44go_cf0g.png)

[## InfoSec Write-ups](https://infosecwriteups.com/?source=post_page---publication_nav-7b722bfd1b8d-396e831ecbdf---------------------------------------)

·

Follow publication

[![InfoSec Write-ups](https://miro.medium.com/v2/resize:fill:76:76/1*SWJxYWGZzgmBP1D0Qg_3zQ.png)](https://infosecwriteups.com/?source=post_page---post_publication_sidebar-7b722bfd1b8d-396e831ecbdf---------------------------------------)

A collection of write-ups from the best hackers in the world on topics ranging from bug bounties and CTFs to vulnhub machines, hardware challenges and real life encounters. Subscribe to our weekly newsletter for the coolest infosec updates: <https://weekly.infosecwriteups.com/>

Follow publication

Member-only story

# Burp Suite? No Thanks! Blind SQLi in DVWA With Python (Part 1)— StackZero

[![StackZero](https://miro.medium.com/v2/resize:fill:64:64/1*NfCOWe2r5LeicNQD3t8xMA.png)](https://medium.com/%40stackzero?source=post_page---byline--396e831ecbdf---------------------------------------)

[StackZero](https://medium.com/%40stackzero?source=post_page---byline--396e831ecbdf---------------------------------------)

13 min read

·

Oct 18, 2022

--

Share

Press enter or click to view image in full size

![]()

> This article was originally published at <https://www.stackzero.net/blind-sql-injection-dvwa-low-security-with-python/>

Hi hackers! Here is another article that will show how to exploit a known vulnerability in practice.
In particular, this time we will exploit the blind SQL injection section of [DVWA](https://github.com/digininja/DVWA) by using Python.

I want to show you an all-in-one script that once running will get all information you need to get the admin password in an environment where you cannot see query results.

This is how will be the final result:

Press enter or click to view image in full size

![]()

There are a lot of ways to solve the challenge, but I have chosen to use a custom script for these main reasons:

* We have to perform numerous calls and the [Burp Suite Community](https://portswigger.net/burp) edition has a limit on the number of threads for the intruder
* I don’t want to depend on an external tool
* The best way to understand something is to make it by yourself

I’m fully aware that a professional tool would be better for a Penetration Tester, anyway this…

--

--

[![InfoSec Write-ups](https://miro.medium.com/v2/resize:fill:96:96/1*SWJxYWGZzgmBP1D0Qg_3zQ.png)](https://infosecwriteups.com/?source=post_page---post_publication_info--396e831ecbdf---------------------------------------)

[![InfoSec Write-ups](https://miro.medium.com/v2/resize:fill:128:128/1*SWJxYWGZzgmBP1D0Qg_3zQ.png)](https://infosecwriteups.com/?source=post_page---post_publication_info--396e831ecbdf---------------------------------------)

Follow

[## Published in InfoSec Write-ups](https://infosecwriteups.com/?source=post_page---post_publication_info--396e831ecbdf---------------------------------------)

[71K followers](/followers?source=post_page---post_publication_info--396e831ecbdf---------------------------------------)

·[Last published 5 days ago](/how-to-find-p1-bugs-using-google-in-your-target-part-1-e37455324dc1?source=post_page---post_publication_info--396e831ecbdf---------------------------------------)

A collection of write-ups from the best hackers in the world on topics ranging from bug bounties and CTFs to vulnhub machines, hardware challenges and real life encounters. Subscribe to our weekly newsletter for the coolest infosec updates: <https://weekly.infosecwriteups.com/>

Follow

[![StackZero](https://miro.medium.com/v2/resize:fill:96:96/1*NfCOWe2r5LeicNQD3t8xMA.png)](https://medium.com/%40stackzero?source=post_page---post_author_info--396e831ecbdf---------------------------------------)

[![StackZero](https://miro.medium.com/v2/resize:fill:128:128/1*NfCOWe2r5LeicNQD3t8xMA.png)](https://medium.com/%40stackzero?source=post_page---post_author_info--396e831ecbdf---------------------------------------)

[## Written by StackZero](https://medium.com/%40stackzero?source=post_page---post_author_info--396e831ecbdf---------------------------------------)

[362 followers](https://medium.com/%40stackzero/followers?source=post_page---post_author_info--396e831ecbdf---------------------------------------)

·[61 following](https://medium.com/%40stackzero/following?source=post_page---post_author_info--396e831ecbdf---------------------------------------)

I have a passion for sharing my knowledge and helping others stay safe online. I just want to share tips and advice useful for me.

## No responses yet

[Help](https://help.medium.com/hc/en-us?source=post_page-----396e831ecbdf---------------------------------------)

[Status](https://status.medium.com/?source=post_page-----396e831ecbdf---------------------------------------)

[About](https://medium.com/about?autoplay=1&source=post_page-----396e831ecbdf---------------------------------------)

[Careers](https://medium.com/jobs-at-medium/work-at-medium-959d1a85284e?source=post_page-----396e831ecbdf---------------------------------------)

Press

[Blog](https://blog.medium.com/?source=post_page-----396e831ecbdf---------------------------------------)

[Privacy](https://policy.medium.com/medium-privacy-policy-f03bf92035c9?source=post_page-----396e831ecbdf---------------------------------------)

[Rules](https://policy.medium.com/medium-rules-30e5502c4eb4?source=post_page-----396e831ecbdf---------------------------------------)

[Terms](https://policy.medium.com/medium-terms-of-service-9db0094a1e0f?source=post_page-----396e831ecbdf---------------------------------------)

[Text to speech](https://speechify.com/medium?source=post_page-----396e831ecbdf---------------------------------------)