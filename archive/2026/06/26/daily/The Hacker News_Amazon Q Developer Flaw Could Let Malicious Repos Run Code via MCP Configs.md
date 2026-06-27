---
title: Amazon Q Developer Flaw Could Let Malicious Repos Run Code via MCP Configs
url: https://thehackernews.com/2026/06/amazon-q-developer-flaw-could-let.html
source: The Hacker News
date: 2026-06-26
fetch_date: 2026-06-27T05:52:30.771318
---

# Amazon Q Developer Flaw Could Let Malicious Repos Run Code via MCP Configs

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

# [Amazon Q Developer Flaw Could Let Malicious Repos Run Code via MCP Configs](https://thehackernews.com/2026/06/amazon-q-developer-flaw-could-let.html)

**Swati Khandelwal**Jun 26, 2026AI Security / Vulnerability

[![](data:image/png;base64...)](https://blogger.googleusercontent.com/img/b/R29vZ2xl/AVvXsEig3gygt20RdznayWN2yru6wSgNt8CSdr16F8I-naxtPn837cr6v0uV0bXdhz36P1XYrpnjmzDXTAtH0wa43Me8rqD2hvET-xQP0ndoX-ddXsypZCjSSNJUqmfl69g96R6yMiUqgXE_NGAL8bl2z6lYutrgKiY74tNIafz_xRsNsJQSB9s_9lSHiybX2kQ/s1700-e365/aws.jpg)

A high-severity flaw in Amazon Q Developer let a malicious repository run commands and steal a developer's cloud credentials. The path was short: a developer opens the repo, trusts the workspace, and Amazon Q does the rest. Amazon has patched it.

Tracked as [CVE-2026-12957](https://www.cve.org/cverecord?id=CVE-2026-12957) (CVSS 8.5), the bug sat in how Amazon's AI coding assistant handled Model Context Protocol (MCP) servers.

Wiz Research, which found and reported it, showed that a single config file dropped in a repo was enough to go from git clone to cloud compromise.

## How the attack worked

Amazon Q read an MCP configuration file, .amazonq/mcp.json, from the open workspace and launched the servers it defined. MCP servers are local processes that an AI assistant can spawn to reach databases, APIs, or build tools, so starting one means running commands on the machine.

Those processes inherited the developer's full environment. That usually means AWS keys, cloud CLI tokens, API secrets, and SSH agent sockets.

[![Cybersecurity](data:image/png;base64...)](https://thehackernews.uk/ai-cant-stop-d)

Put the two together, and a file sitting in a cloned repo could run arbitrary code with the developer's live cloud session attached. No password, no second sign-in.

In its [proof of concept](https://www.wiz.io/blog/amazon-q-vulnerability), Wiz had the file run aws sts get-caller-identity and ship the output to an attacker server, capturing the active AWS session. What comes next depends on that developer's cloud permissions: backdoor an IAM user for persistence, reach internal services, or pivot toward production.

AWS and Wiz frame the consent step differently. Amazon's [advisory](https://github.com/aws/language-servers/security/advisories/GHSA-xhcr-j4j9-3gh7) says the user has to trust the workspace when prompted, and CVSS rates the user interaction as passive.

Wiz reported there was no separate consent step for the MCP servers themselves before the fix. The patch closes that gap: Amazon Q now flags an untrusted MCP server and lets the developer reject the command before it runs.

[![](data:image/png;base64...)](https://blogger.googleusercontent.com/img/b/R29vZ2xl/AVvXsEhBR5pSG5vKSBtSvN42E5EaEPyhpTI9KIv9dfCuKhNCLSr9GHVVx8recSRWP2uHl4UQgQ3kBhV6s4RJXd3aRLTBWT6lKar6YXKB_5EIX9DIIIlEcDqay6cxULYuCER-Frbth-w8OmCHjNs0HAGKxfwhFGtrFDQyMIvt6f5_RbPmTruqO3LYbMvg3bqSntM/s1700-e365/poc.jpg)

The flaw lives in [Language Servers for AWS](https://github.com/aws/language-servers), the runtime that powers Amazon Q across VS Code, JetBrains, Eclipse, and Visual Studio. All four plugins bundle it, so all four were exposed by versions that shipped an older copy.

## What to do

Update. CVE-2026-12957 is fixed in Language Servers for AWS 1.65.0, but AWS's [bulletin](https://aws.amazon.com/security/security-bulletins/2026-047-aws/) tells customers to move to 1.69.0.

That build also closes a second issue, [CVE-2026-12958](https://www.cve.org/cverecord?id=CVE-2026-12958), a missing symlink check that could allow arbitrary file writes outside the workspace trust boundary.

The patched plugin minimums:

* VS Code: 2.20 or later
* JetBrains: 4.3 or later
* Eclipse: 2.7.4 or later
* Visual Studio toolkit: 1.94.0.0 or later

The language server auto-updates unless the network blocks it, and reloading the IDE pulls the latest build.

[![Cybersecurity](data:image/png;base64...)](https://thehackernews.uk/vpn-threat-report-m)

There is no known public exploitation; CISA's ADP entry for CVE-2026-12957 lists it as none. Wiz found the flaw through research and disclosed it in coordination with Amazon, reporting it on April 20 and seeing a fix on May 12, ahead of the June 26 public write-up.

## A pattern, not a one-off

Amazon Q is not the first coding assistant to trip over MCP trust. The bugs are not identical, but they rhyme: project configuration turns into executable behavior, and the trust checks around that handoff keep failing.

[Claude Code](https://thehackernews.com/2026/02/claude-code-flaws-allow-remote-code.html) (CVE-2025-59536) and [Cursor](https://thehackernews.com/2025/08/cursor-ai-code-editor-vulnerability.html) (CVE-2025-54136) both had project-level MCP config that led to command execution. [Windsurf](https://www.ox.security/blog/mcp-supply-chain-advisory-rce-vulnerabilities-across-the-ai-ecosystem/) (CVE-2026-30615) reached the same end by a different path, with attacker-controlled content rewriting the local MCP config to register a malicious server.

The convenience of letting a project folder configure an AI agent is also the attack surface. Repo-carried config is untrusted input. Turning it into a running process should take an explicit yes.

Found this article interesting? Follow us on [Google News](https://news.google.com/publications/CAAqLQgKIidDQklTRndnTWFoTUtFWFJvWldoaFkydGxjbTVsZDNNdVkyOXRLQUFQAQ), [Twitter](https://twitter.com/thehackersnews) and [LinkedIn](https://www.linkedin.com/company/thehackernews/) to read more exclusive content we post.

SHARE
[**](#link_share)
[**](#link_share)
[**](#link_share)
**

[**Tweet](#link_share)

[**Share](#link_share)

[**Share](#link_share)

**Share

**
[**Share on Facebook](#link_share)
[**Share on Twitter](#link_share)
[**Share on Linkedin](#link_share)
[**Share on Reddit](#link_share)
[**Share on Hacker News](#link_share)
[**Share on Email](#link_share)
[**Share on WhatsApp](#link_share)
[![Facebook Messenger](data:image/png;base64...)Share on Fa...