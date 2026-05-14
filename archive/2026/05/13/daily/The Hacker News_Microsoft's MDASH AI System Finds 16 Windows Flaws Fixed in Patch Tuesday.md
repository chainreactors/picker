---
title: Microsoft's MDASH AI System Finds 16 Windows Flaws Fixed in Patch Tuesday
url: https://thehackernews.com/2026/05/microsofts-mdash-ai-system-finds-16.html
source: The Hacker News
date: 2026-05-13
fetch_date: 2026-05-14T05:47:23.528053
---

# Microsoft's MDASH AI System Finds 16 Windows Flaws Fixed in Patch Tuesday

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

[![cybersecurity](https://blogger.googleusercontent.com/img/b/R29vZ2xl/AVvXsEhyqUz0-ifa8jE9rCzud3wzxmhcuzTp1VOWFEvGMoZXDYfaB_4459fPyvyQw7wvAnzjzDL09PkyJM83QGheO69fC3esg1WA7WnJ89i_t_q3K8DxYmgV__QujU8RWRnCK4MpbKqu8nwuMFfLaiRVHy_ov7IZ16hoKI3rIu-5BcISmqXPjlQU7N0sa4lWI-n-/s728-e100/wiz-d.png)](https://thehackernews.uk/wiz-ai-state-d)

# [Microsoft's MDASH AI System Finds 16 Windows Flaws Fixed in Patch Tuesday](https://thehackernews.com/2026/05/microsofts-mdash-ai-system-finds-16.html)

**Ravie Lakshmanan**May 13, 2026Vulnerability / Artificial Intelligence

[![](data:image/png;base64...)](https://blogger.googleusercontent.com/img/b/R29vZ2xl/AVvXsEg1Iq16GS3jdGiIU24GHBkwg6unk05ctdgYwXO5df8zRu1qko95_XhszCjq6jlEIRozLsrtZHgi5GqDZnS1Sw_KDzUzsagwP0If3VswmYHsnuYwVseU2lapxQiPpItTdAiv-CCdTFR87ZVOu65buyvmvzmdWuJPKHuPA4DSo58HQIMAV__2ymsmRe2g3UVe/s1700-e365/windows-ai.jpg)

Microsoft has unveiled a new multi-model artificial intelligence (AI)-driven system called **MDASH** to facilitate vulnerability discovery and remediation at scale, adding that it's being tested by some customers as part of a limited private preview.

MDASH, short for **m**ulti-mo**d**el **a**gentic **s**canning **h**arness, is designed as a model-agnostic system that uses bespoke AI agents for different vulnerability classes to autonomously discover, validate, and prove exploitable defects in complex codebases like Windows.

"Unlike single-model approaches, the harness orchestrates more than 100 specialized AI agents across an ensemble of frontier and distilled models to discover, debate, and prove exploitable bugs end-to-end," Taesoo Kim, vice president of agentic security at Microsoft, [said](https://www.microsoft.com/en-us/security/blog/2026/05/12/defense-at-ai-speed-microsofts-new-multi-model-agentic-security-system-tops-leading-industry-benchmark/).

[![Cybersecurity](data:image/png;base64...)](https://thehackernews.uk/ai-cant-stop-d)

MDASH is envisioned as a "structured pipeline" that ingests a codebase and produces validated, proven findings through a series of actions.

It starts with analyzing the source code to build a threat model and attack surface, running specialized "auditor" agents over candidate code paths to flag potential issues, running a second set of "debater" agents that validate the findings, grouping semantically equivalent findings, and then finally proving the existence of the vulnerabilities.

The system is powered by a configurable panel of models, with state-of-the-art (SOTA) models used for reasoning, distilled models for validation for high-volume passes, and a second separate SOTA model for independent counterpoint.

"Disagreement between models is itself a signal: when an auditor flags something as suspect and the debater can't refute it, that finding’s posterior credibility goes up," Microsoft explained. "An auditor does not reason like a debater, which does not reason like a prover. Each pipeline stage has its own role, prompt regime, tools, and stop criteria."

Redmond noted that the specialized agents have been constructed based on past common vulnerabilities and exposures (CVEs) and their patches. It also said the architecture allows for portability across model generations.

[![](data:image/png;base64...)](https://blogger.googleusercontent.com/img/b/R29vZ2xl/AVvXsEhH6N60CGLSE6IAFBHjgwPACpNx54RIaa2nfqXvq41uLiHcHX20E2GLFzzM9zqCC5aceI8GB9qk7w675a-dy32FQaJsZNW84kPt-1NpAuwhqxTpC-P-DRNYeBBYLni_D4I3WyZhVqznHU4fYlTWUDJHw7kgPHnTAxSc9wKqt6DV2vTkwlSLdITRIO4H4hR6/s1700-e365/cyber-ms.jpg)

MDASH has already been put to test, unearthing 16 of the vulnerabilities that were fixed in this month's Patch Tuesday release. The shortcomings span across the Windows networking and authentication stack, including two critical flaws that could pave the way for remote code execution -

* **[CVE-2026-33824](https://msrc.microsoft.com/update-guide/en-US/vulnerability/CVE-2026-33824)** (CVSS score: 9.8) - A double-free vulnerability in "ikeext.dll" that could allow an unauthenticated attacker to send specially crafted packets to a Windows machine with Internet Key Exchange (IKE) version 2 enabled, leading to remote code execution.
* **[CVE-2026-33827](https://msrc.microsoft.com/update-guide/en-US/vulnerability/CVE-2026-33827)** (CVSS score: 8.1) - A race condition vulnerability in Windows TCP/IP ("tcpip.sys") that allows an unauthorized attacker to send a specially crafted IPv6 packet to a Windows node where IPSec is enabled, leading to remote code execution exploitation.

News of MDASH follows the debut of Anthropic's [Project Glasswing](https://thehackernews.com/2026/04/anthropics-claude-mythos-finds.html) and OpenAI [Daybreak](https://thehackernews.com/2026/05/openai-launches-daybreak-for-ai-powered.html), both of which are AI-powered cybersecurity initiatives for accelerating vulnerability discovery, validation, and remediation before they can be discovered by bad actors.

"The strategic implication is clear: AI vulnerability discovery has crossed from research curiosity into production-grade defense at enterprise scale, and the durable advantage lies in the agentic system around the model rather than any single model itself," Kim said.

Found this article interesting? Follow us on [Google News](https://news.google.com/publications/CAAqLQgKIidDQklTRndnTWFoTUtFWFJvWldoaFkydGxjbTVsZDNNdVkyOXRLQUFQAQ), [Twitter](https://twitter.com/thehackersnews) and [LinkedIn](https://www.linkedin.com/company/thehackernews/) to read more exclusive content we post.

SHARE
[**](#link_share)
[**](#link_share)
[**](#link_share)
**

[**Tweet](#link_share)

[**Share](#link_share)

[**Share](#link_share)

**Share

**
[**Share on Facebook](#link_share)
[**Share on Twitter](#link_share)
[**Share on Linkedin](#link_share)
[**Share on Reddit](#link_share)
[**Share on Hacker News](#link_share)
[**Share on Email](#link_share)
[**Share on WhatsApp](#link_share)
[![Facebook Messenger](data:image/png;base64...)Share on Facebook Messenger](#link_share)
[**Share on Telegram](#link_share)

SHARE **

[artificial intelligence](https://thehackernews.com/search/label/artificial%20intelligence), [cybersecurity](https://thehackernews.com/search/label/cybersecurity), [Microsoft](https://thehackernews.com/search/label/Microsoft), [patch Tuesday](https://thehackernews.com/search/label/patch%2...