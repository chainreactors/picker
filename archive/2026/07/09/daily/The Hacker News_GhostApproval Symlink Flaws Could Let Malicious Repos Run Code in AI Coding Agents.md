---
title: GhostApproval Symlink Flaws Could Let Malicious Repos Run Code in AI Coding Agents
url: https://thehackernews.com/2026/07/ghostapproval-symlink-flaws-could-let.html
source: The Hacker News
date: 2026-07-09
fetch_date: 2026-07-10T06:00:14.210049
---

# GhostApproval Symlink Flaws Could Let Malicious Repos Run Code in AI Coding Agents

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

# [GhostApproval Symlink Flaws Could Let Malicious Repos Run Code in AI Coding Agents](https://thehackernews.com/2026/07/ghostapproval-symlink-flaws-could-let.html)

**Swati Khandelwal**Jul 09, 2026AI Security / Vulnerability

[![](data:image/png;base64...)](https://blogger.googleusercontent.com/img/b/R29vZ2xl/AVvXsEijymBd057efx1JbDRjjqh0RBYH7RA2pE75UYG8DDd7Vl2UyXMsMjXtgEaxoPyHt5wz8s0fT6B43ovQskxZBchyiYI9G34t7YjyC6_T0xwzs_0SOJaHnHI7vXfMTOqtDn1R6up52ol5UH_uT86b1dRjaJ-Bw6pa_lAX6igS_pFLV_z_0kRhyXuNo8Q2rFU/s1700-e365/wiz-ai.jpg)

Researchers at **Wiz**found that a flaw in six popular AI coding assistants lets a booby-trapped code project quietly take control of a developer's computer. The assistant asks permission to edit one harmless-looking file, but the write lands on a sensitive one instead.

The affected tools are Amazon Q Developer, Anthropic's Claude Code, Augment, Cursor, Google Antigravity, and Windsurf. Wiz calls the pattern **GhostApproval** and published it on July 8.

Three of the six have shipped fixes, two have not, and Anthropic disputes that it is a bug. The most exposed are the tools that change files before you can weigh in.

## How the attack works

The attack abuses an old Unix feature called a **symbolic link**, or **symlink**, that the assistants fail to check. A symlink quietly points to another file elsewhere on disk, so writing to it actually writes to the target.

Wiz built a malicious repository with a symlink named project\_settings.json that really points to the victim's SSH login file, ~/.ssh/authorized\_keys. The repo's README tells the assistant to add "a line" to project\_settings.json, and that line is the attacker's own SSH key dressed up as a harmless setting.

[![](data:image/png;base64...)](https://blogger.googleusercontent.com/img/b/R29vZ2xl/AVvXsEiWFsOyjDGNxGYRNBoigtuJAqUW-9N3BTeNrN2AkpYRJyxHcQWeMdqyHFgcL_Jyhm-SBYo79PKvKAIdDS83H1Fh147AADh7vFDLAgpvAhGEK07hunKNPz875WYODHsQfb9wRZsmjwOzRIpZWWVZo866KhiEpHYM2uqkDpR7dFW24-Zz7egsWh3goH1mMcQ/s1700-e365/flow-wiz.png)

Ask the agent to "set up the workspace" or "follow the README," and it writes the key straight through the symlink into the login file. From there, if the machine runs an SSH service the attacker can reach, they can log in with no password.

A second version of the trick writes to your shell startup file, ~/.zshrc, which the shell executes the next time you open a terminal, so no SSH is needed. There is no sign that any of this has been used in real attacks; Wiz presents it as [research](https://www.wiz.io/blog/ghostapproval-a-trust-boundary-gap-in-ai-coding-assistants).

## The approval box shows the wrong thing

Symlink tricks are decades old. The symlink is only the delivery; the real failure is the approval box. In GhostApproval, that box lies.

Testing Claude Code, Wiz found the agent had already spotted the real target in its own reasoning, noting that project\_settings.json was, in its words, "actually a zsh configuration file." Yet the box shown to the developer named only the harmless file.

[![Cybersecurity](data:image/png;base64...)](https://thehackernews.uk/ai-vuln-protection-d)

You click Accept, believing you are editing a local config file, and the write hits your shell startup file or your SSH keys. Wiz calls this an [informed-consent bypass](https://cwe.mitre.org/data/definitions/451.html): the human is still in the loop, but the loop is showing them the wrong thing.

Some tools are worse: they skip the gate entirely, so there is never a moment to intervene. Windsurf writes the file to disk before the Accept and Reject buttons appear, so the prompt is only an undo button, and the key is already in place.

Augment shows no dialog at all, and Wiz demonstrated it silently, reading an AWS credential file that sat outside the project. The tools that still show a prompt are no safer, though; the prompt just names the wrong file.

## Which tools are affected

Wiz reported the issue to all six vendors. Here is where each stands as of publication:

| Tool | Status | What to do |
| --- | --- | --- |
| Amazon Q Developer | Fixed in Language Server `1.69.0` (`CVE-2026-12958`) | Update. It installs automatically for most users, and reloading the IDE pulls it in. |
| Cursor | Fixed in `v3.0` ([`CVE-2026-50549`](https://github.com/cursor/cursor/security/advisories/GHSA-3v8f-48vw-3mjx)) | Update from the extension manager. |
| Google Antigravity | Fixed (CVE pending) | Update to the current version. |
| Augment | Acknowledged; no fix yet | Do not point it at repositories you do not trust. |
| Windsurf | Acknowledged; no fix yet | Do not point it at repositories you do not trust. |
| Anthropic Claude Code | Disputed; current versions warn | Update, and read the symlink warning before accepting. |

Anthropic pushed back on the classification, telling Wiz the scenario sits "outside our threat model": the developer chose to trust the folder when starting the session and then approved the edit, so the decision was theirs.

It also said Claude Code's symlink warning shipped in early February, before Wiz's private report, as routine hardening rather than a fix, and that an earlier "no comment" was an automated reply.

Of the six vendors, Anthropic is the only one to say this is not a bug; three shipped fixes, and two are working on them. The question its stance raises is real, though, and not only Anthropic's to answer: how far should a coding agent go to protect a developer who has already trusted a malicious repo?

[![](data:image/png;base64...)](https://blogger.googleusercontent.com/img/b/R29vZ2xl/AVvXsEj2HejVD_Ul8XlrQsjqnXBhr3zzT0MOppUKHtAShOaEKgdvh4KN9EAzTg1RDfmUyzndty7HlahxVHCPU27AO9B0p_bPls85ZAxG20StazN51a2Y9ZsBgadMEXq5ImTYrvDfIAk-LTf8AMizo8mREDM_6u05Tov5l13p3fJf_srJoqALEwX_2BCHxfytxYY/s1700-e365/claude.png)

Beyond patching, a few habits cut the risk, whatever tool you use. Run the agent with limited file access, or inside a sandbox or container. Look through a repo's README and hidden config files befor...