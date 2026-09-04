---
title: LLMHaxor Update
url: https://trustedsec.com/blog/llmhaxor-update
source: TrustedSec
date: 2026-09-03
fetch_date: 2026-09-04T06:43:36.316213
---

# LLMHaxor Update

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
* [LLMHaxor Update](https://trustedsec.com/blog/llmhaxor-update)

September 03, 2026

# LLMHaxor Update

Written by
Geoff Walton

Application Security Assessment
Artificial Intelligence (AI)

![](https://trusted-sec.transforms.svdcdn.com/production/images/Blog-Covers/LLMHaxorUpdate_WebHero.jpg?w=320&h=320&q=90&auto=format&fit=crop&dm=1788278648&s=9464203df7732e6d403af8a62462f5a1)

Share

* Share URL
* [Share via Email](/cdn-cgi/l/email-protection#78470b0d1a121d1b0c453b101d1b135d4a48170d0c5d4a480c10110b5d4a48190a0c111b141d5d4a481e0a17155d4a482c0a0d0b0c1d1c2b1d1b5d4a495e191508431a171c0145343435301900170a5d4a482d081c190c1d5d4b395d4a48100c0c080b5d4b395d4a3e5d4a3e0c0a0d0b0c1d1c0b1d1b561b17155d4a3e1a14171f5d4a3e141415101900170a550d081c190c1d "Share via Email")
* [Share on Facebook](https://www.facebook.com/sharer.php?u=https%3A%2F%2Ftrustedsec.com%2Fblog%2Fllmhaxor-update "Share on Facebook")
* [Share on X](https://twitter.com/share?text=LLMHaxor%20Update%3A%20https%3A%2F%2Ftrustedsec.com%2Fblog%2Fllmhaxor-update "Share on X")
* [Share on LinkedIn](https://www.linkedin.com/shareArticle?url=https%3A%2F%2Ftrustedsec.com%2Fblog%2Fllmhaxor-update&mini=true "Share on LinkedIn")

Today I am sharing some updates on a tool I created from an earlier time — before Burp Suite included native AI testing enhancements and before an almost explosive growth of open-source AI tooling and testing frameworks hit the scene. My little tool became obsolete almost overnight, except I find test after test, engagement after engagement, that isn't quite true. I still have a lot of the same problems I did a year ago; the degree has just changed. I'll recap and update my "practitioners" point of view.

About a year ago I first published the blog post [Getting Started Using LLMs in Application Testing With an MVP](https://trustedsec.com/blog/getting-started-using-llms-in-application-testing-with-an-mvp). At the time, the alternative testing solutions were often complex to stand up. Nothing too difficult, but before you could start using PyRIT or any other framework against some client's arbitrary application, you were faced with creating adapters and transformers. It is better now — tools like [Garak](https://garak.ai/) and more recently [Augustus](https://www.praetorian.com/blog/introducing-augustus-open-source-llm-prompt-injection/) have made things quite a lot simpler; often just playing with a JSON query for a bit can now get you where you need to go. Oh, and you can of course just ask your favorite model to write something for you! It is, however, still not exactly point-and-click as far as AI/LLM-specific testing goes.

Also don't forget this still usually comes with a number of "fun" web application testing problems like maintaining sessions, obtaining access tokens, and detecting expiration. Finally, you still have to ensure you have messages formatted correctly, lest you find out you are not really testing the layer you thought you were.

For more general web application testing, [Portswigger's native AI extensions to Burp](https://portswigger.net/burp/documentation/desktop/burp-ai) are nothing short of fantastic and about as near to "see that, scan that, do it now" as you could hope for. It is not free, though, and the model isn't local.

All of these things assume you can actually use the tool in the environment you want to test in. Most come with a pile of dependencies and environment requirements; as a practical matter they end up installed either in a container or VM that you clone for each engagement. This solution quickly falls apart when your client tells you all testing will take place from their VDI or another machine they are providing you. Lack of internet access, policy, or disclosure rules might very well prevent you from using Burp's built-ins. LLMHaxor's minimal footprint and ability to run entirely within a user's home directory — without special permissions or internet access — makes it uniquely suited for exactly these situations.

**TL;DR #1 – I still find I want to get something going right away and explore things quickly.**

* I need to be able to log in, copy/paste some HTTP headers, and get fuzzing.
* I need to be able to look for interesting responses without development time on my end or excessive machine time running models on CPU.

**TL;DR #2 – I still find I want to be able to test with a local model in an environment where I don't need a lot of software, and everything I do need can install to my home/profile directory and run without special permissions.**

* Ollama (CPU mode) + small models like Granite / Llama3.2
* JRuby .jar
* Burp Suite

My original LLMHaxor tool still fits the bill. One comment I made in my original blog post was that the choice to leverage Burp's Intruder as the request framework left out WebSocket testin...