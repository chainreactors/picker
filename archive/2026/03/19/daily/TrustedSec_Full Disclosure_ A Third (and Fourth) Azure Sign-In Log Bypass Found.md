---
title: Full Disclosure: A Third (and Fourth) Azure Sign-In Log Bypass Found
url: https://trustedsec.com/blog/full-disclosure-a-third-and-fourth-azure-sign-in-log-bypass-found
source: TrustedSec
date: 2026-03-19
fetch_date: 2026-03-20T04:08:53.772017
---

# Full Disclosure: A Third (and Fourth) Azure Sign-In Log Bypass Found

[Skip to Main Content](#main)

All Trimarc services are now delivered through TrustedSec!
[Learn more](https://trustedsec.com/about-us/news/trimarc-joins-forces-with-trustedsec-to-strengthen-security-advisory-services)

Close

[TrustedSec](https://trustedsec.com/)

* [Solutions](https://trustedsec.com/solutions)

  ## Solutions

  Our custom solutions are tailored to address the unique challenges of different roles in security.

  [Solutions](https://trustedsec.com/solutions)

  + [01

    For Leadership

    We understand the challenges facing modern executives and develop solutions unique to leaders.](https://trustedsec.com/solutions/for-leadership)
  + [02

    For Operations

    We stay one step ahead to proactively safeguard our clients and partners.](https://trustedsec.com/solutions/for-operations)
  + [03

    For Infrastructure

    From architecture to resiliency and maintainability, we keep your tech aligned to best practices.](https://trustedsec.com/solutions/for-infrastructure)
  + [04

    For Assurance

    Our compliance experts guide partners through regulatory requirements to ensure standards are met.](https://trustedsec.com/solutions/for-assurance)
* [Services](https://trustedsec.com/services)

  ## Services

  From building to testing to hardening, our services support security at every stage.

  [Services](https://trustedsec.com/services)

  + [01

    Design

    Design an exceptional, custom security program alongside our security experts.](https://trustedsec.com/services/design)
  + [02

    Evaluate

    Evaluate your security program with proven assessment methodologies.](https://trustedsec.com/services/evaluate)
  + [03

    Harden

    Harden your security program with the help of our security experts.](https://trustedsec.com/services/harden)
  + [04

    Respond

    Respond to threats to your security program with the help of our security experts.](https://trustedsec.com/services/respond)
* [Research](https://trustedsec.com/research)
* [Blog](https://trustedsec.com/blog)
* [Resources](https://trustedsec.com/resources)
* [About Us](https://trustedsec.com/about-us)

  ## About Us

  Driven by purpose, fueled by experts.

  [About Us](https://trustedsec.com/about-us)

  + [01

    Our Team

    Meet our security experts.](https://trustedsec.com/about-us/our-team)
  + [02

    Our Partners

    Become a TrustedSec partner to help your customers anticipate and prepare for potential attacks.](https://trustedsec.com/about-us/our-partners)
  + [03

    News

    Our team is trusted by local and national media to be the subject matter experts for security news.](https://trustedsec.com/about-us/news)
  + [04

    Events

    See our upcoming webinars, conferences, talks, trainings, and more!](https://trustedsec.com/about-us/events)

Search

Menu

Search Input

Search

* [Contact Us](https://trustedsec.com/contact)
* [Report a breach](https://trustedsec.com/report-a-breach)

* [Solutions](https://trustedsec.com/solutions)
* [Services](https://trustedsec.com/services)
* [Research](https://trustedsec.com/research)
* [Blog](https://trustedsec.com/blog)
* [Resources](https://trustedsec.com/resources)
* [About Us](https://trustedsec.com/about-us)

Search

* [Contact Us](https://trustedsec.com/contact)
* [Report a breach](https://trustedsec.com/report-a-breach)

* [Blog](https://trustedsec.com/blog)
* [Full Disclosure: A Third (and Fourth) Azure Sign-In Log Bypass Found](https://trustedsec.com/blog/full-disclosure-a-third-and-fourth-azure-sign-in-log-bypass-found)

March 19, 2026

# Full Disclosure: A Third (and Fourth) Azure Sign-In Log Bypass Found

Written by
@ nyxgeek

Vulnerability Assessment

![](https://trusted-sec.transforms.svdcdn.com/production/images/Blog-Covers/GraphGoblinAzureLoggingBypass_WebHero.jpg?w=320&h=320&q=90&auto=format&fit=crop&dm=1773775733&s=0c492a492d321a95b997e6417969ec40)

Table of contents

* [Background](#Background)
* [Enter GraphGoblin and Graph\*\*\*\*\*\*](#Enter)
* [Detecting Sign-In Log Bypasses - A Futureproof Solution](#Detecting)
* [Denied by MSRC](#Denied)
* [The Four Bypasses](#Bypasses)
* [Going Forward](#Forward)

Share

* Share URL
* [Share via Email](/cdn-cgi/l/email-protection#99a6eaecfbf3fcfaeda4daf1fcfaf2bcaba9f6ecedbcaba9edf1f0eabcaba9f8ebedf0faf5fcbcaba9ffebf6f4bcaba9cdebeceaedfcfdcafcfabcaba8bff8f4e9a2fbf6fde0a4dfecf5f5bcaba9ddf0eafaf5f6eaecebfcbcaad8bcaba9d8bcaba9cdf1f0ebfdbcaba9bcaba1f8f7fdbcaba9dff6ecebedf1bcaba0bcaba9d8e3ecebfcbcaba9caf0fef7b4d0f7bcaba9d5f6febcaba9dbe0e9f8eaeabcaba9dff6ecf7fdbcaad8bcaba9f1edede9eabcaad8bcabdfbcabdfedebeceaedfcfdeafcfab7faf6f4bcabdffbf5f6febcabdfffecf5f5b4fdf0eafaf5f6eaecebfcb4f8b4edf1f0ebfdb4f8f7fdb4fff6ecebedf1b4f8e3ecebfcb4eaf0fef7b4f0f7b4f5f6feb4fbe0e9f8eaeab4fff6ecf7fd "Share via Email")
* [Share on Facebook](http://www.facebook.com/sharer.php?u=https%3A%2F%2Ftrustedsec.com%2Fblog%2Ffull-disclosure-a-third-and-fourth-azure-sign-in-log-bypass-found "Share on Facebook")
* [Share on X](http://twitter.com/share?text=Full%20Disclosure%3A%20A%20Third%20%28and%20Fourth%29%20Azure%20Sign-In%20Log%20Bypass%20Found%3A%20https%3A%2F%2Ftrustedsec.com%2Fblog%2Ffull-disclosure-a-third-and-fourth-azure-sign-in-log-bypass-found "Share on X")
* [Share on LinkedIn](https://www.linkedin.com/shareArticle?url=https%3A%2F%2Ftrustedsec.com%2Fblog%2Ffull-disclosure-a-third-and-fourth-azure-sign-in-log-bypass-found&mini=true "Share on LinkedIn")

Invisible password sprays. Invisible logins. Full tokens returned.

Nyxgeek here. It's 2026 and I've got two more Azure Entra ID sign-in log bypasses to share with you. Don't get too excited…these bypasses were recently fixed, but I think it's important that people know.

By sending a specially crafted login attempt to the Azure authentication endpoint, it was possible to retrieve valid tokens without the activity appearing in the Entra ID sign-in logs. This is critical logging…logging that administrators across the world rely on to detect intrusions…logging that could be made optional.

Today I will walk you through the third and fourth Azure sign-in log bypasses that I have found in the last three years. I will also look at how sign-in log bypasses can be detected using KQL queries. By knowing about Microsoft's past mistakes, we can try to prepare for their future failures.

## Background

Since 2023, I've uncovered four Azure Entra ID sign-in log bypasses. This means I've found four completely different ways to validate an Azure account's password without it showing up in the Azure Entra ID sign-in logs. While the first two of these merely confirmed whether a password was valid without generating a log, my latest logging bypasses returned fully functioning tokens.

Previously, I had written about ***GraphNinja*** and ***GraphGhost*** -- two logging bypasses where a user could identify valid passwords without generating any 'successful' events in the sign-in logs. Neither were overly complicated. You can find blog posts describing them in detail [here](https://trustedsec.com/blog/full-disclosure-a-look-at-a-recently-patched-microsoft-graph-logging-bypass-graphninja) and [here](https://trustedsec.com/blog/full-disclosure-graphghost-are-you-afraid-of-failed-logins).

| **Name** | **Reported** | **Fixed** | **Description** |
| --- | --- | --- | --- |
| [GraphNinja](https://trustedsec.com/blog/full-disclosure-a-look-at-a-recently-patched-microsoft-graph-logging-bypass-graphninja) | 08/2023 | 05/2024 | Validate password without creating a log by specifying a foreign tenant ID as endpoint |
| [GraphGhost](https://trustedsec.com/blog/full-disclosure-graphghost-are-you-afraid-of-failed-logins) | 12/2024 | 04/2025 | Validate password without creating a successful login event by supplying an invalid value for specific logon parameters, causing overall auth flow to fail after performing credential validation |

*Real quick -- a point of clarification on the names: while I've used Graph- prefix to designate these different bypasses, pe...