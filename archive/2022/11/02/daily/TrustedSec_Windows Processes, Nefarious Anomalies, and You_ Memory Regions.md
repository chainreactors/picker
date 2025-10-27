---
title: Windows Processes, Nefarious Anomalies, and You: Memory Regions
url: https://www.trustedsec.com/blog/windows-processes-nefarious-anomalies-and-you-memory-regions/
source: TrustedSec
date: 2022-11-02
fetch_date: 2025-10-03T21:34:50.292581
---

# Windows Processes, Nefarious Anomalies, and You: Memory Regions

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
* [Windows Processes, Nefarious Anomalies, and You: Memory Regions](https://trustedsec.com/blog/windows-processes-nefarious-anomalies-and-you-memory-regions)

November 01, 2022

# Windows Processes, Nefarious Anomalies, and You: Memory Regions

Written by
Brandon McGrath

![](https://trusted-sec.transforms.svdcdn.com/production/images/Blog-Covers/WindowProcesses_Part1_WebHero.jpg?w=320&h=320&q=90&auto=format&fit=crop&dm=1695569721&s=4f9d425b6163df5b0deee2ad2bacf01a)

Share

* Share URL
* [Share via Email](/cdn-cgi/l/email-protection#d1eea2a4b3bbb4b2a5ec92b9b4b2baf4e3e1bea4a5f4e3e1a5b9b8a2f4e3e1b0a3a5b8b2bdb4f4e3e1b7a3bebcf4e3e185a3a4a2a5b4b582b4b2f4e3e0f7b0bca1eab3beb5a8ec86b8bfb5bea6a2f4e3e181a3beb2b4a2a2b4a2f4e392f4e3e19fb4b7b0a3b8bea4a2f4e3e190bfbebcb0bdb8b4a2f4e392f4e3e1b0bfb5f4e3e188bea4f4e290f4e3e19cb4bcbea3a8f4e3e183b4b6b8bebfa2f4e290f4e3e1b9a5a5a1a2f4e290f4e397f4e397a5a3a4a2a5b4b5a2b4b2ffb2bebcf4e397b3bdbeb6f4e397a6b8bfb5bea6a2fca1a3beb2b4a2a2b4a2fcbfb4b7b0a3b8bea4a2fcb0bfbebcb0bdb8b4a2fcb0bfb5fca8bea4fcbcb4bcbea3a8fca3b4b6b8bebfa2 "Share via Email")
* [Share on Facebook](http://www.facebook.com/sharer.php?u=https%3A%2F%2Ftrustedsec.com%2Fblog%2Fwindows-processes-nefarious-anomalies-and-you-memory-regions "Share on Facebook")
* [Share on X](http://twitter.com/share?text=Windows%20Processes%2C%20Nefarious%20Anomalies%2C%20and%20You%3A%20Memory%20Regions%3A%20https%3A%2F%2Ftrustedsec.com%2Fblog%2Fwindows-processes-nefarious-anomalies-and-you-memory-regions "Share on X")
* [Share on LinkedIn](https://www.linkedin.com/shareArticle?url=https%3A%2F%2Ftrustedsec.com%2Fblog%2Fwindows-processes-nefarious-anomalies-and-you-memory-regions&mini=true "Share on LinkedIn")

While operating on a red team, the likelihood of an Endpoint Detection and Response (EDR) being present on a host is becoming increasingly higher than it was a few years ago. When an implant is being initiated on a host, whether it’s on-disk or loaded into memory, then there is a lot to consider. In this post, we will focus on one very specific component of EDR: memory scanners.

A memory scanner is quite self-explanatory. It scans the memory of a process and attempts to identify non-standard attributes within a memory region in effort to determine if the process requires additional analysis and/or containment.

The community has done a great job of implementing memory scanners to identify malicious activity, and they have been adopted by red teamers as a means to QA their own implants:

* [pe-sieve](https://github.com/hasherezade/pe-sieve) by [Hasherezade](https://twitter.com/hasherezade)
* [Moneta](https://github.com/forrest-orr/moneta) by [Forrest Orr](https://twitter.com/_forrestorr)
* [Hunt-Sleeping-Beacons](https://github.com/thefLink/Hunt-Sleeping-Beacons) by [thefLinkk](https://twitter.com/thefLinkk)

For extra points, organizations *could* implement these into their own detection strategy – however, these types of tools look for very specific anomalies within a process, and because of that, may generate false positives.

In terms of EDR vendors, smaller components of these scanners will likely be in their toolkit, but they must undergo a lot of effort to ensure that false positives don’t make it into production, let alone customer environments. However, they are used for a slightly different purpose within an EDR—typically, when one of the memory scanner indicators is hit, it will trigger further analysis of the process. That could be known-malware signatures, log analysis for that particular process, and so on. An EDR is extremely unlikely to create an alert on an endpoint because RWX was allocated in a process. As we go into this series, we will show the sheer number of false positives that memory scanners can create when scanning everything. However, it *may* cause the EDR to take a further look into that process (as a naive example).

In this blog, we will look at what a memory scanner is looking at and why, and then we will identify some low-hanging fruit from a Command & Control (C2) implant.

## 1.  Process Structure

In its simplest form, a process is an executing program. Under the hood, Windows is an object-oriented system. This means that each component of Windows will essentially boil down to sort of object. As for a process, the Windows Kernel knows this as the [EPROCESS structure](https://www.geoffchappell.com/studies/windows/km/ntoskrnl/inc/ntos/ps/eprocess/index.htm). However, going up a level, this structure is simplified to the [Process Environment Block](https://docs.microsoft.com/en-us/windows/win32/api/winternl/ns-winternl-peb) (PEB).

```
typedef ...