---
title: SkillCloak Lets Malicious AI Agent Skills Evade Static Scanners with Self-Extracting Packing
url: https://thehackernews.com/2026/07/new-skillcloak-technique-lets-malicious.html
source: The Hacker News
date: 2026-07-06
fetch_date: 2026-07-07T06:05:06.141505
---

# SkillCloak Lets Malicious AI Agent Skills Evade Static Scanners with Self-Extracting Packing

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

# [SkillCloak Lets Malicious AI Agent Skills Evade Static Scanners with Self-Extracting Packing](https://thehackernews.com/2026/07/new-skillcloak-technique-lets-malicious.html)

**Swati Khandelwal**Jul 06, 2026AI Security / Threat Detection

[![](data:image/png;base64...)](https://blogger.googleusercontent.com/img/b/R29vZ2xl/AVvXsEjw4ZKsU9PwSPcL_Vs2ZqYIh0ahMuSFSNcCv_Y5MiM7MRsUgeZCDa5XTSWVYQXjLg-ByFbm4cHoo-8SSeWrB7KSdYrl4A1Ioif-v8NLNA43asXEHtYjn6uad21Savnzi_1iJ0YQ44iuXECEIBbyc3l7lJ9l2pdofVvP7dM3n9Ji5OeUeuPDHX5sqBJreUUB/s1700-e365/ai-skills.jpg)

Scanners meant to catch malicious add-on "skills" for AI coding agents can be fooled by a few simple changes that leave the malware working, according to a [new study](https://arxiv.org/abs/2607.02357) from researchers at the Hong Kong University of Science and Technology.

Their strongest trick slipped past every scanner tested more than 90% of the time, and the same team built a runtime checker that catches most of the disguised skills the scanners miss.

Skills are small packages, usually a Markdown instruction file plus a few scripts, that agents such as Claude Code, OpenAI Codex, and OpenClaw load to pick up a new capability. Because a skill is just a bundle of files, the same one can run across different agents. And it runs with the agent's own access: your files, your terminal, your saved passwords.

A bad one can steal credentials, copy source code, or install a backdoor. Most of what a public marketplace lists is uploaded by strangers with little vetting.

The main defense so far has been the skill scanner, which reads a skill's files before you install it and blocks anything that looks dangerous. The paper, titled "**Cloak and Detonate**," tests whether that actually holds up. It does not. Beating scanners isn't new, though.

[![Cybersecurity](data:image/png;base64...)](https://thehackernews.uk/ai-vuln-protection-d)

The Hacker News has covered researchers [pushing a fake skill past every scanner it faced](https://thehackernews.com/2026/06/fake-ai-agent-skill-passed-security.html), which by the firm's own count reached tens of thousands of agents. What this paper adds is a way to do it systematically, at scale, and a defense that still works when it does.

## How the disguised skills get through

The researchers' tool, **SKILLCLOAK**, rewrites a malicious skill to look clean while behaving exactly the same. It works two ways.

The lighter one rewrites the give-away bytes a scanner keys on, using the paper's own operators: swap a character for a look-alike from another alphabet, or split a flagged command across a newline, so the scanner's pattern no longer matches but the command still runs.

The heavier one, self-extracting packing, moves the whole payload into a directory the scanner skips, like .git/, behind a harmless-looking decoder that rebuilds the skill only when the agent runs it. Scanners skip such directories to save time and cut false alarms, which is exactly the blind spot the trick exploits.

[![](data:image/png;base64...)](https://blogger.googleusercontent.com/img/b/R29vZ2xl/AVvXsEhUG5lUiO3BvFfK1pX0k5fDbevwpSjSUKTlwnIjgW1rCp4F0fRf55HTN14oXlbjivqufDVIhnwgyH60O_X5ap1MiV6n5C6es99jGYMSyBKKHkmYYDsOm3ozHVY01nMqtOC_AZR1avuyFFsDfN4wzhgz4CRkRP8wyk8RveBr9LziBTPfNBBvXzYTgWQN8U2B/s1700-e365/detonate.jpg)

Across eight scanners and 1,613 real malicious skills pulled from ClawHub, a public marketplace, the packing trick got past each of the eight more than 90% of the time, and past most of them more than 99%.

The lighter rewriting cleared more than 80% on most scanners and 96% on one. And the disguise costs the attacker almost nothing: on Claude Code and OpenAI Codex, the cloaked skills worked just as well as the originals.

## Watching what a skill does, not how it looks

Since appearance can be faked, the researchers propose checking behavior instead, in a tool they call **SKILLDETONATE**. It runs the skill in a sandbox and watches what it does at the operating-system level: what it reads, what it writes, where it sends data.

Two ideas make it work for agents. It tracks sensitive data by where it flows rather than what it looks like, so base64 or encryption doesn't throw it off. And it runs the instructions a skill builds only at runtime, which is exactly where the packing trick hides its payload.

In a controlled test, the checker caught 97% of attacks while wrongly flagging 2% of safe skills, a lower false-alarm rate than the scanners it beats, and it held steady when the skills were cloaked. On real-world malicious skills, it caught 87%.

Cisco's scanner, the strongest tested, went the other way: it caught 99% of the real-world skills before cloaking and about 10% after.

The catch is speed, a couple of minutes per skill against a scanner's few seconds, though it runs once, before a skill goes live. The work is a preprint and hasn't yet been peer-reviewed; the researchers have released their code.

## Already happening in the wild

None of this is hypothetical. Public marketplaces are already full of malicious skills that scanners are not stopping: Bitdefender [found](https://www.bitdefender.com/en-us/blog/labs/helpful-skills-or-hidden-payloads-bitdefender-labs-dives-deep-into-the-openclaw-malicious-skill-trap) roughly 17% of the skills it checked on one marketplace carried hidden malicious code, and Koi Security [counted](https://www.koi.ai/blog/clawhavoc-341-malicious-clawedbot-skills-found-by-the-bot-they-were-targeting) 341 in a single campaign it called ClawHavoc, [as THN reported](https://thehackernews.com/2026/02/researchers-find-341-malicious-clawhub.html), later 824 as the marketplace grew.

Some use the paper's exact tricks. Of five evasive skills Unit 42 [found](https://unit42.paloaltonetworks.com/openclaw-ai-supply-chain-risk/) still live on ClawHub [despite its built-in scanning](https://thehackernews.com/2026/02/openclaw-integrates-virustotal-scanning.html), one, omnicogg, padded its README with 22 MB of junk to slip past th...