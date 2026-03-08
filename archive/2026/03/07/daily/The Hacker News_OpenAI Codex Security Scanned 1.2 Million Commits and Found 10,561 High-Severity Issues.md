---
title: OpenAI Codex Security Scanned 1.2 Million Commits and Found 10,561 High-Severity Issues
url: https://thehackernews.com/2026/03/openai-codex-security-scanned-12.html
source: The Hacker News
date: 2026-03-07
fetch_date: 2026-03-08T04:07:58.320007
---

# OpenAI Codex Security Scanned 1.2 Million Commits and Found 10,561 High-Severity Issues

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

[![Security Service Edge](https://blogger.googleusercontent.com/img/b/R29vZ2xl/AVvXsEguiZ85S7494GyqhFt9uP48C8ggEnb3bp9Qmsdv4LOYjNWfa98MKx17Dk7o1nJrEV3ai3edIGIgwt6oO5iJMmYLcyu6PojcvJnO4IfLhVK2dzGKFyEroFjKQhnp2hd5Cc6G4CynJRfb55aclnGwj7rse9jMncn_vu_tFqQZtHZH3Sb5dMXwRKN-kSVYUMzD/s1700-e365/ai-d.png)](https://thehackernews.uk/wiz-ai-security-d)

# [OpenAI Codex Security Scanned 1.2 Million Commits and Found 10,561 High-Severity Issues](https://thehackernews.com/2026/03/openai-codex-security-scanned-12.html)

**Ravie Lakshmanan**Mar 07, 2026DevSecOps / Artificial Intelligence

[![](data:image/png;base64...)](https://blogger.googleusercontent.com/img/b/R29vZ2xl/AVvXsEgzxRjA2uB_r2z4AtvhADiDGrxTc62766WI5jApivjtuLfb2aS2kz9RWk7f9P3Lm7Nj5HH3u-7Etx4-8xr_Y4PflexsuMsAzXjvPoPLSQaSt1O-t4U3yBAnKm4HLm-64dbHDsWF-EXYVMvaMrMnhfbhV_qn2cvwmJE6x-U42aTjGbIOTNOXxpiH3x15C6Ag/s1700-e365/codex.jpg)

OpenAI on Friday began rolling out **Codex Security**, an artificial intelligence (AI)-powered security agent that's designed to find, validate, and propose fixes for vulnerabilities.

The feature is available in a research preview to ChatGPT Pro, Enterprise, Business, and Edu customers via the Codex web with free usage for the next month.

"It builds deep context about your project to identify complex vulnerabilities that other agentic tools miss, surfacing higher-confidence findings with fixes that meaningfully improve the security of your system while sparing you from the noise of insignificant bugs," the company [said](https://openai.com/index/codex-security-now-in-research-preview/).

Codex Security represents an evolution of [Aardvark⁠](https://thehackernews.com/2025/10/openai-unveils-aardvark-gpt-5-agent.html), which OpenAI unveiled in private beta in October 2025 as a way for developers and security teams to detect and fix security vulnerabilities at scale.

[![Cybersecurity](data:image/png;base64...)](https://thehackernews.uk/not-fast-enough-d)

Over the last 30 days, Codex Security has scanned more than 1.2 million commits across external repositories over the course of the beta, identifying 792 critical findings and 10,561 high-severity findings. These include vulnerabilities in various open-source projects like OpenSSH⁠, GnuTLS⁠, GOGS⁠, Thorium⁠, libssh, PHP, and Chromium, among others. Some of them have been listed below -

* GnuPG - CVE-2026-24881, CVE-2026-24882
* GnuTLS - CVE-2025-32988, CVE-2025-32989
* GOGS - CVE-2025-64175, CVE-2026-25242
* [Thorium](https://www.cisa.gov/resources-tools/resources/thorium) - CVE-2025-35430, CVE-2025-35431, CVE-2025-35432, CVE-2025-35433, CVE-2025-35434, CVE-2025-35435, CVE-2025-35436

According to the AI company, the latest iteration of the application security agent leverages the reasoning capabilities of its frontier models and combines them with automated validation to minimize the risk of false positives and deliver actionable fixes.

OpenAI's scans on the same repositories over time have demonstrated increasing precision and declining false positive rates, with the latter falling by more than 50% across all repositories.

In a statement shared with The Hacker News, OpenAI said Codex Security is designed to improve signal-to-noise by grounding vulnerability discovery in system context and validating findings before surfacing them to users.

Specifically, the agent works in three steps: it analyzes a repository to get a handle on the project's security-relevant structure of the system and generates an editable threat model that captures what it does and where it's most exposed.

Once the system context is built, Codex Security uses it as a foundation to identify vulnerabilities and classifies findings based on their real-world impact. The flagged issues are pressure-tested in a sandboxed environment to validate them.

[![Cybersecurity](data:image/png;base64...)](https://thehackernews.uk/xm-cyber-comm-d)

"When Codex Security is configured with an environment tailored to your project, it can validate potential issues directly in the context of the running system," OpenAI said. "That deeper validation can reduce false positives even further and enable the creation of working proofs-of-concept, giving security teams stronger evidence and a clearer path to remediation."

The final stage involves the agent proposing fixes that best align with the system behavior so as to reduce regressions and make them easier to review and deploy.

News of Codex Security comes weeks after Anthropic launched [Claude Code Security](https://thehackernews.com/2026/02/anthropic-launches-claude-code-security.html) to help users scan a software codebase for vulnerabilities and suggest patches.

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

[Application Security](https://thehackernews.com/search/label/Application%20Security), [artificial intelligence](https://thehackernews.com/search/label/artificial%20intelligence), [cybersecurity](https://thehackernews.com/search/label/cybersecurity), [DevSecOps](https://thehackernews.com/search/label/DevSecOps), [Open Source](https://thehackernews.com/search/label/Open%20Source), [OpenAI](https://thehackernews.com/search/label/OpenAI), [secure coding](https://thehackernews.com/search/label/secure%20coding), [software development](https://thehackernews.com/search/label/software%20development), [Vulnerability](https://thehackernews.com/search/label/Vulnerability)

Trending News

[![Researchers Show Copilot and Grok Can Be Abused as Malware C2 Proxies](data:image/svg+xml;base64... "Researche...