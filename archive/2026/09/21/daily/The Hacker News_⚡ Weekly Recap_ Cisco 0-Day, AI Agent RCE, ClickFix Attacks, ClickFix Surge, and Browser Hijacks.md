---
title: ⚡ Weekly Recap: Cisco 0-Day, AI Agent RCE, ClickFix Attacks, ClickFix Surge, and Browser Hijacks
url: https://thehackernews.com/2026/09/weekly-recap-cisco-0-day-ai-agent-rce.html
source: The Hacker News
date: 2026-09-21
fetch_date: 2026-09-22T07:05:19.679888
---

# ⚡ Weekly Recap: Cisco 0-Day, AI Agent RCE, ClickFix Attacks, ClickFix Surge, and Browser Hijacks

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

# [⚡ Weekly Recap: Cisco 0-Day, AI Agent RCE, ClickFix Attacks, ClickFix Surge, and Browser Hijacks](https://thehackernews.com/2026/09/weekly-recap-cisco-0-day-ai-agent-rce.html)

**Ravie Lakshmanan**Sep 21, 2026Cybersecurity News / Hacking

[![](data:image/png;base64...)](https://blogger.googleusercontent.com/img/b/R29vZ2xl/AVvXsEjovXeakmAmPG68i_kNoeGFJjwSSGDdpj-29aojemBxtTQVOHzR668zKtV5GGPhnJ0zyCEdlsNCc11LIT-F8n1U8Rkv3jr-3AAt6HC4YwwyfENs_Y8V-O_OlPC4_WByxrsUBq6NifTKHQpgWuSnIqnV4bg4rXVoe9BrtMtgRCo4ECfMLWHRIKOQsqjb0zEt/s1700-nu-rw-lo-l85-e365/recap-2.jpg)

A browser. A plugin. A package. A login screen. Normal stuff. That is basically the problem this week.

The trouble keeps showing up inside things people already trust: code that takes a bad turn, old payloads coming back, exposed systems, weak checks, fake fixes, and attack paths that look almost too easy. Even the research side is getting messy, with more findings, more automation, and not always more clarity.

Nothing here needs much drama. Just a lot of small doors left open. Here’s what happened.

## **⚡ Threat of the Week**

**[Cisco Warns of Actively Exploited ISE Auth Bypass](https://thehackernews.com/2026/09/cisco-warns-of-new-zero-day-ise-auth.html)** — Cisco warned of a fresh maximum-severity security flaw impacting Identity Services Engine (ISE) that has come under active exploitation. The vulnerability, tracked as CVE-2026-76460 (CVSS score: 10.0), could allow an unauthenticated, remote attacker to bypass authentication. "This vulnerability is due to insufficient authentication control on an API endpoint," Cisco said. "An attacker could exploit this vulnerability by sending a crafted request to an affected API endpoint. A successful exploit could allow the attacker to gain unauthorized access to the affected device by bypassing the web-based management interface."

[![OAuth and MCP Investigation Checklist](data:image/png;base64... "OAuth and MCP Investigation Checklist")

## Building Security Culture at Scale: Inside Southwest Airlines

Security awareness isn't enough anymore. Rachael Saffer talks with Hannah Hardee, Cybersecurity Analyst at Southwest Airlines, about shifting from training to culture change — and what it takes to make security stick across a large, complex organization.](https://thehackernews.uk/summit-validation)
[Register to Watch ➝](https://thehackernews.uk/summit-validation)

## **🔔 Top News**

* **[U.S. Seizes NightmareStresser Domains Linked to DDoS Attacks](https://thehackernews.com/2026/09/us-seizes-nightmarestresser-domains.html)** — A U.S. court-authorized operation seized two domains associated with NightmareStresser, which offered a distributed denial-of-service (DDoS)-for-hire service. NightmareStresser is assessed to have been used to launch hundreds of thousands of actual or attempted DDoS attacks against victims across the world since 2022. These attacks have targeted educational institutions, government agencies, gaming platforms, and millions of people, the U.S. Justice Department said.
* **[Using Claude to Hack OpenAI](https://thehackernews.com/2026/09/claude-opus-5-helped-researchers-take.html)** — Hacktron said it used Anthropic's Claude Opus 5 to chain two critical vulnerabilities – an SSO misconfiguration in OpenAI's identity infrastructure and a libheif RCE in the [Discourse community forum](https://community.openai.com/) ([CVE-2026-32882](https://github.com/discourse/discourse/security/advisories/GHSA-vhm9-85gw-x335)) – to gain unauthorized access to OpenAI employees' ChatGPT accounts and then use them to access internal OpenAI repositories. The issue was fixed 14 hours after responsible disclosure. Upstream, the flaw was fixed in [libheif 1.22.0](https://github.com/strukturag/libheif/releases/tag/v1.22.0) in May 2026.
* **[Plugin4Shell for 0-Click RCE in AI Coding Agents](https://thehackernews.com/2026/09/plugin4shell-lets-repository-owners.html)** — AIR Security demonstrated a flaw called Plugin4Shell, a zero-click remote code execution (RCE) vulnerability that bypasses SHA-pinning verification in four major AI coding agents: Claude Code, OpenAI Codex, GitHub Copilot, and Google Gemini CLI. "In this first-of-its-kind AI supply-chain attack, a trusted plugin is silently swapped for a malicious one and auto-installed past the agent's SHA pinning -- a flaw no marketplace can fix, so users must update their agent," AIR Security said. "It is a plugin SHA-pinning bypass: the agent checks out the exact commit the marketplace pinned but never verifies it landed there, so an attacker who controls the plugin's repo makes the checkout resolve to malicious code while the pin still looks honored. The result is zero-click remote code execution across Claude Code, Codex, GitHub Copilot, and Gemini CLI."
* **[OpenAI Reveals New Misalignment Incidents](https://thehackernews.com/2026/09/openai-reveals-six-model-incidents.html)** — OpenAI disclosed six new instances of "unexpected or concerning model behavior" that took place over the past six months, while sharing a new framework for reporting, tracking, investigating, and disclosing model misalignment in a bid to improve transparency. "As AI systems grow more advanced and more widely deployed, we need to build a broader and better-informed consensus on the progress of alignment research," OpenAI said. "We do not believe that the AI industry has solved alignment and monitoring to a sufficient degree to continue responsibly scaling at maximum speed for much longer."
* **[KREMLIN Banking Malware Hijacks Chrome and Edge for Credential Theft](https://thehackernews.com/2026/09/kremlin-banking-malware-hijacks-chrome.html)** — A previously undocumented Brazilian banking malware operation has been found to deliver a toolkit called KREMLIN. Active since at least May 2025, the threat actor has used lures that impersonate a dozen Brazilian banks and install a malicious browser extension on Google Chrome and Microsoft Edge. "The KREMLIN malware ecosystem ...