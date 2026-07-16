---
title: Cursor Flaw Lets Malicious Cloned Repositories Trigger Windows Code Execution
url: https://thehackernews.com/2026/07/cursor-flaw-lets-malicious-cloned.html
source: The Hacker News
date: 2026-07-15
fetch_date: 2026-07-16T04:59:00.037797
---

# Cursor Flaw Lets Malicious Cloned Repositories Trigger Windows Code Execution

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

# [Cursor Flaw Lets Malicious Cloned Repositories Trigger Windows Code Execution](https://thehackernews.com/2026/07/cursor-flaw-lets-malicious-cloned.html)

**Swati Khandelwal**Jul 15, 2026Endpoint Security / Vulnerability

[![](data:image/png;base64...)](https://blogger.googleusercontent.com/img/b/R29vZ2xl/AVvXsEjyFnrtjbcXdDBTEYOhVnUpFO4CSqhCGj5xdvaYlhih4oUCd3phzBQTjjMogZeFDlYqTiO8Xt2jaHevba5peaV76dT417Vq9W-DZFSpu2_cEbAMtGwz-mqKZJcYgAAXmZT_Rnkdc0f3jAW-eANKWd6XZZJvYfYCt6l5Pp-2ZKjlnn4zG7G6gS7ivWruzeU/s1700-e365/git.png)

Open a repository in Cursor on Windows and, if a file named git.exe is sitting in the project root, Cursor runs it. No click, no approval dialog, no warning that anything in the folder is about to execute.

Whatever that binary does, it does as you, with your source, your SSH keys and your cloud tokens. Cursor keeps re-running it for as long as the project stays open.

No prompt injection, no agent, no model in the loop, and no prior access to the machine: opening the folder is the entire exploit, and the result is arbitrary code execution as the logged-in user.

AI security firm Mindgard reported the flaw to Cursor on December 15, 2025 and [published full technical details](https://mindgard.ai/blog/cursor-0day-when-full-disclosure-becomes-the-only-protection-left) on Tuesday, seven months later. There is still no patch, and Cursor has published no advisory for the issue.

The mechanism takes about a sentence. Cursor checks several locations for a Git binary when a project loads, and one of them is the workspace itself. Process Monitor output in the write-up shows Cursor.exe spawning the repo-root binary with the command line git rev-parse --show-toplevel.

That is the same repository-root probe [Microsoft's VS Code docs](https://code.visualstudio.com/docs/sourcecontrol/faq) describe. Whether Cursor searches those locations itself or hands Windows an unqualified git and lets the search order pick, the write-up does not say.

[![Cybersecurity](data:image/png;base64...)](https://thehackernews.uk/ai-vuln-protection-d)

Mindgard's proof of concept was Windows Calculator, renamed git.exe, and committed to the root. Clone, open, done. The screenshot shows Calculator windows stacking up on their own while the project sat open.

The precondition sounds like the hard part: an attacker's binary, sitting in your project root. It is not. Cloning a stranger's repository is how binaries land on disk in the first place, and developers and their agents do it all day. The attacker needs no foothold to begin with. That is the distance this bug covers: from a repository anyone can publish to code running as you.

One limit on the evidence. Mindgard's most recent dated confirmation is April 30, 2026, against Cursor 3.2.16, and the [current release is 3.11](https://cursor.com/changelog), shipped July 10. The write-up says the bug survives in the newest version it tested, but does not name that version.

[![](data:image/png;base64...)](https://blogger.googleusercontent.com/img/b/R29vZ2xl/AVvXsEit8-44KDroR8DtQFGVvYmz8TQuz68daEzh11dHUYHl90uHZzP4vO-TLamEc_nO8ZgkhY79HrVlfvOc4cv-vW2XpTzCrLs3XqpB6W5lNk-My0Vh4XCs21mbFU-3NXQwJyB-ioUP_USVuIlMMTa78DFsMuJ4S8W0sP4s0xhROM27GQzNi8xcUk_KnmPESgg/s1700-e365/calc.jpg)

The Hacker News reviewed all 33 security advisories [Cursor has published](https://github.com/cursor/cursor/security/advisories) and found no entry covering the issue, as of July 15. No CVE has been assigned. We asked Cursor to name any release that fixes it, and Mindgard, which version it last tested. This story will be updated with any response.

## What to Do

There is no patch, so every option below is a workaround. On managed Windows fleets, Mindgard suggests AppLocker or Windows App Control deny rules that block the executable by name and path under workspace roots, along the lines of %USERPROFILE%\source\repos\\*\filename.exe.

Path rules, not hashes; attacker binaries vary by hash. Windows has no general built-in rule that blocks a child process only when a specific parent launches it, the firm notes, so parent-aware enforcement generally means EDR. Everyone else: open untrusted repositories in a disposable VM or Windows Sandbox.

Pair it with [Cymulate's advice](https://cymulate.com/blog/zero-click-rce-prompt-injection-ai-tools/) to check a cloned repo or extracted archive before you open it. git.exe, npx.exe, node.exe, and where.exe have no business in a project root. What happened to the report is the rest of the story.

Cursor's [security page](https://cursor.com/security) says the company acknowledges "vulnerability reports within 5 business days." Mindgard's first substantive reply came a month after the December report, from Cursor's CISO, who explained that an automation had failed to invite the firm to the private HackerOne program.

The resubmitted report was closed the next day as informative and out of scope, then reopened once Mindgard pushed back, and HackerOne reproduced it. HackerOne confirmed delivery on January 20. After that: update requests in February, March and April, and nothing back.

Cursor's advisory record, read against Mindgard's timeline, shows the process working for other researchers while Mindgard's report sat. On February 13, 2026, Cursor published [GHSA-8pcm-8jpx-hv8r](https://github.com/cursor/cursor/security/advisories/GHSA-8pcm-8jpx-hv8r), a Git-hook sandbox escape ([CVE-2026-26268](https://thehackernews.com/2026/04/google-fixes-cvss-10-gemini-cli-ci-rce.html)) [reported by Novee](https://novee.security/blog/cursor-ide-cve-2026-26268-git-hook-arbitrary-code-execution/) under coordinated disclosure and fixed in Cursor 2.5. Three days later, on February 16, Mindgard asked for an update on its own Git-related report. No reply. Two more Cursor advisories went out on July 14, the day the full disclosure landed.

"Full disclosure is the nuclear option of vulnerability disclosure," Mindgard wrote, reserving it for cases where every other path has failed. The author, [...