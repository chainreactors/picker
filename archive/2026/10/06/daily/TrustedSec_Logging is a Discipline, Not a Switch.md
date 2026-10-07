---
title: Logging is a Discipline, Not a Switch
url: https://trustedsec.com/blog/logging-is-a-discipline-not-a-switch
source: TrustedSec
date: 2026-10-06
fetch_date: 2026-10-07T07:55:20.747163
---

# Logging is a Discipline, Not a Switch

[Skip to Main Content](#main)

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
* [Logging is a Discipline, Not a Switch](https://trustedsec.com/blog/logging-is-a-discipline-not-a-switch)

October 06, 2026

# Logging is a Discipline, Not a Switch

Written by
Brandon Colley

Active Directory Security Review

![](https://trusted-sec.transforms.svdcdn.com/production/images/Blog-Covers/LoggingIsADiscipline_WebHero.jpg?w=320&h=320&q=90&auto=format&fit=crop&dm=1791201925&s=456a68b7c3f86f5a5affc3171d4a7528)

Table of contents

* [Step One: Log Behavior and Size](#Log)
* [Step Two: Advanced Audit Policy](#Policy )
* [Step Three: Know What You are Trying to Detect](#Detect )
* [Step Four: Find the Gaps, Then Rehearse](#Rehearse)
* [Conclusion: Achieve Discipline](#Conclusion)

Share

* Share URL
* [Share via Email](/cdn-cgi/l/email-protection#5f602c2a3d353a3c2b621c373a3c347a6d6f302a2b7a6d6f2b37362c7a6d6f3e2d2b363c333a7a6d6f392d30327a6d6f0b2d2a2c2b3a3b0c3a3c7a6d6e793e322f643d303b2662133038383631387a6d6f362c7a6d6f3e7a6d6f1b362c3c362f3336313a7a6d1c7a6d6f11302b7a6d6f3e7a6d6f0c28362b3c377a6c1e7a6d6f372b2b2f2c7a6c1e7a6d197a6d192b2d2a2c2b3a3b2c3a3c713c30327a6d193d3330387a6d193330383836313872362c723e723b362c3c362f3336313a7231302b723e722c28362b3c37 "Share via Email")
* [Share on Facebook](https://www.facebook.com/sharer.php?u=https%3A%2F%2Ftrustedsec.com%2Fblog%2Flogging-is-a-discipline-not-a-switch "Share on Facebook")
* [Share on X](https://twitter.com/share?text=Logging%20is%20a%20Discipline%2C%20Not%20a%20Switch%3A%20https%3A%2F%2Ftrustedsec.com%2Fblog%2Flogging-is-a-discipline-not-a-switch "Share on X")
* [Share on LinkedIn](https://www.linkedin.com/shareArticle?url=https%3A%2F%2Ftrustedsec.com%2Fblog%2Flogging-is-a-discipline-not-a-switch&mini=true "Share on LinkedIn")

### Practical Guidance on Logging, Auditing, Monitoring, and Alerting in Active Directory

Across the Active Directory (AD) assessments we run, logging and auditing gaps come up again and again. This is  usually because logging is treated as a switch to flip rather than something to tune and maintain. Logging crosses multiple teams and nobody owns the question of whether the data being collected would actually catch an intrusion.

This blog walks through a successful logging program in the order it should be built.

1. Configure the logs so they can hold what you collect.
2. Configure what gets collected.
3. Define what you are trying to detect.
4. Test whether you can detect it.

![](https://trusted-sec.transforms.svdcdn.com/production/images/Blog-assets/LoggingDiscipline_Colley/Fig01_Colley_LoggingDiscipline.jpg?w=320&q=90&auto=format&fit=max&dm=1790711152&s=61d2ea5ce33a6aeb2a62aa25dc994f01)

## Step One: Log Behavior and Size

Before touching audit policy, make sure the logs themselves can hold the volume you are about to generate. These settings live in Group Policy: ***Computer Configuration > Administrative Templates***.

Set ***Control Event Log behavior when the log file reaches its maximum size*** on all domain controllers to ***Disabled*** for the Application, Security, Setup, and System logs. Disabled means the log rolls and keeps collecting new events once it hits maximum size. This is already the default behavior. In most cases you'll be enforcing it consistently rather than changing it.

Next, raise the maximum log file size from the 20MB default. CIS recommends the following as a minimum, but per Microsoft's [event log recommendations](https://learn.microsoft.com/it-it/previous-versions/windows/it-pro/windows-server-2008-R2-and-2008/dd349798%28v%3Dws.10%29), all modern operating systems support much larger sizes.

| **Log** | **Minimum Recommended Size** |
| --- | --- |
| Application | 32MB (32,768KB) |
| Setup | 32MB (32,768KB) |
| System | 32MB (32,768KB) |
| Security | 192MB (196,608KB) |

![](https://trusted-sec.transforms.svdcdn.com/production/images/Blog-assets/LoggingDiscipline_Colley/Fig02_Colley_LoggingDiscipline.png?w=320&q=90&auto=format&fit=max&dm=1790711153&s=4068237d98596d677b11d95c7dc182ec)

Once these are in place, watch how long logs are actually retained on a domain controller before they begin to roll. There is no universally correct number of hours or days. What matters is that the window is long enough for your environment and for whatever ingests the logs downstream. If your collector goes offline for a maintenance window, the on-box log needs to outlast it. Raise these recommended sizes as appropriate for your environment.

## Step Two: Advanced Audit Policy

Configure domain controllers to use Advanced Audit Policy, not the nine legacy audit categories, by setting the following configuration to ***Enabled***:

* ***Computer Configuration > Windows Settings > Security Settings > Local Policies > Security Options > Audit: Force audit policy subcategory settings (Windows Vista or later) to override audit policy category s...