---
title: XSS | Here’s how I got my first bounty
url: https://infosecwriteups.com/xss-heres-how-i-got-my-first-bounty-4f64785fe6f8?source=rss----7b722bfd1b8d--bug_bounty
source: Bug Bounty in InfoSec Write-ups on Medium
date: 2024-11-22
fetch_date: 2025-10-06T19:15:44.236052
---

# XSS | Here’s how I got my first bounty

[Sitemap](/sitemap/sitemap.xml)

[Open in app](https://rsci.app.link/?%24canonical_url=https%3A%2F%2Fmedium.com%2Fp%2F4f64785fe6f8&%7Efeature=LoOpenInAppButton&%7Echannel=ShowPostUnderCollection&%7Estage=mobileNavBar&source=post_page---top_nav_layout_nav-----------------------------------------)

Sign up

[Sign in](https://medium.com/m/signin?operation=login&redirect=https%3A%2F%2Finfosecwriteups.com%2Fxss-heres-how-i-got-my-first-bounty-4f64785fe6f8&source=post_page---top_nav_layout_nav-----------------------global_nav------------------)

[Medium Logo](https://medium.com/?source=post_page---top_nav_layout_nav-----------------------------------------)

[Write](https://medium.com/m/signin?operation=register&redirect=https%3A%2F%2Fmedium.com%2Fnew-story&source=---top_nav_layout_nav-----------------------new_post_topnav------------------)

[Search](https://medium.com/search?source=post_page---top_nav_layout_nav-----------------------------------------)

Sign up

[Sign in](https://medium.com/m/signin?operation=login&redirect=https%3A%2F%2Finfosecwriteups.com%2Fxss-heres-how-i-got-my-first-bounty-4f64785fe6f8&source=post_page---top_nav_layout_nav-----------------------global_nav------------------)

![](https://miro.medium.com/v2/resize:fill:64:64/1*dmbNkD5D-u45r44go_cf0g.png)

[## InfoSec Write-ups](https://infosecwriteups.com/?source=post_page---publication_nav-7b722bfd1b8d-4f64785fe6f8---------------------------------------)

·

Follow publication

[![InfoSec Write-ups](https://miro.medium.com/v2/resize:fill:76:76/1*SWJxYWGZzgmBP1D0Qg_3zQ.png)](https://infosecwriteups.com/?source=post_page---post_publication_sidebar-7b722bfd1b8d-4f64785fe6f8---------------------------------------)

A collection of write-ups from the best hackers in the world on topics ranging from bug bounties and CTFs to vulnhub machines, hardware challenges and real life encounters. Subscribe to our weekly newsletter for the coolest infosec updates: <https://weekly.infosecwriteups.com/>

Follow publication

Member-only story

# XSS | Here’s How I Got My First Bounty

[![sM0ky4](https://miro.medium.com/v2/resize:fill:64:64/1*cFVgTzwcM6pV7xIFewPJvw.png)](https://medium.com/%40sM0ky4?source=post_page---byline--4f64785fe6f8---------------------------------------)

[sM0ky4](https://medium.com/%40sM0ky4?source=post_page---byline--4f64785fe6f8---------------------------------------)

2 min read

·

May 9, 2024

--

12

Share

Not so long ago, I was reading blogs like this, wondering how to find my first vulnerability in a bug bounty program and probably not thinking that I would get a bounty a little after.

But here we are, having made the decision to revisit a target that seemed initially too big to me as I was only a beginner, I found a reflected XSS vulnerability.

![]()

Was it hard to find? Not really. Did I get lucky? Maybe.

My main goal was to find an XSS, so I was searching for user inputs. I started testing the search bar by entering a random string in order to observe the behavior of the web app. Looking at the response in the Browser DevTools, I saw that my double quotes were not filtered, and I found a tag which looked like this :

So, I started trying to bypass it with a double quote in order to close the attribute :

It works, perfect.
Now, let’s exploit this vulnerability to get an XSS. The tag here is a div, so we can use the payload “onpointerover=”alert(‘XSS’)” in a way that the tag looks like this :

Yay, here’s our popup !

Press enter or click to view image in full size

![]()

I was awarded with a $75 bounty for this one. Not a lot for a medium severity, but it brings motivation especially because it confirms to me that it’s still possible to find XSS vulnerabilities in bug bounty programs with over a hundred vulnerabilities already reported.

That’s it,

I really hope you enjoyed this blog and see you for a next one !

--

--

12

[![InfoSec Write-ups](https://miro.medium.com/v2/resize:fill:96:96/1*SWJxYWGZzgmBP1D0Qg_3zQ.png)](https://infosecwriteups.com/?source=post_page---post_publication_info--4f64785fe6f8---------------------------------------)

[![InfoSec Write-ups](https://miro.medium.com/v2/resize:fill:128:128/1*SWJxYWGZzgmBP1D0Qg_3zQ.png)](https://infosecwriteups.com/?source=post_page---post_publication_info--4f64785fe6f8---------------------------------------)

Follow

[## Published in InfoSec Write-ups](https://infosecwriteups.com/?source=post_page---post_publication_info--4f64785fe6f8---------------------------------------)

[71K followers](/followers?source=post_page---post_publication_info--4f64785fe6f8---------------------------------------)

·[Last published 4 hours ago](/baby-dfc2547dc387?source=post_page---post_publication_info--4f64785fe6f8---------------------------------------)

A collection of write-ups from the best hackers in the world on topics ranging from bug bounties and CTFs to vulnhub machines, hardware challenges and real life encounters. Subscribe to our weekly newsletter for the coolest infosec updates: <https://weekly.infosecwriteups.com/>

Follow

[![sM0ky4](https://miro.medium.com/v2/resize:fill:96:96/1*cFVgTzwcM6pV7xIFewPJvw.png)](https://medium.com/%40sM0ky4?source=post_page---post_author_info--4f64785fe6f8---------------------------------------)

[![sM0ky4](https://miro.medium.com/v2/resize:fill:128:128/1*cFVgTzwcM6pV7xIFewPJvw.png)](https://medium.com/%40sM0ky4?source=post_page---post_author_info--4f64785fe6f8---------------------------------------)

[## Written by sM0ky4](https://medium.com/%40sM0ky4?source=post_page---post_author_info--4f64785fe6f8---------------------------------------)

[293 followers](https://medium.com/%40sM0ky4/followers?source=post_page---post_author_info--4f64785fe6f8---------------------------------------)

·[12 following](https://medium.com/%40sM0ky4/following?source=post_page---post_author_info--4f64785fe6f8---------------------------------------)

🇨🇭 | Bug Bounty Hunter | <https://buymeacoffee.com/sM0ky4> ☕

## Responses (12)

See all responses

[Help](https://help.medium.com/hc/en-us?source=post_page-----4f64785fe6f8---------------------------------------)

[Status](https://status.medium.com/?source=post_page-----4f64785fe6f8---------------------------------------)

[About](https://medium.com/about?autoplay=1&source=post_page-----4f64785fe6f8---------------------------------------)

[Careers](https://medium.com/jobs-at-medium/work-at-medium-959d1a85284e?source=post_page-----4f64785fe6f8---------------------------------------)

Press

[Blog](https://blog.medium.com/?source=post_page-----4f64785fe6f8---------------------------------------)

[Privacy](https://policy.medium.com/medium-privacy-policy-f03bf92035c9?source=post_page-----4f64785fe6f8---------------------------------------)

[Rules](https://policy.medium.com/medium-rules-30e5502c4eb4?source=post_page-----4f64785fe6f8---------------------------------------)

[Terms](https://policy.medium.com/medium-terms-of-service-9db0094a1e0f?source=post_page-----4f64785fe6f8---------------------------------------)

[Text to speech](https://speechify.com/medium?source=post_page-----4f64785fe6f8---------------------------------------)