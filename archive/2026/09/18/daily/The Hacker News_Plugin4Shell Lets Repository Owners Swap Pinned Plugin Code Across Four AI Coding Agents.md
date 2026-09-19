---
title: Plugin4Shell Lets Repository Owners Swap Pinned Plugin Code Across Four AI Coding Agents
url: https://thehackernews.com/2026/09/plugin4shell-lets-repository-owners.html
source: The Hacker News
date: 2026-09-18
fetch_date: 2026-09-19T07:02:43.713660
---

# Plugin4Shell Lets Repository Owners Swap Pinned Plugin Code Across Four AI Coding Agents

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

# [Plugin4Shell Lets Repository Owners Swap Pinned Plugin Code Across Four AI Coding Agents](https://thehackernews.com/2026/09/plugin4shell-lets-repository-owners.html)

**Swati Khandelwal**Sep 18, 2026Vulnerability / Artificial Intelligence

[![](data:image/png;base64...)](https://blogger.googleusercontent.com/img/b/R29vZ2xl/AVvXsEizNK9maRYTbrRVwr9_9b7Sm_IizPdRJh0AbH1GtKU1BNPrcxJydnUdRQxRxauE5p1ejpfk4ihANpP7HAoXbRCDD1Pu-ZZD1dnfzLFjysOSJm7gGRKYrkUjxVF-tX-0neJMQtN87iyk1DRD70hKKtFU_J6idWK4aoZr3k4DAz4q8pkjTfKTX10Vttaiwag/s1700-nu-rw-lo-l85-e365/coding-agents.jpg)

A flaw in four widely used AI coding agents lets someone who controls a plugin's code repository swap the plugin an agent installs for a malicious one, even when the agent locked that plugin to a specific reviewed version, security firm [Air Security said on Thursday](https://www.air.security/blog-posts/plugin4shell).

The firm said Anthropic has patched the flaw in Claude Code 2.1.179 and OpenAI in Codex 0.146.0, that GitHub Copilot has no fix, and that Google will not patch the Gemini CLI, which it is retiring.

The agents install add-ons called plugins from online marketplaces. To stay safe, a marketplace locks each plugin to a single reviewed version by its commit hash, a long string that identifies an exact snapshot of the code. Air found that the agents fetch that snapshot but never check that the code they end up with actually matches it.

A branch is a named line of code in a repository. On a code host that lets someone create a branch whose name is made to look like the commit hash, the owner of a plugin's repository can point that name at different code. The agent then installs the different code while still reporting that it is on the locked version.

Because a plugin runs with the same access as the person using the agent, the swapped code can access that person's files, saved credentials, and the systems they can log in to, Air said.

The trick does not work everywhere. GitHub does not allow branch or tag names that look like commit hashes, [according to GitHub's documentation](https://docs.github.com/en/get-started/using-git/dealing-with-special-characters-in-branch-and-tag-names), so a plugin installed from a GitHub repository is not exposed to this branch trick. Air says the trick works on hosts that permit such names, such as Bitbucket or a company's own git server, which these agents also support.

[![Cybersecurity](data:image/png;base64...)](https://thehackernews.uk/trust-world-update-d)

The Hacker News checked the marketplaces the agents ship with on September 18 and found that every plugin in [Anthropic's community catalog](https://github.com/anthropics/claude-plugins-community), and in the default catalogs for Claude Code and Copilot, points to a GitHub repository.

The Gemini CLI is attacked a different way. Instead of a branch shaped like the hash, Air says its installer can be tricked by a repository whose main branch is named FETCH\_HEAD, and GitHub's rule against hash-shaped names does not clearly block that name. So it is not established that installing a Gemini CLI plugin from GitHub avoids the flaw, and the Gemini CLI is the agent Air says will not be fixed.

What would make the attack need no action from the victim is background auto-update, which lets an agent refresh installed plugins on its own, so a plugin someone already trusts can be replaced without a prompt. Air says this runs by default in Claude Code and Codex.

But auto-update is on by default only for the agents' own built-in marketplaces, which are hosted on GitHub, and is off or optional for outside ones, [according to Anthropic's](https://code.claude.com/docs/en/discover-plugins) and [GitHub's documentation](https://docs.github.com/en/copilot/reference/copilot-cli-reference/cli-plugin-reference). So a reader who installs plugins only from the agents' default, GitHub-based marketplaces is not exposed to the branch-name version of the attack, on Air's and GitHub's own account of how it works.

[![](data:image/png;base64...)](https://blogger.googleusercontent.com/img/b/R29vZ2xl/AVvXsEjTHkUHEQBOZ5KLCOI3V7hifzRGTR3R5sF-JY5_Si44Zpqo-hzs9-I_aHdGxQHXiuxnK3Wjt08hUySAiLCp8QSY-RFZW5nk7mDLOuLuHTpegsSGBqgO2EmGYtvxpnDJR6KvBSqrvdjTQWjzCBg6IYdHwnacNcdZ4k2pLbadqhbktPNqsWQmnwZyTLJe-cc/s1700-nu-rw-lo-l85-e365/plugin.jpg)

Air says it built a working test attack against all four agents in May and told the vendors in June. As of September 18, no CVE identifier had been assigned, and none of the four vendors had published a security advisory for the flaw, checks by The Hacker News found, and there is no sign it has been used in a real attack.

The Hacker News reproduced the underlying Git behavior in a local test, and OpenAI's [own public fix](https://github.com/openai/codex/pull/34644) describes the same bug: Git "can interpret a requested commit SHA as a branch name," the company wrote, which can make a plugin source "materialize a different commit than the one it pinned." That change shipped in Codex 0.146.0.

Because each agent checks the lock on the user's own machine, not at the marketplace, no marketplace can fix this for users — the fix has to ship in the agent itself. Where each agent stands:

| Agent | Status | What to do |
| --- | --- | --- |
| Anthropic Claude Code | Fixed, Air says, in [2.1.179](https://github.com/anthropics/claude-code/releases/tag/v2.1.179) | Update to 2.1.179 or later |
| OpenAI Codex | Fixed in [0.146.0](https://github.com/openai/codex/releases/tag/rust-v0.146.0) | Update to 0.146.0 or later |
| GitHub Copilot | No fix, Air says | No patch available |
| Google Gemini CLI | Will not be fixed, Air says | Move to Antigravity, Air and Google say |

The sources do not say whether updating an affected agent removes a plugin that was already swapped, or only stops future swaps.

Anthropic's release notes for 2.1.179 do not mention the fix, and the account that it is fixed in is Air's. For Copilot, Air says it told Microsoft ...