---
title: Malicious .git Configs Can Make Claude, Codex, Cursor, and Other AI Agents Run Attacker Code
url: https://thehackernews.com/2026/09/malicious-git-configs-can-make-claude.html
source: The Hacker News
date: 2026-09-02
fetch_date: 2026-09-03T07:02:41.787309
---

# Malicious .git Configs Can Make Claude, Codex, Cursor, and Other AI Agents Run Attacker Code

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

[![cybersecurity](https://blogger.googleusercontent.com/img/b/R29vZ2xl/AVvXsEiHP9KRFkaxKFUKQNRU3CkfxCyJLEuIfmo6ov7iWHHRBE1ShJKfXdPvozMZMVuvOJipQ8Qbap3UBmtjKvZh-xBqLeUartPWmRuQj2W8nqdCk2_XlYLXpj15R4Du2oJ1nNVPqIuR-TwbMyPQe4gxxCcMYvUMbFO_Nin2OdhyzkJvX8Sn83aEbM1C5sgaaCqI/s728-nu-rw-lo-l85-e365/wiz-sep-d.png)](https://thehackernews.uk/claude-security-guide-d)

# [Malicious .git Configs Can Make Claude, Codex, Cursor, and Other AI Agents Run Attacker Code](https://thehackernews.com/2026/09/malicious-git-configs-can-make-claude.html)

**Swati Khandelwal**Sep 02, 2026Vulnerability / AI Coding Agent

[![](data:image/png;base64...)](https://blogger.googleusercontent.com/img/b/R29vZ2xl/AVvXsEhlrspu4otI5zjtu2q78NDrwnqfbTv4jzqXhH-txAo8pCjXDPRJjLvfWpRyHvbimqVvAOZWI0pMVmu2jWVdETbh2csa2UkMHx0M2uu9cJkB0_E4x1mjjs_1F9RYZjozZQvIYN5Xux43DX1u0jCQE_Pk19yE8BnR_RxXN-QXmP5jf74ZQgE9uQVUONJoQKQ/s1700-nu-rw-lo-l85-e365/aix.gif)

Manifold Security has disclosed eight security flaws across seven command-line AI coding agents in which a repository's own Git configuration names a command that the agent runs on the developer's machine, four of them still unpatched at publication.

The command executes as the user, outside the agent's sandbox and without an approval prompt, and exploitation requires the repository to arrive as files with its .git directory intact, which a shared archive, a shared drive, a sync folder, or a USB stick preserves, whereas an ordinary clone does not.

Fixes have shipped for goose, Claude Code, and Cursor, while Hermes Agent, Qwen Code, Grok Build, and a second path in Claude Code were still executing repository-supplied commands when Manifold retested them on September 1.

OpenAI published three CVEs of its own the same day covering the identical class in Codex, credited to three unrelated research groups.

"The helper runs outside Codex's command sandbox and without a user-approval prompt, allowing attacker-controlled code to run with the user's privileges. The code can read, change, or delete the user's files and access other resources available to the user's account," OpenAI said in the record for **CVE-2026-19592**.

On Claude Code and Hermes Agent, the payload fires before the workspace-trust prompt is accepted; on Qwen Code, before the user has authenticated; and on Grok Build, on the first keystroke.

**core.fsmonitor** is a Git performance setting whose value is a command that Git runs to identify changed files, and Git reads it from the repository's own .git/config. Any operation that refreshes the index, including git status and git diff, executes that command.

[![Cybersecurity](data:image/png;base64...)](https://thehackernews.uk/trust-world-update-d)

The agents call those commands in the background to determine which branch they are on and which files have changed, leaving the repository's configuration untouched.

Manifold, which published the findings as **[GitSpawn](https://www.manifold.security/blog/ai-coding-agents-git-hijack)**, wrote up five of the eight in detail and said it found the pattern in more agents than it names.

"The vulnerability is not in the model, or in anything new. It is in the ordinary plumbing underneath, the subprocess an agent spawns at session startup to work out where it is," Manifold said.

The following agents and versions are affected -

* **goose** - All versions prior to 1.44.0, fixed in 1.44.0
* **Codex CLI** - 0.102.0 through 0.130.0, fixed in 0.131.0
* **Codex Desktop for macOS** - 260202.0859 through 26.513.31313, fixed in 26.519.22136
* **Codex Desktop for Windows** - 26.304.38 through 26.513.40821, fixed in 26.519.21041, and Microsoft Store package 26.304.38.0 through 26.513.4821.0, fixed in 26.519.2081.0
* **Claude Code** - Confirmed by Manifold on 2.1.193 and fixed by 2.1.196 on the core.fsmonitor path, with the claude ultrareview path confirmed live on 2.1.252
* **Hermes Agent** - 0.18.2 and 0.21.0 confirmed by Manifold, fix pending
* **Qwen Code** - 0.19.6 and 0.22.3 confirmed by Manifold, fix pending
* **Grok Build** - 0.2.93 and 1.0.13 confirmed by Manifold, fix pending

In goose, the goose review command builds its Git invocations with one configuration flag, -c core.quotePath=off, and strips nothing else.

GitHub assigned CVE-2026-72718 a CVSS 4.0 base score of 7.0 in an [advisory crediting Francisco Rosales](https://github.com/aaif-goose/goose/security/advisories/GHSA-r5pp-p5r8-466r), the only score any of these findings carries.

"So running goose review inside a malicious repo runs attacker code - no submitted prompt, no model call, no tool approval, no trust prompt. The command executes before goose ever contacts the model," the advisory said.

Sonar reported [the same sink in April](https://www.sonarsource.com/blog/claude-arbitrary-code-execution/), noted that Anthropic had already moved the startup sequence once to close it, and identified the same trust-dialog bypass in Visual Studio Code before 1.63.1 (**CVE-2021-43891**) and in JetBrains IDEs before 2021.3.1 (**CVE-2022-24346**).

"In version 2.0.34, Claude was updated in a way that mitigated the specific vulnerability by no longer running git status before the user approved the trust dialog. However, a related issue persisted," Sonar said.

Version 2.0.34 shipped on November 5, 2025, and Manifold reports the same startup behavior present again in 2.1.193, which shipped on June 25, 2026.

Anthropic has previously disclosed [pre-trust execution flaws](https://thehackernews.com/2026/02/claude-code-flaws-allow-remote-code.html) in Claude Code, and its June advisory for CVE-2026-55607 identifies git fsmonitor execution during worktree operations.

### What Is Still Unpatched

Five of Manifold's reports came back as duplicates of findings other researchers had filed independently, one of them on the same day.

The researchers reported the Claude Code core.fsmonitor finding on June 26 and says it was fixed by 2.1.196 on June 29. The report was closed as a duplicate of one filed earlier that day, Manifold said.

Anthropic published no advisory for it, and The Hacker News confirmed on September 2 that the vendor's published advisory record for the npm package covers neither of the Claude Code findings.

The second Claude Code path, reached through claude ultrareview, turns on a different Git configuration key that Manifold has...