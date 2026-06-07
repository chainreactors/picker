---
title: Miasma Worm Hits 73 Microsoft GitHub Repositories in Major Supply Chain Attack
url: https://thehackernews.com/2026/06/miasma-worm-hits-73-microsoft-github.html
source: The Hacker News
date: 2026-06-06
fetch_date: 2026-06-07T06:16:38.945598
---

# Miasma Worm Hits 73 Microsoft GitHub Repositories in Major Supply Chain Attack

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

# [Miasma Worm Hits 73 Microsoft GitHub Repositories in Major Supply Chain Attack](https://thehackernews.com/2026/06/miasma-worm-hits-73-microsoft-github.html)

**Ravie Lakshmanan**Jun 06, 2026Supply Chain Attack / Malware

[![](data:image/png;base64...)](https://blogger.googleusercontent.com/img/b/R29vZ2xl/AVvXsEgG8k6LtHNQ3cHl_X1AZbXRn6LZCNZ6lMLjy-9HG7-_OQekMOhCQKkktrnMqVteXfmGHBMMlbTv3v9Rl6kKjXlNQBSHUVybmD_IBVvMDT7IsMGV49OMSfF5V8bMFVW4ZwFjlg_gddyYtiiQqmdpYIJjuKLTZz_rxooZZQQye7omBEOjyxMFFjAaiZuc6Non/s1700-e365/azure-npm.jpg)

Microsoft's GitHub repositories have become the latest to fall victim to the ongoing **[Miasma](https://thehackernews.com/2026/06/ironworm-and-new-miasma-worm-variant.html)** self-replicating supply chain attack campaign.

The incident impacted 73 Microsoft repositories across four of its GitHub organizations, including Azure, Azure-Samples, Microsoft, and MicrosoftDocs, per [OpenSourceMalware](https://opensourcemalware.com/blog/miasma-reaches-azure). The development has GitHub to disable access to those repositories.

"Access to this repository has been disabled by GitHub Staff due to a violation of GitHub's terms of service," reads the message when attempting to access the "[Azure/azure-functions-host](https://github.com/Azure/azure-functions-host)" repository. "If you are the owner of the repository, you may reach out to GitHub Support for more information."

According to OpenSourceMalware, some of the repositories impacted by the incident are listed below -

* azure-search-openai-demo-purviewdatasecurity
* Connectors-NET-LSP
* Connectors-NET-SDK
* durabletask
* durabletask-dotnet
* durabletask-go
* durabletask-js
* durabletask-mssql
* functions-container-action
* homebrew-functions
* llm-fine-tuning
* windows-driver-docs

What's notable about the latest campaign is the re-compromise of the "durabletask" PyPI package, which was [infected](https://thehackernews.com/2026/05/github-investigating-teampcp-claimed.html) by TeamPCP last month to deliver an information stealer on Linux systems.

[![Cybersecurity](data:image/png;base64...)](https://thehackernews.uk/ai-cant-stop-d)

"A month later, not only is Azure/durabletask gone - so is every sibling repo in the Durable Task ecosystem, sitting one org over in Microsoft: the .NET, Go, Java, JS, MSSQL, Netherite, and protobuf implementations, plus the Durable Functions monitor," security researcher Paul McCarty (aka 6mile) said.

"When the repo at the root of last month's compromise is the hub of this month's takedown, that is not a coincidence - that is the same wound reopening. Whoever held those credentials in May plausibly never fully lost them."

[![](data:image/png;base64...)](https://blogger.googleusercontent.com/img/b/R29vZ2xl/AVvXsEhemNR9h_g1pzbtSuNnKWfQIxypfGLWb52x73fTBT1EhzNvDMk7ko7Gt6UPk2IkMPHd1N3TLkYDJmCi1gxMLbale7wTeVdxUfX67kY5D3rGDsiW12pRHdEAMhylTCo-GOikjN6IEJQkgTQ_xH0zDi9LShfBUXh14P9JS7ROjez0Z8vsXJZzHlGS8S6S7WjN/s1700-e365/githubs.jpg)

Miasma is assessed to be a variant of the Mini Shai-Hulud worm that TeamPCP [publicly released](https://www.akamai.com/blog/security-research/mini-shai-hulud-worm-returns-goes-public) in mid-May 2026. It has since continued to mutate and refine its tactics, even as it has [infected more packages](https://www.ox.security/blog/600000-monthly-downloads-affected-miasma-supply-chain-attack-is-back-on-npm/) over the past couple of days, using [various descriptions](https://x.com/OX__Security/status/2063025560738050373) for the newly-created public repositories containing the stolen secrets -

* Miasma: The Spreading Blight
* Miasma : The Spreading Blight
* Miasma - The Spreading Blight
* Hades - The End for the Damned

As of writing, there are [13 repositories](https://github.com/search?q=%22Hades%20The%20End%20for%20the%20Damned%22&type=repositories) with the description "Hades - The End for the Damned" and [82 repositories](https://github.com/search?q=%22Miasma+The+Spreading+Blight%22&type=repositories) with the remaining three naming patterns.

Miasma has also been observed skipping the npm registry entirely, with the threat actors pushing malicious code directly to "icflorescu/mantine-datatable" and four related repositories: "mantine-contextmenu," "next-server-actions-parallel," "mantine-datatable-v6," and "mantine-contextmenu-v6."

"The commit added no dependencies. It planted a 4.3 MB payload runner and wired it to execute automatically through five developer tools: Claude Code, Gemini CLI, Cursor, VS Code, and the npm test script," SafeDep [said](https://safedep.io/miasma-worm-ai-coding-agent-config-injection/). "The attack detonates when a developer clones one of the affected repos and opens it in an AI coding agent. The dropper is the same staged Bun loader, here repurposed for GitHub source-repo persistence rather than registry poisoning."

[![Cybersecurity](data:image/png;base64...)](https://thehackernews.uk/vpn-threat-report-m)

These software supply chain attacks have [exposed](https://www.uvcyber.com/resources/reports/threat-advisory-tanstack-supply-chain-attack) the underlying weaknesses in the trust model that forms the basis of software delivery in open-source ecosystems, making it one of the most significant and sustained campaigns observed to date. What separates the activity from other incidents is its ability to exponentially propagate across the ecosystem by compromising downstream users and repeating the same cycle.

"The worm's genius and the reason conventional defences largely failed is that it operates entirely within legitimate channels. It does not exploit a vulnerability in npm or GitHub," FalconFeeds.io [said](https://falconfeeds.io/blogs/shai-hulud-npm-pypi-supply-chain-worm-analysis/). "It exploits the trust model those platforms are built on: the assumption that if a package is signed with a valid key and published by an authenticated maintainer, it is safe."

"Shai-Hulud compromises the key and the maintainer, then proceeds to act exactly as a legitimate pub...