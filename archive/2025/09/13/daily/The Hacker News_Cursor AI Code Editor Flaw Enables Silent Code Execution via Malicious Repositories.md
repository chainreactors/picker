---
title: Cursor AI Code Editor Flaw Enables Silent Code Execution via Malicious Repositories
url: https://thehackernews.com/2025/09/cursor-ai-code-editor-flaw-enables.html
source: The Hacker News
date: 2025-09-13
fetch_date: 2025-10-02T20:07:18.316438
---

# Cursor AI Code Editor Flaw Enables Silent Code Execution via Malicious Repositories

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

# [Cursor AI Code Editor Flaw Enables Silent Code Execution via Malicious Repositories](https://thehackernews.com/2025/09/cursor-ai-code-editor-flaw-enables.html)

**Sep 12, 2025**Ravie LakshmananAI Security / Vulnerability

[![](data:image/png;base64...)](https://blogger.googleusercontent.com/img/b/R29vZ2xl/AVvXsEjHAKp4IJAmSiZWoK0v8XwpRWrn3YLZ3PZpvLMobinGLjEO70UTmZ36b5CVT00TuJSGsFuBPHO26VzxBZQ3OCgnLB09bj9R0OPIuyO3dm9sTyhvqdttKb1MH2xW6LVamsUJmZweRAreHKA5ddL9T3PMgRwwS6p45PailemmFl61xIGqWOTBmkeangb6d42Q/s790-rw-e365/editor.jpg)

A security weakness has been disclosed in the artificial intelligence (AI)-powered code editor [Cursor](https://thehackernews.com/2025/08/cursor-ai-code-editor-vulnerability.html) that could trigger code execution when a maliciously crafted repository is opened using the program.

The issue stems from the fact that an out-of-the-box security setting is disabled by default, opening the door for attackers to run arbitrary code on users' computers with their privileges.

"Cursor ships with Workspace Trust disabled by default, so VS Code-style tasks configured with runOptions.runOn: 'folderOpen' auto-execute the moment a developer browses a project," Oasis Security [said](https://www.oasis.security/blog/cursor-security-flaw) in an analysis. "A malicious .vscode/tasks.json turns a casual 'open folder' into silent code execution in the user's context."

Cursor is an AI-powered fork of Visual Studio Code, which supports a feature called [Workspace Trust](https://code.visualstudio.com/docs/editing/workspaces/workspace-trust) to allow developers to safely browse and edit code regardless of where it came from or who wrote it.

With this option disabled, an attacker can make available a project in GitHub (or any platform) and include a hidden "autorun" instruction that instructs the IDE to execute a task as soon as a folder is opened, causing malicious code to be executed when the victim attempts to browse the booby-trapped repository in Cursor.

"This has the potential to leak sensitive credentials, modify files, or serve as a vector for broader system compromise, placing Cursor users at significant risk from supply chain attacks," Oasis Security researcher Erez Schwartz said.

To counter this threat, users are advised to enable Workplace Trust in Cursor, open untrusted repositories in a different code editor, and audit them before opening them in the tool.

[![DFIR Retainer Services](data:image/png;base64...)](https://thehackernews.uk/cloud-insight-d)

The development comes as [prompt injections and jailbreaks](https://thehackernews.com/2025/08/cursor-ai-code-editor-fixed-flaw.html) have [emerged](https://thehackernews.com/2025/08/someone-created-first-ai-powered.html) as a stealthy and systemic threat plaguing AI-powered coding and reasoning agents like Claude Code, [Cline](https://embracethered.com/blog/posts/2025/cline-vulnerable-to-data-exfiltration/), [K2 Think](https://adversa.ai/ai-reasoning-leakage-vulnerability-uae-mbzuai-g42-k2-think-jailbreak/), and [Windsurf](https://embracethered.com/blog/posts/2025/windsurf-dangers-lack-of-security-controls-for-mcp-server-tool-invocation/), allowing threat actors to [embed](https://arxiv.org/abs/2411.01077) malicious instructions in [sneaky ways](https://repello.ai/blog/prompt-injection-using-emojis) to trick the systems into performing malicious actions or leaking data from software development environments.

Software supply chain security outfit Checkmarx, in a report last week, revealed how Anthropic's newly introduced [automated security reviews](https://www.anthropic.com/news/automate-security-reviews-with-claude-code) in Claude Code could inadvertently expose projects to security risks, including instructing it to ignore vulnerable code through prompt injections, causing developers to push malicious or insecure code past security reviews.

"In this case, a carefully written comment can convince Claude that even plainly dangerous code is completely safe," the company [said](https://checkmarx.com/zero-post/bypassing-claude-code-how-easy-is-it-to-trick-an-ai-security-reviewer/). "The end result: a developer – whether malicious or just trying to shut Claude up – can easily trick Claude into thinking a vulnerability is safe."

Another problem is that the AI inspection process also generates and executes test cases, which could lead to a scenario where malicious code is run against production databases if Claude Code isn't properly sandboxed.

[![](data:image/png;base64...)](https://blogger.googleusercontent.com/img/b/R29vZ2xl/AVvXsEjNzBhDry7fgrngBCk_6q_dbKgaI2RCQpyEsEnfNWbSQz5bPaXTgu5M7vUj2mbdCZ727V0cX5CRDAt1cnAhvwI3Rtjvp950Gj6TeKJCjoTYJEJmna5Lly1GZ4qAXyNrWDYPy3D0-_YCUJpEEvgiJqw8wWRNSEZtPsYtKpcCP27UC0jM7kPAgF0e4I1ZAky8/s790-rw-e365/claude.jpg)

The AI company, which also recently [launched](https://www.anthropic.com/news/create-files) a new file creation and editing feature in Claude, has warned that the feature carries prompt injection risks due to it running in a "sandboxed computing environment with limited internet access."

Specifically, it's possible for a bad actor to "inconspicuously" add instructions via external files or websites – aka indirect prompt injection – that trick the chatbot into downloading and running untrusted code or reading sensitive data from a knowledge source connected via the Model Context Protocol ([MCP](https://thehackernews.com/2025/07/critical-vulnerability-in-anthropics.html)).

"This means Claude can be tricked into sending information from its context (e.g., prompts, projects, data via MCP, Google integrations) to malicious third parties," Anthropic [said](https://support.anthropic.com/en/articles/12111783-create-and-edit-files-with-claude). "To mitigate these risks, we recommend you monitor Claude while using the feature and stop it if you see it using or accessing data unexpectedly."

That's not all. Late last month, the company also revealed browser-using AI models like Claude for Chrome can face prompt injection attacks, and...