---
title: AutoJack Attack Lets One Web Page Hijack AI Agent for Host Code Execution
url: https://thehackernews.com/2026/06/autojack-attack-lets-one-web-page.html
source: The Hacker News
date: 2026-06-19
fetch_date: 2026-06-20T06:14:42.395164
---

# AutoJack Attack Lets One Web Page Hijack AI Agent for Host Code Execution

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

# [AutoJack Attack Lets One Web Page Hijack AI Agent for Host Code Execution](https://thehackernews.com/2026/06/autojack-attack-lets-one-web-page.html)

**Swati Khandelwal**Jun 19, 2026Vulnerability / Software Supply Chain

[![](data:image/png;base64...)](https://blogger.googleusercontent.com/img/b/R29vZ2xl/AVvXsEg3wJOg5Y5vAn_dM0DcIB6SwV2B34iO0H-moeyuWLJ_DF1KgEEZMBGtKPDXYk0pL4wclWbnSmOB74sqReSZoGI2_SwUSzKSscUxEdvuJFx_sCIfU7UplU2k5s4UA0cOVAZT_s80PDTek6OGfrsnE8f6QxrQU58rBqPiuk_J__Yja3YNzZLzd-6s8Ji1PBhc/s1700-e365/agent.jpg)

Microsoft researchers have detailed an exploit chain, named [AutoJack](https://www.microsoft.com/en-us/security/blog/2026/06/18/autojack-single-page-rce-host-running-ai-agent/), that turns an AI browsing agent into a delivery vehicle for remote code execution.

Steer the agent to load an attacker's web page, and that page's JavaScript can reach a privileged local service on the same machine and spawn a process on the host.

No credentials, no sign-in screen, and no further user interaction once the agent loads the page. The attacker only has to get the agent to open it, and a planted link, a URL field, or a prompt injection will do.

The flaw sits in [AutoGen Studio](https://microsoft.github.io/autogen/docs/autogen-studio/getting-started), the open-source prototyping interface for Microsoft Research's AutoGen multi-agent framework. This is not a bug that hits everyone who installs the package, and the packaging detail is worth getting right.

A plain pip install autogenstudio pulls the current stable release, 0.4.2.2, the build Microsoft inspected, and it has no Model Context Protocol (MCP) route at all.

That is the basis for Microsoft's statement that the vulnerable MCP WebSocket surface "was never included in a PyPI release." It holds for the stable build. But the vulnerable handler did ship to PyPI, in two pre-release builds, 0.4.3.dev1 and 0.4.3.dev2.

[![Cybersecurity](data:image/png;base64...)](https://thehackernews.uk/ai-cant-stop-d)

The Hacker News downloaded and inspected both. The MCP WebSocket route is present, the handler takes the command to run straight from the request, and it does not authenticate the caller. Neither build has been yanked.

pip does not install pre-releases unless you pass --pre or pin the version, so a plain install was never exposed. Anyone who installed one of those pre-releases was. There is still no PyPI build carrying the main-branch hardening for them; the fixed code is in GitHub main at commit b047730.

## How the chain works

AutoJack chains three weaknesses in the MCP WebSocket.

First, the socket trusted localhost, a check meant to block a normal browser pointed at a malicious site. But a browsing agent running on the same box is localhost, so anything it loads inherits that localhost identity and passes the check.

[![](data:image/png;base64...)](https://blogger.googleusercontent.com/img/b/R29vZ2xl/AVvXsEgHo9f5FXl4JHSkSIFVYXHarmPXZnSRlKEGb8flHrOIzrHOszL4kCTg9mos8YXZJge1xuRq4qB07I2rEmYp2sFwcryObZHuIK23EdNM9y5AZkgNNr-KW22x32TqP8cyrZ5JpHm5vr40rA6D64PnwxEMZ0607rSdFENs4gl9lIOB242dR2xg4hM-JEOsecXD/s1700-e365/ms.jpg)

Second, the authentication middleware skipped MCP paths on the assumption that the handler would verify tokens itself. It never did, so the socket accepted unauthenticated connections regardless of the configured auth mode.

Third, the endpoint took a command straight from a request parameter and ran it, with no allowlist on which executable could launch.

Put together, a page on the open internet, rendered by a local agent, could run an attacker-chosen command under the account running AutoGen Studio.

Microsoft describes this as research, not an active campaign, and reported no exploitation in the wild. The proof of concept used a "Web Content Summarizer" agent that, when fed an attacker URL, pops calc.exe on the developer's desktop, launched by the AutoGen Studio process.

[![](data:image/png;base64...)](https://blogger.googleusercontent.com/img/b/R29vZ2xl/AVvXsEjLrWAEfBZzy2ix4MfiP-yAkqP37HMBNt_3J8GKwn6m0mZVlDqifnsgPDqGpM_v7Hub6-sneXzexG8q_XevApYwSezKYcStEuKb1E5Dlw4lTAKEdivTvlXcxPrPkGOF6ej5e1qwKBm8Vy-Au-gsoJHlqhzo5YvXR4o7xITsXu7jfvwTK2NhFvJ0f4KCMg3-/s1700-e365/WebSocket.jpg)

Microsoft reported the behavior to the Microsoft Security Response Center, and the maintainers hardened the main branch in [commit b047730](https://github.com/microsoft/autogen/commit/b0477309d2a0baf489aa256646e41e513ab3bfe8) (PR #7362). The fixed handler no longer reads the command from the URL; parameters are stored server-side behind a one-time session ID, and unknown IDs are refused. MCP routes now run through the normal authentication path. That hardening has not landed in a PyPI release yet.

## What to do

A plain pip install autogenstudio gives you 0.4.2.2, which has no MCP route, so you are not affected.

If you installed a pre-release, you have the vulnerable handler and no patched PyPI build to move to. Pull from GitHub main at or after commit b047730. That is the real fix.

[![Cybersecurity](data:image/png;base64...)](https://thehackernews.uk/vpn-threat-report-m)

Until there is a release, separate the pieces the attack needs. Do not run AutoGen Studio on the same machine as a browsing or code-execution agent that touches untrusted content, because the chain only works when both share the same localhost. If they have to run together, isolate them in separate containers or VMs and run AutoGen Studio under a low-privilege account.

The AutoGen Studio bugs are patched in the source. The pattern is not. Microsoft expects the same shape in other agent frameworks: a local service with too much power, a localhost check treated as security, and an agent that opens untrusted pages.

THN saw it last month in [ChatGPhish](https://thehackernews.com/2026/05/chatgphish-vulnerability-turns-chatgpt.html), where ChatGPT's page summaries became a phishing vector. Microsoft made a similar localhost argument in its [Semantic Kernel RCE research](https://www.microso...