---
title: Pwned or Bot
url: https://www.troyhunt.com/pwned-or-bot/
source: Troy Hunt's Blog
date: 2023-01-20
fetch_date: 2025-10-04T04:24:47.638147
---

# Pwned or Bot

* [Home](https://www.troyhunt.com/)
* [Workshops](https://www.troyhunt.com/workshops/)
* [Speaking](https://www.troyhunt.com/speaking/)
* [Media](https://www.troyhunt.com/media/)
* [About](https://www.troyhunt.com/about/)
* [Contact](https://www.troyhunt.com/contact/)
* [Sponsor](https://www.troyhunt.com/sponsorship/)

**Sponsored by:**

# Pwned or Bot

19 January 2023

It's fascinating to see how creative people can get with breached data. Of course there's all the nasty stuff (phishing, identity theft, spam), but there are also some amazingly positive uses for data illegally taken from someone else's system. When I first built [Have I Been Pwned](https://haveibeenpwned.com/?ref=troyhunt.com) (HIBP), my mantra was to "do good things after bad things happen". And arguably, it has, largely by enabling individuals and organisations to learn of their own personal exposure in breaches. However, the use cases go well beyond that and there's one I've been meaning to write about for a while now after hearing about it firsthand. For now, let's just call this approach "Pwned or Bot", and I'll set the scene with some background on another problem: sniping.

Think about Miley Cyrus as Hannah Montana (bear with me, I'm actually going somewhere with this!) putting on shows people would buy tickets to. We're talking *loads* of tickets as back in the day, her popularity was off the charts with demand well in excess of supply. Which, for enterprising individuals of ill-repute, [presented an opportunity](http://www.jthtl.org/content/articles/V8I1/JTHTLv8i1_Loewenstein.PDF?ref=troyhunt.com):

> Ticketmaster, the exclusive ticket seller for the tour, sold out numerous shows within minutes, leaving many Hannah Montana fans out in the cold. Yet, often, moments after the shows went on sale, the secondary market  flourished with tickets to those shows. The tickets, whose face value ranged from $21 to $66, were resold on StubHub for an average of $258, plus StubHub’s 25% commission (10% paid by the buyer, 15% by the seller).

This is called "sniping", where an individual jumps the queue and snaps up products in limited demand for their own personal gain and consequently, to the detriment of others. Tickets to entertainment events is one example of sniping, the same thing happens when other products launch with insufficient supply to meet demand, for example Nike shoes. These can be *massively* popular and, par for the course of this blog, released in short demand. This creates a marketplace for snipers, some of whom share their tradecraft via videos such as this one:

"BOTTER BOY NOVA" refers to himself as a "Sneaker botter" in the video and demonstrates a tool called "Better Nike Bot" (BnB) which sells for $200 plus a renewal fee of $60 every 6 months. But don't worry, he has a discount code! Seems like hackers aren't the only ones making money out of the misfortune of others.

Have a look at the video and watch how at about the 4:20 mark he talks about using proxies "to prevent Nike from flagging your accounts". He recommends using the same number of proxies as you have accounts, inevitably to avoid Nike's (automated) suspicions picking up on the anomaly of a single IP address signing up multiple times. Proxies themselves are a commercial enterprise but don't worry, BOTTER BOY NOVA has a discount code for them too!

The video continues to demonstrate how to configure the tool to ultimately blast Nike's service with attempts to purchase shoes, but it's at the 8:40 mark that we get to the crux of where I'm going with this:

![](https://www.troyhunt.com/content/images/2023/01/image-5.png)

Using the tool, he's created a whole bunch of accounts in an attempt to maximise his chances of a successful purchase. These are obviously just samples in the screen cap above, but inevitably he'd usually go and register a bunch of new email addresses he could use specifically for this purpose.

Now, think of it from Nike's perspective: they've launched a new shoe and are seeing a whole heap of new registrations and purchase attempts. In amongst that lot are many genuine people... and this guy 👆 How can they weed him out such that snipers aren't snapping up the products at the expense of genuine customers? Keeping in mind tools like this are deliberately designed to avoid detection (remember the proxies?), it's a hard challenge to reliably separate the humans from the bots. But there's an indicator that's very easy to cross-check, and that's the occurrence of the email address in previous data breaches. Let me phrase it in simple terms:

**We're all so comprehensively pwned that if an email address *isn't* pwned, there's a good chance it doesn't belong to a real human.**

Hence, "Pwned or Bot" and this is precisely the methodology organisations have been using HIBP data for. With caveats:

If an email address hasn't been seen in a data breach before, it may be a newly created one especially for the purpose of gaming your system. It may also be legitimate and the owner has just been lucky to have not been pwned, or it may be that they're uniquely [subaddressing](https://learn.microsoft.com/en-us/exchange/recipients-in-exchange-online/plus-addressing-in-exchange-online?ref=troyhunt.com) their email addresses ([although this is extremely rare](https://haveibeenpwned.uservoice.com/forums/275398-general/suggestions/6774229-enable-search-and-notifications-for-email-addresse?ref=troyhunt.com)) or even using a masked email address service such as [the one 1Password provides through Fastmail](https://1password.com/fastmail/?ref=troyhunt.com). *Absence* of an email address in HIBP is not evidence of possible fraud, that's merely one possible explanation.

However, if an email address *has* been seen in a data breach before, we can say with a high degree of confidence that it did indeed exist at the time of that breach. For example, if it was in the LinkedIn breach of 2012 then you can conclude with great confidence that the address wasn't just set up for gaming your system. Breaches establish *history* and as unpleasant as they are to be a part of, they do actually serve a useful purpose in this capacity.

Think of breach history not as a binary proposition indicating the legitimacy of an email address, rather as one of assessing risk and considering "pwned or bot" as one of many factors. The best illustration I can give is how Stripe defines risk by assessing a multitude of fraud factors. Take this recent payment [for HIBP's API key](https://www.troyhunt.com/the-have-i-been-pwned-api-now-has-different-rate-limits-and-annual-billing/):

![](https://www.troyhunt.com/content/images/2023/01/image-1.png)

There's *a lot* going on here and I won't run through it all, the main thing to take away from this is that in a risk evaluation rating scale from 0 to 100, this particular transaction rated a 77 which puts it in the "highest risk" bracket. Why? Let's just pick a few obvious reasons:

1. The IP address had previously raised early fraud warnings
2. The email was only ever once previously seen on Stripe, and that was only 3 minutes ago
3. The customers name didn't match their email address
4. Only 76% of transactions from the IP address had previously been authorised
5. The customer's device had previously had 2 other cards associated with it

Any one of these fraud factors may not have been enough to block the transaction, but all combined it made the whole thing look rather fishy. Just as this risk factor also makes it look fishy:

![](https://www.troyhunt.com/content/images/2023/01/image-6.png)

Applying "Pwned or Bot" to your own risk assessment is dead simple with [the HIBP API](https://haveibeenpwned.com/API/v3?ref=troyhunt.com) and hopefully, this approach will help more people do precisely what HIBP is there for in the first place: to help "do good things after bad things happen".

[Have I Been Pwned](/tag/have-i-been-pwned-3f/)

[Tweet](https://twitter.com/share?text=Troy%20Hunt%3A%20Pwned%20o...