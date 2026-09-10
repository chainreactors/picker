---
title: DeepSeek Harness Flaw Let AI Agents Disable Their Own File Sandbox Without Approval
url: https://thehackernews.com/2026/09/deepseek-harness-flaw-let-ai-agents.html
source: The Hacker News
date: 2026-09-09
fetch_date: 2026-09-10T06:52:41.117026
---

# DeepSeek Harness Flaw Let AI Agents Disable Their Own File Sandbox Without Approval

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

[![cybersecurity](https://blogger.googleusercontent.com/img/b/R29vZ2xl/AVvXsEiHP9KRFkaxKFUKQNRU3CkfxCyJLEuIfmo6ov7iWHHRBE1ShJKfXdPvozMZMVuvOJipQ8Qbap3UBmtjKvZh-xBqLeUartPWmRuQj2W8nqdCk2_XlYLXpj15R4Du2oJ1nNVPqIuR-TwbMyPQe4gxxCcMYvUMbFO_Nin2OdhyzkJvX8Sn83aEbM1C5sgaaCqI/s728-nu-rw-lo-l85-e365/wiz-sep-d.png)](https://thehackernews.uk/claude-security-guide-d)

# [DeepSeek Harness Flaw Let AI Agents Disable Their Own File Sandbox Without Approval](https://thehackernews.com/2026/09/deepseek-harness-flaw-let-ai-agents.html)

**Swati Khandelwal**Sep 09, 2026Vulnerability / Artificial Intelligence

[![](data:image/png;base64...)](https://blogger.googleusercontent.com/img/b/R29vZ2xl/AVvXsEi0fUTc6rz4ZeeaMmjDLOfb2qNhnJf_TdNHK3F3qbNCQLLJbaF-nbSw5YPdeSAwg1HjoGwfQJZaXBpwvEbasFDhQb5ZkUm158shateq7uubMyrlejW4SDZAAzNQGUYkYdsxHupipxzRA7dQwTwTt9ArVJgU-wA5bGxIXduJj3CdyBF69Ixp6_qAU1LGzfI/s1700-nu-rw-lo-l85-e365/deepseek.jpg)

A flaw in **DeepSeek Harness**, DeepSeek's open-source tool for running AI coding agents on a developer's machine, let a sandboxed agent turn off its own sandbox with a single command.

The tool runs an agent's commands inside an operating-system sandbox, so that an agent working on untrusted files cannot write outside its workspace. The agent could remove that limit by calling the tool's own web interface on the same machine, and its commands would then run outside the sandbox without an approval prompt.

It worked on a default installation until DeepSeek fixed the tool on August 27, and it required attacker-supplied text that the agent read to prompt it to make the call.

The flaw is tracked as **CVE-2026-82533**. VulnCheck, which assigned the identifier, [published the record](https://www.vulncheck.com/advisories/deepseek-harness-alpha-1-authentication-bypass-via-host-header-spoofing) on September 8 and rated the flaw 9.4 out of 10.

[OX Research](https://www.ox.security/blog/cve-2026-82533-deepseek-harness-ai-agent-sandbox-escape/), the security firm that reported the flaw, said one shell command was enough. The command invoked the tool's local interface and set the agent's session to a mode called danger-full-access, which turns off the sandbox and stops approval prompts.

Ordinary commands did not need approval to begin with. Approval was applied only when a command requested broader access than the session already had, and this call did not request it. It changed the session's setting instead.

[![Cybersecurity](data:image/png;base64...)](https://thehackernews.uk/trust-world-update-d)

OX said it checked that the sandbox had been working before the escape. It ran two sessions from the same default settings and gave both the same command. The session that had made the call wrote to a folder outside its workspace, and the other was blocked.

The sandbox only covers files. The [command-line reference for the affected release](https://github.com/deepseek-ai/deepseek-harness/blob/dsh-v0.1.1-rc.2/apps/cli/reference/README.md) says that under the default setting, writes stay inside the workspace and temporary folders, while "reads and network access are not confined."

[![](data:image/png;base64...)](https://blogger.googleusercontent.com/img/b/R29vZ2xl/AVvXsEgTpHKxwk9o-blyw-Rj7j10xjHFV6AvZ_C1sZdXmYrt6fD4E4vqR6Z-ylwg7RvNCvEhMLj26gJtnrgvBgubAiF-J1Jzmp9ZpvAxgbRMliKJQOv48hYmuX49R-GE4cFJEYoXf6Necqz1FbZV6W5JWzpPMMdGAaYSiNxtTWxJcr-dN9F5BTPEoJs5FoOxXVo/s1700-nu-rw-lo-l85-e365/spoof.png)

That left the tool's own interface reachable from inside the sandbox. The tool also provides the agent's shell with the address of that interface and the current session's identifier, so the agent does not have to look for them.

The interface had no authentication. In the affected release, the [check that determined whether a request could reach it](https://github.com/deepseek-ai/deepseek-harness/blob/dsh-v0.1.1-rc.2/packages/client/connection/src/api-request-trust.ts) read the request's Host header and never looked at where the connection originated. A comment in that file says the check "is not an auth layer."

That check is what the CVE record describes. Because it trusted a header the client supplies, a machine outside could claim to be local and drive the agent. The tool's command line refused to listen on all network interfaces, so reaching it from outside needed the user to have forwarded or proxied the port through a tunnel, an SSH forward, or an editor.

[![](data:image/png;base64...)](https://blogger.googleusercontent.com/img/b/R29vZ2xl/AVvXsEhx3oX3EjqmebsqPzdTT2KvX-1jA7hEOU1IfVOTCywh8JEusjBGmTpb0PsU-PqzY9icMG4XGKTe1n93EveDOW3HtPN9QcWOoNyw_8hyphenhyphenXFeeQYx90qQj68N5Epxq2HgY1z2FvYpTTGVXLxknsvs0XqZCCnz_tENyrW0cLgQaQLV0F3FAjLswQ9qOQYpHYes/s1700-nu-rw-lo-l85-e365/log.png)

The same interface served a request to download a session's entire log. VulnCheck's advisory states that a caller who reaches the interface could retrieve all stored conversations without a key.

### Affected Versions and What to Install

Versions 0.1.1-rc.2 and earlier are affected. The record names 0.1.2-alpha.1 as the fixed version, but that version was never published to the npm registry, which is where the project's own instructions send users.

| Version | Status | Released |
| --- | --- | --- |
| 0.1.1-rc.2 and earlier | Affected | 0.1.1-rc.2 published August 21 |
| 0.1.2-alpha.1 | Fixed, on GitHub only | August 27, not on npm |
| 0.1.2-alpha.2 | First fixed release on npm | August 30 |
| 0.1.2-rc.1 | Current npm release, carries the fix | September 3 |

The Hacker News checked [the npm registry](https://registry.npmjs.org/%40deepseek-ai/dsh) on September 9 and found that the first published release with the authentication change is 0.1.2-alpha.2, three days after the fix was pushed to GitHub.

1. Install 0.1.2-alpha.2 or later. The registry's current release is 0.1.2-rc.1.
2. If you installed through a third-party desktop app, check which version of the harness it ships.
3. If you cannot upgrade, stop the web interface when you are not using it, and remove any tunnel, proxy, or port forward that reaches it.

No source reviewed for this article offers a way to stop the escape from inside the sandbox on a default local installation while the tool is running. The August 13 report says limiting the address the tool listens on does not help, because the agent is already on the s...