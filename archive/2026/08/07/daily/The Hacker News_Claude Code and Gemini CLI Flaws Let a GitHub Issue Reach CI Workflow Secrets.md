---
title: Claude Code and Gemini CLI Flaws Let a GitHub Issue Reach CI Workflow Secrets
url: https://thehackernews.com/2026/08/claude-code-and-gemini-cli-flaws-let.html
source: The Hacker News
date: 2026-08-07
fetch_date: 2026-08-08T03:25:01.976710
---

# Claude Code and Gemini CLI Flaws Let a GitHub Issue Reach CI Workflow Secrets

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

# [Claude Code and Gemini CLI Flaws Let a GitHub Issue Reach CI Workflow Secrets](https://thehackernews.com/2026/08/claude-code-and-gemini-cli-flaws-let.html)

**Swati Khandelwal**Aug 07, 2026Artificial Intelligence / Vulnerability

[![](data:image/png;base64...)](https://blogger.googleusercontent.com/img/b/R29vZ2xl/AVvXsEguukj-eRhx9RtAq9X96hAxHi0IU3ZWgM_W5XkdWhF8ezevuBQygkpv-ku5PSri9Gt5hRkNVxe6HmJJr5Mg33X_PhOGziqaho9bwm-mkRZSBl2jo94XF3jRwTZOb_PocueKWJkEtvl7kG_YqmbVfUxNht8_ODzLOERIqQteMdPxnWpobM-c9-fHhn0cLMQ/s1700-e365/claude-github.jpg)

A GitHub issue opened by an account with no repository privileges was enough to execute code on the CI runners behind Anthropic's and Google's own coding-agent repositories. On OpenAI's, it was enough to hijack the next agent run.

Novee Security ran the attack against each vendor's agent in the configuration that the vendor ships by default, and presented the work at Black Hat USA on August 5. Two CVEs came out of it. Both are patched.

Gemini CLI carries the worst of the two. **CVE-2026-12537** (CVSS 4 score: 10.0) is an OS command injection in the container launcher, reached through a crafted .gemini/.env file, which lets an unprivileged attacker run code on the host of a headless CI platform before the sandbox starts. It is fixed in Gemini CLI 0.39.1 and run-gemini-cli 0.1.22.

In Claude Code, **CVE-2026-54316** turned Hugging Face's public download counter into an exfiltration channel that leaked an API key one character at a time, and is fixed in 2.1.163. Every Claude Code release from 0.2.54 up to 2.1.163 is affected. Anthropic says exploitation required getting untrusted content into a Claude Code context.

[![Cybersecurity](data:image/png;base64...)](https://thehackernews.uk/threatlocker-d)

The Codex finding produced neither a product-version patch nor a CVE. Novee says OpenAI's position is that its sandbox behaved exactly as documented. Update Gemini CLI to 0.39.1, run-gemini-cli to 0.1.22, and Claude Code to 2.1.163, then audit any workflow an outside user can trigger.

The Gemini host-execution bug did not require talking a model into anything. Across all three, the recurring failure sat in the harness, the code around the model that decides what actually runs: one part marked a value safe, and a later part acted on that value with more authority.

"The harness is the code between the model and the real world," Novee founding engineer Elad Meged [wrote](https://novee.security/blog/critical-flaws-in-anthropic-google-and-openais-coding-agents/).

Novee found that [Claude Code](https://thehackernews.com/2026/06/claude-code-github-action-flaw-let-one.html)'s command validator strips single-quoted text before its 23 checks run, which is correct behavior for bash, so a payload in the value of git push --receive-pack, a flag git executes, reached the runner untouched. That chain has no CVE and no publicly stated fixed version.

[Gemini CLI](https://thehackernews.com/2026/04/google-fixes-cvss-10-gemini-cli-ci-rce.html) parsed its tool allowlist only when registering the tool; at runtime nothing enforced it, and under --yolo every command the model asked for was auto-approved. Google addressed both that and the container-launcher flaw in one [advisory](https://github.com/google-github-actions/run-gemini-cli/security/advisories/GHSA-wpqr-6v78-jr5g), which says the fix "affects all Gemini CLI GitHub Actions."

That advisory itself still shows no CVE; Google Cloud published the identifier separately as CNA, pointing back to it. [Anthropic](https://github.com/anthropics/claude-code/security/advisories/GHSA-fg94-h982-f3mm) rates the Claude Code flaw Moderate at CVSS v4 6.0, while [NVD](https://nvd.nist.gov/vuln/detail/CVE-2026-54316) assigned a CVSS v3.1 score of 9.1. NVD has not scored it under v4, so the two figures are not a like-for-like comparison.

The [Codex](https://thehackernews.com/2026/03/openai-patches-chatgpt-data.html) finding is the one with no version to install. Novee found that the openai/codex repository ran two Codex passes inside a single job sharing one checkout, so the first pass could write AGENTS.md, the file the second pass loads as its own instructions. Failing the JSON validation between the passes is what launched the second one.

[![Cybersecurity](data:image/png;base64...)](https://thehackernews.uk/corelight-d)

OpenAI's [current workflow](https://github.com/openai/codex/blob/main/.github/workflows/issue-deduplicator.yml) separates the passes into different jobs and runs Codex with drop-sudo and a read-only sandbox. OpenAI's [guidance](https://github.com/openai/codex-action/security) now lists repository instruction files among content that "should be considered part of the untrusted input surface," and recommends running Codex as the last step in a job, warning that it may otherwise leave files behind for privileged steps that follow.

Neither change shows that Codex itself now handles a writable instruction file differently; what the sources establish is a repository-level workflow fix and a documentation update.

CISA's entry on both the [Gemini](https://nvd.nist.gov/vuln/detail/CVE-2026-12537) and Claude Code CVE records lists exploitation as none, and The Hacker News confirmed on August 7 that neither appears in the agency's Known Exploited Vulnerabilities catalog. It also found a public GitHub repository describing itself as a reproduction lab for the Claude Code flaw, up since June 18. Nothing in the sources reviewed shows either chain used against a target.

The development comes as Pillar Security [reported](https://www.pillar.security/blog/chaindrop-when-opening-a-repository-becomes-execution) on August 4 that the operators of the [ChainDrop npm worm](https://thehackernews.com/2026/08/keyv-linked-npm-worm-poisons-hundreds.html) planted a Claude Code SessionStart hook and a VS Code folderOpen task in compromised repositories, firing when a developer opened the workspace rather than waiting for an install.

Found this article interesting? Follow us on [Google News](https://news.google.com/publications/CAAqLQgKIidDQklTRndnTWFoTUtFWFJvWldoaFkydGxjbTVsZDNNdVkyOXRLQUFQAQ), [Twitter](https://twitter.com/thehackersnews) and [LinkedIn](https://www.linkedin.com/company/thehackernews/) to read more exclusive content we post....