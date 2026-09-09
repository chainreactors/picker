---
title: What It Took to Reach 1 Billion Build Manifests
url: https://thehackernews.com/2026/09/what-it-took-to-reach-1-billion-build.html
source: The Hacker News
date: 2026-09-08
fetch_date: 2026-09-09T06:56:58.702422
---

# What It Took to Reach 1 Billion Build Manifests

#1 Trusted Cybersecurity News Platform

Followed by 5.70+ million[**](https://twitter.com/thehackersnews)
[**](https://www.linkedin.com/company/thehackernews/)
[**](https://www.facebook.com/thehackernews)

[![The Hacker News Logo](data:image/png;base64...)](/)

**

**

[** Get the Latest News](#email-outer)

* [Home](/)
* [Newsletter](#email-outer)
* [Webinars](/p/upcoming-hacker-news-webinars.html)

* [Home](/)
* [Threat Intelligence](/search/label/Threat%20Intelligence)
* [Vulnerabilities](/search/label/Vulnerability)
* [Cyber Attacks](/search/label/Cyber%20Attack)
* [Webinars](/p/upcoming-hacker-news-webinars.html)
* [Expert Insights](https://thehackernews.com/expert-insights/)
* [Awards](https://awards.thehackernews.com/)

**

**

**

Resources

* [Webinars](/p/upcoming-hacker-news-webinars.html)
* [Awards](https://awards.thehackernews.com/)
* [Free eBooks](https://thehackernews.tradepub.com)

About Site

* [About THN](/p/about-us.html)
* [Jobs](/p/careers-technical-writer-designer-and.html)
* [Advertise with us](/p/advertising-with-hacker-news.html)

Contact/Tip Us

[**

Reach out to get featured—contact us to send your exclusive story idea, research, hacks, or ask us a question or leave a comment/feedback!](/p/submit-news.html)

Follow Us On Social Media

[**](https://www.facebook.com/thehackernews)
[**](https://twitter.com/thehackersnews)
[**](https://www.linkedin.com/company/thehackernews/)
[**](https://www.youtube.com/c/thehackernews?sub_confirmation=1)
[**](https://www.instagram.com/thehackernews/)

[** RSS Feeds](https://feeds.feedburner.com/TheHackersNews)
[** Email Alerts](#email-outer)

[![cybersecurity](https://blogger.googleusercontent.com/img/b/R29vZ2xl/AVvXsEiHP9KRFkaxKFUKQNRU3CkfxCyJLEuIfmo6ov7iWHHRBE1ShJKfXdPvozMZMVuvOJipQ8Qbap3UBmtjKvZh-xBqLeUartPWmRuQj2W8nqdCk2_XlYLXpj15R4Du2oJ1nNVPqIuR-TwbMyPQe4gxxCcMYvUMbFO_Nin2OdhyzkJvX8Sn83aEbM1C5sgaaCqI/s728-nu-rw-lo-l85-e365/wiz-sep-d.png)](https://thehackernews.uk/claude-security-guide-d)

# [What It Took to Reach 1 Billion Build Manifests](https://thehackernews.com/2026/09/what-it-took-to-reach-1-billion-build.html)

**The Hacker News**Sep 08, 2026Cloud Security / Artificial Intelligence

[![](data:image/png;base64...)](https://blogger.googleusercontent.com/img/b/R29vZ2xl/AVvXsEiqJEqJ_CCrFzLtmEtLrrIWQv80hyY6xtGfdsad0NgYCYSs-ur2ObfnMgE8uBWlZ7idJHbjDcOwpo8_ESTMpCAWAUHUwbqhVr-zqxV-oxUWmR3PMwBD_vrDziQFaeL0VTzX8NUQRFGRzVQCuTPrvflnepbKlCgqH84MRNTJUhZRNfqwEtmBUxhIB5a8MfeE/s1700-nu-rw-lo-l85-e365/chainguard.jpg)

In the last six months, Chainguard doubled its output from 500 million to more than 1 billion container build manifests. We also surpassed 3,000 unique container images and 675,000 image versions in our catalog. Those are the headline numbers, but I want to share what's actually behind them. The number itself is less interesting than the system that produced it, and why we had to fundamentally rethink that system to get here.

## **What a build manifest actually represents**

Let’s be precise about what we're counting. How do we define a “build manifest”? Think of it as every time the Chainguard Factory produces a new, verifiable artifact: a fresh image for [go:1.26.5](https://images.chainguard.dev/directory/image/go/versions), a rebuild of nginx triggered by a libc patch, a new architecture variant, a regenerated SBOM after a dependency change - all these events cause a new build and therefore new artifacts.

At our scale, a single project like [Python](https://images.chainguard.dev/directory/image/python/versions) might have dozens of supported versions, each with multiple architecture builds, each rebuilt repeatedly as upstream changes, as dependencies patch, and as we harden the base image further. The count shows how our entire catalog stays fresh at any given moment across every project we support.

That distinction is the difference between a catalog that's secure on the day you pull an image and one that's secure every day after. Most vulnerability management is built around the former, but we’re building infrastructure for the latter.

## **How we build**

Everything starts with Chainguard OS, our purpose-built Linux operating system. Chainguard OS is designed for modern, cloud-native workloads and gives us complete control over the software supply chain. Unlike legacy and incumbent Linux distributions, Chainguard OS is designed for continuous software integration and delivery, as well as rapid nano-updates and rebuilds. We capture all the security, functional, and performance updates built by the open source community and deliver them to customers as fast as possible. We are not cutting a release every six months or so, and then letting the distro age. Chainguard OS uses a rolling release and new artifacts ship all day, every day.

Chainguard Factory is the infrastructure and agentic engine that powers this delivery. Every artifact that comes out of the factory has layers of defense and is built from source with SLSA Level 3 provenance, Sigstore signatures, and full SBOMs.

The factory scale and its architecture make rebuilding at this volume possible. Because builds are declarative and reproducible, we can regenerate an image without worrying about hidden state or drift between what we intended to ship and what actually got shipped. But reproducibility alone doesn't get you to a billion build manifests in the timeframe we're talking about. Velocity requires something else: knowing *when* to rebuild, and being able to act on that signal immediately, across thousands of interdependent projects, without a human in the loop for every decision.

## **Why we built Factory 2.0**

The original Chainguard Factory automated the mechanics of building. It would take a package definition, resolve dependencies, build the package, sign it, and ship it. But that architecture was a traditional event-driven system, and as our catalog grew, its limits became impossible to ignore. It devolved into what we internally called a "cascading mess.” SREs were drowning in event notifications, queues grew brittle, and duplicate build failures and work-item conflicts were common. Whenever a task only partially succeeded or hit something unforeseen, it needed a human to step in and fix it. We had to deal with the “CVE doom loop”: no matter how hard the team worked, the infrastructure was constantly fighting configuration drift and decay rather than getting ahead of it.

Factory 2.0, powered by what we call [DriftlessAF](https://github.com/driftlessaf), is our answer to that problem. It's a self-correcting build system that layers agentic, AI-powered reconciliation onto our existing deterministic automation. Concretely, that means:

* **A reconciliation loop:** Rather than reacting to individual events, DriftlessAF continuously compares a desired state against the actual state, and works to close the gap whenever a CVE is reported, a new package version lands upstream, a new best practice is implemented, or we define some other new criteria as desired.
* **A continuous work queue:** A large number of reconciler bots are continuously assigned work from a shared queue, reconciling state discovered from code repositories, security feeds, and other sources to our target state.
* **Redundant by design:** Because every task is working toward a defined end state rather than executing a one-off action, a failed work item can simply be dropped or retried. The system converges on the right outcome eventually, rather than needing every step to succeed the first time.
* **AI where it earns its place:** Reconciler bots use AI specifically to handle the unstructured judgment calls that traditional automation couldn't — things like reasoning about a newly added component in a minor release or backporting a CVE remediation to an older package and language release — while still working through highly structured, verifiable tools to keep the loop from hallucinating its way to a bad outcome. Furthermore, ...