---
title: New "LeakyLooker" Flaws in Google Looker Studio Could Enable Cross-Tenant SQL Queries
url: https://thehackernews.com/2026/03/new-leakylooker-flaws-in-google-looker.html
source: The Hacker News
date: 2026-03-10
fetch_date: 2026-03-11T04:05:31.426098
---

# New "LeakyLooker" Flaws in Google Looker Studio Could Enable Cross-Tenant SQL Queries

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

[![Security Service Edge](https://blogger.googleusercontent.com/img/b/R29vZ2xl/AVvXsEguiZ85S7494GyqhFt9uP48C8ggEnb3bp9Qmsdv4LOYjNWfa98MKx17Dk7o1nJrEV3ai3edIGIgwt6oO5iJMmYLcyu6PojcvJnO4IfLhVK2dzGKFyEroFjKQhnp2hd5Cc6G4CynJRfb55aclnGwj7rse9jMncn_vu_tFqQZtHZH3Sb5dMXwRKN-kSVYUMzD/s1700-e365/ai-d.png)](https://thehackernews.uk/wiz-ai-security-d)

# [New "LeakyLooker" Flaws in Google Looker Studio Could Enable Cross-Tenant SQL Queries](https://thehackernews.com/2026/03/new-leakylooker-flaws-in-google-looker.html)

**Ravie Lakshmanan**Mar 10, 2026Database Security / Vulnerability

[![](data:image/png;base64...)](https://blogger.googleusercontent.com/img/b/R29vZ2xl/AVvXsEi2sHbLX0XUqPu9yr7S5g-qYzWmRx4m_RGqFl4wqfd87nzpCH4RbDGMzdvRIzXLHfGUFtESqDSbXjksDf73X6VqM9kdl0BsgoRGr6luzPooCoRR5oAzQzxyCPU7HMK_JrXS__l0h22_J0JNkveq_OA87M4MvaASKETRpM9lj57aLzm7znLU4OWz6Gs0ZmwT/s1700-e365/looker.jpg)

Cybersecurity researchers have disclosed nine cross-tenant vulnerabilities in Google Looker Studio that could have permitted attackers to run arbitrary SQL queries on victims' databases and exfiltrate sensitive data within organizations' Google Cloud environments.

The shortcomings have been collectively named **LeakyLooker** by Tenable. There is no evidence that the vulnerabilities were exploited in the wild. Following responsible disclosure in June 2025, the issues have been addressed by Google.

[![Cybersecurity](data:image/png;base64...)](https://thehackernews.uk/not-fast-enough-d)

The list of security flaws is as follows -

* [Cross Tenant Unauthorized Access - Zero-Click SQL Injection on Database Connectors](https://www.tenable.com/security/research/tra-2025-28)
* [Cross Tenant Unauthorized Access - Zero-Click SQL Injection Through Stored Credentials](https://www.tenable.com/security/research/tra-2025-29)
* [Cross Tenant SQL Injection on BigQuery Through Native Functions](https://www.tenable.com/security/research/tra-2025-27)
* [Cross-Tenant Data Sources Leak With Hyperlinks](https://www.tenable.com/security/research/tra-2025-40)
* [Cross Tenant SQL injection on Spanner and BigQuery Through Custom Queries on a Victim’s Data Source](https://www.tenable.com/security/research/tra-2025-38)
* [Cross Tenant SQL Injection on BigQuery and Spanner Through the Linking API](https://www.tenable.com/security/research/tra-2025-37)
* [Cross-Tenant Data Sources Leak With Image Rendering](https://www.tenable.com/security/research/tra-2025-30)
* [Cross-Tenant XS Leak on Arbitrary Data Sources With Frame Counting and Timing Oracles](https://www.tenable.com/security/research/tra-2025-31)
* [Cross Tenant Denial of Wallet Through BigQuery](https://www.tenable.com/security/research/tra-2025-41)

"The vulnerabilities broke fundamental design assumptions, revealed a new attack class, and could have allowed attackers to exfiltrate, insert, and delete data in victims' services and Google Cloud environment," security researcher Liv Matan [said](https://www.tenable.com/blog/leakylooker-google-cloud-looker-studio-vulnerabilities) in a report shared with The Hacker News.

"These vulnerabilities exposed sensitive data across Google Cloud Platform (GCP) environments, potentially affecting any organization using Google Sheets, BigQuery, Spanner, PostgreSQL, MySQL, Cloud Storage, and almost any other Looker Studio data connector."

Successful exploitation of the cross-tenant flaws could enable threat actors to gain access to entire datasets and projects across different cloud tenants.

Attackers could scan for public Looker Studio reports or obtain access to private ones that use these connectors (e.g., BigQuery) and seize control of the databases, allowing them to run arbitrary SQL queries across the owner's entire GCP project.

[![Cybersecurity](data:image/png;base64...)](https://thehackernews.uk/cyber-comm-guide-d)

Alternatively, a victim creates a report as public or shares it with a specific recipient, and uses a JDBC-connected data source such as PostgreSQL. In this scenario, the attacker can take advantage of a logic flaw in the copy report feature that makes it possible to clone reports while retaining the original owner's credentials, enabling them to delete or modify tables.

Another high-impact path detailed by the cybersecurity company involved one-click data exfiltration, where sharing a specially crafted report forces a victim's browser to execute malicious code that contacts an attacker-controlled project to reconstruct entire databases from logs.

"The vulnerabilities broke the fundamental promise that a 'Viewer' should never be able to control the data they are viewing," Matan said, adding they "could have let attackers exfiltrate or modify data across Google services like BigQuery and Google Sheets."

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

[BigQuery](https://thehackernews.com/search/label/BigQuery), [Cloud security](https://thehackernews.com/search/label/Cloud%20security), [cybersecurity](https://thehackernews.com/search/label/cybersecurity), [data exfiltration](https://thehackernews.com/search/label/data%20exfiltration), [database security](https://thehackernews.com/search/label/database%20security), [Google Cloud](https://thehackernews.com/search/label/Google%20Cloud), [sql injection](https://thehackernews.com/search/label/sql%20injection), [Vulnerability](https://thehackernews.com/search/label/Vulnerability)

Trending News

[![ClawJacked Flaw Lets Malicious Sites Hijack Local OpenClaw AI Agents via WebSocket](data:image/svg+xml;base64... "ClawJac...