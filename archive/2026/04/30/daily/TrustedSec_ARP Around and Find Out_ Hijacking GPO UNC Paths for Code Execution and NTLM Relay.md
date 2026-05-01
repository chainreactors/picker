---
title: ARP Around and Find Out: Hijacking GPO UNC Paths for Code Execution and NTLM Relay
url: https://trustedsec.com/blog/arp-around-and-find-out-hijacking-gpo-unc-paths-for-code-execution-and-ntlm-relay
source: TrustedSec
date: 2026-04-30
fetch_date: 2026-05-01T05:39:46.385759
---

# ARP Around and Find Out: Hijacking GPO UNC Paths for Code Execution and NTLM Relay

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
* [ARP Around and Find Out: Hijacking GPO UNC Paths for Code Execution and NTLM Relay](https://trustedsec.com/blog/arp-around-and-find-out-hijacking-gpo-unc-paths-for-code-execution-and-ntlm-relay)

April 30, 2026

# ARP Around and Find Out: Hijacking GPO UNC Paths for Code Execution and NTLM Relay

Written by
Austin Coontz

Active Directory Security Review

![](https://trusted-sec.transforms.svdcdn.com/production/images/Blog-Covers/ARPAroundAndFindOut_WebHero.jpg?w=320&h=320&q=90&auto=format&fit=crop&dm=1777310680&s=55d4457930fc94f38de1a6bfda520d6f)

Table of contents

* [Attack 1: WriteGPLink + MSI Deployment Spoofing](#Attack1)
* [Attack 2: Drive Map Spoofing + NTLM Capture and WebDAV Downgrade](#Attack2)
* [Attack 3: Logon Script Spoofing for Code Execution](#Attack3)
* [Beyond These Attacks](#Beyond)
* [Mitigations](#Mitigations)
* [Conclusion](#Conclusion)

Share

* Share URL
* [Share via Email](/cdn-cgi/l/email-protection#6c531f190e06090f18512f04090f07495e5c031918495e5c1804051f495e5c0d1e18050f0009495e5c0a1e0301495e5c381e191f1809083f090f495e5d4a0d011c570e030815512d3e3c495e5c2d1e03190208495e5c0d0208495e5c2a050208495e5c231918495f2d495e5c2405060d0f0705020b495e5c2b3c23495e5c39222f495e5c3c0d18041f495e5c0a031e495e5c2f030809495e5c2914090f1918050302495e5c0d0208495e5c22382021495e5c3e09000d15495f2d495e5c0418181c1f495f2d495e2a495e2a181e191f1809081f090f420f0301495e2a0e00030b495e2a0d1e1c410d1e03190208410d0208410a05020841031918410405060d0f0705020b410b1c034119020f411c0d18041f410a031e410f030809410914090f1918050302410d02084102180001411e09000d15 "Share via Email")
* [Share on Facebook](http://www.facebook.com/sharer.php?u=https%3A%2F%2Ftrustedsec.com%2Fblog%2Farp-around-and-find-out-hijacking-gpo-unc-paths-for-code-execution-and-ntlm-relay "Share on Facebook")
* [Share on X](http://twitter.com/share?text=ARP%20Around%20and%20Find%20Out%3A%20Hijacking%20GPO%20UNC%20Paths%20for%20Code%20Execution%20and%20NTLM%20Relay%3A%20https%3A%2F%2Ftrustedsec.com%2Fblog%2Farp-around-and-find-out-hijacking-gpo-unc-paths-for-code-execution-and-ntlm-relay "Share on X")
* [Share on LinkedIn](https://www.linkedin.com/shareArticle?url=https%3A%2F%2Ftrustedsec.com%2Fblog%2Farp-around-and-find-out-hijacking-gpo-unc-paths-for-code-execution-and-ntlm-relay&mini=true "Share on LinkedIn")

**TL;DR** - If you have ***WriteGPLink*** on an Active Directory Organizational Unit (OU) and you’re on the same network segment as a computer within that OU, you can abuse that permission to link an existing Group Policy Objects (GPO) with a software installation policy and ARP spoof the server it references, resulting in code execution as ***SYSTEM*** without modifying ***SYSVOL***. More broadly, GPOs that reference UNC paths for drive maps, logon scripts, and startup scripts can be redirected to an attacker-controlled host for NTLMv2 capture. Furthermore, by deliberately disrupting SMB sessions, authentication can be forced to fall back to WebDAV, which sends NTLM over HTTP that can be relayed to services like LDAP(S), AD CS, and SMB.

## Introduction

On engagements, it is common to find overly broad groups like ***Authenticated Users*** or ***Domain Computers*** with permissions over OUs that they were never intended to have. Whether it is left over from migration, a testing OU that never got cleaned up, or an AI-assisted auto-accept gone wrong, these misconfigurations frequently surface in ***BloodHound*** output. One (1) of the more interesting permissions that you may find is ***WriteGPLink***, which indicates the principal has permission to modify the ***gPLink*** attribute of the targeted OU/domain node. This alone does not let you edit the GPO itself or create a new one, but it does let you find existing GPOs in the domain and force them to apply to the objects inside that OU.

The concept of abusing GPO and OU relationships isn’t new. [wald0's foundational work on GPO attack primitives](https://wald0.com/?p=179) laid the groundwork, [WithSecure’s OU Having a Laugh](https://labs.withsecure.com/publications/ou-having-a-laugh) showed how OU attribute modification could be weaponized through rogue infrastructure, and Synacktiv’s [OUned.py](https://www.synacktiv.com/publications/ounedpy-exploiting-hidden-organizational-units-acl-attack-vectors-in-active-directory) provides automation for this style of abuse. The caveat is that these approaches usually depend on additional privileges such as creating machine accounts and adding DNS records. In tighter environments, those requirements may neutralize this path entirely.

Those limitations led to me to a different approach. Instead of building malicious GPO infrastructure from scratch, ***WriteGPLink*** could be abused by taking advantage of software deployments that already exist in the environment. If a legitimate GPO contained a ...