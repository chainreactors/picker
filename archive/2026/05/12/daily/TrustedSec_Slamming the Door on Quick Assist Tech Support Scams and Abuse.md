---
title: Slamming the Door on Quick Assist Tech Support Scams and Abuse
url: https://trustedsec.com/blog/slamming-the-door-on-quick-assist-tech-support-scams-and-abuse
source: TrustedSec
date: 2026-05-12
fetch_date: 2026-05-13T05:47:13.871802
---

# Slamming the Door on Quick Assist Tech Support Scams and Abuse

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
* [Slamming the Door on Quick Assist Tech Support Scams and Abuse](https://trustedsec.com/blog/slamming-the-door-on-quick-assist-tech-support-scams-and-abuse)

May 12, 2026

# Slamming the Door on Quick Assist Tech Support Scams and Abuse

Written by
Thomas Millar

Social Engineering
Incident Response

![](https://trusted-sec.transforms.svdcdn.com/production/images/Blog-Covers/SlammingTheDoorQuickAssist_WebHero.jpg?w=320&h=320&q=90&auto=format&fit=crop&dm=1778075623&s=4337acc25d1b2a9964925dc21d80a6b4)

Share

* Share URL
* [Share via Email](/cdn-cgi/l/email-protection#1c236f697e76797f68215f74797f77392e2c736968392e2c6874756f392e2c7d6e68757f7079392e2c7a6e7371392e2c486e696f6879784f797f392e2d3a7d716c277e737865214f707d717175727b392e2c687479392e2c5873736e392e2c7372392e2c4d69757f77392e2c5d6f6f756f68392e2c48797f74392e2c4f696c6c736e68392e2c4f7f7d716f392e2c7d7278392e2c5d7e696f79392f5d392e2c7468686c6f392f5d392e5a392e5a686e696f6879786f797f327f7371392e5a7e70737b392e5a6f707d717175727b31687479317873736e317372316d69757f77317d6f6f756f683168797f74316f696c6c736e68316f7f7d716f317d7278317d7e696f79 "Share via Email")
* [Share on Facebook](http://www.facebook.com/sharer.php?u=https%3A%2F%2Ftrustedsec.com%2Fblog%2Fslamming-the-door-on-quick-assist-tech-support-scams-and-abuse "Share on Facebook")
* [Share on X](http://twitter.com/share?text=Slamming%20the%20Door%20on%20Quick%20Assist%20Tech%20Support%20Scams%20and%20Abuse%3A%20https%3A%2F%2Ftrustedsec.com%2Fblog%2Fslamming-the-door-on-quick-assist-tech-support-scams-and-abuse "Share on X")
* [Share on LinkedIn](https://www.linkedin.com/shareArticle?url=https%3A%2F%2Ftrustedsec.com%2Fblog%2Fslamming-the-door-on-quick-assist-tech-support-scams-and-abuse&mini=true "Share on LinkedIn")

Over the past month or so, I've worked a number of Incident Response engagements that in some way dealt with social engineering attack vectors. Sure, there are the Business Email Compromise (BEC) situations that end up coming our way that dig into the Microsoft 365 tenant, reviewing all the logs and ultimately discovering what happened and to whom. However, with the success of ClickFix threat campaigns, we have seen an uptick in cases that have started with the use of social engineered “tech support”.

This blog focuses on the Windows 10 and 11 provided tool Quick Assist. Quick Assist is a remote monitoring and management (RMM) utility that allows remote assistance. There are two (2) versions of Quick Assist, which can be identified by where they live on a Windows endpoint.

| **Version** | **Location / Attribute** |
| --- | --- |
| Older edition | Present within **C:\Windows\System32\** |
| Newer edition | Present within **C:\ProgramFiles\WindowsApps\MicrosoftCorporationII.QuickAssist\_<VERSIONVALUE>\_\_8wekyb3d8bbwe\** |

The newer editions of Quick Assist have greater logging features, so if that is present, you can take advantage of more useful pieces of evidence when you have to investigate

In many cases, the attack starts with a series of phishing messages received by unsuspecting users, which after those are sent they are followed up by an unsolicited call through Microsoft Teams. The attacker *claims to work in IT* and is working to do something about the phishing messages. This marks when the attacker posing as a "helper" makes contact as an initial step.

It’s important to note that the selection of Microsoft applications is deliberate because the attackers know they can expect the following:

* Teams is likely to be used and available anywhere a Microsoft Windows endpoint is used
* Quick Assist is included and enabled by default on Windows 10 and 11 workstations and laptops
* The barrage of phishing emails immediately before the Teams call artificially creates a problem to be solved and a sense of urgency, increasing the odds that the user will accept the Teams call and agree to take part in the Quick Assist session

Below are three (3) URLs that can be used for detection across the enterprise and have to do with outbound (egress) requests to legitimate Microsoft infrastructure:

| **URL** | **Description** |
| --- | --- |
| https[:]//remoteassistance.support.services.microsoft[.]com/roleselection | Quick Assist Session Starts |
| https[:]//remoteassistance.support.services.microsoft[.]com/screenshare | Quick Assist Session Screenshare Begins |
| https[:]//remoteassistance.support.services.microsoft[.]com/status/ended | Quick Assist Session Ends |

The URL ending with ***roleselection*** represents the official start of the Quick Assist RMM session. The session is initiated, and the user is presented with a prompt to enter a temporary 6-digit session value, which the attacker provides.

The next URL has to do with the screensharing feature being enabled and started; at this point, the attacker has the ability to see...