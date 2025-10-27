---
title: HTTP Header Injection
url: https://infosecwriteups.com/http-header-injection-4ba857fb9a16?source=rss----7b722bfd1b8d--bug_bounty
source: Bug Bounty in InfoSec Write-ups on Medium
date: 2022-12-23
fetch_date: 2025-10-04T02:19:22.556149
---

# HTTP Header Injection

[Sitemap](/sitemap/sitemap.xml)

[Open in app](https://rsci.app.link/?%24canonical_url=https%3A%2F%2Fmedium.com%2Fp%2F4ba857fb9a16&%7Efeature=LoOpenInAppButton&%7Echannel=ShowPostUnderCollection&%7Estage=mobileNavBar&source=post_page---top_nav_layout_nav-----------------------------------------)

Sign up

[Sign in](https://medium.com/m/signin?operation=login&redirect=https%3A%2F%2Finfosecwriteups.com%2Fhttp-header-injection-4ba857fb9a16&source=post_page---top_nav_layout_nav-----------------------global_nav------------------)

[Medium Logo](https://medium.com/?source=post_page---top_nav_layout_nav-----------------------------------------)

[Write](https://medium.com/m/signin?operation=register&redirect=https%3A%2F%2Fmedium.com%2Fnew-story&source=---top_nav_layout_nav-----------------------new_post_topnav------------------)

[Search](https://medium.com/search?source=post_page---top_nav_layout_nav-----------------------------------------)

Sign up

[Sign in](https://medium.com/m/signin?operation=login&redirect=https%3A%2F%2Finfosecwriteups.com%2Fhttp-header-injection-4ba857fb9a16&source=post_page---top_nav_layout_nav-----------------------global_nav------------------)

![](https://miro.medium.com/v2/resize:fill:64:64/1*dmbNkD5D-u45r44go_cf0g.png)

[## InfoSec Write-ups](https://infosecwriteups.com/?source=post_page---publication_nav-7b722bfd1b8d-4ba857fb9a16---------------------------------------)

·

Follow publication

[![InfoSec Write-ups](https://miro.medium.com/v2/resize:fill:76:76/1*SWJxYWGZzgmBP1D0Qg_3zQ.png)](https://infosecwriteups.com/?source=post_page---post_publication_sidebar-7b722bfd1b8d-4ba857fb9a16---------------------------------------)

A collection of write-ups from the best hackers in the world on topics ranging from bug bounties and CTFs to vulnhub machines, hardware challenges and real life encounters. Subscribe to our weekly newsletter for the coolest infosec updates: <https://weekly.infosecwriteups.com/>

Follow publication

Member-only story

# **HTTP Header Injection**

[![Security Lit Limited](https://miro.medium.com/v2/resize:fill:64:64/1*yrQrISi6PlPkHrHAS2ai3g.png)](https://securitylit.medium.com/?source=post_page---byline--4ba857fb9a16---------------------------------------)

[Security Lit Limited](https://securitylit.medium.com/?source=post_page---byline--4ba857fb9a16---------------------------------------)

5 min read

·

Mar 29, 2022

--

Share

Press enter or click to view image in full size

![]()

Photo by [Jordan Harrison](https://unsplash.com/%40jordanharrison?utm_source=medium&utm_medium=referral) on [Unsplash](https://unsplash.com/?utm_source=medium&utm_medium=referral)

**What is HTTP Header Injection?**

HTTP Header Injection is a web Security Vulnerability where the web application dynamically constructs headers from the user’s supplied input.

HTTP works on the *Request/Response Model*. The user requests a resource from the web server and the web-server resounds accordingly. HTTP headers are used to request the necessary resources. Headers can be categorized into two major categories. The request and the response headers. The vulnerability occurs when an input supplied by the user is included in the HTTP Response. This can lead to a lot of issues such as bypassing CSRF protection, redirecting users to different domains or bypassing the CSRF protection sometimes.

**Causes**

Press enter or click to view image in full size

![]()

[Source](https://developpaper.com/http-host-header-attacks-for-web-security/)

One of the major causes of HTTP Header Injection is CRLF Injection. CRLF Injection occurs when a HTTP request is interred in a different way by a reverse proxy and in a different way by a web server. CRLF Injection can be used by attackers to bypass restrictions, access Forbidden pages and even cause web cache poisoning.

For Example:

Let’s consider a website that is vulnerable to Header Injection. It takes the URL and…

--

--

[![InfoSec Write-ups](https://miro.medium.com/v2/resize:fill:96:96/1*SWJxYWGZzgmBP1D0Qg_3zQ.png)](https://infosecwriteups.com/?source=post_page---post_publication_info--4ba857fb9a16---------------------------------------)

[![InfoSec Write-ups](https://miro.medium.com/v2/resize:fill:128:128/1*SWJxYWGZzgmBP1D0Qg_3zQ.png)](https://infosecwriteups.com/?source=post_page---post_publication_info--4ba857fb9a16---------------------------------------)

Follow

[## Published in InfoSec Write-ups](https://infosecwriteups.com/?source=post_page---post_publication_info--4ba857fb9a16---------------------------------------)

[71K followers](/followers?source=post_page---post_publication_info--4ba857fb9a16---------------------------------------)

·[Last published 5 days ago](/how-to-find-p1-bugs-using-google-in-your-target-part-1-e37455324dc1?source=post_page---post_publication_info--4ba857fb9a16---------------------------------------)

A collection of write-ups from the best hackers in the world on topics ranging from bug bounties and CTFs to vulnhub machines, hardware challenges and real life encounters. Subscribe to our weekly newsletter for the coolest infosec updates: <https://weekly.infosecwriteups.com/>

Follow

[![Security Lit Limited](https://miro.medium.com/v2/resize:fill:96:96/1*yrQrISi6PlPkHrHAS2ai3g.png)](https://securitylit.medium.com/?source=post_page---post_author_info--4ba857fb9a16---------------------------------------)

[![Security Lit Limited](https://miro.medium.com/v2/resize:fill:128:128/1*yrQrISi6PlPkHrHAS2ai3g.png)](https://securitylit.medium.com/?source=post_page---post_author_info--4ba857fb9a16---------------------------------------)

[## Written by Security Lit Limited](https://securitylit.medium.com/?source=post_page---post_author_info--4ba857fb9a16---------------------------------------)

[2K followers](https://securitylit.medium.com/followers?source=post_page---post_author_info--4ba857fb9a16---------------------------------------)

·[150 following](https://medium.com/%40securitylit/following?source=post_page---post_author_info--4ba857fb9a16---------------------------------------)

<https://securitylit.com/contact>

## No responses yet

[Help](https://help.medium.com/hc/en-us?source=post_page-----4ba857fb9a16---------------------------------------)

[Status](https://status.medium.com/?source=post_page-----4ba857fb9a16---------------------------------------)

[About](https://medium.com/about?autoplay=1&source=post_page-----4ba857fb9a16---------------------------------------)

[Careers](https://medium.com/jobs-at-medium/work-at-medium-959d1a85284e?source=post_page-----4ba857fb9a16---------------------------------------)

Press

[Blog](https://blog.medium.com/?source=post_page-----4ba857fb9a16---------------------------------------)

[Privacy](https://policy.medium.com/medium-privacy-policy-f03bf92035c9?source=post_page-----4ba857fb9a16---------------------------------------)

[Rules](https://policy.medium.com/medium-rules-30e5502c4eb4?source=post_page-----4ba857fb9a16---------------------------------------)

[Terms](https://policy.medium.com/medium-terms-of-service-9db0094a1e0f?source=post_page-----4ba857fb9a16---------------------------------------)

[Text to speech](https://speechify.com/medium?source=post_page-----4ba857fb9a16---------------------------------------)