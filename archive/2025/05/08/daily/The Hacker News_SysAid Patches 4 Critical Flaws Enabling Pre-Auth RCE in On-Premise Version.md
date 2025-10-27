---
title: SysAid Patches 4 Critical Flaws Enabling Pre-Auth RCE in On-Premise Version
url: https://thehackernews.com/2025/05/sysaid-patches-4-critical-flaws.html
source: The Hacker News
date: 2025-05-08
fetch_date: 2025-10-06T22:35:38.645631
---

# SysAid Patches 4 Critical Flaws Enabling Pre-Auth RCE in On-Premise Version

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

# [SysAid Patches 4 Critical Flaws Enabling Pre-Auth RCE in On-Premise Version](https://thehackernews.com/2025/05/sysaid-patches-4-critical-flaws.html)

**May 07, 2025**Ravie LakshmananVulnerability / IT Service

[![](data:image/png;base64...)](https://blogger.googleusercontent.com/img/b/R29vZ2xl/AVvXsEjCI_OqisCuCY6aOItfHJDrIf1aCYizFIuPMHBP2AZi9hAAYaPP2b5tfdiM5zWrCOglIkh_-aQnli8eipX05yorav_QmwlToCuMC4LzSnjDqKGUFNhb9406uIxBg2lFvP8T-UvzyRfvKXTATPdHTMlBPpivoy1YpGJiQniRQvkBEBfEVfuCZ9z3WbIvuVUd/s790-rw-e365/poc-exploit.jpg)

Cybersecurity researchers have disclosed multiple security flaws in the on-premise version of SysAid IT support software that could be exploited to achieve pre-authenticated remote code execution with elevated privileges.

The vulnerabilities, tracked as CVE-2025-2775, CVE-2025-2776, and CVE-2025-2777, have all been described as XML External Entity ([XXE](https://www.hackerone.com/knowledge-center/xxe-complete-guide-impact-examples-and-prevention)) injections, which occur when an attacker is able to successfully interfere with an application's parsing of XML input.

This, in turn, could permit attackers to inject unsafe XML entities into the web application, allowing them to carry out a Server-Side Request Forgery ([SSRF](https://owasp.org/www-community/attacks/Server_Side_Request_Forgery)) attack and in worst cases, remote code execution.

[![DFIR Retainer Services](data:image/png;base64...)](https://thehackernews.uk/cloud-insight-d)

A description of the three vulnerabilities, [according](https://labs.watchtowr.com/sysowned-your-friendly-rce-support-ticket/) to watchTowr Labs researchers Sina Kheirkhah and Jake Knott, is as follows -

* CVE-2025-2775 and CVE-2025-2776 - A pre-authenticated XXE within the /mdm/checkin endpoint
* CVE-2025-2777 - A pre-authenticated XXE within the /lshw endpoint

watchTowr Labs described the vulnerabilities as trivial to exploit by means of a specially crafted HTTP POST request to the endpoints in question.

[![](data:image/png;base64...)](https://blogger.googleusercontent.com/img/b/R29vZ2xl/AVvXsEicpoaLX8akgrW9fhnrDXzH9RYG6iZ8o8QlNvUVacGDxHxI7vrWqiqgPJcSCov0w9iqdQA2auLLXC9gfFjN6l0s3i5chaQp41v_yZZrLB-uU0umXH525USUSIRTLOrXPwVqvYZFEPXE5cBj1VNgVpIacNGX4IB99REC9JNeH0TWAKn5g8alJXJPnkp5Gnyt/s790-rw-e365/attack.png)

Successful exploitation of the flaws could enable an attacker to retrieve local files containing sensitive information, including SysAid's own "InitAccount.cmd" file, which contains information about the administrator account username and plaintext password created during installation.

Armed with this information, the attacker could then gain full administrative access to SysAid as an administrator-privileged user.

To make matters worse, the XXE flaws could be chained with another operating system command injection vulnerability – discovered by a third-party – to achieve remote code execution. The command injection issue, assigned the CVE identifier [CVE-2024-36394](https://www.cve.org/CVERecord?id=CVE-2024-36394), was fixed in June 2024 after being discovered by CyberArk.

[![CIS Build Kits](data:image/png;base64...)](https://thehackernews.uk/platform-shield-d)

The three new vulnerabilities have been [rectified](https://documentation.sysaid.com/docs/24-40-60) by SysAid with the release of on-premise version 24.4.60 build 16 in early March 2025, while CVE-2024-36394 was patched in version 23.3.38 build 19. A proof-of-concept (PoC) exploit combining the four vulnerabilities has been [made available](https://github.com/watchtowrlabs/watchTowr-vs-SysAid-PreAuth-RCE-Chain).

With security flaws in SysAid (CVE-2023-47246) previously [exploited](https://thehackernews.com/2023/11/zero-day-alert-lace-tempest-exploits.html) by ransomware actors like Cl0p in zero-day attacks, it's imperative that users update their instances to the latest version.

*(The story was updated after publication on July 23, 2025, to reflect the change in the CVE identifier from CVE-2025-2778 to CVE-2024-36394. CVE-2025-2778 has been marked as withdrawn.)*

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

[cybersecurity](https://thehackernews.com/search/label/cybersecurity)[remote code execution](https://thehackernews.com/search/label/remote%20code%20execution)[Security patch](https://thehackernews.com/search/label/Security%20patch)[Server-Side Request Forgery](https://thehackernews.com/search/label/Server-Side%20Request%20Forgery)[Vulnerability](https://thehackernews.com/search/label/Vulnerability)[WatchTowr Labs](https://thehackernews.com/search/label/WatchTowr%20Labs)

[![c](data:image/svg+xml;base64...)](https://thehackernews.uk/cloud-defense)

Trending News

[![Stop Alert Chaos: Context Is the Key to Effective Incident Response](data:image/svg+xml;base64... "Stop Alert Chaos: Context Is the Key to Effective Incident Response")

Stop Alert Chaos: Context Is the Key to Effective Incident Response](https://thehackernews.com/2025/09/stop-alert-chaos-context-is-key-to.html)

[![Evolving Enterprise Defense to Secure the Modern AI Supply Chain](data:image/svg+xml;base64... "Evolving Enterprise Defense to Secure the Modern AI Supply Chain")

Evolving Enterprise Defense to Secure the Modern AI Supply Chain](http...