---
title: 295 Malicious IPs Launch Coordinated Brute-Force Attacks on Apache Tomcat Manager
url: https://thehackernews.com/2025/06/295-malicious-ips-launch-coordinated.html
source: The Hacker News
date: 2025-06-12
fetch_date: 2025-10-06T22:56:20.478516
---

# 295 Malicious IPs Launch Coordinated Brute-Force Attacks on Apache Tomcat Manager

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

# [295 Malicious IPs Launch Coordinated Brute-Force Attacks on Apache Tomcat Manager](https://thehackernews.com/2025/06/295-malicious-ips-launch-coordinated.html)

**Jun 11, 2025**Ravie LakshmananNetwork Security / Threat Intelligence

[![Apache Tomcat Manager](data:image/png;base64... "Apache Tomcat Manager")](https://blogger.googleusercontent.com/img/b/R29vZ2xl/AVvXsEimdep8SDHWYbr2GAaIAWdXa5EGNI5dDidI1f7JyxTaWaWxtiA_hbCwKiQ5CTLC5pnWxbUCVYr0Ol6RJKUgZ9OKqydQTfsSA4FF1tB3h9ev_kmTwIo50JbRuf992lT0ptqg4ZXGZhpWccyov72WKu_AF94QEl300VWvPtYIu_tTdgJ6t3DfGq_OPcEMX2r0/s790-rw-e365/cyber.jpg)

Threat intelligence firm GreyNoise has warned of a "coordinated brute-force activity" targeting Apache Tomcat Manager interfaces.

The company said it [observed](https://www.greynoise.io/blog/coordinated-brute-force-activity-targeting-apache-tomcat-manager) a surge in brute-force and login attempts on June 5, 2025, an indication that they could be deliberate efforts to "identify and access exposed Tomcat services at scale."

To that end, 295 unique IP addresses have been found to be engaged in brute-force attempts against Tomcat Manager on that date, with all of them classified as malicious. Over the past 24 hours, [188 unique IPs](https://viz.greynoise.io/query/tags%3A%22Tomcat%20Manager%20Brute%20Force%20Attempt%22%20last_seen%3A1d) have been recorded, a majority of them located in the United States, the United Kingdom, Germany, the Netherlands, and Singapore.

[![DFIR Retainer Services](data:image/png;base64...)](https://thehackernews.uk/cloud-insight-d)

In a similar vein, [298 unique IPs](https://viz.greynoise.io/query/tags%3A%22Tomcat%20Manager%20Login%20Attempt%22%20last_seen%3A1d) were observed conducting login attempts against Tomcat Manager instances. Of the 246 IP addresses flagged in the last 24 hours, all of them are categorized as malicious and originate from the same locations.

Targets of these attempts include the United States, the United Kingdom, Spain, Germany, India, and Brazil for the same time period. GreyNoise noted that a significant chunk of the activity came from infrastructure hosted by DigitalOcean (ASN 14061).

"While not tied to a specific vulnerability, this behavior highlights ongoing interest in exposed Tomcat services," the company added. "Broad, opportunistic activity like this often serves as an early warning of future exploitation."

To mitigate any potential risks, organizations with exposed Tomcat Manager interfaces are recommended to implement strong authentication and access restrictions, and monitor for any signs of suspicious activity.

The disclosure comes as Bitsight revealed that it found more than 40,000 security cameras openly accessible on the internet, potentially enabling anyone to access live video feeds captured by these devices over HTTP or Real-Time Streaming Protocol (RTSP). The exposures are concentrated in the United States, Japan, Austria, Czechia, and South Korea.

The telecommunications sector accounts for 79% of the exposed cameras, followed by technology (6%), media (4.1%), utilities (2.5%), education (2.2%), business services (2.2%), and government (1.2%).

The installations range from those installed in residences, offices, public transportation systems, and factory settings, inadvertently leaking sensitive information that could then be exploited for espionage, stalking, and extortion.

[![CIS Build Kits](data:image/png;base64...)](https://thehackernews.uk/platform-shield-d)

Users are advised to change default usernames and passwords, disable remote access if not required (or restrict access with firewalls and VPNs), and keep firmware up-to-date.

"These cameras – intended for security or convenience – have inadvertently become public windows into sensitive spaces, often without their owners' knowledge," security researcher João Cruz [said](https://www.bitsight.com/blog/bitsight-identifies-thousands-of-compromised-security-cameras) in a report shared with The Hacker News.

"No matter the reason why one individual or organization needs this kind of device, the fact that anyone can buy one, plug it in, and start streaming with minimal setup is likely why this is still an ongoing threat."

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

[Apache Tomcat](https://thehackernews.com/search/label/Apache%20Tomcat)[Brute force](https://thehackernews.com/search/label/Brute%20force)[cybersecurity](https://thehackernews.com/search/label/cybersecurity)[DigitalOcean](https://thehackernews.com/search/label/DigitalOcean)[Incident response](https://thehackernews.com/search/label/Incident%20response)[iot security](https://thehackernews.com/search/label/iot%20security)[network security](https://thehackernews.com/search/label/network%20security)[Security Cameras](https://thehackernews.com/search/label/Security%20Cameras)[surveillance](https://thehackernews.com/search/label/surveillance)[Telecom Security](https://thehackernews.com/search/label/Telecom%20Security)[Threat Intelligence](https://thehackernews.com/search/label/Threat%20Intelligence)[Vulnerability](https://thehackernews.com/search/label/Vulnerability)

[![c](data:image/svg+xml;base64...)](https://thehackernews.uk/cloud-defense)

Trending News

[![St...