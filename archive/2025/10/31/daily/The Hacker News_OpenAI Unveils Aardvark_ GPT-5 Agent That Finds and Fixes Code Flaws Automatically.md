---
title: OpenAI Unveils Aardvark: GPT-5 Agent That Finds and Fixes Code Flaws Automatically
url: https://thehackernews.com/2025/10/openai-unveils-aardvark-gpt-5-agent.html
source: The Hacker News
date: 2025-10-31
fetch_date: 2025-11-01T03:13:08.353832
---

# OpenAI Unveils Aardvark: GPT-5 Agent That Finds and Fixes Code Flaws Automatically

#1 Trusted Cybersecurity News Platform

Followed by 5.20+ million[**](https://twitter.com/thehackersnews)
[**](https://www.linkedin.com/company/thehackernews/)
[**](https://www.facebook.com/thehackernews)

[![The Hacker News Logo](data:image/png;base64...)](/)

**

**

[** Subscribe – Get Latest News](#email-outer)

* [** Home](/)
* [** Newsletter](#email-outer)
* [** Webinars](/p/upcoming-hacker-news-webinars.html)

* [Home](/)
* [Data Breaches](/search/label/data%20breach)
* [Cyber Attacks](/search/label/Cyber%20Attack)
* [Vulnerabilities](/search/label/Vulnerability)
* [Webinars](/p/upcoming-hacker-news-webinars.html)
* [Expert Insights](https://thehackernews.com/expert-insights/)
* [Contact](/p/submit-news.html)

**

**

**

Resources

* [Webinars](/p/upcoming-hacker-news-webinars.html)
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

[![Salesforce Security Handbook](https://blogger.googleusercontent.com/img/b/R29vZ2xl/AVvXsEhjMQkm7Ao3yQkNVeqy3au4G4E34VWzSsT55GDPjHHGjbHksJqrJCyM1ChO1hB9WzaFzZcwNTn8fOLN8b3U599XinIlPZBBqNnwZYJFQD0i2dLVdAjszjU-a3Y0iLd5UHOg0H9-IFtS0nGf4MeOGk4NsNNAq-pMpFpi_aZrXHGV7UgoEEOlkFGBW5HOsJFC/s728-e100/zz--header-d.png)](https://thehackernews.uk/zz--header-d)

# [OpenAI Unveils Aardvark: GPT-5 Agent That Finds and Fixes Code Flaws Automatically](https://thehackernews.com/2025/10/openai-unveils-aardvark-gpt-5-agent.html)

**Oct 31, 2025**Ravie LakshmananArtificial Intelligence / Code Security

[![](data:image/png;base64...)](https://blogger.googleusercontent.com/img/b/R29vZ2xl/AVvXsEi1qKVY4KhOkzIkeCDV1BiboPN3n7qh-ElZ2YzQyfHE2ctgVFmcv7KPDcx1Chvc3KxNeMuirmxfoFRlOb_YAPkCds2Pw9H0_dOPmrJPFfmGFglSXLIM6Ycu0nesaNh8hfTvfQ7lKTAp-GOCaRJylT-wId8Sb_urjjXxpqVgkrjUZ4VJboCJ7Fhk4yVZpOiS/s790-rw-e365/flaws.jpg)

OpenAI has announced the launch of an "agentic security researcher" that's powered by its GPT-5 large language model (LLM) and is programmed to emulate a human expert capable of scanning, understanding, and patching code.

Called **Aardvark**, the artificial intelligence (AI) company said the autonomous agent is designed to help developers and security teams flag and fix security vulnerabilities at scale. It's currently available in private beta.

"Aardvark continuously analyzes source code repositories to identify vulnerabilities, assess exploitability, prioritize severity, and propose targeted patches," OpenAI [noted](https://openai.com/index/introducing-aardvark/).

It works by embedding itself into the software development pipeline, monitoring commits and changes to codebases, detecting security issues and how they might be exploited, and proposing fixes to address them using LLM-based reasoning and tool-use.

[![DFIR Retainer Services](data:image/png;base64...)](https://thehackernews.uk/endpoint-protect-d)

Powering the agent is [GPT‑5](https://openai.com/index/introducing-gpt-5/), which OpenAI introduced in August 2025. The company describes it as a "smart, efficient model" that features deeper reasoning capabilities, courtesy of GPT‑5 thinking, and a "real‑time router" to decide the right model to use based on conversation type, complexity, and user intent.

Aardvark, OpenAI added, analyses a project's codebase to produce a threat model that it thinks best represents its security objectives and design. With this contextual foundation, the agent then scans its history to identify existing issues, as well as detect new ones by scrutinizing incoming changes to the repository.

Once a potential security defect is found, it attempts to trigger it in an isolated, sandboxed environment to confirm its exploitability and leverages [OpenAI Codex](https://openai.com/index/introducing-codex/), its coding agent, to produce a patch that can be reviewed by a human analyst.

OpenAI said it's been running the agent across OpenAI's internal codebases and some of its external alpha partners, and that it has helped identify at least 10 CVEs in open-source projects.

The AI upstart is far from the only company to trial AI agents to tackle automated vulnerability discovery and patching. Earlier this month, Google announced [CodeMender](https://thehackernews.com/2025/10/googles-new-ai-doesnt-just-find.html) that it said detects, patches, and rewrites vulnerable code to prevent future exploits. The tech giant also noted that it intends to work with maintainers of critical open-source projects to integrate CodeMender-generated patches to help keep projects secure.

[![CIS Build Kits](data:image/png;base64...)](https://thehackernews.uk/platform-shield-d)

Viewed in that light, Aardvark, CodeMender, and [XBOW](https://xbow.com) are being positioned as tools for continuous code analysis, exploit validation, and patch generation. It also comes close on the heels of OpenAI's release of the [gpt-oss-safeguard models](https://openai.com/index/introducing-gpt-oss-safeguard/) that are fine-tuned for safety classification tasks.

"Aardvark represents a new defender-first model: an agentic security researcher that partners with teams by delivering continuous protection as code evolves," OpenAI said. "By catching vulnerabilities early, validating real-world exploitability, and offering clear fixes, Aardvark can strengthen security without slowing innovation. We believe in expanding access to security expertise."

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

[artificial intelligence](https://thehackernews.com/search/label/artificial%20intelligence)[Code Security](https://thehackernews.com/search/label/Code%20Security)[cybersecurity](https://thehackernews.com/search/label/cybersecurity)[DevSecOps](https://thehackernews.com/search/label/DevSecOps)[machine learning](https://thehackernews.com/search/label/machine%20learning)[OpenAI](https://thehackernews.com/search/label/OpenAI)[software development](https://thehackernews.com/search/label/software%20development)[threat detection](https://thehackernews.com/search/label/threat%20detection)[Vulnerability](https://thehackernews.com/search/label/Vulnerability)

[![c](data:image/svg+xml;base64...)](https://thehackernews.uk/wiz-ai-security)

Trending News

[![⚡ Weekly Recap: WSUS Exploited, LockBit 5.0 Returns, Telegram Backdoor, F5 Breach Widens](data:image/svg+xml;base64... "⚡ Weekly Recap: WSUS Exploited, LockBit 5.0 Returns, Telegram Backdoor, F5 Breach Widens")

⚡ Weekly Recap: WSUS Exploited, LockBit 5.0 Returns, Telegram Backdoor, F5 Breach Widens](https://thehackernews.com/2025/10/weekly-rec...