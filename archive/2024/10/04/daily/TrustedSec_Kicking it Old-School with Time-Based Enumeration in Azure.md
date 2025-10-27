---
title: Kicking it Old-School with Time-Based Enumeration in Azure
url: https://trustedsec.com/blog/kicking-it-old-school-with-time-based-enumeration-in-azure
source: TrustedSec
date: 2024-10-04
fetch_date: 2025-10-06T18:51:41.013414
---

# Kicking it Old-School with Time-Based Enumeration in Azure

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
* [Kicking it Old-School with Time-Based Enumeration in Azure](https://trustedsec.com/blog/kicking-it-old-school-with-time-based-enumeration-in-azure)

October 03, 2024

# Kicking it Old-School with Time-Based Enumeration in Azure

Written by
@ nyxgeek

Cloud Penetration Testing

![](https://trusted-sec.transforms.svdcdn.com/production/images/Blog-Covers/KickingItOldSchool_WebHero.jpg?w=320&h=320&q=90&auto=format&fit=crop&dm=1727721541&s=7574c669a7c233cab68caa5887649250)

Table of contents

* [Introduction](#Introduction)
* [Time-Based User Enumeration – Azure Edition](#TimeBasedAzure)
* [Basic Auth, WHAT?](#Basic)
* [Time for Maths for Times](#Maths)
* [Autodiscover Enumerator](#Autodiscover)
* [Caveats and Notes](#Notes)
* [Conclusion](#Conclusion)

Share

* Share URL
* [Share via Email](/cdn-cgi/l/email-protection#1f206c6a7d757a7c6b225c777a7c743a2d2f706a6b3a2d2f6b77766c3a2d2f7e6d6b767c737a3a2d2f796d70723a2d2f4b6d6a6c6b7a7b4c7a7c3a2d2e397e726f247d707b662254767c747671783a2d2f766b3a2d2f50737b324c7c777070733a2d2f68766b773a2d2f4b76727a325d7e6c7a7b3a2d2f5a716a727a6d7e6b7670713a2d2f76713a2d2f5e656a6d7a3a2c5e3a2d2f776b6b6f6c3a2c5e3a2d593a2d596b6d6a6c6b7a7b6c7a7c317c70723a2d597d7370783a2d5974767c7476717832766b3270737b326c7c777070733268766b77326b76727a327d7e6c7a7b327a716a727a6d7e6b767071327671327e656a6d7a "Share via Email")
* [Share on Facebook](http://www.facebook.com/sharer.php?u=https%3A%2F%2Ftrustedsec.com%2Fblog%2Fkicking-it-old-school-with-time-based-enumeration-in-azure "Share on Facebook")
* [Share on X](http://twitter.com/share?text=Kicking%20it%20Old-School%20with%20Time-Based%20Enumeration%20in%20Azure%3A%20https%3A%2F%2Ftrustedsec.com%2Fblog%2Fkicking-it-old-school-with-time-based-enumeration-in-azure "Share on X")
* [Share on LinkedIn](https://www.linkedin.com/shareArticle?url=https%3A%2F%2Ftrustedsec.com%2Fblog%2Fkicking-it-old-school-with-time-based-enumeration-in-azure&mini=true "Share on LinkedIn")

## Introduction

Yet another user-enumeration method has been identified in Azure. While Microsoft may have disabled Basic Authentication some time ago, we can still abuse it to identify valid users with a classic technique—*time-based user enumeration*.

Time-based enumeration is a means of identifying valid users based on the difference in time it takes for the server to return a response to a login attempt. To test for it, you try to log in with a valid username (and an incorrect password) and measure the time it takes to return an ‘Invalid Password’ response. Then you try to log in with an invalid username and measure the response time. If the ‘Invalid Password’ response for an invalid user is a lot faster or slower than the response of a valid user, then you have found time-based user enumeration.

![](https://trusted-sec.transforms.svdcdn.com/production/images/Blog-assets/OldSchoolEnum_nyxgeek/Fig1_nyx.png?w=320&q=90&auto=format&fit=max&dm=1727721710&s=18425edea6ebac50e580304ae19d9463)

Figure 1 - Time-Based User Enumeration

The particular method I’m about to demonstrate has a few advantages:

1. It is silent and cannot be detected.
2. It works multi-threaded
3. It will detect UPNs and aliases

So strap in, and let’s take a look at time-based user enumeration in Azure, and its origins dating back to 2014.

![](https://trusted-sec.transforms.svdcdn.com/production/images/Blog-assets/OldSchoolEnum_nyxgeek/Fig2_nyx.jpg?w=320&q=90&auto=format&fit=max&dm=1727721641&s=eb8e8e2e44b76dcebce17fc5f37105cc)

Figure 2 - 2014 or Bust

## Time-Based User Enumeration – Azure Edition

Time-based user enumeration flaws have existed in various Microsoft products since at least 2014. This was first discovered in Microsoft Exchange by a member of **foofus** and [published in August of 2014](http://h.foofus.net/?p=784).

![](https://trusted-sec.transforms.svdcdn.com/production/images/Blog-assets/OldSchoolEnum_nyxgeek/Fig3_nyx.png?w=320&q=90&auto=format&fit=max&dm=1727721644&s=b21afc25a3c58e8562f468973a44a9c1)

Figure 3 - The OG Timing Attack

An attacker makes a login attempt and measures the response time. If it’s a quick response, they’ve just found a valid username. If the response took longer (approximately 5-10x as long), then it was an invalid username. This enumeration was really useful and could be run multi-threaded.

This Exchange enumeration technique has been the starting point for many external pen tests over the years (and internal pen tests too!).

![](https://trusted-sec.transforms.svdcdn.com/production/images/Blog-assets/OldSchoolEnum_nyxgeek/Fig4_nyx.png?w=320&q=90&auto=format&fit=max&dm=1727721646&s=87c2dca0e7e9eebaf7eecf8ec8b5f855)...