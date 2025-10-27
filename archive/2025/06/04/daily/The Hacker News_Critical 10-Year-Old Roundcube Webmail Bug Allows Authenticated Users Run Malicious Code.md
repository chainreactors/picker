---
title: Critical 10-Year-Old Roundcube Webmail Bug Allows Authenticated Users Run Malicious Code
url: https://thehackernews.com/2025/06/critical-10-year-old-roundcube-webmail.html
source: The Hacker News
date: 2025-06-04
fetch_date: 2025-10-06T22:56:41.925712
---

# Critical 10-Year-Old Roundcube Webmail Bug Allows Authenticated Users Run Malicious Code

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

# [Critical 10-Year-Old Roundcube Webmail Bug Allows Authenticated Users Run Malicious Code](https://thehackernews.com/2025/06/critical-10-year-old-roundcube-webmail.html)

**Jun 03, 2025**Ravie LakshmananEmail Security / Vulnerability

[![Roundcube Webmail Bug](data:image/png;base64... "Roundcube Webmail Bug")](https://blogger.googleusercontent.com/img/b/R29vZ2xl/AVvXsEh4TFQSjD1H1lbO9nXKHAg0UI12EJ_X4BG0Pw1kPpTLXzktpbR9kdw-VmtIO5rxRD9KJRCQnLTml-5pXvgdQ7e9YwEXQIJduGXAgDi6egr8ubBzUaVHkRdWQYXQSvVSoccGtsYeB4S1L9nSKCzKySVx-dDz_Gx-b41LsCy5EO6YHCbjUNA5J-ykSWApm5p2/s790-rw-e365/cube.jpg)

Cybersecurity researchers have disclosed details of a critical security flaw in the Roundcube webmail software that has gone unnoticed for a decade and could be exploited to take over susceptible systems and execute arbitrary code.

The vulnerability, tracked as **CVE-2025-49113**, carries a CVSS score of 9.9 out of 10.0. It has been described as a case of post-authenticated remote code execution via PHP object deserialization.

"Roundcube Webmail before 1.5.10 and 1.6.x before 1.6.11 allows remote code execution by authenticated users because the \_from parameter in a URL is not validated in program/actions/settings/upload.php, leading to PHP Object Deserialization," reads the [description](https://nvd.nist.gov/vuln/detail/CVE-2025-49113) of the flaw in the NIST's National Vulnerability Database (NVD).

The shortcoming, which affects all versions of the software before and including 1.6.10, has been [addressed in 1.6.11 and 1.5.10 LTS](https://roundcube.net/news/2025/06/01/security-updates-1.6.11-and-1.5.10). Kirill Firsov, founder and CEO of FearsOff, has been credited with discovering and reporting the flaw.

[![CIS Build Kits](data:image/png;base64...)](https://thehackernews.uk/platform-shield-d)

The Dubai-based cybersecurity company [noted](https://fearsoff.org/research/roundcube) in a brief advisory that it intends to make public additional technical details and a proof-of-concept (PoC) "soon" so as to give users sufficient time to apply the necessary patches.

Previously disclosed security vulnerabilities in Roundcube have been a lucrative target for nation-state threat actors like APT28 and Winter Vivern. Last year, Positive Technologies revealed that unidentified hackers [attempted](https://thehackernews.com/2024/10/hackers-exploit-roundcube-webmail-xss.html) to exploit a Roundcube flaw (CVE-2024-37383) as part of a phishing attack designed to steal user credentials.

Then a couple of weeks ago, ESET [noted](https://thehackernews.com/2025/05/russia-linked-apt28-exploited-mdaemon.html) that APT28 had leveraged cross-site scripting (XSS) vulnerabilities in various webmail servers such as Roundcube, Horde, MDaemon, and Zimbra to harvest confidential data from specific email accounts belonging to governmental entities and defense companies in Eastern Europe.

### Positive Technologies Reproduces CVE-2025-49113

Positive Technologies, in a post published on X, said it was able to reproduce CVE-2025-49113, urging users to update to the latest version of Roundcube as soon as possible.

"This vulnerability allows authenticated users to execute arbitrary commands via PHP object deserialization," the Russian cybersecurity company [added](https://x.com/ptswarm/status/1929940817679962141).

### CVE-2025-49113 PoC Released Amid Exploitation Attempts

FearsOff has [released](https://github.com/fearsoff-org/CVE-2025-49113) technical details of CVE-2025-49113 and a proof-of-concept (PoC) after reports of "active exploitation and evidence of the [exploit being sold](https://x.com/k_firsov/status/1930246402099044789) in underground forums." Describing it as an "email armageddon," the company said the vulnerability affects over 53 Million hosts.

The problem, according to Firsov, is rooted in the fact that starting a session variable name with an exclamation mark causes a session to get corrupted and the "$\_GET['\_from']" parameter used during image uploads for [managing sender identities](https://docs.roundcube.net/doc/help/1.1/en_US/settings/identities.html) in Roundcube lacks as any sanitization, allowing an attacker to inject a malicious payload into the current session.

"This vulnerability is now known, exploitable, and being sold," Firsov [said](https://fearsoff.org/research/roundcube). "Consider monitoring file uploads, session activity, and other indicators tied to this attack vector."

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

[APT28](https://thehackernews.com/search/label/APT28)[cybersecurity](https://thehackernews.com/search/label/cybersecurity)[email security](https://thehackernews.com/search/label/email%20security)[Malware](https://thehackernews.com/search/label/Malware)[PHP](https://thehackernews.com/search/label/PHP)[remote code execution](https://thehackernews.com/search/label/remote%20code%20execution)[Roundcube](https://thehackernews.com/search/label/Roundcube)[Threat Intelligence](https://thehackernews.com/search/label/Threat%20Intelligence)[Vulnerability](https://thehackernews.com/search/label/Vulnerability)[Webmail](https://thehackernews.com/search/label/Webmail)

[![c](data:image/svg+xml;base64...)](https://thehackernews.uk/cloud-def...