---
title: The Privileged Roles Nobody Talks About
url: https://trustedsec.com/blog/the-privileged-roles-nobody-talks-about
source: TrustedSec
date: 2026-06-04
fetch_date: 2026-06-05T06:14:05.853749
---

# The Privileged Roles Nobody Talks About

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
* [The Privileged Roles Nobody Talks About](https://trustedsec.com/blog/the-privileged-roles-nobody-talks-about)

June 04, 2026

# The Privileged Roles Nobody Talks About

Written by
Carlos Perez

Incident Response
Mobile Security Assessment

![](https://trusted-sec.transforms.svdcdn.com/production/images/Blog-Covers/StrykerAttackPrivilegeRoles_WebHero.jpg?w=320&h=320&q=90&auto=format&fit=crop&dm=1780421662&s=9d98cab4225c850c8d317ab652682fe7)

Table of contents

* [What Happens](#What)
* [The Real Lesson: Platform Admins are God-Tier Roles](#Real)
* [The Pattern That Keeps Repeating](#Pattern)
* [It’s Not Just Intune](#Not)
* [What You Should Be Doing for Intune, Right Now](#Should)
* [ATT&amp;amp;CK Technique Mapping](#Mapping)
* [If You Only Do Five Things](#Five)
* [The Bigger Picture](#Bigger)
* [Up Next: Part 2, the Implementation Guide](#Next)

Share

* Share URL
* [Share via Email](/cdn-cgi/l/email-protection#516e2224333b3432256c123934323a7463613e24257463612539382274636130232538323d3474636137233e3c7463610523242225343502343274636077303c216a333e35286c05393474636101233827383d34363435746361033e3d34227463611f3e333e352874636105303d3a2274636110333e24257462107463613925252122746210746317746317252324222534352234327f323e3c746317333d3e367463172539347c21233827383d343634357c233e3d34227c3f3e333e35287c25303d3a227c30333e2425 "Share via Email")
* [Share on Facebook](https://www.facebook.com/sharer.php?u=https%3A%2F%2Ftrustedsec.com%2Fblog%2Fthe-privileged-roles-nobody-talks-about "Share on Facebook")
* [Share on X](https://twitter.com/share?text=The%20Privileged%20Roles%20Nobody%20Talks%20About%3A%20https%3A%2F%2Ftrustedsec.com%2Fblog%2Fthe-privileged-roles-nobody-talks-about "Share on X")
* [Share on LinkedIn](https://www.linkedin.com/shareArticle?url=https%3A%2F%2Ftrustedsec.com%2Fblog%2Fthe-privileged-roles-nobody-talks-about&mini=true "Share on LinkedIn")

#### **Part 1: Why Your MDM Platform is a Tier 0 Asset**

*This is Part 1 of a two-part series on Intune security hardening. This post covers what we have seen in real world attacks as well as attack paths our Pentest Team has leveraged, why platform administration roles are systematically underprotected, and what controls you need in place. Part 2 (coming soon) covers the step-by-step implementation: configuration walkthroughs, decision flowcharts, and validation testing for each control.*

If you work in Incident Response long enough, you stop being surprised by the *how* of attacks and start paying more attention to the *why these types of attacks are possible in the first place*. When we perform leverage this attack path it makes every security team stop and rethink assumptions about what "privileged access" actually means in their environment. On-prem, we have seen the same, often with System Center Configuration Manager (SCCM) and other platforms, but now we see that with solutions with wipe capability they pose an even greater lower bar to cause malicious impact.

Let me break down what attackers have leveraged, why it matters beyond the headlines, and what the real operational takeaway is, especially if your organization relies on Microsoft Intune.

## What Happens

The attack vector we have started to see is a legitimate feature of the management platform, executed from a compromised privileged account. Intune in this case does exactly what it was designed to do. The failure we see often is in who had the keys and how those keys were protected.

![](https://trusted-sec.transforms.svdcdn.com/production/images/Blog-assets/PrivilegedRoles_CarlosP/Fig1_Carlos_MDMPlatformPt1.png?w=320&q=90&auto=format&fit=max&dm=1780420984&s=d56ec7e436b244d3ccc69710ca740c6d)

Figure 1 - Combined High-Fidelity Sentinel Analytics Rule

## The Real Lesson: Platform Admins are God-Tier Roles

This is where I want to focus, because this is the conversation the industry keeps avoiding.

When we talk about high-privilege roles in an environment, the usual suspects come up immediately: Domain Admins, Enterprise Admins, Tenant Global Admins, maybe your virtualization platform admins (vCenter, Hyper-V). These are the roles that make it into risk assessments, into tiered access models, into the conversations about Privileged Access Workstations and just-in-time elevation. We recommend this often to customers who have been victims of these types of attacks. To my surprise, there is always a level of pushback even after this has been abused and machines have been encrypted.

But here is what too many organizations miss: The people who administer your Mobile Device Management (MDM) platform, your configuration management tools, and your application deployment systems hold power over your infrastructure that is functionally equivalent to a Domain Admin. In many cases, it exceeds it.

Think about what an Intune admi...