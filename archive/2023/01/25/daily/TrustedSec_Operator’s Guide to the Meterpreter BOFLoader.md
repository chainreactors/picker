---
title: Operator’s Guide to the Meterpreter BOFLoader
url: https://www.trustedsec.com/blog/operators-guide-to-the-meterpreter-bofloader/
source: TrustedSec
date: 2023-01-25
fetch_date: 2025-10-04T04:44:10.379437
---

# Operator’s Guide to the Meterpreter BOFLoader

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
* [Operator's Guide to the Meterpreter BOFLoader](https://trustedsec.com/blog/operators-guide-to-the-meterpreter-bofloader)

January 24, 2023

# Operator's Guide to the Meterpreter BOFLoader

Written by
Kevin Clark

Application Security Assessment
Incident Response
Incident Response & Forensics
Penetration Testing
Research
Security Testing & Analysis

![](https://trusted-sec.transforms.svdcdn.com/production/images/Blog-Covers/OperatorsGuideMeterpreter_WebHero.jpg?w=320&h=320&q=90&auto=format&fit=crop&dm=1695566306&s=2b2e1aa8fe1c8514b48b1b1d0a429615)

Share

* Share URL
* [Share via Email](/cdn-cgi/l/email-protection#fcc38f899e96999f88c1bf94999f97d9cecc938988d9cecc8894958fd9cecc9d8e88959f9099d9cecc9a8e9391d9cecca88e898f889998af999fd9cecdda9d918cc79e939885c1b38c998e9d88938ed9cecb8fd9ceccbb89959899d9cecc8893d9cecc889499d9ceccb19988998e8c8e9988998ed9ceccbeb3bab0939d98998ed9cfbdd9cecc9488888c8fd9cfbdd9cebad9ceba888e898f8899988f999fd29f9391d9ceba9e90939bd9ceba938c998e9d88938e8fd19b89959899d18893d1889499d1919988998e8c8e9988998ed19e939a90939d98998e "Share via Email")
* [Share on Facebook](http://www.facebook.com/sharer.php?u=https%3A%2F%2Ftrustedsec.com%2Fblog%2Foperators-guide-to-the-meterpreter-bofloader "Share on Facebook")
* [Share on X](http://twitter.com/share?text=Operator%27s%20Guide%20to%20the%20Meterpreter%20BOFLoader%3A%20https%3A%2F%2Ftrustedsec.com%2Fblog%2Foperators-guide-to-the-meterpreter-bofloader "Share on X")
* [Share on LinkedIn](https://www.linkedin.com/shareArticle?url=https%3A%2F%2Ftrustedsec.com%2Fblog%2Foperators-guide-to-the-meterpreter-bofloader&mini=true "Share on LinkedIn")

## 1.1      Introduction

Recently, myself and a few friends decided to port my coworker [Kevin Haubris](https://twitter.com/kev169)' [COFFLoader project](https://github.com/trustedsec/COFFLoader) to Metasploit. This [new BOFLoader extension](https://github.com/rapid7/metasploit-framework/pull/16995) allows Beacon Object Files (BOFs) to be used from a Meterpreter session. This addition unlocks many new possibilities for Meterpreter and, in my opinion, elevates Meterpreter back up to the status of a 'modern C2 payload'. In this blog, I want to demonstrate uses of the BOFLoader and common errors an operator might make when using the BOFLoader for the first time.

## 1.2      BOFs: What Are They?

BOFs are compiled but unlinked C programs in the format of an object file. Typically small in size, BOFs can be sent to a 'BOF loader' that loads a BOF into memory, performs linker operations to map external symbols to function addresses, and then executes the BOF code in memory.

Similar to reflective DLL injection or .NET reflection, BOFs allow operators to dynamically add functionality to an implant at runtime. This allows an implant to be built as small as possible in order to keep signatures to a minimum. The word 'Beacon' in Beacon Object File comes from Cobalt Strike's Beacon payload, the first public C2 to release with a BOF loader. We will be focusing on using BOFs in this blog post, but [great resources](https://hstechdocs.helpsystems.com/manuals/cobaltstrike/current/userguide/content/topics/beacon-object-files_main.htm) for [developing BOFs](https://www.trustedsec.com/blog/a-developers-introduction-to-beacon-object-files/) are [out there](https://otterhacker.github.io/Malware/CoffLoader.html) as well.

## 1.3      Meterpreter BOFLoader for Dummies

Meterpreter has [great documentation](https://docs.metasploit.com/docs/using-metasploit/advanced/meterpreter/meterpreter-executebof-command.html) on the BOFLoader already, but sometimes it's better to see example usage and work backwards from there. Before executing our first BOF, we need to learn how to compile a BOF. [Christopher Paschen](https://twitter.com/freefirex2), another coworker of mine, created a collection of [Situational Awareness BOFs](https://github.com/trustedsec/CS-Situational-Awareness-BOF), which we will use throughout this blog. To start, we need to install a C compiler such as [mingw-gcc](https://sourceforge.net/projects/mingw/). Then, we need to use the provided [make\_all.sh](https://github.com/trustedsec/CS-Situational-Awareness-BOF/blob/master/make_all.sh) script to compile each BOF.

![](https://www.trustedsec.com/wp-content/uploads/2023/01/Clark_1.png)

After running the ***make\_all.sh*** script, object (.o) files for x86 and x64 architectures should be present in their respective folders.

![](https://www.trustedsec.com/wp-content/uploads/2023/01/Clark_2.png)

Figure 2 - Viewing Newly Compiled Object Files Within the SA Folder

The last step before we can execute these BOFs ...