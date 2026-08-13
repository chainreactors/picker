---
title: OpenAI, Anthropic, Google API Flaw Let Weaker AI Models Decode Stronger Models' Reasoning
url: https://thehackernews.com/2026/08/openai-anthropic-google-api-flaw-let.html
source: The Hacker News
date: 2026-08-12
fetch_date: 2026-08-13T04:05:20.749689
---

# OpenAI, Anthropic, Google API Flaw Let Weaker AI Models Decode Stronger Models' Reasoning

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

![cybersecurity](data:image/svg+xml;base64...)

# [OpenAI, Anthropic, Google API Flaw Let Weaker AI Models Decode Stronger Models' Reasoning](https://thehackernews.com/2026/08/openai-anthropic-google-api-flaw-let.html)

**Swati Khandelwal**Aug 12, 2026Vulnerability / Artificial Intelligence

[![](data:image/png;base64...)](https://blogger.googleusercontent.com/img/b/R29vZ2xl/AVvXsEiZP21lJn1EY_0JXWBul8gpBgRD_ryI4ACYqFiu6icbKCgIMyta9UqjQrtnzjTkO1Yi9tdzTaQw6X949lzMwtQPKUPPIxA5_EwFjJqjMDwBtFSc56vaCyybwJNcsjVZMfMW4KHQ_VVCjz3AVeovFEtsI8ENZTQmQuc9rDIF5yd0n9uciJmwqlWS_EKf5mo/s1700-e365/ai-models.jpg)

A newly disclosed flaw in the way OpenAI, Anthropic, and Google carried hidden AI reasoning between API calls let researchers recover internal reasoning and secrets from session logs, including API keys and passwords.

The weakness affected encrypted reasoning objects used by the providers' reasoning APIs, where a block created in one session could be replayed into another and, during testing, even handed to a weaker model in the same provider family to make it reveal the hidden content.

The team behind the paper [Stealing Reasoning Traces from Proprietary LLM APIs](https://arxiv.org/abs/2608.09867) demonstrated four abuse paths: stealing proprietary reasoning for [model distillation](https://thehackernews.com/2026/02/anthropic-says-chinese-ai-firms-used-16.html), extracting private data from other users' published traces, recovering harmful content concealed behind a safe visible answer, and hiding prompt injections inside opaque reasoning blocks.

Across 6,708 public agent trajectories, the team decoded 315,320 thinking blocks. After excluding benchmark sources, it counted 704 distinct privacy artifacts from genuine user sessions, including 62 API keys, 33 passwords, 24 access tokens, and seven private keys.

The cross-user attack did not provide arbitrary access to private chats. It required obtaining an encrypted reasoning block, such as one published in an agent log, and API access to a compatible model from the same provider.

[![Cybersecurity](data:image/png;base64...)](https://thehackernews.uk/zero-trust-claude-d)

The researchers disclosed the findings to the affected model providers, Microsoft and Hugging Face, and say the demonstrated attacks stopped working after mitigations. Their reproducibility statement says the main extraction attack is no longer reproducible as of August 2026.

The report does not document malicious exploitation in the wild. Developers are advised to strip reasoning blocks and opaque reasoning fields from shared traces and avoid committing raw API transcripts even when the visible text has been sanitized.

The problem starts with a design meant to preserve reasoning across API calls when conversation state is managed manually or statelessly. [OpenAI](https://developers.openai.com/api/docs/guides/latest-model) can return encrypted reasoning items that applications replay with manually managed history, [Anthropic](https://platform.claude.com/docs/en/about-claude/models/extended-thinking-models) carries full reasoning in an encrypted signature, and [Google](https://ai.google.dev/gemini-api/docs/thought-signatures) uses encrypted thought signatures. These objects preserve reasoning state without exposing the underlying plaintext directly to the client.

[![](data:image/png;base64...)](https://blogger.googleusercontent.com/img/b/R29vZ2xl/AVvXsEi9ckZttZUDJEbJh_9xT_qN6_JPPUQOBa2Xu98giv7kG0BuyDz1WjvULOoli2GiecUQo63CW6PFeUMNRGB72N_aCc3SOuKRNW4ri9zL3wTlKdR0E_enVXSpzI10hz_iRSksoOYdwwbpKnILPHJqPUZcRJByn-cQssUmBm3aon5WSfbeq8dduhII1QBAvgs/s1700-e365/claude.jpg)

The encryption itself was not cracked, and the attack did not require obtaining an encryption key. It relied on intact opaque blocks being accepted and processed by the provider.

During testing, the paper found those objects portable across sessions, users, and models, allowing a weaker compatible model to act as what the authors call a "fuzzy" decoder: Claude Haiku 4.5 for Claude traces, GPT-5.6 Luna for GPT traces, and Gemini Robotics ER-1.6 for Gemini traces. The decoder was prompted to transcribe reasoning produced by a stronger model.

That cross-user behavior turns published agent logs into the sharper security problem. Of the 704 non-benchmark artifacts the team recovered, 64 appeared only in hidden reasoning and nowhere in the visible trace. Sanitizing the readable conversation could therefore leave secrets inside an opaque block that another account was able to replay.

The exposure the study demonstrates is bounded: it lands on developers who published raw agent logs with the reasoning objects intact, one identifiable group rather than every API user, and not necessarily the only one at risk.

The same portability also enabled an invisible prompt-injection proof of concept. The team crafted an opaque reasoning block that carried a malicious instruction and later replayed it into an unrelated task, causing the receiving model to add an attacker-directed upload action without putting the injected instruction in visible text.

The authors caution that they do not have ground-truth plaintext for the proprietary reasoning, so they cannot guarantee every reconstructed trace is an exact copy. Their fidelity checks relied on reasoning-token counts and qualitative comparisons, with extracted lengths generally tracking the providers' reported thinking-token counts.

[![Cybersecurity](data:image/png;base64...)](https://thehackernews.uk/corelight-d)

Current vendor documentation shows that encrypted reasoning remains part of these APIs, but handling has changed. OpenAI still tells developers to replay encrypted reasoning items when manually managing stateless history, while Google says its backend manages thought compatibility when a session switches models.

Anthropic now says thinking blocks are tied to the model that produced them and should be stripped when switching models because other models ignore them.

Several questions the disclosure raises are left open by the public record. No public acknowledgment of the flaw from any of the three providers has surfaced so far, and none has tied its current documentation to this research, so the account that the demonstrated attacks no longer work rests on the researchers' own reproducibility statement rather than on v...