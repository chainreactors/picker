---
title: How I Broke Into My Dev Friend’s Website in Less Than 24 Hour
url: https://infosecwriteups.com/how-i-broke-into-my-dev-friends-website-in-less-than-24-hour-6fdb31ad65a1?source=rss----7b722bfd1b8d--bug_bounty
source: Bug Bounty in InfoSec Write-ups on Medium
date: 2024-12-06
fetch_date: 2025-10-06T19:37:32.061024
---

# How I Broke Into My Dev Friend’s Website in Less Than 24 Hour

[Sitemap](/sitemap/sitemap.xml)

[Open in app](https://rsci.app.link/?%24canonical_url=https%3A%2F%2Fmedium.com%2Fp%2F6fdb31ad65a1&%7Efeature=LoOpenInAppButton&%7Echannel=ShowPostUnderCollection&%7Estage=mobileNavBar&source=post_page---top_nav_layout_nav-----------------------------------------)

Sign up

[Sign in](https://medium.com/m/signin?operation=login&redirect=https%3A%2F%2Finfosecwriteups.com%2Fhow-i-broke-into-my-dev-friends-website-in-less-than-24-hour-6fdb31ad65a1&source=post_page---top_nav_layout_nav-----------------------global_nav------------------)

[Medium Logo](https://medium.com/?source=post_page---top_nav_layout_nav-----------------------------------------)

[Write](https://medium.com/m/signin?operation=register&redirect=https%3A%2F%2Fmedium.com%2Fnew-story&source=---top_nav_layout_nav-----------------------new_post_topnav------------------)

[Search](https://medium.com/search?source=post_page---top_nav_layout_nav-----------------------------------------)

Sign up

[Sign in](https://medium.com/m/signin?operation=login&redirect=https%3A%2F%2Finfosecwriteups.com%2Fhow-i-broke-into-my-dev-friends-website-in-less-than-24-hour-6fdb31ad65a1&source=post_page---top_nav_layout_nav-----------------------global_nav------------------)

![](https://miro.medium.com/v2/resize:fill:64:64/1*dmbNkD5D-u45r44go_cf0g.png)

[## InfoSec Write-ups](https://infosecwriteups.com/?source=post_page---publication_nav-7b722bfd1b8d-6fdb31ad65a1---------------------------------------)

·

Follow publication

[![InfoSec Write-ups](https://miro.medium.com/v2/resize:fill:76:76/1*SWJxYWGZzgmBP1D0Qg_3zQ.png)](https://infosecwriteups.com/?source=post_page---post_publication_sidebar-7b722bfd1b8d-6fdb31ad65a1---------------------------------------)

A collection of write-ups from the best hackers in the world on topics ranging from bug bounties and CTFs to vulnhub machines, hardware challenges and real life encounters. Subscribe to our weekly newsletter for the coolest infosec updates: <https://weekly.infosecwriteups.com/>

Follow publication

Member-only story

# **How I Broke Into My Dev Friend’s Website in Less Than 24 Hour**

[![sM0ky4](https://miro.medium.com/v2/resize:fill:64:64/1*cFVgTzwcM6pV7xIFewPJvw.png)](https://medium.com/%40sM0ky4?source=post_page---byline--6fdb31ad65a1---------------------------------------)

[sM0ky4](https://medium.com/%40sM0ky4?source=post_page---byline--6fdb31ad65a1---------------------------------------)

4 min read

·

Dec 5, 2024

--

6

Share

Press enter or click to view image in full size

![]()

You know what they say about ‘bulletproof’ websites? They never are. My dev friend swore his site was unhackable.

I couldn’t resist… Challenge accepted.

Spoiler : It wasn’t.
To be honest, I didn’t expect my developer friend’s website to fall apart this easily. But in just a few hours, I had full control.

As I started searching for vulnerabilities on his website, I came across a simple login form. I decided to check if I could identify any easy yet critical vulnerabilities. Since he’s primarily a web developer and might not know all the ins and outs of securing a website, I was pretty confident I could uncover some easily overlooked weaknesses.

My first idea was to test this login form with some basic SQL injections. So, I fired up my good old friend Burp Suite, attempted to log in, and noticed something interesting : after submitting the form, I was redirected from `*signin.php*` to `*traitSignin.php*`. This revealed the page responsible for processing the submitted data — exactly what I needed to target next.

Press enter or click to view image in full size

![]()

--

--

6

[![InfoSec Write-ups](https://miro.medium.com/v2/resize:fill:96:96/1*SWJxYWGZzgmBP1D0Qg_3zQ.png)](https://infosecwriteups.com/?source=post_page---post_publication_info--6fdb31ad65a1---------------------------------------)

[![InfoSec Write-ups](https://miro.medium.com/v2/resize:fill:128:128/1*SWJxYWGZzgmBP1D0Qg_3zQ.png)](https://infosecwriteups.com/?source=post_page---post_publication_info--6fdb31ad65a1---------------------------------------)

Follow

[## Published in InfoSec Write-ups](https://infosecwriteups.com/?source=post_page---post_publication_info--6fdb31ad65a1---------------------------------------)

[71K followers](/followers?source=post_page---post_publication_info--6fdb31ad65a1---------------------------------------)

·[Last published 4 hours ago](/baby-dfc2547dc387?source=post_page---post_publication_info--6fdb31ad65a1---------------------------------------)

A collection of write-ups from the best hackers in the world on topics ranging from bug bounties and CTFs to vulnhub machines, hardware challenges and real life encounters. Subscribe to our weekly newsletter for the coolest infosec updates: <https://weekly.infosecwriteups.com/>

Follow

[![sM0ky4](https://miro.medium.com/v2/resize:fill:96:96/1*cFVgTzwcM6pV7xIFewPJvw.png)](https://medium.com/%40sM0ky4?source=post_page---post_author_info--6fdb31ad65a1---------------------------------------)

[![sM0ky4](https://miro.medium.com/v2/resize:fill:128:128/1*cFVgTzwcM6pV7xIFewPJvw.png)](https://medium.com/%40sM0ky4?source=post_page---post_author_info--6fdb31ad65a1---------------------------------------)

[## Written by sM0ky4](https://medium.com/%40sM0ky4?source=post_page---post_author_info--6fdb31ad65a1---------------------------------------)

[293 followers](https://medium.com/%40sM0ky4/followers?source=post_page---post_author_info--6fdb31ad65a1---------------------------------------)

·[12 following](https://medium.com/%40sM0ky4/following?source=post_page---post_author_info--6fdb31ad65a1---------------------------------------)

🇨🇭 | Bug Bounty Hunter | <https://buymeacoffee.com/sM0ky4> ☕

## Responses (6)

See all responses

[Help](https://help.medium.com/hc/en-us?source=post_page-----6fdb31ad65a1---------------------------------------)

[Status](https://status.medium.com/?source=post_page-----6fdb31ad65a1---------------------------------------)

[About](https://medium.com/about?autoplay=1&source=post_page-----6fdb31ad65a1---------------------------------------)

[Careers](https://medium.com/jobs-at-medium/work-at-medium-959d1a85284e?source=post_page-----6fdb31ad65a1---------------------------------------)

Press

[Blog](https://blog.medium.com/?source=post_page-----6fdb31ad65a1---------------------------------------)

[Privacy](https://policy.medium.com/medium-privacy-policy-f03bf92035c9?source=post_page-----6fdb31ad65a1---------------------------------------)

[Rules](https://policy.medium.com/medium-rules-30e5502c4eb4?source=post_page-----6fdb31ad65a1---------------------------------------)

[Terms](https://policy.medium.com/medium-terms-of-service-9db0094a1e0f?source=post_page-----6fdb31ad65a1---------------------------------------)

[Text to speech](https://speechify.com/medium?source=post_page-----6fdb31ad65a1---------------------------------------)