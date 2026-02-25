---
title: Building a Detection Foundation: Part 1 - The Single-Source Problem
url: https://trustedsec.com/blog/building-a-detection-foundation-part-1-the-single-source-problem
source: TrustedSec
date: 2026-02-24
fetch_date: 2026-02-25T04:14:45.455736
---

# Building a Detection Foundation: Part 1 - The Single-Source Problem

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
* [Building a Detection Foundation: Part 1 - The Single-Source Problem](https://trustedsec.com/blog/building-a-detection-foundation-part-1-the-single-source-problem)

February 24, 2026

# Building a Detection Foundation: Part 1 - The Single-Source Problem

Written by
Carlos Perez

MITRE ATT&CK
Threat Hunting
Incident Response

![](https://trusted-sec.transforms.svdcdn.com/production/images/Blog-Covers/BuildingDetectionFoundation-Pt1_WebHero.jpg?w=320&h=320&q=90&auto=format&fit=crop&crop=focalpoint&fp-x=0.4983&fp-y=0.4167&dm=1771606545&s=591ef7b4cbdd0975b8d75bcd0036d7ce)

Table of contents

* [When Your Single Source Goes Blind](#Blind)
* [What the Data Tells Us](#What)
* [The Pieces That Don't Show Up in Raw Numbers](#Don't)
* [The Foundation Mindset](#Foundation)
* [Assume the Worst, and Build for It](#Build)

Share

* Share URL
* [Share via Email](/cdn-cgi/l/email-protection#aa95d9dfc8c0cfc9de97e9c2cfc9c18f989ac5dfde8f989adec2c3d98f989acbd8dec3c9c6cf8f989accd8c5c78f989afed8dfd9decfcef9cfc98f989b8ccbc7da91c8c5ced397e8dfc3c6cec3c4cd8f989acb8f989aeecfdecfc9dec3c5c48f989aecc5dfc4cecbdec3c5c48f99eb8f989afacbd8de8f989a9b8f989a878f989afec2cf8f989af9c3c4cdc6cf87f9c5dfd8c9cf8f989afad8c5c8c6cfc78f99eb8f989ac2dededad98f99eb8f98ec8f98ecded8dfd9decfced9cfc984c9c5c78f98ecc8c6c5cd8f98ecc8dfc3c6cec3c4cd87cb87cecfdecfc9dec3c5c487ccc5dfc4cecbdec3c5c487dacbd8de879b87dec2cf87d9c3c4cdc6cf87d9c5dfd8c9cf87dad8c5c8c6cfc7 "Share via Email")
* [Share on Facebook](http://www.facebook.com/sharer.php?u=https%3A%2F%2Ftrustedsec.com%2Fblog%2Fbuilding-a-detection-foundation-part-1-the-single-source-problem "Share on Facebook")
* [Share on X](http://twitter.com/share?text=Building%20a%20Detection%20Foundation%3A%20Part%201%20-%20The%20Single-Source%20Problem%3A%20https%3A%2F%2Ftrustedsec.com%2Fblog%2Fbuilding-a-detection-foundation-part-1-the-single-source-problem "Share on X")
* [Share on LinkedIn](https://www.linkedin.com/shareArticle?url=https%3A%2F%2Ftrustedsec.com%2Fblog%2Fbuilding-a-detection-foundation-part-1-the-single-source-problem&mini=true "Share on LinkedIn")

## The Uncomfortable Truth About Your Telemetry

Let me start with an observation that might hit close to home. In my years working Incident Response cases and running Tabletop Exercises, I've noticed a pattern that keeps showing up: organizations often rely on a single source of truth for their security telemetry. Most of the time, it's their Endpoint Detection and Response (EDR). Sometimes it's just their Antivirus (AV). When I ask about native Windows auditing, I usually get one of two responses—either 'we have it enabled' (with no clarity on *what* exactly is enabled), or a blank stare.

This isn't a criticism, it's just the reality of how environments evolve. EDR gets deployed because it solves an immediate problem. The vendor says it covers everything. And for a while, that seems true. Until it doesn’t.

That's what this series is about, building the logging foundation that exists independently of any single vendor or tool. We'll start with Windows Security events: the logon tracking and process execution telemetry that gives you session-level visibility into what's happening on your endpoints. From there, we'll move into PowerShell logging to close the gap on script-based activity, then layer on System Monitor (Sysmon) for the network connections, registry changes, and behavioral telemetry that native logging misses. Finally, we'll bring it all together and walk through how these data sources complement each other in real-world detection engineering and Incident Response. Each layer builds on the last, and by the end, you'll have a detection foundation that holds up even when your primary tools don't.

## When Your Single Source Goes Blind

Here's the thing about relying solely on EDR: attackers know you're relying on it too. I've worked cases where the adversary's first move after getting a foothold was to tamper with or disable the EDR agent. They're not subtle about it anymore—they bring their own tools specifically designed to blind your visibility.

Let me share a war story that illustrates exactly why this matters.

### The CACTUS Incident

Last year, we worked an Incident Response engagement against the CACTUS ransomware group. They had compromised the environment and deployed multiple techniques to disable not one, but two different EDR solutions across different locations. One of the methods involved a legitimate anti-cheat driver—signed, trusted, and completely effective at blinding the security tooling.

By the time we were engaged, the EDR was essentially useless for reconstruction. ...