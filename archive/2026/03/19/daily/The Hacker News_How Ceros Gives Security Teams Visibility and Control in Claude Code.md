---
title: How Ceros Gives Security Teams Visibility and Control in Claude Code
url: https://thehackernews.com/2026/03/how-ceros-gives-security-teams.html
source: The Hacker News
date: 2026-03-19
fetch_date: 2026-03-20T04:09:25.431659
---

# How Ceros Gives Security Teams Visibility and Control in Claude Code

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

[![Security Service Edge](https://blogger.googleusercontent.com/img/b/R29vZ2xl/AVvXsEguiZ85S7494GyqhFt9uP48C8ggEnb3bp9Qmsdv4LOYjNWfa98MKx17Dk7o1nJrEV3ai3edIGIgwt6oO5iJMmYLcyu6PojcvJnO4IfLhVK2dzGKFyEroFjKQhnp2hd5Cc6G4CynJRfb55aclnGwj7rse9jMncn_vu_tFqQZtHZH3Sb5dMXwRKN-kSVYUMzD/s1700-e365/ai-d.png)](https://thehackernews.uk/wiz-ai-security-d)

# [How Ceros Gives Security Teams Visibility and Control in Claude Code](https://thehackernews.com/2026/03/how-ceros-gives-security-teams.html)

**The Hacker News**Mar 19, 2026Artificial Intelligence / Enterprise Security

[![Claude Code](data:image/png;base64... "Claude Code")](https://blogger.googleusercontent.com/img/b/R29vZ2xl/AVvXsEh8B3hISiw4s7wL5Eruja2BnTYM2QNrpsi6FnTtzznVz-Vu1pERgS-lZuIVKrps6nlxaauzfCXNfiiSInowjXHDhZ3UgoGD7OlFtwijFG0w5MtfnGu920etTBYP0tHnauL6Owztp_K0I8DUXlMSWd2LZz57O8NFm83E8H5QZ7Kb7RCOja4c-viaPrf9lC8/s1700-e365/bi.jpg)

Security teams have spent years building identity and access controls for human users and service accounts. But a new category of actor has quietly entered most enterprise environments, and it operates entirely outside those controls.

Claude Code, Anthropic's AI coding agent, is now running across engineering organizations at scale. It reads files, executes shell commands, calls external APIs, and connects to third-party integrations called MCP servers. It does all of this autonomously, with the full permissions of the developer who launched it, on the developer's local machine, before any network-layer security tool can see it. It leaves no audit trail that the existing security infrastructure was built to capture.

This walkthrough covers Ceros, an AI Trust Layer built by [Beyond Identity](https://beyondidentity.ai) that sits directly on the developer's machine alongside Claude Code and provides real-time visibility, runtime policy enforcement, and a cryptographic audit trail of every action the agent takes.

## **The Problem: Claude Code Operates Outside Existing Security Controls**

Before walking through the product, it helps to understand why existing tools cannot address this problem.

Most enterprise security tooling sits at the network edge or the API gateway. These tools see traffic after it leaves the machine. By the time a SIEM ingests an event or a network monitor flags unusual traffic, Claude Code has already acted: the file has already been read, the shell command has already executed, and the data has already moved.

Claude Code's behavioral profile compounds this problem significantly. It lives off the land, using tools and permissions already on the developer's machine rather than bringing its own. It communicates through external model calls that look like normal traffic. It executes complex sequences of actions that no human explicitly programmed. And it runs with the full inherited permissions of whoever launched it, including access to credentials, production systems, and sensitive data that developers happen to have on their machine.

The result is a gap that network-layer tools structurally cannot close: everything Claude Code does on the local machine, before any request leaves the device. That is where Ceros operates.

## **Getting Started: Two Commands, Thirty Seconds**

Ceros is designed so that installation does not disrupt developer workflow. Setup requires two commands:

```
curl -fsSL https://agent.beyondidentity.com/install.sh | bash

ceros claude
```

[![](data:image/png;base64...)](https://blogger.googleusercontent.com/img/b/R29vZ2xl/AVvXsEhGM3m4-7yZcn9DVo5KaXL3BQGJrKPtlQ9L6Yco7djdRya8kG3c6vksbAgZmOz47xdPRRmXgQuuPNy6725uGqWP_go6Y6EWsmDHLhL8D9xjq7Y5FPHkS5tYeZ5I0722Gzdpv5lOp9AB_YFGhkncbCusGzelVNznT3t3UgfLDhMc9F808ROz4ighpRkfpK4/s1700-e365/getting-started.png)

The first command installs the CLI. The second launches Claude Code through Ceros. A browser window opens, prompts for an email address, and sends a six-digit verification code. After entering the code, Claude Code starts up and works exactly as it did before. From the developer's perspective, nothing has changed.

For organization-wide rollouts, administrators can configure Ceros so that developers are prompted to enroll automatically when they launch Claude Code. Security becomes invisible to the developer, which is the only way security actually gets adopted at scale.

Once enrolled, before Claude Code generates a single token, Ceros captures full device context, including OS, kernel version, disk encryption status, Secure Boot state, and endpoint protection status, all in under 250 milliseconds. It captures the complete process ancestry of how Claude Code was invoked, with binary hashes of every executable in the chain. And it ties the session to a verified human identity through Beyond Identity's platform, signed with a hardware-bound cryptographic key.

## **The Console: See What Claude Code Has Actually Been Doing**

After enrolling a device and running Claude Code normally for a few days, navigating to the Ceros admin console reveals something most security teams have never seen before: a complete record of what Claude Code has actually been doing across their environment.

[![](data:image/png;base64...)](https://blogger.googleusercontent.com/img/b/R29vZ2xl/AVvXsEiXoaGMU_WlJIBW5uTtyVOZBysYmpEmJrmqZdHxWoiZwo4cB7SeMXyHBl8ITZrLV-SMbQAZ64_2SHkLD-4MHP8TPT4IPDvE5gbL6c1JR4K1bwOxGRFEoXDmbcl-p96FCKaTmkG2RbOkCtvTw4hDn_lAFKtcBhQF_eulPIMKWgaz2Dd2T5T4emBafZeXjq8/s1700-e365/conversations.png)

**The Conversations view** shows every session between a developer and Claude Code across all enrolled devices, listed by user, device, and timestamp. Clicking into any conversation shows the full back-and-forth between the developer and the agent. But between the prompts and responses, something else is visible: tool calls.

When a developer asks Claude Code something as simple as "what files are in my directory?", the LLM does not simply know the answer. It instructs the agent to execute a tool on the local machine, in this case bash ls -la. That shell command runs on the developer's device with the developer's permissions. One casual question triggers real execution on a real machine.

The Conversations view surfaces every one of these tool invocations across every session. For most security teams, this is the first time they have seen this data.

[![](data:image/...