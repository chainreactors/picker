---
title: Researchers Uncover 30+ Flaws in AI Coding Tools Enabling Data Theft and RCE Attacks
url: https://thehackernews.com/2025/12/researchers-uncover-30-flaws-in-ai.html
source: The Hacker News
date: 2025-12-06
fetch_date: 2025-12-07T03:26:28.597513
---

# Researchers Uncover 30+ Flaws in AI Coding Tools Enabling Data Theft and RCE Attacks

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

[![Salesforce Security Handbook](https://blogger.googleusercontent.com/img/b/R29vZ2xl/AVvXsEi4PKjL50qMNKKq6z8Ofu7tXpz51soFtMEKzX6_qMTj-_Exp3EctK0Z7KiOlubgst1DxPrrk8TgthgjViGZmg4FlcOYG8L63G_dX8731tRGkOc42mbtdMv6KDyjdNKRdCPHkhUQJmcoxcFKLcQjeILTu-wEtAOXsTp7JyWMIuP0k1RJo9sZjTo5dYL8CyFQ/s728-e100/z-dd.png)](https://thehackernews.uk/zz--header-d)

# [Researchers Uncover 30+ Flaws in AI Coding Tools Enabling Data Theft and RCE Attacks](https://thehackernews.com/2025/12/researchers-uncover-30-flaws-in-ai.html)

**Dec 06, 2025**Ravie LakshmananAI Security / Vulnerability

[![](data:image/png;base64...)](https://blogger.googleusercontent.com/img/b/R29vZ2xl/AVvXsEhyOpPc8ucnigXsFagXjVCnBwywXC-OOemw_QXXkGAPjAa1YKv0ViLZEPg0AtaGss65NKfl2M7gR9XwjgbFHgxPliOMkLEJ14VEXyLuuqwvqkH0Hj4aCDGKBbRtKuX3j3hmHCD05EKU1K74YgR8m4TdZu2_CZ_cqnWLZRmuvitlyjUW6wE2suxA8Y8oHGNY/s790-rw-e365/ai-coding.jpg)

Over 30 security vulnerabilities have been disclosed in various artificial intelligence (AI)-powered Integrated Development Environments (IDEs) that combine [prompt injection primitives](https://thehackernews.com/2025/11/researchers-find-chatgpt.html) with legitimate features to achieve data exfiltration and remote code execution.

The security shortcomings have been collectively named **[IDEsaster](https://maccarita.com/posts/idesaster/)** by security researcher Ari Marzouk (MaccariTA). They affect popular IDEs and extensions such as Cursor, Windsurf, Kiro.dev, GitHub Copilot, Zed.dev, Roo Code, Junie, and Cline, among others. Of these, 24 have been assigned CVE identifiers.

"I think the fact that multiple universal attack chains affected each and every AI IDE tested is the most surprising finding of this research," Marzouk told The Hacker News.

"All AI IDEs (and coding assistants that integrate with them) effectively ignore the base software (IDE) in their threat model. They treat their features as inherently safe because they've been there for years. However, once you add AI agents that can act autonomously, the same features can be weaponized into data exfiltration and RCE primitives."

At its core, these issues chain three different vectors that are common to AI-driven IDEs -

* Bypass a large language model's (LLM) guardrails to hijack the context and perform the attacker's bidding (aka prompt injection)
* Perform certain actions without requiring any user interaction via an AI agent's auto-approved tool calls
* Trigger an IDE's legitimate features that allow an attacker to break out of the security boundary to leak sensitive data or execute arbitrary commands

The highlighted issues are different from prior attack chains that have leveraged prompt injections in conjunction with vulnerable tools (or abusing legitimate tools to perform read or write actions) to modify an AI agent's configuration to achieve code execution or other unintended behavior.

[![Cybersecurity](data:image/png;base64...)](https://thehackernews.uk/rat-d)

What makes IDEsaster notable is that it takes prompt injection primitives and an agent's tools, using them to activate legitimate features of the IDE to result in information leakage or command execution.

Context hijacking can be pulled off in myriad ways, including through user-added context references that can take the form of pasted URLs or text with hidden characters that are not visible to the human eye, but can be parsed by the LLM. Alternatively, the context can be polluted by using a Model Context Protocol (MCP) server through [tool poisoning](https://thehackernews.com/2025/06/zero-click-ai-vulnerability-exposes.html) or [rug pulls](https://thehackernews.com/2025/09/two-critical-flaws-uncovered-in.html), or when a legitimate MCP server parses attacker-controlled input from an external source.

Some of the identified attacks made possible by the new exploit chain is as follows -

* **[CVE-2025-49150](https://www.cve.org/CVERecord?id=CVE-2025-49150) (Cursor), [CVE-2025-53097](https://www.cve.org/CVERecord?id=CVE-2025-53097) (Roo Code), [CVE-2025-58335](https://www.cve.org/CVERecord?id=CVE-2025-58335) (JetBrains Junie), GitHub Copilot (no CVE), Kiro.dev (no CVE), and Claude Code (addressed with a [security warning](https://code.claude.com/docs/en/vs-code#security-considerations))** - Using a prompt injection to read a sensitive file using either a legitimate ("read\_file") or vulnerable tool ("search\_files" or "search\_project") and writing a JSON file via a legitimate tool ("write\_file" or "edit\_file)) with a remote JSON schema hosted on an attacker-controlled domain, causing the data to be leaked when the IDE makes a GET request
* **[CVE-2025-53773](https://www.cve.org/CVERecord?id=CVE-2025-53773) (GitHub Copilot), [CVE-2025-54130](https://www.cve.org/CVERecord?id=CVE-2025-54130) (Cursor), [CVE-2025-53536](https://www.cve.org/CVERecord?id=CVE-2025-53536) (Roo Code), [CVE-2025-55012](https://www.cve.org/CVERecord?id=CVE-2025-55012) (Zed.dev), and Claude Code (addressed with a [security warning](https://code.claude.com/docs/en/vs-code#security-considerations))** - Using a prompt injection to edit IDE settings files (".vscode/settings.json" or ".idea/workspace.xml") to achieve code execution by setting "php.validate.executablePath" or "PATH\_TO\_GIT" to the path of an executable file containing malicious code
* **[CVE-2025-64660](https://www.cve.org/CVERecord?id=CVE-2025-64660) (GitHub Copilot), [CVE-2025-61590](https://www.cve.org/CVERecord?id=CVE-2025-61590) (Cursor), and [CVE-2025-58372](https://www.cve.org/CVERecord?id=CVE-2025-58372) (Roo Code)** - Using a prompt injection to edit workspace configuration files (\*.code-workspace) and override [multi-root workspace](https://code.visualstudio.com/docs/editing/workspaces/multi-root-workspaces) settings to achieve code execution

It's worth noting that the last two examples hinge on an AI agent being configured to auto-approve file writes, which subsequently allows an attacker with the ability to influence prompts to cause malicious workspace settings to be written. But given that this behavior is auto-approved by default for in-workspace files, it leads to arbitrary code execution without any user interaction or the need to reopen the workspace.

[![](data:image/png;base64...)](https://blogger.googleusercontent.com/img/b/R29vZ2xl/AVvXsEhb05MykrUDlN25IKSGChV8S1xmJ-rhH87CbE6UXZcXoSp8uh-jgsFtqbRFA91hETePSja1B4Z4UxW47uCIMGbrjLPOJZ693I4...