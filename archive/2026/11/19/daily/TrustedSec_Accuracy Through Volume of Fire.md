---
title: Accuracy Through Volume of Fire
url: https://trustedsec.com/blog/accuracy-through-volume-of-fire
source: TrustedSec
date: 2026-11-19
fetch_date: 2026-11-20T09:22:58.809436
---

# Accuracy Through Volume of Fire

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
* [Accuracy Through Volume of Fire](https://trustedsec.com/blog/accuracy-through-volume-of-fire)

November 19, 2026

# Accuracy Through Volume of Fire

Written by
Justin Elze

Artificial Intelligence (AI)

![](https://trusted-sec.transforms.svdcdn.com/production/images/Blog-Covers/AccuracyVolumeOfFire_WebHero.jpg?w=320&h=320&q=90&auto=format&fit=crop&dm=1794941109&s=043facb458dd7635ee6dce8286681da8)

Table of contents

* [Stop Giving Automated Testing Unlimited Room](#Stop)
* [Running the Framework Creates Its Own Attack Surface](#Own)
* [Internal Networks Change the Constraints](#Change)
* [Make the Volume Hit Walls](#Walls)

Share

* Share URL
* [Share via Email](/cdn-cgi/l/email-protection#b887cbcddad2dddbcc85fbd0dddbd39d8a88d7cdcc9d8a88ccd0d1cb9d8a88d9caccd1dbd4dd9d8a88decad7d59d8a88eccacdcbccdddcebdddb9d8a899ed9d5c883dad7dcc185f9dbdbcdcad9dbc19d8a88ecd0cad7cddfd09d8a88eed7d4cdd5dd9d8a88d7de9d8a88fed1cadd9d8bf99d8a88d0ccccc8cb9d8bf99d8afe9d8afecccacdcbccdddccbdddb96dbd7d59d8afedad4d7df9d8afed9dbdbcdcad9dbc195ccd0cad7cddfd095ced7d4cdd5dd95d7de95ded1cadd "Share via Email")
* [Share on Facebook](https://www.facebook.com/sharer.php?u=https%3A%2F%2Ftrustedsec.com%2Fblog%2Faccuracy-through-volume-of-fire "Share on Facebook")
* [Share on X](https://twitter.com/share?text=Accuracy%20Through%20Volume%20of%20Fire%3A%20https%3A%2F%2Ftrustedsec.com%2Fblog%2Faccuracy-through-volume-of-fire "Share on X")
* [Share on LinkedIn](https://www.linkedin.com/shareArticle?url=https%3A%2F%2Ftrustedsec.com%2Fblog%2Faccuracy-through-volume-of-fire&mini=true "Share on LinkedIn")

ARTEX and similar LLM-driven pentesting frameworks can find weaknesses, follow leads, and turn ordinary exposure into useful attack paths. Incident reporting now shows attackers using them successfully. The practical questions are what these tools actually do, what you can learn by running them yourself, and where defenders can interrupt the work.

When I say volume of fire, I mean the number and breadth of attempts a framework can make, including follow-up requests that change based on earlier results. An LLM makes that follow-up cheaper to sustain. It can also improve a hypothesis as evidence comes in. That does not make every conclusion correct, and attempts made against a live target create opportunities to detect or block the activity.

## Familiar Tools With LLM Follow-Up

ARTEX is an LLM-driven pentesting and offensive command-and-control platform that coordinates agents and exposes a web console. The framework gives a model tools to inspect targets and act on the results. PentAGI, HexStrike AI, and Cairn appear in the same reporting, although their implementations differ. ARTEX is a useful example of the broader shift from running a scanner to automating the investigation that follows.

[Google Threat Intelligence Group](https://cloud.google.com/blog/topics/threat-intelligence/artex-and-friends-enter-agentic-offensive-frameworks) and Mandiant's October 30 report documents these frameworks in intrusion investigations. Its ARTEX examples include rapid AWS permission probing and hundreds of logged events while pursuing command execution on a web server. That is evidence of operational use, rather than a claim that every model or default configuration will produce the same results. Successful and noisy can describe the same intrusion.

### The Scanner is Only the Beginning

The common attacker workflow is straightforward, though details differ. Discover assets with tools such as subfinder, identify reachable web services with httpx, enumerate services with Nmap, run nuclei templates, and use ffuf or similar tooling to discover content and parameters. HexStrike's [documented tool inventory](https://github.com/0x4m4/hexstrike-ai#readme) includes all of them. Selection and order vary by framework. Very little of the network behavior is new.

The useful change comes after the initial output. In an agent workflow, the LLM selects an action, the framework executes it, and the result becomes input for the next decision. It might inspect a response, adjust a request with curl or a browser, write a small script, or investigate an exposed file. A discovered secret becomes another hypothesis: Is it valid, and what can it access? The operator still has to decide which questions can be answered within scope and what evidence is sufficient.

The model supplies reasoning and proposed actions. The framework supplies tools, execution, state, and permissions. The deployment supplies the actual access. Changing any of those can change the outcome, so a framework name alone tells you very little about how capable a particular run will be.

Microsoft's [November 6 ARTEX reporting](https://www.microsoft.com/en-us/security/blog/2026/11/06/artex-abuse-expands-as-cybercriminals-target-financial-secto...