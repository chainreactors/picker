---
title: Burp Suite? No Thanks! Blind SQLi in DVWA With Python (Part 2) — StackZero
url: https://infosecwriteups.com/burp-suite-no-thanks-blind-sqli-in-dvwa-with-python-part-2-stackzero-a5c0acf431dc?source=rss----7b722bfd1b8d--bug_bounty
source: Bug Bounty in InfoSec Write-ups on Medium
date: 2022-10-27
fetch_date: 2025-10-03T20:59:31.276228
---

# Burp Suite? No Thanks! Blind SQLi in DVWA With Python (Part 2) — StackZero

[Sitemap](/sitemap/sitemap.xml)

[Open in app](https://rsci.app.link/?%24canonical_url=https%3A%2F%2Fmedium.com%2Fp%2Fa5c0acf431dc&%7Efeature=LoOpenInAppButton&%7Echannel=ShowPostUnderCollection&%7Estage=mobileNavBar&source=post_page---top_nav_layout_nav-----------------------------------------)

Sign up

[Sign in](https://medium.com/m/signin?operation=login&redirect=https%3A%2F%2Finfosecwriteups.com%2Fburp-suite-no-thanks-blind-sqli-in-dvwa-with-python-part-2-stackzero-a5c0acf431dc&source=post_page---top_nav_layout_nav-----------------------global_nav------------------)

[Medium Logo](https://medium.com/?source=post_page---top_nav_layout_nav-----------------------------------------)

[Write](https://medium.com/m/signin?operation=register&redirect=https%3A%2F%2Fmedium.com%2Fnew-story&source=---top_nav_layout_nav-----------------------new_post_topnav------------------)

[Search](https://medium.com/search?source=post_page---top_nav_layout_nav-----------------------------------------)

Sign up

[Sign in](https://medium.com/m/signin?operation=login&redirect=https%3A%2F%2Finfosecwriteups.com%2Fburp-suite-no-thanks-blind-sqli-in-dvwa-with-python-part-2-stackzero-a5c0acf431dc&source=post_page---top_nav_layout_nav-----------------------global_nav------------------)

![](https://miro.medium.com/v2/resize:fill:64:64/1*dmbNkD5D-u45r44go_cf0g.png)

[## InfoSec Write-ups](https://infosecwriteups.com/?source=post_page---publication_nav-7b722bfd1b8d-a5c0acf431dc---------------------------------------)

·

Follow publication

[![InfoSec Write-ups](https://miro.medium.com/v2/resize:fill:76:76/1*SWJxYWGZzgmBP1D0Qg_3zQ.png)](https://infosecwriteups.com/?source=post_page---post_publication_sidebar-7b722bfd1b8d-a5c0acf431dc---------------------------------------)

A collection of write-ups from the best hackers in the world on topics ranging from bug bounties and CTFs to vulnhub machines, hardware challenges and real life encounters. Subscribe to our weekly newsletter for the coolest infosec updates: <https://weekly.infosecwriteups.com/>

Follow publication

Member-only story

# Burp Suite? No Thanks! Blind SQLi in DVWA With Python (Part 2) — StackZero

[![StackZero](https://miro.medium.com/v2/resize:fill:64:64/1*NfCOWe2r5LeicNQD3t8xMA.png)](https://medium.com/%40stackzero?source=post_page---byline--a5c0acf431dc---------------------------------------)

[StackZero](https://medium.com/%40stackzero?source=post_page---byline--a5c0acf431dc---------------------------------------)

10 min read

·

Oct 26, 2022

--

2

Share

Press enter or click to view image in full size

![]()

> This article was originally published at <https://www.stackzero.net/blind-sql-injection-dvwa-medium-python/>

Hi hackers! After pwning low-security [DVWA](https://github.com/digininja/DVWA) with a blind SQL Injection attack, it’s time to try a medium level of security by using Python!
I’m going to assume that you read the previous post at [this link](/how-i-exploited-blind-sqli-without-using-any-tool-stackzero-396e831ecbdf) so that we can focus our efforts just on new concepts.

If you are not familiar with SQL Injection, here there is a list of all my previous articles that can make you an SQLi ninja!

## In-Band SQL injection

* [SQL Injection: What You Need to Know](https://medium.com/codex/sql-injection-what-you-need-to-know-stackzero-abc80bc1ea5e)
* [Learn SQL injection in practice by hacking vulnerable application!](https://medium.com/bugbountywriteup/learn-sql-injection-in-practice-by-hacking-vulnerable-application-stackzero-ef7931c72aec)
* [How To Hack With SQL Injection Attacks! DVWA low security](https://medium.com/bugbountywriteup/how-to-hack-with-sql-injection-attacks-dvwa-low-security-stackzero-9286d7d0dfd1)
* [Hack With SQL Injection Attacks! DVWA medium security](/hack-with-sql-injection-attacks-dvwa-medium-security-stackzero-d4af0a9a5f9)
* [Hack With SQL Injection Attacks! DVWA high security](/hack-with-sql-injection-attacks-dvwa-high-security-stackzero-713638840515)

## Blind SQL injection

* [Burp Suite? No Thanks! Blind SQLi in DVWA With Python (Part 1)](/how-i-exploited-blind-sqli-without-using-any-tool-stackzero-396e831ecbdf)
* [Burp Suite? No Thanks! Blind SQLi in DVWA With Python (Part 2)](/burp-suite-no-thanks-blind-sqli-in-dvwa-with-python-part-2-stackzero-a5c0acf431dc)
* [Burp Suite? No Thanks! Blind SQLi in DVWA With Python (Part 3)](/burp-suite-no-thanks-blind-sqli-in-dvwa-with-python-part-3-stackzero-911545003f01)

--

--

2

[![InfoSec Write-ups](https://miro.medium.com/v2/resize:fill:96:96/1*SWJxYWGZzgmBP1D0Qg_3zQ.png)](https://infosecwriteups.com/?source=post_page---post_publication_info--a5c0acf431dc---------------------------------------)

[![InfoSec Write-ups](https://miro.medium.com/v2/resize:fill:128:128/1*SWJxYWGZzgmBP1D0Qg_3zQ.png)](https://infosecwriteups.com/?source=post_page---post_publication_info--a5c0acf431dc---------------------------------------)

Follow

[## Published in InfoSec Write-ups](https://infosecwriteups.com/?source=post_page---post_publication_info--a5c0acf431dc---------------------------------------)

[71K followers](/followers?source=post_page---post_publication_info--a5c0acf431dc---------------------------------------)

·[Last published 5 days ago](/how-to-find-p1-bugs-using-google-in-your-target-part-1-e37455324dc1?source=post_page---post_publication_info--a5c0acf431dc---------------------------------------)

A collection of write-ups from the best hackers in the world on topics ranging from bug bounties and CTFs to vulnhub machines, hardware challenges and real life encounters. Subscribe to our weekly newsletter for the coolest infosec updates: <https://weekly.infosecwriteups.com/>

Follow

[![StackZero](https://miro.medium.com/v2/resize:fill:96:96/1*NfCOWe2r5LeicNQD3t8xMA.png)](https://medium.com/%40stackzero?source=post_page---post_author_info--a5c0acf431dc---------------------------------------)

[![StackZero](https://miro.medium.com/v2/resize:fill:128:128/1*NfCOWe2r5LeicNQD3t8xMA.png)](https://medium.com/%40stackzero?source=post_page---post_author_info--a5c0acf431dc---------------------------------------)

[## Written by StackZero](https://medium.com/%40stackzero?source=post_page---post_author_info--a5c0acf431dc---------------------------------------)

[362 followers](https://medium.com/%40stackzero/followers?source=post_page---post_author_info--a5c0acf431dc---------------------------------------)

·[61 following](https://medium.com/%40stackzero/following?source=post_page---post_author_info--a5c0acf431dc---------------------------------------)

I have a passion for sharing my knowledge and helping others stay safe online. I just want to share tips and advice useful for me.

## Responses (2)

See all responses

[Help](https://help.medium.com/hc/en-us?source=post_page-----a5c0acf431dc---------------------------------------)

[Status](https://status.medium.com/?source=post_page-----a5c0acf431dc---------------------------------------)

[About](https://medium.com/about?autoplay=1&source=post_page-----a5c0acf431dc---------------------------------------)

[Careers](https://medium.com/jobs-at-medium/work-at-medium-959d1a85284e?source=post_page-----a5c0acf431dc---------------------------------------)

Press

[Blog](https://blog.medium.com/?source=post_page-----a5c0acf431dc---------------------------------------)

[Privacy](https://policy.medium.com/medium-privacy-policy-f03bf92035c9?source=post_page-----a5c0acf431dc---------------------------------------)

[Rules](https://policy.medium.com/medium-rules-30e5502c4eb4?source=post_page-----a5c0acf431dc---------------------------------------)

[Terms](https://policy.medium.com/medium-terms-of-service-9db0094a1e0f?source=post_page-----a5c0acf431dc---------------------------------------)

[Text to speech](https://speechify.com/medium?source=post_page-----a5c0acf431dc---------------------------------------)