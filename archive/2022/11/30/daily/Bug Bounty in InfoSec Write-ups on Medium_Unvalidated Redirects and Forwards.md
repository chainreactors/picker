---
title: Unvalidated Redirects and Forwards
url: https://infosecwriteups.com/unvalidated-redirects-and-forwards-4cad5eb66b64?source=rss----7b722bfd1b8d--bug_bounty
source: Bug Bounty in InfoSec Write-ups on Medium
date: 2022-11-30
fetch_date: 2025-10-04T00:04:17.658633
---

# Unvalidated Redirects and Forwards

[Sitemap](/sitemap/sitemap.xml)

[Open in app](https://rsci.app.link/?%24canonical_url=https%3A%2F%2Fmedium.com%2Fp%2F4cad5eb66b64&%7Efeature=LoOpenInAppButton&%7Echannel=ShowPostUnderCollection&%7Estage=mobileNavBar&source=post_page---top_nav_layout_nav-----------------------------------------)

Sign up

[Sign in](https://medium.com/m/signin?operation=login&redirect=https%3A%2F%2Finfosecwriteups.com%2Funvalidated-redirects-and-forwards-4cad5eb66b64&source=post_page---top_nav_layout_nav-----------------------global_nav------------------)

[Medium Logo](https://medium.com/?source=post_page---top_nav_layout_nav-----------------------------------------)

[Write](https://medium.com/m/signin?operation=register&redirect=https%3A%2F%2Fmedium.com%2Fnew-story&source=---top_nav_layout_nav-----------------------new_post_topnav------------------)

[Search](https://medium.com/search?source=post_page---top_nav_layout_nav-----------------------------------------)

Sign up

[Sign in](https://medium.com/m/signin?operation=login&redirect=https%3A%2F%2Finfosecwriteups.com%2Funvalidated-redirects-and-forwards-4cad5eb66b64&source=post_page---top_nav_layout_nav-----------------------global_nav------------------)

![](https://miro.medium.com/v2/resize:fill:64:64/1*dmbNkD5D-u45r44go_cf0g.png)

[## InfoSec Write-ups](https://infosecwriteups.com/?source=post_page---publication_nav-7b722bfd1b8d-4cad5eb66b64---------------------------------------)

·

Follow publication

[![InfoSec Write-ups](https://miro.medium.com/v2/resize:fill:76:76/1*SWJxYWGZzgmBP1D0Qg_3zQ.png)](https://infosecwriteups.com/?source=post_page---post_publication_sidebar-7b722bfd1b8d-4cad5eb66b64---------------------------------------)

A collection of write-ups from the best hackers in the world on topics ranging from bug bounties and CTFs to vulnhub machines, hardware challenges and real life encounters. Subscribe to our weekly newsletter for the coolest infosec updates: <https://weekly.infosecwriteups.com/>

Follow publication

Member-only story

# Unvalidated Redirects and Forwards

[![Security Lit Limited](https://miro.medium.com/v2/resize:fill:64:64/1*yrQrISi6PlPkHrHAS2ai3g.png)](https://securitylit.medium.com/?source=post_page---byline--4cad5eb66b64---------------------------------------)

[Security Lit Limited](https://securitylit.medium.com/?source=post_page---byline--4cad5eb66b64---------------------------------------)

5 min read

·

Nov 29, 2022

--

Share

![]()

Photo by [Jefferson Santos](https://unsplash.com/%40jefflssantos?utm_source=unsplash&utm_medium=referral&utm_content=creditCopyText) on [Unsplash](https://unsplash.com/%40jefflssantos?utm_source=unsplash&utm_medium=referral&utm_content=creditCopyText)

**Introduction**

Unvalidated Redirects and Forwards might no longer occupy a place in the OWASP Top 10 basket of most common vulnerabilities, as it did in 2013 and 2017, it is however known to harm your reputation. To know what it is and how it can affect your reputation, let’s understand Redirects and Forwards. You might want to learn about a 302 Response Status code, which refers to Temporary Redirect.

**What is a Redirect and Forward?**

Press enter or click to view image in full size

![]()

[Source](https://i.stack.imgur.com/a3pCn.png)

For the sake of this argument, let’s consider Bob, the admin of the site bob.com. He wants to temporarily fix his site but, at the same time, doesn’t want the users to suffer because of the downtime. An idea strikes his mind. He thinks of redirecting his traffic to his friend Alice’s site, called **alice.com.**

So, what he does is, opens his admin panel and set up a 302 redirect to **alice.com** for any incoming request to bob.com.

What this will do is, if I, as a user will type in **bob.com** in my web browser, it’ll take me to bob.com, but the bob’s server, instead of returning me the webpage, will return me a 302 Status code, and a location header of **alice.com**. This will instruct my browser to…

--

--

[![InfoSec Write-ups](https://miro.medium.com/v2/resize:fill:96:96/1*SWJxYWGZzgmBP1D0Qg_3zQ.png)](https://infosecwriteups.com/?source=post_page---post_publication_info--4cad5eb66b64---------------------------------------)

[![InfoSec Write-ups](https://miro.medium.com/v2/resize:fill:128:128/1*SWJxYWGZzgmBP1D0Qg_3zQ.png)](https://infosecwriteups.com/?source=post_page---post_publication_info--4cad5eb66b64---------------------------------------)

Follow

[## Published in InfoSec Write-ups](https://infosecwriteups.com/?source=post_page---post_publication_info--4cad5eb66b64---------------------------------------)

[71K followers](/followers?source=post_page---post_publication_info--4cad5eb66b64---------------------------------------)

·[Last published 5 days ago](/how-to-find-p1-bugs-using-google-in-your-target-part-1-e37455324dc1?source=post_page---post_publication_info--4cad5eb66b64---------------------------------------)

A collection of write-ups from the best hackers in the world on topics ranging from bug bounties and CTFs to vulnhub machines, hardware challenges and real life encounters. Subscribe to our weekly newsletter for the coolest infosec updates: <https://weekly.infosecwriteups.com/>

Follow

[![Security Lit Limited](https://miro.medium.com/v2/resize:fill:96:96/1*yrQrISi6PlPkHrHAS2ai3g.png)](https://securitylit.medium.com/?source=post_page---post_author_info--4cad5eb66b64---------------------------------------)

[![Security Lit Limited](https://miro.medium.com/v2/resize:fill:128:128/1*yrQrISi6PlPkHrHAS2ai3g.png)](https://securitylit.medium.com/?source=post_page---post_author_info--4cad5eb66b64---------------------------------------)

[## Written by Security Lit Limited](https://securitylit.medium.com/?source=post_page---post_author_info--4cad5eb66b64---------------------------------------)

[2K followers](https://securitylit.medium.com/followers?source=post_page---post_author_info--4cad5eb66b64---------------------------------------)

·[150 following](https://medium.com/%40securitylit/following?source=post_page---post_author_info--4cad5eb66b64---------------------------------------)

<https://securitylit.com/contact>

## No responses yet

[Help](https://help.medium.com/hc/en-us?source=post_page-----4cad5eb66b64---------------------------------------)

[Status](https://status.medium.com/?source=post_page-----4cad5eb66b64---------------------------------------)

[About](https://medium.com/about?autoplay=1&source=post_page-----4cad5eb66b64---------------------------------------)

[Careers](https://medium.com/jobs-at-medium/work-at-medium-959d1a85284e?source=post_page-----4cad5eb66b64---------------------------------------)

Press

[Blog](https://blog.medium.com/?source=post_page-----4cad5eb66b64---------------------------------------)

[Privacy](https://policy.medium.com/medium-privacy-policy-f03bf92035c9?source=post_page-----4cad5eb66b64---------------------------------------)

[Rules](https://policy.medium.com/medium-rules-30e5502c4eb4?source=post_page-----4cad5eb66b64---------------------------------------)

[Terms](https://policy.medium.com/medium-terms-of-service-9db0094a1e0f?source=post_page-----4cad5eb66b64---------------------------------------)

[Text to speech](https://speechify.com/medium?source=post_page-----4cad5eb66b64---------------------------------------)