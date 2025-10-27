---
title: Researchers Reported Critical SQLi and Access Flaws in Zendesk Analytics Service
url: https://thehackernews.com/2022/11/researchers-reported-critical-sqli-and.html
source: The Hacker News
date: 2022-11-16
fetch_date: 2025-10-03T22:56:02.691279
---

# Researchers Reported Critical SQLi and Access Flaws in Zendesk Analytics Service

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

# [Researchers Reported Critical SQLi and Access Flaws in Zendesk Analytics Service](https://thehackernews.com/2022/11/researchers-reported-critical-sqli-and.html)

**Nov 15, 2022**Ravie Lakshmanan

[![Zendesk Analytics Service](data:image/png;base64... "Zendesk Analytics Service")](https://blogger.googleusercontent.com/img/b/R29vZ2xl/AVvXsEi0zoNNeYwMT4kd_1EHiziG4SXKUqOyWHf6vQG78pUo7lYi7FPd6fm-753eaSrL7SgalRHl5vcICGZHWaF1xUb_XbmgRF4daHeMwDVDXSUz1c_V5Z6o49kVHB0595YVXneSpZmiVylbXRGqUXQyNhjI7smyRK80yl1D0e7KQazi-OOWhipz7XTxOAo-/s790-rw-e365/ZenDesk.jpg)

Cybersecurity researchers have disclosed details of now-patched flaws in Zendesk Explore that could have been exploited by an attacker to gain unauthorized access to information from customer accounts that have the feature turned on.

"Before it was patched, the flaw would have allowed threat actors to access conversations, email addresses, tickets, comments, and other information from Zendesk accounts with Explore enabled," Varonis [said](https://www.varonis.com/blog/zendesk-sql-injection-and-access-flaws) in a report shared with The Hacker News.

The cybersecurity firm said there was no evidence to suggest that the issues were actively exploited in real-world attacks. No action is required on the part of the customers.

[![DFIR Retainer Services](data:image/png;base64...)](https://thehackernews.uk/cloud-insight-d)

Zendesk Explore is a [reporting and analytics solution](https://support.zendesk.com/hc/en-us/articles/4408846357018-Zendesk-Explore-resources-for-reporting-and-analytics) that allows organizations to "view and analyze key information about your customers, and your support resources."

[![Zendesk Analytics Service](data:image/png;base64... "Zendesk Analytics Service")](https://blogger.googleusercontent.com/img/b/R29vZ2xl/AVvXsEixlJtfjeXQLaR2WSqRyblGfJ8u4NtswO7FlgCQwL6-EpN_fKqS6MpEML7Kd535e2MNamXHGehZjnQhyp8oX_pakEzOfdafxfQWC2W3gMTQcasTZ8z0-ozdXaq4ZPe-r4w_Acm8zZJH4_2EVLvY7bL2NXtTYEDVb-OYOV-TjGh7X6oAD7-GoBP6E6a2/s790-rw-e365/banner.jpg)

According to the security software company, exploitation of the shortcoming first requires an attacker to register for the [ticketing service](https://developer.zendesk.com/api-reference/ticketing/tickets/tickets/) of its victim's Zendesk account as a new external user, a feature that's likely enabled by default to allow end-users to submit support tickets.

The vulnerability relates to an SQL injection in its GraphQL API that could be abused to exfiltrate all information stored in the database as an admin user, including email addresses, tickets, and conversations with live agents.

[![CIS Build Kits](data:image/png;base64...)](https://thehackernews.uk/platform-shield-d)

A second flaw concerns a logic access issue associated with a query execution API, which was configured to run the queries without checking if the "user" making the call had adequate permission to do so.

"This meant that a newly created end-user could invoke this API, change the query, and steal data from any table in the target Zendesk account's RDS, no SQLi required,"

Varonis said the issues were disclosed to Zendesk on August 30, following which the weaknesses were rectified by the company on September 8, 2022.

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

[Analytics Service](https://thehackernews.com/search/label/Analytics%20Service)[sql injection](https://thehackernews.com/search/label/sql%20injection)[SQLi](https://thehackernews.com/search/label/SQLi)[Zendesk](https://thehackernews.com/search/label/Zendesk)

[![c](data:image/svg+xml;base64...)](https://thehackernews.uk/cloud-defense)

Trending News

[![SolarWinds Releases Hotfix for Critical CVE-2025-26399 Remote Code Execution Flaw](data:image/svg+xml;base64... "SolarWinds Releases Hotfix for Critical CVE-2025-26399 Remote Code Execution Flaw")

SolarWinds Releases Hotfix for Critical CVE-2025-26399 Remote Code Execution Flaw](https://thehackernews.com/2025/09/solarwinds-releases-hotfix-for-critical.html)

[![Microsoft Patches Critical Entra ID Flaw Enabling Global Admin Impersonation Across Tenants](data:image/svg+xml;base64... "Microsoft Patches Critical Entra ID Flaw Enabling Global Admin Impersonation Across Tenants")

Microsoft Patches Critical Entra ID Flaw Enabling Global Admin Impersonation Across Tenants](https://thehackernews.com/2025/09/microsoft-patches-critical-entra-id.html)

[![Hackers Exploit Pandoc CVE-2025-51591 to Target AWS IMDS and Steal EC2 IAM Credentials](data:image/svg+xml;base64... "Hackers Exploit Pandoc CVE-2025-51591 to Target AWS IMDS and Steal EC2 IAM Credentials")

Hackers Exploit Pandoc CVE-2025-51591 to Target AWS IMDS and Steal EC2 IAM Credentials](https://thehackernews.com/2025/09/hackers-exploit-pandoc-cve-2025-51591.html)

[![China-Linked PlugX and Bookworm Malware Attacks Target Asian Telecom and ASEAN Networks](data:image/svg+xml;base64... "China-Linked PlugX and Bookworm Malware Attacks Target Asian Telecom and ASEAN Networks")

China-Linked PlugX and Bookworm Malware Attacks Target Asian Telecom and ASEAN Networks](https://thehackernews.com/2025/09/china-linked-plugx-and-bookworm-malware.html)

[![Fortra GoAnywhere CVSS 10 Flaw Exploited as 0-Day a Week Before Public Di...