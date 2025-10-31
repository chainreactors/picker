---
title: The $2,000 Bug That Changed My Life: How a Tiny URL Parameter Broke Web-Store Pricing !!
url: https://infosecwriteups.com/the-2-000-bug-that-changed-my-life-how-a-tiny-url-parameter-broke-web-store-pricing-7275c3d1204b?source=rss----7b722bfd1b8d--bug_bounty
source: Bug Bounty in InfoSec Write-ups on Medium
date: 2025-10-30
fetch_date: 2025-10-31T03:12:49.825935
---

# The $2,000 Bug That Changed My Life: How a Tiny URL Parameter Broke Web-Store Pricing !!

[Sitemap](/sitemap/sitemap.xml)

[Open in app](https://rsci.app.link/?%24canonical_url=https%3A%2F%2Fmedium.com%2Fp%2F7275c3d1204b&%7Efeature=LoOpenInAppButton&%7Echannel=ShowPostUnderCollection&%7Estage=mobileNavBar&source=post_page---top_nav_layout_nav-----------------------------------------)

Sign up

[Sign in](https://medium.com/m/signin?operation=login&redirect=https%3A%2F%2Finfosecwriteups.com%2Fthe-2-000-bug-that-changed-my-life-how-a-tiny-url-parameter-broke-web-store-pricing-7275c3d1204b&source=post_page---top_nav_layout_nav-----------------------global_nav------------------)

[Medium Logo](https://medium.com/?source=post_page---top_nav_layout_nav-----------------------------------------)

[Write](https://medium.com/m/signin?operation=register&redirect=https%3A%2F%2Fmedium.com%2Fnew-story&source=---top_nav_layout_nav-----------------------new_post_topnav------------------)

[Search](https://medium.com/search?source=post_page---top_nav_layout_nav-----------------------------------------)

Sign up

[Sign in](https://medium.com/m/signin?operation=login&redirect=https%3A%2F%2Finfosecwriteups.com%2Fthe-2-000-bug-that-changed-my-life-how-a-tiny-url-parameter-broke-web-store-pricing-7275c3d1204b&source=post_page---top_nav_layout_nav-----------------------global_nav------------------)

![](https://miro.medium.com/v2/resize:fill:64:64/1*dmbNkD5D-u45r44go_cf0g.png)

[## InfoSec Write-ups](https://infosecwriteups.com/?source=post_page---publication_nav-7b722bfd1b8d-7275c3d1204b---------------------------------------)

·

Follow publication

[![InfoSec Write-ups](https://miro.medium.com/v2/resize:fill:76:76/1*SWJxYWGZzgmBP1D0Qg_3zQ.png)](https://infosecwriteups.com/?source=post_page---post_publication_sidebar-7b722bfd1b8d-7275c3d1204b---------------------------------------)

A collection of write-ups from the best hackers in the world on topics ranging from bug bounties and CTFs to vulnhub machines, hardware challenges and real life encounters. Subscribe to our weekly newsletter for the coolest infosec updates: <https://weekly.infosecwriteups.com/>

Follow publication

# The $2,000 Bug That Changed My Life: How a Tiny URL Parameter Broke Web-Store Pricing !!

[![Helmiriahi](https://miro.medium.com/v2/resize:fill:64:64/1*6Kh6mnNLGFm4j2X5sh6qiQ@2x.jpeg)](https://medium.com/%40helmiriahi55?source=post_page---byline--7275c3d1204b---------------------------------------)

[Helmiriahi](https://medium.com/%40helmiriahi55?source=post_page---byline--7275c3d1204b---------------------------------------)

3 min read

·

4 days ago

--

3

Listen

Share

*Hello Hackers — hope you’re well.
 Today I’m sharing a short write‑up about a recent finding on a private program — I’ll call the site* ***EXAMPLE.COM****.*

*While scrolling a popular car‑parts marketplace with a friend I joked, “I could change every product price on this site.” He laughed. That challenge stuck with me — three days later I found a tiny URL parameter that made a paid product free. Let’s dive in.*

*I wasn’t hunting general bugs — I only wanted to change product prices.*

Press enter or click to view image in full size

![]()

*When I clicked the price on a product page it returned an ID and the price. My first thought was the usual: tweak that parameter and the price will change(699 EUR→0) — classic parameter tampering. I tried it — nothing happened.*

![]()

*Somehow, I started thinking about following the payment steps. I tried to change the price just before the request went to the Visa payment, attempting to tweak it right before the final call to the payment API. That’s when I noticed another request — it was fetching the product ID again.*

Press enter or click to view image in full size

![]()

*And here’s where I found something spicy! Can you see it?*

## *The spicy parameter:* `id_product_feature_set`

*While digging, I noticed this parameter in the request:*

```
id_product_feature_set
```

*I wondered what would happen if I tried* `-1`*. Turns out, a few things can go wrong:*

***1. Broken database lookup*** *The server likely runs something like:*

```
SELECT price_modifier FROM product_feature_set WHERE id = -1;
```

*→ No result → fallback = 0 → price = base\_price + 0 =* ***0****.*

***2. Error in price calculation*** *If the backend just adds the feature price from an array:*

```
$total_price = base_price + feature_set_price[$id_product_feature_set];
```

*and* `$feature_set_price[-1]` *doesn’t exist, the total becomes* ***0****.*

***3. Application logic flaw*** *Some systems treat missing or invalid features as “no price,” defaulting the total to 0 so checkout isn’t blocked.*

and here i make the product price to 0 EUR

Press enter or click to view image in full size

![]()

In the end, the company recognized it as a critical vulnerability, and I received the bounty reward.

Thanks for following along!

> **Contact :**
>
> [helmi riahi | LinkedIn](https://www.linkedin.com/in/helmi-riahi-9b3751243/)

[Security](https://medium.com/tag/security?source=post_page-----7275c3d1204b---------------------------------------)

[Web Security](https://medium.com/tag/web-security?source=post_page-----7275c3d1204b---------------------------------------)

[Ecommerce](https://medium.com/tag/ecommerce?source=post_page-----7275c3d1204b---------------------------------------)

[Bug Bounty](https://medium.com/tag/bug-bounty?source=post_page-----7275c3d1204b---------------------------------------)

[Infosec](https://medium.com/tag/infosec?source=post_page-----7275c3d1204b---------------------------------------)

--

--

3

[![InfoSec Write-ups](https://miro.medium.com/v2/resize:fill:96:96/1*SWJxYWGZzgmBP1D0Qg_3zQ.png)](https://infosecwriteups.com/?source=post_page---post_publication_info--7275c3d1204b---------------------------------------)

[![InfoSec Write-ups](https://miro.medium.com/v2/resize:fill:128:128/1*SWJxYWGZzgmBP1D0Qg_3zQ.png)](https://infosecwriteups.com/?source=post_page---post_publication_info--7275c3d1204b---------------------------------------)

Follow

[## Published in InfoSec Write-ups](https://infosecwriteups.com/?source=post_page---post_publication_info--7275c3d1204b---------------------------------------)

[73K followers](/followers?source=post_page---post_publication_info--7275c3d1204b---------------------------------------)

·[Last published 18 hours ago](/how-i-hacked-iit-delhi-885a7f810292?source=post_page---post_publication_info--7275c3d1204b---------------------------------------)

A collection of write-ups from the best hackers in the world on topics ranging from bug bounties and CTFs to vulnhub machines, hardware challenges and real life encounters. Subscribe to our weekly newsletter for the coolest infosec updates: <https://weekly.infosecwriteups.com/>

Follow

[![Helmiriahi](https://miro.medium.com/v2/resize:fill:96:96/1*6Kh6mnNLGFm4j2X5sh6qiQ@2x.jpeg)](https://medium.com/%40helmiriahi55?source=post_page---post_author_info--7275c3d1204b---------------------------------------)

[![Helmiriahi](https://miro.medium.com/v2/resize:fill:128:128/1*6Kh6mnNLGFm4j2X5sh6qiQ@2x.jpeg)](https://medium.com/%40helmiriahi55?source=post_page---post_author_info--7275c3d1204b---------------------------------------)

[## Written by Helmiriahi](https://medium.com/%40helmiriahi55?source=post_page---post_author_info--7275c3d1204b---------------------------------------)

[95 followers](https://medium.com/%40helmiriahi55/followers?source=post_page---post_author_info--7275c3d1204b---------------------------------------)

·[14 following](https://medium.com/%40helmiriahi55/following?source=post_page---post_author_info--7275c3d1204b---------------------------------------)

I’m Helmi Riahi, a Network and System Security Engineer passionate about Red Team assessments and penetration testing.

## Responses (3)

See all responses

[Help](https://help.medium.com/hc/en-us?source=post_page-----7275c3d1204b---------------------------------------)

[Status](https://status.medium.com/?source=post_page-----72...