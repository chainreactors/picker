---
title: Experimenting with Stealer Logs in Have I Been Pwned
url: https://www.troyhunt.com/experimenting-with-stealer-logs-in-have-i-been-pwned/
source: Troy Hunt's Blog
date: 2025-01-14
fetch_date: 2025-10-06T20:24:50.096385
---

# Experimenting with Stealer Logs in Have I Been Pwned

* [Home](https://www.troyhunt.com/)
* [Workshops](https://www.troyhunt.com/workshops/)
* [Speaking](https://www.troyhunt.com/speaking/)
* [Media](https://www.troyhunt.com/media/)
* [About](https://www.troyhunt.com/about/)
* [Contact](https://www.troyhunt.com/contact/)
* [Sponsor](https://www.troyhunt.com/sponsorship/)

**Sponsored by:**

# Experimenting with Stealer Logs in Have I Been Pwned

14 January 2025

**TL;DR — Email addresses in stealer logs can now be queried in HIBP to discover which websites they've had credentials exposed against. Individuals can see this by verifying their address using** [**the notification service**](https://haveibeenpwned.com/NotifyMe?ref=troyhunt.com) **and organisations monitoring domains can** [**pull a list back via a new API**](https://haveibeenpwned.com/API/v3?ref=troyhunt.com#StealerLogsForEmail)**.**

Nasty stuff, stealer logs. [I've written about them and loaded them into Have I Been Pwned (HIBP) before](https://www.troyhunt.com/begging-for-bounties-and-more-info-stealer-logs/) but just as a recap, we're talking about the logs created by malware running on infected machines. You know that game cheat you downloaded? Or that crack for the pirated software product? Or the video of your colleague doing something that sounded crazy but you thought you'd better download and run that executable program showing it just to be sure? That's just a few different ways you end up with malware on your machine that then watches what you're doing and logs it, just like this:

![](https://www.troyhunt.com/content/images/2025/01/image-4.png)

These logs all came from the same person and each time the poor bloke visited a website and logged in, the malware snared the URL, his email address and his password. It's akin to a criminal looking over his shoulder and writing down the credentials for every service he's using, except rather than it being one shoulder-surfing bad guy, it's somewhat larger than that. We're talking about *billions* of records of stealer logs floating around, often published via Telegram where they're easily accessible to the masses. Check out Bitsight's piece titled [Exfiltration over Telegram Bots: Skidding Infostealer Logs](https://www.bitsight.com/blog/exfiltration-over-telegram-bots-skidding-infostealer-logs?ref=troyhunt.com) if you'd like to get into the weeds of how and why this happens. Or, for a really quick snapshot, here's an example that popped up on Telegram as I was writing this post:

![](https://www.troyhunt.com/content/images/2025/01/image-9.png)

As it relates to HIBP, stealer logs have always presented a bit of a paradox: they contain *huge* troves of personal information that by any reasonable measure constitute a data breach that victims would like to know about, but then what can they actually do about it? What are the websites listed against their email address? And what password was used? Reading the comments from the blog post in the first para, you can sense the frustration; people want more info and merely saying "your email address appeared in stealer logs" has left many feeling more frustrated than informed. I've been giving that a lot of thought over recent months and today, we're going to take a big step towards addressing that concern:

**The domains an email address appears next to in stealer logs can now be returned to authorised users.**

This means the guy with the Gmail address from the screen grab above can now see that his address has appeared against Amazon, Facebook and H&R Block. Further, his password is also searchable in [Pwned Passwords](https://haveibeenpwned.com/Passwords?ref=troyhunt.com) so every piece of info we have from the stealer log is now accessible to him. Let me explain the mechanics of this:

Firstly, the volumes of data we're talking about are immense. In the case of the most recent corpus of data I was sent, there are hundreds of text files with well over 100GB of data and *billions* of rows. Filtering it all down, we ended up with 220 million unique rows of email address and domain pairs covering 69 million of the total 71 million email addresses in the data. The gap is explained by a combination of email addresses that appeared against invalidly formed domains and in some cases, addresses that only appeared with a password and not a domain. Criminals aren't exactly renowned for dumping perfectly formed data sets we can seamlessly work with, and I hope folks that fall into that few percent gap understand this limitation.

So, we now have 220 million records of email addresses against domains, how do we surface that information? Keeping in mind that "experimental" caveat in the title, the first decision we made is that it should only be accessible to the following parties:

1. The person who owns the email address
2. The company that owns the domain the email address is on

At face value it might look like that first point deviates from the current model of just entering an email address on the front page of the site and getting back a result ([and there are very good reasons why the service works this way](https://www.troyhunt.com/the-ethics-of-running-a-data-breach-search-service/)). There are some important differences though, the first of which is that whilst your classic email address search on HIBP returns verified breaches of specific services, stealer logs contain a list of services that have *never* have been breached. It means we're talking about much larger numbers that build up far richer profiles; instead of a few breached services someone used, we're talking about potentially *hundreds* of them. Secondly, many of the services that appear next to email addresses in the stealer logs are precisely the sort of thing [we flag as sensitive and hide from public view](https://haveibeenpwned.com/FAQs?ref=troyhunt.com#SensitiveBreach). There's a heap of Pornhub. There are health-related services. Religious one. Political websites. There are a lot of services there that merely by association constitute [sensitive information](https://www.alrc.gov.au/publication/for-your-information-australian-privacy-law-and-practice-alrc-report-108/6-the-privacy-act-some-important-definitions/sensitive-information/?ref=troyhunt.com), and we just don't want to take the risk of showing that info to the masses.

The second point means that companies doing domain searches (for which they already need to prove control of the domain), can pull back the list of the websites people in their organisation have email addresses next to. When the company controls the domain, they also control the email addresses on that domain and by extension, have the *technical* ability to view messages sent to their mailbox. Whether they have policies prohibiting this is a different story but remember, [your work email address is your work's email address](https://www.troyhunt.com/your-work-email-address-is-your-works-email-address/)! They can already see the services sending emails to their people, and in the case of stealer logs, this is likely to be *enormously* useful information as it relates to protecting the organisation. I ran a few big names through the data, and even I was shocked at the prevalence of corporate email addresses against services you wouldn't expect to be used in the workplace (then again, using the corp email address in places you definitely shouldn't be [isn't exactly anything new](https://thehill.com/policy/cybersecurity/251431-ashley-madison-leak-appears-real-includes-thousands-of-government-emails/?ref=troyhunt.com)). That in itself is an issue, then there's the question of whether these logs came from an infected corporate machine or from someone entering their work email address into their personal device.

I started thinking more about what you can learn about an organisation's exposure in these logs, so I grabbed a well-known brand in the Fortune 500. Here are some of the highlights:

1. 2,850 unique corporate email addresses in the stealer logs
2. 3,...