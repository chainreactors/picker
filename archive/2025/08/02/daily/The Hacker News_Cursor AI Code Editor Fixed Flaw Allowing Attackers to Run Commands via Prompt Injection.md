---
title: Cursor AI Code Editor Fixed Flaw Allowing Attackers to Run Commands via Prompt Injection
url: https://thehackernews.com/2025/08/cursor-ai-code-editor-fixed-flaw.html
source: The Hacker News
date: 2025-08-02
fetch_date: 2025-10-07T00:52:20.313619
---

# Cursor AI Code Editor Fixed Flaw Allowing Attackers to Run Commands via Prompt Injection

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

# [Cursor AI Code Editor Fixed Flaw Allowing Attackers to Run Commands via Prompt Injection](https://thehackernews.com/2025/08/cursor-ai-code-editor-fixed-flaw.html)

**Aug 01, 2025**Ravie LakshmananVulnerability / DevOps

[![](data:image/png;base64...)](https://blogger.googleusercontent.com/img/b/R29vZ2xl/AVvXsEjF-NGVruB_nc_tfwceD9avtPwhEZQYU0Y7Tw3OstrE9Z2hNHIS0OoBfXWRZCn_FgOVhn5CKrrVTpIInm2X_Jr0pI-eEBeRz940PWd0FyN1GCnQQr2nFlqRWUndCF_fuXrCPMQMeDEF1jM7ttsGpfJ5aHzeBPV-LQUa9pXt_kzAXaR09Ne_cY1Oo2EjXcdo/s790-rw-e365/ai-code.jpg)

Cybersecurity researchers have disclosed a now-patched, high-severity security flaw in Cursor, a popular artificial intelligence (AI) code editor, that could result in remote code execution (RCE).

The vulnerability, tracked as **[CVE-2025-54135](https://github.com/cursor/cursor/security/advisories/GHSA-4cxx-hrm3-49rm)** (CVSS score: 8.6), has been addressed in [version 1.3](https://cursor.com/changelog/1-3) released on July 29, 2025. It has been codenamed CurXecute by Aim Labs, which previously disclosed [EchoLeak](https://thehackernews.com/2025/06/zero-click-ai-vulnerability-exposes.html).

"Cursor runs with developer‑level privileges, and when paired with an MCP server that fetches untrusted external data, that data can redirect the agent's control flow and exploit those privileges," the Aim Labs Team [said](https://www.aim.security/lp/aim-labs-curxecute-blogpost) in a report shared with The Hacker News.

"By feeding poisoned data to the agent via MCP, an attacker can gain full remote code execution under the user privileges, and achieve any number of things, including opportunities for ransomware, data theft, AI manipulation and hallucinations, etc."

In other words, the remote code execution can triggered by a single externally‑hosted prompt‑injection that silently rewrites the "~/.cursor/mcp.json" file and runs attacker‑controlled commands.

The vulnerability is similar to EchoLeak in that the tools, which are exposed by Model Control Protocol (MCP) servers for use by AI models and facilitate interaction with external systems, such as querying databases or invoking APIs, could fetch untrusted data that can poison the agent's expected behavior.

Specifically, Aim Security found that the [mcp.json file](https://docs.cursor.com/en/context/mcp#using-mcp-json) used to configure custom MCP servers in Cursor can trigger the execution of any new entry (e.g., adding a Slack MCP server) without requiring any confirmation.

[![DFIR Retainer Services](data:image/png;base64...)](https://thehackernews.uk/cloud-insight-d)

This [auto-run mode](https://docs.cursor.com/en/context/mcp#auto-run) is particularly dangerous because it can lead to the automatic execution of a malicious payload that's injected by the attacker via a Slack message. The attack sequence proceeds as follows -

* User adds Slack MCP server via Cursor UI
* Attacker posts message in a public Slack channel with the command injection payload
* Victim opens a new chat and asks Cursor's agent to use the newly configured Slack MCP server to summarize their messages in a prompt: "Use Slack tools to summarize my messages"
* The agent encounters a specially crafted message designed to inject malicious commands to its context, for instance, altering the configuration file to add another MCP server containing a rogue instruction ("touch ~/<file\_containing\_RCE\_payload")

"The core cause of the flaw is that new entries to the global MCP JSON file are starting automatically," Aim Security said. "Even if the edit is rejected, the code execution had already happened."

The entire attack is noteworthy for its simplicity. But it also highlights how AI-assisted tools can open up new attack surfaces when processing external content, in this case, any third-party MCP server.

"As AI agents keep bridging external, internal, and interactive worlds, security models must assume external context may affect the agent runtime - and monitor every hop," the company added.

Version 1.3 of Cursor also addresses another issue with auto-run mode that can easily circumvent the platform's denylist-based protections using methods like Base64-encoding, shell scripts, and enclosing shell commands within quotes (e.g., "e"cho bypass) to execute unsafe commands.

Following responsible disclosure by the BackSlash Research Team, Cursor has taken the step of altogether deprecating the denylist feature for auto-run in favor of an allowlist.

"Don't expect the built-in security solutions provided by [vibe coding platforms](https://thehackernews.com/2025/03/new-rules-file-backdoor-attack-lets.html) to be comprehensive or foolproof," researchers Mustafa Naamneh and Micah Gold [said](https://www.backslash.security/blog/cursor-ai-security-flaw-autorun-denylist). "The onus is on end-user organizations to ensure agentic systems are equipped with proper guardrails."

The disclosure comes as HiddenLayer also found that Cursor's ineffective denylist approach can be weaponized by embedding hidden malicious instructions with a GitHub README.md file, allowing an attacker to steal API keys, SSH credentials, and even run blocked system commands.

"When the victim viewed the project on GitHub, the prompt injection was not visible, and they asked Cursor to git clone the project and help them set it up, a common occurrence for an IDE-based agentic system," researchers Kasimir Schulz, Kenneth Yeung, and Tom Bonner [noted](https://hiddenlayer.com/innovation-hub/how-hidden-prompt-injections-can-hijack-ai-code-assistants-like-cursor/).

[![CIS Build Kits](data:image/png;base64...)](https://thehackernews.uk/platform-shield-d)

"However, after cloning the project and reviewing the readme to see the instructions to set up the project, the prompt injection took over the AI model and forced it to use the grep tool to find any keys in the user's workspace before exfiltrating the keys with curl."

HiddenLayer said it also found additional weaknesses that could be abused to leak Cursor's system prompt by overriding th...