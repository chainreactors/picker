---
title: World's Largest AI Model Repository Hugging Face Breached by Autonomous AI Agent
url: https://thehackernews.com/2026/07/worlds-largest-ai-model-repository.html
source: The Hacker News
date: 2026-07-20
fetch_date: 2026-07-21T05:03:17.658677
---

# World's Largest AI Model Repository Hugging Face Breached by Autonomous AI Agent

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

[![cybersecurity](https://blogger.googleusercontent.com/img/b/R29vZ2xl/AVvXsEgrKWHErc__Wn0forfQ5eJ5sIR1hVKCHCTeNQOaAX4lbygJ8S1Xpemx6JXl78dpwiT65DDBGURp48A3EemKzmli-jXPI3v1928MnJm-1j2ZPUaFXCvuySFhyphenhyphenKR-Li6fAinFT2bhLgsqUSNUR_ggMAnOHi3jD1qYWHXvueX8WdtxAd6GYety9cBGYABo18hX/s728-e100/tt-d.jpg)](https://thehackernews.uk/ai-zero-trust-h-d)

# [World's Largest AI Model Repository Hugging Face Breached by Autonomous AI Agent](https://thehackernews.com/2026/07/worlds-largest-ai-model-repository.html)

**Ravie Lakshmanan**Jul 20, 2026AI Security / Vulnerability

[![](data:image/png;base64...)](https://blogger.googleusercontent.com/img/b/R29vZ2xl/AVvXsEhehTKRdIydGsJI5vxP4R5baH5VrDh8ZNLg1RyLMhSnVOFr6cdDZRyqkKhazs4oBdZxw5YV7fNYKCcZ9tkKkTap2chfMR6XCdiG4GmUhv4S_tUVYTS7jvn8iZcTL3RuJ-3K0U1WJ0pKfq16pcJRZhAXTm1gk-xvzjzmdJ85PWEgnQ6oFK1eUPKRBiTRtEr1/s1700-e365/huggingface.jpg)

In an ironic twist, open-source artificial intelligence (AI) platform Hugging Face revealed that it was the victim of a hack perpetrated by an autonomous AI agent system.

The company said it detected and responded to the incident targeting its production infrastructure earlier last week.

"We identified unauthorized access to a limited set of internal datasets and to several credentials used by our services," the company [said](https://huggingface.co/blog/security-incident-july-2026) in a statement.

While an investigation into the intrusion remains ongoing, Hugging Face said it has found no evidence that the AI agent tampered with public, user-facing models, datasets, or Spaces, and its own software supply chain.

[![Cybersecurity](data:image/png;base64...)](https://thehackernews.uk/ai-vuln-protection-d)

The starting point of the attack was the data processing pipeline itself, with a malicious dataset abusing two code execution paths, viz., in its remote code dataset loader and a template injection in a dataset configuration, to run code on a processing worker.

With that access, the threat actor is said to have escalated to node-level access, collected cloud and cluster credentials, and moved laterally into several internal clusters over a weekend.

The exact large language model (LLM) used to pull off the attack is unclear, but the campaign was executed by an autonomous agent framework performing "many thousands of individual actions across a swarm of short-lived sandboxes, with self-migrating command-and-control staged on public services."

Hugging Face said it has since addressed the root cause of the issue, precisely the code execution pathways used for initial access. It also carried out the following remediation steps -

* Removed the attacker's foothold across the affected clusters and rebuilt the compromised nodes
* Revoked and rotated the affected credentials and tokens, and a broader rotation of secrets was undertaken as a precautionary measure.
* Deployed additional guardrails and stricter admission controls on its clusters
* Improved detection and alerting to ensure responders are notified within minutes, 24x7

As a further safeguard, Hugging Face is urging customers to rotate any access tokens and review recent activity on their accounts.

[![Cybersecurity](https://blogger.googleusercontent.com/img/b/R29vZ2xl/AVvXsEiBxLQDy7VdLze43eMmpRllTXaPKPfB_veNUxQlqIu3-68GBJtegkhDGCqtaiSymOQviROdxln1FSd4zdMp5Jv9jeF1xQxLPc9uo9H7zW2nWHNax0wT0Y8JRj-zyUfbaCLqhxSfQT2sCfhWMBPL6UVgsh5RYVNVxwus_mW_BY9Ptwz3z7iF0_LWOnte-gqg/s1600/sy-d-1.jpg)](https://thehackernews.uk/sygnia-cyber-response-d-1)

The company also said it turned to Z.ai's [GLM 5.2](https://z.ai/blog/glm-5.2), a Chinese open-weight model, to conduct the forensic analysis after Western frontier models refused requests containing real attack commands, exploit payloads, and command-and-control (C2) artifacts because their safety guardrails were triggered and owing to their inability to differentiate between an attacker and a legitimate incident response effort.

"This experience points to a gap worth planning for," the New York-headquartered company said. "We do not know which model powered the attacker's agents, whether a jailbroken hosted model or an unrestricted open-weight one; either way, the attacker was bound by no usage policy, while our own forensic work was blocked by the guardrails of the hosted models we first tried."

"The practical lesson for defenders: have a capable model you can run on your own infrastructure vetted and ready before an incident, both to avoid guardrail lockout and to keep attacker data and credentials from leaving your environment."

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

[AI Security](https://thehackernews.com/search/label/AI%20Security), [Cloud security](https://thehackernews.com/search/label/Cloud%20security), [Code Execution](https://thehackernews.com/search/label/Code%20Execution), [Credential Theft](https://thehackernews.com/search/label/Credential%20Theft), [Cyber Attack](https://thehackernews.com/search/label/Cyber%20Attack), [data breach](https://thehackernews.com/search/label/data%20breach), [Incident response](https://thehackernews.com/search/label/Incident%20response), [Infrastructure Security](https://thehackernews.com/search/label/Infrastructure%20Security), [Open Source](https://thehackernews.com/search/label/Open%20Source), [Vulnerability](https://thehackernews.com/search/label/Vulnerability)

⚡ Top Stories This Week

[![URGENT - Progress Tells ShareFile Customers to Shut Down Storage Zone Controllers Over Security Threat](data:image/svg+xml;base64... "URGENT - Pro...