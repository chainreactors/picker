---
title: Highly Critical Drupal Core Flaw Exposes PostgreSQL Sites to RCE Attacks
url: https://thehackernews.com/2026/05/highly-critical-drupal-core-flaw.html
source: The Hacker News
date: 2026-05-21
fetch_date: 2026-05-22T06:08:40.592366
---

# Highly Critical Drupal Core Flaw Exposes PostgreSQL Sites to RCE Attacks

#1 Trusted Cybersecurity News Platform

Followed by 5.70+ million[**](https://twitter.com/thehackersnews)
[**](https://www.linkedin.com/company/thehackernews/)
[**](https://www.facebook.com/thehackernews)

[![The Hacker News Logo](data:image/png;base64...)](/)

**

**

[** Get the Latest News](#email-outer)

* [Home](/)
* [Newsletter](#email-outer)
* [Webinars](/p/upcoming-hacker-news-webinars.html)

* [Home](/)
* [Threat Intelligence](/search/label/Threat%20Intelligence)
* [Vulnerabilities](/search/label/Vulnerability)
* [Cyber Attacks](/search/label/Cyber%20Attack)
* [Webinars](/p/upcoming-hacker-news-webinars.html)
* [Expert Insights](https://thehackernews.com/expert-insights/)
* [Awards](https://awards.thehackernews.com/)

**

**

**

Resources

* [Webinars](/p/upcoming-hacker-news-webinars.html)
* [Awards](https://awards.thehackernews.com/)
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

[![cybersecurity](https://blogger.googleusercontent.com/img/b/R29vZ2xl/AVvXsEhyqUz0-ifa8jE9rCzud3wzxmhcuzTp1VOWFEvGMoZXDYfaB_4459fPyvyQw7wvAnzjzDL09PkyJM83QGheO69fC3esg1WA7WnJ89i_t_q3K8DxYmgV__QujU8RWRnCK4MpbKqu8nwuMFfLaiRVHy_ov7IZ16hoKI3rIu-5BcISmqXPjlQU7N0sa4lWI-n-/s728-e100/wiz-d.png)](https://thehackernews.uk/wiz-ai-state-d)

# [Highly Critical Drupal Core Flaw Exposes PostgreSQL Sites to RCE Attacks](https://thehackernews.com/2026/05/highly-critical-drupal-core-flaw.html)

**Ravie Lakshmanan**May 21, 2026Web Security / Vulnerability

[![](data:image/png;base64...)](https://blogger.googleusercontent.com/img/b/R29vZ2xl/AVvXsEhyhKX1WKEWbBPd4sElCP9BB26eorxZX1Lo25Mcu-A5bfBUuWT63SQ-Hyycv1YPSlvVeZPfLSEbb8mQnuPvf0KEDm8mYTtCLoYZuMG6A8maidLefE12_3Plum0keZ-mbAS4dGN-x7Oj0NWOmoeqp6_PEK0fqpnZwz8ZFV-NhyFl78WS4Nck76yAbfgWRpK7/s1700-e365/drupal-flaw.jpg)

Drupal has released security updates for a "highly critical" security vulnerability in Drupal Core that could be exploited by attackers to achieve remote code execution, privilege escalation, or information disclosure.

The vulnerability, now tracked as [**CVE-2026-9082**](https://www.cve.org/CVERecord?id=CVE-2026-9082), carries a CVSS score of 6.5 out of 10.0, per CVE.org. Drupal said the vulnerability resides in a database abstraction API that is used in Drupal Core to validate queries and ensure they are sanitized against SQL injection attacks.

"A vulnerability in this API allows an attacker to send specially crafted requests, resulting in arbitrary SQL injection for sites using PostgreSQL databases," it [said](https://www.drupal.org/sa-core-2026-004). "This can lead to information disclosure, and in some cases privilege escalation, remote code execution, or other attacks."

Drupal noted the security flaw can be exploited by anonymous users, and impacts only sites that use PostgreSQL. The following versions address the issue -

* Drupal 11.3.10
* Drupal 11.2.12
* Drupal 11.1.10
* Drupal 10.6.9
* Drupal 10.5.10
* Drupal 10.4.10

[![Cybersecurity](data:image/png;base64...)](https://thehackernews.uk/threatlabz-vpn-risk-2026-d)

Drupal 7 isn't affected. The releases for supported branches (versions 11.3, 11.2, 10.6, and 10.5) include upstream security updates for Symfony and Twig, making it essential that the latest versions are installed.

As previously [disclosed](https://thehackernews.com/2026/05/drupal-to-release-urgent-core-security.html) by Drupal, manual patches have also been released for Drupal versions 9 and 8, which have reached end-of-life -

* Drupal 9.5
* Drupal 8.9

"Drupal 11.1.x, Drupal 11.0.x, Drupal 10.4.x, and below are end-of-life and do not receive security coverage," Drupal said. "Drupal 8 and Drupal 9 have both reached end-of-life.

"Due to this issue's severity, the unsupported releases and patches for unsupported versions are provided as a best effort. Those unsupported versions will still have other, previously disclosed security vulnerabilities."

### Update

Searchlight Cyber has released two working proof-of-concept (PoC) code for CVE-2026-9082, stating the vulnerability can be exploited by anonymous users on any deployment that backs Drupal with PostgreSQL.

"Both are gated on PostgreSQL being the database backend, so MySQL and SQLite installs are not exploitable through these paths," researchers Patrik Grobshäuser, Kevin Gervot, and Tomais Williamson [said](https://slcyber.io/research-center/keys-to-the-kingdom-anonymous-sql-injection-in-drupal-core-cve-2026-9082/). "The upgrade is still worth picking up on those installs for the bundled Symfony and Twig advisories that the same Drupal release carries."

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

[cybersecurity](https://thehackernews.com/search/label/cybersecurity), [Drupal](https://thehackernews.com/search/label/Drupal), [PostgreSQL](https://thehackernews.com/search/label/PostgreSQL), [privilege escalation](https://thehackernews.com/search/label/privilege%20escalation), [remote code execution](https://thehackernews.com/search/label/remote%20code%20execution), [Symfony](https://thehackernews.com/search/label/Symfony), [Vulnerability](https://thehackernews.com/search/label/Vulnerability)

⚡ Top Stories This Week

[![Ollama Out-of-Bounds Read Vulnerability Allows Remote Process Memory Leak](data:image/svg+xml;base64... "Ollama Out-of-Bounds Read Vulnerability Allows Remote Process Memory Leak")

Ollama Out-of-Bounds Read Vulnerability Allows Remote Process Memory Leak](https://thehackernews.com/2026/05/ollama-out-of-bounds-read-vulnerability.html)

[![Four OpenClaw Flaws Enable Data Theft, Privilege Escalation, and Persistence](data:image/svg+xml;base64... "Four OpenClaw Flaws Enable Data Theft, Privilege Escalation, and Persistence")

Four OpenClaw Flaws Enable Data Theft, Privilege Escalation, and Persistence](https://thehackernews.com/2026/05/four-openclaw-flaws-enable-data-theft.html)

[![On-Prem Microsoft Exchange Server CVE-2026-42897 Exploited via Crafted Email](data:image/svg+xml;base64... "On-Prem Microsoft Exchange Server CVE-2026-42897 Exploited via Crafted Email")

On-Prem Microsoft Exchange Server CVE-2026-42897 Exploited via Crafted Email](https://thehackernews.com/2026/05/on-prem-microsoft-exchange-server-cve.html)

[![Cisco Catalyst SD-WAN Controller Auth Bypass Actively Exploited to Gain Admin Access](data:image/svg+xml;base64... "Cisco Catalyst SD-WAN Controller Auth Bypass Actively Exploited to Gain Admin Access")

Cisco Catalyst SD-WAN Controller Auth Bypass Actively Exploited to Gain Admin Acc...