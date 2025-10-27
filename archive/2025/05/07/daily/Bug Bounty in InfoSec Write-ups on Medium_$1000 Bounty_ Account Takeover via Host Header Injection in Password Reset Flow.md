---
title: $1000 Bounty: Account Takeover via Host Header Injection in Password Reset Flow
url: https://infosecwriteups.com/1000-bounty-account-takeover-via-host-header-injection-in-password-reset-flow-dc0cdb2d972b?source=rss----7b722bfd1b8d--bug_bounty
source: Bug Bounty in InfoSec Write-ups on Medium
date: 2025-05-07
fetch_date: 2025-10-06T22:25:43.855809
---

# $1000 Bounty: Account Takeover via Host Header Injection in Password Reset Flow

[Sitemap](/sitemap/sitemap.xml)

[Open in app](https://rsci.app.link/?%24canonical_url=https%3A%2F%2Fmedium.com%2Fp%2Fdc0cdb2d972b&%7Efeature=LoOpenInAppButton&%7Echannel=ShowPostUnderCollection&%7Estage=mobileNavBar&source=post_page---top_nav_layout_nav-----------------------------------------)

Sign up

[Sign in](https://medium.com/m/signin?operation=login&redirect=https%3A%2F%2Finfosecwriteups.com%2F1000-bounty-account-takeover-via-host-header-injection-in-password-reset-flow-dc0cdb2d972b&source=post_page---top_nav_layout_nav-----------------------global_nav------------------)

[Medium Logo](https://medium.com/?source=post_page---top_nav_layout_nav-----------------------------------------)

[Write](https://medium.com/m/signin?operation=register&redirect=https%3A%2F%2Fmedium.com%2Fnew-story&source=---top_nav_layout_nav-----------------------new_post_topnav------------------)

[Search](https://medium.com/search?source=post_page---top_nav_layout_nav-----------------------------------------)

Sign up

[Sign in](https://medium.com/m/signin?operation=login&redirect=https%3A%2F%2Finfosecwriteups.com%2F1000-bounty-account-takeover-via-host-header-injection-in-password-reset-flow-dc0cdb2d972b&source=post_page---top_nav_layout_nav-----------------------global_nav------------------)

![](https://miro.medium.com/v2/resize:fill:64:64/1*dmbNkD5D-u45r44go_cf0g.png)

[## InfoSec Write-ups](https://infosecwriteups.com/?source=post_page---publication_nav-7b722bfd1b8d-dc0cdb2d972b---------------------------------------)

·

Follow publication

[![InfoSec Write-ups](https://miro.medium.com/v2/resize:fill:76:76/1*SWJxYWGZzgmBP1D0Qg_3zQ.png)](https://infosecwriteups.com/?source=post_page---post_publication_sidebar-7b722bfd1b8d-dc0cdb2d972b---------------------------------------)

A collection of write-ups from the best hackers in the world on topics ranging from bug bounties and CTFs to vulnhub machines, hardware challenges and real life encounters. Subscribe to our weekly newsletter for the coolest infosec updates: <https://weekly.infosecwriteups.com/>

Follow publication

Member-only story

# $1000 Bounty: Account Takeover via Host Header Injection in Password Reset Flow

[![Ehtesham Ul Haq](https://miro.medium.com/v2/resize:fill:64:64/1*Ol6i1EKzTepUIEn8uE8KJg.png)](https://ehteshamulhaq198.medium.com/?source=post_page---byline--dc0cdb2d972b---------------------------------------)

[Ehtesham Ul Haq](https://ehteshamulhaq198.medium.com/?source=post_page---byline--dc0cdb2d972b---------------------------------------)

4 min read

·

May 2, 2025

--

4

Share

Free Article Link: [Click for free!](https://ehteshamulhaq198.medium.com/1000-bounty-account-takeover-via-host-header-injection-in-password-reset-flow-dc0cdb2d972b?sk=c99b35580d8cd4534a394437f7917f54)

![]()

> ***A simple header… a full takeover.***

Hey folks!

Today I want to share one of my favorite findings — a simple but deadly **Host Header Injection** that led to **full account takeover** via password reset link manipulation. It’s wild how a single overlooked header can lead to such critical impact.

Let me walk you through how I found this bug, chained it for max effect, and walked away with a **$1000 reward**.

## The Setup

Like any good recon session, I was exploring forgotten corners of **target.com** when I decided to test their password reset functionality. Why? Because “Forgot Password” flows are often goldmines — especially when developers get lazy with URL generation.

I typed in my email, hit the “Reset” button, and intercepted the request with Burp Suite.

Here’s the request:

```
POST /signup/send-password-reset-email HTTP/1.1
Host: target.com
Content-Type: application/json
Content-Length: ...
```

So far, nothing unusual — but I had a hunch.

## The Trick

--

--

4

[![InfoSec Write-ups](https://miro.medium.com/v2/resize:fill:96:96/1*SWJxYWGZzgmBP1D0Qg_3zQ.png)](https://infosecwriteups.com/?source=post_page---post_publication_info--dc0cdb2d972b---------------------------------------)

[![InfoSec Write-ups](https://miro.medium.com/v2/resize:fill:128:128/1*SWJxYWGZzgmBP1D0Qg_3zQ.png)](https://infosecwriteups.com/?source=post_page---post_publication_info--dc0cdb2d972b---------------------------------------)

Follow

[## Published in InfoSec Write-ups](https://infosecwriteups.com/?source=post_page---post_publication_info--dc0cdb2d972b---------------------------------------)

[71K followers](/followers?source=post_page---post_publication_info--dc0cdb2d972b---------------------------------------)

·[Last published 2 hours ago](/actuator-unleashed-a-guide-to-finding-and-exploiting-spring-boot-actuator-endpoints-29252dcd9d79?source=post_page---post_publication_info--dc0cdb2d972b---------------------------------------)

A collection of write-ups from the best hackers in the world on topics ranging from bug bounties and CTFs to vulnhub machines, hardware challenges and real life encounters. Subscribe to our weekly newsletter for the coolest infosec updates: <https://weekly.infosecwriteups.com/>

Follow

[![Ehtesham Ul Haq](https://miro.medium.com/v2/resize:fill:96:96/1*Ol6i1EKzTepUIEn8uE8KJg.png)](https://ehteshamulhaq198.medium.com/?source=post_page---post_author_info--dc0cdb2d972b---------------------------------------)

[![Ehtesham Ul Haq](https://miro.medium.com/v2/resize:fill:128:128/1*Ol6i1EKzTepUIEn8uE8KJg.png)](https://ehteshamulhaq198.medium.com/?source=post_page---post_author_info--dc0cdb2d972b---------------------------------------)

[## Written by Ehtesham Ul Haq](https://ehteshamulhaq198.medium.com/?source=post_page---post_author_info--dc0cdb2d972b---------------------------------------)

[520 followers](https://ehteshamulhaq198.medium.com/followers?source=post_page---post_author_info--dc0cdb2d972b---------------------------------------)

·[99 following](https://medium.com/%40ehteshamulhaq198/following?source=post_page---post_author_info--dc0cdb2d972b---------------------------------------)

Penetration Tester & Bug Bounty Hunter focused on finding vulnerabilities and helping organizations stay ahead of cyber threats.

## Responses (4)

See all responses

[Help](https://help.medium.com/hc/en-us?source=post_page-----dc0cdb2d972b---------------------------------------)

[Status](https://status.medium.com/?source=post_page-----dc0cdb2d972b---------------------------------------)

[About](https://medium.com/about?autoplay=1&source=post_page-----dc0cdb2d972b---------------------------------------)

[Careers](https://medium.com/jobs-at-medium/work-at-medium-959d1a85284e?source=post_page-----dc0cdb2d972b---------------------------------------)

Press

[Blog](https://blog.medium.com/?source=post_page-----dc0cdb2d972b---------------------------------------)

[Privacy](https://policy.medium.com/medium-privacy-policy-f03bf92035c9?source=post_page-----dc0cdb2d972b---------------------------------------)

[Rules](https://policy.medium.com/medium-rules-30e5502c4eb4?source=post_page-----dc0cdb2d972b---------------------------------------)

[Terms](https://policy.medium.com/medium-terms-of-service-9db0094a1e0f?source=post_page-----dc0cdb2d972b---------------------------------------)

[Text to speech](https://speechify.com/medium?source=post_page-----dc0cdb2d972b---------------------------------------)