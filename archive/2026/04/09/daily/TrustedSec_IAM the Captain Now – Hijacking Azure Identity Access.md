---
title: IAM the Captain Now – Hijacking Azure Identity Access
url: https://trustedsec.com/blog/iam-the-captain-now-hijacking-azure-identity-access
source: TrustedSec
date: 2026-04-09
fetch_date: 2026-04-10T04:47:33.019079
---

# IAM the Captain Now – Hijacking Azure Identity Access

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
* [IAM the Captain Now – Hijacking Azure Identity Access](https://trustedsec.com/blog/iam-the-captain-now-hijacking-azure-identity-access)

April 09, 2026

# IAM the Captain Now – Hijacking Azure Identity Access

Written by
Justin Mahon

Vulnerability Assessment
Cloud Penetration Testing

![](https://trusted-sec.transforms.svdcdn.com/production/images/Blog-Covers/IAMtheCaptainNow_WebHero.jpg?w=320&h=320&q=90&auto=format&fit=crop&dm=1775570349&s=5b43d7689dfd0a95075d1372df8410be)

Table of contents

* [Lab Setup](#Setup)
* [RoleAssignment/Write Demo Time 👽](#Demo)
* [RoleDefinition/Write and RoleAssignment/Write](#Role)
* [FIC/Write](#Federated)

Share

* Share URL
* [Share via Email](/cdn-cgi/l/email-protection#152a6660777f70766128567d70767e3027257a6061302725617d7c663027257467617c76797030272573677a7830272541676066617071467076302724337478652e777a716c285c5458302725617d7030272556746561747c7b3027255b7a62302725305027302d25302c263027255d7c7f74767e7c7b72302725546f6067703027255c71707b617c616c3027255476767066663026543027257d61616566302654302753302753616760666170716670763b767a7830275377797a723027537c747838617d703876746561747c7b387b7a62387d7c7f74767e7c7b7238746f606770387c71707b617c616c38747676706666 "Share via Email")
* [Share on Facebook](http://www.facebook.com/sharer.php?u=https%3A%2F%2Ftrustedsec.com%2Fblog%2Fiam-the-captain-now-hijacking-azure-identity-access "Share on Facebook")
* [Share on X](http://twitter.com/share?text=IAM%20the%20Captain%20Now%20%E2%80%93%20Hijacking%20Azure%20Identity%20Access%3A%20https%3A%2F%2Ftrustedsec.com%2Fblog%2Fiam-the-captain-now-hijacking-azure-identity-access "Share on X")
* [Share on LinkedIn](https://www.linkedin.com/shareArticle?url=https%3A%2F%2Ftrustedsec.com%2Fblog%2Fiam-the-captain-now-hijacking-azure-identity-access&mini=true "Share on LinkedIn")

I decided to spend some research time diving in depth into Identity and Access Management (IAM) within Microsoft Azure. I am going to show you within this blog how IAM permissions can be abused within an Azure environment. From seeing these misconfigurations on real engagements to understanding them through the [HackTricks Azure Red Team Expert (AzRTE) course](https://training.hacktricks.xyz/courses/azrte), it’s clear that IAM permissions can be dangerous if not fully understood.

First I will walk through my lab setup so others can set this up on their own, and I'll demonstrate how an attacker can exploit these permissions to escalate their privileges in an Azure environment.

As a side note: I did learn a TON of information and methods from the HackTricks AzRTE cloud course. I highly recommend looking into their cloud courses as they are the best that I've tried at the time of this blog.

![](https://trusted-sec.transforms.svdcdn.com/production/images/Blog-assets/IAMtheCaptain_Mahon/FigA_Mahon_IAM.png?w=320&q=90&auto=format&fit=max&dm=1775568997&s=b9fba4e462943bb7f29ad4ccee0e378d)

In cloud environments, IAM is used to control who can do what to which resources. It’s built on the core of RBAC (Role-Based Access Control). You can get a plethora of permissions from a pre-made role from Microsoft, or you can assign a custom role with custom permissions.

The following IAM permissions will allow privilege escalation in Azure:

* ***Roleassignment/Write*** assigns privileged roles.
* ***Roledefinition/Write*** creates roles and associated permissions.
* ***FederatedIdentityCredentials/Write*** creates or updates Federated Identity Credentials (FICs).

I demonstrated this lab to highlight how a misconfiguration or a misunderstanding of a role/permission can lead to a risky cloud security posture. It’s vital to highlight the dangers and consequences of privileges and to know exactly what can be done with them.

## Lab Setup

For this demo, we are going to create a custom role. For each demonstrated user we will assign the privileged role permission.

We are going to jump into creating the custom roles and their permissions used for this lab. Start off with creating an account in Azure and making your own tenant. You will then want to create your own subscription and user(s) or service principal(s) to assign permissions to.

Once this is complete…

You’ll want to go to: your subscription → go to IAM → and add custom role.

![](https://trusted-sec.transforms.svdcdn.com/production/images/Blog-assets/IAMtheCaptain_Mahon/Fig01_Mahon_IAM.png?w=320&q=90&auto=format&fit=max&dm=1775499701&s=0b4be05b0a6b036def2d7e83e0ddad29)

Figure 1 - IAM on Subscription

You will then create a custom role with the custom permissions you want. The role name does not matter.

![](https://trusted-sec.transforms.svdcdn.com/production/images/Blog-assets/IAMtheCaptain_Mahon/Fig02_Mahon_IAM.png?w=320&q=90&auto=format&fit=max&dm=1775499703&s=175d466cc936047d31ff82234a8c15b3)

Figure 2 - Cre...