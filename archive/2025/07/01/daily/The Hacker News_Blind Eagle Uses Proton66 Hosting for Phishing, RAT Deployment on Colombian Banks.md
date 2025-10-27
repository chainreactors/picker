---
title: Blind Eagle Uses Proton66 Hosting for Phishing, RAT Deployment on Colombian Banks
url: https://thehackernews.com/2025/06/blind-eagle-uses-proton66-hosting-for.html
source: The Hacker News
date: 2025-07-01
fetch_date: 2025-10-06T23:58:21.620770
---

# Blind Eagle Uses Proton66 Hosting for Phishing, RAT Deployment on Colombian Banks

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

# [Blind Eagle Uses Proton66 Hosting for Phishing, RAT Deployment on Colombian Banks](https://thehackernews.com/2025/06/blind-eagle-uses-proton66-hosting-for.html)

**Jun 30, 2025**Ravie LakshmananCybercrime / Vulnerability

[![Proton66 Hosting for Phishing, RAT](data:image/png;base64... "Proton66 Hosting for Phishing, RAT")](https://blogger.googleusercontent.com/img/b/R29vZ2xl/AVvXsEgCBZZMZ9PZhmGIu_fUYJYOr7FcwnPlKA0D5Mvzys6aOhYtrmLI-kJptHeAxvaTbVYVPEX6OUbjPGYctJyLa9UrNP8R82B_8yw6F9hwmWDLg8WqJHjO22S05HtPwgx0DNpn0ivjbG9vHGMpy75pV-bqfTyh9CaEMCWlLpexn5jrVwFjhGyibT2FQL6JTCGZ/s790-rw-e365/coin.jpg)

The threat actor known as [Blind Eagle](https://thehackernews.com/2025/03/blind-eagle-hacks-colombian.html) has been attributed with high confidence to the use of the Russian bulletproof hosting service [Proton66](https://thehackernews.com/2025/04/hackers-abuse-russian-bulletproof-host.html).

Trustwave SpiderLabs, in a [report](https://www.trustwave.com/en-us/resources/blogs/spiderlabs-blog/tracing-blind-eagle-to-proton66/) published last week, said it was able to make this connection by pivoting from Proton66-linked digital assets, leading to the discovery of an active threat cluster that leverages Visual Basic Script (VBS) files as its initial attack vector and installs off-the-shelf remote access trojans (RATS).

Many threat actors rely on bulletproWhile Visual Basic Script (VBS) might seem outdated, it's still aof hosting providers like Proton66 because these services intentionally ignore abuse reports and legal takedown requests. This makes it easier for attackers to run phishing sites, command-and-control servers, and malware delivery systems without interruption.

The cybersecurity company said it identified a set of domains with a similar naming pattern (e.g., gfast.duckdns[.]org, njfast.duckdns[.]org) beginning in August 2024, all of which resolved to the same IP address ("45.135.232[.]38") that's associated with Proton66.

The use of dynamic DNS services like DuckDNS also plays a key role in these operations. Instead of registering new domains each time, attackers rotate subdomains tied to a single IP address — making detection harder for defenders.

[![DFIR Retainer Services](data:image/png;base64...)](https://thehackernews.uk/cloud-insight-d)

"The domains in question were used to host a variety of malicious content, including phishing pages and VBS scripts that serve as the initial stage of malware deployment," security researcher Serhii Melnyk said. "These scripts act as loaders for second-stage tools, which, in this campaign, are limited to publicly available and often open-source RATs."

While VBS might seem outdated, it's still a go-to tool for initial access due to its compatibility with Windows systems and ability to run silently in the background. Attackers use it to download malware loaders, bypass antivirus tools, and blend into normal user activity. These lightweight scripts are often the first step in multi-stage attacks, which later deploy RATs, data stealers, or keyloggers.

The phishing pages have been found to legitimate Colombian banks and financial institutions, including Bancolombia, BBVA, Banco Caja Social, and Davivienda. Blind Eagle, also known as AguilaCiega, APT-C-36, and APT-Q-98, is known for its targeting of entities in South America, particularly Colombia and Ecuador.

The deceptive sites are engineered to harvest user credentials and other sensitive information. The VBS payloads hosted on the infrastructure come fitted with capabilities to retrieve encrypted executable files from a remote server, essentially acting as a loader for commodity RATS like AsyncRAT or Remcos RAT.

Furthermore, an analysis of the VBS codes has revealed overlaps with Vbs-Crypter, a tool linked to a subscription-based crypter service called [Crypters and Tools](https://thehackernews.com/2025/06/rust-based-myth-stealer-malware-spread.html) that's used to obfuscate and pack VBS payloads with an aim to avoid detection.

Trustwave said it also discovered a botnet panel that allows users to "control infected machines, retrieve exfiltrated data, and interact with infected endpoints through a broad set of capabilities typically found in commodity RAT management suites."

[![CIS Build Kits](data:image/png;base64...)](https://thehackernews.uk/platform-shield-d)

The disclosure comes as Darktrace revealed details of a Blind Eagle campaign that has been targeting Colombian organizations since November 2024 by exploiting a now-patched Windows flaw (CVE-2024-43451) to download and execute the next-stage payload, a behavior that was [first documented](https://thehackernews.com/2025/03/blind-eagle-hacks-colombian.html) by Check Point in March 2025.

[![](data:image/png;base64...)](https://blogger.googleusercontent.com/img/b/R29vZ2xl/AVvXsEghpJwIebap24c3iw49XTeJqmxjiwRsrajUXS4bpOuNNgbJ2UC3OF336Vt7NQZKFQNgTPtHBwNarC-hUysUtlQ5DYr_i3OTXuRbIejhiSMWl-3rIq17vbe7JUEevnLsspLmdgx2NUQuqDXAjTjwSr7iG5-9YBhD4zSMWTPeFZNj0wyfh8SwI0sX5fbrMBqv/s790-rw-e365/code.jpg)

"The persistence of Blind Eagle and ability to adapt its tactics, even after patches were released, and the speed at which the group were able to continue using pre-established TTPs highlights that timely vulnerability management and patch application, while essential, is not a standalone defense," the company [said](https://www.darktrace.com/blog/patch-and-persist-darktraces-detection-of-blind-eagle-apt-c-36).

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
[**Share...