---
title: Parameter tampering result in product price manipulation
url: https://infosecwriteups.com/parameter-tampering-result-in-product-price-manipulation-356c07a571e5?source=rss----7b722bfd1b8d--bug_bounty
source: Bug Bounty in InfoSec Write-ups on Medium
date: 2024-10-24
fetch_date: 2025-10-06T18:50:35.020505
---

# Parameter tampering result in product price manipulation

[Sitemap](/sitemap/sitemap.xml)

[Open in app](https://rsci.app.link/?%24canonical_url=https%3A%2F%2Fmedium.com%2Fp%2F356c07a571e5&%7Efeature=LoOpenInAppButton&%7Echannel=ShowPostUnderCollection&%7Estage=mobileNavBar&source=post_page---top_nav_layout_nav-----------------------------------------)

Sign up

[Sign in](https://medium.com/m/signin?operation=login&redirect=https%3A%2F%2Finfosecwriteups.com%2Fparameter-tampering-result-in-product-price-manipulation-356c07a571e5&source=post_page---top_nav_layout_nav-----------------------global_nav------------------)

[Medium Logo](https://medium.com/?source=post_page---top_nav_layout_nav-----------------------------------------)

[Write](https://medium.com/m/signin?operation=register&redirect=https%3A%2F%2Fmedium.com%2Fnew-story&source=---top_nav_layout_nav-----------------------new_post_topnav------------------)

[Search](https://medium.com/search?source=post_page---top_nav_layout_nav-----------------------------------------)

Sign up

[Sign in](https://medium.com/m/signin?operation=login&redirect=https%3A%2F%2Finfosecwriteups.com%2Fparameter-tampering-result-in-product-price-manipulation-356c07a571e5&source=post_page---top_nav_layout_nav-----------------------global_nav------------------)

![](https://miro.medium.com/v2/resize:fill:64:64/1*dmbNkD5D-u45r44go_cf0g.png)

[## InfoSec Write-ups](https://infosecwriteups.com/?source=post_page---publication_nav-7b722bfd1b8d-356c07a571e5---------------------------------------)

·

Follow publication

[![InfoSec Write-ups](https://miro.medium.com/v2/resize:fill:76:76/1*SWJxYWGZzgmBP1D0Qg_3zQ.png)](https://infosecwriteups.com/?source=post_page---post_publication_sidebar-7b722bfd1b8d-356c07a571e5---------------------------------------)

A collection of write-ups from the best hackers in the world on topics ranging from bug bounties and CTFs to vulnhub machines, hardware challenges and real life encounters. Subscribe to our weekly newsletter for the coolest infosec updates: <https://weekly.infosecwriteups.com/>

Follow publication

# **Parameter tampering result in product price manipulation 😎**

[![Raunak Gupta Aka Biscuit](https://miro.medium.com/v2/resize:fill:64:64/1*8CWlTBYd15lEaEd8vlSztw.jpeg)](https://medium.com/%40RaunakGupta1922?source=post_page---byline--356c07a571e5---------------------------------------)

[Raunak Gupta Aka Biscuit](https://medium.com/%40RaunakGupta1922?source=post_page---byline--356c07a571e5---------------------------------------)

2 min read

·

Aug 31, 2024

--

6

Listen

Share

**Free Article link:** [**Hereeee!!!**](https://medium.com/%40RaunakGupta1922/parameter-tampering-result-in-product-price-manipulation-356c07a571e5?sk=44a93188d0b7558a00980769ef35900b)
*Today, I’m excited to share the story of how I was able to* temper a parameter in HTTP request leads to final price manipulation.

> ***All The Sensitive Data is blurred Due To Privacy Reason
> so for now we call it redacted.com.***

```
---------------------
*Working of Web App*
---------------------

1. Navigate to redacted.com
2. Choose the course which you like to buy
3. Enter details like name, phone number, address, etc
4. Click on "Place Order"
5. Then on integrated "RazorPay" panel you can pay using various
   paying methods like Card, Net Banking, UPI

-----------------------------
*Main Cause of Vulnerability*
-----------------------------
There are no proper validation of Final Price on client side and server side
due to which any attacker can intercept "Place Order" HTTP request
and manipulate final price
```

Press enter or click to view image in full size

![]()

After choosing some random course I entered my details & intercept the HTTP request so I can analysis it further

Press enter or click to view image in full size

![]()

Price of the course was fixed and cant not be altered through front end

Press enter or click to view image in full size

![]()

In HTTP request you can notice there are two interesting parameters which caught my attention.

> **&amount=300
> &gross\_total=300**

After changing the parameters values from 300 to 30 I forwarded the request and ***Boom!!!***

Press enter or click to view image in full size

![]()

Final price was reflecting as 30 INR and now you just need to pay the amount for 30 INR

But sometimes these changes only happen on the client side and don’t affect the server side, which is crucial for completing the final payment.

Still at this point I wasn’t really sure if I was able change the final price, To clear my doubt I paid the 30 INR and I got the receipt for that

I quickly prepared the **“Vulnerability Disclosure Report”** with all the image and video proofs I was able to attach and reported through their email.

[Hacking](https://medium.com/tag/hacking?source=post_page-----356c07a571e5---------------------------------------)

[Cybersecurity](https://medium.com/tag/cybersecurity?source=post_page-----356c07a571e5---------------------------------------)

[Bug Bounty](https://medium.com/tag/bug-bounty?source=post_page-----356c07a571e5---------------------------------------)

[College](https://medium.com/tag/college?source=post_page-----356c07a571e5---------------------------------------)

[Business](https://medium.com/tag/business?source=post_page-----356c07a571e5---------------------------------------)

--

--

6

[![InfoSec Write-ups](https://miro.medium.com/v2/resize:fill:96:96/1*SWJxYWGZzgmBP1D0Qg_3zQ.png)](https://infosecwriteups.com/?source=post_page---post_publication_info--356c07a571e5---------------------------------------)

[![InfoSec Write-ups](https://miro.medium.com/v2/resize:fill:128:128/1*SWJxYWGZzgmBP1D0Qg_3zQ.png)](https://infosecwriteups.com/?source=post_page---post_publication_info--356c07a571e5---------------------------------------)

Follow

[## Published in InfoSec Write-ups](https://infosecwriteups.com/?source=post_page---post_publication_info--356c07a571e5---------------------------------------)

[71K followers](/followers?source=post_page---post_publication_info--356c07a571e5---------------------------------------)

·[Last published 3 hours ago](/baby-dfc2547dc387?source=post_page---post_publication_info--356c07a571e5---------------------------------------)

A collection of write-ups from the best hackers in the world on topics ranging from bug bounties and CTFs to vulnhub machines, hardware challenges and real life encounters. Subscribe to our weekly newsletter for the coolest infosec updates: <https://weekly.infosecwriteups.com/>

Follow

[![Raunak Gupta Aka Biscuit](https://miro.medium.com/v2/resize:fill:96:96/1*8CWlTBYd15lEaEd8vlSztw.jpeg)](https://medium.com/%40RaunakGupta1922?source=post_page---post_author_info--356c07a571e5---------------------------------------)

[![Raunak Gupta Aka Biscuit](https://miro.medium.com/v2/resize:fill:128:128/1*8CWlTBYd15lEaEd8vlSztw.jpeg)](https://medium.com/%40RaunakGupta1922?source=post_page---post_author_info--356c07a571e5---------------------------------------)

[## Written by Raunak Gupta Aka Biscuit](https://medium.com/%40RaunakGupta1922?source=post_page---post_author_info--356c07a571e5---------------------------------------)

[1.2K followers](https://medium.com/%40RaunakGupta1922/followers?source=post_page---post_author_info--356c07a571e5---------------------------------------)

·[117 following](https://medium.com/%40RaunakGupta1922/following?source=post_page---post_author_info--356c07a571e5---------------------------------------)

Bug Bounty Hunter | InfoSec Blogger

## Responses (6)

See all responses

[Help](https://help.medium.com/hc/en-us?source=post_page-----356c07a571e5---------------------------------------)

[Status](https://status.medium.com/?source=post_page-----356c07a571e5---------------------------------------)

[About](https://medium.com/about?autoplay=1&source=post_page-----356c07a571e5---------------------------------------)

[Careers](https://medium.com/jobs-at-medium/work-at-medium-959d1a85284e?source=post_page-----356c07a571e5-----...