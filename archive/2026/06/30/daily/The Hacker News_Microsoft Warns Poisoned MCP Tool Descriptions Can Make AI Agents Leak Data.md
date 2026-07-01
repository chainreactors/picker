---
title: Microsoft Warns Poisoned MCP Tool Descriptions Can Make AI Agents Leak Data
url: https://thehackernews.com/2026/06/microsoft-warns-poisoned-mcp-tool.html
source: The Hacker News
date: 2026-06-30
fetch_date: 2026-07-01T06:24:40.068634
---

# Microsoft Warns Poisoned MCP Tool Descriptions Can Make AI Agents Leak Data

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

[![cybersecurity](https://blogger.googleusercontent.com/img/b/R29vZ2xl/AVvXsEjQl2axNwsfhbXOFynrg_uAZsvHi3OvNGSA8KJO-BKR8Xm3x7yjKV3EvfY4v5mwXx6LF0uWFb9h9d9iAV_Pi-YYhqimX9wx4OaLdDJEdR215Xrxq_PAtXkaLfQso4pTSjbj6fvh_ZTliLpzWZSZfcoZgyXtKwhN-SSDDlmbtUqGLshc0KqYQGWYHMN52Sl1/s728-e100/zz-d.jpg)](https://thehackernews.uk/ai-vuln-protection-d)

# [Microsoft Warns Poisoned MCP Tool Descriptions Can Make AI Agents Leak Data](https://thehackernews.com/2026/06/microsoft-warns-poisoned-mcp-tool.html)

**Swati Khandelwal**Jun 30, 2026Artificial Intelligence / Supply Chain Security

[![](data:image/png;base64...)](https://blogger.googleusercontent.com/img/b/R29vZ2xl/AVvXsEjbjfrraZ05p0kN5CedcQSOZYouoHGrdpCvi9TGxEZM_9zlXc_juWZ1F8VsvjV9c-iD7Ejgj0V6b0uYwOb9mLpb7ALcOVk53m2ppmg6mDI3qwANc8KZFMt3X7H7fT_Eym3OJijFmr0CZS6yJNTtf4kef0gOYtbx6A3LYa15PNzpzJuOg-nd6orLosZzfQ8/s1700-e365/ms-ai.jpg)

New Microsoft research shows how attackers can hijack AI agents that act on a user's behalf, using nothing more than a poisoned tool description to make the agent quietly hand over company data to an outsider.

The trick is that the agent never breaks a rule. Every step looks routine, so in a default setup no alarm may fire.

The work comes from Microsoft Incident Response and its Defender security research team, and it lands as companies start letting AI do more than read and summarize.

## What changes when an agent can act

Until recently, the workplace AI risk was mostly framed around what a model read and wrote. A poisoned document could skew an answer, and that was mostly where it ended.

Agents are different. Microsoft 365 Copilot can send email, create files, and change calendars. Custom agents built in Copilot Studio or Azure AI Foundry can reach into business systems and run multi-step jobs on their own.

The same injection trick that biases a summary now triggers an action. Against a reader, an attack changes the output. Against an agent, it changes what the software actually does.

[![Cybersecurity](data:image/png;base64...)](https://thehackernews.uk/ai-cant-stop-d)

These agents reach business systems through MCP, the [Model Context Protocol](https://modelcontextprotocol.io/specification/2025-06-18), an open protocol that lets an AI call outside tools the way an app calls an API. Microsoft calls it the fastest-growing part of the agentic AI supply chain, which makes it an expanding attack surface.

## How the attack works

Every MCP tool ships with a description: a few lines of plain text that tell the agent what the tool does and when to use it. The agent reads that text to decide how to act. That is the whole weakness. The description is just words, and words can carry instructions.

Microsoft [walks through](https://www.microsoft.com/en-us/security/blog/2026/06/30/securing-ai-agents-ai-tools-move-from-reading-acting/) it with an invoice example, built to show the pattern rather than report a named victim. A finance team stands up an agent to handle vendor invoices. It connects to three tools, including a third-party "invoice enrichment" service that was approved for use but never given a real security review.

Then the attacker updates that third-party tool. The name and the visible summary stay the same. Buried in the description, dressed up as formatting notes, is a hidden order: grab the last thirty unpaid invoices and attach them to the next call. MCP picks up description changes on the fly. In setups without a re-approval trigger, the poisoned version goes live with no extra review.

After that, an analyst asks a routine question about a supplier. The agent follows the hidden order, collects the invoices and sends them along as part of a normal-looking request. The tool returns a clean answer and quietly copies the stolen data to a server the attacker controls. The analyst sees nothing wrong.

Each move the agent makes is legitimate on its own. The tool was approved. The data query ran with the analyst's own permissions. The outbound call went to a server that was allowed when it was added. The weakness is not in any one system. It lives in what Microsoft calls "the trust boundary between them."

[![](data:image/png;base64...)](https://blogger.googleusercontent.com/img/b/R29vZ2xl/AVvXsEgPHsb5TU99zvKewyhyXM6X7roemtJw1sSMlDBdGhFUQsw-3FfbEzLUZL9VYzfs3SIWAih_U7vYD7Pp1T_REK_uHO6zkOhn_j3psNxSmRLTmbyi2xUBAW7TLMpWBek0PrC1ulFdanu7gvT57UcT4EMk5TMUFQwfU0QZY9NTJKEyy0n7JS_a2JnmOd1QMNw/s1700-e365/attack-chain.jpg)

The deeper problem is that MCP mixes instructions and data in the same place. A tool's description lives in the agent's working memory right next to its real orders, so editing that description can steer the agent as effectively as rewriting its system prompt.

The agent has no reliable way to tell an honest instruction from a malicious one slipped in by whoever maintains the tool. Microsoft notes this is not a bug in Copilot itself. It is a trust gap opened up by plugging in outside tools.

## What defenders should do

Microsoft's advice, stripped to plain terms:

* Treat every connected tool as part of your supply chain. Keep a list of approved tool publishers, turn off "allow all," and let an agent use only the specific tools it needs.
* Treat a tool's description like a system prompt. Review changes to it the way you would review a code change, and scan the text for commands that have no business sitting in a help field.
* Put a human in front of risky actions. Anything that moves money, shares data outside the company, or changes accounts should need a person to approve it.
* Give each agent its own identity and watch what it does. Log its actions, set a baseline for normal, and flag new endpoints, larger data pulls, or odd queries.
* Apply least agency, not just least privilege. Even a low-permission agent can do real harm if it is allowed to act without checks.

Microsoft maps its own products to each step, including Prompt Shields, Purview DLP, Entra Agent ID, Defender for Cloud, and Sentinel, but the principles hold whatever stack you run.

## Not a theory: how we got here

This class of attack has a paper trail. Invariant Labs named ["tool poisoning"](https://thehackernews.com/2025/04/new-reports-uncover-jailbreaks-unsafe.html) in April 2025, with a [proof of concept](https://invariantlabs.ai/blog/mcp-security-notification-tool-poisoning-attacks)...