---
title: Shai-Hulud Is Back, and This Time It Ate the Whole Ecosystem
url: https://trustedsec.com/blog/shai-hulud-is-back
source: TrustedSec
date: 2026-05-21
fetch_date: 2026-05-22T06:08:09.476421
---

# Shai-Hulud Is Back, and This Time It Ate the Whole Ecosystem

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
* [Shai-Hulud Is Back, and This Time It Ate the Whole Ecosystem](https://trustedsec.com/blog/shai-hulud-is-back)

May 21, 2026

# Shai-Hulud Is Back, and This Time It Ate the Whole Ecosystem

Written by
Carlos Perez

Incident Response
Malware Analysis

![](https://trusted-sec.transforms.svdcdn.com/production/images/Blog-Covers/Shai-HuludIsBack_WebHero.jpg?w=320&h=320&q=90&auto=format&fit=crop&dm=1779307828&s=206c80d3d99a39a89de449131fa47d9e)

Table of contents

* [1.1      What Actually Happened](#What)
* [1.2      How the Malware Works](#How)
* [1.3      Detecting Compromise](#Compromise)
* [1.4      Cleanup](#Cleanup)
* [1.5      Auditd Rules for Linux Systems](#Auditd)
* [1.6      What to Change Going Forward](#Change)
* [1.7      Closing](#Closing)
* [1.8      Shai-Hulud IOC Reference Tables](#Reference)

Share

* Share URL
* [Share via Email](/cdn-cgi/l/email-protection#e5da9690878f808691d8a68d80868ec0d7d58a9091c0d7d5918d8c96c0d7d58497918c868980c0d7d583978a88c0d7d5b1979096918081b68086c0d7d4c3848895de878a819cd8b68d848cc8ad90899081c0d7d5ac96c0d7d5a784868ec0d7a6c0d7d5848b81c0d7d5b18d8c96c0d7d5b18c8880c0d7d5ac91c0d7d5a49180c0d7d5918d80c0d7d5b28d8a8980c0d7d5a0868a969c96918088c0d6a4c0d7d58d91919596c0d6a4c0d7a3c0d7a391979096918081968086cb868a88c0d7a387898a82c0d7a3968d848cc88d90899081c88c96c88784868e "Share via Email")
* [Share on Facebook](http://www.facebook.com/sharer.php?u=https%3A%2F%2Ftrustedsec.com%2Fblog%2Fshai-hulud-is-back "Share on Facebook")
* [Share on X](http://twitter.com/share?text=Shai-Hulud%20Is%20Back%2C%20and%20This%20Time%20It%20Ate%20the%20Whole%20Ecosystem%3A%20https%3A%2F%2Ftrustedsec.com%2Fblog%2Fshai-hulud-is-back "Share on X")
* [Share on LinkedIn](https://www.linkedin.com/shareArticle?url=https%3A%2F%2Ftrustedsec.com%2Fblog%2Fshai-hulud-is-back&mini=true "Share on LinkedIn")

The name Shai-Hulud is not new to anyone who's been watching npm supply chain attacks over the past few years, or has heard me sound like a broken record in threat intel reports and when warning customers about gaps in software inventory and processes when building playbooks. It's the same worm, but a different wave.

What changed this time is the blast radius of over 300 packages across Alibaba's AntV data visualization ecosystem, and at the time of this writing, the count is still climbing. The nasty touch of setting a dead-man switch to delete the root folder was one that I will be adding to Tabletop Exercises and will make some organizations think twice when doing rapid isolation.

## 1.1      What Actually Happened

All it took was one (1) npm account. The **atool** account, which owns the popular ***timeago.js*** package (around 1.5 million weekly downloads) and publishes across a large chunk of the ***@antv*** namespace, got compromised. Whoever did this pushed malicious versions across charting libraries, graph tools, mapping components, and general-purpose utilities, the whole suite of packages. Anything that pulls from AntV is in scope, from front-end teams to data visualization pipelines. This will be the hardest part for many out there, as your perimeter logs will be king when hunting for hosts to inspect,in addition to the use of EDR and other tools that allow you to script or leverage built-in string searches.

The attacker didn't try to hide the impact, with over 2,200 public GitHub repositories created using stolen tokens. Each one was named with Dune-universe terminology, described with the reversed string ***"niagA oG eW ereH :duluH-iahS."*** Flip that around: ***"Shai-Hulud: Here We Go Again."*** They're announcing themselves in real time, using the credentials they just stole. That is not accidental, it is someone making a point. With how well orchestrated the attack is, I cannot say this is sloppy but intentional.

**Any environment that installed an affected package should be treated as fully compromised. Rotate everything now, before you finish reading this.**

High-impact packages by download volume:

| **Package** | **Compromised Versions** |
| --- | --- |
| timeago.js | 4.1.2, 4.2.2 |
| echarts-for-react | 3.0.7, 3.1.7, 3.2.7 |
| jest-canvas-mock | 2.5.3, 2.6.3, 2.7.3 |
| @antv/g6 | 5.2.1, 5.3.1 |
| @antv/g2 | 5.5.8, 5.6.8 |
| @antv/l7 | 2.26.10, 2.27.10 |
| mcp-echarts | 0.8.1, 0.9.1 |
| mcp-mermaid | 0.5.1, 0.6.1 |

The full list at the end and it keeps growing. I still recommend you perform a threat hunt for the indicators of compromise (IOCs)).

## 1.2      How the Malware Works

This second time around, we see the same payload across every compromised package, just differently obfuscated (note that this does not mean it has not changed recently). The entry point is either a preinstall or postinstall hook. Execution fires the moment npm install runs, which happens before anything in your codebase loads.

##...