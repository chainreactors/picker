---
title: AWS, Google, and Vercel Agent Flaws Let Attackers Trigger Tools Without Running the Model
url: https://thehackernews.com/2026/08/aws-google-and-vercel-patch-agent-flaws.html
source: The Hacker News
date: 2026-08-06
fetch_date: 2026-08-07T04:30:25.962499
---

# AWS, Google, and Vercel Agent Flaws Let Attackers Trigger Tools Without Running the Model

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

![cybersecurity](data:image/svg+xml;base64...)

# [AWS, Google, and Vercel Agent Flaws Let Attackers Trigger Tools Without Running the Model](https://thehackernews.com/2026/08/aws-google-and-vercel-patch-agent-flaws.html)

**Swati Khandelwal**Aug 06, 2026DevSecOps / Vulnerability

[![](data:image/png;base64...)](https://blogger.googleusercontent.com/img/b/R29vZ2xl/AVvXsEhNMtOKfZBxSDQ1928IVtFay3f8_6go4rnTY6yFaQYCzAdGt3e6uBkZfZkoFtHbS_cEbTCri3ZNVVO7BbuvoVpjGCLSpdphneotNbiXRT3vciQT6dzPa0K81_ee8Al2rxx7GlT5qTS3_B2MKjCCUcHut1pdIeqaLBRjoD5ZqttMcHxZ5AwKea3eL-wruta7/s1700-e365/agent-sdk.jpg)

Security flaws in agent infrastructure from Amazon Web Services (AWS), Google, and Vercel let untrusted or forged instructions reach an agent's tools with no check that a model turn had authorized them.

In several of the attack paths, the model never ran at all, so system prompts, content filters, and model-level guardrails never got a chance to intervene.

The affected products include Amazon Bedrock AgentCore's InvokeHarness API, Google's Agent Development Kit (ADK) for Python, and the Vercel AI SDK harness packages for the Codex and OpenCode coding agents. AWS has fixed the managed service, Google addressed the issues in ADK 2.5.0, and Vercel patched @ai-sdk/harness-codex in version 1.0.29 and @ai-sdk/harness-opencode in version 1.0.28.

These are not identical vulnerabilities and do not share the same attack conditions. AWS involved an authenticated remote request, Google's paths required attacker-controlled session events or user-authored function calls, and Vercel's flaws required untrusted code already running inside a Linux sandbox.

The exposure is bounded by what each agent can already do, so an agent wired to no sensitive tools gains an attacker nothing.

## The Missing Proof Behind a Tool Call

**[Hedi Ingber](https://www.linkedin.com/in/hedi-ingber/)** and **[Aviyam Ivgi](https://www.linkedin.com/in/aviyam-ivgi/)**, co-founders of Stealth, today presented the cross-platform pattern, which they call [CoreBreak](https://blackhat.com/us-26/briefings/schedule/#the-corebreak-attack-turning-ai-agents-into-credentials-exfiltration-vectors-53825), at Black Hat USA 2026. Both answered questions from The Hacker News by email.

In a normal agent flow, the software development kit sends the user's request, system prompt, conversation history, and available tool definitions to the model. The model decides whether to call a tool and returns a structured instruction containing the tool name and arguments. The SDK then executes it.

[![Cybersecurity](data:image/png;base64...)](https://thehackernews.uk/threatlocker-d)

The vulnerable paths did not verify provenance between those last two steps. The runtime received data shaped like a model-generated tool call and treated it as authoritative.

An attacker did not have to persuade the model to break its rules; the attacker could reach the dispatch or authorization path without a legitimate model turn.

## AWS Fixed AgentCore, Strands Retains the Resume Path

AWS's [security bulletin](https://aws.amazon.com/security/security-bulletins/2026-073-aws/) assigns CVE-2026-18830, with a CVSS v4.0 score of 8.6, to insufficient input validation in the [Amazon Bedrock AgentCore](https://thehackernews.com/2026/03/ai-flaws-in-amazon-bedrock-langsmith.html) harness.

An authenticated remote user could place a tool-use content block in the final message of an InvokeHarness request. The event loop could then dispatch the named tool directly without asking the model.

AWS says the issue affected the managed InvokeHarness API before July 31, 2026. It added server-side validation that rejects caller-supplied tool-use blocks before they reach the event loop. The mitigation was applied automatically and does not require customer action.

The managed-service fix does not cover a comparable model-skipping path in the open-source Strands Python code, which the researchers say AgentCore's harness is built on. The current upstream [event\_loop.py](https://github.com/strands-agents/harness-sdk/blob/main/strands-py/src/strands/event_loop/event_loop.py) calls a helper named \_has\_tool\_use\_in\_latest\_message, and when that check passes, the event loop sets the stop reason to tool\_use, takes the latest message directly, and skips model execution.

A comment above that branch reads: "Skip model invocation if the latest message contains ToolUse." The Hacker News confirmed the branch is still present in the repository's main branch as of August 5, 2026.

Immediately above the check sits a narrower branch that restores a tool-use message the agent stored before an interrupt, rather than taking whatever sits in the latest message.

An [April pull request](https://github.com/strands-agents/harness-sdk/pull/2136) warned that externally injected toolUse blocks could reach tool execution without model invocation. The proposed change would have removed the shortcut, but it was closed unmerged on June 19.

The presence of the shortcut does not make every Strands application remotely exploitable. Exposure depends on whether an application permits untrusted callers to submit structured conversation messages, alter stored history, or otherwise place a toolUse block in the position consumed by the event loop.

AWS has not published a separate CVE, affected-version range, or patch notice for standalone Strands deployments. Ingber and Ivgi said AWS told them the behavior falls on the customer's side of its shared-responsibility model, and that the company responded with a documentation change rather than a code fix.

AWS documented the behavior instead. A Strands page titled Trusted Message History, filed under Safety and Security, tells developers that a tool-call block as the most recent message causes the agent to run that tool directly on its next invocation with no model call in between, and that the block's author chooses the tool and its arguments outright. It instructs developers to build message history from their own application rather than from input a caller can shape.

## Two Separate Paths in Google's ADK

The first Google flaw, tracked as [CVE-2026-18236](https://nvd.nist.gov/vuln/detail/CVE-2026-18236) with a CVSS v4.0 score of 9.3, affects [ADK for Python](https://thehackernews.com/2026/08/google-deletes-3-adk-ai-workflows-after.html)...