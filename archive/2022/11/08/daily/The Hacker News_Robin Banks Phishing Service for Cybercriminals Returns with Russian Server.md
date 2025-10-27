---
title: Robin Banks Phishing Service for Cybercriminals Returns with Russian Server
url: https://thehackernews.com/2022/11/robin-banks-phishing-service-for.html
source: The Hacker News
date: 2022-11-08
fetch_date: 2025-10-03T21:59:37.229864
---

# Robin Banks Phishing Service for Cybercriminals Returns with Russian Server

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

# [Robin Banks Phishing Service for Cybercriminals Returns with Russian Server](https://thehackernews.com/2022/11/robin-banks-phishing-service-for.html)

**Nov 07, 2022**Ravie Lakshmanan

[![Robin Banks Phishing Service](data:image/png;base64... "Robin Banks Phishing Service")](https://blogger.googleusercontent.com/img/b/R29vZ2xl/AVvXsEgayyjGZ19P9Gkf7iUwdz9-LyjSQve2VFHLTckF6juxDRjsZXgsllm7HBQ0Z_J2iy2EBDcXBRnaKj_w3jqu-UiOp7gkBqnmK1Yiug9LEG7jD4WZaaxhB6pdZWDtH5PdfmqXxRZ65n61fUXhCbnxAFzAlYF-C8U_Cyy3hLniyA8hvgBkgvz6OTZ1-tWM/s790-rw-e365/phishing.jpg)

A phishing-as-a-service (PhaaS) platform known as **Robin Banks** has relocated its attack infrastructure to DDoS-Guard, a Russian provider of bulletproof hosting services.

The switch comes after "Cloudflare disassociated Robin Banks phishing infrastructure from its services, causing a multi-day disruption to operations," according to a [report](https://www.ironnet.com/blog/robin-banks-still-might-be-robbing-your-bank-part-2) from cybersecurity company IronNet.

Robin Banks was [first documented](https://thehackernews.com/2022/07/researchers-warns-of-increase-in.html) in July 2022 when the platform's abilities to offer ready-made phishing kits to criminal actors were revealed, making it possible to steal the financial information of customers of popular banks and other online services.

It was also found to prompt users to enter Google and Microsoft credentials on rogue landing pages, suggesting an attempt on part of the malware authors to monetize initial access to corporate networks for post-exploitation activities such as espionage and ransomware.

[![DFIR Retainer Services](data:image/png;base64...)](https://thehackernews.uk/cloud-insight-d)

In recent months, Cloudflare's decision to blocklist its infrastructure in the wake of public disclosure has prompted the Robin Banks actor to move its frontend and backend to DDoS-Guard, which has in the past [hosted](https://www.group-ib.com/media-center/press-releases/ddos-guard-database/) the alt-tech social network [Parler](https://krebsonsecurity.com/2021/01/ddos-guard-to-forfeit-internet-space-occupied-by-parler/) and the notorious [Kiwi Farms](https://ddos-guard.net/en/info/blog-detail/ddos-guard-terminating-services-for-kiwi-farms).

"This hosting provider is also notorious in not complying with takedown requests, thus making it more appealing in the eyes of threat actors," the researchers noted.

Chief among the new updates introduced is a cookie-stealing functionality, in what's seen as an attempt to serve a broader clientele such as advanced persistent threat (APT) groups that are looking to compromise specific enterprise environments. It's offered for $1,500 per month.

[![Robin Banks Phishing Service](data:image/png;base64... "Robin Banks Phishing Service")](https://blogger.googleusercontent.com/img/b/R29vZ2xl/AVvXsEj4M78T8a76XVSo7gQJOqgMmDdDEoR-t6vSgwW3VaEAfjamy9k7F3dttsy0nqm9wv08T4TMiDCXUS_RGWkFxvfbt1_Wg4nxOGACqJZGcNYPcN0ETAq-26b-skaORGwSAs8m8a-sDWXoaHGOP_TrsenZuUY0huD4jsXpHRV2AQwcobwmetCaHkFCmkr6/s790-rw-e365/code.jpg)

This is achieved by reusing code from [evilginx2](https://github.com/kgretzky/evilginx2), an open source adversary-in-the-middle ([AiTM](https://thehackernews.com/2022/08/researchers-warn-of-aitm-attack.html)) attack framework employed to steal credentials and session cookies from Google, Yahoo, and Microsoft Outlook even on accounts that have multi-factor authentication (MFA) enabled.

Robin Banks is also said to have incorporated a new security measure that requires its customers to turn on two-factor authentication (2FA) to view the stolen information via the service, or, alternatively, receive the data through a Telegram bot.

Another notable feature is its use of [Adspect](https://docs.adspect.ai/en/latest/overview.html), an ad fraud detection service, to redirect targets of phishing campaigns to rogue websites, while leading scanners and unwanted traffic to benign websites to slip under the radar.

[![CIS Build Kits](data:image/png;base64...)](https://thehackernews.uk/platform-shield-d)

The findings are just the latest in a series of new PhaaS services that have emerged in the threat landscape, including [Frappo, EvilProxy](https://thehackernews.com/2022/09/new-evilproxy-phishing-service-allowing.html), and [Caffeine](https://thehackernews.com/2022/10/researchers-warn-of-new-phishing-as.html), making cybercrime more accessible to amateur and experienced bad actors alike.

What's more, the improvements also illustrate the growing need for threat actors to rely on different methods such as AiTM and prompt bombing (aka MFA fatigue) – as recently observed in the case of [Uber](https://thehackernews.com/2022/09/uber-blames-lapsus-hacking-group-for.html) – to circumvent security measures and gain initial access.

"The infrastructure of the Robin Banks phishing kit relies heavily on open source code and off-the-shelf tooling, serving as a prime example of the lowering barrier-to-entry to not only conducting phishing attacks, but also to creating a PhaaS platform for others to use," the researchers said.

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

[CloudFlare](https://thehackernews.com/search/label/CloudFlare...