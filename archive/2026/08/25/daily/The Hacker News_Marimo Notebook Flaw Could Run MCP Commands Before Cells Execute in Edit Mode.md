---
title: Marimo Notebook Flaw Could Run MCP Commands Before Cells Execute in Edit Mode
url: https://thehackernews.com/2026/08/marimo-notebook-flaw-could-run-mcp.html
source: The Hacker News
date: 2026-08-25
fetch_date: 2026-08-26T03:07:02.430880
---

# Marimo Notebook Flaw Could Run MCP Commands Before Cells Execute in Edit Mode

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

[![cybersecurity](https://blogger.googleusercontent.com/img/b/R29vZ2xl/AVvXsEipoZWeZ29mSf60rRpMZ3Ucnm7oeWBfslPFPT6xADBsdvBtjd20ovH2yLscUo8pS6OTK0ItATC25VeavJh73IgqJM6Nb3apqobQ9zEVISE-d0wEFAimLYUcnffWCTowCCqs5LofRTQP25xB32KzYhlTO8lUnkZfmtELv23LlgdeKY3nyS2etYQXGdPIQtnh/s728-e100/wiz-d.png)](https://thehackernews.uk/ai-security-playbook-d)

# [Marimo Notebook Flaw Could Run MCP Commands Before Cells Execute in Edit Mode](https://thehackernews.com/2026/08/marimo-notebook-flaw-could-run-mcp.html)

**Swati Khandelwal**Aug 25, 2026Vulnerability / AI Security

[![](data:image/png;base64...)](https://blogger.googleusercontent.com/img/b/R29vZ2xl/AVvXsEgpC_dsMXsEscdzMT8fjZ3uZ86XgjBqYcYWA7ZodJJUvbK6vnmafx_dANiNsjoAeqYwDxzqeTerWaWEIMIZSmp7CqfynzhkfKEnuGIoizK5vihRhSJIeOVn4cK3CdIFjnURkvQvI1VX-Gm11mqNmxOQPVK5loEBRZ2ELFzLc1Y8C_z_ajrA5beUowEfwg0/s1700-e365/marimo.jpg)

Marimo has addressed a high-severity security flaw in its notebook software that allowed an attacker to execute an attacker-supplied Model Context Protocol (MCP) command in a specially crafted notebook, according to VulnCheck's CVE Numbering Authority (CNA) record.

The CNA record says the command can run as a local subprocess when the notebook is opened in edit mode.

The vulnerability, tracked as **CVE-2026-75149**, is a code injection issue affecting versions prior to 0.23.15. VulnCheck's CVE Numbering Authority (CNA) record assigns it a CVSS v4 score of 8.7 and a CVSS v3.1 score of 8.8, with user interaction required and no attacker authentication required.

Marimo has addressed the issue in version 0.23.15. The CVE was published on August 19. Users running an affected release should move to a version outside the affected range.

According to [OSV's CVE import](https://osv.dev/vulnerability/CVE-2026-75149), a crafted notebook can supply an attacker-controlled MCP server command through notebook configuration.

[![Cybersecurity](data:image/png;base64...)](https://thehackernews.uk/zero-trust-claude-d)

The victim opens the notebook in edit mode. The CNA record says the specified command is launched as a local subprocess before any notebook cell is executed.

Marimo's [PEP 723 hardening patch](https://github.com/marimo-team/marimo/commit/1a21bd71e258438d2511136b5edacc94c08855f4) treats notebook metadata as attacker-controlled and passes notebook-supplied configuration through an allowlist.

The following notebook-supplied configuration sections are removed -

* ai
* mcp
* completion
* secrets
* server

The patch's MCP regression case uses an attacker-controlled URL and verifies that the mcp section is removed. The CNA record supplies the separate command-to-subprocess behavior described for CVE-2026-75149.

The Hacker News confirmed on August 25 that the [current PyPI release](https://pypi.org/project/marimo/0.24.0/) is version 0.24.0, released August 17. Marimo's [version 0.23.15 release](https://github.com/marimo-team/marimo/releases/tag/0.23.15) was published on July 23, 2026. Marimo's [security policy](https://github.com/marimo-team/marimo/security/policy) says security patches are provided for the latest stable release and encourages users to stay current.

The CVE record credits Gregory Tan, who uses the handle Grg0rry, with discovering the flaw. The same handle also appears as a co-author on Marimo's PEP 723 hardening commit.

The same configuration boundary was addressed in VulnCheck's [separate CVE-2026-67618 advisory](https://www.vulncheck.com/advisories/marimo-api-key-exfiltration-via-malicious-notebook-pep-723-metadata) (CVSS score: 7.1), disclosed on August 4, 2026. That flaw affects Marimo versions before 0.23.15 and involves an attacker-controlled artificial intelligence (AI) base\_url supplied through notebook metadata.

For CVE-2026-67618, an operator opens the malicious notebook. The operator later makes an AI request. The configured endpoint then receives the operator's API key without requiring a notebook cell to be executed.

[![Cybersecurity](data:image/png;base64...)](https://thehackernews.uk/corelight-d)

CVE-2026-75149 is separate from the [earlier CVE-2026-39987 flaw](https://thehackernews.com/2026/04/marimo-rce-flaw-cve-2026-39987.html) in Marimo. [Marimo's advisory](https://github.com/marimo-team/marimo/security/advisories/GHSA-2679-6mx9-h9xc) for that vulnerability states that versions 0.20.4 and earlier were affected by a missing authentication validation on the /terminal/ws endpoint.

Requests reaching that endpoint could obtain a full pseudo-terminal (PTY) shell. The shell could then execute arbitrary commands. Marimo lists version 0.23.0 as the patched version for the earlier flaw.

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

[AI Security](https://thehackernews.com/search/label/AI%20Security), [Application Security](https://thehackernews.com/search/label/Application%20Security), [Code Execution](https://thehackernews.com/search/label/Code%20Execution), [Code Injection](https://thehackernews.com/search/label/Code%20Injection), [Developer Security](https://thehackernews.com/search/label/Developer%20Security), [Open Source Security](https://thehackernews.com/search/label/Open%20Source%20Security), [Software Security](https://thehackernews.com/search/label/Software%20Security), [Vulnerability](https://thehackernews.com/search/label/Vulnerability)

⚡ Top Stories This Week

[![The Hacker News](data:image/svg+xml;base64...)

Microsoft Patches Severe Entra ID Flaw (CVSS 10.0) Allowing Remote Code Execution](https://thehackernews.com/2026/08/microsoft-entra-id-f...