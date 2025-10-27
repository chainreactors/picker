---
title: Hiding in the Shadows: Covert Tunnels via QEMU Virtualization
url: https://trustedsec.com/blog/hiding-in-the-shadows-covert-tunnels-via-qemu-virtualization
source: TrustedSec
date: 2025-07-18
fetch_date: 2025-10-06T23:54:51.654447
---

# Hiding in the Shadows: Covert Tunnels via QEMU Virtualization

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
* [Hiding in the Shadows: Covert Tunnels via QEMU Virtualization](https://trustedsec.com/blog/hiding-in-the-shadows-covert-tunnels-via-qemu-virtualization)

July 17, 2025

# Hiding in the Shadows: Covert Tunnels via QEMU Virtualization

Written by
Caroline Fenstermacher

Incident Response
Social Engineering

![](https://trusted-sec.transforms.svdcdn.com/production/images/Blog-Covers/HidingInTheShadows_WebHero.jpg?w=320&h=320&q=90&auto=format&fit=crop&dm=1752243066&s=5bdac0b85c0effdd7de35ad4b8cd20d0)

Table of contents

* [Initial Access](#Access)
* [QEMU VM Deployment](#Qemu)
* [SSH Backdoor Attempts](#SSH)
* [Remediation and Prevention](#Remediation)
* [IOCs](#IOCs)

Share

* Share URL
* [Share via Email](/cdn-cgi/l/email-protection#b38cc0c6d1d9d6d0c78ef0dbd6d0d8968183dcc6c7968183c7dbdac0968183d2c1c7dad0dfd6968183d5c1dcde968183e7c1c6c0c7d6d7e0d6d096818295d2dec388d1dcd7ca8efbdad7daddd4968183dadd968183c7dbd6968183e0dbd2d7dcc4c09680f2968183f0dcc5d6c1c7968183e7c6ddddd6dfc0968183c5dad2968183e2f6fee6968183e5dac1c7c6d2dfdac9d2c7dadcdd9680f2968183dbc7c7c3c09680f29681f59681f5c7c1c6c0c7d6d7c0d6d09dd0dcde9681f5d1dfdcd49681f5dbdad7daddd49edadd9ec7dbd69ec0dbd2d7dcc4c09ed0dcc5d6c1c79ec7c6ddddd6dfc09ec5dad29ec2d6dec69ec5dac1c7c6d2dfdac9d2c7dadcdd "Share via Email")
* [Share on Facebook](http://www.facebook.com/sharer.php?u=https%3A%2F%2Ftrustedsec.com%2Fblog%2Fhiding-in-the-shadows-covert-tunnels-via-qemu-virtualization "Share on Facebook")
* [Share on X](http://twitter.com/share?text=Hiding%20in%20the%20Shadows%3A%20Covert%20Tunnels%20via%20QEMU%20Virtualization%3A%20https%3A%2F%2Ftrustedsec.com%2Fblog%2Fhiding-in-the-shadows-covert-tunnels-via-qemu-virtualization "Share on X")
* [Share on LinkedIn](https://www.linkedin.com/shareArticle?url=https%3A%2F%2Ftrustedsec.com%2Fblog%2Fhiding-in-the-shadows-covert-tunnels-via-qemu-virtualization&mini=true "Share on LinkedIn")

Attackers are getting increasingly creative—not just with their payloads, but with how they deliver and operate them. In a recent Incident Response engagement, TrustedSec investigated a case involving an attacker who used a combination of social engineering, remote support tools, and virtual machine (VM) deployment to gain access to a corporate endpoint and attempt covert communications. What started as a Microsoft Teams vishing attack escalated into an intrusion involving Qemu-based Tiny Core Linux virtual machines and an attempted reverse SSH tunnel. Though not highly sophisticated, this engagement highlighted how virtualization can be used to avoid host-based detection such as EDR and AV tools as well as the effectiveness of social engineering.

## Initial Access

This intrusion started as a well-executed vishing attempt. A user was contacted via Microsoft Teams by someone claiming to be from their IT support team. This “support tech” was actually coming from an external Microsoft 365 tenant, and thanks to Team’s default settings, external communication was allowed.

Once the call started, the threat actor instructed the user to open Quick Assist, which is a native Windows feature that allows for interactive remote management of endpoints by relying on Remote Desktop Protocol (RDP). Essentially, this is a built-in remote monitoring and management (RMM) tool, much like familiar third-party options, such as: AnyDesk, Atera, TeamViewer, etc. The threat actor then instructed the user to download Zoho Meeting, another remote management tool. Often, attackers will place several different RMM tools on a host to have a better chance at persistence in case one is discovered and removed.

After opening the Quick Assist session, the threat actor instructed the user to run a `curl` command to download a ZIP file from an attacker-controlled IP address. Due to a lack of telemetry, TrustedSec was not able to capture this command; however, the process execution of the ***curl.exe*** process was captured, followed by the introduction of ***updqem.zip*** to the file system.

Leveraging the access the attacker had gained via Quick Assist, the following file extraction command was captured within the host’s ***ConsoleHost\_history.txt*** file:

![](https://trusted-sec.transforms.svdcdn.com/production/images/Blog-assets/HidingCovertTunnelsQemu_Caroline/Fig01_CarolineF_HidingQemu.png?w=320&q=90&auto=format&fit=max&dm=1752244765&s=b9b5d06bdd822bf63b175e36d80fb85e)

Figure 1 - Console Host History

Over the course of one (1) week, the threat actor attacker contacted the user twice. Several days after the initial contact to the user, the threat actor contacted the user to inform them that the “IT support steps...