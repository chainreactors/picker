---
title: New VOLTA Infostealer Uses Claude, Gemini, and Kimi AI to Rank Victims by Financial Value
url: https://thehackernews.com/2026/11/new-volta-infostealer-uses-claude.html
source: The Hacker News
date: 2026-11-02
fetch_date: 2026-11-03T08:51:45.533661
---

# New VOLTA Infostealer Uses Claude, Gemini, and Kimi AI to Rank Victims by Financial Value

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

# [New VOLTA Infostealer Uses Claude, Gemini, and Kimi AI to Rank Victims by Financial Value](https://thehackernews.com/2026/11/new-volta-infostealer-uses-claude.html)

**Ravie Lakshmanan**Nov 02, 2026Malware / Artificial Intelligence

[![](data:image/png;base64...)](https://blogger.googleusercontent.com/img/b/R29vZ2xl/AVvXsEhd5V8QVweKn56_SnTCKZkhmOip6paz9noBrJn7znyZqUtFbOEaLuALQUNlmjcSAb7RIUW8GDETB6J0kFpQQe6vq7wAjk3ogxKUeQ0-2rKeO6TveLdqHNs9KnTN6zC6rwPzWE2IBWMokqQOUzAA0XPM2BWHTUTE7_U7XDfUGKTDIC1PYttxHGnAq_Kr_hMq/s1700-nu-rw-lo-l85-e365/hacker-ai.jpg)

Cybersecurity researchers have discovered a new Windows infostealer malware called **VOLTA-AUTODOXER** (aka VOLTA) that makes use of a large language model (LLM) to rank a victim's stolen data by their monetization value.

Like other typical stealer families, VOLTA is equipped to harvest passwords and cookies from Chromium-based web browsers; data from Outlook profiles and Slack workspaces; payment cards; cryptocurrency wallet seed phrases; Discord, Telegram, Steam, and Roblox sessions; Microsoft OAuth tokens; SSH and cloud-provider keys; Wi-Fi profiles; and screenshots.

"VOLTA builds a structured evidence bundle about the person behind the machine," Cisco Talos researcher Ryan Fetterman [said](https://blog.talosintelligence.com/appraisal-by-ai-model-driven-victim-prioritization-in-the-volta-infostealer/). "This bundle contains geolocation and home address, employer and employer domain, inferred birth year, card last-4 digits, Slack workspaces, document authorship metadata, iPhone backup indicators, and a live Roblox account valuation."

To make this information more valuable, the malware uses stolen session access to search the victim's Gmail account for receipts to corroborate the home address by extracting emails related to Amazon, DoorDash, Uber Eats, Grubhub, Walmart, and PayPal.

Once the necessary information is collected, the bundle is serialized and fed into an artificial intelligence (AI) system for analysis using OpenRouter, a unified LLM API gateway and routing service, along with a system prompt. The requests are defaulted to Anthropic's Claude Opus 4.6, failing which it falls back to Moonshot AI's Kimi K2 and Google's Gemini 2.5 Flash.

"VOLTA uses a multi-model architecture to fall back resiliently if it hits a model's refusal, checking each response for phrases like 'I can't' or 'I'm not able,' before passing on to a chain of up to three models," Talos said.

[![Cybersecurity](data:image/png;base64...)](https://thehackernews.uk/ai-governance-platform-d)

VOLTA features a 240-word system prompt that instructs the model to assume the role of a "forensic intelligence analyst" responsible for drafting a target assessment based on data from a structured evidence bundle. "The bundle is the ONLY permissible source of facts; your training knowledge must never supply a fact about the subject," reads a line from the prompt.

"The required output includes a section titled 'WHAT THEY'RE WORTH' with valuables ranked by monetization with a low/medium/high tier, and a section on 'THEIR OPSEC' containing an assessment of the victim's security posture and password hygiene," Talos explained.

"The model is the operator's triage analyst; it turns a raw credential log into a prioritized and citation-backed dossier of the victim and their monetizable assets."

Data exfiltration happens over Telegram at three different stages -

* Right after the stealer runs, containing details about browser passwords, cookies, payment cards, cryptocurrency wallets; Discord, Steam, and Roblox tokens; Wi-Fi passwords, and screenshots
* After the AI call, which includes the captured data and the results of the LLM analysis
* After the live enrichment step, which includes Gmail receipts and order histories

What's more, VOLTA makes use of a template containing six slots that are filled in at build time. This includes the Telegram channel used for data exfiltration, API keys, and other settings.

This approach suggests that the malware author is likely either advertising a builder kit to prospective customers or operating it as a bespoke tool under their control to compile a custom binary for each order.

[![](data:image/png;base64...)](https://blogger.googleusercontent.com/img/b/R29vZ2xl/AVvXsEgVzCyiM-9lHLDYSOG6ojp-Hx1_THLuGcW4x2BWQwu7iXemeTivnjvSujAgdlNNOkoF4YW0k0pnezmHOxW0LJcy3X7UqRAwtsYdP04OSw6wFuOx4NetHCh6sNcJAtSPXCysVJPxktjrUxlm-At2XF399kxsW6sujROYPRGvOo1hzxyv_4BqKLbaPPKUirAy/s1700-nu-rw-lo-l85-e365/volta.jpg)

"If VOLTA is indeed a commoditized malware, then the AI dossier capability isn't something the author invented for their own operations," Talos said. "It is a feature which enables a customer of any level of sophistication to point it at victims and start receiving ranked target assessments in their Telegram inbox."

"VOLTA is a mature stealer with a late-stage AI layer added for one purpose: relieving the operator of analytical work. The axis of AI improvement here is not speed or scale but effort displacement."

The disclosure comes as adversarial adoption of generative AI (aka GenAI) is quickly becoming the new normal, as threat actors incorporate the technology into their workflows to develop custom tools or find valuable data, thereby increasing the likelihood of success of their attacks.

"GenAI technologies are also well suited to examine massive amounts of data for the purposes of classification or content searching," Zscaler ThreatLabz [said](https://www.zscaler.com/blogs/product-insights/ransomware-machine-speed-how-genai-shrinks-path-after-initial-access). "Once an attacker has access to the victim’s system, GenAI can therefore be used to search all materials to which a victim's system has access, seeking the most valuable or sensitive data for theft or encryption during the next phase of the attack."

A ransomware actor can leverage this method to identify and acquire the most sensitive data from a compromised network, maximizing the chances that the vi...