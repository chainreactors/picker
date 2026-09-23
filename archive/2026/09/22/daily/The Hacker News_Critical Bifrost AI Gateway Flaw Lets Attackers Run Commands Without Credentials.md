---
title: Critical Bifrost AI Gateway Flaw Lets Attackers Run Commands Without Credentials
url: https://thehackernews.com/2026/09/critical-bifrost-ai-gateway-flaw-lets.html
source: The Hacker News
date: 2026-09-22
fetch_date: 2026-09-23T06:54:52.882405
---

# Critical Bifrost AI Gateway Flaw Lets Attackers Run Commands Without Credentials

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

# [Critical Bifrost AI Gateway Flaw Lets Attackers Run Commands Without Credentials](https://thehackernews.com/2026/09/critical-bifrost-ai-gateway-flaw-lets.html)

**Swati Khandelwal**Sep 22, 2026Artificial Intelligence / Vulnerability

[![](data:image/png;base64...)](https://blogger.googleusercontent.com/img/b/R29vZ2xl/AVvXsEieRvfWKvxkIOajVIJ1qC7l54ZBCtHMwZTfUHGqSZ_35vGzAl23py6GfaqrxYkcfWZ_K75t9BGC6btqJQiS9jwaV7O4kJsCSIIQxmn9VnZrBbdjxSN4AzQ05K9G-ES82qV1G6IUcsBetsb0mVO5e5IHTr2FyAA3gtCN8Vne5N1H5Swgd2FLLlwi0GXFQ0o/s1700-nu-rw-lo-l85-e365/bifrost.jpg)

A critical vulnerability in [Bifrost](https://github.com/maximhq/bifrost), an open-source AI gateway that routes requests to more than 20 LLM providers, allows an unauthenticated attacker to run arbitrary commands on the gateway server with a single HTTP request.

The flaw, tracked as [CVE-2026-90898](https://www.cve.org/CVERecord?id=CVE-2026-90898) (CVSS score: 9.8), affects all versions of the Bifrost HTTP transport before 2.1.0 when management authentication is disabled, which is the default configuration. A fix is available in transports/v2.1.0.

Yuval Moravchick of [JFrog Security Research](https://research.jfrog.com/vulnerabilities/bifrost-is-vulnerable-to-unauthenticated-remote-code-execution-via-mcp-stdio-client-registration-cve-2026-90898/), who discovered the flaw, said an attacker can register a stdio-type MCP client through a single unauthenticated POST to the management API endpoint /api/mcp/client. Bifrost starts the specified command immediately, before any MCP handshake, as the gateway process user.

On the official Docker image, that user is appuser. Because the gateway stores API keys for every connected provider, executing commands on the gateway process grants the attacker access to those credentials.

[![Cybersecurity](data:image/png;base64...)](https://thehackernews.uk/trust-world-update-d)

The stock Bifrost binary binds the management API to localhost by default, which limits exposure to the local machine. The official Docker image binds to 0.0.0.0, making the management API reachable from outside the container if the port is published.

Operators should upgrade to transports/v2.1.0, which returns 403 when an unauthenticated caller tries to register a stdio MCP client. Those who cannot upgrade immediately should set governance.auth\_config.is\_enabled to true, use strong credentials, and keep the management listener off untrusted networks.

JFrog advises treating any instance that ran with authentication disabled and the management API exposed as compromised, and rotating virtual keys and provider API keys.

Operators on transports/v2.0.0 are still affected by the MCP flaw. That release fixed only an earlier plugin vulnerability and does not block the unauthenticated registration. The 1.6.x line through 1.6.11 contains neither fix.

A second, related flaw found by Or Peles of the same research team was [disclosed on September 6](https://research.jfrog.com/vulnerabilities/bifrost-is-vulnerable-to-unauthenticated-remote-code-execution-via-a-custom-plugin-http-path-on-dynamically-linked-builds-cve-2026-86242-jfsa-2026-001684572/). [CVE-2026-86242](https://www.cve.org/CVERecord?id=CVE-2026-86242) (CVSS score: 8.1) allows an unauthenticated attacker to register a custom plugin whose path is an HTTP URL. Bifrost downloads the file, writes it as a temporary shared object, and loads it through Go's plugin.Open function.

On dynamically linked builds, which Bifrost requires for custom Go plugins, the plugin loads and its code runs as the gateway process user. On statically linked builds, including the official Docker image, plugin.Open fails and the result is server-side request forgery only. The fix is in transports/v2.0.0.

[![Cybersecurity](data:image/png;base64...)](https://thehackernews.uk/ai-security-guide-b)

Both flaws share the same root cause: Bifrost's management API ships with authentication disabled by default. They are the second and third security issues disclosed in the project in under a month, after an unrelated SSRF flaw (CVE-2026-55245) fixed in late August.

The MCP flaw follows a pattern that has already led to real-world attacks. In April 2026, researchers [disclosed a design flaw in MCP's STDIO transport](https://thehackernews.com/2026/04/anthropic-mcp-design-vulnerability.html) that affects Anthropic's official SDKs. A similar command-injection flaw in LiteLLM, another AI gateway, was [actively exploited](https://thehackernews.com/2026/06/litellm-flaw-cve-2026-42271-exploited.html) and added to CISA's Known Exploited Vulnerabilities catalog in June.

Neither Bifrost CVE appears in the KEV catalog as of publication.

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

[API Security](https://thehackernews.com/search/label/API%20Security), [artificial intelligence](https://thehackernews.com/search/label/artificial%20intelligence), [Vulnerability](https://thehackernews.com/search/label/Vulnerability), [Web Security](https://thehackernews.com/search/label/Web%20Security)

⚡ Top Stories This Week

[![The Hacker News](data:image/svg+xml;base64...)

Claude Opus 5 Helped Researchers Take Over OpenAI Staff Accounts ...