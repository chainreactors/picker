---
title: Joomla SEO Spam Injector: Obfuscated PHP Backdoor Hijacking Site Visitors
url: https://blog.sucuri.net/2026/04/joomla-seo-spam-injector-obfuscated-php-backdoor-hijacking-site-visitors.html
source: Over Security - Cybersecurity news aggregator
date: 2026-04-16
fetch_date: 2026-04-17T04:50:42.388064
---

# Joomla SEO Spam Injector: Obfuscated PHP Backdoor Hijacking Site Visitors

[![Sucuri Blog](https://blog.sucuri.net/wp-content/uploads/2023/04/Sucuri_Blog_Header_Logo_342x60.png)](https://blog.sucuri.net/)

* Products
  + [Website Security Platform](https://sucuri.net/website-security-platform/)
  + [Website Firewall (WAF)](https://sucuri.net/website-firewall/)
  + [Multi-Site plans](https://sucuri.net/custom/agency/)
  + [Custom & Enterprise Plans](https://sucuri.net/custom/enterprise/)
  + [Partnerships](https://sucuri.net/partners/)
* Features
  + [Detection  Website Monitoring & Alerts](https://sucuri.net/malware-detection-scanning/)
  + [Protection  Future Website Hacks](https://sucuri.net/website-hack-protection/)
  + [Performance  Speed Up Your Website](https://sucuri.net/website-performance/)
  + [Response  Help For Hacked Websites](https://sucuri.net/website-malware-removal/)
  + [Backups  Disaster Recovery Plan](https://sucuri.net/website-backups/)
* Resources
  + [Guides](https://sucuri.net/guides/)
  + [Webinars](https://sucuri.net/webinars/)
  + [Infographics](https://sucuri.net/infographics/)
  + [Blog](/)
  + [SiteCheck](https://sitecheck.sucuri.net/)
  + [Reports](https://sucuri.net/reports/)
  + [Email Courses](https://sucuri.net/email-courses/)
* [Pricing](https://sucuri.net/website-security-platform/signup)
* [Immediate Help](https://sucuri.net/website-security-platform/help-now/)
* [Login](https://sucuri.net/website-security-platform/signup/)

[![Sucuri Blog](https://blog.sucuri.net/wp-content/uploads/2023/04/Sucuri_Blog_Header_Logo_342x60.png)](https://blog.sucuri.net/)

* Products
  + [Website Security Platform](https://sucuri.net/website-security-platform/)
  + [Website Firewall (WAF)](https://sucuri.net/website-firewall/)
  + [Multi-Site plans](https://sucuri.net/custom/agency/)
  + [Custom & Enterprise Plans](https://sucuri.net/custom/enterprise/)
  + [Partnerships](https://sucuri.net/partners/)
* Features
  + [Detection  Website Monitoring & Alerts](https://sucuri.net/malware-detection-scanning/)
  + [Protection  Future Website Hacks](https://sucuri.net/website-hack-protection/)
  + [Performance  Speed Up Your Website](https://sucuri.net/website-performance/)
  + [Response  Help For Hacked Websites](https://sucuri.net/website-malware-removal/)
  + [Backups  Disaster Recovery Plan](https://sucuri.net/website-backups/)
* Resources
  + [Guides](https://sucuri.net/guides/)
  + [Webinars](https://sucuri.net/webinars/)
  + [Infographics](https://sucuri.net/infographics/)
  + [Blog](/)
  + [SiteCheck](https://sitecheck.sucuri.net/)
  + [Reports](https://sucuri.net/reports/)
  + [Email Courses](https://sucuri.net/email-courses/)
* [Pricing](https://sucuri.net/website-security-platform/signup)
* [Immediate Help](https://sucuri.net/website-security-platform/help-now/)
* [Login](https://sucuri.net/website-security-platform/signup/)

* [Immediate Help](https://sucuri.net/website-security-platform/help-now/)

[Login](https://dashboard.sucuri.net/login/)

[Login](https://dashboard.sucuri.net/login)

New Customer?

[Sign up now.](https://sucuri.net/website-security-platform/signup/)

* [Submit a ticket](https://support.sucuri.net/support/?new)
* [Knowledge base](https://docs.sucuri.net/)
* [Chat now](https://sucuri.net/live-chat/)

Search for:

Search

* [Joomla Security](https://blog.sucuri.net/category/joomla-security)
* [Security Advisory](https://blog.sucuri.net/category/security-advisory)
* [Website Malware Infections](https://blog.sucuri.net/category/website-malware-infections)

# Joomla SEO Spam Injector: Obfuscated PHP Backdoor Hijacking Site Visitors

[![](https://secure.gravatar.com/avatar/3bb7fb42c6bf04c758d570c2f6bb217266c127e77766dc9d8e6754f15cdd5867?s=60&d=mm&r=g)](https://blog.sucuri.net/author/puja-srivastava)

[Puja Srivastava](https://blog.sucuri.net/author/puja-srivastava)

* April 16, 2026

![Joomla SEO Spam Injector: Obfuscated PHP Backdoor Hijacking Site Visitors](https://blog.sucuri.net/wp-content/uploads/2026/04/Obfuscated-PHP-Backdoor-Hijacking-Site-Visitors-820x385.png)

## Overview

During a recent malware cleanup investigation, we encountered a compromised Joomla website where the site owner reported a strange issue. Their website displayed a large number of suspicious product links that had nothing to do with their business. These products were not added by the website owner and did not exist in their catalog.

Visitors and search engines were seeing pages that promoted unrelated products, raising immediate concerns about spam injection or remote content manipulation.

SEO spam is one of the most common types of website infections we handle at Sucuri. Attackers inject malicious code that silently serves spam content to visitors and search engines, all without the site owner knowing. The goal is simple: abuse the site’s reputation to push traffic towards products the attacker wants to promote.

## What Did We Find?

When we inspected the site, we found a block of heavily obfuscated PHP code injected at the very top of the site’s `index.php` file.

Underneath the obfuscation, the malware was doing three things:

* Contacting external command-and-control (C2) servers
* Receiving instructions
* Redirecting visitors or injecting spam content accordingly.

## What Was New This Time?

One interesting aspect of this infection is that the malware itself does not directly include the spam content linked to the suspicious product listings reported by the site owner.

Instead, the script acts as a remote loader. It contacts an external server, sends information about the infected website, and waits for instructions. The response from the remote server determines what content the infected site should serve.

This approach allows attackers to change the behavior of the compromised website at any time without modifying the local files again. The attacker can inject spam product links, redirect visitors, or display malicious pages dynamically.

Another thing we noticed was that the strings are not stored as single base64 blobs. Instead, the code is broken into two-character strings that reassemble and execute perfectly at runtime. This helps avoid many signature-based scanners that look for a recognisable base64 string.

![code broken into two-character strings](https://blog.sucuri.net/wp-content/uploads/2026/04/code-broken-into-two-character-strings.png)

## Domains Involved in the Infection

Three domains appear in this malware. Two are active C2s. One is a dead decoy.

* **PRIMARY:** `cdn[.]erpsaz[.]com` – Primary C2
* **FALLBACK:** `cdn[.]saholerp[.]com` – Fallback C2, used automatically if the primary returns an empty response
* **Doesn’t return anything:** `lashowroom[.]com` – Decoded into the string table at `mpjy(25)` but never referenced by any index call that constructs a URL. Present in the code but was never used.

These domains appear inside the encoded payload and are used by the malware to retrieve instructions from attacker-controlled infrastructure.

When the infected website loads, the script tries to contact these domains and send details about the server environment. The response from these servers determines how the website behaves.

## Indicators of Compromise (IoC)

One of the main indicators in this case was the presence of heavily obfuscated PHP code injected at the top of the Joomla `index.php` file.

![heavily obfuscated PHP code](https://blog.sucuri.net/wp-content/uploads/2026/04/heavily-obfuscated-PHP-code.png)

Other indicators included suspicious outbound requests to external domains and the appearance of unrelated product links on the site. These links were not stored in the Joomla database, but were instead injected dynamically by the malicious loader script.

## Analysis of the Malware

The malware is structured across four PHP functions, each with a specific role. We walk through each one in full detail below.

### 1. `wffn()`: The Bootstrap Decoder

Everything in this malware depends on this tiny function. It exists purely to avoid writing the words explode and `b...