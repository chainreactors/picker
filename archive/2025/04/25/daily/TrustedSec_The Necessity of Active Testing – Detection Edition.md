---
title: The Necessity of Active Testing – Detection Edition
url: https://trustedsec.com/blog/the-necessity-of-active-testing-detection-edition
source: TrustedSec
date: 2025-04-25
fetch_date: 2025-10-06T22:07:05.435588
---

# The Necessity of Active Testing – Detection Edition

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
* [The Necessity of Active Testing – Detection Edition](https://trustedsec.com/blog/the-necessity-of-active-testing-detection-edition)

April 24, 2025

# The Necessity of Active Testing – Detection Edition

Written by
Megan Nilsen

Purple Team Adversarial Detection & Countermeasures
Security Testing & Analysis

![](https://trusted-sec.transforms.svdcdn.com/production/images/Blog-Covers/ActiveTestingDetectionEdition_WebHero.jpg?w=320&h=320&q=90&auto=format&fit=crop&dm=1744902898&s=62191dfeaf5e1dc2eddf05edb89f9575)

Table of contents

* [Detection Engineering and Common Pitfalls](#Engineering)
* [The Solution - Active Testing and Purple Teaming](#Solution)
* [Conclusion](#Conclusion)

Share

* Share URL
* [Share via Email](/cdn-cgi/l/email-protection#9da2eee8fff7f8fee9a0def5f8fef6b8afadf2e8e9b8afade9f5f4eeb8afadfcefe9f4fef1f8b8afadfbeff2f0b8afadc9efe8eee9f8f9cef8feb8afacbbfcf0eda6fff2f9e4a0c9f5f8b8afadd3f8fef8eeeef4e9e4b8afadf2fbb8afaddcfee9f4ebf8b8afadc9f8eee9f4f3fab8afadb8d8afb8a5adb8a4aeb8afadd9f8e9f8fee9f4f2f3b8afadd8f9f4e9f4f2f3b8aedcb8afadf5e9e9edeeb8aedcb8afdbb8afdbe9efe8eee9f8f9eef8feb3fef2f0b8afdbfff1f2fab8afdbe9f5f8b0f3f8fef8eeeef4e9e4b0f2fbb0fcfee9f4ebf8b0e9f8eee9f4f3fab0f9f8e9f8fee9f4f2f3b0f8f9f4e9f4f2f3 "Share via Email")
* [Share on Facebook](http://www.facebook.com/sharer.php?u=https%3A%2F%2Ftrustedsec.com%2Fblog%2Fthe-necessity-of-active-testing-detection-edition "Share on Facebook")
* [Share on X](http://twitter.com/share?text=The%20Necessity%20of%20Active%20Testing%20%E2%80%93%20Detection%20Edition%3A%20https%3A%2F%2Ftrustedsec.com%2Fblog%2Fthe-necessity-of-active-testing-detection-edition "Share on X")
* [Share on LinkedIn](https://www.linkedin.com/shareArticle?url=https%3A%2F%2Ftrustedsec.com%2Fblog%2Fthe-necessity-of-active-testing-detection-edition&mini=true "Share on LinkedIn")

Most security teams understand the importance of log collection and building detections to provide early indicators of anomalous or potentially malicious activity. However, what is often forgotten is testing the detections to ensure they fire when the specified activity is generated. This blog post will discuss the value of actively testing detections, common pitfalls in failed detection triggering, and how purple teaming can assist in building better, higher fidelity detections.

## Detection Engineering and Common Pitfalls

Detection Research Engineering (DRE) has become a more prominent subsection of cyber security work in recent years as the emphasis on high-fidelity detections has grown. In general, though, having worked with organizations of all sizes, we see many common issues across enterprise security teams, including:

* Improperly tuning/baselining detections (out of the box or otherwise)
* Relying too much on tool-based detections/not properly evaluating detection logic (Gap Analysis)
* Overreliance on Endpoint Detection and Response (EDR) for endpoint-based detections
* Incorrect audit configurations for logging
* Broken system access control lists (SACLs)
* Security Information and Event Management (SIEM) parsing issues

### Tuning and Baselining Detections

Few enterprises have dedicated DRE teams that test and build detections internally.

This means that an overwhelming amount of DRE work takes place on the side of contracted Managed Security Service Providers (MSSPs) or out-of-the-box detections that are default to the organization's SIEM. While this is not a bad option, detections implemented in this fashion typically require significant tuning and adjustments that often are not performed by the parties involved. As a result, such detections are often disabled and/or over-tuned, filtering out potentially malicious activity that could occur.

### Tool vs Technique-Based Detections

In addition to issues with un-tuned detections, there is often a lack of consideration on how detections are actually detecting attacker Tactics, Techniques, and Procedures (TTPs). This typically manifests in the following forms:

* Detections are implemented with a tool-based focused and **NOT** on detecting underlying techniques.
* Detections are implemented without reviewing the logic to identify potential gaps.

Briefly, tool-based detections are typically built by leveraging certain functionalities of a specific tool, i.e., Mimikatz or Impacket, whereas technique-based detections use the underlying behavior of the attack and the artifacts that may be generated on a system.

Both detection methodologies have drawbacks. Tool-based detections can be evaded if tool signatures or code bases are changed (e.g., renaming Mimikatz); however, technique-ba...