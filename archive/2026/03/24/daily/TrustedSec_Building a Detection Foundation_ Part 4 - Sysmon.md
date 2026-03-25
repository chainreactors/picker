---
title: Building a Detection Foundation: Part 4 - Sysmon
url: https://trustedsec.com/blog/building-a-detection-foundation-part-4-sysmon
source: TrustedSec
date: 2026-03-24
fetch_date: 2026-03-25T04:17:31.876808
---

# Building a Detection Foundation: Part 4 - Sysmon

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
* [Building a Detection Foundation: Part 4 - Sysmon](https://trustedsec.com/blog/building-a-detection-foundation-part-4-sysmon)

March 24, 2026

# Building a Detection Foundation: Part 4 - Sysmon

Written by
Carlos Perez

Threat Hunting
Incident Response

![](https://trusted-sec.transforms.svdcdn.com/production/images/Blog-Covers/BuildingDetectionFoundation-Pt4_WebHero.jpg?w=320&h=320&q=90&auto=format&fit=crop&dm=1774027355&s=e596ea8a946438e6735af4fa67116059)

Table of contents

* [What Sysmon Provides](#SysmonProvides)
* [Essential Sysmon Events](#Essential)
* [A Practical Sysmon Configuration](#Configuration)
* [Configuration Tuning Philosophy](#Philosophy)
* [Sysmon Alternatives and Companions](#Alternatives)
* [What We've Built So Far](#Built)
* [Resources for Going Deeper](#Resources)

Share

* Share URL
* [Share via Email](/cdn-cgi/l/email-protection#38074b4d5a525d5b4c057b505d5b531d0a08574d4c1d0a084c50514b1d0a08594a4c515b545d1d0a085e4a57551d0a086c4a4d4b4c5d5c6b5d5b1d0a091e595548035a575c41057a4d51545c51565f1d0a08591d0a087c5d4c5d5b4c5157561d0a087e574d565c594c5157561d0b791d0a0868594a4c1d0a080c1d0a08151d0a086b414b5557561d0b791d0a08504c4c484b1d0b791d0a7e1d0a7e4c4a4d4b4c5d5c4b5d5b165b57551d0a7e5a54575f1d0a7e5a4d51545c51565f1559155c5d4c5d5b4c515756155e574d565c594c5157561548594a4c150c154b414b555756 "Share via Email")
* [Share on Facebook](http://www.facebook.com/sharer.php?u=https%3A%2F%2Ftrustedsec.com%2Fblog%2Fbuilding-a-detection-foundation-part-4-sysmon "Share on Facebook")
* [Share on X](http://twitter.com/share?text=Building%20a%20Detection%20Foundation%3A%20Part%204%20-%20Sysmon%3A%20https%3A%2F%2Ftrustedsec.com%2Fblog%2Fbuilding-a-detection-foundation-part-4-sysmon "Share on X")
* [Share on LinkedIn](https://www.linkedin.com/shareArticle?url=https%3A%2F%2Ftrustedsec.com%2Fblog%2Fbuilding-a-detection-foundation-part-4-sysmon&mini=true "Share on LinkedIn")

## Filling the Gaps Native Logging Can't

At this point in our series, we have Windows Security events capturing logon sessions and process creation, and PowerShell logging capturing script execution. That's a solid foundation. But if you've worked Incident Response, you've hit the walls of native logging:

* *"We know PowerShell ran, but what did it connect to?"*
* *"Something modified this registry key, but we don't know which process."*
* *"A malicious DLL was loaded—when? By what?"*

This is where Sysmon enters the picture. Sysmon, a free Windows system service and driver from Microsoft [Sysinternals](https://learn.microsoft.com/en-us/sysinternals/) that monitors and logs system activity to the Windows event log, is soon to be included in the latest versions of Windows Server and Windows 11. It's not a replacement for native logging—it's a complement that provides telemetry Windows simply doesn't offer natively.

I do have a small bias since I have been writing about the tool since it came out, given multiple training classes on it, and wrote most of the [Sysmon Community Guide](https://github.com/trustedsec/SysmonCommunityGuide), but I do see where it falls short and will do my best to cover some of the basics. Do check the [resources](#Resources) at the end of this blog to go deeper on how to leverage the tool.

## What Sysmon Provides

Looking back at our [MITRE ATT&CK](https://attack.mitre.org/) data source coverage, here's where Sysmon fills critical gaps:

| **Data Component** | **Technique Coverage** | **Sysmon Event** |
| --- | --- | --- |
| **Process Creation** | 452 | Event 1 (enhanced parent info, hashes) |
| **Network Connection Creation** | 151 | Event 3 |
| **Module Load** | 109 | Event 7 |
| **Windows Registry Key Modification** | 86 | Events 12, 13, 14 |
| **Process Access** | 77 | Event 10 |
| **File Creation** | 174 | Event 11 |
| **Driver Load** | 14 | Event 6 |
| **WMI Operations** | 7 | Events 19, 20, 21 |
| **Named Pipe** | 4 | Events 17, 18 |
| **DNS Queries** | — | Event 22 |

Let me walk through the Sysmon events you should care about and why.

## Essential Sysmon Events

### Event 1: Process Creation

Yes, we have Event ID 4688 from native logging. So why use Sysmon Event 1?

**What Sysmon adds:**

* File hashes (MD5, SHA1, SHA256) of the executable
* More reliable parent process information
* Parent command line
* Integrity level
* More consistent formatting

**Detection value:**

* Hash lookups for known-bad binaries
* Detecting renamed legitimate tools (hash matches, name doesn't)
* Process tree reconstruction

### Event 3: Network Connection

This is huge. Native Windows logging does not provide a reliable way to track which process connected to whic...