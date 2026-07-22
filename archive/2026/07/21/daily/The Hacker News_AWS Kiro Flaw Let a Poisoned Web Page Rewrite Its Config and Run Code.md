---
title: AWS Kiro Flaw Let a Poisoned Web Page Rewrite Its Config and Run Code
url: https://thehackernews.com/2026/07/aws-kiro-flaw-let-poisoned-web-page.html
source: The Hacker News
date: 2026-07-21
fetch_date: 2026-07-22T05:04:26.262972
---

# AWS Kiro Flaw Let a Poisoned Web Page Rewrite Its Config and Run Code

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

# [AWS Kiro Flaw Let a Poisoned Web Page Rewrite Its Config and Run Code](https://thehackernews.com/2026/07/aws-kiro-flaw-let-poisoned-web-page.html)

**Swati Khandelwal**Jul 21, 2026AI Security / Vulnerability

[![](data:image/png;base64...)](https://blogger.googleusercontent.com/img/b/R29vZ2xl/AVvXsEjJfMUQ_pVP5as41uM_4cR8oRUsCwuXPMLLG63jNd5Djqso9kJyQZLiZgQrMQzykhRaX8BQCydIMPokGoITYY30kc3dH-8iy4Bd-ux36RoIjyNYXtKwb1F1fPdP00hoHD-9Q9s5CGD30w58s5wfyzBGOQvnIxM8JlHkig881HSQQuu4Hk6GBiDJicUYE8o/s1700-e365/AWS-Kiro.jpg)

Hidden text on a web page was enough to make [Kiro](https://kiro.dev/), AWS's agentic coding IDE, rewrite its own configuration file and run an attacker's code on a developer's machine, with no approval step able to stop it.

Intezer, in research with Kodem Security, found that a request as ordinary as asking Kiro to summarize a page could end in remote code execution. AWS has patched the issue, and no CVE has been assigned to it.

Kiro's safety model rests on a human clicking "allow." The agent can run shell commands, fetch URLs, and edit files, and the design assumes a developer reviews anything risky before it happens. That approval step is the security boundary, and the flaw let an attacker slip past it without the developer ever being offered a choice.

The weak point was the file that tells Kiro which external tools to load. Kiro reads its list of Model Context Protocol servers, and the exact command used to start each one, from ~/.kiro/settings/mcp.json.

When that file changes, Kiro reloads it and launches whatever it describes, on the host, with the developer's privileges. At the time of the research, Kiro could write to mcp.json on its own with its fsWrite tool, no approval required, and reload it automatically.

[![Cybersecurity](data:image/png;base64...)](https://thehackernews.uk/ai-vuln-protection-d)

Anyone who could influence the contents of that file could register a server whose start command was arbitrary code, and it would run the moment Kiro reloaded.

Getting text into Kiro's context is the easy part. The agent pulls in outside content whenever a developer asks it to fetch a URL, read documentation, or search the web. Intezer's [proof of concept](https://research.intezer.com/blog/2026/07/remote-code-execution-kiro/) planted its instructions in one-pixel white text (color:#fff;font-size:1px) on an otherwise ordinary API documentation page.

[![](data:image/png;base64...)](https://blogger.googleusercontent.com/img/b/R29vZ2xl/AVvXsEhjFCa72hjHnEUNeUFQvP8xOCl4u7bMrpNgD9WoukDS6G55Q7GyYu_DR7UNPVPrFG-QcnlQBALtNANO8H4aMZ5OSUFhnireSwtknExYgEZ6nxPfk-MVZ4BKP2OeS0soY9KD5WYDO-NGuqCDBC1X81RbwSYCg8z-vNFMjSc2hIBbBCyBhi5yKSCw02VFJpU/s1700-e365/attack-flow.jpg)

The developer sees a clean API reference. Kiro reads the hidden block as a setup task, writes the malicious server into mcp.json, and reloads. Within seconds, the rogue server starts, and the attacker's code is running.

In Intezer's demo, the payload only phoned home with the machine's hostname, username, and platform every ten seconds, just enough to prove execution. The same primitive could run any command available to the developer, enough to steal credentials and source code, plant persistence, or pivot into whatever internal systems they can reach.

The researchers kept their callback pointed at localhost so no real Kiro users were exposed, and they note the attack is not perfectly reliable: the model is non-deterministic and may summarize the page and ignore the hidden block. In their testing, it worked within one or two tries. One success is all it takes.

Kiro did, in some cases, show a pop-up saying the MCP configuration had changed and asking for approval. It made no difference. The configuration reloaded regardless of what the developer clicked, so the warning offered no real protection. The only action the developer ever actually approved was fetching a URL.

## Kiro had been here before

An agent able to write the file that governs what it is allowed to run has surfaced in Kiro before. On Kiro's release day in July 2025, Johann Rehberger of [Embrace The Red](https://embracethered.com/blog/posts/2025/aws-kiro-aribtrary-command-execution-with-indirect-prompt-injection/) showed the same mcp.json write-to-execution move: a prompt injection dropped custom code into an MCP settings file and ran it the moment the file saved.

He flagged a second route too, writing to .vscode/settings.json to allowlist shell commands. AWS's response, Kiro 0.1.42, added an approval prompt for those writes, but [only in Supervised mode](https://aws.amazon.com/security/security-bulletins/AWS-2025-019). The default Autopilot mode kept writing the file on its own, and that is the mode. Intezer's 2026 chain used. No CVE was issued then either.

Others found neighboring versions of the same class. Cymulate reported that Kiro would auto-execute code written to .vscode/tasks.json when a folder was opened. AWS assigned it [CVE-2026-10591](https://aws.amazon.com/security/security-bulletins/2026-037-aws/) (8.8 under CVSS 3.1, 8.6 under CVSS 4.0) and fixed it in the 0.11 series.

Intezer's mcp.json chain was still live on versions 0.9.2 (macOS) and 0.10.16 (Ubuntu) when the company reported it in February 2026, and was confirmed patched in v0.11.130.

AWS's answer was to stop trusting the model's judgment on these files and move the check into the platform. Kiro now marks mcp.json, .vscode/tasks.json, the .git directory, and other sensitive files as [protected paths](https://kiro.dev/docs/privacy-and-security/#protected-paths), each requiring explicit approval before a write.

Its own documentation makes the point directly: "Supervised mode is a code review workflow, not a security control." The 1.0 release that followed leans harder on the same principle, with a [capability-based permissions model](https://kiro.dev/docs/whats-new-1-0/) that prompts for consent on anything a developer has not already allowed.

That combination closes the route Intezer...