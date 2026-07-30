---
title: New Gitea RCE Lets Repository Writers Plant a Git Hook to Run Shell Commands
url: https://thehackernews.com/2026/07/new-gitea-rce-lets-repository-writers.html
source: The Hacker News
date: 2026-07-29
fetch_date: 2026-07-30T04:52:45.381478
---

# New Gitea RCE Lets Repository Writers Plant a Git Hook to Run Shell Commands

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

# [New Gitea RCE Lets Repository Writers Plant a Git Hook to Run Shell Commands](https://thehackernews.com/2026/07/new-gitea-rce-lets-repository-writers.html)

**Swati Khandelwal**Jul 29, 2026Vulnerability / DevOps

[![](data:image/png;base64...)](https://blogger.googleusercontent.com/img/b/R29vZ2xl/AVvXsEjm9I3aoAsUS5yCtKTvSX6LYxjKfJu-RShA1QmcUiBLu760VFfeqd6D4NfH3ttKHoQkfWT57oL0_4KJBovY7nshgiGQ4R5wimWh-2k48f9qjdlJtjKqK0oM5vxquJFPuguLbBkbqzA7xc4NgjQaxkcU7tVSQ0a3GyXreEyvdvR4NmERWPbkiR6Um2thKfY/s1700-e365/Gitea-rce.jpg)

Gitea, the self-hosted Git platform, has patched a critical remote code execution vulnerability. A user with ordinary repository write access can turn attacker-controlled patch content into a live Git hook and run shell commands as the Gitea service account.

Tracked as `CVE-2026-60004` (CVSS score: 9.8), the flaw affects Gitea versions 1.17 and later before 1.27.1 and is fixed in 1.27.1. The vulnerable API call requires authentication and repository write permission. But Gitea enables registration by default, so an outside visitor can create a normal account and repository on an unchanged installation, then exploit the bug without pre-existing credentials.

Upgrading to 1.27.1 is the fix. Gitea said on July 27 that Gitea Cloud instances would be upgraded automatically. Gitea's July 28 advisory does not say the flaw has been exploited in the wild, but it includes public proof-of-concept (PoC) code.

Disabling open registration can remove the public account-creation path while the update is deployed, but it does not fix the flaw or protect against existing users with repository write access.

[![Cybersecurity](data:image/png;base64...)](https://thehackernews.uk/ai-vuln-protection-d)

The flaw was reported by security researcher [Shai Rod, who goes by NightRang3r](https://x.com/NightRang3r/status/2082167303190241483). Gitea credits NightRang3r as the reporter in its advisory.

Gitea's [affected route](https://github.com/go-gitea/gitea/blob/v1.27.0/routers/api/v1/api.go#L1407) invokes `reqToken()`, which rejects requests without a signed-in user. The no-prior-credentials path comes from the project's [default configuration](https://docs.gitea.com/1.27/administration/config-cheat-sheet), which leaves registration open, requires neither email nor manual approval, does not mark new users as restricted, and imposes no default repository-creation limit.

The bug sits in the `POST /api/v1/repos/{owner}/{repo}/diffpatch` endpoint. According to Gitea's [security advisory](https://github.com/go-gitea/gitea/security/advisories/GHSA-rcr6-4jqh-j84m), the endpoint applies a supplied patch inside a shared bare temporary clone. Vulnerable builds invoke `git apply` with `--index`, `--recount`, `--cached`, and `--binary`, adding the `-3` three-way fallback option when the server runs Git 2.32 or later.

An attacker submits the same patch twice to create an add/add collision. The three-way fallback then checks the indexed path out even though the operation uses `--cached`. Because the temporary clone is bare, its root is `$GIT_DIR`. An executable file placed at `hooks/post-index-change` therefore lands in [Git's hook directory](https://thehackernews.com/2026/04/google-fixes-cvss-10-gemini-cli-ci-rce.html) and becomes active. Git runs it while updating the index.

[![](data:image/png;base64...)](https://blogger.googleusercontent.com/img/b/R29vZ2xl/AVvXsEiSY38SkVmSwWfzVCew9Uxq3fAbRzE3Wg-a6ULmInmDuYqnP2vTKCWgChKSyFLtCvynW_8i19LHXUYPZN1SiKAu1QLF7vOq1MOjaa9BpW7dSTlZWyYAcji4eljuTMPA1gq5QBDGDTvbOi-lF7KKnl28HRkQoaqMqkMP3HHP3ar87Ydn5efdZZem8_PWISw/s1700-e365/rce-lfi.jpg)

The PoC signs in with a normal account, creates an initialized private repository, sends the malicious patch twice, and retrieves the command output. It needs no outbound callback. The hook stores the output in Git objects, creates a branch containing the result, and lets the attacker fetch it over authenticated smart HTTP.

As of July 29, 2026, none of the cited primary sources reports whether the flaw was exploited before or after version 1.27.1 became available.

Successful exploitation gives the attacker the privileges of the Gitea operating-system account. Depending on how the instance is isolated, Gitea said that could expose application and environment secrets, mounted repositories, database credentials and contents, OAuth credentials, and reachable internal services.

[![Cybersecurity](https://blogger.googleusercontent.com/img/b/R29vZ2xl/AVvXsEhleDdO_4O9-8Pkmidym8Pi9yV4V4jI_M5U0iNRDuoW5Jz3pq7DskZI9OqIChqmY1soaW1ppsC8VLeO55vxSh1m5Q8MJ9ZHuEOSNO5q7K-LwrF6IxrRfCIJOFyoBGaLXGZpkSo8tDirSz-9LmmoOs31tQTlvJWBMLiWJKqMFFaiMmNLV3l-p8zXaFm1VmGG/s728-e100/sygnia-d-2.png)](https://thn.news/sygnia-webinar)

Exploitation still requires repository write access, Git 2.32 or later, an enabled `diffpatch` route, and a writable, executable temporary filesystem. Default registration lets an outsider obtain the required write access on an unchanged installation.

The fix is easy to miss in the changelog. Gitea changed the temporary clone from bare to non-bare. The [code comment](https://github.com/go-gitea/gitea/commit/470d34b1de87d901bd9135564d5ee18c0d339e82) explicitly warns that Git commands using `--index` may operate on the working tree. The change was merged and backported on July 26, 2026.

Version [1.27.1 shipped](https://github.com/go-gitea/gitea/releases/tag/v1.27.1) on July 27, and the security advisory followed on July 28. The release notes listed the change under MISC as "refactor: git patch apply," not under SECURITY.

Rod had [previewed the RCE alongside a separate file-inclusion issue](https://x.com/NightRang3r/status/2081053859581960519), with a PoC retrieving `/etc/passwd` from a Gitea 1.27.0 host. That issue appears to correspond to a separate [change included in 1.27.1](https://github.com/go-gitea/gitea/commit/3e6cb7c16b837e993f90dbe1ff06dd5726b74588) that altered Gitea's Org-mode renderer so `#+INCLUDE` paths are returned as plain text inst...