---
title: CRLF Injection — xxx$ — How was it possible for me to earn a bounty with the Cloudflare WAF?
url: https://infosecwriteups.com/crlf-injection-xxx-how-was-it-possible-for-me-to-earn-a-bounty-with-the-cloudflare-waf-f581506f97f5?source=rss----7b722bfd1b8d--bug_bounty
source: Bug Bounty in InfoSec Write-ups on Medium
date: 2022-12-25
fetch_date: 2025-10-04T02:29:21.735810
---

# CRLF Injection — xxx$ — How was it possible for me to earn a bounty with the Cloudflare WAF?

[Sitemap](/sitemap/sitemap.xml)

[Open in app](https://rsci.app.link/?%24canonical_url=https%3A%2F%2Fmedium.com%2Fp%2Ff581506f97f5&%7Efeature=LoOpenInAppButton&%7Echannel=ShowPostUnderCollection&%7Estage=mobileNavBar&source=post_page---top_nav_layout_nav-----------------------------------------)

Sign up

[Sign in](https://medium.com/m/signin?operation=login&redirect=https%3A%2F%2Finfosecwriteups.com%2Fcrlf-injection-xxx-how-was-it-possible-for-me-to-earn-a-bounty-with-the-cloudflare-waf-f581506f97f5&source=post_page---top_nav_layout_nav-----------------------global_nav------------------)

[Medium Logo](https://medium.com/?source=post_page---top_nav_layout_nav-----------------------------------------)

[Write](https://medium.com/m/signin?operation=register&redirect=https%3A%2F%2Fmedium.com%2Fnew-story&source=---top_nav_layout_nav-----------------------new_post_topnav------------------)

[Search](https://medium.com/search?source=post_page---top_nav_layout_nav-----------------------------------------)

Sign up

[Sign in](https://medium.com/m/signin?operation=login&redirect=https%3A%2F%2Finfosecwriteups.com%2Fcrlf-injection-xxx-how-was-it-possible-for-me-to-earn-a-bounty-with-the-cloudflare-waf-f581506f97f5&source=post_page---top_nav_layout_nav-----------------------global_nav------------------)

![](https://miro.medium.com/v2/resize:fill:64:64/1*dmbNkD5D-u45r44go_cf0g.png)

[## InfoSec Write-ups](https://infosecwriteups.com/?source=post_page---publication_nav-7b722bfd1b8d-f581506f97f5---------------------------------------)

·

Follow publication

[![InfoSec Write-ups](https://miro.medium.com/v2/resize:fill:76:76/1*SWJxYWGZzgmBP1D0Qg_3zQ.png)](https://infosecwriteups.com/?source=post_page---post_publication_sidebar-7b722bfd1b8d-f581506f97f5---------------------------------------)

A collection of write-ups from the best hackers in the world on topics ranging from bug bounties and CTFs to vulnhub machines, hardware challenges and real life encounters. Subscribe to our weekly newsletter for the coolest infosec updates: <https://weekly.infosecwriteups.com/>

Follow publication

Member-only story

# CRLF Injection — xxx$ — How was it possible for me to earn a bounty with the Cloudflare WAF?

[![Proviesec](https://miro.medium.com/v2/resize:fill:64:64/1*8sxoWONIiXCM7_9zKPJRxw.png)](https://proviesec.medium.com/?source=post_page---byline--f581506f97f5---------------------------------------)

[Proviesec](https://proviesec.medium.com/?source=post_page---byline--f581506f97f5---------------------------------------)

5 min read

·

Dec 24, 2022

--

Share

I recently discovered a CRLF injection vulnerability on a popular website. In this blog post, I will describe the vulnerability and the attack scenarios that I was able to demonstrate. I will also discuss the potential impacts of CRLF injection vulnerabilities.

Press enter or click to view image in full size

![]()

### What is CRLF?

CRLF (Carriage Return and Line Feed) is a sequence of two special characters that’s used to represent the end of a line of text in many computing contexts. In the context of cybersecurity, CRLF attacks can be used by attackers to inject malicious content into websites. To protect against these attacks, web developers need to properly handle CRLF sequences and sanitize user-generated content.

CRLF Injection attack has two most important use cases:

* **Log Splitting:** The attacker inserts an end of line character and an extra line to falsify the log file entries in order to deceive the system administrators by hiding other attacks.
* **HTTP Response Splitting:** CRLF injection is used to add HTTP headers to the HTTP response and, for example, perform an XSS attack that leads to information disclosure.

## The Report

--

--

[![InfoSec Write-ups](https://miro.medium.com/v2/resize:fill:96:96/1*SWJxYWGZzgmBP1D0Qg_3zQ.png)](https://infosecwriteups.com/?source=post_page---post_publication_info--f581506f97f5---------------------------------------)

[![InfoSec Write-ups](https://miro.medium.com/v2/resize:fill:128:128/1*SWJxYWGZzgmBP1D0Qg_3zQ.png)](https://infosecwriteups.com/?source=post_page---post_publication_info--f581506f97f5---------------------------------------)

Follow

[## Published in InfoSec Write-ups](https://infosecwriteups.com/?source=post_page---post_publication_info--f581506f97f5---------------------------------------)

[71K followers](/followers?source=post_page---post_publication_info--f581506f97f5---------------------------------------)

·[Last published 5 days ago](/how-to-find-p1-bugs-using-google-in-your-target-part-1-e37455324dc1?source=post_page---post_publication_info--f581506f97f5---------------------------------------)

A collection of write-ups from the best hackers in the world on topics ranging from bug bounties and CTFs to vulnhub machines, hardware challenges and real life encounters. Subscribe to our weekly newsletter for the coolest infosec updates: <https://weekly.infosecwriteups.com/>

Follow

[![Proviesec](https://miro.medium.com/v2/resize:fill:96:96/1*8sxoWONIiXCM7_9zKPJRxw.png)](https://proviesec.medium.com/?source=post_page---post_author_info--f581506f97f5---------------------------------------)

[![Proviesec](https://miro.medium.com/v2/resize:fill:128:128/1*8sxoWONIiXCM7_9zKPJRxw.png)](https://proviesec.medium.com/?source=post_page---post_author_info--f581506f97f5---------------------------------------)

[## Written by Proviesec](https://proviesec.medium.com/?source=post_page---post_author_info--f581506f97f5---------------------------------------)

[497 followers](https://proviesec.medium.com/followers?source=post_page---post_author_info--f581506f97f5---------------------------------------)

·[245 following](https://medium.com/%40proviesec/following?source=post_page---post_author_info--f581506f97f5---------------------------------------)

All about Cybersecurity

## No responses yet

[Help](https://help.medium.com/hc/en-us?source=post_page-----f581506f97f5---------------------------------------)

[Status](https://status.medium.com/?source=post_page-----f581506f97f5---------------------------------------)

[About](https://medium.com/about?autoplay=1&source=post_page-----f581506f97f5---------------------------------------)

[Careers](https://medium.com/jobs-at-medium/work-at-medium-959d1a85284e?source=post_page-----f581506f97f5---------------------------------------)

Press

[Blog](https://blog.medium.com/?source=post_page-----f581506f97f5---------------------------------------)

[Privacy](https://policy.medium.com/medium-privacy-policy-f03bf92035c9?source=post_page-----f581506f97f5---------------------------------------)

[Rules](https://policy.medium.com/medium-rules-30e5502c4eb4?source=post_page-----f581506f97f5---------------------------------------)

[Terms](https://policy.medium.com/medium-terms-of-service-9db0094a1e0f?source=post_page-----f581506f97f5---------------------------------------)

[Text to speech](https://speechify.com/medium?source=post_page-----f581506f97f5---------------------------------------)