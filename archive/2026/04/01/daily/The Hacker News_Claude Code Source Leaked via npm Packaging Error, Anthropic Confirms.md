---
title: Claude Code Source Leaked via npm Packaging Error, Anthropic Confirms
url: https://thehackernews.com/2026/04/claude-code-tleaked-via-npm-packaging.html
source: The Hacker News
date: 2026-04-01
fetch_date: 2026-04-02T04:31:36.619383
---

# Claude Code Source Leaked via npm Packaging Error, Anthropic Confirms

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

[![Security Service Edge](https://blogger.googleusercontent.com/img/b/R29vZ2xl/AVvXsEgWajeG0cdaapf1GKTZRUZUB7BzuYGegyw5k0eAorJXlmkFdYCCeLXXhXYJuXU9lWD33rV6rRnIyly3czoNfYifpxk1eGA5slItPmim3HkubXoQMgC4J7hdQPywxGbWq7Eqeff_o6s2Fq-WmSFd5guwdLn7IqpveMqULqtVnd-ndnljWYGj45EkMFB7m0qm/s728-e100/z-d.jpg)](https://thehackernews.uk/zscaler-threatlabz-d)

# [Claude Code Source Leaked via npm Packaging Error, Anthropic Confirms](https://thehackernews.com/2026/04/claude-code-tleaked-via-npm-packaging.html)

**Ravie Lakshmanan**Apr 01, 2026Data Breach / Artificial Intelligence

[![](data:image/png;base64...)](https://blogger.googleusercontent.com/img/b/R29vZ2xl/AVvXsEj39e4BXzk1M6BK7XEJcfogVbdwnYJjie08kNTAeW5T46Tn8UvbbaYGrrEpgw1Pa4IpJYeGe8AR7T_UCp4_vWYTcG-c5DY0HNlHW-8SbYkscVvjAKjKR3gHmlWAQONEx8kg_ANVfOr8OsQ7uTm-XWHW1PNfusxBj-Tn2kn-V2EedPykA3ESB66doPXxGzT8/s1700-e365/claude-code.jpg)

Anthropic on Tuesday confirmed that internal code for its popular artificial intelligence (AI) coding assistant, Claude Code, had been inadvertently released due to a human error.

"No sensitive customer data or credentials were involved or exposed," an Anthropic spokesperson [said](https://www.cnbc.com/2026/03/31/anthropic-leak-claude-code-internal-source.html) in a statement shared with CNBC News. "This was a release packaging issue caused by human error, not a security breach. We’re rolling out measures to prevent this from happening again."

The discovery came after the AI upstart released [version 2.1.88](https://www.npmjs.com/package/%40anthropic-ai/claude-code?activeTab=versions) of the Claude Code npm package, with users spotting that it contained a source map file that could be used to access Claude Code's source code – comprising nearly 2,000 TypeScript files and more than 512,000 lines of code. The version is no longer available for download from npm.

Security researcher Chaofan Shou was the first to [publicly flag](https://x.com/Fried_rice/status/2038894956459290963) it on X, stating "Claude code source code has been leaked via a map file in their npm registry!" The X post has since amassed more than 28.8 million views. The leaked codebase remains accessible via a [public GitHub repository](https://github.com/instructkr/claw-code), where it has surpassed 84,000 stars and 82,000 forks.

[![Cybersecurity](data:image/png;base64...)](https://thehackernews.uk/vpn-risk-report-inside-d)

A source code leak of this kind is significant, as it gives software developers and Anthropic's competitors a blueprint for how the popular coding tool works. Users who have [dug into the code](https://www.reddit.com/r/ClaudeAI/comments/1s8lkkm/i_dug_through_claude_codes_leaked_source_and/) have published details of its [self-healing memory architecture](https://x.com/himanshustwts/status/2038924027411222533) to overcome the model's [fixed context window constraints](https://x.com/troyhua/status/2039052328070734102), as well as other internal components.

These [include](https://dev.to/gabrielanhaia/claude-codes-entire-source-code-was-just-leaked-via-npm-source-maps-heres-whats-inside-cjo) a tools system to facilitate various capabilities like file read or bash execution, a query engine to handle LLM API calls and orchestration, multi-agent orchestration to spawn "sub-agents" or swarms to carry out complex tasks, and a bidirectional communication layer that connects IDE extensions to Claude Code CLI.

The leak has also shed light on a feature called [KAIROS](https://x.com/itsolelehmann/status/2039018963611627545) that allows Claude Code to operate as a persistent, background agent that can periodically fix errors or run tasks on its own without waiting for human input, and even send push notifications to users. Complementing this proactive mode is a [new "dream" mode](https://x.com/AlexFinn/status/2039005703160172723) that will allow Claude to constantly think in the background to develop ideas and iterate existing ones.

[![](data:image/png;base64...)](https://blogger.googleusercontent.com/img/b/R29vZ2xl/AVvXsEh-8BU5HpgGZ9cTYZqswMdEoMZgwYK7Py1unMSuXMJwaifmm5N1_1RhUB0P_CKOMnvaProx0uD3_6TZPVbtzVmBtxBsWOjqko6CLw9bnX2MjpHekHUraaKsxxWOgws8A0WUsGP8fmhPTSyQFI-q6Eq6n2nd3wFrTGMLjgrC5sV9iiYskYK8qk8JlyuzlH3z/s1700-e365/code.jpg)

Perhaps the most intriguing detail is the tool's Undercover Mode for making "stealth" contributions to open-source repositories. "You are operating UNDERCOVER in a PUBLIC/OPEN-SOURCE repository. Your commit messages, PR titles, and PR bodies MUST NOT contain ANY Anthropic-internal information. Do not blow your cover," reads the system prompt.

Another fascinating finding involves Anthropic's attempts to covertly fight [model distillation attacks](https://thehackernews.com/2026/02/anthropic-says-chinese-ai-firms-used-16.html). The system has [controls in place](https://x.com/nyk_builderz/status/2039004963943133589) that inject fake tool definitions into API requests to poison training data if competitors attempt to scrape Claude Code's outputs.

### Typosquat npm Packages Pushed to Registry

With Claude Code's internals now laid bare, the development risks providing bad actors with ammunition to bypass guardrails and trick the system into performing unintended actions, such as running malicious commands or exfiltrating data.

"Instead of brute-forcing jailbreaks and prompt injections, attackers can now study and fuzz exactly how data flows through Claude Code's four-stage context management pipeline and craft payloads designed to survive compaction, effectively persisting a backdoor across an arbitrarily long session," AI security company Straiker [said](https://www.straiker.ai/blog/claude-code-source-leak-with-great-agency-comes-great-responsibility).

The more pressing concern is the fallout from the [Axios supply chain attack](https://thehackernews.com/2026/03/axios-supply-chain-attack-pushes-cross.html), as users who installed or updated Claude Code via npm on March 31, 2026, between 00:21 and 03:29 UTC may have pulled with it a trojanized version of the HTTP client that contains a cross-platform remote access trojan. Users are advised to immediately downgrade to a safe version and rotate all secrets.

[![Cybersecurity](data:image/png;base64...)](https://thehackernews.uk/fast-response-not-fast-d)

What's more, attackers are already capitalizing...