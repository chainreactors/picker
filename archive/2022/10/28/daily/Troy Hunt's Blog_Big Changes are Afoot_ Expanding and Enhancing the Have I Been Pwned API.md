---
title: Big Changes are Afoot: Expanding and Enhancing the Have I Been Pwned API
url: https://www.troyhunt.com/expanding-and-enhancing-the-have-i-been-pwned-api/
source: Troy Hunt's Blog
date: 2022-10-28
fetch_date: 2025-10-03T21:09:39.457133
---

# Big Changes are Afoot: Expanding and Enhancing the Have I Been Pwned API

* [Home](https://www.troyhunt.com/)
* [Workshops](https://www.troyhunt.com/workshops/)
* [Speaking](https://www.troyhunt.com/speaking/)
* [Media](https://www.troyhunt.com/media/)
* [About](https://www.troyhunt.com/about/)
* [Contact](https://www.troyhunt.com/contact/)
* [Sponsor](https://www.troyhunt.com/sponsorship/)

**Sponsored by:**

# Big Changes are Afoot: Expanding and Enhancing the Have I Been Pwned API

27 October 2022

Just over 3 years ago now, I sat down at a makeshift desk (ok, so it was a kitchen table) in an Airbnb in Olso and built [the authenticated API for Have I Been Pwned](https://www.troyhunt.com/authentication-and-the-have-i-been-pwned-api/) (HIBP). As I explained at the time, the primary goal was to combat abuse of the service and by adding the need to supply a credit card, my theory was that the bad guys would be very reluctant to, well, be bad guys. The theory checked out, and now with the benefit of several years of data, I can confidently say abuse is near non-existent. I just don't see it. Which is awesome 😊

But there were other things I also didn't see, and it's taken a while for me to get around to addressing them. Some of them are fixed *now* (like right now, already in production), and some of them will be fixed very, very soon. I think it's all pretty cool, let me explain:

### Payments Can Be Hard... if You Don't Stripe Right

A little more background will help me explain this better: in the opening sentence of this blog post I mentioned building the original authenticated API out on a kitchen table at an Airbnb in Oslo. By that time, everyone knew [I was going through an M&A process with HIBP I called Project Svalbard](https://www.troyhunt.com/project-svalbard-the-future-of-have-i-been-pwned/), which ultimately failed. What most people didn't know at the time was [the other very stressful goings on in my life](https://www.troyhunt.com/sustaining-performance-under-extreme-stress/) which combined, had me on a crazy rollercoaster ride I had little control over. It was in that environment that I created the authenticated API, complete with the [Azure API Management](https://azure.microsoft.com/en-us/products/api-management/?ref=troyhunt.com#overview) (APIM) component and Stripe integration. It was rough, and I wish I'd done it better. Now, I have.

In the beginning, I pushed as much of the payment processing as possible to the HIBP website. This was due to a combination of me wanting to create a slick UX and frankly, not understanding Stripe's own UI paradigms. It looked like this:

![](https://www.troyhunt.com/content/images/2022/10/image.png)

Cards never ended up hitting HIBP directly, rather the site did a dance with Stripe that involved the card data going to them directly from the client side, a token coming back and then that being used for the processing. It worked, but it had numerous problems ranging from lack of support for things like [3D Secure payments](https://stripe.com/docs/payments/3d-secure?ref=troyhunt.com), no support for other payments mechanisms such as Google Pay and Apple Pay and increasingly, large amounts of plumbing required to tie it all together. For example, there were hundreds of lines of code on my end to process payments, change the default card and show a list of previous receipts. The Stripe APIs are extraordinarily clever, but I couldn't escape writing large troves of my own code to make it work the way I originally designed it.

Two new things from Stripe since I originally wrote the code have opened up a whole new way of doing this:

1. [Customer Portal](https://www.youtube.com/watch?v=u8H6awDJVpM&ref=troyhunt.com): This is a fully hosted environment where payments are made, cards and subscriptions are managed, invoices and receipts are retrieved and basically, a huge amount of the work I'd previously hand-built can be managed by them rather than by me
2. [Embeddable Pricing Table](https://www.youtube.com/watch?v=tY8fVEoPHIc&ref=troyhunt.com): This brings the products and prices defined in Stripe into the UI of third party services (such as HIBP) such that customers can select their product then head off to Stripe and do the purchasing there

Rolling to these services removed a *huge* amount of code from HIBP with the bulk of what's left being email address verification, API key management and handling callbacks from Stripe when a payment is successful. What all this means is that when you first create a subscription, after verifying your email address, you see these two screens:

![](https://www.troyhunt.com/content/images/2022/10/image-1.png)![](https://www.troyhunt.com/content/images/2022/10/Stripe-Payment.png)

That's the embeddable pricing table following by Stripe's own hosted payment page. I left the browser address bar in the latter to highlight that this is served by Stripe rather than HIBP. I *love* distancing myself from any sort of card processing and what's more, everything to do with actually taking the payment is now Stripe's problem 😊 If you're interested in the mechanics of this, a successful payment calls a webhook on HIBP with the customer's details which updates their account with a month of API key whilst the screen above redirects them over to the HIBP website where they can grab their key. Easy peasy.

I silently rolled this out a week ago, watched it being used, made a few little tweaks and then waited until now to write about it. The rollout coincided with a typical email I've received so many times before:

> First of all I would like to thank you for the wonderful service that helps people to keep track of their email breaches. I was trying to build a product to provide your services via my website, something similar to Firefox, avast and 100's of other companies doing. We were trying to do it according to the guidelines mentioned in the website. However **I am not able to renew my purchase due to payment gateway failures at stripe payment.** Requesting you to kindly check the same and advise me on alternate methods for making the payment.

The old model often caused payments to be rejected, especially from subscribers in India. The painful thing for me when trying to help folks is that Stripe would simply report the failed payment as follows:

![](https://www.troyhunt.com/content/images/2022/10/image-4.png)

However, going back to the individual who raised the query above after rolling out this update, things changed very dramatically:

![](https://www.troyhunt.com/content/images/2022/10/image-3.png)

To the title of this section, I simply wasn't "Striping" right. I'm sure there's a way with enough plumbing that it's feasible, but why bother? I cut *hundreds* of lines of code out just by delegating more of the workload back to them. Further, with [ever tightening PCI DSS standards](https://scotthelme.co.uk/pci-dss-4-0-its-time-to-get-serious-on-magecart/?ref=troyhunt.com) (read Scott's piece, interesting stuff) the less I have to do with cards, the better.

This was a "penny drop" moment for me and it's already made a big difference in a positive way. But there's another penny that dropped for me at the same time: one-off keys were an unnecessary problem.

### There Are No More One-Off Keys

It was at the moment I was ripping out those hundreds of lines of code that I wondered: why do I have all the additional kludge to support the paradigm of a one-off key that only lasts a month? Why had I built (and was now maintaining) server side code to handle different types of purchases and UX paradigms to represent one-off versus recurring keys? My gut feel was that most payments formed part of an ongoing subscription but hey, who needs gut feels when you have real data?! So I pulled the numbers:

***Only 7% of payments were one-offs, with 93% of payments forming part of ongoing subscriptions.***

And so I killed the one-off keys. Kinda, because you can still have a key for only one month, you just purchase a monthly subscription then immediately cancel it vi...