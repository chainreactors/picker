---
title: OVHcloud Hit with Record 840 Million PPS DDoS Attack Using MikroTik Routers
url: https://thehackernews.com/2024/07/ovhcloud-hit-with-record-840-million.html
source: The Hacker News
date: 2024-07-06
fetch_date: 2025-10-06T17:45:29.420878
---

# OVHcloud Hit with Record 840 Million PPS DDoS Attack Using MikroTik Routers

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

# [OVHcloud Hit with Record 840 Million PPS DDoS Attack Using MikroTik Routers](https://thehackernews.com/2024/07/ovhcloud-hit-with-record-840-million.html)

**Jul 05, 2024**Ravie LakshmananNetwork Security / DDoS Attack

[![DDoS Attack](data:image/png;base64... "DDoS Attack")](https://blogger.googleusercontent.com/img/b/R29vZ2xl/AVvXsEjv8yQJbaMN3G8tXS1dNVhkhSEwTHsVDt1j-VnFXftmXfqnhw4sipjp82UuyT2IZu6hflz9boojuGe4ly6eksnKlrUz-Ctbb0ypORh-D9vYLoDrvuai5ADyv83I5M2qiRBYUrr-hHFfCtwcW2qY6jxm917jmun7DeISn4lZtJAeddcHgcA6EOpyeUk8YVS1/s790-rw-e365/ddos-attack.png)

French cloud computing firm OVHcloud said it mitigated a record-breaking distributed denial-of-service (DDoS) attack in April 2024 that reached a packet rate of 840 million packets per second (Mpps).

This is just above the previous record of 809 million Mpps [reported](https://www.akamai.com/blog/news/largest-ever-recorded-packet-per-secondbased-ddos-attack-mitigated-by-akamai) by Akamai as targeting a large European bank in June 2020.

The 840 Mpps DDoS attack is said to have been a combination of a TCP ACK flood that originated from 5,000 source IPs and a DNS reflection attack leveraging about 15,000 DNS servers to amplify the traffic.

"While the attack was distributed worldwide, 2/3 of total packets entered from only four [points of presence], all located in the U.S. with 3 of them being on the west coast," OVHcloud [noted](https://blog.ovhcloud.com/the-rise-of-packet-rate-attacks-when-core-routers-turn-evil/). "This highlights the capability of the adversary to send a huge packet rate through only a few peerings, which can prove very problematic."

[![DFIR Retainer Services](data:image/png;base64...)](https://thehackernews.uk/cloud-insight-d)

The company said it has observed a significant uptick in DDoS attacks in terms of both frequency and intensity starting 2023, adding those reaching above 1 terabit per second (Tbps) have become a regular occurrence.

"In the past 18 months, we went from 1+ Tbps attacks being quite rare, then weekly, to almost daily (averaged out over one week)," OVHcloud's Sebastien Meriot said. "The highest bit rate we observed during that period was ~2.5 Tbps."

Unlike typical DDoS attacks that rely on sending a flood of junk traffic to targets with an aim to exhaust available bandwidth, packet rate attacks work by overloading the packet processing engines of networking devices close to the destination, such as load balancers.

[![DDoS Attack](data:image/png;base64... "DDoS Attack")](https://blogger.googleusercontent.com/img/b/R29vZ2xl/AVvXsEj4v_cUP2naBdZc3y6J6GE9iclHQrmDLkoTCDKJYVVn1bEaCWC86vmrZHTKzTzG8cggi-LhNQY0IJyzajfY5vQmLgptZpRlxKWFuihj5neorF5VG81hsdtF1k9tHn_1nzLgqbWWtggBCpQegTqzSDG0MxpOkNovU-lHgxHorRedBTwaqXyaCvFJjWAb8W_Z/s790-rw-e365/ddos.png)

Data gathered by the company shows that DDoS attacks leveraging packet rates greater than 100 Mpps have witnessed a sharp increase for the same time period, with many of them emanating from compromised MikroTik Cloud Core Router (CCR) devices. As many as 99,382 MikroTik routers are accessible over the internet.

These routers, besides exposing an administration interface, run on outdated versions of the operating system, making them susceptible to known security vulnerabilities in RouterOS. It's suspected that threat actors are likely weaponizing the operating system's Bandwidth test feature to pull off the attacks.

[![CIS Build Kits](data:image/png;base64...)](https://thehackernews.uk/platform-shield-d)

It's estimated that even hijacking 1% of the exposed devices into a DDoS botnet could theoretically give adversaries enough capabilities to launch [layer 7 attacks](https://www.cloudflare.com/learning/ddos/application-layer-ddos-attack/) reaching 2.28 billion packets per second (Gpps).

It bears noting at this stage that MikroTik routers have been [leveraged](https://thehackernews.com/2022/03/over-200000-microtik-routers-worldwide.html) for building potent botnets such as Mēris and even used for launching botnet-as-a-service operations.

"Depending on the number of compromised devices and their actual capabilities, this could be a new era for packet rate attacks: with botnets possibly capable of issuing billions of packets per second, it could seriously challenge how anti-DDoS infrastructures are built and scaled," Meriot said.

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

[Cloud computing](https://thehackernews.com/search/label/Cloud%20computing)[Cyber Attack](https://thehackernews.com/search/label/Cyber%20Attack)[Cyber Threat](https://thehackernews.com/search/label/Cyber%20Threat)[cybersecurity](https://thehackernews.com/search/label/cybersecurity)[ddos attack](https://thehackernews.com/search/label/ddos%20attack)[network security](https://thehackernews.com/search/label/network%20security)[Threat Intelligence](https://thehackernews.com/search/label/Threat%20Intelligence)

[![c](data:image/svg+xml;base64...)](https://thehackernews.uk/cloud-defense)

Trending News

[![Stop Alert Chaos: Context Is the Key to Effective Incident Response](data:image/svg+xml;base64... "Stop Alert Chaos: Context Is the Key to Effective Incident Response")

Stop Alert Chaos: Context Is the Key to Effective Incident Respo...