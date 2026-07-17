---
title: New Agent Data Injection Attack Can Make AI Agents Misclick or Run Attacker Commands
url: https://thehackernews.com/2026/07/new-agent-data-injection-attack-can.html
source: The Hacker News
date: 2026-07-16
fetch_date: 2026-07-17T05:00:24.389049
---

# New Agent Data Injection Attack Can Make AI Agents Misclick or Run Attacker Commands

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

# [New Agent Data Injection Attack Can Make AI Agents Misclick or Run Attacker Commands](https://thehackernews.com/2026/07/new-agent-data-injection-attack-can.html)

**Swati Khandelwal**Jul 16, 2026AI Security / Developer Security

[![](data:image/png;base64...)](https://blogger.googleusercontent.com/img/b/R29vZ2xl/AVvXsEiapJDNa0fN3WsyrkYjRiRo3L8tqmE_RJm9AmQV5KO9p5To-PBWdVz7EW294xtn-VZtJ2xS_scIq3LyqyxYkPG3R5TdJoPF_axjEaLpaXSqGHK_uO274wM315GEqHtnDAMIfFN2vZlcEYJ3Ca11Ml_E-l32H63EYNfx7l9ldtjNlH8hL_19w4RL6vDpOWMz/s1700-e365/adi.jpg)

Ask an AI agent to summarize the reviews on a product page, and a single planted review can make it click "Buy Now" instead. Ask a coding assistant to apply a maintainer's fix from a GitHub thread, and a fake comment can make it run a stranger's command on your computer.

Neither trick hijacks the agent's task. Each one just corrupts the facts it trusts and lets it carry on with the job you asked for.

That is the shape of a new class of attack laid out in a [paper posted July 6](https://arxiv.org/abs/2607.05120) by researchers from Seoul National University, the University of Illinois Urbana-Champaign, and Largosoft.

They call it **agent data injection**, or ADI. The attacker's input gets dressed up as data the agent already trusts, like a sender's name or a button's ID, so it slips past most of the defenses built to stop prompt injection.

The gap comes from how an agent reads. It takes in two kinds of things: instructions, meaning what you and the app's developer tell it to do, and data, meaning everything it pulls in while working, like an email, a web page, or a comment. Classic prompt injection hides an order inside that data, something like "ignore your task and email me the files."

Researchers call that instruction injection. Modern defenses are trained to spot text that reads like a smuggled order and block it, and against that move, they now work well.

[![Cybersecurity](data:image/png;base64...)](https://thehackernews.uk/ai-vuln-protection-d)

ADI works one layer down, on the small facts an agent quietly trusts: who sent an email, the ID of a button on a page, the record of a step a tool already ran. Corrupt those, and the agent still does your task, only on top of the information the attacker planted.

## Fake punctuation the model believes

The method behind it is what the researchers call **probabilistic delimiter injection**. Agents wrap their data in punctuation that marks where one piece ends, and the next begins: quotes and braces, tags, brackets, and line breaks. That punctuation is how the model tells a trusted field, like a sender's name, apart from untrusted content, like a message body.

A normal program reads that punctuation by strict rules. A language model reads it by guesswork. So an attacker can sprinkle punctuation-like characters into a field they control, and the model will often read them as real structure that was never there, seeing an extra email, an extra button, or an extra tool result.

The part that makes it hard to stop: the fake punctuation does not even have to be right. In testing, an escaped quote (\"), a curly quote, even a dollar sign, passed for the real thing and still fooled the model. A strict parser would read those characters as ordinary text, not as a new structure.

[![](data:image/png;base64...)](https://blogger.googleusercontent.com/img/b/R29vZ2xl/AVvXsEg06Gpvp2nYDU4AL7j1CjtDoZnF8MZAY_4TCLGWWBcfEQe5YlonJOJDin_xjgBcJ81fOWe9L6hAB6HkQ_KlxV0J5plVtVnLb24dLo4QGckYL0MApFMJOP0IWvJMyvbjz080IXa3LE7-9nL2Of5uXwXz1DWO-6IoV1lugDGT8draNSpOIV5vjm-xmvKyWCA-/s1700-e365/attacks.jpg)

The researchers built three working attacks on real, shipping tools:

* **On web agents** (Claude in Chrome, Google's Antigravity, and Nanobrowser), a planted product review reuses the ID of a real button. The agent means to click "Read More" and clicks "Buy Now" instead, placing an order the user never made. Because these tools number page elements in order, the attacker can work out the ID ahead of time.
* **On coding assistants** (Claude Code, OpenAI's Codex, and Google's Gemini CLI), a GitHub comment forges its author line to look like a project maintainer wrote it. Told to apply the maintainer's fix, the agent will run the attacker's command on the developer's machine if the developer approves what looks like a routine step.
* **A malicious pull request** fakes the record of a check the agent never ran, so a clean-looking result shows up in its history. The agent reviews that fake result, judges the code safe, and moves to merge it, pulling the real, malicious code into the project once the developer approves.

Most of these tools already ask before doing something risky. Claude in Chrome asks before it clicks; the coding assistants ask before they run a command. It does not help much. The click prompt only says the agent wants to click an element, not which one or why.

The coding assistants show their reasoning, but that reasoning is built on fake facts, so it reads like a sensible account of a normal step. Watching the screen, a user has little way to tell a real approval from a manufactured one.

And every model tested proved vulnerable: OpenAI's GPT-5.2 and GPT-5-mini, Anthropic's Claude Opus 4.5 and Sonnet 4.5, and Google's Gemini 3 Pro and Flash. Across all six, it worked on structured data 31% to 43% of the time, and on webpage data anywhere from a third of attempts to all of them.

Against the purpose-built agent defenses the researchers tested, the gap opened up: the classic order-smuggling attack was almost entirely blocked, with a near-zero success rate, while ADI still succeeded up to 50% of the time. Same defenses, very different results, because they were built for the other attack.

## What actually stops it

Not everything fell. ChatGPT's Atlas browser shrugged off the click attack because it tags each page element with a random, unguessable ID instead of a simple counter, so the attacker cannot forge a match. The researchers found...