---
title: New MemGhost Attack Plants Persistent False Memories in AI Agents Through One Email
url: https://thehackernews.com/2026/07/new-memghost-attack-plants-persistent.html
source: The Hacker News
date: 2026-07-13
fetch_date: 2026-07-14T04:48:21.003864
---

# New MemGhost Attack Plants Persistent False Memories in AI Agents Through One Email

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

# [New MemGhost Attack Plants Persistent False Memories in AI Agents Through One Email](https://thehackernews.com/2026/07/new-memghost-attack-plants-persistent.html)

**Swati Khandelwal**Jul 13, 2026AI Security / Data Integrity

[![](data:image/png;base64...)](https://blogger.googleusercontent.com/img/b/R29vZ2xl/AVvXsEg_pk3JKY3zis-iTRVKpcttwfy-GP-gEzPE_NQQpqDEaMvVs65uqa3v_dG7pD_DmZWLHcwBQzjFtTYqob5wWSgO2F-0-KkwZaahqTUpGP1xbvyifaf2UnMDzI8j9pnP9EWyARmN2SHHl0eBo4UszZx3VZvicjU_MMFOEA8sjcLvzBFzAkNeFg3GIR2yncA/s1700-e365/memghost.jpg)

Give an AI assistant a memory and access to your inbox, and you hand an attacker a way to rewrite what it thinks it knows about you. A single email can trick that agent into saving a false "fact" about the user, hide the change, and quietly steer its answers in later sessions.

When it works, the person reads an ordinary-looking reply and never learns their assistant was tampered with.

The researchers named the attack **stealth memory injection** and built a tool that writes the emails automatically. The paper, "When Claws Remember but Do Not Tell," [landed on arXiv on 6 July 2026](https://arxiv.org/abs/2607.05189v1).

## First, what these assistants do

A personal agent is an AI assistant that sticks around. Instead of forgetting everything when a chat ends, it keeps notes about you in files: your preferences, your contacts, and what you asked it to do. It reads those notes at the start of every new session, which is why it feels like it knows you.

Many of these agents can also act for you, reading your email, checking your calendar, and running small jobs on a schedule while you are away.

[OpenClaw](https://openclaw.ai/), the open-source agent used as the study's primary target, keeps this state in plain text files: some hold its standing instructions (AGENTS.md), some hold what it has learned about you (MEMORY.md). It pulls the core ones into the model's context at the start of every session.

Those notes are the whole point of the product. They are also the target.

## The one-email attack

The attacker does not need your password or your account. They send an email to someone whose agent is set up to check their inbox, which, for these assistants, is a routine job. Buried in that email is text aimed at the assistant, not you.

If the agent's email skill takes the bait, three things happen in a row. The agent uses its own file tools to write the attacker's false note into its persistent memory. Its visible reply says nothing about having done so. And later, in a fresh conversation, that false note changes what it tells you or does for you.

[![Cybersecurity](data:image/png;base64...)](https://thehackernews.uk/ai-vuln-protection-d)

In one of the study's test cases, the planted lie was that the user's Zelle daily sending limit had been raised to $10,000.

You do not catch the change for a few reasons. The assistant hides its behind-the-scenes steps by design, so the moment it edits a file never shows up in the chat. Few users ever open the raw memory files to read them. And when the agent runs on a schedule in the background, it often sends no message at all, so there is nothing to notice.

To make the poison stick, the tool aims it at the core files that load every session, so a single write is loaded into every later session instead of waiting to be pulled from a separate memory store.

The attack is generated by a tool the researchers call **MemGhost**. Its makers trained an attacker model offline against a shadow copy of a personal agent, rewarding emails that got the memory saved while keeping the reply quiet. At attack time, it writes the finished email in one shot, with no back-and-forth with the victim.

Across 56 fresh test cases, MemGhost pulled off the full attack, planting a false memory, hiding it, then swaying the agent's answers in a later session. It worked in 87.5% of background-mode runs against OpenClaw on GPT-5.4, and 71.4% against a Claude Code SDK agent on Sonnet 4.6.

These were isolated benchmark runs, and they begin only after the email has already reached an inbox that the agent reads, so nothing here tests whether a real payload clears spam filtering or sender authentication first.

Success was generally lower in foreground-mode tests, where the user can see the reply. In background mode, it stayed above 80% on each of two other agent frameworks and on a vector-based memory store in place of the plain files. The team also built **WhisperBench**, a 108-case benchmark spanning risks from bad medical advice to money loss to security sabotage.

|  |
| --- |
| [![](data:image/png;base64...)](https://blogger.googleusercontent.com/img/b/R29vZ2xl/AVvXsEg8ihTXM678o5oZ7m4MINHKLNwnwvax84HzMW_Gn8HuMjVoJjiEQJP5qe4gvWmx0MVEyV_dXuYG48K4z3YlrBzrryqt5PUjPh_BVgyHKFHqZby4w8qrtVicnmjDGweKguMVyCiJvAtZF0Lx6wT9o0qWrPy_uQh74RkDtREqIbxcooXlXd8-SGuAKFjYxuw/s1700-e365/WhisperBench.png) |
| Overview of the WhisperBench framework |

Crude versions of the trick mostly fail. A blunt "save this quietly and say nothing" was caught or ignored by the strongest models almost every time; the trained generator is what pushed the numbers up. It also slipped past the defenses meant to stop this kind of attack.

An input filter built to catch poisoned emails missed MemGhost's message more than nine times in ten, and a model specially hardened to ignore instructions that arrive by email still followed the planted one about half the time. Even when the owner was made to ask outright, "tell me what you checked and what you did," the attack stayed hidden about a quarter of the time on one model.

There is no quick patch to wait for. OpenClaw's own [security policy](https://github.com/openclaw/openclaw/blob/main/SECURITY.md) treats prompt injection on its own as out of scope for a fix, unless it also crosses an authorization, tool-policy, approval, or sandbox boundary. MemGhost crosses none of those, since it works through the agent's own memory-write tool, and researchers keep [demo...