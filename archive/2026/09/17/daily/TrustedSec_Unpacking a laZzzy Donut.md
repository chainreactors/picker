---
title: Unpacking a laZzzy Donut
url: https://trustedsec.com/blog/unpacking-a-lazzzy-donut
source: TrustedSec
date: 2026-09-17
fetch_date: 2026-09-18T06:53:10.326708
---

# Unpacking a laZzzy Donut

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
* [Unpacking a laZzzy Donut](https://trustedsec.com/blog/unpacking-a-lazzzy-donut)

September 17, 2026

# Unpacking a laZzzy Donut

Written by
Scott Nusbaum

Malware Analysis
Incident Response & Forensics
Research

![](https://trusted-sec.transforms.svdcdn.com/production/images/Blog-Covers/UnoackingLaZzzyDonut_WebHero.jpg?w=320&h=320&q=90&auto=format&fit=crop&dm=1789047927&s=dc0fb6211f9e5fc75bd695ce94a5eba2)

Table of contents

* [Stage 1: Obfuscated Python Bytecode](#One)
* [Stage 2: First Donut Layer](#Two)
* [Stage 3: laZzzy Layer - A Gap in Tooling](#Three)
* [Stage 4: Second Donut Layer](#Four)
* [Stage 5: Embedded .NET DLL](#Five)
* [Stage 6: .NET Resources](#Six)
* [Conclusion](#Conclusion)

Share

* Share URL
* [Share via Email](/cdn-cgi/l/email-protection#9da2eee8fff7f8fee9a0def5f8fef6b8afadf2e8e9b8afade9f5f4eeb8afadfcefe9f4fef1f8b8afadfbeff2f0b8afadc9efe8eee9f8f9cef8feb8afacbbfcf0eda6fff2f9e4a0c8f3edfcfef6f4f3fab8afadfcb8afadf1fcc7e7e7e4b8afadd9f2f3e8e9b8aedcb8afadf5e9e9edeeb8aedcb8afdbb8afdbe9efe8eee9f8f9eef8feb3fef2f0b8afdbfff1f2fab8afdbe8f3edfcfef6f4f3fab0fcb0f1fce7e7e7e4b0f9f2f3e8e9 "Share via Email")
* [Share on Facebook](https://www.facebook.com/sharer.php?u=https%3A%2F%2Ftrustedsec.com%2Fblog%2Funpacking-a-lazzzy-donut "Share on Facebook")
* [Share on X](https://twitter.com/share?text=Unpacking%20a%20laZzzy%20Donut%3A%20https%3A%2F%2Ftrustedsec.com%2Fblog%2Funpacking-a-lazzzy-donut "Share on X")
* [Share on LinkedIn](https://www.linkedin.com/shareArticle?url=https%3A%2F%2Ftrustedsec.com%2Fblog%2Funpacking-a-lazzzy-donut&mini=true "Share on LinkedIn")

Recently, we came across an interesting malware sample. It used a multi-stage malware loader that chains together obfuscation and shellcode-injection techniques. The sample begins as obfuscated Python bytecode and concludes with encrypted .NET resources, using nested layers of shellcode generation, encryption, and obfuscation to frustrate detection and analysis at each stage.

While I performed the initial triage of the malware manually, it was a significant time saver to find existing public tooling to speed up the recovery. Public tools needed to be modified, and in some cases, we needed to create a customer tool to address a specific technique. In this post, we will walk through the steps used and what needed to be created or modified.

## The Full Chain

![](https://trusted-sec.transforms.svdcdn.com/production/images/Blog-assets/laZzzyDonut_Nusbaum/Fig01_Nusbaum_laZzzyDonut.png?w=320&q=90&auto=format&fit=max&dm=1788983828&s=14232bd341d39e9cd4d9ab4b213a3660)

Figure 1- Malware Execution Chain

Each stage encrypts or obfuscates the next, and each must be reversed in order to trace the execution path and understand the final payload.

## Stage 1: Obfuscated Python Bytecode

The file we first analyzed had the extension .pyc, meaning that it is most likely Python bytecode. To verify this, we run the file command:

```
******.pyc: Byte-compiled Python module for CPython 3.13 (magic: 3571), timestamp-based, .py timestamp: Wed Jun 24 06:18:29 2026 UTC, .py size: 8371083 bytes
```

Let’s see what strings are visible in the file. Most of the time, I will use strings, but this time I opened the file in Vim. I noticed the string ***Kramer*** right away, and later in the file there is a large blob of text, which seemed to make no sense at first.

![](https://trusted-sec.transforms.svdcdn.com/production/images/Blog-assets/laZzzyDonut_Nusbaum/Fig02_Nusbaum_laZzzyDonut.png?w=320&q=90&auto=format&fit=max&dm=1788983830&s=db4bed4705f4fdde29894b1b6c5c0ae8)

Figure 2 - HEX View of the File Showing Kramer String

![](https://trusted-sec.transforms.svdcdn.com/production/images/Blog-assets/laZzzyDonut_Nusbaum/Fig03_Nusbaum_laZzzyDonut.png?w=320&q=90&auto=format&fit=max&dm=1788983830&s=5c762a74b06fae1104eda485d6bff6a6)

Figure 3 - HEX View of the File Showing the Obfuscated Code

Next, we need to get from a .pyc file to .py. I used the [NPX](https://classic.yarnpkg.com/en/package/depyo) to convert from the bytecode to standard Python, which makes the script much easier to read.

![](https://trusted-sec.transforms.svdcdn.com/production/images/Blog-assets/laZzzyDonut_Nusbaum/Fig04_Nusbaum_laZzzyDonut.png?w=320&q=90&auto=format&fit=max&dm=1788983831&s=354a032fef39e5c13448e97fd9614d46)

Figure 4 - Obfuscated Code after Converting from pyc to py

After searching for a little while, I came across the [Kramer GitHub repo](https://github.com/billythegoat356/Kramer/tree/main). This matched what I was seeing perfectly. The only problem was that it was protected by a key, so back to searching again. This time I came across a tool to brute-force the key, [kramer\_python\_](https://gist.githubusercontent.com/bobby-tablez/bb1f13c10231192a8e0ebc58548951d3/raw/a4937a65eb1a494ee4fe43e2f3beb2713991a2ed/kram...