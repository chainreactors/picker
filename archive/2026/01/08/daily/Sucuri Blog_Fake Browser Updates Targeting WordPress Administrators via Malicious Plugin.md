---
title: Fake Browser Updates Targeting WordPress Administrators via Malicious Plugin
url: https://blog.sucuri.net/2026/01/fake-browser-updates-targeting-wordpress-administrators-via-malicious-plugin.html
source: Sucuri Blog
date: 2026-01-08
fetch_date: 2026-01-09T03:30:33.994737
---

# Fake Browser Updates Targeting WordPress Administrators via Malicious Plugin

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

* [Security Advisory](https://blog.sucuri.net/category/security-advisory)
* [Website Malware Infections](https://blog.sucuri.net/category/website-malware-infections)
* [WordPress Security](https://blog.sucuri.net/category/wordpress-security)

# Fake Browser Updates Targeting WordPress Administrators via Malicious Plugin

[![](https://secure.gravatar.com/avatar/3bb7fb42c6bf04c758d570c2f6bb217266c127e77766dc9d8e6754f15cdd5867?s=60&d=mm&r=g)](https://blog.sucuri.net/author/puja-srivastava)

[Puja Srivastava](https://blog.sucuri.net/author/puja-srivastava)

* January 7, 2026

![Fake Browser Updates Targeting WordPress Administrators via Malicious Plugin](https://blog.sucuri.net/wp-content/uploads/2026/01/Fake-Browser-Updates-Targeting-WordPress-Administrators-via-Malicious-Plugin-820x385.png)

We recently investigated a case involving a WordPress website where a customer reported persistent fake pop-up notifications appearing on their site. The warnings were urging them to update their browser (Chrome or Firefox), even though their software was already fully up-to-date.

What made this case particularly unique was the targeting. The fake alerts were not visible to regular visitors on the public-facing site. They only appeared when the site owner was logged into the wp-admin dashboard.

## What We Observed

During our investigation, we found a malicious plugin named Modern Recent Posts, pretending to be a harmless widget plugin. In reality, it downloaded and executed remote JavaScript from an external domain.

We have seen waves of similar social engineering attacks in the past, like [fake Java updates](https://blog.sucuri.net/2025/05/fake-java-update-popup-found-in-malicious-wordpress-plugin.html), [fake Cloudflare CAPTCHAs](https://blog.sucuri.net/2025/05/another-fake-cloudflare-verification-targets-wordpress-sites.html), and Windows system alerts. However, this new campaign targeting wp-admin users is utilizing a malicious plugin to hide in plain sight.

![fake browser update warning](https://blog.sucuri.net/wp-content/uploads/2026/01/fake-browser-update-warning.png)

The malicious domain backing this campaign, **persistancejs**[**.**]**store**, is currently detected on [28 websites](https://publicwww.com/websites/%22persistancejs.store%22/), suggesting this is an active and emerging threat.

## Compromise Indicators

The infection leaves behind several clear signs.

* A plugin named “Modern Recent Posts” was installed without the owner’s knowledge.
* Malicious script injection inside admin pages.
* The most important IoC is the domain used to fetch malicious JavaScript: hxxps://persistancejs[.]store/jsplug/plugin[.]php

## Analysis of the Malware

Below is a technical breakdown of the malicious behavior inside the fake plugin.

### 1. Targeted Delivery System

The malware is designed to be stealthy. It does not want to waste its payload on bots, crawlers, or non-Windows users (who cannot run the .exe file it drops).

It uses a specific function **is\_windows\_ua** to check the visitor’s User-Agent string. It explicitly looks for “Windows,” “Win32,” or “Win64.”

![function checking user-agent string](https://blog.sucuri.net/wp-content/uploads/2026/01/function-checking-user-agent-string.png)

The injection logic then combines this check with WordPress permissions. It ensures the payload only fires if:

1. The user is **an administrator** (current\_user\_can(‘manage\_options’)).
2. The user is **currently on the dashboard** (is\_admin()).
3. The user is on a **Windows machine**.

If these conditions are met, it executes a Base64 encoded JavaScript payload.

![payload executed](https://blog.sucuri.net/wp-content/uploads/2026/01/payload-executed.png)

### 2. Remote Payload Download from external domain

This is the most important malicious function in the plugin. The plugin sends the following information to the attacker:

* Site hostname
* Admin username

It then downloads a base64-encoded JavaScript payload from the attacker’s server. The plugin injects this script into the admin dashboard. Whatever the attacker provides will run inside the browser with admin privileges.

This is exactly how the fake browser update pop-ups are displayed.

![Remote Payload Download from external domain](https://blog.sucuri.net/wp-content/uploads/2026/01/Remote-Payload-Download-from-external-domain.png)

### 3. The Fake Java Update Payload

The script also generates a fake Java update pop-up. It is designed to appear authentic and urgent.

Once decoded by the browser, the script injects a high-priority overlay that blocks the screen. It uses classic social engineering language, warning of a “Critical Java Update Required” and claiming the environment is “severely outdated” to prevent “s...