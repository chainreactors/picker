---
title: SmartLoader Attack Uses Trojanized Oura MCP Server to Deploy StealC Infostealer
url: https://thehackernews.com/2026/02/smartloader-attack-uses-trojanized-oura.html
source: The Hacker News
date: 2026-02-17
fetch_date: 2026-02-18T04:16:20.812277
---

# SmartLoader Attack Uses Trojanized Oura MCP Server to Deploy StealC Infostealer

#1 Trusted Cybersecurity News Platform

Followed by 5.20+ million[**](https://twitter.com/thehackersnews)
[**](https://www.linkedin.com/company/thehackernews/)
[**](https://www.facebook.com/thehackernews)

[![The Hacker News Logo](data:image/png;base64...)](/)

**

**

[** Subscribe – Get Latest News](#email-outer)

* [** Home](/)
* [** Newsletter](#email-outer)
* [** Webinars](/p/upcoming-hacker-news-webinars.html)

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

[![Security Service Edge](https://blogger.googleusercontent.com/img/b/R29vZ2xl/AVvXsEg5Ij_-TeqFMEsRFzgRRFzSRlVK6oHCncN_eJ2fkOdsA_1tN9HQbAlEEife2Z2JUt1lPv4st5n9KZP84jGEYY9Up6BQ7QE-N5rs6OhzL5thxGzVxnMx3JH9cGRLi9S5Kl-iV5PgjBeTdkBLnv_inF8UUAo88iqdmgJuPIc_6qiPyUMXwFyZWbZvkZkcRXSw/s728-e100/gartner-d.jpg)](https://thehackernews.uk/sse-awards-insight-d)

# [SmartLoader Attack Uses Trojanized Oura MCP Server to Deploy StealC Infostealer](https://thehackernews.com/2026/02/smartloader-attack-uses-trojanized-oura.html)

**Ravie Lakshmanan**Feb 17, 2026Infostealer / Artificial Intelligence

[![](data:image/png;base64...)](https://blogger.googleusercontent.com/img/b/R29vZ2xl/AVvXsEhTqbI3s_iPxMUClWM1mAlNmZ1XoIGvcr_s7qE8slqSkSFCyPIU50Ml0XsqsxGAnsMt1Ys4v9Z2MYWapLXIB9bvkvXw7pPt8NvS05UotSaichBUZjw-WaoUwIlUCMjk1elkTOAFdwFfZyNCufWdiNoL2CmhbuW79HpBxWDELf1mqDC6ZA3BShpMK8C8sUbL/s1700-e365/mcp-hack.jpg)

Cybersecurity researchers have disclosed details of a new **SmartLoader** campaign that involves distributing a trojanized version of a Model Context Protocol ([MCP](https://thehackernews.com/2025/04/experts-uncover-critical-mcp-and-a2a.html)) server associated with Oura Health to deliver an information stealer known as [StealC](https://thehackernews.com/2025/01/mintsloader-delivers-stealc-malware-and.html).

"The threat actors cloned a legitimate Oura MCP Server – a tool that connects AI assistants to Oura Ring health data – and built a deceptive infrastructure of fake forks and contributors to manufacture credibility," Straiker's AI Research (STAR) Labs team [said](https://www.straiker.ai/blog/smartloader-clones-oura-ring-mcp-to-deploy-supply-chain-attack) in a report shared with The Hacker News.

The end game is to leverage the trojanized version of the Oura MCP server to deliver the StealC infostealer, allowing the threat actors to steal credentials, browser passwords, and data from cryptocurrency wallets.

SmartLoader, [first highlighted](https://thehackernews.com/2024/04/new-redline-stealer-variant-disguised.html) by OALABS Research in early 2024, is a malware loader that's known to be distributed via fake GitHub repositories containing artificial intelligence (AI)-generated lures to give the impression that they are legitimate.

In an analysis published in March 2025, Trend Micro [revealed](https://thehackernews.com/2025/03/microsoft-warns-of-clickfix-phishing.html) that these repositories are disguised as game cheats, cracked software, and cryptocurrency utilities, typically coaxing victims with promises of free or unauthorized functionality to make them download ZIP archives that deploy SmartLoader.

[![Cybersecurity](data:image/png;base64...)](https://thehackernews.uk/sse-customer-awards-d)

The latest findings from Straiker highlight a new AI twist, with threat actors creating a network of bogus GitHub accounts and repositories to serve trojanized MCP servers and submitting them to legitimate MCP registries like [MCP Market](https://mcpmarket.com). The MCP server is [still listed](https://mcpmarket.com/server/oura-9) on the MCP directory.

By poisoning MCP registries and weaponizing platforms like GitHub, the idea is to leverage the trust and reputation associated with services to lure unsuspecting users into downloading malware.

[![](data:image/png;base64...)](https://blogger.googleusercontent.com/img/b/R29vZ2xl/AVvXsEiFHmDiRApF8aT_xdH6It4oQ5NuYyo49xsKn2n9q-ZUYrDbg8WHujJCwglgTLMh16_spPRryR6-YKJWlgfB1EDoulIK70x8Xprsa13RgP7ZclM1ey8beQNsO94HbNPAAsUBeanxKgPRUX0H4aegIYNu5ilss3dTiF1bpuPND0osC__ZiQAfY616O8MI99k4/s1700-e365/oura.png)

"Unlike opportunistic malware campaigns that prioritize speed and volume, SmartLoader invested months building credibility before deploying their payload," the company said. "This patient, methodical approach demonstrates the threat actor's understanding that developer trust requires time to manufacture, and their willingness to invest that time for access to high-value targets."

The attack essentially unfolded over four stages -

* Created at least 5 fake GitHub accounts (YuzeHao2023, punkpeye, dvlan26, halamji, and yzhao112) to build a collection of seemingly legitimate repository forks of [Oura MCP server](https://github.com/tomekkorbak/oura-mcp-server).
* Created another Oura MCP server repository with the malicious payload under a new account "SiddhiBagul"
* Added the newly created fake accounts as "contributors" to lend a veneer of credibility, while deliberately excluding the original author from contributor lists
* Submitted the trojanized server to the MCP Market

[![Cybersecurity](data:image/png;base64...)](https://thehackernews.uk/ztw-hands-on-d)

This also means that users who end up searching for the Oura MCP server on the registry would end up finding the rogue server listed among other benign alternatives. Once launched via a ZIP archive, it results in the execution of an obfuscated Lua script that's responsible for dropping SmartLoader, which then proceeds to deploy StealC.

The evolution of the SmartLoader campaign indicates a shift from attacking users looking for pirated software to developers, whose systems have become high-value targets, given that they tend to contain sensitive data such as API keys, cloud credentials, cryptocurrency wallets, and access to production systems. The stolen data could then be abused to fuel follow-on intrusions.

As mitigations to combat the threat, organizations are recommended to inventory installed MCP servers, establish a formal security review before installation, verify the origin of MCP servers, and monitor for suspicious egress traffic and persistence mechanisms.

"This campaign exposes fundamental weaknesses in how organizations evaluate AI tooling," Straiker said. "SmartLoader's success depends on security teams and developers applying outdated trust heuristics to a new attack surface."

Found this article interesting? Follow us on [Google News](https://news.google.com/publications/CAAqLQgKIidDQklTRndnTWFoTUtFWFJvWldoaFkydGxjbTVsZDNNdVkyOXRLQUFQAQ), [Twitter](https://twitter.com/thehackersnews) and [LinkedIn](https://www.linkedin.com/company/thehackernews/) to read more exclusive content we post.

SHARE
[**](#link_share)
[**](#link_share)
[**](#link_share)
**

[**Tweet](#link_share)

[**Share](#link_share)

[**Share](#link_share)

*...