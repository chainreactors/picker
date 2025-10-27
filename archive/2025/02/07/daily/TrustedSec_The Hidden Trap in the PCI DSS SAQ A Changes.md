---
title: The Hidden Trap in the PCI DSS SAQ A Changes
url: https://trustedsec.com/blog/the-hidden-trap-in-the-pci-dss-saq-a-changes
source: TrustedSec
date: 2025-02-07
fetch_date: 2025-10-06T20:38:11.535252
---

# The Hidden Trap in the PCI DSS SAQ A Changes

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
* [The Hidden Trap in the PCI DSS SAQ A Changes](https://trustedsec.com/blog/the-hidden-trap-in-the-pci-dss-saq-a-changes)

March 04, 2025

# The Hidden Trap in the PCI DSS SAQ A Changes

Written by
Chris Camejo

Information Security Compliance
PCI DSS

![](https://trusted-sec.transforms.svdcdn.com/production/images/Blog-Covers/TheHiddenTrap_WebHero.jpg?w=320&h=320&q=90&auto=format&fit=crop&dm=1741532430&s=b0a2d9ca12cddec74b9dfb16bf85767a)

Table of contents

* [Another Guidance Update (March 10, 2025)](#AnotherGuidance)
* [Guidance Update (March 04, 2025)](#GuidanceUpdate)
* [Applicability](#Applicability)
* [The Change](#Change)
* [Solutions](#Solutions)
* [Implementing Requirements 6.4.3 and 11.6.1](#Implementing)
* [Next Steps](#Next)

Share

* Share URL
* [Share via Email](/cdn-cgi/l/email-protection#e9d69a9c8b838c8a9dd4aa818c8a82ccdbd9869c9dccdbd99d81809accdbd9889b9d808a858cccdbd98f9b8684ccdbd9bd9b9c9a9d8c8dba8c8accdbd8cf888499d28b868d90d4bd818cccdbd9a1808d8d8c87ccdbd9bd9b8899ccdbd98087ccdbd99d818cccdbd9b9aaa0ccdbd9adbabaccdbd9baa8b8ccdbd9a8ccdbd9aa8188878e8c9accdaa8ccdbd9819d9d999accdaa8ccdbafccdbaf9d9b9c9a9d8c8d9a8c8ac78a8684ccdbaf8b85868eccdbaf9d818cc481808d8d8c87c49d9b8899c48087c49d818cc4998a80c48d9a9ac49a8898c488c48a8188878e8c9a "Share via Email")
* [Share on Facebook](http://www.facebook.com/sharer.php?u=https%3A%2F%2Ftrustedsec.com%2Fblog%2Fthe-hidden-trap-in-the-pci-dss-saq-a-changes "Share on Facebook")
* [Share on X](http://twitter.com/share?text=The%20Hidden%20Trap%20in%20the%20PCI%20DSS%20SAQ%20A%20Changes%3A%20https%3A%2F%2Ftrustedsec.com%2Fblog%2Fthe-hidden-trap-in-the-pci-dss-saq-a-changes "Share on X")
* [Share on LinkedIn](https://www.linkedin.com/shareArticle?url=https%3A%2F%2Ftrustedsec.com%2Fblog%2Fthe-hidden-trap-in-the-pci-dss-saq-a-changes&mini=true "Share on LinkedIn")

The Payment Card Industry Security Standards Council (PCI SSC) just announced a [change to Self Assessment Questionnaire A (SAQ A)](https://blog.pcisecuritystandards.org/important-updates-announced-for-merchants-validating-to-self-assessment-questionnaire-a). The change eliminates two (2) requirements relevant to eCommerce sites, 6.4.3 and 11.6.1, that are designed to prevent and detect tampering with payment page scripts. While this appears to make compliance easier, and SAQ A eCommerce merchants may be celebrating this change, there's a catch: a new line in the eligibility criteria needs to be met to qualify for SAQ A, and failure to meet this requirement could drastically increase the number of applicable requirements.

For any merchant with a payment channel that they intended to assess using SAQ A, TrustedSec recommends using one (1) or more of the following options to remain eligible:

* Implement requirements 6.4.3 and 11.6.1 as if this change was never made.
* Get assurances from the processor that their iFrame is not susceptible to script-based attacks when installed properly.
* Develop and implement an alternative method of confirming that the eCommerce site is not susceptible to attacks from scripts, for example:
  + Conduct web application testing specifically to demonstrate that malicious insertion of or tampering with scripts is not feasible on the eCommerce site.
  + Deploy and configure a Web Application Firewall (WAF) to protect the site from script-based attacks.

Read on for more details on which organizations are affected, the nuances of the change, and the potential solutions.

## Another Guidance Update (March 10, 2025)

PCI SSC [released](https://blog.pcisecuritystandards.org/new-information-supplement-payment-page-security-and-preventing-e-skimming "https://blog.pcisecuritystandards.org/new-information-supplement-payment-page-security-and-preventing-e-skimming") an [information supplement](https://docs-prv.pcisecuritystandards.org/PCI%20DSS/Supporting%20Document/Guidance-for-PCI-DSS-Requirements-6_4_3-and-11_6_1.pdf "https://docs-prv.pcisecuritystandards.org/PCI%20DSS/Supporting%20Document/Guidance-for-PCI-DSS-Requirements-6_4_3-and-11_6_1.pdf") with more requirement 6.4.3 and 11.6.1 guidance on March 10, 2025. This additional guidance does not change our understanding of requirements 6.4.3 and 11.6.1 or the advice given in this post but offers some more helpful information that organizations implementing these requirements should review. No further updates to this post have been made because of the new guidance.

## Guidance Update (March 04, 2025)

PCI SSC released [FAQ 1588](https://www.pcisecuritystandards.org/faq/articles/Frequently_Asked_Question/how-does-an-e-commerce-merchant-meet-the-saq-a-eligibility-criteria-fo...