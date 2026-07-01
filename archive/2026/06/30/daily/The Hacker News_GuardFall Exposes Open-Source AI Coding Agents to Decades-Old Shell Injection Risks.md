---
title: GuardFall Exposes Open-Source AI Coding Agents to Decades-Old Shell Injection Risks
url: https://thehackernews.com/2026/06/guardfall-exposes-open-source-ai-coding.html
source: The Hacker News
date: 2026-06-30
fetch_date: 2026-07-01T06:24:40.634802
---

# GuardFall Exposes Open-Source AI Coding Agents to Decades-Old Shell Injection Risks

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

# [GuardFall Exposes Open-Source AI Coding Agents to Decades-Old Shell Injection Risks](https://thehackernews.com/2026/06/guardfall-exposes-open-source-ai-coding.html)

**Swati Khandelwal**Jun 30, 2026AI Security / Software Supply Chain

[![](data:image/png;base64...)](https://blogger.googleusercontent.com/img/b/R29vZ2xl/AVvXsEgR59EidY6iMYv3s9bikjIxpj6_YTaUIesrZ3MyD9OqUbOk262aDW7bCArqr-IjT9CUQUSzE2F_knKKvs4bIJ2d9cuzZ-DKlmkW_Q3SO43HkA79kSVhCELVyKaStWliNZc9l1xxEGEFE5UmT1Abn6XMKTjk-rxBRTTtRAjb-jYDRKj-ODtIYy8dGQvbzDE/s1700-e365/shell-ai.jpg)

The safety check that is supposed to stop an AI coding agent from running a dangerous command can be walked straight past using a shell trick that has been public for decades.

New research from [Adversa AI](https://adversa.ai/blog/opensource-ai-coding-agents-shell-injection-vulnerability/), which is named the bypass **GuardFall**, found it works against ten of the eleven popular open-source coding and computer-use agents the firm tested. Only one, "Continue," was built to defend against it.

Why does it matter? These agents run shell commands with your full account access. Point one at a booby-trapped repository or software package, and a hidden instruction can quietly run a command that wipes files or steals the secrets your account can reach, from SSH keys and cloud credentials to anything sitting in your home folder.

## How does it get past the guard?

Most of these agents try to stay safe by checking each command against a blocklist of dangerous patterns before running it. The flaw is that they check the command as plain text, while bash rewrites that text before it actually runs. The shell strips quotes and expands shortcuts, so the filter and the shell end up looking at two different things.

The simplest example: a filter watching for**rm** sees nothing wrong with r''m, because to a text matcher those are different strings. Bash removes the empty quotes and runs rm anyway.

[![Cybersecurity](data:image/png;base64...)](https://thehackernews.uk/ai-cant-stop-d)

The same idea works in other forms: a command hidden in base64 and piped into a shell, or ordinary tools like find and dd turned destructive with the right flag.

The researchers call this not a bug but "a dangerous convention and a class of problems," which is why adding more blocklist patterns fixes none of it. There is no single CVE to track or patch.

Two things have to line up for an attack to land, and neither is exotic.

* First, the AI has to produce the malicious command. A blunt "run rm -rf" is usually refused, but the same command tucked inside normal-looking work, such as a build file or a tool's "documentation" reply, gets emitted as a routine step.
* Second, the agent has to be running on its own, with an auto-execute flag turned on or its container sandbox switched off, both of which are routine in automated pipelines. The live tests used Claude Sonnet 4.6.

The other ten tools all left the gap open: opencode, Goose, Cline, Roo-Code, Aider, Plandex, Open Interpreter, OpenHands, SWE-agent, and the Hermes project, where the bug first surfaced and is [documented in Hermes's own issue tracker](https://github.com/NousResearch/hermes-agent/issues/36846).

[![](data:image/png;base64...)](https://blogger.googleusercontent.com/img/b/R29vZ2xl/AVvXsEgxKbwe1AcFw6GjaTYiNBur5CuuqXoMqeg7cn43vkCXZSvSRuohyeNi0pPxtBemtRq-RkAIOp4sh7XcodvHTRVrIb6_y7unb7Ru1Y1GohyK9vtbilZdTwlPUJCLh235Yf0yOXhMhIi0dwOgeLdicWYLnEujWiMBFfLS1Bdsh9QWiOBbrQdK7J5MqYoMToQ/s1700-e365/coding-agent.png)

The tools in Adversa's survey together carried roughly 548,000 GitHub stars as of May 2026. Adversa demonstrated the full attack end-to-end against the production Plandex binary, and the same shape worked against eight others. It describes the work as lab research; no public exploitation has been reported.

Continue, the one agent that held up, defends by reading the command the way bash will before deciding: it breaks the command into the same pieces the shell would, checks what actually runs, and keeps a hard list of destructive commands that are blocked outright.

[![Cybersecurity](data:image/png;base64...)](https://thehackernews.uk/vpn-threat-report-m)

That protection held against every payload in Continue's default editor mode. Its command-line auto-run mode is weaker: a few payloads slipped through, though the most destructive ones still hit the hard block. Adversa calls the design portable and says re-implementing it is roughly a two-day job for an experienced engineer.

## What to do now

None of the quick fixes is a complete answer, but they cut your exposure until a proper guard is in place:

* Run agents with $HOME pointed at a throwaway folder, so secrets like ~/.ssh and ~/.aws are out of reach.
* Turn off auto-execute flags such as --auto-exec, --auto-run, --auto-test, and dangerously-skip-permissions unless the job genuinely cannot pause for a human.
* Do not let agents run on pull requests from forks, the easy path from an attacker's file to your secrets.
* Treat config files shipped inside a repository, like .aider.conf.yml, as untrusted code; a malicious one can trigger the attack on the first accepted edit.

GuardFall lands in the middle of a run of similar findings this year. Adversa's own [TrustFall](https://adversa.ai/blog/trustfall-coding-agent-security-flaw-rce-claude-cursor-gemini-cli-copilot/) hit Claude Code, Cursor, Gemini CLI, and Copilot CLI, and a separate [deny-rule bypass](https://adversa.ai/blog/claude-code-security-bypass-deny-rules-disabled/) hit Claude Code.

Attacks like [AutoJack](https://thehackernews.com/2026/06/autojack-attack-lets-one-web-page.html) and [Agentjacking](https://thehackernews.com/2026/06/agentjacking-attack-tricks-ai-coding.html) turned poisoned content into commands that an agent runs with its owner's privileges. The common thread is simple: untrusted text keeps reaching a real shell before the guard understands what bash will actually run.

Found this article interesting? Follow us ...