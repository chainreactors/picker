---
title: Vulnify: Giving Your Agents a CVE Brain
url: https://trustedsec.com/blog/vulnify-giving-your-agents-a-cve-brain
source: TrustedSec
date: 2026-07-09
fetch_date: 2026-07-10T05:59:47.501377
---

# Vulnify: Giving Your Agents a CVE Brain

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
* [Vulnify: Giving Your Agents a CVE Brain](https://trustedsec.com/blog/vulnify-giving-your-agents-a-cve-brain)

July 09, 2026

# Vulnify: Giving Your Agents a CVE Brain

Written by
Brandon McGrath

Artificial Intelligence (AI)

![](https://trusted-sec.transforms.svdcdn.com/production/images/Blog-Covers/Vulnify_WebHero.jpg?w=320&h=320&q=90&auto=format&fit=crop&dm=1783432440&s=49627ee624694b31a3e277eb17fd3114)

Table of contents

* [How It Got Built](#How)
* [What's Actually In It?](#What)
* [One CVE](#CVE)
* [The Explorer](#Explorer)
* [Talking to It: The MCP Server](#MCPServer)
* [Actually Using It](#Using)
* [You Don't Have to Use MCP](#donot)
* [Wrapping Up](#WrappingUp)

Share

* Share URL
* [Share via Email](/cdn-cgi/l/email-protection#a29dd1d7c0c8c7c1d69fe1cac7c1c9879092cdd7d6879092d6cacbd1879092c3d0d6cbc1cec7879092c4d0cdcf879092f6d0d7d1d6c7c6f1c7c187909384c3cfd299c0cdc6db9ff4d7cecccbc4db8791e3879092e5cbd4cbccc5879092fbcdd7d0879092e3c5c7ccd6d1879092c3879092e1f4e7879092e0d0c3cbcc8791e3879092cad6d6d2d18791e38790e48790e4d6d0d7d1d6c7c6d1c7c18cc1cdcf8790e4c0cecdc58790e4d4d7cecccbc4db8fc5cbd4cbccc58fdbcdd7d08fc3c5c7ccd6d18fc38fc1d4c78fc0d0c3cbcc "Share via Email")
* [Share on Facebook](https://www.facebook.com/sharer.php?u=https%3A%2F%2Ftrustedsec.com%2Fblog%2Fvulnify-giving-your-agents-a-cve-brain "Share on Facebook")
* [Share on X](https://twitter.com/share?text=Vulnify%3A%20Giving%20Your%20Agents%20a%20CVE%20Brain%3A%20https%3A%2F%2Ftrustedsec.com%2Fblog%2Fvulnify-giving-your-agents-a-cve-brain "Share on X")
* [Share on LinkedIn](https://www.linkedin.com/shareArticle?url=https%3A%2F%2Ftrustedsec.com%2Fblog%2Fvulnify-giving-your-agents-a-cve-brain&mini=true "Share on LinkedIn")

When building agentic components for pentesting, CVEs are inevitably going to come up. I never found anything that matched what I needed; I did not want "search the web and hope," but actual answers bound to a technology, and the ability to answer questions like “Does this version of this package have this CVE?”, “Is there a public exploit?”, “and “Where is it?” By packaging all that up, agents can get a head start on the scope of the product they’re looking at.

Prior to this work, there are a few ways it can be fudged. The first is by letting the agent search the web with [Tavily](https://tavily.com). It sort of works, but it is slow and non-deterministic, and the agent ends up reading vendor marketing and blogspam to find a CVSS score that lives in a database somewhere. Or, even worse, the 1,000 free credits a month don’t scale - I don’t fancy *Yet-Another-Subscription*.

The second is by bolting on a scanner like [Nuclei](https://github.com/projectdiscovery/nuclei). Nuclei is great at templated detection against a live host. But we may not always want to point heavy tools at a product right away. Following the approach of recon and light poking first, Nuclei doesn’t fit.

The third is by hitting [NVD](https://nvd.nist.gov/) and vendor APIs live. This is the closest-to-right solution, but painful to do deterministically and a waste of tokens to let agents figure it out. NVD also throttles you to about five (5) requests every 30 seconds without a key. Furthermore, every source has its own schema, and nothing joins together well.

None of these solve the problem, they work around it and are probably fine for smaller projects, but they do not satisfy my stability and reproducibility requirements, let alone save tokens.

This is where [Vulnify](https://github.com/mez-0/vulnify/) comes in. It is an MCP-capable server set on top of one (1) normalized SQLite database that stitches the authoritative sources together and hands the agent a clean, joined answer.

One (1) caveat up front, Vulnify is point-in-time. It needs to pull data every so often to stay relevant; I am working on something CICD-able for this in the future.

## How It Got Built

Before I discuss the internals, I want to make a foreword on writing bigger projects with agentic workflows. I find that LLMs are great at extending a codebase that already has a strong opinion baked in. If you let an agent loose on a new project with no guardrails or guidelines, you will see all sorts of weird and wonderful coding styles.

My personal approach, and the approach used to build Vulnify, is to manually build v0.1. I know, writing code in 2026—wow. But, by doing so, I get to lay the groundwork for coding paradigms: how docstrings are laid out, how functions are named, data models, and generally writing the code how I like to. Then, I pass an agent (Claude, in my case) over top of it to learn it, write docs, and update CLAUDE.md and memory; whatever it needs to ensure it matches my style. Then, over time, I introduce subagents to reinforce that pre-commit. If this first pre-pass is done in a strong model like...