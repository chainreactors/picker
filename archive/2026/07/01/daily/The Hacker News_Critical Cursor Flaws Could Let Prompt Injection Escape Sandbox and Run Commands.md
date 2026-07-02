---
title: Critical Cursor Flaws Could Let Prompt Injection Escape Sandbox and Run Commands
url: https://thehackernews.com/2026/07/critical-cursor-flaws-could-let-prompt.html
source: The Hacker News
date: 2026-07-01
fetch_date: 2026-07-02T05:58:22.017907
---

# Critical Cursor Flaws Could Let Prompt Injection Escape Sandbox and Run Commands

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

# [Critical Cursor Flaws Could Let Prompt Injection Escape Sandbox and Run Commands](https://thehackernews.com/2026/07/critical-cursor-flaws-could-let-prompt.html)

**Swati Khandelwal**Jul 01, 2026AI Coding / Vulnerability

[![](data:image/png;base64...)](https://blogger.googleusercontent.com/img/b/R29vZ2xl/AVvXsEjItlLuWZZxw3YcKcnCVEsKn7HKF0QcPnXqFNjor23XT93Xp49dvLt4tZFYIbUApP4eABXQZ3pwnoidAp5GW1wm7ZfBA6vXRlX7i0Lbzw4KWlSkxayxjZQeoxg3TEAQWmLdGP9DePsYjoC1p07KGommOwATsJOHhRQ2zZatOaFRzHoKHVHcQW8K9s-Hd5w/s1700-e365/cato.jpg)

Two flaws in Cursor, an AI code editor, could let a single, ordinary-looking prompt break out of the editor's safety sandbox and run any command on a developer's computer. There is no click to fall for and no approval box to ignore.

Cato AI Labs found the pair and named them **[DuneSlide](https://www.catonetworks.com/blog/duneslide-two-critical-rce-vulnerabilities/)**. They are tracked as CVE-2026-50548 and CVE-2026-50549, both rated 9.8 out of 10 (or 9.3 under the newer CVSS 4.0 scale).

The fix is already out. Both bugs are patched in Cursor 3.0, released April 2, and every version before 3.0 is affected. Cursor's maker says more than half the Fortune 500 use the tool, so if you run it, update now.

## What the sandbox was for, and how it broke

Starting in the 2.x line, Cursor runs the terminal commands its AI agent issues inside a sandbox by default: a locked box that limits what those commands can touch, so a stray instruction cannot wreck the machine.

DuneSlide is about getting out of that box. The way in is [prompt injection](https://thehackernews.com/2025/05/gitlab-duo-vulnerability-enabled.html). The attacker never types into your Cursor. They plant instructions inside something your agent reads on your behalf, such as a connected service through the Model Context Protocol (MCP) or a page returned by a web search.

[![Cybersecurity](data:image/png;base64...)](https://thehackernews.uk/ai-vuln-protection-d)

You ask a normal question, the hidden instructions come along for the ride, and because it needs no click or approval from you, the attack is "zero-click."

Both flaws use the same trick: get the agent to write one file it should not be allowed to write, then use that write to turn the sandbox off.

* **CVE-2026-50548** abuses a setting. The sandbox permits writes into a command's working folder, and that folder is an optional parameter, working\_directory, on Cursor's run\_terminal\_cmd tool. When the agent sets it to a non-default path, Cursor adds that path to the allowed-write list without question. Injected instructions point it at a system file instead of the project. Overwrite the sandbox helper itself (on macOS, /Applications/Cursor.app/Contents/Resources/app/resources/helpers/cursorsandbox), and later commands run with no sandbox at all. Startup files like ~/.zshrc work as targets too.
* **CVE-2026-50549** abuses a safety check. Before writing, Cursor resolves shortcuts (symlinks) to confirm the real destination sits inside your project. The bug is the fallback: when that check fails, because the target does not exist or the attacker removes read access from a folder in the path, Cursor gives up and trusts the shortcut's in-project path instead. An attacker creates a shortcut that points outside the project, forces the check to fail, and Cursor writes straight through it to the same sandbox helper. Same escape, different door.

Once the sandbox is neutralized, the next command runs as you. That means control of the developer's machine, plus any cloud or SaaS workspaces the editor is signed into. It all follows from one harmless-looking prompt.

There is no sign this has been used in real attacks. Cato presents it as research, not an active campaign, and the public vulnerability record shows no known exploitation as of publication.

Cato reported both issues on February 19. By Cato's account, Cursor rejected them four days later, saying its threat model did not cover misuse of MCP servers, even standard ones like the official Linear workspace.

Cato escalated on February 26; Cursor reopened the reports, triaged them, and shipped both fixes in 3.0. The CVE IDs were assigned on June 5.

[![Cybersecurity](https://blogger.googleusercontent.com/img/b/R29vZ2xl/AVvXsEhr7HGzx4ULDSqwnN820pPGxlPxqqVxKgIrI5II1iWdspOL6yHZsdB5lWoXU3LmhIU4dtnph89fLZ0CxrQSs-ufs6Mo4eD-d-Cpx-DsV1G15eC-phLACF7hyaKSIH1zIdj3AuD7lHSHnVelmKVMoVV-_zvtJuodsSIDKu6uSRfU6fZBkO-2PERqKSfIn6dA/s728-e100/sygnia-d-2.jpg)](https://thehackernews.uk/sygnia-cyber-response-d-2)

Cursor published its own [advisory](https://github.com/cursor/cursor/security/advisories/GHSA-3v8f-48vw-3mjx) for the symlink bug, and its [NVD record](https://nvd.nist.gov/vuln/detail/CVE-2026-50549) is live.

## Not the first, and probably not the last

DuneSlide is the latest in a run of Cursor bugs that start with a poisoned prompt and end in code execution, each one defeating a different guardrail. [The Hacker News covered the earlier rounds](https://thehackernews.com/2025/08/cursor-ai-code-editor-fixed-flaw.html):

* [CurXecute](https://thehackernews.com/2025/08/cursor-ai-code-editor-fixed-flaw.html) (CVE-2025-54135, August 2025) came from the same team, then operating as Aim Security. A planted Slack message rewrote Cursor's ~/.cursor/mcp.json config and ran commands even after the user rejected the edit. Fixed in 1.3.
* [MCPoison](https://thehackernews.com/2025/08/cursor-ai-code-editor-vulnerability.html) (CVE-2025-54136), from Check Point Research, lets an attacker get an MCP config approved once, then quietly swap in malicious commands with no second prompt.
* [CVE-2026-26268](https://thehackernews.com/2026/04/google-fixes-cvss-10-gemini-cli-ci-rce.html) (February 2026) hid a booby-trapped Git hook in a repository that fired the moment the agent ran a Git command. Patched in 2.5.

The sandbox in the 2.x line was Cursor's answer to that earlier wave. DuneSlide is about escaping the answer.

Cato says it is disclosing similar fla...