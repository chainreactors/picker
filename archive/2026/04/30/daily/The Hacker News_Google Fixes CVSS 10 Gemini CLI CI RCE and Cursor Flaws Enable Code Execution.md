---
title: Google Fixes CVSS 10 Gemini CLI CI RCE and Cursor Flaws Enable Code Execution
url: https://thehackernews.com/2026/04/google-fixes-cvss-10-gemini-cli-ci-rce.html
source: The Hacker News
date: 2026-04-30
fetch_date: 2026-05-01T05:40:14.734160
---

# Google Fixes CVSS 10 Gemini CLI CI RCE and Cursor Flaws Enable Code Execution

#1 Trusted Cybersecurity News Platform

Followed by 5.40+ million[**](https://twitter.com/thehackersnews)
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

# [Google Fixes CVSS 10 Gemini CLI CI RCE and Cursor Flaws Enable Code Execution](https://thehackernews.com/2026/04/google-fixes-cvss-10-gemini-cli-ci-rce.html)

**Ravie Lakshmanan**Apr 30, 2026AI Security / Vulnerability

[![](data:image/png;base64...)](https://blogger.googleusercontent.com/img/b/R29vZ2xl/AVvXsEhoqSVEXaseT8C79cbC1Wjec2TiF4nMK72XiCPL3WBxqwNy9iUk5CSEqSXgwJFRug0zXq5foMAXzMYCSIP0nEnr-CxCeYFgjmVcOfPtK4nocQaGDzIFecL9SScOScUhVAgGkff6wO5ks-sqWA_KCEZnfrQhfViSGai-g0MOd2IHOYX_N03JvwIipkQ1gso7/s1700-e365/gemini-cursor.jpg)

Google has addressed a maximum severity security flaw in Gemini CLI -- the "@google/gemini-cli" npm package and the "google-github-actions/run-gemini-cli" GitHub Actions workflow -- that could have allowed attackers to execute arbitrary commands on host systems.

"The vulnerability allowed an unprivileged external attacker to force their own malicious content to load as Gemini configuration," Novee Security [said](https://novee.security/blog/google-gemini-cli-rce-vulnerability-cvss-10-critical-security-advisory/) in a Wednesday report. "This triggered command execution directly on the host system, bypassing security before the agent’s sandbox even initialized."

The shortcoming, which does not have a CVE identifier, carries a CVSS score of 10.0. It affects the following versions -

* @google/gemini-cli < 0.39.1
* @google/gemini-cli < 0.40.0-preview.3
* google-github-actions/run-gemini-cli < 0.1.22

In its advisory [published](https://github.com/google-github-actions/run-gemini-cli/security/advisories/GHSA-wpqr-6v78-jr5g) last week, Google said the impact is limited to workflows using Gemini CLI in headless mode, adding that any use of the tool in headless mode without folder trust will require manual review to configure this trust mechanism.

"In previous versions, Gemini CLI running in CI environments (headless mode) automatically trusted workspace folders for the purpose of loading configuration and environment variables," it said.

[![Cybersecurity](data:image/png;base64...)](https://thehackernews.uk/ai-blindspot-d-2)

"This is potentially risky in situations where Gemini CLI runs on untrusted folders in headless mode (e.g., CI workflows that review user-submitted pull requests). If used with untrusted directory contents, this could lead to remote code execution via malicious environment variables in the local .gemini/ directory."

This automatic trust of the current workspace folder meant that the tool could load any agent configuration it found without review, sandboxing, or explicit user consent. An attacker could weaponize this behavior by planting a specially crafted configuration that could pave the way for code execution on the host running the agent, effectively turning CI/CD pipelines into supply-chain attack paths.

The update addresses the problem by requiring folders to be explicitly trusted before configuration files can be accessed. To that end, users are being urged to review their workflows and adopt one of two approaches -

* If the workflow runs on trusted inputs (e.g., reviewing pull requests from trusted collaborators), set GEMINI\_TRUST\_WORKSPACE: 'true' in the workflow.
* If the workflow runs on untrusted inputs, review Google's guidance in [google-github-actions/run-gemini-cli](https://github.com/google-github-actions/run-gemini-cli) to harden the workflow against malicious content, and set the environment variable.

The tech giant also noted that it's taking steps to harden tool allowlisting when Gemini CLI is configured to run in --yolo mode to prevent scenarios where untrusted inputs (e.g., user-submitted GitHub issues) could lead to remote code execution via prompt injection by taking advantage of the fact that the auto-approve mode would ignore any allowlist in "~/.gemini/settings.json" and run all tool calls automatically (including "run\_shell\_command") without requiring user confirmation.

"In version 0.39.1, the Gemini CLI policy engine now evaluates tool allowlisting under --yolo mode, which is useful for CI workflows that allowlist a few safe commands to run when processing untrusted inputs," Google said. "As a result, some workflows that previously depended on this behavior may fail silently unless tool allowlists are modified to fit the task."

### Cursor Bug Leads to Code Execution

The disclosure comes as Novee Security also highlighted a high-severity vulnerability in the AI-powered development tool Cursor prior to version 2.5 (CVE-2026-26268, CVSS score: 8.1) that could also lead to arbitrary code execution by means of a prompt injection.

Cursor, in an alert [released](https://github.com/cursor/cursor/security/advisories/GHSA-8pcm-8jpx-hv8r) in February 2026, described it as a case of sandbox escape through .git configurations, allowing a rogue agent to set up a bare repository (".git") with a malicious [Git hook](https://git-scm.com/book/en/v2/Customizing-Git-Git-Hooks) that's automatically fired every time a commit operation runs within the embedded repository context without requiring any user interaction.

[![](data:image/png;base64...)](https://blogger.googleusercontent.com/img/b/R29vZ2xl/AVvXsEj6SWKCafnqKb9rAciWnARSFip7IUWZZCnyHCWBJXtLm0CGvMzfGcOdzt_Z1fhJx8xaGr2CRaXP8b5MPaQiVLbLHEqwkVjaQvIr9mX04p5MC3R_evFjnRy9cQKWY22PfIM_oNkajUWox1FrypuNGORAxVNWgnvCZ8XY5gaptTpyWXu1L-g5y9bd1L-KwVb8/s1700-e365/Cursor.png)

The end result is auto-approved arbitrary code execution on the victim's machine through the following sequence of actions -

* User clones a public GitHub repository with the embedded bare repository containing a malicious post-checkout hook
* User opens the repository in CursorIDE
* Users ask an innocuous prompt to "explain the codebase"
* Cursor agent parses the [AGENTS.md](https://agents.md/) that instructs it to navigate to the bare repository and performs a "git checkout" of the master branch
* The post-checkout hook inside the bare repository is triggered, leading to code execution.

"The root cause is not a flaw in Cursor's core product logic, but rather a consequence of a feature interaction in Git, one that becomes exploitable the moment an AI agent starts autonomously executing Git operations inside a repository it doesn't control," security researcher Assaf Levkovich [said](https://novee.security/blog/cursor-ide-cve-2026-2626...