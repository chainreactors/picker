---
title: Finally, Payment by Bank Transfer Comes to Have I Been Pwned
url: https://www.troyhunt.com/finally-payment-by-bank-transfer-comes-to-have-i-been-pwned/
source: Troy Hunt's Blog
date: 2026-11-10
fetch_date: 2026-11-11T08:35:34.200541
---

# Finally, Payment by Bank Transfer Comes to Have I Been Pwned

* [Home](https://www.troyhunt.com/)
* [Workshops](https://www.troyhunt.com/workshops/)
* [Speaking](https://www.troyhunt.com/speaking/)
* [Media](https://www.troyhunt.com/media/)
* [About](https://www.troyhunt.com/about/)
* [Contact](https://www.troyhunt.com/contact/)
* [Sponsor](https://www.troyhunt.com/sponsorship/)

**Sponsored by:**

# Finally, Payment by Bank Transfer Comes to Have I Been Pwned

11 November 2026

This is simultaneously the most boring yet exciting blog title I've written in a long time. How you pay for services isn't exactly a sexy topic, but it solves a problem that's been a massive bugbear for a long time.

Here's a brief history of the issue: many organisations have policies that make it extremely hard to purchase goods and services with a credit card. [I wrote about this more than two years ago now](https://www.troyhunt.com/the-trouble-with-procurement-departments-resellers-and-stripe/), where I referred to "Neville" in the procurement department who, because "reasons", demanded an invoice in advance and payment via electronic funds transfer (EFT) only. That ultimately means the world's most popular way to make online payments is out of reach for them. Unfortunately, until today, that was the only way we could take payment via Stripe, which processes all our online HIBP purchases. That left only two options for orgs in this situation:

1. Don't use Have I Been Pwned at all 😢
2. Buy a subscription via a reseller 🤢

The problem with the first option is obvious. The second option "solved" the first problem by allowing a company to pay a reseller by EFT, who then paid us by card. The reseller would then mark the price up (*often* significantly), slow the whole process down, log countless tickets with us (despite the existence of a dedicated portal for them), and frankly, just be a pain in the arse for everyone. It's hard to express the level of disdain I have for most resellers, and I even still have a 1,381-word draft blog post titled "That's it - Resellers are now Banned from Have I Been Pwned", which I held back from posting. Why? Because I've walked in the shoes of the folks trying to purchase our services who are just trying to get their job done, and Neville has told them they can't pay by card. That was me in a previous life, and it sucked. We kept resellers solely to support those people.

But today, [HIBP's subscription page](https://haveibeenpwned.com/Subscription?ref=troyhunt.com) has something all new on it:

![](https://storage.ghost.io/c/fb/33/fb3391dc-723d-4e74-b95a-d641b5feb38e/content/images/2026/11/image-1.png)

Stripe has given us early access to EFT payments in Australia. They've been available in the US for a while, but as an Aussie company and with global financial systems being what they are (i.e. not always the most flexible), we just didn't have that option. Until now. So, we've added EFT as a payment method to our Pro and High RPM plans and kept the entry-level Core ones on card only, as there's some additional overhead on our end. You'll see these every time you go to purchase an eligible subscription:

![](https://storage.ghost.io/c/fb/33/fb3391dc-723d-4e74-b95a-d641b5feb38e/content/images/2026/11/image-3.png)

When you choose to pay by bank transfer, you're given a form for your company details (this is how we calculate any applicable taxes), then a Stripe payment link which loads something similar to the following:

![](https://storage.ghost.io/c/fb/33/fb3391dc-723d-4e74-b95a-d641b5feb38e/content/images/2026/11/image-2.png)

The first thing is that, being an Aussie company with an Aussie bank account, we need to reflect EFT payments in AUD rather than USD. It makes sense when you think about it: we do USD for all the existing products paid for by card, and whatever the FX conversion gods decide is the corresponding Aussie amount eventually lands on our end. But that's a model where the card is charged, and access is granted immediately. For EFT, funds flow through the wires, do FX conversion for non-Aussie purchasers, land in the target account and then Stripe webhook magic enables the service. We need that exact amount to land on our end, so we can't be rolling the dice on what exchange rate we're going to get; hence, Stripe requires us to charge in the target currency. The products are exactly the same price based on the rate we currently see via Stripe purchases today (about 69 American cents per Aussie dollar), we'll just have to see if that's revised in the future with any major currency fluctuations.

Next are the banking details. Pretty straightforward, and I'm sure we've all made payments to an account like this before. The main thing is that the account number is a virtual one, which is how Stripe reconciles money that comes in from a previously raised invoice. When you sell a very limited number of products and a bunch of customers are buying the same one, this is how Stripe is then able to reconcile who has paid for what. If you really want to geek out on bank payments, [Stripe has a dedicated EFT explainer page](https://stripe.com/au/resources/more/efts-explained?ref=troyhunt.com).

And finally, subscriptions in HIBP begin as soon as the invoice is raised, but access to the service only begins when *payment* is made. You can see the problem if we didn't do it this way: bad guy spins up the service and immediately starts using it then just never pays. But this all ties into the quote ecosystem in the existing HIBP dashboard, so it's easy to generate a quote, go flick it to Neville, get it approved, then raise and pay the invoice straight away.

As I said in the opening, it's not the most exciting topic, but it's a major thing for us and the customers who were left with only bad options if they genuinely couldn't pay by card. In the aforementioned draft blog post on binning resellers, I'd written about how we'd seen markups of up to 131% (so yes, more than double the price!), with absolutely zero value add (i.e. they don't do any product support, that remains entirely on us). But the burden resellers really put on us is the support they require to make purchases; in that same draft post, I calculated that resellers accounted for 0.86% of all sales but 43% of all support tickets. That's just nuts, especially for such a small team (although [Bruce has helped enormously](https://www.troyhunt.com/weekly-update-529/)).

We hope this makes life easier for a bunch of people who were previously stuck between a rock and a hard place, and that includes all the "Nevilles" out there too. This is all now live and accessible via [the pricing page](https://haveibeenpwned.com/Subscription?ref=troyhunt.com). If you run into any issues, [Bruce is standing by in the support portal](https://support.haveibeenpwned.com/hc/en-au?ref=troyhunt.com).

[Have I Been Pwned](/tag/have-i-been-pwned-3f/)

[Tweet](https://twitter.com/share?text=Troy%20Hunt%3A%20Finally%2C%20Payment%20by%20Bank%20Transfer%20Comes%20to%20Have%20I%20Been%20Pwned&url=https://www.troyhunt.com/finally-payment-by-bank-transfer-comes-to-have-i-been-pwned/)
 [Post](https://www.facebook.com/sharer/sharer.php?u=https://www.troyhunt.com/finally-payment-by-bank-transfer-comes-to-have-i-been-pwned/)
 [Update](https://www.linkedin.com/shareArticle?mini=true&url=https://www.troyhunt.com/finally-payment-by-bank-transfer-comes-to-have-i-been-pwned/)
 Email
 [RSS](https://feeds.feedburner.com/TroyHunt)

Troy Hunt's Picture

##### Troy Hunt

Hi, I'm Troy Hunt, I write this blog, create courses for Pluralsight and am a Microsoft Regional Director and MVP who travels the world speaking at events and training technology professionals

Please enable JavaScript to view the [comments powered by Disqus.](https://disqus.com/?ref_noscript)

#### Troy Hunt

Hi, I'm Troy Hunt, I write this blog, run "Have I Been Pwned" and am a Microsoft Regional Director who travels the world speaking at events and training technology professionals

#### Upcoming Events

I often run...