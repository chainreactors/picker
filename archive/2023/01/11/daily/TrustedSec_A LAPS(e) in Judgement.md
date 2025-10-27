---
title: A LAPS(e) in Judgement
url: https://www.trustedsec.com/blog/a-lapse-in-judgement/
source: TrustedSec
date: 2023-01-11
fetch_date: 2025-10-04T03:33:01.592823
---

# A LAPS(e) in Judgement

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
* [A LAPS(e) in Judgement](https://trustedsec.com/blog/a-lapse-in-judgement)

January 10, 2023

# A LAPS(e) in Judgement

Written by
Megan Nilsen

![](https://trusted-sec.transforms.svdcdn.com/production/images/Blog-Covers/LAPSe_WebHero.jpg?w=320&h=320&q=90&auto=format&fit=crop&dm=1695566746&s=9b3c56fabd52349fd6665994853fd16b)

Share

* Share URL
* [Share via Email](/cdn-cgi/l/email-protection#ac93dfd9cec6c9cfd891efc4c9cfc7899e9cc3d9d8899e9cd8c4c5df899e9ccdded8c5cfc0c9899e9ccadec3c1899e9cf8ded9dfd8c9c8ffc9cf899e9d8acdc1dc97cec3c8d591ed899e9ce0edfcff899e94c9899e95899e9cc5c2899e9ce6d9c8cbc9c1c9c2d8899fed899e9cc4d8d8dcdf899fed899eea899eead8ded9dfd8c9c8dfc9cf82cfc3c1899eeacec0c3cb899eeacd81c0cddcdfc981c5c281c6d9c8cbc9c1c9c2d8 "Share via Email")
* [Share on Facebook](http://www.facebook.com/sharer.php?u=https%3A%2F%2Ftrustedsec.com%2Fblog%2Fa-lapse-in-judgement "Share on Facebook")
* [Share on X](http://twitter.com/share?text=A%20LAPS%28e%29%20in%20Judgement%3A%20https%3A%2F%2Ftrustedsec.com%2Fblog%2Fa-lapse-in-judgement "Share on X")
* [Share on LinkedIn](https://www.linkedin.com/shareArticle?url=https%3A%2F%2Ftrustedsec.com%2Fblog%2Fa-lapse-in-judgement&mini=true "Share on LinkedIn")

As security practitioners, we live in a time where there is an abundance of tools and solutions to help us secure our homes, organizations, and critical data. We know the dangers of unpatched applications and devices as well as the virtues of things like password managers and encrypted databases to protect our passwords and other sensitive information.

However, we often forget that these tools, while helpful and no doubt beneficial, are subject to the same attacks as other applications. As practitioners, we should ensure we are building out both engineering protections and security detections that protect those tools in the same way we do for the rest of our environment.

## 1.1     Overview

This blog will focus on one such tool—Microsoft LAPS—and how we can build Splunk SPL queries for detecting the attacks described using Windows Security Log events from a domain controller.

## 1.2     What is LAPS?

Microsoft LAPS (Local Administrator Password Solution) is a Windows native tool used to manage local **Administrator** accounts within an AD domain.

To keep things simple, instead of requiring an administrator to manually set, rotate, and store the local **Administrator** passwords, LAPS will do this automatically while providing an easy interface for authorized users to access passwords for recovery and/or other admin-related tasks.

The benefits to an organization here are obvious—automate and protect a well-known critical security challenge and free up IT resources on your team.

However, the fact that LAPS has so much information means that it provides a potential avenue of attack for malicious actors looking to further compromise an environment. If LAPS isn't properly locked down, an organization can inadvertently allow anybody to grab local **Admin** powers on a given machine. That alone makes logging the telemetry worthwhile.

## 1.3     Building your LAPS Lab

One of the major advantages of LAPS is that it is quick and easy (and free!) to install and can automatically be deployed to workstations and servers on a domain through GPO.

[This guide](https://techcommunity.microsoft.com/t5/itops-talk-blog/step-by-step-guide-how-to-configure-microsoft-local/ba-p/2806185#:~:text=Installing%20Microsoft%20LAPS%201%201.%20Download%20Microsoft%20LAPS,select%20%E2%80%9C%20Management%20Tools%20%E2%80%9D.%20...%20More%20items) does a great job at walking you through the install process and getting some initial configuration done.

## 1.4     Enhancing Logging

There are a couple of things that must be done to generate the logs you need for the detections we will build.

First, ensure Event ID 4662 is logging 'Success' and 'Fail':

***Group Policy Editor > Policies > Windows Settings > Security Settings > Advanced Audit Policy Configuration > Audit Policies > DS Access***

![](https://www.trustedsec.com/wp-content/uploads/2023/01/Nilsen_FIGURE-1.png)

The second thing we need to do is enable logging for the objects that we will look for and use in our LAPS detection. There are a few ways to do this, but if you are running a lab environment, I would recommend enabling auditing for ALL objects:

![](https://www.trustedsec.com/wp-content/uploads/2023/01/Nilsen_FIGURE-2.png)

Figure 2 - Adding Object Auditing for All Objects - Part 1

![](https://www.trustedsec.com/wp-content/uploads/2023/01/Nilsen_FIGURE-3.png)

Figure 3 - Adding Object Auditing for All Objects - Part 2

...