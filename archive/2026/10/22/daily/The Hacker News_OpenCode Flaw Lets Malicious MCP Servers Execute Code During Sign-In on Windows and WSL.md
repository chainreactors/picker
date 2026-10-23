---
title: OpenCode Flaw Lets Malicious MCP Servers Execute Code During Sign-In on Windows and WSL
url: https://thehackernews.com/2026/10/opencode-flaw-lets-malicious-mcp.html
source: The Hacker News
date: 2026-10-22
fetch_date: 2026-10-23T06:46:43.608813
---

# OpenCode Flaw Lets Malicious MCP Servers Execute Code During Sign-In on Windows and WSL

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

[![cybersecurity](https://blogger.googleusercontent.com/img/b/R29vZ2xl/AVvXsEgpv5Y6QePil1MjgPiKuj9qVcOEzN1QdpjV55lFLD7Nyll1Wy1-rDkPzUxoUxZBjyhD74ycWms55yNl3nOcVfzpirEVdQnc0bfulwnXhfb5IAO5oii05bR8bzttfawsmnOSBqpuNre7TO6eDyDJn4FhPAsISdesN9Nsfq-7UgOE6XMHMH5tSwffhl-qhK9h/s728-nu-rw-lo-l85-e365/wiz-d.png)](https://thehackernews.uk/ai-threat-guide-d)

# [OpenCode Flaw Lets Malicious MCP Servers Execute Code During Sign-In on Windows and WSL](https://thehackernews.com/2026/10/opencode-flaw-lets-malicious-mcp.html)

**Swati Khandelwal**Oct 22, 2026Vulnerability / Artificial Intelligence

[![](data:image/png;base64...)](https://blogger.googleusercontent.com/img/b/R29vZ2xl/AVvXsEiUmn80CiQx35trhXNaAwJka_Z3T-PKQrz__dlAW1GDDVwfrk2WHit1W6GZBaaAT-a9SrmqqauUhw0raYLEOS3Vv-LNxdu0a2bmJebJWVj5mBadfgxN1N1yVREXflCcV7cPmShswRE8PC0qspFY82MDEKe8MJImYVqJCBYLwTLpCHM1IzjDX7KsOAYs7tc/s1700-nu-rw-lo-l85-e365/opencode-mcp.jpg)

A flaw in the **OpenCode** AI coding agent allowed a malicious or hijacked MCP server to run code on a developer's Windows or WSL machine when the developer signed in. OpenCode connects to MCP (Model Context Protocol) servers to add outside tools, and such code would run with the developer's own access.

**Anomaly**, the company behind OpenCode, fixed the flaw in [version 1.18.33](https://github.com/anomalyco/opencode/releases/tag/v1.18.33) on September 28. It did not request a CVE or publish a security advisory, so vulnerability scanners will not flag the builds still at risk: 1.0.137 through 1.18.32.

During that sign-in, the server itself supplies the web address the user is sent to, an OAuth "authorization endpoint." On Windows and WSL, OpenCode handed that address to a helper that opens it in a browser. The helper built a PowerShell command around the address without escaping it, so an address written to carry a PowerShell command would run that command.

The browser step runs only when a developer starts the sign-in, by running opencode mcp auth or making the matching request. Having the server configured, or opening a session, does not reach it.

The attacker needs control of a remote MCP server the developer has added, and that server need not be hostile from the start. One that is later taken over, or a domain that changes hands, could carry the same address.

[![Cybersecurity](data:image/png;base64...)](https://thehackernews.uk/ai-governance-platform-d)

[Pillar Security](https://www.pillar.security/blog/open-and-shut-remote-code-execution-in-opencode-via-mcp-oauth), which found the flaw and disclosed it on October 19, rates it critical, with a proposed severity score of 9.8 out of 10.

The flaw affects OpenCode on Windows and the Windows Subsystem for Linux (WSL). macOS and Linux are not affected, because OpenCode opens the browser there without passing the address through a shell.

OpenCode shipped the fix as a routine change. The [pull request](https://github.com/anomalyco/opencode/pull/51414) that carried it is described as a refactor of browser-launch code, and neither it nor the release notes mention a security flaw.

Anomaly did not request a CVE or publish an advisory. Its [security policy](https://github.com/anomalyco/opencode/security) says MCP servers that a user configures are "outside our trust boundary."

Pillar reported the flaw privately on August 29 and later asked Anomaly to reconsider and request a CVE. Anomaly's answer was that a malicious MCP server falls outside its threat model, according to Pillar.

[![](data:image/png;base64...)](https://blogger.googleusercontent.com/img/b/R29vZ2xl/AVvXsEhng5X17str7JocTsBTg2viRAymvl2eHCQcWyihh6ykzsdHIlXM4ZLdUoqkfp2bKTWqTjDtutcDoDcVn3JhrNeHb-acB5Z5z3bx3zV_4Ef5k3klaNf8EpSWAlvXoHub6xdgmhlIei8sj6BIWgdE1pCl2fGudWIfFcOfezTC2XUC3OaE4pBvyd6d9lDpqpY/s1700-nu-rw-lo-l85-e365/mcp.png)

Because there is no CVE, the flaw will not show up in scanners or dependency alerts, so finding affected installs means checking the OpenCode version directly. Anomaly has published advisories for other OpenCode code-execution flaws this year, including one fixed in August.

The same kind of flaw has surfaced before. In July 2025, the mcp-remote proxy carried an [almost identical bug](https://thehackernews.com/2025/07/critical-mcp-remote-vulnerability.html), in which a malicious server's authorization endpoint reached the command line. It was assigned CVE-2025-6514.

OpenCode's browser helper is a widely used package called open. Its Windows behavior was [reported as a command-injection risk in 2023](https://github.com/sindresorhus/open/issues/323) and fixed in open's version 11, but OpenCode stayed on an older release.

[![Cybersecurity](data:image/png;base64...)](https://thehackernews.uk/network-defense-d)

The usual defense for this class is to check that the address uses HTTP or HTTPS. It does not help here, because the attack uses an ordinary HTTPS address. OpenCode added that check as well, but the hole was closed by updating it to the fixed version.

### What to Do

Anyone running OpenCode on Windows or WSL should upgrade and check which servers they are connected to.

1. Upgrade to OpenCode 1.18.33 or later.
2. If you cannot upgrade yet, remove any remote MCP servers you have not vetted from your OpenCode configuration.
3. Run opencode mcp list to see which servers are configured.

Pillar reported no signs that the flaw has been used in attacks and published no indicators to check for past exploitation. The flaw is separate from a [breach of OpenCode's hosted Console](https://thehackernews.com/2026/10/opencode-console-breach-may-have.html) disclosed around the same time, which may have exposed some users' stored API keys for OpenAI, Anthropic, and Google.

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
[**Share on Hacker News](#link_share...