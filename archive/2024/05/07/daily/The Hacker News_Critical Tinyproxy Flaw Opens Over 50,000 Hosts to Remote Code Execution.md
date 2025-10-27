---
title: Critical Tinyproxy Flaw Opens Over 50,000 Hosts to Remote Code Execution
url: https://thehackernews.com/2024/05/critical-tinyproxy-flaw-opens-over.html
source: The Hacker News
date: 2024-05-07
fetch_date: 2025-10-06T17:19:52.674432
---

# Critical Tinyproxy Flaw Opens Over 50,000 Hosts to Remote Code Execution

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

# [Critical Tinyproxy Flaw Opens Over 50,000 Hosts to Remote Code Execution](https://thehackernews.com/2024/05/critical-tinyproxy-flaw-opens-over.html)

**May 06, 2024**Ravie LakshmananVulnerability / Server Security

[![](data:image/png;base64...)](https://blogger.googleusercontent.com/img/b/R29vZ2xl/AVvXsEgYwSjTl9gBIYg034Yyyb7jcL7o-V8gRw0CUg64_aYZMRSO-WjStmTCGk-5eQ_LATE7HAsaINjkNaLOzhh_die20Sl95IAqCYwOlUfoLgH44rdEou6dlfCZRsm0U_y6N5CJpOVIkF0jdRzlEA2fLepjrZAPnktNEqkT3hbJl3lxo-zDcgtWV9j46F9lKDF_/s790-rw-e365/hack.jpg)

More than 50% of the 90,310 hosts have been found exposing a [Tinyproxy service](https://tinyproxy.github.io/) on the internet that's vulnerable to a critical unpatched security flaw in the HTTP/HTTPS proxy tool.

The issue, tracked as **[CVE-2023-49606](https://nvd.nist.gov/vuln/detail/CVE-2023-49606)**, carries a CVSS score of 9.8 out of a maximum of 10, per Cisco Talos, which described it as a use-after-free bug impacting versions 1.10.0 and 1.11.1, the latter of which is the latest version.

"A specially crafted HTTP header can trigger reuse of previously freed memory, which leads to memory corruption and could lead to remote code execution," Talos [said](https://talosintelligence.com/vulnerability_reports/TALOS-2023-1889) in an advisory last week. "An attacker needs to make an unauthenticated HTTP request to trigger this vulnerability."

[![DFIR Retainer Services](data:image/png;base64...)](https://thehackernews.uk/cloud-insight-d)

In other words, an unauthenticated threat actor could send a specially crafted [HTTP Connection header](https://developer.mozilla.org/en-US/docs/Web/HTTP/Headers/Connection) to trigger memory corruption that can result in remote code execution.

According to [data](https://censys.com/cve-2023-49606/) shared by attack surface management company Censys, of the 90,310 hosts exposing a Tinyproxy service to the public internet as of May 3, 2024, 52,000 (~57%) of them are running a vulnerable version of Tinyproxy.

A majority of the publicly-accessible hosts are located in the U.S. (32,846), South Korea (18,358), China (7,808), France (5,208), and Germany (3,680).

Talos, which reported the issue to December 22, 2023, has also released a proof-of-concept (PoC) for the flaw, describing how the issue with parsing HTTP Connection connections could be weaponized to trigger a crash and, in some cases, code execution.

The maintainers of Tinyproxy, in a [set of commits](https://github.com/tinyproxy/tinyproxy/commits/master/) made over the weekend, called out Talos for sending the report to a likely "outdated email address," adding they were made aware by a Debian Tinyproxy package maintainer on May 5, 2024.

[![CIS Build Kits](data:image/png;base64...)](https://thehackernews.uk/platform-shield-d)

"No GitHub issue was filed, and nobody mentioned a vulnerability on the mentioned IRC chat," rofl0r [said](https://github.com/tinyproxy/tinyproxy/commit/12a8484265f7b00591293da492bb3c9987001956) in a commit. "If the issue had been reported on Github or IRC, the bug would have been fixed within a day."

### Update: Fix Available

Users are [advised](https://github.com/tinyproxy/tinyproxy/issues/533) to pull the latest master branch from git or manually apply the [aforementioned commit](https://github.com/tinyproxy/tinyproxy/commit/12a8484265f7b00591293da492bb3c9987001956) as a patch on version 1.11.1 until Tinyproxy 1.11.2 is made available. It's also recommended that the Tinyproxy service is not exposed to the public internet.

### Tinyproxy version 1.11.2 now available

Tinyproxy maintainers have officially released [version 1.11.2](https://github.com/tinyproxy/tinyproxy/releases/tag/1.11.2) to fix the critical use-after-free bug that could enable an unauthenticated attacker to achieve remote code execution.

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

[botnet](https://thehackernews.com/search/label/botnet)[Malware](https://thehackernews.com/search/label/Malware)[network security](https://thehackernews.com/search/label/network%20security)[server security](https://thehackernews.com/search/label/server%20security)[Vulnerability](https://thehackernews.com/search/label/Vulnerability)

[![c](data:image/svg+xml;base64...)](https://thehackernews.uk/cloud-defense)

Trending News

[![Stop Alert Chaos: Context Is the Key to Effective Incident Response](data:image/svg+xml;base64... "Stop Alert Chaos: Context Is the Key to Effective Incident Response")

Stop Alert Chaos: Context Is the Key to Effective Incident Response](https://thehackernews.com/2025/09/stop-alert-chaos-context-is-key-to.html)

[![Evolving Enterprise Defense to Secure the Modern AI Supply Chain](data:image/svg+xml;base64... "Evolving Enterprise Defense to Secure the Modern AI Supply Chain")

Evolving Enterprise Defense to Secure the Modern AI Supply Chain](https://thehackernews.com/2025/09/evolving-enterprise-defense-to-secure.html)

[![First Malicious MCP Server Found Stealing Emails in Rogue Postmark-MCP Package](data:image/svg+xml;base64... "First Malicious MCP Server Found Stealing Emails in Rogue Postmark-MCP Package")

First Malicious MCP Server Found Stealing Emails in Rogue Postmark-MCP Package](https://thehackernews.com/2025/09/firs...