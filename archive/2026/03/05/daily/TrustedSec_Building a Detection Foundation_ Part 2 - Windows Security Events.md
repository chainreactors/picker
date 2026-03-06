---
title: Building a Detection Foundation: Part 2 - Windows Security Events
url: https://trustedsec.com/blog/building-a-detection-foundation-part-2-windows-security-events
source: TrustedSec
date: 2026-03-05
fetch_date: 2026-03-06T04:04:26.279229
---

# Building a Detection Foundation: Part 2 - Windows Security Events

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
* [Building a Detection Foundation: Part 2 - Windows Security Events](https://trustedsec.com/blog/building-a-detection-foundation-part-2-windows-security-events)

March 05, 2026

# Building a Detection Foundation: Part 2 - Windows Security Events

Written by
Carlos Perez

Threat Hunting
Incident Response

![](https://trusted-sec.transforms.svdcdn.com/production/images/Blog-Covers/BuildingDetectionFoundation-Pt2_WebHero.jpg?w=320&h=320&q=90&auto=format&fit=crop&dm=1771956145&s=5ff2623485564c6ceebf35a4645c962f)

Table of contents

* [Understanding Advanced Audit Policy](#Understanding)
* [Logon and Logoff Events: Your Forensic Backbone](#Backbone)
* [Process Creation: The 452-Technique Workhorse](#Workhorse)
* [Additional Events Worth Enabling](#Additional)
* [The LogonID Correlation in Practice](#Practice)

Share

* Share URL
* [Share via Email](/cdn-cgi/l/email-protection#9ea1edebfcf4fbfdeaa3ddf6fbfdf5bbacaef1ebeabbacaeeaf6f7edbbacaeffeceaf7fdf2fbbbacaef8ecf1f3bbacaecaecebedeafbfacdfbfdbbacafb8fff3eea5fcf1fae7a3dcebf7f2faf7f0f9bbacaeffbbacaedafbeafbfdeaf7f1f0bbacaed8f1ebf0faffeaf7f1f0bbaddfbbacaeceffeceabbacaeacbbacaeb3bbacaec9f7f0faf1e9edbbacaecdfbfdebecf7eae7bbacaedbe8fbf0eaedbbaddfbbacaef6eaeaeeedbbaddfbbacd8bbacd8eaecebedeafbfaedfbfdb0fdf1f3bbacd8fcf2f1f9bbacd8fcebf7f2faf7f0f9b3ffb3fafbeafbfdeaf7f1f0b3f8f1ebf0faffeaf7f1f0b3eeffeceab3acb3e9f7f0faf1e9edb3edfbfdebecf7eae7b3fbe8fbf0eaed "Share via Email")
* [Share on Facebook](http://www.facebook.com/sharer.php?u=https%3A%2F%2Ftrustedsec.com%2Fblog%2Fbuilding-a-detection-foundation-part-2-windows-security-events "Share on Facebook")
* [Share on X](http://twitter.com/share?text=Building%20a%20Detection%20Foundation%3A%20Part%202%20-%20Windows%20Security%20Events%3A%20https%3A%2F%2Ftrustedsec.com%2Fblog%2Fbuilding-a-detection-foundation-part-2-windows-security-events "Share on X")
* [Share on LinkedIn](https://www.linkedin.com/shareArticle?url=https%3A%2F%2Ftrustedsec.com%2Fblog%2Fbuilding-a-detection-foundation-part-2-windows-security-events&mini=true "Share on LinkedIn")

## The Audit Policies Nobody Configures

In [Part 1](https://trustedsec.com/blog/building-a-detection-foundation-part-1-the-single-source-problem), we looked at why relying on a single telemetry source is a recipe for blind spots. Now let's get practical. Windows has a rich set of security auditing capabilities built in—capabilities that are often either disabled entirely or only partially configured.

I've audited environments where ‘auditing is enabled’ turned out to mean that someone checked a box years ago without understanding what it actually captured. In other cases, the defaults were never touched, which means critical events simply aren't being generated.

Let's fix that.

## Understanding Advanced Audit Policy

Windows has two audit policy systems: the legacy **Local Security Policy** settings and the more granular **Advanced Audit Policy Configuration**. You want the advanced version. It gives you fine-grained control over exactly what gets logged.

You'll find these under: ***Computer Configuration → Windows Settings → Security Settings → Advanced Audit Policy Configuration***

The categories that matter most for our detection foundation are:

* **Logon/Logoff** – Session tracking and LogonID correlation
* **Account Logon** – Authentication events (especially for domain controllers)
* **Detailed Tracking** – Process creation, process termination
* **Object Access** – File, registry, and other object access (when SACLs are configured)
* **Privilege Use** – Sensitive privilege operations

And yes, I know there are gaps, and that there is more we can enable, but in this series, we are working on a foundation you can build upon. Our Purple Team can assist you with expanding this and ensuring you have proper coverage for techniques used by actors that target your industry, and can help tailor the detections in your environment. If you'd like to learn more, please [get in touch with us](https://trustedsec.com/contact). Let me walk through the essentials.

## Logon and Logoff Events: Your Forensic Backbone

I cannot overstate how important these events are. They're not flashy. They don't directly tell you ‘malware executed here.’ But they're the foundation for correlating everything else.

### Event ID 4624 – Successful Logon

This event fires every time an account successfully logs on to a system. It tells you:

* Who logged on (account name, domain)
* From where (source IP address, workstation name)
* How (logon type)
* The LogonID assigned to this session
  + That LogonID is gold. It appears in subsequent events (p...