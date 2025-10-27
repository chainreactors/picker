---
title: Inside the "3 Billion People" National Public Data Breach
url: https://www.troyhunt.com/inside-the-3-billion-people-national-public-data-breach/
source: Troy Hunt's Blog
date: 2024-08-14
fetch_date: 2025-10-06T18:05:55.595528
---

# Inside the "3 Billion People" National Public Data Breach

* [Home](https://www.troyhunt.com/)
* [Workshops](https://www.troyhunt.com/workshops/)
* [Speaking](https://www.troyhunt.com/speaking/)
* [Media](https://www.troyhunt.com/media/)
* [About](https://www.troyhunt.com/about/)
* [Contact](https://www.troyhunt.com/contact/)
* [Sponsor](https://www.troyhunt.com/sponsorship/)

**Sponsored by:**

# Inside the "3 Billion People" National Public Data Breach

14 August 2024

I decided to write this post because there's no concise way to explain the nuances of [what's being described as one of the largest data breaches ever](https://www.conchovalleyhomepage.com/news/data-of-3-billion-people-exposed-in-one-of-the-largest-data-breaches-in-history-heres-what-you-need-to-know/?ref=troyhunt.com). Usually, it's easy to articulate a data breach; a service people provide their information to had someone snag it through an act of unauthorised access and publish a discrete corpus of information that can be attributed back to that source. But in the case of National Public Data, we're talking about a data aggregator most people had never heard of where a "threat actor" has published various *partial* sets of data with no clear way to attribute it back to the source. And [they're already the subject of a class action](https://news.bloomberglaw.com/privacy-and-data-security/background-check-data-of-3-billion-stolen-in-breach-suit-says?ref=troyhunt.com), to add yet another variable into the mix. I've been collating information related to this incident over the last couple of months, so let me talk about what's known about the incident, what data is circulating and what remains a bit of a mystery.

Let's start with the easy bit - who is [National Public Data](https://nationalpublicdata.com/?ref=troyhunt.com) (NPD)? They're what we refer to as a "data aggregator", that is they provide services based on the large volumes of personal information they hold. From the front page of their website:

> Criminal Records, Background Checks and more. Our services are currently used by investigators, background check websites, data resellers, mobile apps, applications and more.

There are *many* legally operating data aggregators out there... and there are many that end up with their data in [Have I Been Pwned](https://haveibeenpwned.com/?ref=troyhunt.com) (HIBP). For example, [Master Deeds](https://www.troyhunt.com/questions-about-the-massive-south-african-master-deeds-data-breach-answered/), [Exactis](https://www.wired.com/story/exactis-database-leak-340-million-records/?ref=troyhunt.com) and [Adapt](https://hackenproof.com/blog/industry-news/another-decision-makers-database-leaked?ref=troyhunt.com), to name but a few. In April, we started seeing news of National Public Data and billions of breached records, with one of the first references coming from the Dark Web Intelligence account:

> USDoD Allegedly Breached National Public Data Database, Selling 2.9 Billion Records [https://t.co/emQIZ0lgsn](https://t.co/emQIZ0lgsn?ref=troyhunt.com) [pic.twitter.com/Tt8UNppPSu](https://t.co/Tt8UNppPSu?ref=troyhunt.com)
>
> — Dark Web Intelligence (@DailyDarkWeb) [April 8, 2024](https://twitter.com/DailyDarkWeb/status/1777335594567283045?ref_src=twsrc%5Etfw&ref=troyhunt.com)

Back then, the breach was attributed to "USDoD", a name to remember as you'll see that throughout this post. The embedded image is the first reference of the 2.9B number we've subsequently seen flashed all over the press, and it's right there alongside the request of $3.5M for the data. Clearly, there is a financial motive involved here, so keep that in mind as we dig further into the story. That image also refers to 200GB of compressed data that expands out to 4TB when uncompressed, but that's not what initially caught my eye. Instead, something quite obvious in the embedded image doesn't add up: if this data is "the entire population of USA, CA and UK" (which is ~450M people in total), what's the 2.9B number we keep seeing? Because that doesn't reconcile with reports about ["nearly 3 billion people" with social security numbers exposed](https://mashable.com/article/background-check-company-breached-3-billion-affected?ref=troyhunt.com). Further, SSNs are a rather American construct with Canada having SINs (Social Insurance Number) and the UK having, well, NI (National Insurance) numbers are probably the closestequivalent. This is the constant theme you'll read about in this post, stuff just being a bit... off. But hyperbole is often a theme with incidents like this, so let's take the headlines with a grain of salt and see what the data tells us.

I was first sent data allegedly sourced from NPD in early June. The corpus I received reconciled with what vx-underground reported on around the same time (note their reference to the 8th of April, which also lines up with the previous tweet):

> April 8th, 2024, a Threat Actor operating under the moniker "USDoD" placed a large database up for sale on Breached titled: "National Public Data". They claimed it contained 2,900,000,000 records on United States citizens. They put the data up for sale for $3,500,000.
>
> National…
>
> — vx-underground (@vxunderground) [June 1, 2024](https://twitter.com/vxunderground/status/1797047998481854512?ref_src=twsrc%5Etfw&ref=troyhunt.com)

In their message, they refer to having received data totalling 277.1GB *uncompressed,* which aligns with the sum total of the 2 files I received:

![](https://www.troyhunt.com/content/images/2024/08/image-2-1.png)

They also mentioned the data contains first and last names, addresses and SSNs, all of which appear in the first file above (among other fields):

![](https://www.troyhunt.com/content/images/2024/08/image-1-1.png)

These first rows also line up precisely with [the post Dark Web Intelligence included in the earlier tweet](https://dailydarkweb.net/usdod-allegedly-leaks-national-public-data-database-exposing-2-9-billion-records/?ref=troyhunt.com). And in case you're looking at it and thinking "that's the same SSN repeated across multiple rows with different names", those records are all the same people, just with the names represented in different orders and with different addresses (all in the same city). In other words, those 6 rows only represent one person, which got me thinking about the ratio of rows to distinct numbers. Curious, I took 100M samples and found that only 31% of the rows had unique SSNs, so extrapolating that out, 2.9B would be more like 899M. This is something to always be conscious of when you read headline numbers: "2.9B" doesn't necessarily mean 2.9B *people*, it often means *rows of data*. Speaking of which, those 2 files contain 1,698,302,004 and 997,379,506 rows respectively for a combined total of 2.696B. Is this where the headline number comes from? Perhaps, it's close, and [it's also precisely the same as Bleeping Computer reported a few days ago](https://www.bleepingcomputer.com/news/security/hackers-leak-27-billion-data-records-with-social-security-numbers/?ref=troyhunt.com).

At this point in the story, there's no question that there is legitimate data in there. From the aforementioned Bleeping Computer story:

> numerous people have confirmed to us that it included their and family members' legitimate information, including those who are deceased

And in vx-underground's tweet, they mention that:

> It also allowed us to find their parents, and nearest siblings. We were able to identify someones parents, deceased relatives, Uncles, Aunts, and Cousins. Additionally, we can confirm this database also contains informed on individuals who are deceased. Some individuals located had been deceased for nearly 2 decades.

A quick tangential observation in the same tweet:

> The database DOES NOT contain information from individuals who use data opt-out services. Every person who used some sort of data opt-out service was not present.

Which is what you'd expect from a legally operating data aggregator service. It's a minor point, b...