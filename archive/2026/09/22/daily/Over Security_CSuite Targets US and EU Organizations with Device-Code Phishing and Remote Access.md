---
title: CSuite Targets US and EU Organizations with Device-Code Phishing and Remote Access
url: https://any.run/cybersecurity-blog/csuite-attack-analysis/
source: Over Security
date: 2026-09-22
fetch_date: 2026-09-23T06:54:42.782973
---

# CSuite Targets US and EU Organizations with Device-Code Phishing and Remote Access

[![ANY.RUN's Cybersecurity Blog](https://any.run/cybersecurity-blog/wp-content/uploads/2026/02/anyrun-logo.svg)](https://any.run)
/
[BLOG](https://any.run/cybersecurity-blog/)

* [Guides and tutorials](https://any.run/cybersecurity-blog/guides/)
* [Research](https://any.run/cybersecurity-blog/research/)
* Categories
  + [Analyst Training](https://any.run/cybersecurity-blog/category/training/)
  + [Cybersecurity Lifehacks](https://any.run/cybersecurity-blog/category/lifehacks/)
  + [Instructions on ANY.RUN](https://any.run/cybersecurity-blog/category/instructions/)
  + [Interviews](https://any.run/cybersecurity-blog/category/interviews/)
  + [Malicious History](https://any.run/cybersecurity-blog/category/history/)
  + [Malware Analysis](https://any.run/cybersecurity-blog/category/malware-analysis/)
  + [News](https://any.run/cybersecurity-blog/category/news/)
  + [Service Updates](https://any.run/cybersecurity-blog/category/service-updates/)
* [Write for us](https://any.run/cybersecurity-blog/write-for-us/)
* [Go to service](https://app.any.run/)
* [Register for free](https://app.any.run/?register)
* [Register for free](https://app.any.run/?register)

* + Search

[![ANY.RUN's Cybersecurity Blog](https://any.run/cybersecurity-blog/wp-content/uploads/2026/02/anyrun-logo.svg)](https://any.run)
/
[BLOG](https://any.run/cybersecurity-blog/)

* [Guides and tutorials](https://any.run/cybersecurity-blog/guides/)
* [Research](https://any.run/cybersecurity-blog/research/)
* Categories
  + [Analyst Training](https://any.run/cybersecurity-blog/category/training/)
  + [Cybersecurity Lifehacks](https://any.run/cybersecurity-blog/category/lifehacks/)
  + [Instructions on ANY.RUN](https://any.run/cybersecurity-blog/category/instructions/)
  + [Interviews](https://any.run/cybersecurity-blog/category/interviews/)
  + [Malicious History](https://any.run/cybersecurity-blog/category/history/)
  + [Malware Analysis](https://any.run/cybersecurity-blog/category/malware-analysis/)
  + [News](https://any.run/cybersecurity-blog/category/news/)
  + [Service Updates](https://any.run/cybersecurity-blog/category/service-updates/)
* [Write for us](https://any.run/cybersecurity-blog/write-for-us/)
* [Go to service](https://app.any.run/)
* [Register for free](https://app.any.run/?register)
* [Register for free](https://app.any.run/?register)

* + Search

[![ANY.RUN's Cybersecurity Blog](https://any.run/cybersecurity-blog/wp-content/uploads/2026/02/anyrun-logo.svg)](https://any.run)
/
[BLOG](https://any.run/cybersecurity-blog/)

* + Search

![CSuite Targets US and EU Organizations with Device-Code Phishing and Remote Access](https://any.run/cybersecurity-blog/wp-content/uploads/2026/09/CSuite-scaled.png)

[Malware Analysis](https://any.run/cybersecurity-blog/category/malware-analysis/)

# CSuite Targets US and EU Organizations with Device-Code Phishing and Remote Access

September 22, 2026

[Add comment](#comments-23219)
2372 views
31 min read

[Home](https://any.run/cybersecurity-blog/)[Malware Analysis](https://any.run/cybersecurity-blog/category/malware-analysis/)

CSuite Targets US and EU Organizations with Device-Code Phishing and Remote Access

#### Recent posts

* [![](https://any.run/cybersecurity-blog/wp-content/uploads/2026/09/CSuite-1024x497.png)

  #### CSuite Targets US and EU Organizations with Device-Code Phishing and Remote Access

  2372
  0](https://any.run/cybersecurity-blog/csuite-attack-analysis/)
* [![](https://any.run/cybersecurity-blog/wp-content/uploads/2026/09/Make-Your-MSSPs-Value-Visible-1024x497.png)

  #### How MSSPs Can Prove Their Value When “Nothing Happened”

  7230
  0](https://any.run/cybersecurity-blog/how-mssps-prove-value/)
* [![](https://any.run/cybersecurity-blog/wp-content/uploads/2026/09/How_to_Buy_new-1024x497.png)

  #### Enterprise Threat Intelligence Buying Guide: How to Choose the Right Solution

  7946
  0](https://any.run/cybersecurity-blog/enterprise-threat-intelligence-guide/)

[Home](https://any.run/cybersecurity-blog/)[Malware Analysis](https://any.run/cybersecurity-blog/category/malware-analysis/)

CSuite Targets US and EU Organizations with Device-Code Phishing and Remote Access

[ANY.RUN](https://any.run/?utm_source=anyrunblog&utm_medium=article&utm_campaign=csuite-attack-analysis&utm_term=220926&utm_content=linktolanding) researchers investigated **CSuite**, a phishing and remote-access operation that combines credential theft, Microsoft 365 session hijacking, and the abuse of legitimate management tools. The campaign showed a strong US focus, with **60% of identified victim organizations based in the United States**.

By blending trusted business services with legitimate remote-access software, CSuite can give attackers both account and endpoint access while making malicious activity harder to distinguish from normal workflows.

Discover how the operation works, which tools and techniques it relies on, and what SOC teams should watch to detect related activity earlier.

## TL;DR

* **CSuite is a multi-stage phishing and remote-access operation targeting organizations across the US and Europe.** Its campaigns use Adobe, DocuSign, Zoom, SharePoint, Microsoft 365 voicemail, and other trusted business themes to reach victims.
* **The operation follows two main attack paths.** One delivers legitimate remote-management and endpoint-management tools such as ScreenConnect, Action1, Atera, Syncro, and PDQ Connect. The other steals credentials and Microsoft 365 sessions through phishing and device-code authentication flows.
* **US organizations make up the largest identified share.** 60% of identified victim organizations were US-based, while 51% of sandbox submissions came from the United States.
* **The campaign shows a significant scale.** ANY.RUN identified 351 related sandbox analyses across 170 hosts, while the CSuite panel contained 216 unique Chameleon victims, 29 captured Microsoft 365 sessions, 1,593 lure documents, and 15,955 harvested email addresses.
* **CSuite relies heavily on legitimate services and software.** Hijacked Adobe Document Cloud tenants, Cloudflare Workers, public code hosting, and legitimate management tools help the operation blend malicious activity with normal business infrastructure.
* **The strongest link between the campaigns is shared tooling and infrastructure.** Delivery pages, phishing panels, domains, operator accounts, and exfiltration channels connect the remote-access and credential-theft activity to the same CSuite operation.

## CSuite Threat Overview

![CSuite campaign in brief](https://any.run/cybersecurity-blog/wp-content/uploads/2026/09/CSuite-Campaign-in-Brief-1024x707.png)

*CSuite campaign in brief*

CSuite creates risk on both the identity and endpoint sides of the environment. A single campaign can lead to stolen Microsoft 365 access, compromised mailboxes, or direct remote control of employee devices.

| Attribute | Detail |
| --- | --- |
|  |  |
| --- | --- |
| Tracking name | CSuite, after the CSuite v1.1 panel at the centre of the operation |
| Structure | Infrastructure supplier with affiliates; the supplier hands out hosting, remote-desktop access and domains in private messaging channels, and each affiliate runs its own exfiltration endpoint |
| Motivation | Financial. Credential theft feeding manual mailbox access and business email compromise |
| Primary targets | Managed service providers, technology firms, government and administration, consulting, manufacturing, education and mortgage licensees, concentrated in the United States |
| Delivery | Adobe-themed download pages, plus DocuSign, Zoom, Google Meet and Dropbox lure lines |
| Payloads | Legitimate remote-management and device-management agents deployed as RATs — ScreenConnect, Action1, Atera, Syncro, PDQ Connect renamed to Adobe, Dotloop, DocuSign and others |
| Capture tooling | CSuite v1.1 phishing panel with 23 modules, a GSuitepanel, a per-affiliate worker view, an address validator, Cloudflare Worker proxies an...