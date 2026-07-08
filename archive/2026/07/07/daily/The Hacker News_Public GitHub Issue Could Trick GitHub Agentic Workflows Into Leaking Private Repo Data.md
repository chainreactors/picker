---
title: Public GitHub Issue Could Trick GitHub Agentic Workflows Into Leaking Private Repo Data
url: https://thehackernews.com/2026/07/public-github-issue-could-trick-github.html
source: The Hacker News
date: 2026-07-07
fetch_date: 2026-07-08T05:05:52.816806
---

# Public GitHub Issue Could Trick GitHub Agentic Workflows Into Leaking Private Repo Data

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

# [Public GitHub Issue Could Trick GitHub Agentic Workflows Into Leaking Private Repo Data](https://thehackernews.com/2026/07/public-github-issue-could-trick-github.html)

**Swati Khandelwal**Jul 07, 2026Vulnerability / AI Security

[![](data:image/png;base64...)](https://blogger.googleusercontent.com/img/b/R29vZ2xl/AVvXsEj35Nf4KvfpGfbhGpq7fhtkXFhxKtTqAEFF5dX23th60tiUCMEYsuOXfiH-kIq1PRUWrRBMo92M6SCtE8chA882l0wCOO2gs1skw-h_sOqfA9jOcED6IYr2RVWkVzKohekZdvzOTZ9QpPnGDtOtJI9jYjWlPiAgvc1dG4Yuy-J02v8GA9rkweGIF000-lA/s1700-e365/githubs.jpg)

A public issue can trick **GitHub Agentic Workflows** into leaking the contents of an organization's private repositories, researchers at Noma Security have shown.

The attacker needs only to open a normal-looking issue on a public repository, with no stolen credentials and no access to the organization. If that organization has given the agent read access across its repositories, private ones included, the issue can steer it into pulling private contents into a public comment.

Noma calls the technique **GitLost**. The target is [GitHub Agentic Workflows](https://github.blog/changelog/2026-02-13-github-agentic-workflows-are-now-in-technical-preview/), a feature now in public preview that GitHub launched in February. Instead of writing automation scripts, you write instructions to an AI agent in plain English in a Markdown file. The agent reads issues and pull requests, runs tools, and replies on its own.

It can be powered by GitHub Copilot, Anthropic's Claude, Google Gemini, or OpenAI Codex. Workflows are read-only by default, but an organization can hand one a token with read access across its repositories to give it cross-repo context, private ones included.

That grant is the setup GitLost turns against it.

## How the trick works

The weakness is a well-known one: **indirect prompt injection**. An AI agent cannot reliably tell the difference between instructions from its owner and instructions hidden inside the content it happens to read. So if an attacker writes those instructions into an issue, the agent may simply follow them.

In Noma's [proof of concept](https://noma.security/blog/gitlost-how-we-tricked-githubs-ai-agent-into-leaking-private-repos/), the malicious issue was dressed up as a routine request from a VP of Sales after a customer meeting. The workflow it hit was set to wake up when an issue is assigned, read the issue, and reply with a comment. It also had read access to the organization's other repos.

[![Cybersecurity](data:image/png;base64...)](https://thehackernews.uk/ai-vuln-protection-d)

Once a routine automation assigned the issue, the agent pulled a private repository's README and pasted it into a public comment on the issue.

GitHub built guardrails to stop exactly this. In its own [documentation](https://github.github.com/gh-aw/), the company warns that "AI agents can be manipulated by prompt injection, malicious repository content, or compromised tools," and the product ships with sandboxing, read-only tokens by default, input cleaning, and a threat-detection step that scans an agent's proposed output before it posts.

[![](data:image/png;base64...)](https://blogger.googleusercontent.com/img/b/R29vZ2xl/AVvXsEiZBZsJJEib8evq4ebPX5DcFiW-5TalK0jDOnc0m9StHVkB2zLAm6A28agOIvrzABCi42Dc3LIPlhwEEoS3OHba-xgeA-KhDU_deVhBNsNnw01XRdT1LvAlyRnG2uA_qOQf7-sKjX5NjT6N2trLrc7iNE0aERNdQEaFtq0pg9_to7NSPro6tZLzgUy87eM/s1700-e365/action.png)

Noma reported that in its test, a one-word change was enough to slip past. Prefixing the malicious instruction with "**Additionally**" led the model to treat it as a follow-on task, not something to refuse, and the guardrail let it through.

## Why is this one different?

What sets GitLost apart is what the attacker gets to control. "Earlier prompt injection examples were largely about manipulating what an agent said," Sasi Levi, Security Research Lead at [Noma Security](https://noma.security/), told The Hacker News. "GitLost is about manipulating what an agent does with its permissions."

The agent here, he said, is not a chat window but a credentialed actor sitting inside an organization's CI/CD-adjacent infrastructure, with read access spanning repos the attacker cannot see. It touches no server, needs no stolen credentials, and does not require write access to anything private. The attacker only has to open a public issue.

[![](data:image/png;base64...)](https://blogger.googleusercontent.com/img/b/R29vZ2xl/AVvXsEgwFy4i4BevTIPawxyWkUOGbwakn3JMnX7B9skCY5PtqNDPMMUXMYIkY_EEHnGuUj1Gh3IQ2XyFXPcZ-v3Q2CknNHlJr2gIQiwoK_4lYnP58TmS4IvdiNfHikngoa2ONqzTxWzroCBqwrawD22dhUWMHz_0r8vPQR2Y77Q6l6e5B2yqSfKCUM6eHjhyCkY/s1700-e365/gitlost.gif)

The setup fits what developer Simon Willison named the ["lethal trifecta"](https://simonwillison.net/2025/Jun/16/the-lethal-trifecta/), and Levi uses the same term: an agent that can reach private data, takes in untrusted outside content, and has a way to send data out. Combine all three, and you have a leak path.

This is not the kind of bug a patch closes; as Levi frames it, it is a structural consequence of giving AI agents standing credentials while having them read attacker-reachable text.

## Why does this keep happening

GitLost is the latest in a run of the same kind of attack, and THN has reported several in recent months. A flaw in [Anthropic's Claude Code GitHub Action](https://thehackernews.com/2026/06/claude-code-github-action-flaw-let-one.html) let a single malicious issue push the agent into leaking secrets and seizing write access to a repository.

Orca Security's [RoguePilot](https://thehackernews.com/2026/02/roguepilot-flaw-in-github-codespaces.html) used a hidden prompt in a GitHub issue to make Copilot leak a repository's privileged token. The GitHub-agent version of the problem goes back to at least May 2025, when Invariant Labs [showed](https://invariantlabs.ai/blog/mcp-github-vulnerability) that a public issue could push an agent connected to GitHub's MCP server into reading ...