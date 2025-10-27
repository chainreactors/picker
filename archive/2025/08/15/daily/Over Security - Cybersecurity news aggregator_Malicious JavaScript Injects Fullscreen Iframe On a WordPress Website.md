---
title: Malicious JavaScript Injects Fullscreen Iframe On a WordPress Website
url: https://blog.sucuri.net/2025/08/malicious-javascript-injects-fullscreen-iframe-on-a-wordpress-website.html
source: Over Security - Cybersecurity news aggregator
date: 2025-08-15
fetch_date: 2025-10-07T00:50:08.255392
---

# Malicious JavaScript Injects Fullscreen Iframe On a WordPress Website

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

# Malicious JavaScript Injects Fullscreen Iframe On a WordPress Website

[![](https://secure.gravatar.com/avatar/3bb7fb42c6bf04c758d570c2f6bb217266c127e77766dc9d8e6754f15cdd5867?s=60&d=mm&r=g)](https://blog.sucuri.net/author/puja-srivastava)

[Puja Srivastava](https://blog.sucuri.net/author/puja-srivastava)

* August 13, 2025

![Malicious JavaScript Injects Fullscreen Iframe On a Wordpress Website](https://blog.sucuri.net/wp-content/uploads/2025/08/Malicious-JavaScript-Injects-Fullscreen-Iframe-On-a-Wordpress-Website-820x385.png)

Last month, we came across an ongoing JavaScript-based malware campaign affecting compromised websites. The malware injects a fullscreen iframe that silently loads content from a suspicious external domain.

This type of malicious script aims to force users to view unsolicited content, often for ad fraud, traffic generation, or deceptive social engineering.

This is the fake cloudflare captcha that was shown when we access the malicious domain **capcloud**[**.**]**icu**

![fake cloudflare captcha](https://blog.sucuri.net/wp-content/uploads/2025/08/fake-cloudflare-captcha.png)

## What did we find?

The script’s primary purpose was to infect systems by forcefully displaying a fullscreen iframe from a suspicious domain. The payload used advanced evasion techniques such as anti-debugging, function hijacking, and localStorage abuse to limit visibility and persist across page loads.

## Indicator of the Compromise

The infection was found embedded inside the WordPress `wp_options` database table, under the `option_name=wpcode_snippets`.

**WPCode** is a WordPress plugin used to safely add custom code like tracking scripts or PHP snippets without editing theme files. However, attackers abuse it to inject malicious code because it lets them run hidden scripts directly from the admin panel.

### Domains Involved and Blocklisted

#### **Capcloud**[**.**]**icu**

![SiteCheck](https://blog.sucuri.net/wp-content/uploads/2025/08/capcloud-sitecheck.png)

[SiteCheck](https://sitecheck.sucuri.net/results/Capcloud.icu)

  ![capcloud VirusTotal](https://blog.sucuri.net/wp-content/uploads/2025/08/capcloud-virustotal-scaled.png)

[VirusTotal](https://www.virustotal.com/gui/url/338a6e5f07c3d1596b893b845e85ee77ed2894b2304222c49cccb9482ae8e927?nocache=1)

#### **Wallpaper-engine**[**.**]**pro**

![wallpaper-engine SiteCheck](https://blog.sucuri.net/wp-content/uploads/2025/08/wallpaper-engine-sitecheck.png)

[SiteCheck](https://sitecheck.sucuri.net/results/Wallpaper-engine.pro)

  ![wallpaper-engine VirusTotal](https://blog.sucuri.net/wp-content/uploads/2025/08/wallpaper-engine-virustotal-scaled.png)

[VirusTotal](https://www.virustotal.com/gui/url/f2c896163c0dfdb4a32b49f13194b7a2de59848710bc3c0ae5c2babd5f13255d?nocache=1)

The malicious code is fully obfuscated, and when we deobfuscate them, we can see these domains:

![deobfuscated domains](https://blog.sucuri.net/wp-content/uploads/2025/08/deobfuscated-domains.png)

![deobfuscated domains 2](https://blog.sucuri.net/wp-content/uploads/2025/08/deobfuscated-domains-2.png)

### All malware-related domains at this IP address

These are all the domains that are connected to the same IP address, as posted by Sucuri Labs here: <https://labs.sucuri.net/details.php?domain=wallpaper-engine.pro>

* **wanderclean**[**.**]**com**
* **ampunshifu**[**.**]**org**
* **wallpaper-engine**[**.**]**pro**
* **cdnstat**[**.**]**net**
* **adoodlz**[**.**]**com**
* **secretdinosaurcult**[**.**]**com**
* **weathersnoop**[**.**]**com**

## Analysis of the Malware

### Anti-Debugging Routine and Console Override to Hide Logs

The script begins with a self-invoking function that installs anti-debugging measures using infinite loops and constructor abuse. The function calls are intended to break execution if a browser debugger is open, stalling reverse analysis attempts. Another notable tactic is the redefinition of native console methods to suppress output.

![redefinition of native console methods](https://blog.sucuri.net/wp-content/uploads/2025/08/redefinition-of-native-console-methods.png)

By replacing all console functions (like log, warn, error, etc.), the script hides runtime logs, making it harder for site owners or developers to catch the attack in action.

### Iframe Injection Based on User-Agent

The payload selectively targets Windows users using specific browsers. This ensures that the attack is more likely to succeed on popular platforms while minimizing suspicion from less targeted de...