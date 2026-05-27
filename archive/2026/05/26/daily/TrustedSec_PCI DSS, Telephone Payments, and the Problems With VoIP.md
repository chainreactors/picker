---
title: PCI DSS, Telephone Payments, and the Problems With VoIP
url: https://trustedsec.com/blog/pci-dss-telephone-payments-and-the-problems-with-voip
source: TrustedSec
date: 2026-05-26
fetch_date: 2026-05-27T06:12:32.923446
---

# PCI DSS, Telephone Payments, and the Problems With VoIP

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
* [PCI DSS, Telephone Payments, and the Problems With VoIP](https://trustedsec.com/blog/pci-dss-telephone-payments-and-the-problems-with-voip)

May 26, 2026

# PCI DSS, Telephone Payments, and the Problems With VoIP

Written by
Chris Camejo

PCI DSS

![](https://trusted-sec.transforms.svdcdn.com/production/images/Blog-Covers/PCIDSSTelephoneVoIP_WebHero.jpg?w=320&h=320&q=90&auto=format&fit=crop&dm=1778076383&s=5b3c4fa1ad070ccfdab6002af4fb057d)

Table of contents

* [The Interpretation](#Interpretation)
* [Options to Maintain Compliance](#Compliance)
* [QSA Gripes and A Way Forward](#QSA)

Share

* Share URL
* [Share via Email](/cdn-cgi/l/email-protection#a897dbddcac2cdcbdc95ebc0cdcbc38d9a98c7dddc8d9a98dcc0c1db8d9a98c9dadcc1cbc4cd8d9a98cedac7c58d9a98fcdadddbdccdccfbcdcb8d9a998ec9c5d893cac7ccd195f8ebe18d9a98ecfbfb8d9aeb8d9a98fccdc4cdd8c0c7c6cd8d9a98f8c9d1c5cdc6dcdb8d9aeb8d9a98c9c6cc8d9a98dcc0cd8d9a98f8dac7cac4cdc5db8d9a98ffc1dcc08d9a98fec7e1f88d9be98d9a98c0dcdcd8db8d9be98d9aee8d9aeedcdadddbdccdccdbcdcb86cbc7c58d9aeecac4c7cf8d9aeed8cbc185ccdbdb85dccdc4cdd8c0c7c6cd85d8c9d1c5cdc6dcdb85c9c6cc85dcc0cd85d8dac7cac4cdc5db85dfc1dcc085dec7c1d8 "Share via Email")
* [Share on Facebook](https://www.facebook.com/sharer.php?u=https%3A%2F%2Ftrustedsec.com%2Fblog%2Fpci-dss-telephone-payments-and-the-problems-with-voip "Share on Facebook")
* [Share on X](https://twitter.com/share?text=PCI%20DSS%2C%20Telephone%20Payments%2C%20and%20the%20Problems%20With%20VoIP%3A%20https%3A%2F%2Ftrustedsec.com%2Fblog%2Fpci-dss-telephone-payments-and-the-problems-with-voip "Share on X")
* [Share on LinkedIn](https://www.linkedin.com/shareArticle?url=https%3A%2F%2Ftrustedsec.com%2Fblog%2Fpci-dss-telephone-payments-and-the-problems-with-voip&mini=true "Share on LinkedIn")

Merchants have been accepting payment cards over telephones for a long time, but changing interpretations of VoIP guidance have led to confusion about which PCI DSS requirements apply to telephone-based payment channels. Merchants that have used SAQ C-VT or P2PE to reduce the number of PCI DSS requirements that apply to telephone payment channels are discovering that they cannot use and benefit from these SAQs if they collect payments over VoIP.

Merchants typically encounter this issue when additional requirements appear in the annual PCI DSS compliance attestation web form provided by their processor after answering 'Yes' to a question about the use of VoIP. Merchants may also encounter this issue when their transaction volumes increase to the point that they can no longer self-assess and are informed by a QSA that they have been incorrectly applying the PCI DSS SAQ C-VT or P2PE to their telephone payment channel.

This post explains who is affected by the VoIP guidance interpretation, where this interpretation comes from, and how merchants can reduce the number of PCI DSS requirements applicable to their telephone-based payment channels and be prepared for their next assessment (with some QSA gripes along the way).

TrustedSec has long worked to move its clients into compliance with the PCI SSC guidance around how telephone payments via VoIP must be scoped and assessed and can assist other merchants struggling with this issue. If you need assistance with this, [get in touch with us!](https://trustedsec.com/contact)

## Who This Applies To

This issue applies to merchants using eligibility for PCI SAQ C-VT or P2PE to reduce the number of PCI DSS requirements applicable to a telephone-based payment channel when payment card account data is received over VoIP. This includes merchants that complete a ROC but use eligibility for SAQ C-VT or P2PE to determine the applicable controls within the ROC, as per [PCI SSC FAQ 1331](https://www.pcisecuritystandards.org/faq/articles/Frequently_Asked_Question/can-saq-eligibility-criteria-be-used-as-a-guide-for-determining-applicability-of-pci-dss-requirements-for-merchant-assessments-documented-in-a-report-on-compliance/).

Merchants that attest to PCI DSS compliance via a guided questionnaire on their processor’s website may not be aware of which SAQ they are effectively using. Behind the scenes, the first few questions in these forms are usually used to determine which SAQ applies to the merchant, and the remaining questions are based on the requirements in applicable SAQ.

The following list can be used by merchants to determine which SAQ their processor has likely been applying to them and how many requirements to expect compared to the full set of 236 PCI DSS merchant requirements (not including the rarely used appendices). Note that all SAQ types are included in this list to help merchants identify which may be applied, but only SAQs C-VT and P2PE are subject to the VoIP issue described in this post.

| **SAQ** | **Requirements** | **Use Case** |
| --- | --- | --...