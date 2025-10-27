---
title: Hacking OWASP Juice Shop: Part 2 — Exposing Critical Vulnerabilities in the Payment Flow
url: https://infosecwriteups.com/hacking-owasp-juice-shop-part-2-exposing-critical-vulnerabilities-in-the-payment-flow-45630ed1633e?source=rss----7b722bfd1b8d--bug_bounty
source: Bug Bounty in InfoSec Write-ups on Medium
date: 2024-07-31
fetch_date: 2025-10-06T17:42:00.981952
---

# Hacking OWASP Juice Shop: Part 2 — Exposing Critical Vulnerabilities in the Payment Flow

[Sitemap](/sitemap/sitemap.xml)

[Open in app](https://rsci.app.link/?%24canonical_url=https%3A%2F%2Fmedium.com%2Fp%2F45630ed1633e&%7Efeature=LoOpenInAppButton&%7Echannel=ShowPostUnderCollection&%7Estage=mobileNavBar&source=post_page---top_nav_layout_nav-----------------------------------------)

Sign up

[Sign in](https://medium.com/m/signin?operation=login&redirect=https%3A%2F%2Finfosecwriteups.com%2Fhacking-owasp-juice-shop-part-2-exposing-critical-vulnerabilities-in-the-payment-flow-45630ed1633e&source=post_page---top_nav_layout_nav-----------------------global_nav------------------)

[Medium Logo](https://medium.com/?source=post_page---top_nav_layout_nav-----------------------------------------)

[Write](https://medium.com/m/signin?operation=register&redirect=https%3A%2F%2Fmedium.com%2Fnew-story&source=---top_nav_layout_nav-----------------------new_post_topnav------------------)

[Search](https://medium.com/search?source=post_page---top_nav_layout_nav-----------------------------------------)

Sign up

[Sign in](https://medium.com/m/signin?operation=login&redirect=https%3A%2F%2Finfosecwriteups.com%2Fhacking-owasp-juice-shop-part-2-exposing-critical-vulnerabilities-in-the-payment-flow-45630ed1633e&source=post_page---top_nav_layout_nav-----------------------global_nav------------------)

![](https://miro.medium.com/v2/resize:fill:64:64/1*dmbNkD5D-u45r44go_cf0g.png)

[## InfoSec Write-ups](https://infosecwriteups.com/?source=post_page---publication_nav-7b722bfd1b8d-45630ed1633e---------------------------------------)

·

Follow publication

[![InfoSec Write-ups](https://miro.medium.com/v2/resize:fill:76:76/1*SWJxYWGZzgmBP1D0Qg_3zQ.png)](https://infosecwriteups.com/?source=post_page---post_publication_sidebar-7b722bfd1b8d-45630ed1633e---------------------------------------)

A collection of write-ups from the best hackers in the world on topics ranging from bug bounties and CTFs to vulnhub machines, hardware challenges and real life encounters. Subscribe to our weekly newsletter for the coolest infosec updates: <https://weekly.infosecwriteups.com/>

Follow publication

![]()

# Hacking OWASP Juice Shop: Part 2 — Exposing Critical Vulnerabilities in the Payment Flow

## In the Name of Allah, the Most Beneficent, the Most Merciful. All the praises and thanks be to Allah, the Lord of the ‘Alamin (mankind, jinns and all that exists).

[![callgh0st](https://miro.medium.com/v2/resize:fill:64:64/1*S943nhX0uzpVeh6N-49duw.jpeg)](https://callgh0st.medium.com/?source=post_page---byline--45630ed1633e---------------------------------------)

[callgh0st](https://callgh0st.medium.com/?source=post_page---byline--45630ed1633e---------------------------------------)

3 min read

·

Jul 28, 2024

--

Listen

Share

I hope you enjoyed [Part 1](https://callgh0st.medium.com/hacking-owasp-juice-shop-part-1-discovering-vulnerabilities-b85e974fb3e5). Here, I’m starting Part 2, which focuses on the logic vulnerabilities in the payment flow of OWASP Juice Shop.

**NOTE: I’ll add an important narrative at the end.**

I found two vulnerabilities in the payment flow.

First, if I place an order and proceed to check out at `POST /rest/basket/6/checkout`, the body contains:

```
{"couponData":"bnVsbA==","orderDetails":{"paymentId":"8","addressId":"7","deliveryMethodId":"2"}}
```

However, if I remove the `paymentId`, I can still check out without paying:

```
{"couponData":"bnVsbA==","orderDetails":{"paymentId":"","addressId":"7","deliveryMethodId":"2"}}
```

Press enter or click to view image in full size

![]()

**Ninth vulnerability: Ability to checkout without payment due to improper validation of payment ID.**

Second, I selected a product with only one item remaining. I couldn’t increase the quantity to two, so I tried setting it to `-10` in my Burp Suite request, and it worked. Upon checkout, the total price was `-49999.50¤` (negative instead of `49999.50¤`). This allowed me to bypass payment again. Additionally, my balance showed. `-4000¤`.

Press enter or click to view image in full size

![]()

**Tenth vulnerability: Bypassing product quantity restrictions by allowing negative values.**

**Eleventh vulnerability: Bypassing payment and causing a negative total price, resulting in a negative balance.**

I discovered another vulnerability in adding money to my wallet. The website restricts adding more than 1000¤, but the transaction is successful by intercepting the request and changing the amount to a larger value.

![]()

Press enter or click to view image in full size

![]()

I’m rich :)

Press enter or click to view image in full size

![]()

**Twelfth vulnerability: Bypassing wallet deposit limit by modifying the request payload.**

That’s all for now. Thanks for reading! Don’t forget to drop a like. You can sign up to get the next write-up delivered straight to your inbox.

Look-up Part 1:

[## Hacking OWASP Juice Shop: Part 1 - Discovering Vulnerabilities

### In the Name of Allah, the Most Beneficent, the Most Merciful. All the praises and thanks be to Allah, the Lord of the…

callgh0st.medium.com](https://callgh0st.medium.com/hacking-owasp-juice-shop-part-1-discovering-vulnerabilities-b85e974fb3e5?source=post_page-----45630ed1633e---------------------------------------)

> *For any suggestions or Correction, Kindly reach out to me:*
>
> *Twitter —* [*callgh0st*](https://twitter.com/callgh0st)

أَخْبَرَنَا عَمْرُو بْنُ عَلِيٍّ، عَنْ يَحْيَى، قَالَ حَدَّثَنَا شُعْبَةُ، قَالَ حَدَّثَنِي قَتَادَةُ، عَنْ أَبِي الْخَلِيلِ، عَنْ عَبْدِ اللَّهِ بْنِ الْحَارِثِ، عَنْ حَكِيمِ بْنِ حِزَامٍ، قَالَ قَالَ رَسُولُ اللَّهِ صلى الله عليه وسلم ‏ “‏ الْبَيِّعَانِ بِالْخِيَارِ مَا لَمْ يَفْتَرِقَا فَإِنْ صَدَقَا وَبَيَّنَا بُورِكَ فِي بَيْعِهِمَا وَإِنْ كَذَبَا وَكَتَمَا مُحِقَ بَرَكَةُ بَيْعِهِمَا ‏”‏ ‏.‏

It was narrated that Hakim bin Hizam said: “The Messenger of Allah said: ‘The two parties to a transaction have the choice so long as they have not separated. If they are honest and open, their transaction will be blessed, but if they tell lies and conceal anything, the blessing of their transaction will be lost.”

Sunan an-Nasa’i 4457
[https://sunnah.com/nasai:4457](https://sunnah.com/nasai/44)

[Payments](https://medium.com/tag/payments?source=post_page-----45630ed1633e---------------------------------------)

[Logic](https://medium.com/tag/logic?source=post_page-----45630ed1633e---------------------------------------)

[Vulnerability](https://medium.com/tag/vulnerability?source=post_page-----45630ed1633e---------------------------------------)

[Hacking](https://medium.com/tag/hacking?source=post_page-----45630ed1633e---------------------------------------)

[Bug Bounty](https://medium.com/tag/bug-bounty?source=post_page-----45630ed1633e---------------------------------------)

--

--

[![InfoSec Write-ups](https://miro.medium.com/v2/resize:fill:96:96/1*SWJxYWGZzgmBP1D0Qg_3zQ.png)](https://infosecwriteups.com/?source=post_page---post_publication_info--45630ed1633e---------------------------------------)

[![InfoSec Write-ups](https://miro.medium.com/v2/resize:fill:128:128/1*SWJxYWGZzgmBP1D0Qg_3zQ.png)](https://infosecwriteups.com/?source=post_page---post_publication_info--45630ed1633e---------------------------------------)

Follow

[## Published in InfoSec Write-ups](https://infosecwriteups.com/?source=post_page---post_publication_info--45630ed1633e---------------------------------------)

[71K followers](/followers?source=post_page---post_publication_info--45630ed1633e---------------------------------------)

·[Last published 2 hours ago](/baby-dfc2547dc387?source=post_page---post_publication_info--45630ed1633e---------------------------------------)

A collection of write-ups from the best hackers in the world on topics ranging from bug bounties and CTFs to vulnhub machines, hardware challenges and real life encounters. Subscribe to our weekly newsletter for the coolest infosec updates: <https://weekly.infosecwriteups.com/>

Follow

[![callgh0st](https://miro.medium.com/v2...