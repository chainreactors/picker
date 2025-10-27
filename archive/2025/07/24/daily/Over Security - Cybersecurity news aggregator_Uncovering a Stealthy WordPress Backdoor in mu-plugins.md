---
title: Uncovering a Stealthy WordPress Backdoor in mu-plugins
url: https://blog.sucuri.net/2025/07/uncovering-a-stealthy-wordpress-backdoor-in-mu-plugins.html
source: Over Security - Cybersecurity news aggregator
date: 2025-07-24
fetch_date: 2025-10-06T23:54:51.124647
---

# Uncovering a Stealthy WordPress Backdoor in mu-plugins

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
* [WordPress Security](https://blog.sucuri.net/category/wordpress-security)

# Uncovering a Stealthy WordPress Backdoor in mu-plugins

[![](https://secure.gravatar.com/avatar/3bb7fb42c6bf04c758d570c2f6bb217266c127e77766dc9d8e6754f15cdd5867?s=60&d=mm&r=g)](https://blog.sucuri.net/author/puja-srivastava)

[Puja Srivastava](https://blog.sucuri.net/author/puja-srivastava)

* July 22, 2025

![Uncovering a Stealthy WordPress Backdoor in mu-plugins](https://blog.sucuri.net/wp-content/uploads/2025/07/Uncovering-a-Stealthy-WordPress-Backdoor-in-mu-plugins-820x385.png)

Recently, our team uncovered a particularly sneaky piece of malware tucked away in a place many WordPress users don’t even know exists: the mu-plugins folder. In fact, back in March, we saw a similar trend with hidden malware in this very directory, as detailed in our post [Hidden Malware Strikes Again: MU-Plugins Under Attack](https://blog.sucuri.net/2025/03/hidden-malware-strikes-again-mu-plugins-under-attack.html). This current infection was designed to be quiet, persistent, and very hard to spot.

```
./wp-content/mu-plugins/wp-index.php
```

For those unfamiliar, mu-plugins stands for **“must-use plugins.”** These are special WordPress plugins that are automatically activated and cannot be deactivated from the WordPress admin panel.

This script acts as a loader, silently fetching a remote payload from a **ROT13-obfuscated URL** and storing it in the database. The fetched content is then temporarily written to disk and executed. This [backdoor](https://blog.sucuri.net/tag/website-backdoor) gives the attacker persistent access to the site and the ability to run any PHP code remotely.

### What is ROT13 Obfuscation?

ROT13 is a simple obfuscation method that shifts each letter 13 places in the alphabet. Its legitimate use cases consist of things like obscuring spoiler text, jokes, or puzzle answers in online discussions without true encryption. It’s also used to hide text like URLs or code in malware. ROT13 is reversible and provides no real security.

Here’s a simple ROT13 example:

“**HelloWorld**” becomes “**UryybJbeyq**”

Each letter is rotated 13 places in the alphabet (**A**↔**N, B**↔**O, C**↔**P**, etc.).

## Indicator of Compromise

The attacker’s loader uses WordPress functions to execute its payload and achieve stealth. Here are some Indicators of Compromise (IoCs):

* **Malicious file:** `wp-content/mu-plugins/wp-index.php`
* **ROT13-encoded URL:** `str_rot13('uggcf://1870l4ee4l3q1x757673d.klm/peba.cuc')`
* **Decodes to:** `hxxps://1870y4rr4y3d1k757673q[.]xyz/cron.php`
* **Database option key used:** `_hdra_core`
* **Temporary payload path:** `.sess-[hash].php` inside the uploads directory
* **Hidden admin user:** `officialwp`

These indicators are critical for identifying if your WordPress site has been infected.

## Analysis of the Malware

### The Loader in wp-index.php

The malicious file wp-index.php located in the mu-plugins directory acts as the main entry point for this malware. Being in the mu-plugin directory, it is automatically loaded by WordPress and cannot be disabled via the admin dashboard. This is how the attacker achieves persistence.

The code begins by decoding a ROT13-obfuscated URL to access the remote payload:

![decoding obfuscated URL to access the remote payload](https://blog.sucuri.net/wp-content/uploads/2025/07/decoding-obfuscated-URL-to-access-the-remote-payload.png)

Once fetched, the payload is base64-encoded. The script checks whether the content is valid base64 before proceeding:

![payload base64-encoded and checked](https://blog.sucuri.net/wp-content/uploads/2025/07/payload-base64-encoded-and-checked.png)

The payload is saved in the WordPress options table under **\_hdra\_core**, providing a stealthy storage location that avoids filesystem detection. The script then decodes and executes the payload dynamically:

![hides itself and dynamically executes](https://blog.sucuri.net/wp-content/uploads/2025/07/hides-itself-and-dynamically-executes.png)

The payload is included and then deleted immediately, leaving little to no trace behind.

### The Remote Payload at cron.php

When we decoded the base64 payload from **hxxps://1870y4rr4y3d1k757673q**[**.**]**xyz/cron.php**, we found a complex malware framework.

We found a hidden file manager injected into the theme directory as **pricing-table-3.php**. It supports browsing, uploading, and deleting files. The access is gated using a custom HTTP header token:

![hidden file manager](https://blog.sucuri.net/wp-content/uploads/2025/07/hidden-file-manager.png)

The user **‘officialwp’** is created and granted administrator rights.

![admin user crea...