---
title: Threat Prevention & Detection in SaaS Environments - 101
url: https://thehackernews.com/2024/07/threat-prevention-detection-in-saas.html
source: The Hacker News
date: 2024-07-17
fetch_date: 2025-10-06T17:46:50.784068
---

# Threat Prevention & Detection in SaaS Environments - 101

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

# [Threat Prevention & Detection in SaaS Environments - 101](https://thehackernews.com/2024/07/threat-prevention-detection-in-saas.html)

**Jul 16, 2024**The Hacker NewsSaaS Security / Identity Management

[![Threat Prevention](data:image/png;base64... "Threat Prevention")](https://blogger.googleusercontent.com/img/b/R29vZ2xl/AVvXsEjkXKL32iLEPc0uIbAtrupoAR9xhX0_rpFkou0ZbUVs61Epj8UAq8PtZRW0Is_joyguVin0J5YsLkz8wUwdJ8k5GnRZ7odKea3cXPihf7SZgbkp8-8sc2_oLZtUggcEVKG8z46inwCumNCbxjE7AIhRWivkcHmMDj_arbb1pR4KOHvTzHAlacgxUyDmOs8/s790-rw-e365/adaptive.png)

Identity-based threats on SaaS applications are a growing concern among security professionals, although few have the capabilities to detect and respond to them.

According to the US Cybersecurity and Infrastructure Security Agency (CISA), [90% of all cyberattacks](https://www.cisa.gov/stopransomware/general-information#:~:text=Fend%20Off%20Phishing%20%3A%20Learn%20how,to%20better%20recognize%20phishing%20emails.) begin with phishing, an identity-based threat. Throw in attacks that use stolen credentials, over-provisioned accounts, and insider threats, and it becomes quite clear that identity is a primary attack vector.

To make matters worse, it's not just human accounts that are being targeted. Threat actors are also hijacking non-human identities, including service accounts and OAuth authorizations, and riding them deep into SaaS applications.

When threat actors get through the initial defenses, having a robust Identity Threat Detection and Response (ITDR) system in place as an integral part of Identity Security can prevent massive breaches. Last month's [Snowflake](https://www.adaptive-shield.com/blog/breach-debrief-series-snowflake-mfa-meltdown-creates-data-leak-blizzard/?utm_source=thehackernews&utm_medium=sponsored_content&utm_campaign=thn_itdr-identityfabric_1) breach is a perfect example. Threat actors took advantage of single-factor authentication to access the account. Once inside, the company lacked any meaningful threat detection capability, which enabled the threat actors to exfiltrate over 560 million customer records.

## How ITDR Works

[ITDR](https://www.adaptive-shield.com/academy/identity-threat-detection-and-response-itdr/?utm_source=thehackernews&utm_medium=sponsored_content&utm_campaign=thn_itdr-identityfabric_2) combines several elements to detect SaaS threats. It monitors events from across the SaaS stack, and uses login information, device data, and user behavior to identify behavioral anomalies that indicate a threat. Each anomaly is considered an indicator of compromise (IOC), and when those IOCs reach a predefined threshold, the ITDR triggers an alert.

For example, if an admin downloads an unusual amount of data, ITDR would consider that to be an IOC. However, if the downloading takes place in the middle of the night or is on an unusual computer, the combination of those IOCs may rise to be considered a threat.

Similarly, if a user logs in from a suspicious ASN following brute-force login attempts, the ITDR classifies the login as a threat, which triggers an incident response. By using a rich data set from multiple applications, the ITDR can detect threats based on data from different applications. If a user is logged into one application from New York and a second application from Paris at the same time, it might appear as normal behavior if the ITDR was limited to reviewing event logs for a single app. The power of SaaS ITDR comes from monitoring data from across the SaaS stack.

In a recent breach detected by Adaptive Shield, threat actors infiltrated an HR payroll system and changed the account numbers for several employees' bank accounts. Fortunately, the ITDR engines detected the anomalous actions, and the account data was corrected before any funds were transferred to the threat actors.

## Reducing Identity-Based Risks

There are a number of steps organizations should take to reduce their risk of identity-based threats and strengthen their identity fabric.

Multi-factor authentication (MFA) and single sign-on (SSO) are critical in these efforts. Permission trimming, adhering to the principle of least privilege (PoLP), and role-based access control (RBAC) also limit user access and reduce the attack surface.

Unfortunately, many identity management tools are underutilized. Organizations turn off MFA, and most SaaS applications require admins to have local login capabilities in case the SSO goes down.

Here are some proactive identity management measures to mitigate the risk of identity-based breaches:

### Classify Your Accounts

High-risk accounts generally fall into several categories. To create strong identity governance and management, security teams should start by classifying the different user types. These may be former employees' accounts, high-privilege accounts, dormant accounts, non-human accounts, or external accounts.

### 1. Deprovision Former Employees and Deactivate Dormant User Accounts

Active accounts of former employees can lead to significant risk for organizations. Many SaaS administrators assume that once an employee is offboarded from the Identity Provider (IdP), their access is automatically removed from company SaaS applications.

While that may be true for SaaS applications connected to the IdP, many SaaS apps aren't connected. In those circumstances, administrators and security teams must work together to deprovision former users with local credentials.

Dormant accounts should be identified and deactivated whenever possible. Often, administrators used these accounts to run testing or set up the application. They have high privileges and are shared by multiple users with an easy-to-remember password. These user accounts represent a significant risk to the application and its data.

### 2. Monitor External Users

External accounts must also be monitored. Often given to agencies, partners, or freelancers, the organization has no real control over who is accessing their data. When projects end, these accounts often remain ...