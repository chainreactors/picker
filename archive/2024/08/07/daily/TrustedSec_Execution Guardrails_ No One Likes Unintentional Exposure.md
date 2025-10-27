---
title: Execution Guardrails: No One Likes Unintentional Exposure
url: https://trustedsec.com/blog/execution-guardrails-no-one-likes-unintentional-exposure
source: TrustedSec
date: 2024-08-07
fetch_date: 2025-10-06T18:04:53.214656
---

# Execution Guardrails: No One Likes Unintentional Exposure

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
* [Execution Guardrails: No One Likes Unintentional Exposure](https://trustedsec.com/blog/execution-guardrails-no-one-likes-unintentional-exposure)

August 06, 2024

# Execution Guardrails: No One Likes Unintentional Exposure

Written by
Brandon McGrath

Red Team Adversarial Attack Simulation

![](https://trusted-sec.transforms.svdcdn.com/production/images/Blog-Covers/ExecutionGuardrails_WebHero.jpg?w=320&h=320&q=90&auto=format&fit=crop&dm=1721828926&s=76109ae96331d090af029357fe430cfc)

Table of contents

* [1.1 Introduction](#Introduction)
* [1.2 The Multi-Step Process](#Process)
* [1.3 Local Machine](#Local)
* [1.4 Network Keying](#Network)
* [1.5 External Resources](#External)
* [1.6 Payload Design](#Payload)
* [1.7 Conclusion](#Conclusion)

Share

* Share URL
* [Share via Email](/cdn-cgi/l/email-protection#c0ffb3b5a2aaa5a3b4fd83a8a5a3abe5f2f0afb5b4e5f2f0b4a8a9b3e5f2f0a1b2b4a9a3aca5e5f2f0a6b2afade5f2f094b2b5b3b4a5a493a5a3e5f2f1e6a1adb0fba2afa4b9fd85b8a5a3b5b4a9afaee5f2f087b5a1b2a4b2a1a9acb3e5f381e5f2f08eafe5f2f08faea5e5f2f08ca9aba5b3e5f2f095aea9aeb4a5aeb4a9afaea1ace5f2f085b8b0afb3b5b2a5e5f381e5f2f0a8b4b4b0b3e5f381e5f286e5f286b4b2b5b3b4a5a4b3a5a3eea3afade5f286a2acafa7e5f286a5b8a5a3b5b4a9afaeeda7b5a1b2a4b2a1a9acb3edaeafedafaea5edaca9aba5b3edb5aea9aeb4a5aeb4a9afaea1aceda5b8b0afb3b5b2a5 "Share via Email")
* [Share on Facebook](http://www.facebook.com/sharer.php?u=https%3A%2F%2Ftrustedsec.com%2Fblog%2Fexecution-guardrails-no-one-likes-unintentional-exposure "Share on Facebook")
* [Share on X](http://twitter.com/share?text=Execution%20Guardrails%3A%20No%20One%20Likes%20Unintentional%20Exposure%3A%20https%3A%2F%2Ftrustedsec.com%2Fblog%2Fexecution-guardrails-no-one-likes-unintentional-exposure "Share on X")
* [Share on LinkedIn](https://www.linkedin.com/shareArticle?url=https%3A%2F%2Ftrustedsec.com%2Fblog%2Fexecution-guardrails-no-one-likes-unintentional-exposure&mini=true "Share on LinkedIn")

## 1.1 Introduction

A hopefully rare scenario that gives red teamers a mini heart-attack is a sudden check-in from a new agent: ***admin*** on ***ALICE-PC***.

If a blue teamer has managed to get hold of a payload used on an engagement and is able to unravel it to reveal the inner implant, then something has gone awfully wrong somewhere. In this post, I will review how an engagement went awfully wrong for me by expanding on this concept and looking at the laziness behind it.

In my case, I had access to a VDI for an assumed breach and generated a like-for-like key on the hostname—let’s called it ***WORKSTATION1***. At some point during the engagement, I tripped an alarm unrelated to the implant itself and caused the blue team to track down ***WORKSTATION1***. After some time, they managed to identify the implant process and took it offline. A few days later, I saw the ***admin@ALICE-PC*** check-in to my C2. So then, I immediately panicked and cycled all IPs, set up new listeners with new redirectors, and carried on. But, after speaking with the blue teamer who unraveled it, they said that all they did was gather a bunch of environmental components and just did some brute-forcing until they managed to fire off the payload.

On my side, all I had done was use a hostname key with SHA256 (***265a787c97f61f963efe6d397ef712eef1b89f0641003d1664d118d123828379***) to enter the execution cycle and then derived a new encryption key from the SHA256 value to decrypt the actual payload. In this instance, the implant was embedded within the payload using whatever transformations I applied.

I made several mistakes here:

1. Having easy access to the VDI made me lower my guard/paranoia
2. Used a single key
3. Used an embedded payload

Points 2 and 3 above are directly fueled by point 1 because it’s not something I typically do. Alas, here we are.

In this blog, I want to discuss how these mistakes can be avoided by using a collection of different keying variations and mechanisms. The code shown in this blog is merely an example/proof of concept and will have OpSec considerations—this is purely to demonstrate the ideas and methodology.

## 1.2 The Multi-Step Process

The diagram below shows the flow of keying that will be discussed in this blog.

![](https://trusted-sec.transforms.svdcdn.com/production/images/Blog-assets/Execution_McGrath/Fig1_McGrath.png?w=320&q=90&auto=format&fit=max&dm=1721828805&s=0c65d5faf9199906838afdb983dd0e67)

It starts with a general local host check—i.e., the hostname is X, or file Y exists. If that is successful, it moves on to a network level check. This could be domain X, or ***SYSVOL*** file Y exists. And if both pass, we add an extra cont...