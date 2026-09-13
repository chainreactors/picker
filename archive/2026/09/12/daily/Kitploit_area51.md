---
title: area51
url: https://kitploit.com/en/tools/github/thoropass-public/area51
source: Kitploit
date: 2026-09-12
fetch_date: 2026-09-13T07:01:27.330514
---

# area51

[Skip to content](#main-content)

[![Kitploit](/_next/image?url=%2Flogo.png&w=64&q=75)KITPLOIT](/en)[Tools](/en/tools)[Blog](/en/blog)Categories

EN

[Submit](/en/submit)

[Tools](/en/tools)[Blog](/en/blog)Categories

[Submit](/en/submit)

EN

Hacking, PenTest, and Cybersecurity Tools for Your Security Arsenal!

Kitploit is a directory of hacking, cybersecurity, and pentesting tools. Discover the latest project updates to find vulnerabilities, analyze systems, automate testing, and strengthen your security.

·Analytics preferences·[Feeds](/en/feeds)·[Contact](/en/contact)·[Privacy](/en/privacy)·© 2026 Kitploit

Tool Directory

## Categories

[View all categories](/en/categories)

Loading categories

[Tools](/en/tools)/![GitHub](/providers/github.png)GitHub/thoropass-public/area51

![](https://assets.kitploit.com/production/public/tools/54672/33a97defb3dc98446f1e085f0b29944b5860c94d8cb803c2d0732c0d88946679-display-v1.webp)

[Exploitation](/en/categories/exploitation)[Web Application Exploitation](/en/categories/web-application-exploitation)[API Security Testing](/en/categories/api-security-testing)[Information Gathering](/en/categories/information-gathering)[Penetration Testing](/en/categories/penetration-testing)[Cloud Security](/en/categories/cloud-security)[Email Security](/en/categories/email-security)

![GitHub](/providers/github.png)thoropass-public/area51

# area51

The exploit server for out-of-band findings. Point a target at a domain you own. Every HTTP request and every email it sends back lands in a dashboard you control, and it gets whatever response you choose in return.

[View Repository](https://github.com/thoropass-public/area51)

3283 days ago![Not yet reviewed](/_next/image?url=%2Fbadges%2Fkitploit_badge_not_reviewed_full.png&w=48&q=75)

### Most Popular

[View all →](/en/tools)

Discover the most used tools by our community.

Last 7 DaysLast 30 Days

Explore all tools

Browse our collection of tools

[View all tools →](/en/tools)

Share

![AREA 51 exploit server](https://assets.kitploit.com/production/public/readmes/54672/48232f8a9c059da9a8343e515b39024bacb2bcb9b56d9ab1ea0f5e66854a8683/e49d14eb4965ad8ca13e5f2069b5d0cd16a2bdb40970548c9b10425b43448075-display-v1.webp)
[![by Thoropass](https://assets.kitploit.com/production/public/readmes/54672/f26300db672149ff6a335dbef974fd4615112782c7a653fc4ef463eba02f6deb/f10a81bca500b530dc3844afc99be3908b6f79aa8a1e5386ef6bb5c88eaae6e1-display-v1.webp)](https://thoropass.com)

### Every callback, captured.

**The exploit server for out-of-band findings.** Point a target at a domain you
own. Every HTTP request and every email it sends back lands in a dashboard you
control, and it gets whatever response you choose in return.

[![License](https://img.shields.io/badge/license-Apache--2.0-88C0D0?style=flat-square)](LICENSE)
[![Runs on Cloudflare](https://img.shields.io/badge/runs_on-Cloudflare-D08770?style=flat-square&logo=cloudflare&logoColor=white)](docs/internals/architecture.md)
[![Node](https://img.shields.io/badge/node-20+-88C0D0?style=flat-square)](#requirements)
[![MCP](https://img.shields.io/badge/MCP-agent_ready-8FBCBB?style=flat-square)](docs/internals/autopilot.md)

[Getting started](https://github.com/thoropass-public/area51/blob/main/docs/guides/getting-started.md) ·
[Playbooks](https://github.com/thoropass-public/area51/blob/main/docs/guides/usage.md) ·
 ·
 ·

[CLI](https://github.com/thoropass-public/area51/blob/main/docs/reference/cli.md)

[Architecture](https://github.com/thoropass-public/area51/blob/main/docs/internals/architecture.md)

[Documentation](https://github.com/thoropass-public/area51/blob/main/docs/README.md)

> ⚠️ **For authorized security testing and research only.** A black hole is a
> live, internet-reachable catch-all: everything a target sends it is stored, and
> it serves back whatever you configure. Only point targets you have **explicit,
> written authorization** to test at it, and treat every deployment as
> client-data storage. Test only what you are authorized to test.

---

## Why it exists

Half of what you find on an engagement only proves itself when something calls
home. A blind SSRF. An XXE that exfiltrates over HTTP. A stored XSS firing in an
admin's browser you will never see. A password-reset flow you need to read. An
OAuth `redirect_uri` nobody validated. Each one needs infrastructure that is
reachable from the target, captures everything, and answers exactly how you want.

Public interaction services give you a hostname and a log. AREA 51 gives you the
whole thing, on infrastructure you own:

* **Nothing shared.** Your domains, your storage, your captures. No third party
  holds your clients' tokens, reset links or internal hostnames.
* **Any response you like.** A `302` into a metadata endpoint, a DTD, a `.js`
  beacon, a JSON stub, a 25 MB binary. Per exact path.
* **Email is a first-class capture.** Every address at the domain is live, and
  every message is kept verbatim, headers and attachments included.
* **Your agent can drive it.** An MCP server exposes recent captures and a
  sandboxed slice of the endpoint table, so an AI agent can inject a callback URL
  and confirm the hit without you in the loop.
* **One command to stand up, one to tear down.** No servers, no containers, no
  cron host, and no bill at pentest volumes.

> **Released early, on purpose.** AREA 51 began as an internal tool for a small,
> trusted team, so it favors simplicity over hardening and scale. Expect rough
> edges. If you hit one, [open an issue](https://github.com/thoropass-public/area51/issues)
> with repro steps. Contributions are welcome; see [CONTRIBUTING.md](https://github.com/thoropass-public/area51/blob/main/CONTRIBUTING.md).

## The three pieces

|  |  |  |
| --- | --- | --- |
| **AREA 51** · the dashboard  Configure endpoints, read captured requests and email, manage noise filters. Locked behind single sign-on with an emailed one-time PIN. | **Black Holes** · your domains  Every path serves what you defined, and every request and every address at the domain is captured. Public by necessity, because targets have to reach it. | **Autopilot** · the agent interface  A key-authenticated MCP + REST server. Reads the last hour of callbacks, stages its own response stubs, and cannot touch anything else. |

### Drive it from an agent 🆕

Cool and easy: **Autopilot** exposes an MCP server (with a REST mirror) so an
authorized AI agent can run the loop itself mid-engagement, without you in the
middle of it. It reads the last hour of callbacks, stages its own response stub
under the fenced `/-/*` namespace, and confirms the hit. Every operator gets
their own API key, and it is sandboxed: it can never read your files, or any
endpoint outside `/-/`. → [Autopilot internals](https://github.com/thoropass-public/area51/blob/main/docs/internals/autopilot.md)

## What it looks like

|  |  |
| --- | --- |
| ![AREA 51 Home](https://assets.kitploit.com/production/public/readmes/54672/7515e219878f1c1189ff8620dd299c870bba0daf04a1293e69dfe09e799c4baf/12e8cf9e3f5f2562d71fe065aec6a6246285c9d1cda3ee73194e4f8f669539d7-display-v1.webp) | ![Endpoints](https://assets.kitploit.com/production/public/readmes/54672/b48384662069e55e0f3c6466b77b5ae9ef6f78914226814f0678d94589a8e755/25bd7d9d53fdd6e0863e2e584b2ff847ebd103d17de5f2cabce74e62e03ef7c9-display-v1.webp) |
| ![Captured requests](https://assets.kitploit.com/production/public/readmes/54672/7761116c6d38c264ceb7cd98eaa8ea5f96c31cdff486fb3432d0ce3ffb170305/451ce004acc01a8746a1587e53772564be7393b39d77976a7134be676d6b0890-display-v1.webp) | ![Captured email](https://assets.kitploit.com/production/public/readmes/54672/553b815155600d238851f54bf7b2f42f8ed9d8010b47fdf83d42c1ca84ec2f3f/64b27f2f05121eb5e9d324698321ac8296eae9b28551d2e66fbfa2d9f54b4bcb-display-v1.webp) |

## What you can do with it

| Finding | How AREA 51 proves it | Playbook |
| --- | --- | --- |
| Blind SSRF | An unconfigured path already captures the hit, with egress IP, User-Agent a...