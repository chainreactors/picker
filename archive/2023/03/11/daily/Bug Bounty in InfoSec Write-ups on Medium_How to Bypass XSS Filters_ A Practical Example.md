---
title: How to Bypass XSS Filters: A Practical Example
url: https://infosecwriteups.com/how-to-bypass-xss-filters-a-practical-example-3189877fe2ce?source=rss----7b722bfd1b8d--bug_bounty
source: Bug Bounty in InfoSec Write-ups on Medium
date: 2023-03-11
fetch_date: 2025-10-04T09:13:40.413560
---

# How to Bypass XSS Filters: A Practical Example

[Sitemap](/sitemap/sitemap.xml)

[Open in app](https://rsci.app.link/?%24canonical_url=https%3A%2F%2Fmedium.com%2Fp%2F3189877fe2ce&%7Efeature=LoOpenInAppButton&%7Echannel=ShowPostUnderCollection&%7Estage=mobileNavBar&source=post_page---top_nav_layout_nav-----------------------------------------)

Sign up

[Sign in](https://medium.com/m/signin?operation=login&redirect=https%3A%2F%2Finfosecwriteups.com%2Fhow-to-bypass-xss-filters-a-practical-example-3189877fe2ce&source=post_page---top_nav_layout_nav-----------------------global_nav------------------)

[Medium Logo](https://medium.com/?source=post_page---top_nav_layout_nav-----------------------------------------)

[Write](https://medium.com/m/signin?operation=register&redirect=https%3A%2F%2Fmedium.com%2Fnew-story&source=---top_nav_layout_nav-----------------------new_post_topnav------------------)

[Search](https://medium.com/search?source=post_page---top_nav_layout_nav-----------------------------------------)

Sign up

[Sign in](https://medium.com/m/signin?operation=login&redirect=https%3A%2F%2Finfosecwriteups.com%2Fhow-to-bypass-xss-filters-a-practical-example-3189877fe2ce&source=post_page---top_nav_layout_nav-----------------------global_nav------------------)

![](https://miro.medium.com/v2/resize:fill:64:64/1*dmbNkD5D-u45r44go_cf0g.png)

[## InfoSec Write-ups](https://infosecwriteups.com/?source=post_page---publication_nav-7b722bfd1b8d-3189877fe2ce---------------------------------------)

·

Follow publication

[![InfoSec Write-ups](https://miro.medium.com/v2/resize:fill:76:76/1*SWJxYWGZzgmBP1D0Qg_3zQ.png)](https://infosecwriteups.com/?source=post_page---post_publication_sidebar-7b722bfd1b8d-3189877fe2ce---------------------------------------)

A collection of write-ups from the best hackers in the world on topics ranging from bug bounties and CTFs to vulnhub machines, hardware challenges and real life encounters. Subscribe to our weekly newsletter for the coolest infosec updates: <https://weekly.infosecwriteups.com/>

Follow publication

Member-only story

# How to Bypass XSS Filters: A Practical Example

[![Security Lit Limited](https://miro.medium.com/v2/resize:fill:64:64/1*yrQrISi6PlPkHrHAS2ai3g.png)](https://securitylit.medium.com/?source=post_page---byline--3189877fe2ce---------------------------------------)

[Security Lit Limited](https://securitylit.medium.com/?source=post_page---byline--3189877fe2ce---------------------------------------)

4 min read

·

Mar 8, 2023

--

1

Share

Press enter or click to view image in full size

![]()

Photo by [David Pupaza](https://unsplash.com/%40dav420?utm_source=unsplash&utm_medium=referral&utm_content=creditCopyText) on [Unsplash](https://unsplash.com/%40dav420?utm_source=unsplash&utm_medium=referral&utm_content=creditCopyText)

Cross-site scripting (XSS) is a common web application vulnerability that allows attackers to inject malicious scripts into web pages. XSS can be used for various purposes, such as stealing cookies, session hijacking, phishing, defacement, and more.

However, many web applications have implemented XSS filters to prevent or mitigate XSS attacks. XSS filters are mechanisms that scan user input and output for suspicious strings or characters that may indicate an XSS attempt. They may block, encode, sanitize, or remove such input or output.

But XSS filters are not perfect. They can be bypassed by using various techniques that exploit their weaknesses or limitations. In this blog post, we will show you a practical example of how to bypass an XSS filter using character encoding tricks.

Character Encoding Tricks

To bypass filters that rely on scanning text for specific suspicious strings, attackers can encode any number of characters in a variety of ways:

* HTML encoding: This involves using HTML entities to represent characters. For example, `<` can be encoded as `&lt;`, `>` as `&gt;`, and `”` as `&quot;`.
* - URL encoding: This involves using percent signs followed by hexadecimal values to represent characters. For example, `<` can be encoded as…

--

--

1

[![InfoSec Write-ups](https://miro.medium.com/v2/resize:fill:96:96/1*SWJxYWGZzgmBP1D0Qg_3zQ.png)](https://infosecwriteups.com/?source=post_page---post_publication_info--3189877fe2ce---------------------------------------)

[![InfoSec Write-ups](https://miro.medium.com/v2/resize:fill:128:128/1*SWJxYWGZzgmBP1D0Qg_3zQ.png)](https://infosecwriteups.com/?source=post_page---post_publication_info--3189877fe2ce---------------------------------------)

Follow

[## Published in InfoSec Write-ups](https://infosecwriteups.com/?source=post_page---post_publication_info--3189877fe2ce---------------------------------------)

[71K followers](/followers?source=post_page---post_publication_info--3189877fe2ce---------------------------------------)

·[Last published 5 days ago](/how-to-find-p1-bugs-using-google-in-your-target-part-1-e37455324dc1?source=post_page---post_publication_info--3189877fe2ce---------------------------------------)

A collection of write-ups from the best hackers in the world on topics ranging from bug bounties and CTFs to vulnhub machines, hardware challenges and real life encounters. Subscribe to our weekly newsletter for the coolest infosec updates: <https://weekly.infosecwriteups.com/>

Follow

[![Security Lit Limited](https://miro.medium.com/v2/resize:fill:96:96/1*yrQrISi6PlPkHrHAS2ai3g.png)](https://securitylit.medium.com/?source=post_page---post_author_info--3189877fe2ce---------------------------------------)

[![Security Lit Limited](https://miro.medium.com/v2/resize:fill:128:128/1*yrQrISi6PlPkHrHAS2ai3g.png)](https://securitylit.medium.com/?source=post_page---post_author_info--3189877fe2ce---------------------------------------)

[## Written by Security Lit Limited](https://securitylit.medium.com/?source=post_page---post_author_info--3189877fe2ce---------------------------------------)

[2K followers](https://securitylit.medium.com/followers?source=post_page---post_author_info--3189877fe2ce---------------------------------------)

·[150 following](https://medium.com/%40securitylit/following?source=post_page---post_author_info--3189877fe2ce---------------------------------------)

<https://securitylit.com/contact>

## Responses (1)

See all responses

[Help](https://help.medium.com/hc/en-us?source=post_page-----3189877fe2ce---------------------------------------)

[Status](https://status.medium.com/?source=post_page-----3189877fe2ce---------------------------------------)

[About](https://medium.com/about?autoplay=1&source=post_page-----3189877fe2ce---------------------------------------)

[Careers](https://medium.com/jobs-at-medium/work-at-medium-959d1a85284e?source=post_page-----3189877fe2ce---------------------------------------)

Press

[Blog](https://blog.medium.com/?source=post_page-----3189877fe2ce---------------------------------------)

[Privacy](https://policy.medium.com/medium-privacy-policy-f03bf92035c9?source=post_page-----3189877fe2ce---------------------------------------)

[Rules](https://policy.medium.com/medium-rules-30e5502c4eb4?source=post_page-----3189877fe2ce---------------------------------------)

[Terms](https://policy.medium.com/medium-terms-of-service-9db0094a1e0f?source=post_page-----3189877fe2ce---------------------------------------)

[Text to speech](https://speechify.com/medium?source=post_page-----3189877fe2ce---------------------------------------)