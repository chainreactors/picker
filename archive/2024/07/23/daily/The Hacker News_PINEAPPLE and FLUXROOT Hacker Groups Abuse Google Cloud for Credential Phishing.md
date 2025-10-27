---
title: PINEAPPLE and FLUXROOT Hacker Groups Abuse Google Cloud for Credential Phishing
url: https://thehackernews.com/2024/07/pineapple-and-fluxroot-hacker-groups.html
source: The Hacker News
date: 2024-07-23
fetch_date: 2025-10-06T17:48:15.389425
---

# PINEAPPLE and FLUXROOT Hacker Groups Abuse Google Cloud for Credential Phishing

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

# [PINEAPPLE and FLUXROOT Hacker Groups Abuse Google Cloud for Credential Phishing](https://thehackernews.com/2024/07/pineapple-and-fluxroot-hacker-groups.html)

**Jul 22, 2024**Ravie LakshmananCloud Security / Phishing Attack

[![Google Cloud for Credential Phishing](data:image/png;base64... "Google Cloud for Credential Phishing")](https://blogger.googleusercontent.com/img/b/R29vZ2xl/AVvXsEhxN548S3lNEFxg88a4otKes9YC08IadM9IcDuIerTjN16IlE0zGFsg_nO_MFIynlAYJYoa6lZVjG2OIvO3qYfn6zvaBMVLprtMgrrEFFLaRng5Xo33w-xa7KY-v6zNntvo1fvfD-VdoQuFe_8XCL9JnnD1-UstA_vvWtM7kz6hK68i8DBDRdfcGU8lXFwn/s790-rw-e365/google-cloud.png)

A Latin America (LATAM)-based financially motivated actor codenamed **FLUXROOT** has been observed leveraging Google Cloud serverless projects to orchestrate credential phishing activity, highlighting the abuse of the cloud computing model for malicious purposes.

"Serverless architectures are attractive to developers and enterprises for their flexibility, cost effectiveness, and ease of use," Google said in its biannual [Threat Horizons Report](https://services.google.com/fh/files/misc/threat_horizons_report_h2_2024.pdf) [PDF] shared with The Hacker News.

"These same features make serverless computing services for all cloud providers attractive to threat actors, who use them to deliver and communicate with their malware, host and direct users to phishing pages, and to run malware and execute malicious scripts specifically tailored to run in a serverless environment."

[![DFIR Retainer Services](data:image/png;base64...)](https://thehackernews.uk/cloud-insight-d)

The campaign involved the use of Google Cloud container URLs to host credential phishing pages with the aim of harvesting login information associated with Mercado Pago, an online payments platform popular in the LATAM region.

FLUXROOT, per Google, is the threat actor known for distributing the Grandoreiro banking trojan, with recent campaigns also taking advantage of legitimate cloud services like Microsoft Azure and Dropbox to distribute the malware.

Separately, Google's cloud infrastructure has also been weaponized by another adversary named PINEAPPLE to propagate another stealer malware known as [Astaroth](https://thehackernews.com/2024/06/grandoreiro-banking-trojan-hits-brazil.html) (aka Guildma) as part of attacks targeting Brazilian users.

"PINEAPPLE used compromised Google Cloud instances and Google Cloud projects they created themselves to create container URLs on legitimate Google Cloud serverless domains such as cloudfunctions[.]net and run.app," Google noted. "The URLs hosted landing pages redirecting targets to malicious infrastructure that dropped Astaroth."

Furthermore, the threat actor is said to have attempted to bypass email gateway protections by making use of mail forwarding services that do not drop messages with failed Sender Policy Framework ([SPF](https://en.wikipedia.org/wiki/Sender_Policy_Framework)) records, or incorporating unexpected data in the [SMTP Return-Path field](https://mxtoolbox.com/dmarc/spf/setup/spf-return-path) in order to trigger a DNS request timeout and cause email authentication checks to fail.

The search giant said it took steps to mitigate the activities by taking down the malicious Google Cloud projects and updating its [Safe Browsing lists](https://developers.google.com/safe-browsing/v4/lists).

[![CIS Build Kits](data:image/png;base64...)](https://thehackernews.uk/platform-shield-d)

The weaponization of cloud services and infrastructure by threat actors – ranging from illicit cryptocurrency mining as a [consequence](https://www.aquasec.com/blog/kubernetes-exposed-exploiting-the-kubelet-api/) of [weak configurations](https://www.cadosecurity.com/news-and-events/warpscan-cloudflare-warp-abused-to-hijack-cloud-services) to ransomware – has been [fueled](https://services.google.com/fh/files/misc/threat_horizons_report_h12024.pdf) by the enhanced adoption of cloud across industries.

Furthermore, the approach has the added benefit of allowing adversaries to [blend into normal network activities](https://thehackernews.com/2024/02/chinese-hackers-operate-undetected-in.html), making detection a lot more challenging.

"Threat actors take advantage of the flexibility and ease of deployment of serverless platforms to distribute malware and host phishing pages," the company said. "Threat actors abusing cloud services shift their tactics in response to defenders' detection and mitigation measures."

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

[Cloud security](https://thehackernews.com/search/label/Cloud%20security)[cybersecurity](https://thehackernews.com/search/label/cybersecurity)[Financial Cybercrime](https://thehackernews.com/search/label/Financial%20Cybercrime)[Google Cloud](https://thehackernews.com/search/label/Google%20Cloud)[Malware](https://thehackernews.com/search/label/Malware)[phishing attack](https://thehackernews.com/search/label/phishing%20attack)[Serverless](https://thehackernews.com/search/label/Serverless)

[![c](data:image/svg+xml;base64...)](https://thehackernews.uk/cloud-defense)

Trending News

[![Stop Alert Chaos: Context Is the Key to Effective Incident Response](data:image/svg+xml;base64... "...