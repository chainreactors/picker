---
title: GitHub Internal Repositories Breached via Malicious Nx Console VS Code Extension
url: https://thehackernews.com/2026/05/github-internal-repositories-breached.html
source: The Hacker News
date: 2026-05-21
fetch_date: 2026-05-22T06:08:40.410026
---

# GitHub Internal Repositories Breached via Malicious Nx Console VS Code Extension

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

[![cybersecurity](https://blogger.googleusercontent.com/img/b/R29vZ2xl/AVvXsEhyqUz0-ifa8jE9rCzud3wzxmhcuzTp1VOWFEvGMoZXDYfaB_4459fPyvyQw7wvAnzjzDL09PkyJM83QGheO69fC3esg1WA7WnJ89i_t_q3K8DxYmgV__QujU8RWRnCK4MpbKqu8nwuMFfLaiRVHy_ov7IZ16hoKI3rIu-5BcISmqXPjlQU7N0sa4lWI-n-/s728-e100/wiz-d.png)](https://thehackernews.uk/wiz-ai-state-d)

# [GitHub Internal Repositories Breached via Malicious Nx Console VS Code Extension](https://thehackernews.com/2026/05/github-internal-repositories-breached.html)

**Ravie Lakshmanan**May 21, 2026Supply Chain Attack / Developer Tools

[![](data:image/png;base64...)](https://blogger.googleusercontent.com/img/b/R29vZ2xl/AVvXsEjJ64wgVqZTQx208NgY0sBvUUQcR5mb-G4ENkfw4PEX9KlJJxEI_uUKQvPG0rReXB4chZ3wXrvNSR1QsrK525DDHkzY9X3nQYduh36qKTyC-k4EfixFeOU7YR1mRIw8ZJL-oYN8k_wwBid2GU8NYJtCqEFLOSzomuu-Xx7yA3Djim0nq79RyoZJs6HGga_H/s1700-e365/github-hacked.jpg)

GitHub on Wednesday officially confirmed that the [breach of its internal repositories](https://thehackernews.com/2026/05/github-investigating-teampcp-claimed.html) was the result of a compromise of an employee device involving a poisoned version of the Nx Console Microsoft Visual Studio Code (VS Code) extension.

The development comes as the Nx team revealed that the extension, [nrwl.angular-console](https://thehackernews.com/2026/05/compromised-nx-console-18950-targeted.html), was breached after one of its developers' systems was hacked in the wake of the recent [TanStack](https://thehackernews.com/2026/05/mini-shai-hulud-worm-compromises.html) supply chain attack. Other companies that were impacted by the TanStack compromise include [OpenAI, Mistral AI](https://thehackernews.com/2026/05/tanstack-supply-chain-attack-hits-two.html), and [Grafana Labs](https://thehackernews.com/2026/05/grafana-github-breach-exposes-source.html).

"We have no evidence of impact to customer information stored outside of GitHub's internal repositories, such as our customer's own enterprises, organizations, and repositories," Alexis Wales, Chief Information Security Officer of GitHub, [said](https://github.blog/security/investigating-unauthorized-access-to-githubs-internal-repositories/) in a statement.

"Some of GitHub's internal repositories contain information from customers, for example, excerpts of support interactions. If any impact is discovered, we will notify customers via established incident response and notification channels."

[![Cybersecurity](data:image/png;base64...)](https://thehackernews.uk/threatlabz-vpn-risk-2026-d)

The attack is said to have allowed the threat actor, a cybercriminal group known as TeamPCP, to exfiltrate about 3,800 repositories. GitHub said it has taken steps to contain the incident and rotated critical secrets, adding it's continuing to monitor the situation for follow-on activity.

In a post on X, Jeff Cross, co-founder of Narwhal Technologies, the company behind nx.dev, [said](https://x.com/jeffbcross/status/2057236396658811020), "this incident highlights that there need to be deeper, more fundamental changes to how we and other maintainers need to think about securing developer tooling and open source distribution."

"We're also beginning conversations with other high-profile open source maintainers about how we can work together on some of the deeper structural problems around software supply chain security. A lot of the assumptions the ecosystem has operated under for years no longer hold."

In recent months, TeamPCP has rapidly gained notoriety for large-scale software supply chain attacks, specifically going after widely-used open-source projects and security-adjacent tools that developers rely on.

What's notable here is that the trojanized version of the VS Code extension was live on Visual Studio Marketplace only for 18 minutes (between 12:30 p.m. and 12:48 p.m. UTC on May 18, 2026). But this short window was enough for the attackers to distribute a credential stealer capable of harvesting sensitive data from 1Password vaults, Anthropic Claude Code configurations, npm, GitHub, and Amazon Web Services (AWS).

"The extension looked and behaved like normal Nx Console, but on startup it silently ran a single shell command that downloaded and executed a hidden package from a planted commit on the official nrwl/nx GitHub repository," OX Security researcher Nir Zadok [said](https://www.ox.security/blog/teampcp-strikes-again-how-a-trojan-vs-code-extension-brought-down-github/). "The command was disguised as a routine MCP setup task so it would not raise suspicion."

[![Cybersecurity](data:image/png;base64...)](https://thehackernews.uk/ai-cant-stop-d)

The interlinked nature of modern software has allowed TeamPCP to unleash a self-sustaining cycle of new compromises. The pattern that drives home this aspect is deceptively simple as it's nefarious: break into one trusted tool, steal credentials from developer systems that may install it, and use those credentials to break into the next legitimate tool.

"Every popular extension marketplace ships with auto-update on by default. VS Code, Cursor, the whole lineup," Aikido security researcher Raphael Silva [said](https://www.aikido.dev/blog/vs-code-extension-github-breach). "The reasoning makes sense in isolation, because most developers never update anything manually, so leaving it off means a long tail of editors running stale, vulnerable code."

"The trade-off stops making sense once you account for hostile/compromised publishers. Auto-update gives an attacker who controls a release a direct push channel into every machine running that extension. Marketplaces don't impose any review gate or waiting period between when an update is published and when installed clients pull it in."

Found this article interesting? Follow us on [Google News](https://news.google.com/publications/CAAqLQgKIidDQklTRndnTWFoTUtFWFJvWldoaFkydGxjbTVsZDNNdVkyOXRLQUFQAQ), [Twitter](https://twitter.com/thehackersnews) and [LinkedIn](https://www.linkedin.com/company/thehackernews/) to read more exclusive content we post.

SHARE
[**](#link_share)
[**](#link_share)
[**](#link_share)
**

[**Tweet](#link_share)

[**Share](#link_share)

[**Share](#link_share)

**Share

**
[**Share on Facebook](#link_share)
[**Share on Twitter](#link_share)
[**Share on Linkedin](#link_share)
[**Share on Reddit](#link_share)
[**Share on Hacker ...