---
title: Critical RCE Flaw in GFI KerioControl Allows Remote Code Execution via CRLF Injection
url: https://thehackernews.com/2025/01/critical-rce-flaw-in-gfi-keriocontrol.html
source: The Hacker News
date: 2025-01-10
fetch_date: 2025-10-06T20:12:51.319062
---

# Critical RCE Flaw in GFI KerioControl Allows Remote Code Execution via CRLF Injection

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

# [Critical RCE Flaw in GFI KerioControl Allows Remote Code Execution via CRLF Injection](https://thehackernews.com/2025/01/critical-rce-flaw-in-gfi-keriocontrol.html)

**Jan 09, 2025**Ravie LakshmananVulnerability / Threat Intelligence

[![GFI KerioControl](data:image/png;base64... "GFI KerioControl")](https://blogger.googleusercontent.com/img/b/R29vZ2xl/AVvXsEjunIfQFH4Bbh4G7ZlmeDYZ9hKZ2oJBvVP9hmRVt8X6Y-t9UpVGCirikcmYn4RQ1cbqbKPFML73wb9P-0h_pmHq8evdIt5ZBd8Xvd6faqLXMSyFss1wb9qypw-vYmA2RBeOEgt21RgJEoxrHxGJoMLZZQbNVN8uYQVyqUzNXvx3NkUMqYIjpothYI_m-koF/s790-rw-e365/kerio.png)

Threat actors are attempting to take advantage of a recently disclosed security flaw impacting [GFI KerioControl](https://gfi.ai/products-and-solutions/network-security-solutions/keriocontrol) firewalls that, if successfully exploited, could allow malicious actors to achieve remote code execution (RCE).

The [vulnerability](https://thehackernews.com/2024/12/thn-weekly-recap-top-cybersecurity.html) in question, **CVE-2024-52875**, refers to a carriage return line feed ([CRLF](https://owasp.org/www-community/vulnerabilities/CRLF_Injection)) injection attack, paving the way for [HTTP response splitting](https://capec.mitre.org/data/definitions/34.html), which could then lead to a cross-site scripting (XSS) flaw.

Successful exploitation of the 1-click RCE flaw permits an attacker to inject malicious inputs into HTTP response headers by introducing carriage return (\r) and line feed (\n) characters.

[![DFIR Retainer Services](data:image/png;base64...)](https://thehackernews.uk/cloud-insight-d)

The flaw impacts KerioControl versions 9.2.5 through 9.4.5, according to security researcher Egidio Romano, who [discovered and reported](https://karmainsecurity.com/hacking-kerio-control-via-cve-2024-52875) the flaw in early November 2024.

The HTTP response splitting flaws have been uncovered in the following URI paths -

* /nonauth/addCertException.cs
* /nonauth/guestConfirm.cs
* /nonauth/expiration.cs

"User input passed to these pages via the 'dest' GET parameter is not properly sanitized before being used to generate a 'Location' HTTP header in a 302 HTTP response," Romano [said](https://karmainsecurity.com/KIS-2024-07).

"Specifically, the application does not correctly filter/remove line feed (LF) characters. This can be exploited to perform HTTP Response Splitting attacks, which, in turn, might allow it to carry out reflected cross-site scripting (XSS) and possibly other attacks."

A fix for the vulnerability was released by GFI on December 19, 2024, with [version 9.4.5 Patch 1](https://gfi.ai/products-and-solutions/network-security-solutions/keriocontrol/resources/documentation/product-releases). A proof-of-concept (PoC) exploit has since been made available.

Specifically, an adversary could craft a malicious URL such that an administrator user clicking on it triggers the execution of the PoC hosted on an attacker-controlled server, which then uploads a malicious .img file via the firmware upgrade functionality, granting root access to the firewall.

[![CIS Build Kits](data:image/png;base64...)](https://thehackernews.uk/platform-shield-d)

Threat intelligence firm GreyNoise has [reported](https://viz.greynoise.io/tags/kerio-control-cve-2024-52875-crlf-injection-attempt?days=30) that exploitation attempts targeting CVE-2024-52875 commenced back on December 28, 2024, with the attacks originating from seven unique IP addresses from Singapore and Hong Kong to date.

According to [Censys](https://censys.com/cve-2024-52875/), there are more than 23,800 internet-exposed GFI KerioControl instances. A majority of these servers are located in Iran, Uzbekistan, Italy, Germany, the United States, Czechia, Belarus, Ukraine, Russia, and Brazil.

The exact nature of the attacks exploiting the flaw is presently not known. Users of KerioControl are advised to take steps to secure their instances as soon as possible to mitigate potential threats.

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

[Cross-site Scripting](https://thehackernews.com/search/label/Cross-site%20Scripting)[cybersecurity](https://thehackernews.com/search/label/cybersecurity)[Firewall](https://thehackernews.com/search/label/Firewall)[network security](https://thehackernews.com/search/label/network%20security)[remote code execution](https://thehackernews.com/search/label/remote%20code%20execution)[Threat Intelligence](https://thehackernews.com/search/label/Threat%20Intelligence)[Vulnerability](https://thehackernews.com/search/label/Vulnerability)

[![c](data:image/svg+xml;base64...)](https://thehackernews.uk/cloud-defense)

Trending News

[![Stop Alert Chaos: Context Is the Key to Effective Incident Response](data:image/svg+xml;base64... "Stop Alert Chaos: Context Is the Key to Effective Incident Response")

Stop Alert Chaos: Context Is the Key to Effective Incident Response](https://thehackernews.com/2025/09/stop-alert-chaos-context-is-key-to.html)

[![Evolving Enterprise Defense to Secure the Modern AI Supply Chain](data:image/svg+xml;base64... "Evolving Enterprise Defense to Secure the Modern AI Supply Chain")

Evolving Enterprise Defense to Secure the Modern AI Supply Chain](https://thehackernews.com/2025/09...