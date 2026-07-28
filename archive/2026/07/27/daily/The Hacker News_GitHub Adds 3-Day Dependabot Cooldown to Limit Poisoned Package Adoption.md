---
title: GitHub Adds 3-Day Dependabot Cooldown to Limit Poisoned Package Adoption
url: https://thehackernews.com/2026/07/github-adds-3-day-dependabot-cooldown.html
source: The Hacker News
date: 2026-07-27
fetch_date: 2026-07-28T05:00:17.185390
---

# GitHub Adds 3-Day Dependabot Cooldown to Limit Poisoned Package Adoption

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

# [GitHub Adds 3-Day Dependabot Cooldown to Limit Poisoned Package Adoption](https://thehackernews.com/2026/07/github-adds-3-day-dependabot-cooldown.html)

**Ravie Lakshmanan**Jul 27, 2026Software Supply Chain / DevSecOps

[![](data:image/png;base64...)](https://blogger.googleusercontent.com/img/b/R29vZ2xl/AVvXsEiFpE4BZgV3wILI8fonm9742zR85yLmBdM2ExXv-uTUS1StV04ZlNVVIwV6FjjhYLZUAFk-DAIInwp3mlXa2W2xekDA_EqSl1UiHrKCgocsjhVAKlvCD48QnlVdUdCIQia7T4ilS65ZFptdi_wox0Q9brVTdpoqDNTvpCjg0D6BslyCAPRzY7QMyUoYNkv-/s1700-e365/gitbot.jpg)

GitHub has announced a new cooldown mechanism in Dependabot, allowing the tool to wait at least three days after a release is published before opening a pull request.

"The cooldown configuration option in the dependabot.yml still controls the behavior, though, so you can choose a different cooldown parameter that fits your project," the Microsoft-owned subsidiary [said](https://github.blog/security/supply-chain-security/the-case-for-a-cooldown-why-dependabot-now-waits-before-issuing-version-updates/).

According to GitHub, the three-day cooldown default only applies to version updates, which are designed to keep software dependencies up-to-date. Security updates will continue to be pushed right away, permitting Dependabot to issue an alert and open a pull request to move the project to the patched version.

With this update, the idea is to handle scenarios where a threat actor manages to push a poisoned version of a popular package, which then gets quickly pulled by downstream projects before that version is yanked from the registry. Although such trojanized packages are short-lived, the time period for which they remain accessible is enough to expand the blast radius of a supply chain attack.

GitHub said it arrived at three days as the default as it considers the duration to be in the goldilocks zone. "Three days as the default balances two goals: it pushes you past the window where most of these attacks live, and it doesn't hold your dependencies back longer than necessary," it added.

[![Cybersecurity](data:image/png;base64...)](https://thehackernews.uk/ai-vuln-protection-d)

At the same time, the software development platform emphasized that the control should be just one layer of defense among several others, including pinning dependencies with lockfiles, disabling install scripts in CI, scoping the tokens in build pipelines, and reviewing updates before they merge.

"A cooldown is built for a specific pattern: a malicious version that ships, spreads, and gets caught quickly," GitHub said. "It does little against attacks that play a longer game, including backdoors planted in releases and left dormant, maintainer sabotage, or a compromised build system."

It's worth noting [similar cooldown controls](https://thehackernews.com/2026/06/vs-code-adds-2-hour-extension-auto.html) have been announced across various package ecosystems over the past year, including Microsoft Visual Studio Code (VS Code), Ruby, Bun, npm, pnpm, and Yarn.

GitHub's time-based defense comes as the maintainers of the Python Package Index (PyPI) [announced](https://thehackernews.com/2026/07/threatsday-android-spyware-plc-attacks.html#old-releases-locked-down) plans to block maintainers from adding new files to a package release after 14 days have passed since its publication.

"The measure is intended to prevent attackers who compromise publishing tokens or workflows from poisoning old, trusted releases," PyPI noted.

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
[**Share on Hacker News](#link_share)
[**Share on Email](#link_share)
[**Share on WhatsApp](#link_share)
[![Facebook Messenger](data:image/png;base64...)Share on Facebook Messenger](#link_share)
[**Share on Telegram](#link_share)

SHARE **

[Application Security](https://thehackernews.com/search/label/Application%20Security), [CI/CD Security](https://thehackernews.com/search/label/CI/CD%20Security), [DevSecOps](https://thehackernews.com/search/label/DevSecOps), [GitHub](https://thehackernews.com/search/label/GitHub), [Open Source](https://thehackernews.com/search/label/Open%20Source), [Package Security](https://thehackernews.com/search/label/Package%20Security), [Python](https://thehackernews.com/search/label/Python), [Software Supply Chain](https://thehackernews.com/search/label/Software%20Supply%20Chain)

⚡ Top Stories This Week

[![New Bit2Watt Attack Could Let Cloud Tenants Disrupt Power Grids Without an Exploit](data:image/svg+xml;base64... "New Bit2Watt Attack Could Let Cloud Tenants Disrupt Power Grids Without an Exploit")

New Bit2Watt Attack Could Let Cloud Tenants Disrupt Power Grids Without an Exploit](https://thehackernews.com/2026/07/new-bit2watt-attack-could-let-cloud.html)

[![Open-Source Android AI Agents Could Let Invisible Screen Text Run Code on Host PCs](data:image/svg+xml;base64... "Open-Source Android AI Agents Could Let Invisible Screen Text Run Code on Host PCs")

Open-Source Android AI Agents Could Let Invisible Screen Text Run Code on Host PCs](https://thehackernews.com/2026/07/open-source-android-ai-agents-could-let.html)

[![Critical SharePoint RCE CVE-2026-50522 Under Active Exploitation After Public PoC](data:image/svg+xml;base64... "Critical SharePoint RCE CVE-2026-50522 Under Active Exploitation After Public PoC")

Critical SharePoint RCE CVE-2026-50522 Under Active Exploitation After Public PoC](https://thehackernews.com/2026/07/critical-sharepoint-...