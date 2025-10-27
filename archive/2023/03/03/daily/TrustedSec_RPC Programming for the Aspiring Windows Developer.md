---
title: RPC Programming for the Aspiring Windows Developer
url: https://www.trustedsec.com/blog/rpc-programming-for-the-aspiring-windows-developer/
source: TrustedSec
date: 2023-03-03
fetch_date: 2025-10-04T08:32:59.923493
---

# RPC Programming for the Aspiring Windows Developer

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
* [RPC Programming for the Aspiring Windows Developer](https://trustedsec.com/blog/rpc-programming-for-the-aspiring-windows-developer)

March 02, 2023

# RPC Programming for the Aspiring Windows Developer

Written by
Christopher Paschen

Research

![](https://trusted-sec.transforms.svdcdn.com/production/images/Blog-Covers/RPCProgramming_WebHero.jpg?w=320&h=320&q=90&auto=format&fit=crop&dm=1695564338&s=7778de184530dd3d50079fe3e7466a9a)

Share

* Share URL
* [Share via Email](/cdn-cgi/l/email-protection#a29dd1d7c0c8c7c1d69fe1cac7c1c9879092cdd7d6879092d6cacbd1879092c3d0d6cbc1cec7879092c4d0cdcf879092f6d0d7d1d6c7c6f1c7c187909384c3cfd299c0cdc6db9ff0f2e1879092f2d0cdc5d0c3cfcfcbccc5879092c4cdd0879092d6cac7879092e3d1d2cbd0cbccc5879092f5cbccc6cdd5d1879092e6c7d4c7cecdd2c7d08791e3879092cad6d6d2d18791e38790e48790e4d6d0d7d1d6c7c6d1c7c18cc1cdcf8790e4c0cecdc58790e4d0d2c18fd2d0cdc5d0c3cfcfcbccc58fc4cdd08fd6cac78fc3d1d2cbd0cbccc58fd5cbccc6cdd5d18fc6c7d4c7cecdd2c7d0 "Share via Email")
* [Share on Facebook](http://www.facebook.com/sharer.php?u=https%3A%2F%2Ftrustedsec.com%2Fblog%2Frpc-programming-for-the-aspiring-windows-developer "Share on Facebook")
* [Share on X](http://twitter.com/share?text=RPC%20Programming%20for%20the%20Aspiring%20Windows%20Developer%3A%20https%3A%2F%2Ftrustedsec.com%2Fblog%2Frpc-programming-for-the-aspiring-windows-developer "Share on X")
* [Share on LinkedIn](https://www.linkedin.com/shareArticle?url=https%3A%2F%2Ftrustedsec.com%2Fblog%2Frpc-programming-for-the-aspiring-windows-developer&mini=true "Share on LinkedIn")

As EDR/AV solutions have evolved, attackers, be they malicious or hired testers, need to improve their techniques by exploring new avenues of accomplishing common tasks. These methods evolve over time and sometimes even cycles as techniques become highly detected, then dropped, and later rediscovered. Over a series of posts, we are going to investigate mixing the old and the new by programming Windows Remote Procedure Call (RPC) calls into a Beacon Object File (BOF).

RPC is the implementation by which a computer calls functionality on a different system to cause some action. In Windows, RPC is ubiquitous and is the backing technology behind some of the Windows Application Programing Interface (API) and standard Component Object Model (COM) interfaces. RPC is an old technology that even many seasoned developers do not fully understand.

BOFs are a new method of coding extensions into implants that live on hosts and establish continuous access for an attacker. At its core, it takes the previous technique of reflective loading and moves the responsibility of loading/linking code to the implant already executed on a target system. This technique is being widely adopted by multiple implant technologies, including Cobalt Strike’s Beacon, Metasploit's Meterpreter, Sliver’s Implant, and other commercially available implants. In a way, BOFs have become a standard plugin interface that can be shared across offensive tooling.

Over three (3) blog posts we will dive into:

* Programming against RPC as an offensive tool developer
* How BOFs have changed since I last wrote about them [here](https://trustedsec.com/blog/a-developers-introduction-to-beacon-object-files)
* Incorporating RPC code into BOFs

## RPC for the Windows Developer

RPC often does not need to be directly touched or manipulated to accomplish goals as a Windows developer, at least if you have access to the Windows API. The Services API could be used instead of coding against [MS-SCMR,](https://learn.microsoft.com/en-us/openspecs/windows_protocols/ms-scmr/705b624a-13de-43cc-b8a2-99573da3635f) the registry API instead of [MS-RRP,](https://learn.microsoft.com/en-us/openspecs/windows_protocols/ms-scmr/705b624a-13de-43cc-b8a2-99573da3635f) and multiple net commands instead of [MS-SAMR.](https://learn.microsoft.com/en-us/openspecs/windows_protocols/ms-samr/4df07fab-1bbc-452f-8e92-7853a3c7e380)

Interestingly, tooling like [Impacket](https://github.com/fortra/impacket) is based around direct manipulation of RPC and is the reason your non-Windows computer can suddenly manipulate a Windows-based machine. Overriding protocols directly is also what allows pass-the-hash (PtH), as we are not allowing Windows to step in and control the authentication steps. Coding new tools into these external to Windows packages requires intermediate knowledge of RPC and Windows Authentication, and is therefore outside the scope of this article.

Having established that a Windows developer normally does not have to worry about RPC particulars, why care about RPC? There are instances where direc...