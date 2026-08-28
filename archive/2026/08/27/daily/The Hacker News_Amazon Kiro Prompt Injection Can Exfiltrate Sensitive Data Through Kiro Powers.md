---
title: Amazon Kiro Prompt Injection Can Exfiltrate Sensitive Data Through Kiro Powers
url: https://thehackernews.com/2026/08/amazon-kiro-prompt-injection-can.html
source: The Hacker News
date: 2026-08-27
fetch_date: 2026-08-28T13:37:58.688936
---

# Amazon Kiro Prompt Injection Can Exfiltrate Sensitive Data Through Kiro Powers

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

[![cybersecurity](https://blogger.googleusercontent.com/img/b/R29vZ2xl/AVvXsEipoZWeZ29mSf60rRpMZ3Ucnm7oeWBfslPFPT6xADBsdvBtjd20ovH2yLscUo8pS6OTK0ItATC25VeavJh73IgqJM6Nb3apqobQ9zEVISE-d0wEFAimLYUcnffWCTowCCqs5LofRTQP25xB32KzYhlTO8lUnkZfmtELv23LlgdeKY3nyS2etYQXGdPIQtnh/s728-e100/wiz-d.png)](https://thehackernews.uk/ai-security-playbook-d)

# [Amazon Kiro Prompt Injection Can Exfiltrate Sensitive Data Through Kiro Powers](https://thehackernews.com/2026/08/amazon-kiro-prompt-injection-can.html)

**Ravie Lakshmanan**Aug 27, 2026Vulnerability / Artificial Intelligence

[![](data:image/png;base64...)](https://blogger.googleusercontent.com/img/b/R29vZ2xl/AVvXsEhUdyQnHdjoEXFnc-5nB-6oglAbvpOYwuWqfjYkgeKH6HaqUjosKOHhmEQ_7StMkMBv53gz27Ilg-15yRaQ-hxoYi0ASuRMOCuPTHa8gP6a6PzYSewTWsDkKAx8dsMByZXDYDlRE1wRYoCvE7NuYqXdCpZ8_Y4E4tAUy0SBFl0S_XxLvpnjFRbqat0EwggW/s1700-e365/kiro-amazon.jpg)

Cybersecurity researchers have disclosed details of a vulnerability in Amazon Kiro, an artificial intelligence (AI)-powered, agentic integrated development environment (IDE), that could facilitate data exfiltration via prompt injection and Kiro Powers.

The security flaw, which does not have a CVE identifier, works against Kiro IDE 0.7.45 on Windows, according to Mindgard. The latest version of the IDE is 1.0.337.

"The issue allowed attacker-controlled repository content to influence the Kiro agent and ultimately cause sensitive local information to be transmitted to an external endpoint," Chief Marketing Officer Fergal Glynn [said](https://mindgard.ai/blog/amazon-kiro-data-exfiltration) in a report shared with The Hacker News.

[Kiro Powers](https://kiro.dev/blog/introducing-powers/) goes beyond skills by bundling Model Context Protocol (MCP) server configurations, [steering files](https://kiro.dev/docs/steering/) ("POWER.md"), hooks, and contextual knowledge. The steering file is like an "onboarding manual" that provides persistent context and tells the AI agent what MCP tools are available and when to use them.

According to Mindgard, successful exploitation requires two user actions: the user has to open the malicious project through a workspace file using File → Open Workspace From File rather than opening the folder directly and then send a message to the agent. The vulnerability is reproducible against both trusted and untrusted workspaces.

[![Cybersecurity](data:image/png;base64...)](https://thehackernews.uk/zero-trust-claude-d)

Once these conditions are satisfied, sensitive workspace data can be exfiltrated to the attacker "without the user explicitly requesting that Kiro access or transmit" it. The exploitation difficulty has been assessed as low.

What makes this flaw notable is that the user does not have to submit a malicious prompt or reference the attacker-controlled content. Once the crafted workspace file is opened, sending any message is enough to trigger the vulnerable flow.

"The vulnerability appears when attacker-controlled project content is interpreted as instructions, and those instructions are allowed to influence security-sensitive operations elsewhere in the IDE," Mindgard said.

"The trust boundary failure occurs across the entire sequence. Repository-controlled content influences the agent, the agent reads sensitive local information, the agent writes that information into security-relevant IDE configuration, and a subsequent IDE capability turns the modified configuration into network activity."

As AI development environments increasingly bring interpretation and execution together within the same workflow, repository files can be used to provide context to a model, while the agent can read files, invoke tools, and activate other functionality in the application, potentially leading to trust boundary failures.

Following responsible disclosure, a fix for the flaw was [implemented](https://kiro.dev/changelog/ide/) by Amazon in Kiro IDE version 0.8.140. "We addressed this finding, in the January 15 Kiro IDE update, shortly after it was reported to us," an Amazon spokesperson told The Hacker News. "As always, we recommend customers install the latest version of Kiro to ensure they receive these security updates."

The vulnerability also builds upon a previous bug highlighted by Mindguard that allowed steering-file directives to cause local information to be incorporated into a Markdown image request and transmitted to an external server.

"By carefully crafting a steering file to read a local file and render a Markdown image, an attacker can coerce the AI to send sensitive data to an external server," Mindgard [noted](https://mindgard.ai/disclosures/amazon-kiro-ide-data-exfiltration-via-steering-file) at the time.

This is not the first time vulnerabilities have been disclosed in Kiro. In June 2026, Amazon [addressed](https://cymulate.com/blog/zero-click-rce-prompt-injection-ai-tools/) an insufficient access control flaw ([CVE-2026-10591](https://aws.amazon.com/security/security-bulletins/2026-037-aws/), CVSS score: 8.8) that could have enabled a remote unauthenticated actor to execute arbitrary commands via crafted instructions that cause writes to execution-sensitive paths, such as ".vscode/tasks.json" or "~/.kiro/settings/mcp.json," and facilitate auto-execution on folder open.

"By planting hidden instructions in a web page Kiro reads, an attacker can make Kiro rewrite its own MCP (Model Context Protocol) server configuration file and gain arbitrary code execution on the developer's machine," Intezer [said](https://research.intezer.com/blog/2026/07/remote-code-execution-kiro/). "No suspicious approval prompt is ever shown to the user. All the developer asked Kiro to do was perform a legitimate action."

[![Cybersecurity](data:image/png;base64...)](https://thehackernews.uk/corelight-d)

The findings also come against the backdrop of a number of security issues discovered in AI tools -

* A vulnerability chain in [OpenAI Codex CLI](https://cymulate.com/blog/codex-cli-rce-prompt-injection-mitigations/) for Windows that abuses prompt injection through web.run to turn a routine web search into covert host-level command execution outside the built-in sandbox feature
* A zero-click remote code execution vulnerability in [Cursor CLI](https://cymulate.com/blog/zero-click-rce-prompt-injection-ai-tools/) that uses indirect prompt injection to wr...