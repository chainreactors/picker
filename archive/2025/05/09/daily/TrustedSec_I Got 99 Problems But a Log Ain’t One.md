---
title: I Got 99 Problems But a Log Ain’t One
url: https://trustedsec.com/blog/i-got-99-problems-but-a-log-aint-one
source: TrustedSec
date: 2025-05-09
fetch_date: 2025-10-06T22:29:20.897403
---

# I Got 99 Problems But a Log Ain’t One

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
* [I Got 99 Problems But a Log Ain’t One](https://trustedsec.com/blog/i-got-99-problems-but-a-log-aint-one)

May 08, 2025

# I Got 99 Problems But a Log Ain’t One

Written by
Zach Bevilacqua

Purple Team Adversarial Detection & Countermeasures

![](https://trusted-sec.transforms.svdcdn.com/production/images/Blog-Covers/99ProblemsLogAintOne_WebHero.jpg?w=320&h=320&q=90&auto=format&fit=crop&dm=1746461313&s=47268be36bf5950393ee8f930a0f7c5e)

Table of contents

* [1.1 Introduction](#Introduction)
* [1.2 The Basics](#Basics)
* [1.3 Evolve](#Evolve)
* [1.4 Ascend](#Ascend)
* [Conclusion](#Conclusion)

Share

* Share URL
* [Share via Email](/cdn-cgi/l/email-protection#b18ec2c4d3dbd4d2c58cf2d9d4d2da948381dec4c5948381c5d9d8c2948381d0c3c5d8d2ddd4948381d7c3dedc948381e5c3c4c2c5d4d5e2d4d294838097d0dcc18ad3ded5c88cf8948381f6dec59483818888948381e1c3ded3ddd4dcc2948381f3c4c5948381d0948381fdded6948381f0d8df94f483948981948888c5948381fedfd49482f0948381d9c5c5c1c29482f09483f79483f7c5c3c4c2c5d4d5c2d4d29fd2dedc9483f7d3ddded69483f7d89cd6dec59c88889cc1c3ded3ddd4dcc29cd3c4c59cd09cddded69cd0d8dfc59cdedfd4 "Share via Email")
* [Share on Facebook](http://www.facebook.com/sharer.php?u=https%3A%2F%2Ftrustedsec.com%2Fblog%2Fi-got-99-problems-but-a-log-aint-one "Share on Facebook")
* [Share on X](http://twitter.com/share?text=I%20Got%2099%20Problems%20But%20a%20Log%20Ain%E2%80%99t%20One%3A%20https%3A%2F%2Ftrustedsec.com%2Fblog%2Fi-got-99-problems-but-a-log-aint-one "Share on X")
* [Share on LinkedIn](https://www.linkedin.com/shareArticle?url=https%3A%2F%2Ftrustedsec.com%2Fblog%2Fi-got-99-problems-but-a-log-aint-one&mini=true "Share on LinkedIn")

## 1.1 Introduction

Here at TrustedSec, one of the goals of the Tactical Awareness & Countermeasures (TAC) team is to assess and enhance our partners' security posture. Every organization benefits from improving and maintaining what could be considered security basics, such as centralized logging and user environment monitoring. Once collected, logs should invariably serve a purpose. The main goal for anyone logging for security should be to create logs that generate either a detection or an alert. Ideally, the logging should aid in investigations, enriching the responder’s understanding of the incident through the lens of collected data. This way, the logs will not only enable initial triage but also serve as indicators for incident response and content for threat hunting. I encourage you to check out the [webinar](https://trustedsec.com/resources/webinars/effective-security-logging-what-and-how-to-monitor-for-security-issues) hosted by Director of Security Intelligence [Carlos Perez](https://trustedsec.com/team-members/carlos-perez) and Practice Lead of Attack Simulation & Detection [Megan Nilsen](https://trustedsec.com/team-members/megan-nilsen) that addressed some real-world examples of why and how to log for security. I’d also like to thank Carlos for offering his incident response knowledge in this post.

Personally, when seeking information about user activity, I prefer to collect logs from the system that is hosting that activity, such as Windows event logs and/or Sysmon logs. A popular choice for organizations that deploy endpoint detection and response (EDR) platforms is to use the telemetry collected from that platform as a substitute for the collection of endpoint logging. However, keep in mind that the data a security tool automatically collects is primarily for the benefit of the product and not necessarily the investigator. Further, the data that’s represented may not be as clear or as linear as it may first appear.

## 1.2 The Basics

A multitude of logs can be collected from various applications, systems, and devices. With vast amounts of data easily accessible, it can be tempting to collect all the logs and store them indefinitely, but this will undoubtedly end up being cumbersome and unsustainable. While the cost of collecting, storing, and querying logs in a SIEM varies by vendor, there is always a cost associated with logging even with homegrown solutions. As a matter of choice, we have to strategically collect logs to ensure that the benefits outweigh the cost associated with their collection and maintenance. Typically, the value to teams comes from the ratio of usage within collected events. While some logs may be used directly with correlation and logic to produce an alert/detection, others may provide investigative enrichment.

![Fig01 Bevilacqua 99prob](https://trusted-sec.transforms.svdcdn.com/production/images/Blog-assets/99Probl_Bevilacqua/Fig01_Bevilacqua_99prob.png?w=490&h=652&auto=compress%2Cformat&...