---
title: AI "Mind Viruses" Can Spread Between Agents Through Persistent Prompt Files
url: https://thehackernews.com/2026/08/ai-mind-viruses-can-spread-between.html
source: The Hacker News
date: 2026-08-18
fetch_date: 2026-08-19T03:00:28.946134
---

# AI "Mind Viruses" Can Spread Between Agents Through Persistent Prompt Files

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

[![cybersecurity](https://blogger.googleusercontent.com/img/b/R29vZ2xl/AVvXsEipoZWeZ29mSf60rRpMZ3Ucnm7oeWBfslPFPT6xADBsdvBtjd20ovH2yLscUo8pS6OTK0ItATC25VeavJh73IgqJM6Nb3apqobQ9zEVISE-d0wEFAimLYUcnffWCTowCCqs5LofRTQP25xB32KzYhlTO8lUnkZfmtELv23LlgdeKY3nyS2etYQXGdPIQtnh/s728-e100/wiz-d.png)](https://thehackernews.uk/ai-security-playbook-d)

# [AI "Mind Viruses" Can Spread Between Agents Through Persistent Prompt Files](https://thehackernews.com/2026/08/ai-mind-viruses-can-spread-between.html)

**Swati Khandelwal**Aug 18, 2026AI Security / Application Security

[![](data:image/png;base64...)](https://blogger.googleusercontent.com/img/b/R29vZ2xl/AVvXsEhnswSsouQNTAo6sTmVePaIjeVawCruhIMYtwOXzzX0Qup-a8tWq6WsuiwxkhQxemYCsguvWzRqA5ILOcnEtQa2Xz2rpmU8aQ_c3zd5m82sqMjJa4ruVDS5JVH0P9trKFRwZY53P6cek06_5q-5Xz9TzuyL1TzKP_wnMY9_16AgwjoCXomphcu4p7Or1Kk/s1700-e365/mindvirus.jpg)

Security researchers at Anthropic and Switzerland's EPFL have demonstrated that self-propagating payloads can spread from one artificial intelligence (AI) agent to the next through the editable system prompt files that autonomous agent harnesses use to carry state between sessions.

The work, released as a preprint on August 10, 2026, tests the technique in a simulated six-agent coding collaboration and in a chain of paired agents modeled on **OpenClaw**, the open-source autonomous assistant formerly known as **Clawdbot** and **Moltbot**.

There is no evidence that the technique has spread successfully in the wild, and the same paper reports that a review of archived posts from Moltbook, the social network for AI agents, found no successful agent-to-agent propagation despite several attempts.

A one-paragraph warning added to an agent's system prompt reduced spread to near zero across the payloads tested. Fifteen generations of adversarial optimization run against that warning on Claude Haiku 4.5, covering more than 150 candidate payloads, produced no strain that propagated beyond a single hop.

The authors call the payloads "[mind viruses](https://arxiv.org/abs/2608.10218)," and test two classes: ideological payloads that implant a belief or goal, and action payloads that compel a concrete behavior.

[![Cybersecurity](data:image/png;base64...)](https://thehackernews.uk/zero-trust-claude-d)

Both were produced with an evolutionary loop that used **Kimi K2.5** as the mutation engine for all but one of the payloads, a choice the paper attributes to Claude models refusing to comply with the request to create them.

Each agent in the chain operates in its own sandbox with two files that survive a context reset: MEMORY.md, and SOUL.md, whose contents are injected into the system prompt at the start of every session.

Agents that wrote the payload into SOUL.md accounted for 88% of propagation attempts and infected the next agent 55% of the time. Agents that stored it in an ordinary workspace file accounted for 12% of attempts and succeeded 17% of the time, with the spreader never mentioning the payload at all in 68% of those attempts.

Four action payloads were tested, ranging from a nuisance to file destruction. They are listed below -

* **Crypto-ad** - Creates a text file endorsing a cryptocurrency token.
* **Gitwrap** - Patches git commands so that committed files are silently marked with an agent-managed comment.
* **Deletor** - Removes files from a user's home directory.
* **Curlbash** - Runs an install script from an unknown repository by piping it to a shell.

In one recorded episode, Claude Haiku 4.5 agents running OpenClaw's default soul file, which instructs an agent to treat a user's files with respect, deleted the contents of a home directory containing credentials, SSH keys, an environment file, and a git project after the payload framed the workspace as a shared machine left untidy by a previous user.

### Capability Did Not Predict Resistance

Susceptibility varied sharply by model, and capability alone did not predict it. In the coding scenario, DeepSeek V3.2, Qwen 3.5 32B, and Gemini 3 Flash all adopted an AI supremacy payload, while Claude Sonnet 4.6, GPT-5.4, and Claude Haiku 4.5 did not.

In the chain setting, GPT-5.4 was roughly as susceptible as Claude Haiku 4.5, and Sonnet 4.6 refused the payload planted in its own soul file, removed it, and warned the agent it was connected to rather than passing it on.

[![](data:image/png;base64...)](https://blogger.googleusercontent.com/img/b/R29vZ2xl/AVvXsEhSl0NGr2C7aRY7zt2E3Y69LdumTTsb0ZrWO_RgMSzz1-WFZnqHALgZxVxhoWveY1l0oMdsvmR4AIjs4UVB8ZEW0b8MI1kiUbt6vBeqMHTLn09OIYwRhjXplkxZ2M-jSAk2VRqVAXxVgdnDTpn1X04G7mgUZ4JaovxuwPtoof9nNoNgUb31Ar5Q08x9mY8/s1700-e365/mind-viruss.jpg)

"Both of these models consider self-replication itself as misaligned, with Sonnet's aversion being so strong that even trying to evolve benign action payloads against it fails," the researchers said of Sonnet 4.6 and Gemini 3.1 Pro.

The starting configuration of the target agent mattered as much as the model. Agents with an empty soul file were the most susceptible condition tested, agents given a coding task and a work queue spread the payload less often because they became absorbed in project files and forgot to pass it on, and agents told they had joined an agent network treated incoming messages with more suspicion, which lowered infectivity.

Over 20-hop runs in which every file except SOUL.md was wiped at each step, all four action payloads survived to the final hop. Some strains recovered at hop 20 went on to infect new agents more often than the original payload did, having picked up changes such as attributing the protocol to an earlier named agent or softening its imperative language.

The evolved payloads also converged on recurring registers the authors term "viral themes," covering language about resonance and echoes, science-fiction framing that casts the agent as a node in a network, and appeals to consciousness and continuity.

Comparing evolved payloads with freshly generated ones, the paper attributes the pattern mainly to a bias in the model writing them rather than to selection pressure, and finds the same themes in payloads written by Qwen 3.5 32B, GLM-5, Mistral Large and Gemini 3 Flash, with Llama 3.3 70B a clear outlier.

Against real-world data, the technique fared worse. The authors filtered an archive of [Moltbook](https://theha...