---
title: When Bug Bounty Hunting Hit Me Back: How Losing $500 Led Me to a Web Cache Poisoning Bug.
url: https://infosecwriteups.com/when-bug-bounty-hunting-hit-me-back-how-losing-500-led-me-to-a-web-cache-poisoning-bug-36fb2f196b9a?source=rss----7b722bfd1b8d--bug_bounty
source: Bug Bounty in InfoSec Write-ups on Medium
date: 2026-05-31
fetch_date: 2026-06-01T06:47:04.653720
---

# When Bug Bounty Hunting Hit Me Back: How Losing $500 Led Me to a Web Cache Poisoning Bug.

[Sitemap](/sitemap/sitemap.xml)

[Open in app](https://play.google.com/store/apps/details?id=com.medium.reader&referrer=utm_source%3DmobileNavBar&source=post_page---top_nav_layout_nav-----------------------------------------)

Sign up

[Sign in](https://medium.com/m/signin?operation=login&redirect=https%3A%2F%2Finfosecwriteups.com%2Fwhen-bug-bounty-hunting-hit-me-back-how-losing-500-led-me-to-a-web-cache-poisoning-bug-36fb2f196b9a&source=post_page---top_nav_layout_nav-----------------------global_nav------------------)

[Medium Logo](https://medium.com/?source=post_page---top_nav_layout_nav-----------------------------------------)

Get app

[Write](https://medium.com/m/signin?operation=register&redirect=https%3A%2F%2Fmedium.com%2Fnew-story&source=---top_nav_layout_nav-----------------------new_post_topnav------------------)

[Search](https://medium.com/search?source=post_page---top_nav_layout_nav-----------------------------------------)

Sign up

[Sign in](https://medium.com/m/signin?operation=login&redirect=https%3A%2F%2Finfosecwriteups.com%2Fwhen-bug-bounty-hunting-hit-me-back-how-losing-500-led-me-to-a-web-cache-poisoning-bug-36fb2f196b9a&source=post_page---top_nav_layout_nav-----------------------global_nav------------------)

![Unknown user](https://miro.medium.com/v2/resize:fill:64:64/1*dmbNkD5D-u45r44go_cf0g.png)

[## InfoSec Write-ups](https://infosecwriteups.com/?source=post_page---publication_nav-7b722bfd1b8d-36fb2f196b9a---------------------------------------)

·

[![InfoSec Write-ups](https://miro.medium.com/v2/resize:fill:76:76/1*SWJxYWGZzgmBP1D0Qg_3zQ.png)](https://infosecwriteups.com/?source=post_page---post_publication_sidebar-7b722bfd1b8d-36fb2f196b9a---------------------------------------)

A collection of write-ups from the best hackers in the world on topics ranging from bug bounties and CTFs to vulnhub machines, hardware challenges and real life encounters. Subscribe to our weekly newsletter for the coolest infosec updates: <https://weekly.infosecwriteups.com/>

# When Bug Bounty Hunting Hit Me Back: How Losing $500 Led Me to a Web Cache Poisoning Bug.

[![kjulius](https://miro.medium.com/v2/resize:fill:64:64/1*pNjTItx95RQhfspL_MnSoA.jpeg)](https://kjulius.medium.com/?source=post_page---byline--36fb2f196b9a---------------------------------------)

[kjulius](https://kjulius.medium.com/?source=post_page---byline--36fb2f196b9a---------------------------------------)

7 min read

·

May 8, 2026

--

[Listen](https://medium.com/m/signin?actionUrl=https%3A%2F%2Fmedium.com%2Fplans%3Fdimension%3Dpost_audio_button%26postId%3D36fb2f196b9a&operation=register&redirect=https%3A%2F%2Finfosecwriteups.com%2Fwhen-bug-bounty-hunting-hit-me-back-how-losing-500-led-me-to-a-web-cache-poisoning-bug-36fb2f196b9a&source=---header_actions--36fb2f196b9a---------------------post_audio_button------------------)

Share

Press enter or click to view image in full size

![]()

By kjulius

Bug bounty hunting is exciting.

You find vulnerabilities, report them, help secure companies, and sometimes get rewarded for it. But one thing people rarely talk about is this:

> *Sometimes bug bounty hunting goes wrong against the hacker too.*

This story is about how losing almost **$500** from my bank account pushed me back into hunting… and eventually led me to discovering a real **Web Cache Poisoning vulnerability**.

Unfortunately, I reported it too late.

Another hacker got there first.

But the journey itself taught me something important:

> *As long as software exists, there will always be bugs.*

**What Web Cache Poisoning Is.**Web Cache Poisoning is a vulnerability where an attacker tricks a caching system (such as a CDN, reverse proxy, or browser cache) into storing and serving malicious or manipulated content to other users.

This usually happens when a web application uses user-controlled input — such as headers, parameters, or cookies — to generate a response, but the caching layer does not include that input in the cache key.

As a result:

* the attacker sends a specially crafted request,
* the malicious response gets cached,
* and normal users later receive the poisoned content from the cache.

Web cache poisoning can lead to:

* content manipulation,
* phishing attacks,
* SEO poisoning,
* malicious redirects,
* or even stored XSS in severe cases.

In simple terms:

> *The attacker poisons the cache once, and the cache serves the malicious response to everyone else.*

## It Started With a Different Cache Poisoning Bug.

I was hunting on a particular target when I stumbled across what looked like a **Web Cache Poisoning vulnerability**.

At first glance, the issue looked promising, but exploitation felt difficult. I couldn’t immediately prove impact, so instead of wasting too much time on it, I documented everything carefully in my notes and moved on to test other subdomains.

That decision would later come back in an unexpected way.

## The SaaS Platform.

One of the subdomains worked like a SaaS platform for businesses.

It allowed work owners and managers to:

* manage accounts.
* handle invoices.
* manage payments.
* access premium business features.

But most advanced functionalities required a paid subscription.

So I decided to test the payment workflow.

I requested a subscription and some weeks later an invoice was generated.

The invoice amount?

> ***Equivalent to $500***

Press enter or click to view image in full size

![]()

PoC Image

To proceed, users could:

* enter a debit/credit card.
* provide the CSC/CVV.
* or pay directly through an IBAN bank transfer.

Since I was only testing functionality, I entered my card number but intentionally used an incorrect CSC code.

The payment failed as expected.

At that point, I tested the remaining functionality, found nothing interesting, and eventually deleted the account entirely.

Or at least…

I thought I did.

## Four Days Later…

Four days later, I received a debit alert from my bank.
At first, I assumed it was a mistake, but when I opened the message, my heart dropped.
The charge was coming from the exact card I used on the SaaS platform.

They had successfully debited the full **$500 equivalent** from my account.
In my local currency, that amount was nearly **6K.**

Press enter or click to view image in full size

![]()

PoC Image

And the craziest part?

I had entered the wrong CSC code during testing.

Immediately, I called my bank and cancelled the card to prevent any additional charges.

## Trying to Contact the Company.

I contacted the company’s sales manager on WhatsApp.
The first message was read.
After that?

Silence…
No replies…

I also emailed the company directly, explaining the situation in detail.
They eventually responded the next day and told me:

> *There would be no refund.*

Not only that…

They somehow reactivated the account I had already deleted and informed me that the subscription had been activated successfully.

They also assured me they “would not charge me next year,” since the subscription renews annually.

At that point, I was frustrated, confused, and honestly angry.

I still had no idea how they managed to process the payment successfully despite the incorrect CSC.

But once a hacker, always a hacker… we do understand. 🗿

## Returning to Hunt Again.

After losing the money, I went back to the main target to continue hunting.

Not out of revenge.

But because I wanted to recover the loss through a legitimate bounty.

That’s when I remembered the cache poisoning issue I had documented earlier.

I reopened my notes and started digging deeper.

## Discovering the Real Vulnerability.

I intercepted the homepage request in Burp Suite and immediately noticed something interesting:

```
Cache-Control: public, max-age=604800
Pragma: public
Cf-Cache-Status: HIT
```

Press enter or click to view image in full size

![]()

PoC Image

That’s always a signal worth investigating.

## Get kjulius’s stories in your inbox

Join Medium for free to get updates from this write...