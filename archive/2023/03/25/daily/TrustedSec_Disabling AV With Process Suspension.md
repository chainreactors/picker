---
title: Disabling AV With Process Suspension
url: https://www.trustedsec.com/blog/disabling-av-with-process-suspension/
source: TrustedSec
date: 2023-03-25
fetch_date: 2025-10-04T10:40:00.355221
---

# Disabling AV With Process Suspension

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
* [Disabling AV With Process Suspension](https://trustedsec.com/blog/disabling-av-with-process-suspension)

March 24, 2023

# Disabling AV With Process Suspension

Written by
Christopher Paschen

Penetration Testing
Research
Security Testing & Analysis

![](https://trusted-sec.transforms.svdcdn.com/production/images/Blog-Covers/DisablingAVwithProcessSuspension_WebHero.jpg?w=320&h=320&q=90&auto=format&fit=crop&dm=1695562644&s=cb7135b12fc02cd33e17e811791e5b93)

Share

* Share URL
* [Share via Email](/cdn-cgi/l/email-protection#37084442555d5254430a745f52545c120507584243120507435f5e441205075645435e545b521205075145585a1205076345424443525364525412050611565a470c5558534e0a735e4456555b5e59501205077661120507605e435f12050767455854524444120507644244475259445e58591204761205075f43434744120476120571120571434542444352534452541954585a120571555b5850120571535e4456555b5e59501a56411a405e435f1a474558545244441a444244475259445e5859 "Share via Email")
* [Share on Facebook](http://www.facebook.com/sharer.php?u=https%3A%2F%2Ftrustedsec.com%2Fblog%2Fdisabling-av-with-process-suspension "Share on Facebook")
* [Share on X](http://twitter.com/share?text=Disabling%20AV%20With%20Process%20Suspension%3A%20https%3A%2F%2Ftrustedsec.com%2Fblog%2Fdisabling-av-with-process-suspension "Share on X")
* [Share on LinkedIn](https://www.linkedin.com/shareArticle?url=https%3A%2F%2Ftrustedsec.com%2Fblog%2Fdisabling-av-with-process-suspension&mini=true "Share on LinkedIn")

Every now and again, I see a crazy tweet that feels like it just can’t be true. Many of them are not true or are folks making overblown statements about something cool they found—this is part of the research game, and folks are entitled to be excited about what they are learning. Recently, however, I saw something that I thought needed more attention. There was a [tweet](https://twitter.com/0gtweet/status/1638069413717975046) by [@0gtweet](https://twitter.com/0gtweet) claiming that one could suspend Windows Defender and then straight up run Mimikatz. This kicked off a fun little research effort that I’d like to share.

## Does suspending Defender work?

Simply put: yes, you can suspend Defender but not without issue. When Defender is disabled, the entire system will grind to a halt. Explorer will start to freeze up, and the act of starting a new process will hang for minutes, if it works at all. Without diving into a bunch of disassembly, one can assume that any action that would trigger a request for scanning/analysis by Defender is what’s blocking and waiting for a result that won’t come.

That said, results speak for themselves.

Two (2) beacon object files (BOFs) were used to avoid steps that would normally freeze Windows. The first was TrustedSec’s own [suspendresume](https://github.com/trustedsec/CS-Remote-OPs-BOF/blob/main/src/Remote/suspendresume/entry.c) from our public [CS-Remote-Ops-BOF](https://github.com/trustedsec/CS-Remote-OPs-BOF/blob/main/src/Remote/suspendresume/entry.c) repository. The second was the excellent [NanoDump](https://github.com/fortra/nanodump) by Fortra. Using these BOFs, one can initiate a minidump of lsass.exe in a short enough period that a standard user may just assume their computer glitched. Some other ways of accomplishing this same goal, such as using an EXE on disk, were much more unreliable and took long enough that a user would likely force reboot or call support.

## Why does this work?

For anyone unfamiliar with process protections on Windows, it’s worth knowing that Defender runs using a technology called Protected Process Light (PPL). This can be observed using a tool such as [Process Explorer.](https://learn.microsoft.com/en-us/sysinternals/downloads/process-explorer)

![](https://www.trustedsec.com/wp-content/uploads/2023/03/DisablingAV_1.png)

PPL is intended to limit what a non-protected process can do to a protected process. Microsoft kindly [documents](https://learn.microsoft.com/en-us/windows/win32/procthread/process-security-and-access-rights) what is and is not allowed. This means that a normal process can request and potentially be granted the following access rights to a PPL process:

* PROCESS\_QUERY\_LIMITED\_INFORMATION
* PROCESS\_SUSPEND\_RESUME
* PROCESS\_TERMINATE
* SYNCHRONIZE

But wait—PROCESS\_TERMINATE is in that list, and I can’t just kill Defender, so what gives? Most AV/EDR products are split into two (2) or more components. A kernel component can use kernel callbacks to examine new/duplicated handles, file writes, etc., and a userland component may be responsible for sending logs, responding to userland hooks, or interacting with the user.

When ...