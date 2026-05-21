---
title: Microsoft Open-Sources RAMPART and Clarity to Secure AI Agents During Development
url: https://thehackernews.com/2026/05/microsoft-open-sources-rampart-and.html
source: The Hacker News
date: 2026-05-20
fetch_date: 2026-05-21T06:04:42.857735
---

# Microsoft Open-Sources RAMPART and Clarity to Secure AI Agents During Development

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

# [Microsoft Open-Sources RAMPART and Clarity to Secure AI Agents During Development](https://thehackernews.com/2026/05/microsoft-open-sources-rampart-and.html)

**Ravie Lakshmanan**May 20, 2026Artificial Intelligence / Security Testing

[![Secure AI Agents](data:image/png;base64... "Secure AI Agents")](https://blogger.googleusercontent.com/img/b/R29vZ2xl/AVvXsEheh8SBZDUM83ug6w9EopUahk6CPc27TOD5qpmZWVC8hDMYM-8wdgTLXt1KHv_66Q061_5gm3crZszZf-UvSWWZKb6Aax7BxJ5gzPEyfQTp9JPEcNUmLZnEBD3YuFHoqCU4stvSdSVON7hFJq4ZYb4Rdq1vyOK0VUURDjUpCcEP9_SN5xkQckqwaFS_-dQz/s1700-e365/mss.jpg)

Microsoft has unveiled two new open-source tools called **RAMPART** and **Clarity** to assist developers in better testing the security of artificial intelligence (AI) agents.

[RAMPART](https://github.com/microsoft/RAMPART), short for Risk Assessment and Measurement Platform for Agentic Red Teaming, functions as a Pytest-native safety and security testing framework for writing and running safety and security tests for AI agents, covering both adversarial and benign issues, as well as various harm categories.

Users can write test cases to attack or probe an AI agent to explore possible safety violations like cross-prompt injections, where untrusted data reaches an AI system indirectly via a data source (e.g., email, file, or a web page) processed by it, or unintended behavioral regressions and data exfiltration.

RAMPART then evaluates the outcome of those tests and reports the results. All it needs is an adapter that connects an agent to the test suite. The tool builds on [PyRIT](https://thehackernews.com/2024/02/microsoft-releases-pyrit-red-teaming.html) (short for Python Risk Identification Tool), which Microsoft released more than two years ago as a way to test AI systems.

[Clarity](https://github.com/microsoft/clarity-agent/), on the other hand, has been described by the tech giant as a "structured sounding board" to help developers arrive at the right approach even before writing a single line of code. It's an "AI thinking partner that pushes back," guiding them through problem clarification, solution exploration, failure analysis, and decision tracking.

[![Cybersecurity](data:image/png;base64...)](https://thehackernews.uk/ai-cant-stop-d)

In publicly releasing these tools, Microsoft said the idea is to address why certain decisions are incorporated at an early stage of software development so that any potential issue - for example, an agent's access to a tool - is addressed well before the system is built.

"We wanted to give product managers and engineers a way to pressure-test their assumptions at the start of a project, when changing course is cheap and the right conversation can save months of rework," [Ram Shankar Siva Kumar](https://www.ram-shankar.com/bio), a Data Cowboy and founder of Microsoft's AI Red Team, [said](https://www.microsoft.com/en-us/security/blog/2026/05/20/introducing-rampart-and-clarity-open-source-tools-to-bring-safety-into-agent-development-workflow/) in a blog shared with The Hacker News.

Microsoft noted that a secondary motivation behind investing in these tools is to make incidents reproducible and mitigations verifiable and scale the learnings from red teaming exercises by turning them into runnable engineering assets.

"Where PyRIT is optimized for black-box discovery by security researchers after the system is built, RAMPART is built for engineers as the system is being built," Siva Kumar added. "Clarity helps teams clarify design intent and capture assumptions. Together, these approaches move AI safety from a one-time review to a set of living artifacts that developers can use throughout the lifecycle."

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

[AI Agent](https://thehackernews.com/search/label/AI%20Agent), [artificial intelligence](https://thehackernews.com/search/label/artificial%20intelligence), [cybersecurity](https://thehackernews.com/search/label/cybersecurity), [Microsoft](https://thehackernews.com/search/label/Microsoft), [Open Source](https://thehackernews.com/search/label/Open%20Source), [Prompt Injection](https://thehackernews.com/search/label/Prompt%20Injection), [Red Teaming](https://thehackernews.com/search/label/Red%20Teaming), [Security Testing](https://thehackernews.com/search/label/Security%20Testing)

⚡ Top Stories This Week

[![Ollama Out-of-Bounds Read Vulnerability Allows Remote Process Memory Leak](data:image/svg+xml;base64... "Ollama Out-of-Bounds Read Vulnerability Allows Remote Process Memory Leak")

Ollama Out-of-Bounds Read Vulnerability Allows Remote Process Memory Leak](https://thehackernews.com/2026/05/ollama-out-of-bounds-read-vulnerability.html)

[![Four OpenClaw Flaws Enable Data Theft, Privilege Escalation, and Persistence](data:image/svg+xml;base64... "Four OpenClaw Flaws Enable Data Theft, Privilege Escalation, and Persistence")

Four OpenClaw Flaws Enable Data Theft, Privilege Escalation, and Persistence](https://thehackernews.com/2026/05/four-openclaw-flaws-enable-data-theft.html)

[![On-Prem Microsoft Exchange Server CVE-2026-42897 Exploited via Crafted Email](data:image/svg+xml;base64... "On-Prem Microsoft Exchange Server CVE-2026-42897 Exploited via Crafte...