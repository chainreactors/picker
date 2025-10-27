---
title: Reflected XSS on Gaming Blog Website
url: https://infosecwriteups.com/reflected-xss-on-gaming-blog-website-edc448d613a3?source=rss----7b722bfd1b8d--bug_bounty
source: Bug Bounty in InfoSec Write-ups on Medium
date: 2025-01-06
fetch_date: 2025-10-06T20:08:05.201766
---

# Reflected XSS on Gaming Blog Website

[Sitemap](/sitemap/sitemap.xml)

[Open in app](https://rsci.app.link/?%24canonical_url=https%3A%2F%2Fmedium.com%2Fp%2Fedc448d613a3&%7Efeature=LoOpenInAppButton&%7Echannel=ShowPostUnderCollection&%7Estage=mobileNavBar&source=post_page---top_nav_layout_nav-----------------------------------------)

Sign up

[Sign in](https://medium.com/m/signin?operation=login&redirect=https%3A%2F%2Finfosecwriteups.com%2Freflected-xss-on-gaming-blog-website-edc448d613a3&source=post_page---top_nav_layout_nav-----------------------global_nav------------------)

[Medium Logo](https://medium.com/?source=post_page---top_nav_layout_nav-----------------------------------------)

[Write](https://medium.com/m/signin?operation=register&redirect=https%3A%2F%2Fmedium.com%2Fnew-story&source=---top_nav_layout_nav-----------------------new_post_topnav------------------)

[Search](https://medium.com/search?source=post_page---top_nav_layout_nav-----------------------------------------)

Sign up

[Sign in](https://medium.com/m/signin?operation=login&redirect=https%3A%2F%2Finfosecwriteups.com%2Freflected-xss-on-gaming-blog-website-edc448d613a3&source=post_page---top_nav_layout_nav-----------------------global_nav------------------)

![](https://miro.medium.com/v2/resize:fill:64:64/1*dmbNkD5D-u45r44go_cf0g.png)

[Mastodon](https://me.dm/%40enigma_)

[## InfoSec Write-ups](https://infosecwriteups.com/?source=post_page---publication_nav-7b722bfd1b8d-edc448d613a3---------------------------------------)

·

Follow publication

[![InfoSec Write-ups](https://miro.medium.com/v2/resize:fill:76:76/1*SWJxYWGZzgmBP1D0Qg_3zQ.png)](https://infosecwriteups.com/?source=post_page---post_publication_sidebar-7b722bfd1b8d-edc448d613a3---------------------------------------)

A collection of write-ups from the best hackers in the world on topics ranging from bug bounties and CTFs to vulnhub machines, hardware challenges and real life encounters. Subscribe to our weekly newsletter for the coolest infosec updates: <https://weekly.infosecwriteups.com/>

Follow publication

Member-only story

# Reflected XSS on Gaming Blog Website

[![enigma_](https://miro.medium.com/v2/resize:fill:64:64/1*Ym19t_vpdbvu02efSrcJXQ.jpeg)](https://medium.com/%40enigma_?source=post_page---byline--edc448d613a3---------------------------------------)

[enigma\_](https://medium.com/%40enigma_?source=post_page---byline--edc448d613a3---------------------------------------)

3 min read

·

Dec 13, 2024

--

Share

I found a reflected XSS vulnerability on a website I used to frequent when playing a text-based MUD (multi user dungeon).

This website had a calculator of sorts, that would determine how much skill you needed to progress to a given level that you would enter into a text input box. I decided to test this and see if it was vulnerable.

Upon inspecting the source code, I see that the javascript shows I’m within a “textarea” tag. So I decided to test this by escaping it.

```
</textarea>
```

I also learned that modern websites are typically defended against the alert() method. We now use the print() method to demonstrate XSS on most modern websites according to Portswigger.

[## What is cross-site scripting (XSS) and how to prevent it? | Web Security Academy

### In this section, we'll explain what cross-site scripting is, describe the different varieties of cross-site scripting…

portswigger.net](https://portswigger.net/web-security/cross-site-scripting?source=post_page-----edc448d613a3---------------------------------------)

## XSS proof of concept

> You can confirm most kinds of XSS vulnerability by injecting a payload that causes your own browser to execute some arbitrary JavaScript. It’s long been common practice to use the `alert()` function for this purpose because it's short, harmless, and pretty hard to miss when it's successfully called. In fact, you solve the majority of our XSS labs by invoking `alert()` in a simulated victim's browser.
>
> Unfortunately, there’s a slight hitch if you use…

--

--

[![InfoSec Write-ups](https://miro.medium.com/v2/resize:fill:96:96/1*SWJxYWGZzgmBP1D0Qg_3zQ.png)](https://infosecwriteups.com/?source=post_page---post_publication_info--edc448d613a3---------------------------------------)

[![InfoSec Write-ups](https://miro.medium.com/v2/resize:fill:128:128/1*SWJxYWGZzgmBP1D0Qg_3zQ.png)](https://infosecwriteups.com/?source=post_page---post_publication_info--edc448d613a3---------------------------------------)

Follow

[## Published in InfoSec Write-ups](https://infosecwriteups.com/?source=post_page---post_publication_info--edc448d613a3---------------------------------------)

[71K followers](/followers?source=post_page---post_publication_info--edc448d613a3---------------------------------------)

·[Last published 5 hours ago](/baby-dfc2547dc387?source=post_page---post_publication_info--edc448d613a3---------------------------------------)

A collection of write-ups from the best hackers in the world on topics ranging from bug bounties and CTFs to vulnhub machines, hardware challenges and real life encounters. Subscribe to our weekly newsletter for the coolest infosec updates: <https://weekly.infosecwriteups.com/>

Follow

[![enigma_](https://miro.medium.com/v2/resize:fill:96:96/1*Ym19t_vpdbvu02efSrcJXQ.jpeg)](https://medium.com/%40enigma_?source=post_page---post_author_info--edc448d613a3---------------------------------------)

[![enigma_](https://miro.medium.com/v2/resize:fill:128:128/1*Ym19t_vpdbvu02efSrcJXQ.jpeg)](https://medium.com/%40enigma_?source=post_page---post_author_info--edc448d613a3---------------------------------------)

[## Written by enigma\_](https://medium.com/%40enigma_?source=post_page---post_author_info--edc448d613a3---------------------------------------)

[374 followers](https://medium.com/%40enigma_/followers?source=post_page---post_author_info--edc448d613a3---------------------------------------)

·[277 following](https://medium.com/%40enigma_/following?source=post_page---post_author_info--edc448d613a3---------------------------------------)

Information Security enthusiast. Targeting OSCP Certification currently.

## No responses yet

[Help](https://help.medium.com/hc/en-us?source=post_page-----edc448d613a3---------------------------------------)

[Status](https://status.medium.com/?source=post_page-----edc448d613a3---------------------------------------)

[About](https://medium.com/about?autoplay=1&source=post_page-----edc448d613a3---------------------------------------)

[Careers](https://medium.com/jobs-at-medium/work-at-medium-959d1a85284e?source=post_page-----edc448d613a3---------------------------------------)

Press

[Blog](https://blog.medium.com/?source=post_page-----edc448d613a3---------------------------------------)

[Privacy](https://policy.medium.com/medium-privacy-policy-f03bf92035c9?source=post_page-----edc448d613a3---------------------------------------)

[Rules](https://policy.medium.com/medium-rules-30e5502c4eb4?source=post_page-----edc448d613a3---------------------------------------)

[Terms](https://policy.medium.com/medium-terms-of-service-9db0094a1e0f?source=post_page-----edc448d613a3---------------------------------------)

[Text to speech](https://speechify.com/medium?source=post_page-----edc448d613a3---------------------------------------)