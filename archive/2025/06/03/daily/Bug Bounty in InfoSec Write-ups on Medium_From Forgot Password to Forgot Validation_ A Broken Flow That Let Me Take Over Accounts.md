---
title: From Forgot Password to Forgot Validation: A Broken Flow That Let Me Take Over Accounts
url: https://infosecwriteups.com/from-forgot-password-to-forgot-validation-a-broken-flow-that-let-me-take-over-accounts-04fb7c5b7ecc?source=rss----7b722bfd1b8d--bug_bounty
source: Bug Bounty in InfoSec Write-ups on Medium
date: 2025-06-03
fetch_date: 2025-10-06T22:51:46.734971
---

# From Forgot Password to Forgot Validation: A Broken Flow That Let Me Take Over Accounts

[Sitemap](/sitemap/sitemap.xml)

[Open in app](https://rsci.app.link/?%24canonical_url=https%3A%2F%2Fmedium.com%2Fp%2F04fb7c5b7ecc&%7Efeature=LoOpenInAppButton&%7Echannel=ShowPostUnderCollection&%7Estage=mobileNavBar&source=post_page---top_nav_layout_nav-----------------------------------------)

Sign up

[Sign in](https://medium.com/m/signin?operation=login&redirect=https%3A%2F%2Finfosecwriteups.com%2Ffrom-forgot-password-to-forgot-validation-a-broken-flow-that-let-me-take-over-accounts-04fb7c5b7ecc&source=post_page---top_nav_layout_nav-----------------------global_nav------------------)

[Medium Logo](https://medium.com/?source=post_page---top_nav_layout_nav-----------------------------------------)

[Write](https://medium.com/m/signin?operation=register&redirect=https%3A%2F%2Fmedium.com%2Fnew-story&source=---top_nav_layout_nav-----------------------new_post_topnav------------------)

[Search](https://medium.com/search?source=post_page---top_nav_layout_nav-----------------------------------------)

Sign up

[Sign in](https://medium.com/m/signin?operation=login&redirect=https%3A%2F%2Finfosecwriteups.com%2Ffrom-forgot-password-to-forgot-validation-a-broken-flow-that-let-me-take-over-accounts-04fb7c5b7ecc&source=post_page---top_nav_layout_nav-----------------------global_nav------------------)

![](https://miro.medium.com/v2/resize:fill:64:64/1*dmbNkD5D-u45r44go_cf0g.png)

[## InfoSec Write-ups](https://infosecwriteups.com/?source=post_page---publication_nav-7b722bfd1b8d-04fb7c5b7ecc---------------------------------------)

·

Follow publication

[![InfoSec Write-ups](https://miro.medium.com/v2/resize:fill:76:76/1*SWJxYWGZzgmBP1D0Qg_3zQ.png)](https://infosecwriteups.com/?source=post_page---post_publication_sidebar-7b722bfd1b8d-04fb7c5b7ecc---------------------------------------)

A collection of write-ups from the best hackers in the world on topics ranging from bug bounties and CTFs to vulnhub machines, hardware challenges and real life encounters. Subscribe to our weekly newsletter for the coolest infosec updates: <https://weekly.infosecwriteups.com/>

Follow publication

Member-only story

# From Forgot Password to Forgot Validation: A Broken Flow That Let Me Take Over Accounts 🔄🔐

[![Iski](https://miro.medium.com/v2/resize:fill:64:64/1*PpvkjPQ1lY6aTYHT9kDX5w.png)](https://medium.com/%40iski?source=post_page---byline--04fb7c5b7ecc---------------------------------------)

[Iski](https://medium.com/%40iski?source=post_page---byline--04fb7c5b7ecc---------------------------------------)

4 min read

·

Jun 1, 2025

--

1

Share

Free [Link](https://medium.com/%40iski/from-forgot-password-to-forgot-validation-a-broken-flow-that-let-me-take-over-accounts-04fb7c5b7ecc?sk=1f5a204cb1724fbdb9ddcc2a7c50751b) 🎈

Hey there!😁

Press enter or click to view image in full size

![]()

Image by Gemini AI

## ☕️📉 Life Was Good Until My Wi-Fi Bill Showed Up…

One fine Monday, I was chilling, sipping chai, and scrolling memes, thinking life couldn’t get any better. Then boom — a Wi-Fi disconnection mid-TikTok scroll. Checked my balance. Guess what? 0.00 INR. Not even enough to call customer care.

As a certified bug bounty broke boy™, I knew it was time to put my hoodie on, fire up Burp Suite, and hunt for a juicy bug that could pay this damn bill.

## 🧭 Mass Recon: May the Subdomains Be With You

I started my recon routine, as always:

```
subfinder -d target.com -o subs.txt
httpx -l subs.txt -status-code -title -o alive.txt
```

While scanning for misconfigured subdomains, one stood out like a sore thumb:

```
auth-dev.target.com
```

The title said: **“Authentication Dev Portal”**
 And my mind said: **“Attack Surface Alert 🚨”**

--

--

1

[![InfoSec Write-ups](https://miro.medium.com/v2/resize:fill:96:96/1*SWJxYWGZzgmBP1D0Qg_3zQ.png)](https://infosecwriteups.com/?source=post_page---post_publication_info--04fb7c5b7ecc---------------------------------------)

[![InfoSec Write-ups](https://miro.medium.com/v2/resize:fill:128:128/1*SWJxYWGZzgmBP1D0Qg_3zQ.png)](https://infosecwriteups.com/?source=post_page---post_publication_info--04fb7c5b7ecc---------------------------------------)

Follow

[## Published in InfoSec Write-ups](https://infosecwriteups.com/?source=post_page---post_publication_info--04fb7c5b7ecc---------------------------------------)

[71K followers](/followers?source=post_page---post_publication_info--04fb7c5b7ecc---------------------------------------)

·[Last published 2 hours ago](/actuator-unleashed-a-guide-to-finding-and-exploiting-spring-boot-actuator-endpoints-29252dcd9d79?source=post_page---post_publication_info--04fb7c5b7ecc---------------------------------------)

A collection of write-ups from the best hackers in the world on topics ranging from bug bounties and CTFs to vulnhub machines, hardware challenges and real life encounters. Subscribe to our weekly newsletter for the coolest infosec updates: <https://weekly.infosecwriteups.com/>

Follow

[![Iski](https://miro.medium.com/v2/resize:fill:96:96/1*PpvkjPQ1lY6aTYHT9kDX5w.png)](https://medium.com/%40iski?source=post_page---post_author_info--04fb7c5b7ecc---------------------------------------)

[![Iski](https://miro.medium.com/v2/resize:fill:128:128/1*PpvkjPQ1lY6aTYHT9kDX5w.png)](https://medium.com/%40iski?source=post_page---post_author_info--04fb7c5b7ecc---------------------------------------)

[## Written by Iski](https://medium.com/%40iski?source=post_page---post_author_info--04fb7c5b7ecc---------------------------------------)

[1.8K followers](https://medium.com/%40iski/followers?source=post_page---post_author_info--04fb7c5b7ecc---------------------------------------)

·[7 following](https://medium.com/%40iski/following?source=post_page---post_author_info--04fb7c5b7ecc---------------------------------------)

Cybersecurity Researcher | Penetration Tester | Bug Bounty Hunter | Web security| Passionate about cyber security, security automation

## Responses (1)

See all responses

[Help](https://help.medium.com/hc/en-us?source=post_page-----04fb7c5b7ecc---------------------------------------)

[Status](https://status.medium.com/?source=post_page-----04fb7c5b7ecc---------------------------------------)

[About](https://medium.com/about?autoplay=1&source=post_page-----04fb7c5b7ecc---------------------------------------)

[Careers](https://medium.com/jobs-at-medium/work-at-medium-959d1a85284e?source=post_page-----04fb7c5b7ecc---------------------------------------)

Press

[Blog](https://blog.medium.com/?source=post_page-----04fb7c5b7ecc---------------------------------------)

[Privacy](https://policy.medium.com/medium-privacy-policy-f03bf92035c9?source=post_page-----04fb7c5b7ecc---------------------------------------)

[Rules](https://policy.medium.com/medium-rules-30e5502c4eb4?source=post_page-----04fb7c5b7ecc---------------------------------------)

[Terms](https://policy.medium.com/medium-terms-of-service-9db0094a1e0f?source=post_page-----04fb7c5b7ecc---------------------------------------)

[Text to speech](https://speechify.com/medium?source=post_page-----04fb7c5b7ecc---------------------------------------)