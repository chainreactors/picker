---
title: How Searchable Encryption Changes the Data Security Game
url: https://thehackernews.com/2024/07/how-searchable-encryption-changes-data.html
source: The Hacker News
date: 2024-07-30
fetch_date: 2025-10-06T17:59:05.182918
---

# How Searchable Encryption Changes the Data Security Game

#1 Trusted Cybersecurity News Platform

Followed by 5.20+ million[**](https://twitter.com/thehackersnews)
[**](https://www.linkedin.com/company/thehackernews/)
[**](https://www.facebook.com/thehackernews)

[![The Hacker News Logo](data:image/png;base64...)](/)

**

**

[** Subscribe – Get Latest News](#email-outer)

* [** Home](/)
* [** Newsletter](#email-outer)
* [** Webinars](/p/upcoming-hacker-news-webinars.html)

* [Home](/)
* [Data Breaches](/search/label/data%20breach)
* [Cyber Attacks](/search/label/Cyber%20Attack)
* [Vulnerabilities](/search/label/Vulnerability)
* [Webinars](/p/upcoming-hacker-news-webinars.html)
* [Expert Insights](https://thehackernews.com/expert-insights/)
* [Contact](/p/submit-news.html)

**

**

**

Resources

* [Webinars](/p/upcoming-hacker-news-webinars.html)
* [Free eBooks](https://thehackernews.tradepub.com)

About Site

* [About THN](/p/about-us.html)
* [Jobs](/p/careers-technical-writer-designer-and.html)
* [Advertise with us](/p/advertising-with-hacker-news.html)

Contact/Tip Us

[**

Reach out to get featured—contact us to send your exclusive story idea, research, hacks, or ask us a question or leave a comment/feedback!](/p/submit-news.html)

Follow Us On Social Media

[**](https://www.facebook.com/thehackernews)
[**](https://twitter.com/thehackersnews)
[**](https://www.linkedin.com/company/thehackernews/)
[**](https://www.youtube.com/c/thehackernews?sub_confirmation=1)
[**](https://www.instagram.com/thehackernews/)

[** RSS Feeds](https://feeds.feedburner.com/TheHackersNews)
[** Email Alerts](#email-outer)

[![Salesforce Security Handbook](https://blogger.googleusercontent.com/img/b/R29vZ2xl/AVvXsEjWa8tsMNqlevi1HGF1ALQRGIq7hROPFAbHd3R1RTEOe73T8_Q2xW_-91t2jSGjU5peiPb8QYblGp4igNW-u2Qmlxbp2BKzTVMSvyXDZJmC-BYpiiJHrcnG5drmSP97iZ9PVIf1DeEr7U-7vWpe4HXwfMjt8FGNgq5mOycOJluYr9wF7YOKrQY9MfArwgjt/s728-e100/ai-agent-security-d.png)](https://thehackernews.uk/ai-agent-security-d)

# [How Searchable Encryption Changes the Data Security Game](https://thehackernews.com/2024/07/how-searchable-encryption-changes-data.html)

**Jul 29, 2024**The Hacker NewsData Security / Encryption

Searchable Encryption has long been a mystery. An oxymoron. An unattainable dream of cybersecurity professionals everywhere.

Organizations know they must encrypt their most valuable, sensitive data to prevent data theft and breaches. They also understand that organizational data exists to be used. To be searched, viewed, and modified to keep businesses running. Unfortunately, our Network and Data Security Engineers were taught for decades that you just can't search or edit data while in an encrypted state.

The best they could do was to wrap that plaintext, unencrypted data within a cocoon of complex hardware, software, policies, controls, and governance. And how has that worked to date? Just look at the T-Mobile breach, the United Healthcare breach, Uber, Verizon, Kaiser Foundation Health Plan, Bank of America, Prudential… and the list goes on. All the data that was stolen in those breaches remained unencrypted to support day-to-day operations.

It's safe to conclude that the way we're securing that data just isn't working. It's critical that we evolve our thought and approach. It's time to encrypt all data at rest, in transit, and also IN USE. So, how do we effectively encrypt data that needs to be used?

## **The Encryption Challenge**

[![Data Security Game](data:image/png;base64... "Data Security Game")](https://blogger.googleusercontent.com/img/b/R29vZ2xl/AVvXsEiaNFfZoX58KrOoNAln3Gcc2jtXo1cc6BSpmTM4PPfOweryzPVPpxWTbi87vUxQDyFxvjjt1OhIuKxU1lPhz-iJAvp2EoLKjb9EPC5b4I4tFR-Jp18eUUFm0PENSfj-EyuNXOo4hMrfknF0rRUb-hlzB5ZcmUZ6fVdGkwR7uKRSV31R4cyl0LgGlFTYicA/s1700/main.png)

As stated, it's well established that most data is not being encrypted. Just look at the well documented, ongoing growth rate of cybercrime activity. In short, all data breaches and data ransom cases have one glaring common thread— every target maintains millions of private, sensitive, and confidential records in an unencrypted state. Stores of data, fully indexed, structured and unencrypted as easy to read plaintext simply to support operational use cases. This challenge falls under the auspices of "Acceptable Risk".

It's often viewed that if an organization has good cyber hygiene, that organization is encrypting data at rest (in storage, archived, or backed up) and in transit or motion (i.e. email encryption, or sending data from one point to another point). And many may think that's enough—or that is the best they can do. After all, encryption at rest and in motion is the only encryption focus of current compliance and governance bodies, where they address database encryption.

In truth, most compliance lacks any real definition of what would be considered strong database encryption. Unfortunately, the mindset for many is still 'if compliance doesn't address it, it must not be that important, right?'

Let's unpack this a little. Why don't we encrypt data? Encryption has a reputation for being complex, expensive, and difficult to manage.

Just looking at traditional encryption of data at rest (archives and static data), these encryption solutions commonly involve a complete "lift and shift" of the database to the encryption at rest solution. This exercise often requires a network architect, database administrator, detailed mapping, and *time*.

Once encrypted, and assuming that long-string encryption such as AES 256 is utilized, the data is only secure right up to the point that it is needed. The data will eventually be needed to support a business function, such as customer service, sales, billing, financial service, healthcare, audit, and/or general update operations. At that point, the entire required dataset (whether the full database or a segment) needs to be decrypted and moved to a datastore as vulnerable plaintext.

This brings another layer of complexity—the expertise of a DBA or database expert, time to decrypt, the build out of a security enclave of complex solutions designed to monitor and "secure" the plaintext datastore. Now this enclave of complex solutions requires a specialized team of experts with knowledge of how each of those security tools function. Add in the need to patch and refresh each of those security tools just to maintain their effectiveness, and we now understand why so much data is compromised daily.

Of course, once the data set has been utilized, it's supposed to be moved back to its encrypted state. So, the cycle of complexity (and expense) begins again.

Because of this cycle of complexity, in many situations, this sensitive data remains in a completely unencrypted, vulnerable state, so it is always readily available. 100% of threat actors agree that unencrypted data is the best kind of data for them to easily access.

This example focuses on encryption of data at rest, but it's important to note that data encrypted in transit goes through much of the same process—it's only encrypted in transit but needs to be decrypted for use on both ends of the transaction.

There is a much better approach. One that goes beyond baseline encryption. A modern, more complete database encryption strategy must account for encryption of critical database data in three states: at rest, in motion, and now IN USE. Searchable Encryption, also called Encryption-in-Use, [keeps that data fully encrypted while it's still usable](https://paperclip.com/safe/?utm_source=publication&utm_medium=the_hacker_news&utm_campaign=safe_gtm). Removing the complexity and expense related to supporting an archaic encrypt, decrypt, use, re-encrypt process.

[![Data Security Game](data:image/png;base64... "Data Security Game")](https://blogger.googleusercontent.com/img/b/R29vZ2xl/AVvXsEjjaopT8kmjLCOXsbVt-QCHYdzCz2wdy5dwdzh7FQ3vYncnL8-Lio8ALS7Nm9Y_1_p2tIjFX0fxTkM46dZYutsy3mCKXT8EgIsuvHt380sz8OKBBWY_D_GN69HZVxzzApdjCaqod8_9Gsbi2Wq8712qHTvblDDI7c48834D_8MUWlZT5lTEzAvTyK1iEoc...