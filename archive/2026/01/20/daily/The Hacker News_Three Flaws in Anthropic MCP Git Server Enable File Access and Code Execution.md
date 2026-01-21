---
title: Three Flaws in Anthropic MCP Git Server Enable File Access and Code Execution
url: https://thehackernews.com/2026/01/three-flaws-in-anthropic-mcp-git-server.html
source: The Hacker News
date: 2026-01-20
fetch_date: 2026-01-21T03:33:18.234583
---

# Three Flaws in Anthropic MCP Git Server Enable File Access and Code Execution

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
* [Data Breaches](/search/label/data%20breach)
* [Cyber Attacks](/search/label/Cyber%20Attack)
* [Vulnerabilities](/search/label/Vulnerability)
* [Webinars](/p/upcoming-hacker-news-webinars.html)
* [Expert Insights](https://thehackernews.com/expert-insights/)
* [Contact](/p/submit-news.html)

**

**

**

Resources

* [Webinars](/p/upcoming-hacker-news-webinars.html)
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

# [Three Flaws in Anthropic MCP Git Server Enable File Access and Code Execution](https://thehackernews.com/2026/01/three-flaws-in-anthropic-mcp-git-server.html)

**Ravie Lakshmanan**Jan 20, 2026Vulnerability / Artificial Intelligence

[![](data:image/png;base64...)](https://blogger.googleusercontent.com/img/b/R29vZ2xl/AVvXsEj-pw9mrLv_u7G4cYmZabAPduOBzVremxpnTTBjAnpvt95Kdt-kVFdO1GuHAnFwKZ0MNOAB86u6PacmrUDnAT0tcXghadZTRaEQTFiCXUTcoQksHFc4FKIpWGGYeVmJHM0kLvyWrUC7QPHJ6sjkHGEPgjNwkjpJSQihknrukwDKzuvW445fDoi1tNPfThXW/s1600-e365/git-ai-flaw.jpg)

A set of three security vulnerabilities has been disclosed in [mcp-server-git](https://pypi.org/project/mcp-server-git/), the official Git Model Context Protocol ([MCP](https://github.com/modelcontextprotocol/servers)) server maintained by Anthropic, that could be exploited to read or delete arbitrary files and execute code under certain conditions.

"These flaws can be exploited through prompt injection, meaning an attacker who can influence what an AI assistant reads (a malicious README, a poisoned issue description, a compromised webpage) can weaponize these vulnerabilities without any direct access to the victim's system," Cyata researcher Yarden Porat [said](https://cyata.ai/blog/cyata-research-breaking-anthropics-official-mcp-server/) in a report shared with The Hacker News.

Mcp-server-git is a Python package and an MCP server that provides a set of built-in tools to read, search, and manipulate Git repositories programmatically via large language models (LLMs).

[![Cybersecurity](data:image/png;base64...)](https://thehackernews.uk/zero-trust-summit-d)

The security issues, which have been addressed in versions 2025.9.25 and 2025.12.18 following responsible disclosure in June 2025, are listed below -

* **[CVE-2025-68143](https://github.com/modelcontextprotocol/servers/security/advisories/GHSA-5cgr-j3jf-jw3v)** (CVSS score: 8.8 [v3] / 6.5 [v4]) - A path traversal vulnerability arising as a result of the git\_init tool accepting arbitrary file system paths during repository creation without validation (Fixed in version 2025.9.25)
* **[CVE-2025-68144](https://github.com/modelcontextprotocol/servers/security/advisories/GHSA-9xwc-hfwc-8w59)** (CVSS score: 8.1 [v3] / 6.4 [v4]) - An argument injection vulnerability arising as a result of git\_diff and git\_checkout functions passing user-controlled arguments directly to git CLI commands without sanitization (Fixed in version 2025.12.18)
* **[CVE-2025-68145](https://github.com/modelcontextprotocol/servers/security/advisories/GHSA-j22h-9j4x-23w5)** (CVSS score: 7.1 [v3] / 6.3 [v4]) - A path traversal vulnerability arising as a result of a missing path validation when using the --repository flag to limit operations to a specific repository path (Fixed in version 2025.12.18)

Successful exploitation of the above vulnerabilities could allow an attacker to turn any directory on the system into a Git repository, overwrite any file with an empty diff, and access any repository on the server.

In an attack scenario documented by Cyata, the three vulnerabilities could be chained with the [Filesystem MCP server](https://github.com/modelcontextprotocol/servers/tree/main/src/filesystem) to write to a ".git/config" file (typically located within the hidden .git directory) and achieve remote code execution by triggering a call to git\_init by means of a prompt injection.

* Use git\_init to create a repo in a writable directory
* Use the Filesystem MCP server to write a malicious .git/config with a clean filter
* Write a .gitattributes file to apply the filter to certain files
* Write a shell script with the payload
* Write a file that triggers the filter
* Call git\_add, which executes the clean filter, running the payload

[![Cybersecurity](data:image/png;base64...)](https://thehackernews.uk/attack-surface-insight-d)

In response to the findings, the git\_init tool has been removed from the package and adds extra validation to prevent path traversal primitives. Users of the Python package are recommended to update to the latest version for optimal protection.

"This is the canonical Git MCP server, the one developers are expected to copy," Shahar Tal, CEO and co-founder of Agentic AI security company Cyata, said. "If security boundaries break down even in the reference implementation, it's a signal that the entire MCP ecosystem needs deeper scrutiny. These are not edge cases or exotic configurations, they work out of the box."

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

[Anthropic](https://thehackernews.com/search/label/Anthropic)[artificial intelligence](https://thehackernews.com/search/label/artificial%20intelligence)[cybersecurity](https://thehackernews.com/search/label/cybersecurity)[Git](https://thehackernews.com/search/label/Git)[Path Traversal](https://thehackernews.com/search/label/Path%20Traversal)[Prompt Injection](https://thehackernews.com/search/label/Prompt%20Injection)[remote code execution](https://thehackernews.com/search/label/remote%20code%20execution)[Vulnerability](https://thehackernews.com/search/label/Vulnerability)

Trending News

[![⚡ Weekly Recap: Fortinet Exploits, RedLine Clipjack, NTLM Crack, Copilot Attack and More](data:image/svg+xml;base64... "⚡ Weekly Recap: Fortinet Exploits, RedLine Clipjack, NTLM Crack, Copilot Attack and More")

⚡ Weekly Recap: Fortinet Exploits, RedLine Clipjack, NTLM Crack, Copilot Attack and More](https://thehackernews.com/2026/01/weekly-recap-fortinet-exploits-redline.html)

[![n8n Supply Chain Attack Abuses Community Nodes to Steal OAuth Tokens](data:im...