---
title: One Paste to Rule Them All: Inside a ClickFix → EtherHiding → GULoader Intrusion
url: https://blog.sicuranext.com/one-paste-to-rule-them-all-inside-a-clickfix-etherhiding-guloader-intrusion/
source: Over Security
date: 2026-06-15
fetch_date: 2026-06-16T07:16:47.748980
---

# One Paste to Rule Them All: Inside a ClickFix → EtherHiding → GULoader Intrusion

[![Sicuranext Blog](https://blog.sicuranext.com/content/images/2026/03/sicuranext_h-accent-2.png)](https://blog.sicuranext.com)

* [Home](https://blog.sicuranext.com/)
* [WAAP](https://blog.sicuranext.com/tag/waap/)
* [SOC](https://blog.sicuranext.com/tag/soc/)
* [PWNPress](https://blog.sicuranext.com/tag/pwnpress/)
* [AI](https://blog.sicuranext.com/tag/ai/)

[Sign in](#/portal/signin)
[Subscribe](#/portal/signup)

# One Paste to Rule Them All: Inside a ClickFix → EtherHiding → GULoader Intrusion

#### [claudio bono](/author/claudio/), [Simone Fasolis](/author/simone-fasolis/)

15 Jun 2026
• 12 min read

[Share](#/share)

![One Paste to Rule Them All: Inside a ClickFix → EtherHiding → GULoader Intrusion](/content/images/size/w2000/2026/06/php-object-injection-ring.png)

A real-world ClickFix intrusion observed from both sandbox and endpoint telemetry, revealing the complete attack path from a compromised WordPress site to a blocked GULoader execution, including a full process creation call stack from the Windows Run dialog to the kernel.

---

## Preamble

In April 2026, we responded to an endpoint detection alert triggered by a **rundll32.exe** execution with anomalous arguments on a corporate workstation. The investigation traced the execution back to a compromised European small-business website that leveraged EtherHiding, a technique that stores malicious payloads in smart contracts on the BNB Smart Chain, to deliver a ClickFix social engineering lure. The user, believing they were completing a CAPTCHA verification, pasted and executed a command that attempted to load a remote DLL attributed to GULoader via a UNC path (a file path referencing a remote network share).

Elastic Defend's behavioral rule for **RunDLL32 with Unusual Arguments** killed the process in under 300 milliseconds, preventing GULoader from initializing.

This post details the full attack chain as reconstructed from two independent data sources: an ANY.RUN sandbox detonation of the compromised site and real-time EDR telemetry from the affected endpoint. The combination of these perspectives yields forensic details that neither source could produce alone, most notably a complete call stack proving that SmartScreen evaluated and allowed the execution, and sub-second timing between process creation and behavioral kill.

**Note**: The compromised site is a legitimate European small business, a victim, not a threat actor. Its identity has been redacted. All other indicators are defanged.

## Key takeaways

* The attack chain combines four distinct components, compromised WordPress, EtherHiding via BSC Testnet, ClickFix social engineering, and GULoader delivery via UNC path, into a single intrusion sequence where every traditional defensive layer has a structural reason to remain silent
* A full process creation call stack from **explorer.exe** through the Run dialog to `NtCreateUserProcess` demonstrates that SmartScreen evaluated and passed the execution, confirming the attack is entirely user-initiated with no exploit involved
* The compromised site implements platform-based filtering through its Traffic Direction System, serving the malicious payload exclusively to desktop Windows browsers, mobile inspection reveals a clean site
* User interview confirmed the social engineering loop: the victim followed the ClickFix prompt believing it was a legitimate reCAPTCHA challenge
* Behavioral detection on **rundll32.exe** with ordinal-based function call terminated the process before GULoader could execute, with no child processes, no network connections, and no evidence of data exfiltration

## Attack overview

The following table summarizes the intrusion timeline as observed through endpoint DNS logs and EDR telemetry.

![](https://blog.sicuranext.com/content/images/2026/04/data-src-image-c7328923-b0f0-4adc-8e73-6bc9e89d68bf.jpeg)

## Compromised WordPress site with ErrTraffic backdoor

**Domain:** [REDACTED] (European small-business website) **IP:** [REDACTED] (Hetzner, DE) **CMS:** WordPress 6.9.4

The site is a legitimate e-commerce website with an active WooCommerce storefront.
The victim reached the site independently via Google search, no phishing email or messages were involved.

The attacker injected malicious JavaScript while preserving all legitimate functionality: product pages, Google Maps integration, contact forms, and analytics continued to operate normally. This is consistent with the **ErrTraffic v3** framework documented by [LevelBlue SpiderLabs in April 2026](https://www.levelblue.com/blogs/spiderlabs-blog/err-hiding-and-seek-how-errtraffic-v3-leverages-etherhiding-in-clickfix-campaign?ref=blog.sicuranext.com), which deploys PHP backdoors in the WordPress mu-plugins directory to achieve persistence and inject obfuscated inline scripts using XOR and Base64 encoding.

Must-use plugins (a.k.a. mu-plugins) are Wordpress plugins installed in a special directory inside the content folder and which are automatically enabled on all sites in the installation. Must-use plugins do not show in the default list of plugins on the Plugins page of wp-admin (although they do appear in a special Must-Use section) and cannot be disabled except by removing the plugin file from the must-use directory.

The backdoor includes self-healing capabilities: it creates a hidden administrator account, force-installs a secondary plugin that reinstalls the primary backdoor if removed, and overwrites the passwords of common admin usernames (admin, root, wpsupport) with an attacker-controlled default. This means that even if the site owner discovers and deletes the mu-plugin file, the secondary plugin reinstalls it on the next request, and the attacker retains admin access through the hidden account.

With the backdoor active, the JavaScript injection does not require modifying theme files or core WordPress code. The mu-plugin registers two WordPress hooks, template\_redirect and wp\_footer, that execute on every public page load. These hooks append two <script> blocks to the HTML footer.

The first block is a tracking beacon. It collects visitor metadata (IP, User-Agent, referrer, browser, OS, screen resolution) and transmits it to external domains on cheap TLDs (.sbs, .cyou, .cfd, .icu) commonly associated with malvertising infrastructure. This beacon feeds the Traffic Direction System controlled by the attacker, which uses the collected data to decide whether the visitor should receive the malicious payload: it checks user-agent, virtualized environments and blocks debuggers or advanced inspection tools.

The second block is the ErrTraffic framework payload. It contains Base64-encoded data that is decoded through a routine applying a static XOR key, then converted back to executable JavaScript via `TextDecoder()`. This decoded JavaScript initiates the EtherHiding chain, the smart contract query, sandbox detection, victim deduplication, and ultimately the ClickFix overlay rendering.

The injected JavaScript is appended **after** the legitimate page content, not replacing it. Every WordPress function, WooCommerce product pages, contact forms, maps, analytic, continues to operate normally. The site owner checking from their phone sees a clean site. Google's crawler sees a clean site. Automated uptime monitors see a clean site. Only a desktop Windows browser visiting the page triggers the payload chain. This design makes detection exceptionally difficult without server-side file integrity monitoring or explicit inspection of the mu-plugins directory.

## EtherHiding: blockchain-based payload delivery

Two seconds after the page loaded, the injected JavaScript initiated outbound queries to the **BNB Smart Chain** (BSC) Testnet. The BSC Testnet (Chain ID 97) is a free-to-use Ethereum Virtual Machine-compatible blockchain. Smart contracts can be deployed and updated at zero cost, and their data is readable by anyone via public RPC endpoints using the eth\_call method without authentication.

The follow...