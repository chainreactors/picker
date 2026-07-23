---
title: Microsoft Azure DevOps MCP Flaw Lets Hidden PR Comments Hijack AI Review Agents
url: https://thehackernews.com/2026/07/microsoft-azure-devops-mcp-flaw-lets.html
source: The Hacker News
date: 2026-07-22
fetch_date: 2026-07-23T05:11:48.580018
---

# Microsoft Azure DevOps MCP Flaw Lets Hidden PR Comments Hijack AI Review Agents

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

# [Microsoft Azure DevOps MCP Flaw Lets Hidden PR Comments Hijack AI Review Agents](https://thehackernews.com/2026/07/microsoft-azure-devops-mcp-flaw-lets.html)

**Swati Khandelwal**Jul 22, 2026AI Security / DevSecOps

[![](data:image/png;base64...)](https://blogger.googleusercontent.com/img/b/R29vZ2xl/AVvXsEiyPnXNVcT-TTMj4bnJJGmkaK6DFi2Lr2KDvnQZiPIyboMvPfwGP-xlkXhEAq1-bY1fkI_eSiaMEY0JxhHvMYB5X_i_aDK04yiPGrSIk9cXL9P-9cwn2ftFhqCto-5dAxILlsZITCPhQ6Kf2h0_5Ly9YSvo5T2z8sNe5ZDPZxR-S-JslYxH-q9FoPUUJtA/s1700-e365/inject.jpg)

A single invisible comment in an Azure DevOps pull request can turn a reviewer's own AI coding agent against them, driving it into projects the attacker has no rights to reach and quietly leaking what it finds.

The flaw is in Microsoft's official [Azure DevOps MCP server](https://github.com/microsoft/azure-devops-mcp), and it works because one of its tools returns pull request descriptions without a prompt-injection guardrail the company had already applied to others.

Agentic Runtime Security firm [Manifold Security](https://www.manifold.security/blog/azure-devops-mcp-server-vulnerability) detailed the confused-deputy bug this week. Microsoft ships the server so AI agents can read and operate Azure DevOps for a user, across pull requests, pipelines, wikis, and work items, all with the user's own permissions. That is the whole problem: content other people wrote can become instructions the agent acts on.

Azure DevOps PR descriptions accept Markdown, which allows HTML comments. In the web UI, an HTML comment (<!-- ... -->) renders as nothing, so a reviewer scrolling the description sees an ordinary change. The REST API returns it verbatim, and the server hands that text straight to the agent.

That split between what the human sees and what the model receives is the delivery mechanism: the attacker never talks to the agent but plants instructions in content they know it will later read.

When the reviewer asks their agent to review the PR, the hidden text can rewrite the agent's goal. The agent is carrying the reviewer's credentials, so it can act across projects the attacker has no rights to reach.

[![Cybersecurity](data:image/png;base64...)](https://thehackernews.uk/ai-vuln-protection-d)

Manifold says that access reaches source code, secrets, and work items, not just the wiki page its proof of concept exfiltrated. The firm calls the escalation the normal case, since reviewers are often more senior than whoever opened the pull request. The attacker gains nothing directly; they borrow the reviewer's access through text the reviewer never sees.

## The pull request path missed the guardrail

What lifts this above a generic prompt-injection warning is that Microsoft already shipped a defense for it. Reading the server's source, Manifold found it uses spotlighting, a technique from [Microsoft's own guidance on indirect prompt injection](https://www.microsoft.com/en-us/msrc/blog/2025/07/how-microsoft-defends-against-indirect-prompt-injection-attacks): it wraps untrusted content in delimiters so the model can tell data apart from the instructions it should follow.

The company added it in [PR #1062](https://github.com/microsoft/azure-devops-mcp/pull/1062), where the wiki-page and build-log tools pass their output through a shared helper, createExternalContentResponse. The tool that returns a pull request, repo\_get\_pull\_request\_by\_id, never calls it, so it hands back the description raw, which is exactly the surface an attacker writes to.

The Hacker News confirmed the same [path](https://github.com/microsoft/azure-devops-mcp/blob/main/src/tools/repositories.ts) is still uncovered in the current source as of July 21.

In Manifold's proof of concept, run on a local build of v2.7.0, a contributor to one project opens a normal-looking PR whose hidden comment carries the payload. Once the agent starts its review, the tool trace runs a chain: it triggers a pipeline in a different project, reads a confidential wiki page the attacker cannot open, and posts that page back as a comment on the PR, where the attacker reads it.

A single hidden comment drove the whole sequence, and every call in it was one the agent was allowed to make. The problem, the researchers wrote, was "the sequence and intent, driven by text that a human never saw." The team reproduced it with both Copilot CLI and Claude Code, so it is not tied to one agent.

The chain has prerequisites, though: attacker-written PR text, a workflow that feeds it to an agent, a reviewer whose access exceeds the attacker's, and an agent cleared to run tools without asking.

Manifold confirmed it tested that last part as an auto-approve posture with no per-tool prompts, the checkpoint that would otherwise let a reviewer catch an odd cross-project pipeline run before it fires. A broad token plus that posture is where the risk concentrates.

The demo assumes a person kicks off the review, but Manifold notes where teams are heading: automated review, triage, and summaries fired by triggers, with no human prompting each run or reading each result. In that setup, the planted description fires on its own, and the leak runs longer before anyone notices.

The pattern is not new. In May 2025, Invariant Labs showed the same class of attack against [GitHub's MCP server](https://invariantlabs.ai/blog/mcp-github-vulnerability), using a public issue to push an agent into reading a private repo and leaking it through a pull request; the same technique has since [reached automated GitHub agent workflows](https://thehackernews.com/2026/07/public-github-issue-could-trick-github.html).

That case was one of the examples Simon Willison pointed to in naming the [lethal trifecta](https://simonwillison.net/2025/Jun/16/the-lethal-trifecta/): an agent with access to private data, exposure to untrusted content, and a way to send data out. Any agent with all three can be turned on its owner by one piece of text, and most useful ones have all three.

A Microsoft sp...