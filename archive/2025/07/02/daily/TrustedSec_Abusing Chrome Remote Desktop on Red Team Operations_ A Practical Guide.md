---
title: Abusing Chrome Remote Desktop on Red Team Operations: A Practical Guide
url: https://trustedsec.com/blog/abusing-chrome-remote-desktop-on-red-team-operations-a-practical-guide
source: TrustedSec
date: 2025-07-02
fetch_date: 2025-10-06T23:54:22.807708
---

# Abusing Chrome Remote Desktop on Red Team Operations: A Practical Guide

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
* [Abusing Chrome Remote Desktop on Red Team Operations: A Practical Guide](https://trustedsec.com/blog/abusing-chrome-remote-desktop-on-red-team-operations-a-practical-guide)

July 01, 2025

# Abusing Chrome Remote Desktop on Red Team Operations: A Practical Guide

Written by
Oddvar Moe

Red Team Adversarial Attack Simulation

![](https://trusted-sec.transforms.svdcdn.com/production/images/Blog-Covers/AbusingChromeRedTeam_WebHero.jpg?w=320&h=320&q=90&auto=format&fit=crop&dm=1750793013&s=3b203852243f050aa302b5f363ac470e)

Table of contents

* [Primer – Chrome Remote Desktop](#Primer)
* [Walkthrough – Deploying It](#Walkthrough)
* [Conclusion](#Conclusion)

Share

* Share URL
* [Share via Email](/cdn-cgi/l/email-protection#19266a6c7b737c7a6d245a717c7a723c2b29766c6d3c2b296d71706a3c2b29786b6d707a757c3c2b297f6b76743c2b294d6b6c6a6d7c7d4a7c7a3c2b283f787469227b767d6024587b6c6a70777e3c2b295a716b76747c3c2b294b7c74766d7c3c2b295d7c6a726d76693c2b2976773c2b294b7c7d3c2b294d7c78743c2b2956697c6b786d7076776a3c2a583c2b29583c2b29496b787a6d707a78753c2b295e6c707d7c3c2a583c2b29716d6d696a3c2a583c2b5f3c2b5f6d6b6c6a6d7c7d6a7c7a377a76743c2b5f7b75767e3c2b5f787b6c6a70777e347a716b76747c346b7c74766d7c347d7c6a726d7669347677346b7c7d346d7c78743476697c6b786d7076776a347834696b787a6d707a7875347e6c707d7c "Share via Email")
* [Share on Facebook](http://www.facebook.com/sharer.php?u=https%3A%2F%2Ftrustedsec.com%2Fblog%2Fabusing-chrome-remote-desktop-on-red-team-operations-a-practical-guide "Share on Facebook")
* [Share on X](http://twitter.com/share?text=Abusing%20Chrome%20Remote%20Desktop%20on%20Red%20Team%20Operations%3A%20A%20Practical%20Guide%3A%20https%3A%2F%2Ftrustedsec.com%2Fblog%2Fabusing-chrome-remote-desktop-on-red-team-operations-a-practical-guide "Share on X")
* [Share on LinkedIn](https://www.linkedin.com/shareArticle?url=https%3A%2F%2Ftrustedsec.com%2Fblog%2Fabusing-chrome-remote-desktop-on-red-team-operations-a-practical-guide&mini=true "Share on LinkedIn")

In this post, we’ll be exploring a practical technique for abusing Chrome Remote Desktop (also known as Google Remote Desktop) within a Red Team operation. I sometimes find myself needing to use legitimate software to achieve my goals, due to client restrictions or other preventive measures. This post is just meant to highlight how to actually use Chrome Remote Desktop on operations.

![](https://trusted-sec.transforms.svdcdn.com/production/images/Blog-assets/AbusingChromeRemoteDesktop_Moe/Moe_AbusingChromeRemote.png?w=320&q=90&auto=format&fit=max&dm=1750793420&s=aa9d89edffbf21203f345c3c33966a32)

## Primer – Chrome Remote Desktop

Chrome Remote Desktop is essentially a piece of software that you install and configure on a client that you originally download from <https://remotedesktop.google.com/>. After installing and configuring it, the compromised host connects to the server (cloud service), and you can click on it in the web portal to connect to it. Neat? I think so. Behind the scenes, it uses a proprietary protocol developed by Google, referred to internally as Chromoting. Based on the information I have found, it communicates over HTTPS and uses WebRTC for transferring data.

What are the requirements for getting started using Chrome Remote Desktop? The only thing you need is a Google account that everyone can [create for free here](https://accounts.google.com/signup). After creating the account, head over to [here to download the software](https://remotedesktop.google.com/) and start to use it. Another requirement is that the installer needs local administrator access on the client.

## Walkthrough – Deploying It

Here is a step-by-step guide on how to deploy Chrome Remote Desktop with some tips along the way.

### 1. Access the setup page

The first step is to navigate to the [Chrome Remote Desktop](https://remotedesktop.google.com/) setup page and under the ***Set up via SSH*** menu option, click begin and then click on the MSI file for Windows to download the MSI file.

![](https://trusted-sec.transforms.svdcdn.com/production/images/Blog-assets/AbusingChromeRemoteDesktop_Moe/Fig01_Moe_AbusingChromeRemote.png?w=320&q=90&auto=format&fit=max&dm=1750793398&s=74d0793321f43105e7c740142bc7271a)

Figure 1 - Start set up via SSH

### 2. Download MSI File

![](https://trusted-sec.transforms.svdcdn.com/production/images/Blog-assets/AbusingChromeRemoteDesktop_Moe/Fig02_Moe_AbusingChromeRemote.png?w=320&q=90&auto=format&fit=max&dm=1750793399&s=5e4844490ca20a9e3c6ba3324c67cd60)

Figure 2 - Download MSI File

### 3. Run the installer

Next, you need to install the MSI file on the target. How you do that depends on...