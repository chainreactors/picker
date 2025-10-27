---
title: GitHub Token Leak Exposes Python's Core Repositories to Potential Attacks
url: https://thehackernews.com/2024/07/github-token-leak-exposes-pythons-core.html
source: The Hacker News
date: 2024-07-16
fetch_date: 2025-10-06T17:52:16.551449
---

# GitHub Token Leak Exposes Python's Core Repositories to Potential Attacks

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

# [GitHub Token Leak Exposes Python's Core Repositories to Potential Attacks](https://thehackernews.com/2024/07/github-token-leak-exposes-pythons-core.html)

**Jul 15, 2024**Ravie LakshmananSupply Chain Attack / Cyber Threat

[![GitHub Token Leak](data:image/png;base64... "GitHub Token Leak")](https://blogger.googleusercontent.com/img/b/R29vZ2xl/AVvXsEhCNOw_vgzN7tDBG29nHUqWtnFHGrFRi0mitSVTQPyQGvKug2tCAAKCyuTlY-VzL_2Lom2yv4ABAPpf2Cdm6tBucws7V1Cbscn370daqjr3qXadHJoqKtASP5cC8WrLlzMkLdRruh-Lgzm3LOPBqMY8N2Zgxm2LvLbrQXQ-groZY3OhY_3cF8heDIjLUJxL/s790-rw-e365/hack.png)

Cybersecurity researchers said they discovered an accidentally leaked GitHub token that could have granted elevated access to the GitHub repositories of the Python language, Python Package Index (PyPI), and the Python Software Foundation (PSF).

JFrog, which found the GitHub Personal Access Token, said the secret was leaked in a public Docker container hosted on Docker Hub.

"This case was exceptional because it is difficult to overestimate the potential consequences if it had fallen into the wrong hands – one could supposedly inject malicious code into PyPI packages (imagine replacing all Python packages with malicious ones), and even to the Python language itself," the software supply chain security company [said](https://jfrog.com/blog/leaked-pypi-secret-token-revealed-in-binary-preventing-suppy-chain-attack/).

An attacker could have hypothetically weaponized their admin access to orchestrate a large-scale supply chain attack by poisoning the source code associated with the core of the Python programming language, or the PyPI package manager.

[![DFIR Retainer Services](data:image/png;base64...)](https://thehackernews.uk/cloud-insight-d)

JFrog noted that the authentication token was found inside a Docker container, in a compiled Python file ("build.cpython-311.pyc") that was inadvertently not cleaned up.

Following responsible disclosure on June 28, 2024, the token – which was issued for the GitHub account linked to PyPI Admin Ee Durbin – was immediately revoked. There is no evidence that the secret was exploited in the wild.

PyPI said the token was issued sometime prior to March 3, 2023, and that the exact date is unknown due to the fact that security logs are unavailable beyond 90 days.

[![](data:image/png;base64...)](https://blogger.googleusercontent.com/img/b/R29vZ2xl/AVvXsEgrT588BPscaDSE24EhpSRxspWxAvuU2dctgkAL613OoxySYZ9bY7MLGl-7uRyPbSiQSqEXw5gfTLYWPN6fGh5wBzwS0WWwhfo2F4KUzVK-3Imrax90xeGV7lFVOaf0RXDbrCyaBBEGINHG_lrD_nAFagRi2ZusKskgNmLbKcsoiY0474RIo6HdpRRysSuI/s790-rw-e365/python.png)

"While developing cabotage-app locally, working on the build portion of the codebase, I was consistently running into GitHub API rate limits," Durbin [explained](https://blog.pypi.org/posts/2024-07-08-incident-report-leaked-admin-personal-access-token/).

"These rate limits apply to anonymous access. While in production the system is configured as a GitHub App, I modified my local files to include my own access token in an act of laziness, rather than configure a localhost GitHub App. These changes were never intended to be pushed remotely."

The disclosure comes as Checkmarx uncovered a series of malicious packages on PyPI that are designed to exfiltrate sensitive information to a Telegram bot without victims' consent or knowledge.

[![CIS Build Kits](data:image/png;base64...)](https://thehackernews.uk/platform-shield-d)

The packages in question – testbrojct2, proxyfullscraper, proxyalhttp, and proxyfullscrapers – work by scanning the compromised system for files matching extensions like .py, .php, .zip, .png, .jpg, and .jpeg.

"The Telegram bot is linked to multiple cybercriminal operations based in Iraq," Checkmarx researcher Yehuda Gelb [said](https://checkmarx.com/blog/malicious-python-packages-reveal-extensive-cybercriminal-operation-based-in-iraq/), noting the bot's message history dates all the way back to 2022.

"The bot functions also as an underground marketplace offering social media manipulation services. It has been linked to financial theft and exploits victims by exfiltrating their data."

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

[Cyber Threat](https://thehackernews.com/search/label/Cyber%20Threat)[cybersecurity](https://thehackernews.com/search/label/cybersecurity)[data exfiltration](https://thehackernews.com/search/label/data%20exfiltration)[Docker](https://thehackernews.com/search/label/Docker)[GitHub](https://thehackernews.com/search/label/GitHub)[Open Source](https://thehackernews.com/search/label/Open%20Source)[Python](https://thehackernews.com/search/label/Python)[software security](https://thehackernews.com/search/label/software%20security)[supply chain attack](https://thehackernews.com/search/label/supply%20chain%20attack)[Telegram Bot](https://thehackernews.com/search/label/Telegram%20Bot)

[![c](data:image/svg+xml;base64...)](https://thehackernews.uk/cloud-defense)

Trending News

[![Stop Alert Chaos: Context Is the Key to Effective Incident Response](data:image/svg+xml;base64... "Stop Alert Chaos: Context Is the Key to Effective Incident Response")

Stop Alert Chaos: Context Is the Key to Effective Incident Response](https://thehackernews.com/2...