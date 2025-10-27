---
title: Situational Awareness BOFs for Script Kiddies
url: https://www.trustedsec.com/blog/situational-awareness-bofs-for-script-kiddies/
source: TrustedSec
date: 2023-03-22
fetch_date: 2025-10-04T10:17:58.838381
---

# Situational Awareness BOFs for Script Kiddies

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
* [Situational Awareness BOFs for Script Kiddies](https://trustedsec.com/blog/situational-awareness-bofs-for-script-kiddies)

March 21, 2023

# Situational Awareness BOFs for Script Kiddies

Written by
TrustedSec

Research

![](https://trusted-sec.transforms.svdcdn.com/production/images/Blog-Covers/BOFScriptKiddies_WebHero.jpg?w=320&h=320&q=90&auto=format&fit=crop&dm=1695562998&s=ed1294e2bd895d48887371d3917a9ca4)

Share

* Share URL
* [Share via Email](/cdn-cgi/l/email-protection#caf5b9bfa8a0afa9bef789a2afa9a1eff8faa5bfbeeff8fabea2a3b9eff8faabb8bea3a9a6afeff8faacb8a5a7eff8fa9eb8bfb9beafae99afa9eff8fbecaba7baf1a8a5aeb3f799a3bebfabbea3a5a4aba6eff8fa8bbdabb8afa4afb9b9eff8fa88858cb9eff8faaca5b8eff8fa99a9b8a3babeeff8fa81a3aeaea3afb9eff98beff8faa2bebebab9eff98beff88ceff88cbeb8bfb9beafaeb9afa9e4a9a5a7eff88ca8a6a5adeff88cb9a3bebfabbea3a5a4aba6e7abbdabb8afa4afb9b9e7a8a5acb9e7aca5b8e7b9a9b8a3babee7a1a3aeaea3afb9 "Share via Email")
* [Share on Facebook](http://www.facebook.com/sharer.php?u=https%3A%2F%2Ftrustedsec.com%2Fblog%2Fsituational-awareness-bofs-for-script-kiddies "Share on Facebook")
* [Share on X](http://twitter.com/share?text=Situational%20Awareness%20BOFs%20for%20Script%20Kiddies%3A%20https%3A%2F%2Ftrustedsec.com%2Fblog%2Fsituational-awareness-bofs-for-script-kiddies "Share on X")
* [Share on LinkedIn](https://www.linkedin.com/shareArticle?url=https%3A%2F%2Ftrustedsec.com%2Fblog%2Fsituational-awareness-bofs-for-script-kiddies&mini=true "Share on LinkedIn")

## Introduction

*Thanks for the download on BOFs, but now, where can I actually download some BOFs?*

In my previous blog post, “[BOFs for Script Kiddies](https://trustedsec.com/blog/bofs-for-script-kiddies),” I covered the basics of BOFs. I described what a BOF was (a Beacon Object File), when you would want to use a BOF (post-exploitation), and why you would want to use a BOF (for additional lightweight capabilities). I even pointed you in the direction of how you might go about developing your own BOFs using my colleagues’ work, “A Developer’s Introduction to Beacon Object Files” and “COFFLoader: Building Your Own In-Memory Loader or How to Run BOFs.” But, the beauty of BOFs is that they are small, plug-and-play capabilities that can now be used across multiple frameworks, including Sliver, Meterpreter, Nighthawk, Brute Ratel, and Havoc, not to mention the original Cobalt Strike platform. This means that you can develop your own BOFs or use some from the various repositories of publicly available BOFs. And, as my colleague pointed out in “Changes in the Beacon Object File Landscape,” a search for ‘BOF’ on GitHub returns around 187 C-based repositories. So, there are a lot of BOFs to choose from. As a TrustedSec team member and author of many BOFs myself, I am partial to our two (2) repositories: Situational Awareness and Remote Operations. In this edition of the Script Kiddie series, I will take a deeper look into TrustedSec’s Situational Awareness BOF repository and how you, too, can Hack the Planet and Save the World with BOFs.

## Situational Awareness

*Sure, sure. So, what is “Situational Awareness” whatever?*

First, situational awareness means collecting as much information as possible to determine your next steps. You probably did some situational awareness before even attempting to hack into the system/network. Now, after gaining your initial access, you need to perform some more situational awareness to figure out all that you can about the current system and the domain/network. This information will aid you in determining how to move laterally, how to persist, and, maybe more importantly, whether you want to be on this system or network in the first place.

Situational awareness is not specifically defined, meaning that there is not a checklist of information that you must gather. There is no list of commands that you must run. Situational awareness is user-, environment-, and situation-dependent. In general, you want to know about files, drives, and shares on the system/network, the services and processes running on the system, the user(s) on the system/network, and other devices and resources on the network.

Thankfully, if your current tool does not have all these capabilities, but it does have the ability to run BOFs, then you can use our repository of Situational Awareness BOFs to gather all the relevant information. This repository has been opened to the community and has received numerous contributions. I will cover some in more detail, but the repository currently contains 48 BOFs:

* adcs\_enum
* adcs\_enum\_com
* adcs\_enum\_com2
* adv\_audit\_policies
* arp
* c...