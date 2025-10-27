---
title: BOFs for Script Kiddies
url: https://www.trustedsec.com/blog/bofs-for-script-kiddies/
source: TrustedSec
date: 2023-02-17
fetch_date: 2025-10-04T06:54:40.732399
---

# BOFs for Script Kiddies

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
* [BOFs for Script Kiddies](https://trustedsec.com/blog/bofs-for-script-kiddies)

February 16, 2023

# BOFs for Script Kiddies

Written by
TrustedSec

Incident Response
Incident Response & Forensics
Penetration Testing
Research
Security Testing & Analysis

![](https://trusted-sec.transforms.svdcdn.com/production/images/Blog-Covers/BOFsForScriptKiddies_WebHero.jpg?w=320&h=320&q=90&auto=format&fit=crop&dm=1695564910&s=277613c554537442ecf4a5cbae3c7493)

Share

* Share URL
* [Share via Email](/cdn-cgi/l/email-protection#d3eca0a6b1b9b6b0a7ee90bbb6b0b8f6e1e3bca6a7f6e1e3a7bbbaa0f6e1e3b2a1a7bab0bfb6f6e1e3b5a1bcbef6e1e387a1a6a0a7b6b780b6b0f6e1e2f5b2bea3e8b1bcb7aaee919c95a0f6e1e3b5bca1f6e1e380b0a1baa3a7f6e1e398bab7b7bab6a0f6e092f6e1e3bba7a7a3a0f6e092f6e195f6e195a7a1a6a0a7b6b7a0b6b0fdb0bcbef6e195b1bfbcb4f6e195b1bcb5a0feb5bca1fea0b0a1baa3a7feb8bab7b7bab6a0 "Share via Email")
* [Share on Facebook](http://www.facebook.com/sharer.php?u=https%3A%2F%2Ftrustedsec.com%2Fblog%2Fbofs-for-script-kiddies "Share on Facebook")
* [Share on X](http://twitter.com/share?text=BOFs%20for%20Script%20Kiddies%3A%20https%3A%2F%2Ftrustedsec.com%2Fblog%2Fbofs-for-script-kiddies "Share on X")
* [Share on LinkedIn](https://www.linkedin.com/shareArticle?url=https%3A%2F%2Ftrustedsec.com%2Fblog%2Fbofs-for-script-kiddies&mini=true "Share on LinkedIn")

## Introduction

*I hope I don’t sound like a complete n00b, but what or who or where is a BOF? All the cool kids are talking about it, and I just smile and nod. Is he the newest Crypto billionaire, or is a meetup for like-minded hackers, or is it some other 1337 slang?*

I understand the confusion. Acronyms can be tricky and there is nothing like jargon to make one feel lost. However, I'm here yet again to provide guidance to all those Script Kiddies out there trying to keep up with the latest techniques. I'll attempt to answer all your basic questions about BOFs: who, what, where, when, and most importantly why, so at your next DefCon meetup you won’t feel quite so out-of-the-loop. Soon, you too will be using BOFs or at least correctly using the term.

## What BOF?

*Great. So, first things first, what is a BOF?*

Before I explain what a BOF is, it helps to have a little background information. Microsoft Windows relies on many different file formats but probably none more important than the Portable Executable (PE) file format. Almost all executable files on a Windows machine follow the PE file format. In addition to this file format, we have the Common Object File Format (COFF). COFF describes the layout for object files which are the compiled binary files that are linked together to produce a PE binary. Therefore, COFF files are the result of compiling C/C++ files, AKA: your basic .o/.obj files.

These object files contain a COFF header, section headers, and raw data (Such as code, data, debug info, and relocations). Object files themselves are not executable as a standalone binary, but they do contain all the required information. This information is used by the linker to produce the executable binary. The operating system in turn uses this information when loading and executing the binary. In particular, the COFF header has several important fields (illustrated in the following table).

![](https://www.trustedsec.com/wp-content/uploads/2023/02/Todd_BOF_1.jpg)

In the object file, following the COFF Header are the Section Headers. The Section Headers describe the layout, location, and characteristics of the Raw Data. This includes the data, code, and relocations. The Section Headers appear in a table and each table entry has the following format.

![](https://www.trustedsec.com/wp-content/uploads/2023/02/Todd_BOF_2.jpg)

Table 2 - Section Headers

Now that we have an idea of what an object file and COFF are, we can discuss BOFs. BOFs are Beacon Object Files. They are a special type of object file that is designed and developed to work specifically with the Cobalt Strike framework. In particular, the Cobalt Strike agent, known as a Beacon, can load and execute these object files directly without the use of a linker and without using the operating system to load and run them. Essentially, the Beacon treats the object file as just a block of position-independent code and uses the information from the COFF Header and Section Headers to load the BOF into memory. In addition, the Beacon loader provides pointers to some of the Beacon internal APIs. Therefore, you can develop your C code as if you were going to be linked against these internal Beacon APIs. More specifically, BOFs have access to:

* Data parsing APIs used for passing argu...