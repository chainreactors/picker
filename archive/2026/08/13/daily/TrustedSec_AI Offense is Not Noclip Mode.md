---
title: AI Offense is Not Noclip Mode
url: https://trustedsec.com/blog/ai-offense-is-not-noclip-mode
source: TrustedSec
date: 2026-08-13
fetch_date: 2026-08-14T04:00:44.022553
---

# AI Offense is Not Noclip Mode

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
* [AI Offense is Not Noclip Mode](https://trustedsec.com/blog/ai-offense-is-not-noclip-mode)

August 13, 2026

# AI Offense is Not Noclip Mode

Written by
Justin Elze

Artificial Intelligence (AI)

![](https://trusted-sec.transforms.svdcdn.com/production/images/Blog-Covers/AIOffenseIsNotNoclipMode_WebHero.jpg?w=320&h=320&q=90&auto=format&fit=crop&dm=1786545220&s=b67bcbbdd0026af098e923ecda1ff779)

Table of contents

* [The Walls Are Real](#Walls)
* [Reachability is the Variable Nobody Prices](#Reachability)
* [Why wp2shell Matters](#Why)
* [Ten Thousand Eyes](#Eyes)
* [Humans Are an Attack Surface Too](#Humans)
* [AI Changes the Economics, Not the Requirements](#Economics)
* [What Defenders Should Actually Do](#Do)
* [Persistence is Not a Skeleton Key](#Persistence)
* [References](#References)

Share

* Share URL
* [Share via Email](/cdn-cgi/l/email-protection#053a7670676f60667138466d60666e2037356a7071203735716d6c762037356477716c66696020373563776a6820373551777076716061566066203734236468753e676a617c38444c2037354a6363606b76602037356c762037354b6a712037354b6a66696c75203735486a61602036442037356d71717576203644203743203743717770767160617660662b666a6820374367696a62203743646c286a6363606b7660286c76286b6a71286b6a66696c7528686a6160 "Share via Email")
* [Share on Facebook](https://www.facebook.com/sharer.php?u=https%3A%2F%2Ftrustedsec.com%2Fblog%2Fai-offense-is-not-noclip-mode "Share on Facebook")
* [Share on X](https://twitter.com/share?text=AI%20Offense%20is%20Not%20Noclip%20Mode%3A%20https%3A%2F%2Ftrustedsec.com%2Fblog%2Fai-offense-is-not-noclip-mode "Share on X")
* [Share on LinkedIn](https://www.linkedin.com/shareArticle?url=https%3A%2F%2Ftrustedsec.com%2Fblog%2Fai-offense-is-not-noclip-mode&mini=true "Share on LinkedIn")

![](https://trusted-sec.transforms.svdcdn.com/production/images/Blog-assets/AIOffenseNoclipMode_Elze/Fig01_Elze_AiNoclipSM.jpg?w=320&q=90&auto=format&fit=max&dm=1786546573&s=73c56d698bd31ba0d0e53a4119feaa21)

Everyone wants the cinematic version of offensive AI. The model finds a path nobody knew existed, ignores the controls, and lands on the objective using an attack class that did not previously exist. Noclip mode. Walk through the wall, skip the level.

That framing is fun. It is also mostly wrong about the near-term risk.

The practical advantage is more boring and more dangerous. AI makes it cheap to keep trying against attack paths we already understand. It can test more variations, explain why something failed, change approaches, connect findings across a codebase nobody has time to read end to end, and continue long after a human operator would have burned the engagement budget and moved on.

That matters. It is also not magic, and the difference between those two statements is where most of the current commentary falls apart.

## The Walls Are Real

Known attack paths generally have controls built around them. Conditional Access with device compliance and phishing-resistant authentication breaks a lot of credential abuse. WDAC or AppLocker in enforcement mode breaks a lot of execution. ASLR, DEP, CFG, CET, and the rest of the memory protection stack made entire exploit classes harder, less reliable, and more expensive. Segmentation limits movement. Tiered administration and LAPS limit what a foothold is worth. Rate limits, lockouts, logging, and behavioral detection still work at machine speed.

A model does not reason its way past those controls because it tried hard enough. A blocked process is still blocked. A token that does not satisfy Conditional Access is still rejected. A memory corruption bug still has to survive whatever mitigations are compiled into the target. A host that cannot route to another segment does not acquire a route because someone wrote a better prompt.

The problem is that almost nobody has one clean wall—a single, consistently enforced defensive boundary where the same controls apply everywhere. Instead, they have fifteen years of overlapping products, exceptions, legacy workflows, trusted paths, exclusions, stale systems, half-finished deployments, and controls enforced in one OU and left in audit mode in another. The result not exactly a wall, but a patchwork of defenses with gaps, seams, and inconsistent enforcement that attackers can work around.

As I wrote in [The Defensive Stack Is Exposed](https://trustedsec.com/blog/the-defensive-stack-is-exposed), the decision logic inside defensive products is increasingly part of the attack surface. Rules, thresholds, exclusions, trusted paths, and management states can now be studied together instead of one at a time.

AI makes finding those seams cheaper. It can test every door, window, vent, service entrance, and badly patched section of drywall, compare versions, watch how the defensive product behaves, recover from dead ends, and keep r...