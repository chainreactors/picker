---
title: Good Riddance Teespring, Hello Fourthwall
url: https://www.troyhunt.com/good-riddance-teespring-hello-fourthwall/
source: Troy Hunt's Blog
date: 2025-07-22
fetch_date: 2025-10-06T23:51:51.905185
---

# Good Riddance Teespring, Hello Fourthwall

* [Home](https://www.troyhunt.com/)
* [Workshops](https://www.troyhunt.com/workshops/)
* [Speaking](https://www.troyhunt.com/speaking/)
* [Media](https://www.troyhunt.com/media/)
* [About](https://www.troyhunt.com/about/)
* [Contact](https://www.troyhunt.com/contact/)
* [Sponsor](https://www.troyhunt.com/sponsorship/)

**Sponsored by:**

# Good Riddance Teespring, Hello Fourthwall

21 July 2025

If I'm honest, I was never that keen on a merch store for [Have I Been Pwned](https://haveibeenpwned.com/?ref=troyhunt.com). It doesn't make the code run faster, nor does it load any more data breaches or add any useful features to the service whatsoever. But... people were keen. They wanted swag they could wear or drink from or whatever, and it's actually pretty cool that there's excitement about HIBP as a brand. Plus, setting up a merch store is easy, right?

To cut to the chase, we set up a store on [Teespring](https://teespring.com/?ref=troyhunt.com) and they've been an absolute bloody disaster. Like, *appalling* bad to the point where we began to wonder if they're even legitimate, and I wish we had found a blog post like this before entrusting them with our brand. Initially, it was just dumb stuff like this:

> FFS [@teespringcom](https://twitter.com/teespringcom?ref_src=twsrc%5Etfw&ref=troyhunt.com) 🤦‍♂️ So far finding their support just appealing incompetent, this is regarding the [@haveibeenpwned](https://twitter.com/haveibeenpwned?ref_src=twsrc%5Etfw&ref=troyhunt.com) merch store, check out the canonical link: [https://t.co/uHBeTlI1yU](https://t.co/uHBeTlI1yU?ref=troyhunt.com) [pic.twitter.com/nJBTGfCrqg](https://t.co/nJBTGfCrqg?ref=troyhunt.com)
>
> — Troy Hunt (@troyhunt) [June 2, 2025](https://twitter.com/troyhunt/status/1929647702658503157?ref_src=twsrc%5Etfw&ref=troyhunt.com)

I mean, *really* dumb:

```
<link rel="canonical" href="https://0.0.0.0:3000" />
```

So, everyone who visited the store and tried to share it via a mobile device was sending *that* address, and Teespring's response was that people should just manually copy and paste the URL! I stand by my reactions in that tweet - FFS 🤦‍♂️

Or on a similar note of technical incompetence, they were completely unable to add me to our store as an admin:

> For those that come later and consider [@teespringcom](https://twitter.com/teespringcom?ref_src=twsrc%5Etfw&ref=troyhunt.com), don't even think about it! I've been trying to join the store [@Charlotte\_Hunt\_](https://twitter.com/Charlotte_Hunt_?ref_src=twsrc%5Etfw&ref=troyhunt.com) set up for us for 4 weeks ago now and the invite just gives a JSON response about failed CAPTCHA every time. Support is completely useless 😡 [pic.twitter.com/d4EH6nC5O2](https://t.co/d4EH6nC5O2?ref=troyhunt.com)
>
> — Troy Hunt (@troyhunt) [June 9, 2025](https://twitter.com/troyhunt/status/1931890751547543765?ref_src=twsrc%5Etfw&ref=troyhunt.com)

That support thread spanned from the 16th of May to the 12th of June and culminated in:

> At this time, I still don’t have any updates from the Tech team. I understand this isn’t the resolution you were hoping for, and I sincerely apologize for the inconvenience and the delay.

And that's just the technical examples. The real pain came once we ordered merch, here's the timeline:

1. 19 May: Order placed with a 3 Jun to 11 Jun delivery timeframe
2. 20 May: We're advised that the order is "in production" (the status has not changed at the time of writing)
3. 29 Jun: We lodged a complaint: "We have a bunch of fans complaining they are not getting their orders."
4. 1 Jul: We receive a platitude response citing "unexpectedly high volume of orders"
5. 8 Jul: Teespring advises they "recently lost one of our key print partners" and we reply the same day, cancelling the order. Their auto-reply states that "We'll get back within the next 24 business hours".
6. 11 Jul: 3 days passed with no response, so we gave them a 24-hour deadline before lodging a dispute with the card provider, to which we received another automated response: "We'll get back within the next 24 business hours"
7. 17 Jul: Still no feedback, so we lodge a dispute with Amex

It's not just us either; not only have I not seen a single "hey, check out my cool HIBP merch" social post, I *have* received messages like this:

![](https://www.troyhunt.com/content/images/2025/07/image-7.png)

So, onto that dispute and believe it or not, this is the first time I've ever lodged a one. Turns out it's really simple, and I'd like to show everyone who made a purchase through the Teespring store just how easy it is. Firstly, I found the transaction on my Amex card:

![](https://www.troyhunt.com/content/images/2025/07/image-4.png)

That record had an option to submit a dispute which then allowed me to choose a reason:

![](https://www.troyhunt.com/content/images/2025/07/image-5.png)

A few little questions in between (dates, attempts to contact them, etc), and we're done:

![](https://www.troyhunt.com/content/images/2025/07/image-6.png)

And just like that, Teespring suddenly found the ability to reply to support queries again!

> We noticed a dispute was recently submitted for your transaction related to order #[reacted], with the reason noted as PRODUCT\_NOT\_RECEIVED. We wanted to reach out directly to better understand the situation and see how we can assist.

That came through yesterday, the 20th of July. As I think I've done a pretty decent job of outlining the situation in this blog post, we'll be sending them a link to it and following through with the dispute. Raising a dispute with your card provider not only returns the funds to your account, but it also levies a fee on the merchant, which in this case, seems entirely deserved.

I sincerely apologise to the HIBP supporters who trusted us enough to go to the merch store and make a purchase. This experience seriously sucks and should never have happened. I'll update this post with any further feedback I get from Teespring or Amex.

Onto more positive things, and an opportunity did arise out of Teespring's incompetence:

> Happy to help you switch to Fourthwall. Shoot me a DM and we’ll move everything over for you
>
> — Will Baumann (@dubbaumann) [June 3, 2025](https://twitter.com/dubbaumann/status/1930005538781442186?ref_src=twsrc%5Etfw&ref=troyhunt.com)

Usually, I'd be reluctant to respond to someone jumping in on a thread and pitching their product, but hey, we were desperate! And it turns out that Fourthwall is pretty awesome because people there actually talk to you and get stuff done 🙄 I mean, *properly* done:

> We’ve got [@haveibeenpwned](https://twitter.com/haveibeenpwned?ref_src=twsrc%5Etfw&ref=troyhunt.com) merch! Arrived a little while ago and finally got into it today, we’ll keep adding more stuff to the store based on demand: [https://t.co/uHBeTlI1yU](https://t.co/uHBeTlI1yU?ref=troyhunt.com) [pic.twitter.com/dQW7dcM0Ey](https://t.co/dQW7dcM0Ey?ref=troyhunt.com)
>
> — Troy Hunt (@troyhunt) [July 21, 2025](https://twitter.com/troyhunt/status/1947093608278216725?ref_src=twsrc%5Etfw&ref=troyhunt.com)

We ordered it on 2 July and received part of the order in Australia on 7 July, and the other part on 18 July. That's 5 and 16 days (both of which exceeded their estimate of 21-24 July), whilst the Teespring order was lodged 63 days ago 🤷‍♂️

So, check out [merch.haveibeenpwned.com](https://merch.haveibeenpwned.com/?ref=troyhunt.com) and have confidence that you will actually get what you order. Please leave a comment below if there's anything else you'd like to see in the store, and don't forget to pick up some nice thongs for yourself [some nice thongs](https://merch.haveibeenpwned.com/en-aud/products/breach-thongs?ref=troyhunt.com)!

[Have I Been Pwned](/tag/have-i-been-pwned-3f/)

[Tweet](https://twitter.com/share?text=Troy%20Hunt%3A%20Good%20Riddance%20Teespring%2C%20Hello%20Fourthwall&url=https://www.troyhunt.com/good-riddance-teespring-hello-fourthwall/)
 [Post](https://www.facebook.com/sharer/sharer.p...