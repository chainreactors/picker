---
title: FrodoPIR: New Privacy-Focused Database Querying System
url: https://thehackernews.com/2022/12/frodopir-new-privacy-focused-database.html
source: The Hacker News
date: 2022-12-24
fetch_date: 2025-10-04T02:27:53.846907
---

# FrodoPIR: New Privacy-Focused Database Querying System

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

# [FrodoPIR: New Privacy-Focused Database Querying System](https://thehackernews.com/2022/12/frodopir-new-privacy-focused-database.html)

**Dec 23, 2022**Ravie LakshmananEncryption / Privacy / Browser

[![Brave open-source web browser](data:image/png;base64... "Brave open-source web browser")](https://blogger.googleusercontent.com/img/b/R29vZ2xl/AVvXsEj79OEjTu7uo1_PMphTdL55aDVE2-3F1GYtp2A60d0b8JjfwwKRWgaLKrL-FAJFPbfHGXIHuAOu-tKOV8VtEi_HunbG5ptGgAo_BR64m7QJ9Q12nnAaUofcvG04yOne4KJJaok1IHdIrkARj17i36toNVrbnK8dUBwBp3VLJru89QzdjMkxzFO4CG_g/s790-rw-e365/webbrowser.png)

The developers behind the Brave open-source web browser have revealed a new privacy-preserving data querying and retrieval system called **FrodoPIR**.

The idea, the company [said](https://brave.com/frodopir/), is to use the technology to build out a wide range of use cases such as safe browsing, scanning passwords against breached databases, certificate revocation checks, and streaming, among others.

The scheme is called [FrodoPIR](https://eprint.iacr.org/2022/981) because "the client can perform hidden queries to the server, just as Frodo remained hidden from Sauron," a reference to the characters from J. R. R. Tolkien's [*The Lord of the Rings*](https://en.wikipedia.org/wiki/The_Lord_of_the_Rings).

PIR, short for [private information retrieval](https://en.wikipedia.org/wiki/Private_information_retrieval), is a cryptographic protocol that enables users (aka clients) to retrieve a piece of information from a database server without revealing to its owner which element was selected.

[![DFIR Retainer Services](data:image/png;base64...)](https://thehackernews.uk/cloud-insight-d)

In other words, the goal is to be able to query a platform for information (say, cooking videos) without letting the service provider infer from a user's search history to offer personalized recommendations or targeted ads based on the search criteria.

One way this is achieved is by using an approach called [homomorphic encryption](https://thenextweb.com/news/google-open-sources-cryptographic-tool-to-keep-data-sets-private), which allows computation to be performed directly on enciphered data without requiring access to a private key.

But a common problem afflicting such methods is that they are "expensive in terms of either bandwidth, or in the amount of time taken to process each client query," making them prohibitive for real-world deployments.

[![](data:image/png;base64...)](https://blogger.googleusercontent.com/img/b/R29vZ2xl/AVvXsEhJ_9WdrLG0bJpOLO4rTr2AlqUES6DuPnRYRJAXUJseOlzPTy1hU58nlwfBY_olEAO2QC-hcIq9IR9gxGe3AMewxf3HzWLnP1ICt-75cPn6Ly_qS5qmTFP7zfQMv6JC7_4AyKIeqV3Ekl_YC4NMSzobWaQJV_-13CI55k00A3mvg_lTOjB-NSaVhF61/s790-rw-e365/privacy.png)

That's where FrodoPIR steps in. It involves two phases, an offline preparatory step and an online step wherein the client transmits encrypted queries to the server.

The server subsequently opts to return a positive or negative value depending on whether or not the query is found in the database without learning what the user is actually querying for.

"In terms of performance for a database of 1 million KB elements, FrodoPIR requires <1 second for responding to a client query, has a server response size blow-up factor of > 3.6x, and financial costs are ~$1 for answering client queries," Brave [said](https://github.com/brave-experiments/frodo-pir) in a GitHub description of the project.

## Google Open Sources Two Privacy-Enhancing Technologies (PETs)

The development comes as Google [said](https://developers.googleblog.com/2022/12/new-privacy-enhancing-technology-for-everyone.html) it's open-sourcing two privacy-enhancing technologies (PETs) as part of its ongoing efforts to democratize access to techniques beyond [Federated Learning](https://ai.googleblog.com/2017/04/federated-learning-collaborative.html) and [Differential Privacy](https://developers.googleblog.com/2019/09/enabling-developers-and-organizations.html).

[![CIS Build Kits](data:image/png;base64...)](https://thehackernews.uk/platform-shield-d)

This consists of a new machine learning tool called [Magritte](https://github.com/google/magritte) that's designed to blur objects like license plates present in videos, as well as efficiency improvements to its Fully Homomorphic Encryption ([FHE](https://github.com/google/fully-homomorphic-encryption)) Transpiler.

The [transpiler](https://developers.googleblog.com/2021/06/our-latest-updates-on-fully-homomorphic-encryption.html), aka source-to-source compiler or translator, is designed to run computation-based queries on encrypted information sans any access to personally identifiable data.

The PETs "will provide the broader developer community (researchers, governments, nonprofits, businesses and more) new ways to deploy and enhance privacy features in their own work," Google noted.

Found this article interesting? Follow us on [Google News](https://news.google.com/publications/CAAqLQgKIidDQklTRndnTWFoTUtFWFJvWldoaFkydGxjbTVsZDNNdVkyOXRLQUFQAQ), [Twitter](https://twitter.com/thehackersnews) and [LinkedIn](https://www.linkedin.com/company/thehackernews/) to read more exclusive content we post.

SHARE
[**](#link_share)
[**](#link_share)
[**](#link_share)
**

[**Tweet](#link_share)

[**Share](#link_share)

[**Share](#link_share)

**Share

**
[**Share on Facebook](#link_share)
[**Share on Twitter](#link_share)
[**Share on Linkedin](#link_share)
[**Share on Reddit](#link_share)
[**Share on Hacker News](#link_share)
[**Share on Email](#link_share)
[**Share on WhatsApp](#link_share)
[![Facebook Messenger](data:image/png;base64...)Share on Facebook Messenger](#link_share)
[**Share on Telegram](#link_share)

SHARE **

[Brave Browser](https://thehackernews.com/search/label/Brave%20Browser)[FrodoPIR](https://thehackernews.com/search/label/FrodoPIR)[Google](https://thehackernews.com/search/label/Google)[Homomorphic Encryption](https://thehackernews.com/search/label/Homomorphic%20Encryption)[Privacy](https://thehackernews.com/search...