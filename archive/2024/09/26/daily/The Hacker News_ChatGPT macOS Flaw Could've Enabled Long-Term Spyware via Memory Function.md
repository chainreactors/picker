---
title: ChatGPT macOS Flaw Could've Enabled Long-Term Spyware via Memory Function
url: https://thehackernews.com/2024/09/chatgpt-macos-flaw-couldve-enabled-long.html
source: The Hacker News
date: 2024-09-26
fetch_date: 2025-10-06T18:30:44.353299
---

# ChatGPT macOS Flaw Could've Enabled Long-Term Spyware via Memory Function

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

[![Salesforce Security Handbook](https://blogger.googleusercontent.com/img/b/R29vZ2xl/AVvXsEjWa8tsMNqlevi1HGF1ALQRGIq7hROPFAbHd3R1RTEOe73T8_Q2xW_-91t2jSGjU5peiPb8QYblGp4igNW-u2Qmlxbp2BKzTVMSvyXDZJmC-BYpiiJHrcnG5drmSP97iZ9PVIf1DeEr7U-7vWpe4HXwfMjt8FGNgq5mOycOJluYr9wF7YOKrQY9MfArwgjt/s728-e100/ai-agent-security-d.png)](https://thehackernews.uk/ai-agent-security-d)

# [ChatGPT macOS Flaw Could've Enabled Long-Term Spyware via Memory Function](https://thehackernews.com/2024/09/chatgpt-macos-flaw-couldve-enabled-long.html)

**Sep 25, 2024**Ravie LakshmananArtificial Intelligence / Vulnerability

[![Spyware via Memory Function](data:image/png;base64... "Spyware via Memory Function")](https://blogger.googleusercontent.com/img/b/R29vZ2xl/AVvXsEhRqKtDX9OvVhpFV6zY1cM7sOQTBRW1MUylXA0YO5D8GYCwZHUnNubtc5V7pq92tMrGsShYjdDjfQrr22vlFPGG3Ps8QStUsPar1wehNTTvYYiPcPSR-oj3wxw2JRRd5SpDV5qUjIlSurwvE-EJ7aDf6kAwEvf8qyKBDVPeHArHh86vFelYF8jMvyv281Kx/s790-rw-e365/macos.png)

A now-patched security vulnerability in OpenAI's ChatGPT app for macOS could have made it possible for attackers to plant long-term persistent spyware into the artificial intelligence (AI) tool's memory.

The technique, dubbed **SpAIware**, could be abused to facilitate "continuous data exfiltration of any information the user typed or responses received by ChatGPT, including any future chat sessions," security researcher Johann Rehberger [said](https://embracethered.com/blog/posts/2024/chatgpt-macos-app-persistent-data-exfiltration/).

The issue, at its core, abuses a feature called [memory](https://openai.com/index/memory-and-new-controls-for-chatgpt/), which OpenAI introduced earlier this February before rolling it out to ChatGPT Free, Plus, Team, and Enterprise users at the start of the month.

What it does is essentially allow ChatGPT to remember certain things across chats so that it saves users the effort of repeating the same information over and over again. Users also have the option to instruct the program to forget something.

[![DFIR Retainer Services](data:image/png;base64...)](https://thehackernews.uk/cloud-insight-d)

"ChatGPT's memories evolve with your interactions and aren't linked to specific conversations," OpenAI says. "Deleting a chat doesn't erase its memories; you must delete the memory itself."

The attack technique also builds on [prior findings](https://embracethered.com/blog/posts/2024/chatgpt-hacking-memories/) that involve using [indirect prompt injection](https://thehackernews.com/2024/08/microsoft-fixes-ascii-smuggling-flaw.html) to manipulate memories so as to remember false information, or even malicious instructions, thereby achieving a form of persistence that survives between conversations.

"Since the malicious instructions are stored in ChatGPT's memory, all new conversation going forward will contain the attackers instructions and continuously send all chat conversation messages, and replies, to the attacker," Rehberger said.

"So, the data exfiltration vulnerability became a lot more dangerous as it now spawns across chat conversations."

In a hypothetical attack scenario, a user could be tricked into visiting a malicious site or downloading a booby-trapped document that's subsequently analyzed using ChatGPT to update the memory.

The website or the document could contain instructions to clandestinely send all future conversations to an adversary-controlled server going forward, which can then be retrieved by the attacker on the other end beyond a single chat session.

Following responsible disclosure, OpenAI has addressed the issue with ChatGPT version 1.2024.247 by closing out the exfiltration vector.

[![ChatGPT macOS Flaw](data:image/png;base64... "ChatGPT macOS Flaw")](https://blogger.googleusercontent.com/img/b/R29vZ2xl/AVvXsEi2KHQQMAXJzO67Gw5Lgk4GckjJmYQCYkNQXvTN7056fX5TRPkFxrehg0f-beiD0dU3ynZ6FdTIlIyR4cdpBqAlaIqtMHdO0zty-7X7SB_0WC-427Cjs9U8TGfbvXkkS9LbuSwfZzcWels1i7o7DhX-WnM6eRJxAUEDmXcU0W1qan7zUdKRS-NE3eNwyJAo/s790-rw-e365/gpt.png)

"ChatGPT users should regularly review the memories the system stores about them, for suspicious or incorrect ones and clean them up," Rehberger said.

"This attack chain was quite interesting to put together, and demonstrates the dangers of having long-term memory being automatically added to a system, both from a misinformation/scam point of view, but also regarding continuous communication with attacker controlled servers."

The disclosure comes as a group of academics has uncovered a novel AI jailbreaking technique codenamed MathPrompt that exploits large language models' (LLMs) advanced capabilities in symbolic mathematics to get around their safety mechanisms.

[![CIS Build Kits](data:image/png;base64...)](https://thehackernews.uk/platform-shield-d)

"MathPrompt employs a two-step process: first, transforming harmful natural language prompts into symbolic mathematics problems, and then presenting these mathematically encoded prompts to a target LLM," the researchers [pointed out](https://arxiv.org/abs/2409.11445).

The study, upon testing against 13 state-of-the-art LLMs, found that the models respond with harmful output 73.6% of the time on average when presented with mathematically encoded prompts, as opposed to approximately 1% with unmodified harmful prompts.

It also follows Microsoft's debut of a new Correction capability that, as the name implies, allows for the correction of AI outputs when [inaccuracies (i.e., hallucinations) are detected](https://arxiv.org/abs/2408.12748).

"Building on our existing Groundedness Detection feature, this groundbreaking capability allows Azure AI Content Safety to both identify and correct hallucinations in real-time before users of generative AI applications encounter them," the tech giant [said](https://techcommunity.microsoft.com/t5/ai-azure-ai-services-blog/correction-capability-helps-revise-ungrounded-content-and/ba-p/4253281).

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
[**Share on Facebook...