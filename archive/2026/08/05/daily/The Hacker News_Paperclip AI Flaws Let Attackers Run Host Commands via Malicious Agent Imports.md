---
title: Paperclip AI Flaws Let Attackers Run Host Commands via Malicious Agent Imports
url: https://thehackernews.com/2026/08/paperclip-ai-flaws-let-attackers-run.html
source: The Hacker News
date: 2026-08-05
fetch_date: 2026-08-06T05:02:51.429196
---

# Paperclip AI Flaws Let Attackers Run Host Commands via Malicious Agent Imports

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

![cybersecurity](data:image/svg+xml;base64...)

# [Paperclip AI Flaws Let Attackers Run Host Commands via Malicious Agent Imports](https://thehackernews.com/2026/08/paperclip-ai-flaws-let-attackers-run.html)

**Swati Khandelwal**Aug 05, 2026Vulnerability / Web Security

[![](data:image/png;base64...)](https://blogger.googleusercontent.com/img/b/R29vZ2xl/AVvXsEgnNyDWyCEMrA99LxVQMqKNr188rBBjKa6Kg3nHdjVLxWCCVgfqa0cChHo_JWbHgbSLHgZVpcgWn0kw0FUySWhScczQi6LNme-wY9rkUAxE-IvoFLvfum-zWxEnppDBu6bAHBO0ObN39kCDwSK4jnsqdCAOhCPGG0FtoLX_2vvCi2DcoWPmzGUk6Hs_gB4/s1700-e365/paperclipai.jpg)

Two security flaws in Paperclip could let attackers execute commands on a network server or a developer's computer. Paperclip is an open-source control plane for teams of artificial intelligence (AI) agents, and both paths rely on importing a malicious agent and starting it.

A third flaw could expose sensitive data and control-plane details through application programming interface (API) routes that did not enforce the expected access checks.

The more severe server-side path, tracked as **CVE-2026-41679** (CVSS score: 10.0), requires no pre-existing account or victim interaction against network-accessible deployments using authenticated mode with the default registration configuration.

The second path, tracked as **GHSA-x8hx-rhr2-9rf7** (CVSS score: 9.6), requires a user to open an attacker-controlled page while Paperclip is running in its default local\_trusted mode.

The source tagged as Paperclip v2026.416.0 contains the import-authorization fix and hostname-validation guard discussed below, although the DNS-rebinding advisory does not identify a patched version. Rapid7 has since shipped a public Metasploit module for CVE-2026-41679, and CISA's Stakeholder-Specific Vulnerability Categorization (SSVC) enrichment carried by NVD classifies exploitation as proof-of-concept.

No authoritative source reviewed by The Hacker News reported exploitation in the wild as of August 5, 2026. Operators should update to v2026.416.0 or later and review how registration and deployment exposure are configured.

[Oasis Security's analysis](https://www.oasis.security/blog/paperclip-agent-vulnerabilities), backed by a [17-page technical report](https://pages.oasis.security/rs/106-PZV-596/images/paperclip-agent-vulnerabilities-technical-report.pdf), connects the findings through one product property: agent configuration can become executable behavior. Paperclip's built-in process adapter intentionally launches a configured command as a child process of the server.

[![Cybersecurity](data:image/png;base64...)](https://thehackernews.uk/threatlocker-d)

The execution feature is legitimate. The vulnerabilities changed who could reach it and whose configuration the server would trust.

"Agent configuration must be treated as executable input," Oasis said.

Unauthorized users or [browser-originated requests](https://thehackernews.com/2026/06/autojack-attack-lets-one-web-page.html) could introduce and activate configuration that reached the launcher.

The server-side chain applies to network-accessible authenticated deployments using the vulnerable registration configuration. The localhost chain applies when a user opens an attacker-controlled page while Paperclip is running in its default local\_trusted configuration. Both end with attacker-controlled agent configuration reaching the host execution adapter.

## A Board Key Approved by Its Owner

The [attack against an internet-accessible instance](https://github.com/paperclipai/paperclip/security/advisories/GHSA-68qg-g8mg-6pr7) begins with Paperclip's default open-signup flow. An attacker can register without an invitation or verified email address, sign in, and enter the command-line interface authorization process. The same newly registered user could create a pending CLI challenge and approve it, activating a durable board API credential without a separate administrator making the decision.

That credential should not have been enough to create a top-level company. Paperclip required instance-administrator rights when a user created a company directly, but the equivalent new-company import route accepted board-level access.

An attacker could therefore supply a .paperclip.yaml bundle defining a new company, an agent using the process adapter, and the command that agent would run.

The import also made the attacker a member of the new company, so the normal wakeup check passed when the attacker started the agent. Paperclip then launched the command with the operating-system privileges of its server process.

The practical impact depends on the service account and host. Oasis said it could include application data, source repositories, locally stored credentials, secrets available to agent processes, and internal services reachable from the machine.

Paperclip fixed CVE-2026-41679 in v2026.416.0 by requiring instance-administrator access for imports targeting a new company and company access for imports targeting an existing one. The same check now protects both import preview and execution.

Open registration remains available, but a newly registered board user can no longer treat the new-company import route as an instance-administrator operation.

[Rapid7 published a Metasploit module](https://docs.rapid7.com/insight/release-notes-5.0.0-2026061601/) in June 2026 that automates the six-request CVE-2026-41679 attack chain. The [CISA-ADP enrichment carried by NVD](https://nvd.nist.gov/vuln/detail/CVE-2026-41679) marks the flaw as automatable, with total technical impact and proof-of-concept exploitation.

The vulnerability was not listed in [CISA's Known Exploited Vulnerabilities (KEV) catalog](https://www.cisa.gov/known-exploited-vulnerabilities-catalog) when The Hacker News checked it on August 5, 2026. Absence from KEV does not rule out exploitation.

## The Browser Crosses Into Localhost

The [second critical path](https://github.com/paperclipai/paperclip/security/advisories/GHSA-x8hx-rhr2-9rf7) targets a different deployment model. In its default local\_trusted configuration, Paperclip binds to the loopback interface and historically treated every request reaching the service as an implicit instance administrator. That removed authentication friction for local development, but it also treated network location as identity.

Oasis de...