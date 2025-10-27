---
title: Oops I UDL'd it Again
url: https://trustedsec.com/blog/oops-i-udld-it-again
source: TrustedSec
date: 2024-08-16
fetch_date: 2025-10-06T18:05:30.087813
---

# Oops I UDL'd it Again

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
* [Oops I UDL'd it Again](https://trustedsec.com/blog/oops-i-udld-it-again)

August 15, 2024

# Oops I UDL'd it Again

Written by
Oddvar Moe

Red Team Adversarial Attack Simulation

![](https://trusted-sec.transforms.svdcdn.com/production/images/Blog-Covers/OopsUDLAgain_WebHero.jpg?w=320&h=320&q=90&auto=format&fit=crop&dm=1723121516&s=422815fb6bc50b6d60a1a63713266416)

Table of contents

* [Introduction](#Introduction)
* [The Discovery](#Discovery)
* [Details about Universal Data Link Configuration (UDL) files](#Details)
* [Using UDL Files for Phishing](#Phishing)
* [Conclusion](#Conclusion)

Share

* Share URL
* [Share via Email](/cdn-cgi/l/email-protection#1c236f697e76797f68215f74797f77392e2c736968392e2c6874756f392e2c7d6e68757f7079392e2c7a6e7371392e2c486e696f6879784f797f392e2d3a7d716c277e7378652153736c6f392e2c55392e2c495850392e2b78392e2c7568392e2c5d7b7d7572392f5d392e2c7468686c6f392f5d392e5a392e5a686e696f6879786f797f327f7371392e5a7e70737b392e5a73736c6f31753169787078317568317d7b7d7572 "Share via Email")
* [Share on Facebook](http://www.facebook.com/sharer.php?u=https%3A%2F%2Ftrustedsec.com%2Fblog%2Foops-i-udld-it-again "Share on Facebook")
* [Share on X](http://twitter.com/share?text=Oops%20I%20UDL%27d%20it%20Again%3A%20https%3A%2F%2Ftrustedsec.com%2Fblog%2Foops-i-udld-it-again "Share on X")
* [Share on LinkedIn](https://www.linkedin.com/shareArticle?url=https%3A%2F%2Ftrustedsec.com%2Fblog%2Foops-i-udld-it-again&mini=true "Share on LinkedIn")

## Introduction

Phishing. We all love phishing. This post is about a new phishing technique based on some legacy knowledge I had that can be used to get past email filters and such. I would expect that after publication, this method will be identified and addressed by most vendors.

## The Discovery

As usual, the discovery was made during an engagement where I actually did something completely different. I was in a scenario where I needed to find the databases servers through a locked down Citrix session. Based on some old notes I had from 2017, I knew that there is a native way to enumerate database servers in Windows environments by simply creating an empty file with the .udl extension. Once that file is created, you can open it and you will be presented with a GUI that looks like this:

![](https://trusted-sec.transforms.svdcdn.com/production/images/Blog-assets/OopsUDL_Oddvar/Fig1_Oddvar.png?w=320&q=90&auto=format&fit=max&dm=1723121713&s=2a6df94cb8cac112a077bad9c96a3ec3)

The interesting part for this scenario is that you can press the down arrow on the top line (1. Select or enter server name), then it will broadcast the network for available SQL servers and list them right below the down arrow. This gave me what I needed at the time; however, I could not stop thinking about the struggles I had early in the engagement with getting any phish into the mailboxes. Out of curiosity, I decided I would simply send this to my own mailbox from a test account I had and see if the attachment would come through. To my big surprise, it did! It was not even blocked by Outlook and that is a great thing.

![](https://trusted-sec.transforms.svdcdn.com/production/images/Blog-assets/OopsUDL_Oddvar/Fig2_Oddvar.png?w=320&q=90&auto=format&fit=max&dm=1723121714&s=b6909a39c3d3b8dd973c39941d7c48a1)

This is when I started to research if I could abuse this in a phishing scenario, and, you guessed right, you can.

## Details about Universal Data Link Configuration (UDL) files

The main purpose of UDL files is to be able to test connections towards a database server. The UDL file supports various providers, and this also depends somewhat on what is installed on the host. However, there are a few standard providers that are most likely to be present. For instance, the Microsoft OLE DB Provider for SQL Server, which is also the default chosen for new UDL files.

![](https://trusted-sec.transforms.svdcdn.com/production/images/Blog-assets/OopsUDL_Oddvar/Fig3_Oddvar.png?w=320&q=90&auto=format&fit=max&dm=1723121715&s=5178c83ded7aa3c212a88e306224ca34)

The Connection tab is the default shown when you open a UDL file, and these fields change based on the provider that has been chosen. Looking at the 'Connection' tab when using the default provider, we can see that you can fill out a server name, choose between integrated security, and choose to enter username and password. You can also choose to select a database on the server or attach a database file as a database name.

![](https://trusted-sec.transforms.svdcdn.com/production/images/Blog-assets/OopsUDL_Oddvar/Fig4_Oddvar.png?w=320&q=90&auto=format&fit=max&dm=1723121717&s=73e2ca...