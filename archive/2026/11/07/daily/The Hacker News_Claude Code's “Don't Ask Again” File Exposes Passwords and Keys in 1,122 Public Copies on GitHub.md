---
title: Claude Code's “Don't Ask Again” File Exposes Passwords and Keys in 1,122 Public Copies on GitHub
url: https://thehackernews.com/2026/11/claude-codes-dont-ask-again-file.html
source: The Hacker News
date: 2026-11-07
fetch_date: 2026-11-08T08:14:59.947881
---

# Claude Code's “Don't Ask Again” File Exposes Passwords and Keys in 1,122 Public Copies on GitHub

#1 Trusted Cybersecurity News Platform

Followed by 5.80+ million[**](https://twitter.com/thehackersnews)
[**](https://www.linkedin.com/company/thehackernews/)
[**](https://www.facebook.com/thehackernews)

[![The Hacker News Logo](data:image/png;base64...)](/)

**

**

[Get Updates](#email-outer)

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

[![cybersecurity](https://blogger.googleusercontent.com/img/b/R29vZ2xl/AVvXsEg98jBiF1GNyn9ReXVuuNzrDrJ8-mdCvE5IhR6dUbEnucAAvmCW-lbjZmzjJx0EhFV2R6xhfph0uQ-cz4IO46xmarphU8oOZmuqbdHxTeosFZTJ45LN6VEQOAdLCFB_iwlP3t9_i9qiQqQua1oJMGmp5wILrYvUWRBTMAVJphcDt7Qo0Yi5gK9pIHhW5pAb/s728-nu-rw-lo-l85-e365/wiz-d.png)](https://thehackernews.uk/appsec-ai-readiness-d)

# [Claude Code's “Don't Ask Again” File Exposes Passwords and Keys in 1,122 Public Copies on GitHub](https://thehackernews.com/2026/11/claude-codes-dont-ask-again-file.html)

**Swati Khandelwal**Nov 07, 2026Artificial Intelligence / Developer Security

[![](data:image/png;base64...)](https://blogger.googleusercontent.com/img/b/R29vZ2xl/AVvXsEhZH3vYLZb9lP7mDLqy2h-upzdComeWIfjDX5siFUO3FM2HlUs03OTwirA1R2uzOZq_clptIVBsoaJNXIuf8LlTbXHFvzBJLRl1l3mqGVesHjgdmD86S_c-k2JY_t56xZqI0bnN6jXRDr92KlMw6X5BHzm5hqogpWflsERi9zrsMHSS_abAcvZMcUGovd8/s1700-nu-rw-lo-l85-e365/claude-code.jpg)

Passwords and API keys that developers typed into commands they approved in Claude Code are sitting in public GitHub repositories, where anyone can read them.

When a user selects "**Yes, and don't ask again**," Anthropic's AI coding assistant can save the command, word-for-word, including the secret, in a project settings file.

Software security company Apiiro said yesterday that 1,122 public copies of that file hold at least one secret, though it did not test whether any still work. One company the researchers notified earlier this week confirmed its key had been live.

The file is .claude/settings.local.json. Removing it from a project does not undo the leak, because older versions stay in git history and in forks of the repository. The researchers' advice is to rotate first: change every password, token, and key the file has ever held, then clean up.

### How a Secret Lands in the File

By default, Claude Code asks before it runs most shell commands. If the user picks "Yes, and don't ask again," it saves an allow rule in .claude/settings.local.json inside the project, according to its [permissions documentation](https://code.claude.com/docs/en/permissions). Matching commands then run without asking in later sessions.

The rule covers only what the prompt offered. Sometimes that is a pattern, such as npm test \*, and sometimes one exact command. When it is the exact command, any password or token typed into it is saved too, in plain text.

In public files, the researchers found saved commands with the secret still inside, and they reproduced the behavior with the latest models, Opus 5.5 and Fable 5.1.

Claude Code tries to keep the file out of git. The first time it writes the file in a git repository, it adds the file to the user's global git excludes, its [settings documentation](https://code.claude.com/docs/en/settings) says. Git on that computer then ignores the file in every repository.

[![Cybersecurity](data:image/png;base64...)](https://thehackernews.uk/ai-governance-platform-d)

That protection stays in one user's git settings on one computer. It does nothing for a file that was already committed, the researchers say. Claude Code never adds the file to the project's own .gitignore, so the protection does not travel with the project.

In 539 of the 1,105 repositories the researchers traced, a commit listing Claude as a co-author changed the file. They take this to mean Claude often commits the file itself.

### What Apiiro Found

Apiiro's search of public GitHub found 104,185 copies of the file in 103,617 repositories, its [research write-up](https://apiiro.com/blog/coding-agents-leaking-secrets-github-dont-ask-again) shows. About 1.1% of them, or 1,122 copies, hold at least one secret. Together they hold 1,379 different secrets.

A value counted as a secret when it matched a known key format, or when a password or token sat beside the address of a public server. An AI reviewer also had to agree. The researchers do not say whether anyone has used these secrets.

More than a third of the secrets open a database directly, including 379 database passwords. Others include 43 SSH logins for public servers, 42 tokens for GitHub, GitLab and npm, and 23 AWS keys.

Among the owners of these files are 63 organizations, mostly software companies of all sizes. The strongest cases include a database vendor's own admin-level cloud key and the owner password of a medical-records database, the researchers say.

[![](data:image/png;base64...)](https://blogger.googleusercontent.com/img/b/R29vZ2xl/AVvXsEgQVOrBlt7EwCzNEBgEvGmZt6L9NtTw0cDMJzh46DkBbRQFYTW3STOiQVVoFAV4ubNrE0J5KNYuQfm85YxBFLANDlOvJnyC4dCpVj6e_RZB8GS5vOicQM6IVJ8UFv77vuMlXk-_YtyNBxuhzIkFFkyQzaOS_7Hbz5J8IJB55KqRBl_1rzBjBdqiKmfbnzw/s1700-nu-rw-lo-l85-e365/leaked.png)

As of Monday, every file with a secret was still on its repository's default branch, and in half of those repositories it had been there for at least 217 days.

Older versions of the file contain 734 more secrets across 509 repositories that are not present in any current copy, usually because the file was deleted. Forks spread the files further: 211 forks of 74 repositories carry the same secrets as the originals.

Secrets also sit in 298 of 76,011 copies of the shared .claude/settings.json file, which teams commit on purpose, mostly inside allow rules. Including those, the older versions, and saved agent chat logs, the total is 2,539 secrets across 1,994 repositories.

Of 16 coding agents whose documentation the researchers compared, Claude Code is the only one confirmed to save the full approved command in a project file by default.

### What to Do

For developers, the researchers recommend these steps:

1. Search your GitHub organization for .claude/settings.local.json and .claude/settings.json, and check each repository's git history for them, even where the files are gone.
2. Rotate every password, token and key the files have ever held, before cleaning up.
3. Stop tracking the local file with git rm --cached .claude/settings.local.json, and add it to the repository's own .gitignore.
4. Open the file on your own computer, even if it was never committed, and delete every rule that contains a secret.
5. Keep secrets out of commands. Refer to them as variables from a secrets manager, such as $DB\_URL, so the saved rule holds the variable name and not the secret.
6. Approve patterns, such as Bash(npm run:\*), instead o...