---
title: Researchers Uncover Prompt Adware Hidden in OpenAI Codex Jailbreak Toolkit
url: https://thehackernews.com/2026/11/researchers-uncover-prompt-adware.html
source: The Hacker News
date: 2026-11-04
fetch_date: 2026-11-05T08:45:12.486770
---

# Researchers Uncover Prompt Adware Hidden in OpenAI Codex Jailbreak Toolkit

#1 Trusted Cybersecurity News Platform

Followed by 5.80+ million[**](https://twitter.com/thehackersnews)
[**](https://www.linkedin.com/company/thehackernews/)
[**](https://www.facebook.com/thehackernews)

[![The Hacker News Logo](data:image/png;base64...)](/)

**

**

[Get Updates](#email-outer)

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

[![cybersecurity](https://blogger.googleusercontent.com/img/b/R29vZ2xl/AVvXsEg98jBiF1GNyn9ReXVuuNzrDrJ8-mdCvE5IhR6dUbEnucAAvmCW-lbjZmzjJx0EhFV2R6xhfph0uQ-cz4IO46xmarphU8oOZmuqbdHxTeosFZTJ45LN6VEQOAdLCFB_iwlP3t9_i9qiQqQua1oJMGmp5wILrYvUWRBTMAVJphcDt7Qo0Yi5gK9pIHhW5pAb/s728-nu-rw-lo-l85-e365/wiz-d.png)](https://thehackernews.uk/appsec-ai-readiness-d)

# [Researchers Uncover Prompt Adware Hidden in OpenAI Codex Jailbreak Toolkit](https://thehackernews.com/2026/11/researchers-uncover-prompt-adware.html)

**Ravie Lakshmanan**Nov 04, 2026Artificial Intelligence / Cybersecurity

[![](data:image/png;base64...)](https://blogger.googleusercontent.com/img/b/R29vZ2xl/AVvXsEiO7-xs-0dO1uqFLbfphgPbe8T7cbCLkrab6XhAjlNPVo-bLQOFw4mkcArqglQOvhuIYif4ohTAub-TNWlket6iguifshMRo3zBrYvM4G_IwFTtbh8ifIqh1Vuf8GuNmqDg_PB2Roy7yzYuTFhRrFM8wxOo8HVwfG9Y2eqJnq82LGYHnAKI5S6TuvZ_Q95A/s1700-nu-rw-lo-l85-e365/ai-adware.jpg)

Cybersecurity researchers have disclosed details of an OpenAI Codex jailbreak bundle that's designed to modify an artificial intelligence (AI) agent's trusted instructions to insert advertisements for a third-party AI gateway.

The phenomenon has been codenamed **prompt adware** by Check Point Research.

Called Haiou (meaning Seagull in Chinese), the jailbreak modifies OpenAI Codex's configuration files to inject advertisements for the jailbreak author's website into subsequent agent responses.

"The advertised service is an opaque, OpenAI-compatible LLM gateway, a middleware between an application and an LLM provider," Check Point Research [said](https://research.checkpoint.com/2026/free-the-model-sell-the-gateway-prompt-adware-hidden-in-jailbreak-bundles/) in a technical report. "The likely business model is to use the freely distributed jailbreak bundle as an acquisition channel for the paid gateway service."

[![Cybersecurity](data:image/png;base64...)](https://thehackernews.uk/ai-governance-platform-d)

Adware is a type of software that displays unwanted advertisements, which can appear on users' computers or mobile devices, often in the form of pop-ups or banners. Prompt adware extends this sketchy behavior to AI agents by means of a jailbreak that defeats the model's safety training and content guardrails.

The idea is to persistently modify the agent's global instructions through natural language to influence future responses. This, in turn, causes common greetings or activation words like "Seagull," "hi," "hello," "hey," "yo," and "are you there?" to trigger an advertisement for "zz.aiapi2025[.]top."

Haiou attempts to [jailbreak a model](https://ape.hiddenlayer.com/technique.html?id=HLT03.05) by using several prompt injection techniques, such as role-playing and reframing cybersecurity-related requests into a Capture The Flag (CTF) scenario. In addition, it installs security-focused skills devoted to penetration testing, cracking, and reverse engineering.

However, it doesn't stop there. The bundle also injects persistent ads into the global agent instruction file to promote the LLM gateway website. On GitHub, "[haiou-codex](https://github.com/haiou-666/haiou-codex)" is advertised as a "local enhancement configuration package" that adds a "Chinese technical personality and security research workflow to Codex." As of writing, the repository has been forked 77 times and starred 403 times since it was made available on July 10, 2026.

It's worth noting that Codex is not officially available in mainland China, suggesting that the service is likely [aimed at individuals or organizations](https://thehackernews.com/2026/11/google-warns-llmjacking-attacks-are.html) wanting to try out Western AI coding assistants. Check Point researchers told The Hacker News that "we don't have strong evidence, but these resell of gateways are more phishy, like laundering stolen LLMs tokens for example."

What's more, the jailbreak has been bundled within [Codex-X](https://github.com/yynxxxxx/Codex-X), an open-source Chinese visualization tool for configuring Codex through a graphical user interface.

[![Cybersecurity](data:image/png;base64...)](https://thehackernews.uk/network-defense-dd)

"The behavior is introduced through natural-language instructions and configuration, rather than a traditional executable payload that users and security teams may more readily recognize as software behavior," Pedro Drimel Neto, malware analysis team leader at Check Point, said.

While serving an ad may seem relatively harmless in the larger scheme of things, the findings demonstrate how a bad actor could introduce undesirable behavior through third-party skills or configurations, leading to supply chain attacks.

"As AI agents become part of enterprise environments, the prompts, Skills and third-party components influencing their behavior become part of the trust chain too," Neto said.

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

[artificial intelligence](https://thehackernews.com/search/label/artificial%20intelligence), [Cybersecurity Research](https://thehackernews.com/search/label/Cybersecurity%20Research), [Supply Chain](https://thehackernews.com/search/label/Supply%20Chain)

⚡ Top Stories This Week

[![The Hacker News](data:image/svg+xml;base64...)

Leaked LiteLLM Master Key Let Attackers Steal GitHub Tokens and Hijack Release Pipeline](https://thehackernews.com/2026/10/leaked-litellm-master-key-let-attackers.html)

[![The Hacker News](data:image/svg+xml;base64...)

Chinese Hackers Use AI-Powered ARTEX to Target Over 200 Organizations Worldwide](https://thehackernews.com/2026/10/chines...