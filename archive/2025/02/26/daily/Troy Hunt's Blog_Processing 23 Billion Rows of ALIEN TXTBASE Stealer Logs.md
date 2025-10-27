---
title: Processing 23 Billion Rows of ALIEN TXTBASE Stealer Logs
url: https://www.troyhunt.com/processing-23-billion-rows-of-alien-txtbase-stealer-logs/
source: Troy Hunt's Blog
date: 2025-02-26
fetch_date: 2025-10-06T20:48:26.921076
---

# Processing 23 Billion Rows of ALIEN TXTBASE Stealer Logs

* [Home](https://www.troyhunt.com/)
* [Workshops](https://www.troyhunt.com/workshops/)
* [Speaking](https://www.troyhunt.com/speaking/)
* [Media](https://www.troyhunt.com/media/)
* [About](https://www.troyhunt.com/about/)
* [Contact](https://www.troyhunt.com/contact/)
* [Sponsor](https://www.troyhunt.com/sponsorship/)

**Sponsored by:**

# Processing 23 Billion Rows of ALIEN TXTBASE Stealer Logs

26 February 2025

I like to start long blog posts with a tl;dr, so here it is:

**We've ingested a corpus of 1.5TB worth of stealer logs known as "ALIEN TXTBASE" into Have I Been Pwned. They contain 23 billion rows with 493 million unique website and email address pairs, affecting 284M unique email addresses. We've also added 244M passwords we've never seen before to Pwned Passwords and updated the counts against another 199M that were already in there. Finally, we now have a way for domain owners to query their entire domain for stealer logs and for website operators to identify customers who have had their email addresses snared when entering them into the site. (Note: stealer logs are still freely and easily searchable by individuals, scroll to the bottom for a walkthrough.)**

This work has been a month-long saga that began hot off the heels of [processing the last massive stash of stealer logs in the middle of Jan](https://www.troyhunt.com/experimenting-with-stealer-logs-in-have-i-been-pwned/). That was the first time we'd ever added more context to stealer logs by way of making the websites email addresses had been logged against searchable. To save me repeating it all here, if you're unfamiliar with stealer logs as a concept and what we've previously done with HIBP, start there.

Up to speed? Good, let's talk about ALIEN TXTBASE.

### Origin Story

Last month after loading the aforementioned corpus of data, someone in a government agency reached out and pointed me in the direction of more data by way of two files totalling just over 5GB. Their file names respectively contained the numbers "703" and "704", the word "Alien" and the following text at the beginning of each file:

![](https://www.troyhunt.com/content/images/2025/02/image-9.png)

Pulling the threads, it turned out the Telegram channel referred to contained 744 files of which my contact had come across just the two. The data I'm writing about today is that full corpus, published to Telegram as individual files:

![](https://www.troyhunt.com/content/images/2025/02/image-10.png)

A quick side note on Telegram: There's been growing concern in recent years about the [use of Telegram by organised crime](https://www.lawfaremedia.org/article/how-telegram-turbocharges-organized-crime?ref=troyhunt.com), especially since [the founder's arrest in France last year for not cracking down on illegal activity on the platform](https://en.wikipedia.org/wiki/Arrest_and_indictment_of_Pavel_Durov?ref=troyhunt.com). Telegram makes it super easy to publish large volumes of data (such as we're talking about here) under the veil of anonymity and distribute it en mass. This is just one of many channels involved in cybercrime, but it's noteworthy due to the huge amount of freely accessible data.

The file in the image above contained over 36 *million* rows of data consisting of website URLs and the email addresses and passwords entered into them. But the file is just a sample - *a teaser* - with more data available via the subscription options offered in the message. And that's the monetisation route: provide existing data for free, then offer a subscription to feed newly obtained logs to consuming criminals with a desire to exploit the victims *again*. Again? The stealer logs are obtained in the first place by exploiting the victim's machine, for example:

> How do people end up in stealer logs? By doing dumb stuff like this: “Around October I downloaded a pirated version of Adobe AE and after that a trojan got into my pc” [pic.twitter.com/igEzOayCu6](https://t.co/igEzOayCu6?ref=troyhunt.com)
>
> — Troy Hunt (@troyhunt) [August 5, 2024](https://twitter.com/troyhunt/status/1820591861771485597?ref_src=twsrc%5Etfw&ref=troyhunt.com)

So now this guy has malware running on his PC which is siphoning up all his credentials as they're entered into websites. It's those credentials that are then sold in the stealer logs and later used to access the victim's accounts, which is the second exploitation. Pirating software is just one way victims become infected; have a read of [this recent case study from our Australian Signals Directorate](https://www.cyber.gov.au/about-us/view-all-content/alerts-and-advisories/silent-heist-cybercriminals-use-information-stealer-malware-compromise-corporate-networks?ref=troyhunt.com):

> When working from home, Alice remotely accesses the corporate network of her organisation using her personal laptop. Alice downloaded, onto her personal laptop, a version of Notepad++ from a website she believed to be legitimate. An info stealer was disguised as the installer for the Notepad++ software.

> When Alice attempted to install the software, the info stealer activated and began harvesting user credentials from her laptop. This included her work username and password, which she had saved in her web browser’s saved logins feature. The info stealer then sent those user credentials to a remote command-and-control server controlled by a cybercriminal group.

Eventually, data like Alice's ends up in places like this Telegram channel and from there, it enables further crimes. From the same ASD article:

> Stolen valid user credentials are highly valuable to cybercriminals, because they expedite the initial access to corporate networks and enterprise systems.

So, that's where the data has come from. As I said earlier, ALIEN TXTBASE is by no means the only Telegram channel out there, but it is definitely a major distribution channel.

### Verification

When there's a breach of a discrete website, verification of the incident is usually pretty trivial. For example, if Netflix suffered a breach (and I have no indication they have, this is just an example), I can go to their website, head to the password reset field, enter a *made-up* email address and see a response like this:

![](https://www.troyhunt.com/content/images/2025/02/image-11.png)

On the other hand, an address that does exist on the service usually returns a message to the effect of "we've sent you a password reset email". This is called an "enumeration vector" in that it enables you to enumerate through a list of email addresses and find out which ones have an account on the site.

But stealer logs don't come from a single source like Netflix, instead they contain the credentials for a whole range of different sites visited by people infected with malware. However, I can still take lines from the stealer logs that were captured against Netflix and test the email addresses. (Note: I *never* test if the password is valid, that would be a privacy violation that constitutes unauthorised access and besides, as you'll read next, there's simply no need to.)

Initially, I actually ran into a bit of a roadblock when testing this:

![](https://www.troyhunt.com/content/images/2025/02/image-14.png)

I found this over and over again so, I went back and checked the source data and inspected this poor victim's record:

![](https://www.troyhunt.com/content/images/2025/02/image-15.png)

Their Netflix credentials were snared when they were entered into the website with a path of "/ph-en/login", implying they're likely Filipino. Let's try VPN'ing into Manilla:

![](https://www.troyhunt.com/content/images/2025/02/image-13.png)

And suddenly, a password reset gives me exactly what I need:

![](https://www.troyhunt.com/content/images/2025/02/image-12.png)

That's a little tangent from stealer logs, but Netflix obviously applies some geo-fencing logic to certain features. This actually worked out better than expected verification-wise because not only was I able to conf...