---
title: Must I TRA?: PCI Targeted Risk Analysis
url: https://trustedsec.com/blog/must-i-tra-pci-targeted-risk-analysis
source: TrustedSec
date: 2024-08-14
fetch_date: 2025-10-06T18:04:18.782276
---

# Must I TRA?: PCI Targeted Risk Analysis

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
* [Must I TRA?: PCI Targeted Risk Analysis](https://trustedsec.com/blog/must-i-tra-pci-targeted-risk-analysis)

August 13, 2024

# Must I TRA?: PCI Targeted Risk Analysis

Written by
Steve Maxwell

PCI DSS
Information Security Compliance
Business Risk Assessment

![](https://trusted-sec.transforms.svdcdn.com/production/images/Blog-Covers/PCITargetedRiskAnalysis_WebHero.jpg?w=320&h=320&q=90&auto=format&fit=crop&dm=1722975863&s=b3c8fab6795aa2e5e3e68601e7b4e529)

Table of contents

* [Must I TRA?](#Must)
* [Which Requirements? High View](#Requirements)
* [Common Implementations](#Implementations)
* [TRA per SAQ Type](#SAQ)
* [Defining the TRA Process](#Process)
* [Conclusion](#Conclusion)

Share

* Share URL
* [Share via Email](/cdn-cgi/l/email-protection#58672b2d3a323d3b2c651b303d3b337d6a68372d2c7d6a682c30312b7d6a68392a2c313b343d7d6a683e2a37357d6a680c2a2d2b2c3d3c0b3d3b7d6a697e393528633a373c2165152d2b2c7d6a68117d6a680c0a197d6b1e7d6b197d6a68081b117d6a680c392a3f3d2c3d3c7d6a680a312b337d6a6819363934212b312b7d6b197d6a68302c2c282b7d6b197d6a1e7d6a1e2c2a2d2b2c3d3c2b3d3b763b37357d6a1e3a34373f7d6a1e352d2b2c7531752c2a3975283b31752c392a3f3d2c3d3c752a312b337539363934212b312b "Share via Email")
* [Share on Facebook](http://www.facebook.com/sharer.php?u=https%3A%2F%2Ftrustedsec.com%2Fblog%2Fmust-i-tra-pci-targeted-risk-analysis "Share on Facebook")
* [Share on X](http://twitter.com/share?text=Must%20I%20TRA%3F%3A%20PCI%20Targeted%20Risk%20Analysis%3A%20https%3A%2F%2Ftrustedsec.com%2Fblog%2Fmust-i-tra-pci-targeted-risk-analysis "Share on X")
* [Share on LinkedIn](https://www.linkedin.com/shareArticle?url=https%3A%2F%2Ftrustedsec.com%2Fblog%2Fmust-i-tra-pci-targeted-risk-analysis&mini=true "Share on LinkedIn")

Use of Targeted Risk Analysis (TRA) is a PCI best practice until March 31, 2025, at which time it becomes required for several controls across many assessment types. Unlike many other new controls, this applies as much to merchants as it does to service providers.

If you are weary from blogs that are not very helpful for minimizing your compliance efforts, then this was written just for you.

Topics include:

* Must I TRA?
* Which Requirements? High View
* Common Implementations
* TRA per SAQ Type
* Defining the TRA Process

So that this ages properly, this is regarding the current Payment Card Industry Data Security Standard (PCI DSS) version 4.0.1 and reporting templates version r1 from December 2022. TRAs have been a source of many, many questions that I will answer here. As with all blogs, applicability to you may vary with your unique compliance obligations.

## Must I TRA?

Just because a PCI DSS report is a full ROC or SAQ type D does not mean that TRAs must be applied. TRA requirements are attached to other requirements that may or may not be applicable to a specific organization. If the organization’s scope is such that none of the PCI DSS requirements that reference Requirement 12.3.1 are in scope, then a TRA will not be required.

TRAs are required if:

* Using an iFrame or URL to redirect to a third-party payment processor
* Directly processing, transporting, or storing cardholder data, including mail order payments, call center payments, mobile device payments, eCommerce payments, viewing cardholder data online, and much more
* Utilizing Point of Sale (POS) solutions that are not Point-to-Point Encryption (P2PE)-validated
* Declaring some system types as not requiring anti-malware software
* Periodically reviewing access less often than every six months
* Utilizing the customized approach
* Having payment channels eligible for SAQ types A, A-EP, C, and D

Merchants qualifying for SAQ types B, B-IP, C-VT, and P2PE should not require TRAs. It takes only one in-scope activity in order to require a TRA, but the following activities or systems might not require TRAs:

* Legacy: analog phone, fax, imprint machine
* Stand-alone POI device
* Network-isolated, Internet-connected POS devices
* Network-isolated virtual terminals
* P2PE solutions

Other considerations, especially for PCI DSS service providers, are detailed within the ‘TRA per SAQ type’ section below.

## Which Requirements? High View

I want you, fearless reader, to adeptly communicate TRAs to different audiences. For this reason, the following information is a summary for executives, and details supporting implementation are further down. I see you, TL;DR crowd!

There are 11 total PCI DSS controls summarized in the short table below. Keep reading for the full details and how to define the TRA process.

|  |  |
| --- | --- |
| Requirement | Does it apply? |
| 5.2.3.1 | This is applic...