---
title: Large Workflows with Local LLMs
url: https://trustedsec.com/blog/large-workflows-with-local-llms
source: TrustedSec
date: 2026-06-25
fetch_date: 2026-06-26T06:09:03.087675
---

# Large Workflows with Local LLMs

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
* [Large Workflows with Local LLMs](https://trustedsec.com/blog/large-workflows-with-local-llms)

June 25, 2026

# Large Workflows with Local LLMs

Written by
Kevin Haubris

Artificial Intelligence (AI)

![](https://trusted-sec.transforms.svdcdn.com/production/images/Blog-Covers/LargeWorkflowsLocalLLMs_WebHero.jpg?w=320&h=320&q=90&auto=format&fit=crop&dm=1781890241&s=f80b9934d49753e936aa38fb0f6ee617)

Table of contents

* [Context Size Issues](#Issues)
* [LLMs Going Off the Rails](#Off)
* [An Attempt to Address These](#Attempt)
* [Encountered Issues](#Encountered)
* [Project Details](#Details)
* [Takeaways](#Takeaways)
* [Future Work](#Future)
* [Resources](#Resources)

Share

* Share URL
* [Share via Email](/cdn-cgi/l/email-protection#76490503141c1315024b351e13151d534446190302534446021e1f055344461704021f151a135344461004191b5344462204030502131225131553444750171b064d1419120f4b3a170411135344462119041d101a190105534446011f021e5344463a1915171a5344463a3a3b055345375344461e02020605534537534430534430020403050213120513155815191b534430141a19115344301a170411135b0119041d101a1901055b011f021e5b1a1915171a5b1a1a1b05 "Share via Email")
* [Share on Facebook](https://www.facebook.com/sharer.php?u=https%3A%2F%2Ftrustedsec.com%2Fblog%2Flarge-workflows-with-local-llms "Share on Facebook")
* [Share on X](https://twitter.com/share?text=Large%20Workflows%20with%20Local%20LLMs%3A%20https%3A%2F%2Ftrustedsec.com%2Fblog%2Flarge-workflows-with-local-llms "Share on X")
* [Share on LinkedIn](https://www.linkedin.com/shareArticle?url=https%3A%2F%2Ftrustedsec.com%2Fblog%2Flarge-workflows-with-local-llms&mini=true "Share on LinkedIn")

Over the last few months, I have been digging into local LLMs and Frontier models. Frontier models have huge context windows, which gives them an advantage because it can keep the entire project in its context, but with smaller-scale tests, local LLMs can be extremely capable as well. In this post, I’ll be going over some pain points of using local LLMs and how I approached working around them.

## Picking a Local Model

The first thing we should talk about is how to pick a good local model to use. During my testing, I broke these down into categories:

* Summarization Tasks
  + Tasks where speed is more important and full info is provided for it to just summarize
* Programming Tasks
  + Tasks where accuracy is the most important, and full context is not provided; an example would be having an LLM insert a function into a previously existing code base in a specific subset of files
* Reverse Engineering Tasks
  + Tasks like using Ghidra to pull apart malware samples and clean up the disassembly
* Research Tasks
  + Tasks that can provide multiple MCP servers to try to identify related topics that may not normally be categorized together

All of these tasks can be done with different sized models, but some of them benefit **HEAVILY** from larger models. For example, a 20b to 35b model will do infinitely better than a 4b to 9b model on programming tasks, but a 4b to 9b model will run significantly faster than a 20b to 35b model on summarization tasks without a significant decrease in output. The size of model that you choose will depend on what you are trying to do, so experimentation with different models is recommended.

## Context Size Issues

No matter what models you choose, some workflows end up needing more context than others. The problem is that most models I’ve encountered have an upper limit at 256K context. If you tried to use GhidraMCP with larger binaries and a local model through something like OpenCode, you may have noticed that after a while, the naming for some functions starts being wrong, and sometimes, some models may go into a loop trying tools that error out. When that happens, the context size may increase and need to be compacted through various methods, and it may just keep looping indefinitely, increasing the size of the context until you exit out. In these tasks, Frontier models seem to be an answer. Another option is to just use local models on smaller samples with a 256K context setup. There is also the concept of “context rot,” (5) when increasing the size of context doesn’t necessarily increase the performance of a model and, in some cases, degrades it based on size. Due to this, it’s worth testing how accurate your chosen model performs.

## LLMs Going Off the Rails

Another major issue I’ve encountered is that, when using tools like Claude Code and OpenCode, even when in “plan mode,” it seems the LLM is what determines if it can run specific tools. When the LLM decides to follow instructions, that works fine, but if you are going to be running long-term workflows, completely disabling specific tools would be ideal. For instance, if the workflow you are running only needs GhidraMCP’s functions and writing a...