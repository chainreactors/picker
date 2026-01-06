---
title: Kimwolf Android Botnet Infects Over 2 Million Devices via Exposed ADB and Proxy Networks
url: https://thehackernews.com/2026/01/kimwolf-android-botnet-infects-over-2.html
source: The Hacker News
date: 2026-01-05
fetch_date: 2026-01-06T03:28:09.414782
---

# Kimwolf Android Botnet Infects Over 2 Million Devices via Exposed ADB and Proxy Networks

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

[![Salesforce Security Handbook](https://blogger.googleusercontent.com/img/b/R29vZ2xl/AVvXsEhlCcy_j509wX0FKMRQX-zVzeBNtSIDsH6oDFlljaAeQRz65xSx8g9jicghxtpvDC8yI10jCv1TPEcyPvfoCKOby_0ZjsnNc-3wZG5YeA8sZQBCbZxhzd00jR2ZG8rZr-vp3WLrbXaMVbsVrDwBEeBWBbNSSwFjeuNzhrVOigDqTM7VWfSUJqBwEoYALS58/s728-e100/z-header-d.png)](https://thehackernews.uk/modern-security-shift-d)

# [Kimwolf Android Botnet Infects Over 2 Million Devices via Exposed ADB and Proxy Networks](https://thehackernews.com/2026/01/kimwolf-android-botnet-infects-over-2.html)

**Jan 05, 2026**Ravie LakshmananIoT Security / Mobile Security

[![](data:image/png;base64...)](https://blogger.googleusercontent.com/img/b/R29vZ2xl/AVvXsEgaeV0itvv125PlLqvGK97v34m6fdEcSIwgagUCSvL0Z2hcuBWhc-Va5zUjeF3_CgbFojPUcu-Sx2byaI00B67aw49WjKuTDH7zrW7f2Z3lbAt4HLkfA1-k2Vo2sGbrOO9XGCGGjCYQKfdCiUee_aL_UwgcFfxM2jZJxQQkFAtF9P2_raILtD7Orm01ixpE/s790-rw-e365/android-malware.jpg)

The botnet known as **Kimwolf** has infected more than 2 million Android devices by tunneling through residential proxy networks, according to findings from Synthient.

"Key actors involved in the Kimwolf botnet are observed monetizing the botnet through app installs, selling residential proxy bandwidth, and selling its DDoS functionality," the company [said](https://synthient.com/blog/a-broken-system-fueling-botnets) in an analysis published last week.

Kimwolf was [first publicly documented](https://thehackernews.com/2025/12/kimwolf-botnet-hijacks-18-million.html) by QiAnXin XLab last month, while documenting its connections to another botnet known as AISURU. Active since at least August 2025, Kimwolf is assessed to be an Android variant of AISURU. There is growing evidence to suggest that the botnet is actually behind a series of [record-setting DDoS attacks](https://thehackernews.com/2025/12/record-297-tbps-ddos-attack-linked-to.html) late last year.

The malware turns infected systems into conduits for relaying malicious traffic and orchestrating distributed denial-of-service (DDoS) attacks at scale. The vast majority of the infections are concentrated in Vietnam, Brazil, India, and Saudi Arabia, with Synthient observing approximately 12 million unique IP addresses per week.

[![Cybersecurity](data:image/png;base64...)](https://thehackernews.uk/zero-trust-summit-d)

Attacks distributing the botnet have been primarily found to target Android devices running an exposed Android Debug Bridge (ADB) service using a scanning infrastructure that uses residential proxies to install the malware. No less than 67% of the devices connected to the botnet are unauthenticated and have ADB enabled by default.

It's suspected that these devices come pre-infected with software development kits (SDKs) from proxy providers so as to surreptitiously enlist them in the botnet. The [top compromised devices](https://github.com/synthient/public-research/tree/main/2026/01/kimwolf) include unofficial Android-based smart TVs and set-top boxes.

[![](data:image/png;base64...)](https://blogger.googleusercontent.com/img/b/R29vZ2xl/AVvXsEjgKx-0VorYBO0U-_Curxm5rj7ItDug6hkJW5C1CFb8c5mn6kaPlypWNJLi-ZXKTUToRjsMW0SQGxtQrkIDlNX_PVzUvuX3sGcMsXb4YYwB4xagh6QxjILR1rMgvP2d2xuZjNzNfBYlawNni0Nssd_wduQmljfnb3ManB5pAJKrqnzRzG3EhZDyYvyp3gd2/s790-rw-e365/kim.png)

As recently as December 2025, Kimwolf infections have leveraged proxy IP addresses offered for rent by China-based IPIDEA, which implemented a security patch on December 27 to block access to local network devices and various sensitive ports. IPIDEA [describes](https://www.ipidea.io) itself as the "world's leading provider of IP proxy" with more than 6.1 million daily updated IP addresses and 69,000 daily new IP addresses.

In other words, the modus operandi is to leverage IPIDEA's proxy network and other proxy providers, and then tunnel through the local networks of systems running the proxy software to drop the malware. The main payload listens on port 40860 and connects to 85.234.91[.]247:1337 to receive further commands.

[![](data:image/png;base64...)](https://blogger.googleusercontent.com/img/b/R29vZ2xl/AVvXsEhMxNXYHXGOYhnMA-gzjTP8TNfjMR6Zg4TQJzTYSYw1S8Asu7dujZa94TBPYBsQwMrXVzV14GgQvn9wBGGrU-ShnLact_KpIRCjK96NgwSBkrUycVr02t7wrpMP-er3eoGZWilaMtzMyXk0De4CYryzoKn9L9TaalQeDNkhgmZIU1xZm9j_DhHx38JJGsZF/s790-rw-e365/android.png)

"The scale of this vulnerability was unprecedented, exposing millions of devices to attacks," Synthient said.

Furthermore, the attacks infect the devices with a bandwidth monetization service known as Plainproxies Byteconnect SDK, indicating broader attempts at monetization. The SDK uses 119 relay servers that receive proxy tasks from a command-and-control server, which are then executed by the compromised device.

[![Cybersecurity](data:image/png;base64...)](https://thehackernews.uk/attack-surface-insight-d)

Synthient said it detected the infrastructure being used to conduct credential-stuffing attacks targeting IMAP servers and popular online websites.

"Kimwolf's monetization strategy became apparent early on through its aggressive sale of residential proxies," the company said. "By offering proxies as low as 0.20 cents per GB or $1.4K a month for unlimited bandwidth, it would gain early adoption by several proxy providers."

"The discovery of pre-infected TV boxes and the monetization of these bots through secondary SDKs like Byteconnect indicates a deepening relationship between threat actors and commercial proxy providers."

To counter the risk, proxy providers are recommended to block requests to [RFC 1918](https://www.rfc-editor.org/rfc/rfc1918) addresses, which are [private IP address ranges](https://en.wikipedia.org/wiki/Private_network) defined for use in private networks. Organizations are advised to lock down devices running unauthenticated ADB shells to prevent unauthorized access.

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
[**Share on Linke...