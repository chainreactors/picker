---
title: RANsacked: Over 100 Security Flaws Found in LTE and 5G Network Implementations
url: https://thehackernews.com/2025/01/ransacked-over-100-security-flaws-found.html
source: The Hacker News
date: 2025-01-25
fetch_date: 2025-10-06T20:13:03.221738
---

# RANsacked: Over 100 Security Flaws Found in LTE and 5G Network Implementations

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

# [RANsacked: Over 100 Security Flaws Found in LTE and 5G Network Implementations](https://thehackernews.com/2025/01/ransacked-over-100-security-flaws-found.html)

**Jan 24, 2025**Ravie LakshmananTelecom Security / Vulnerability

[![LTE and 5G Network Implementations](data:image/png;base64... "LTE and 5G Network Implementations")](https://blogger.googleusercontent.com/img/b/R29vZ2xl/AVvXsEhePNFbvgxIjP-qdgsmvOht_nOITaHPOed2POnKRuzai8xmQQiM76JLTWhZSsiTrScJiB06CPp1hgV2bqTbMmZ9_qypISemoRrD2TlGIs4rkkpp3b8bkoub12eN2PYMGZZ8IDmtiTL1o5faQrwAoSM3xkiXmV1BdeSgC4Rs1COh6E0055YtP9a2GNizFXMs/s790-rw-e365/telecom.png)

A group of academics has disclosed details of over 100 security vulnerabilities impacting LTE and 5G implementations that could be exploited by an attacker to disrupt access to service and even gain a foothold into the cellular core network.

The [119 vulnerabilities](https://cellularsecurity.org/ransacked), assigned 97 unique CVE identifiers, span seven LTE implementations – [Open5GS](https://open5gs.org/), [Magma](https://magmacore.org), [OpenAirInterface](https://openairinterface.org/), [Athonet](https://www.hpe.com/us/en/solutions/athonet.html), [SD-Core](https://opennetworking.org/sd-core/), [NextEPC](https://nextepc.org/), [srsRAN](https://www.srsran.com) – and three 5G implementations – Open5GS, Magma, OpenAirInterface, according to researchers from the University of Florida and North Carolina State University.

[![DFIR Retainer Services](data:image/png;base64...)](https://thehackernews.uk/cloud-insight-d)

The findings have been detailed in a study titled "RANsacked: A Domain-Informed Approach for Fuzzing LTE and 5G RAN-Core Interfaces."

"Every one of the >100 vulnerabilities discussed below can be used to persistently disrupt all cellular communications (phone calls, messaging and data) at a city-wide level," the researchers said.

"An attacker can continuously crash the Mobility Management Entity (MME) or Access and Mobility Management Function (AMF) in an LTE/5G network, respectively, simply by sending a single small data packet over the network as an unauthenticated user (no SIM card required)."

[![](data:image/png;base64...)](https://blogger.googleusercontent.com/img/b/R29vZ2xl/AVvXsEjUtfj_kVKnjkpfFb2jyO6fptlIWBJqMvhl1x_zfOWX75ZIUg1N_RnIwJN-qRa2pOb3eijWh_tFImJsYOqvvoRDns9zsfNaxNdGa0nejC0axlEIPH2x-8c7hRfi1k94byLvEAt0GXgNyG-FuNgARoxEcBq3d8ULnpFf5dYng7Y1wnf6JNU_31OxAQpxov62/s790-rw-e365/telecom.png)

The discovery is the result of a [fuzzing exercise](https://github.com/FICS/asnfuzzgen), dubbed RANsacked, undertaken by the researchers against Radio Access Network ([RAN](https://en.wikipedia.org/wiki/Radio_access_network))-Core interfaces that are capable of receiving input directly from mobile handsets and base stations.

The researchers said several of the identified vulnerabilities relate to buffer overflows and memory corruption errors that could be weaponized to breach the cellular core network, and leverage that access to monitor cellphone location and connection information for all subscribers at a city-wide level, carry out targeted attacks on specific subscribers, and perform further malicious actions on the network itself.

What's more, the identified flaws fall under two broad categories: Those that can be exploited by any unauthenticated mobile device and those that can be weaponized by an adversary who has [compromised a base station](https://thehackernews.com/2021/12/new-mobile-network-vulnerabilities.html) or a [femtocell](https://en.wikipedia.org/wiki/Femtocell).

[![CIS Build Kits](data:image/png;base64...)](https://thehackernews.uk/platform-shield-d)

Of the 119 vulnerabilities discovered, 79 were found in MME implementations, 36 in AMF implementations, and four in SGW implementations. Twenty-five shortcomings lead to Non-Access Stratum ([NAS](https://en.wikipedia.org/wiki/Non-access_stratum)) pre-authentication attacks that can be carried out by an arbitrary cellphone.

"The introduction of home-use femtocells, followed by more easily-accessible gNodeB base stations in 5G deployments, represent a further shift in security dynamics: where once physically locked-down, RAN equipment is now openly exposed to physical adversarial threats," the study noted.

"Our work explores the implications of this final area by enabling performant fuzzing interfaces that have historically been assumed implicitly secure but now face imminent threats."

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

[5G](https://thehackernews.com/search/label/5G)[cybersecurity](https://thehackernews.com/search/label/cybersecurity)[Fuzzing](https://thehackernews.com/search/label/Fuzzing)[LTE](https://thehackernews.com/search/label/LTE)[mobile security](https://thehackernews.com/search/label/mobile%20security)[network security](https://thehackernews.com/search/label/network%20security)[Telecom Security](https://thehackernews.com/search/label/Telecom%20Security)[Vulnerability](https://thehackernews.com/search/label/Vulnerability)

[![c](data:image/svg+xml;base64...)](https://thehackernews.uk/cloud-defense)

Trending News

[![Stop Alert Chaos: Context Is the Key to Effective Incident Response](data:image/svg+xml;base64... "Stop Alert Chaos: Co...