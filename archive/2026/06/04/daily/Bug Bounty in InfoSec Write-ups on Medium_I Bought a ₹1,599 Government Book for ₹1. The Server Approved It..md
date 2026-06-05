---
title: I Bought a ₹1,599 Government Book for ₹1. The Server Approved It.
url: https://infosecwriteups.com/i-bought-a-1-599-government-book-for-1-the-server-approved-it-8a832499b1fb?source=rss----7b722bfd1b8d--bug_bounty
source: Bug Bounty in InfoSec Write-ups on Medium
date: 2026-06-04
fetch_date: 2026-06-05T06:12:52.409582
---

# I Bought a ₹1,599 Government Book for ₹1. The Server Approved It.

[Sitemap](/sitemap/sitemap.xml)

[Open in app](https://play.google.com/store/apps/details?id=com.medium.reader&referrer=utm_source%3DmobileNavBar&source=post_page---top_nav_layout_nav-----------------------------------------)

Sign up

[Sign in](https://medium.com/m/signin?operation=login&redirect=https%3A%2F%2Finfosecwriteups.com%2Fi-bought-a-1-599-government-book-for-1-the-server-approved-it-8a832499b1fb&source=post_page---top_nav_layout_nav-----------------------global_nav------------------)

[Medium Logo](https://medium.com/?source=post_page---top_nav_layout_nav-----------------------------------------)

Get app

[Write](https://medium.com/m/signin?operation=register&redirect=https%3A%2F%2Fmedium.com%2Fnew-story&source=---top_nav_layout_nav-----------------------new_post_topnav------------------)

[Search](https://medium.com/search?source=post_page---top_nav_layout_nav-----------------------------------------)

Sign up

[Sign in](https://medium.com/m/signin?operation=login&redirect=https%3A%2F%2Finfosecwriteups.com%2Fi-bought-a-1-599-government-book-for-1-the-server-approved-it-8a832499b1fb&source=post_page---top_nav_layout_nav-----------------------global_nav------------------)

![Unknown user](https://miro.medium.com/v2/resize:fill:64:64/1*dmbNkD5D-u45r44go_cf0g.png)

[## InfoSec Write-ups](https://infosecwriteups.com/?source=post_page---publication_nav-7b722bfd1b8d-8a832499b1fb---------------------------------------)

·

[![InfoSec Write-ups](https://miro.medium.com/v2/resize:fill:76:76/1*SWJxYWGZzgmBP1D0Qg_3zQ.png)](https://infosecwriteups.com/?source=post_page---post_publication_sidebar-7b722bfd1b8d-8a832499b1fb---------------------------------------)

A collection of write-ups from the best hackers in the world on topics ranging from bug bounties and CTFs to vulnhub machines, hardware challenges and real life encounters. Subscribe to our weekly newsletter for the coolest infosec updates: <https://weekly.infosecwriteups.com/>

# I Bought a ₹1,599 Government Book for ₹1. The Server Approved It.

[![LordofHeaven](https://miro.medium.com/v2/resize:fill:64:64/1*KZRV0GWTj8BUGxiz_w7oPg.png)](https://lordofheaven1234.medium.com/?source=post_page---byline--8a832499b1fb---------------------------------------)

[LordofHeaven](https://lordofheaven1234.medium.com/?source=post_page---byline--8a832499b1fb---------------------------------------)

5 min read

·

21 hours ago

--

1

[Listen](https://medium.com/m/signin?actionUrl=https%3A%2F%2Fmedium.com%2Fplans%3Fdimension%3Dpost_audio_button%26postId%3D8a832499b1fb&operation=register&redirect=https%3A%2F%2Finfosecwriteups.com%2Fi-bought-a-1-599-government-book-for-1-the-server-approved-it-8a832499b1fb&source=---header_actions--8a832499b1fb---------------------post_audio_button------------------)

Share

**The payment page showed ₹1.00. I had not touched the price field. I had only touched one number in one request.**

Press enter or click to view image in full size

![]()

I was not looking for a vulnerability that day.

I was clicking around a government website — an official portal where students could buy books published by government bodies. Study material, reference texts, the kind of dense, official content you’d find in competitive exam prep stacks. The kind of website that nobody thinks to test because it’s government, it’s boring, and what’s the worst that could happen with a bookstore?

I had Burp Suite running in the background. Force of habit.

I picked a book. Added it to the cart. Clicked checkout. Filled in fake billing details — Lord, Hello World, 9999999999, a pincode that doesn’t exist, an email with a typo in the domain. The kind of information you enter when you’re testing a flow and have no intention of completing the purchase.

Then I clicked Pay Now.

Burp caught the POST request before it hit the server.

The endpoint was `/ccavRequestHandler`. The request body had sixteen parameters: `order_id`, `billing_name`, `billing_tel`, `billing_email`, `billing_address`, `billing_city`, `billing_state`, `billing_zip`, `billing_country`, `merchant_id`, `language`, `currency`, `redirect_url`, `success_url`, `cancel_url` — and one more.

`amount=1599`

Press enter or click to view image in full size

![]()

I stared at that for a moment. Then I changed it to `1`.

Not ₹100. Not ₹10. ₹1. I wanted to see how far this would go.

I forwarded the request.

Press enter or click to view image in full size

![]()

The payment page loaded.

In the top-left corner, in blue text:

**INR 1.00 (Total Amount Payable)**

Press enter or click to view image in full size

![]()

The payment gateway had received a transaction request for ₹1. It had no reason to question this. As far as the gateway was concerned, a legitimate merchant server had just told it: this order costs one rupee. Process it.

The “Make Payment” button was right there. Accepting American Express, Mastercard, RuPay, Visa.

I turned off the intercept and refreshed the page. ₹1.00 was still showing. This was not a rendering artifact. The transaction session had been created at ₹1. The gateway was waiting for me to pay one rupee for a ₹1,599 book.

## Get LordofHeaven’s stories in your inbox

Join Medium for free to get updates from this writer.

Subscribe

Subscribe

[x]

Remember me for faster sign in

I did not proceed with the payment. I had enough.

Here is the architecture failure underneath this:

The government portal was treating the `amount` field in the checkout POST request as a trusted user-supplied value. The merchant ID, the order ID, the item itself — all server-side. But the price? Client-side. Passed through the browser. Interceptable. Modifiable. No validation on the server before it was handed to the payment gateway.

This is a business logic vulnerability — not an injection, not a bypass, not a CVE with a complicated name. No payload. No encoding. I opened Burp Suite, found a number, and changed it. That was the entire attack.

The assumption the developers had made — one that gets made constantly on Indian e-commerce platforms — was that a normal user would never look at the raw HTTP request. And they are right about normal users. Normal users do not run Burp Suite. But an attacker does.

Think about what this looks like at scale.

This was a government portal that sold books to students — students preparing for government exams, students buying prescribed reference material, students on tight budgets who were likely the exact demographic this portal existed to serve.

Every book in that catalog. Any user with a proxy tool. Any price they chose.

The gateway had no way to cross-reference the amount it received against the actual product price on the backend. There was no order validation webhook, no server-to-server price confirmation, no check that said: “Wait — this order was created for ₹1,599. Why are you asking us to collect ₹1?”

In a commercial platform, that’s a revenue leak. In a government portal distributing official study material, that’s a publicly funded resource being made freely exploitable. Not hypothetically. Actually, directly, by anyone willing to spend five minutes with an intercept proxy.

I reported it.

The address was `rvdp@nciipc.gov.in` — the Responsible Vulnerability Disclosure Program run by India's National Critical Information Infrastructure Protection Centre. I wrote up what I'd found: the endpoint, the vulnerable parameter, the steps to reproduce, the screenshot of the ₹1 payment page. I sent it off.

I wasn’t sure what to expect. Government VDPs in India have a reputation for silence. Not because no one cares — but because the pipeline from researcher inbox to development team is long, and the process isn’t always visible from the outside.

A reply came.

They acknowledged the finding. The vulnerability was taken seriously. The fix was deployed.

That was it. No bounty — this was a responsible disclosure program, not a bug bounty program. No CVE. No hall of fame that I was aware of. But t...