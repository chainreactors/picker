---
title: Fake WordPress Plugin Impacts SEO by Injecting Casino Spam
url: https://blog.sucuri.net/2025/02/fake-wordpress-plugin-impacts-seo-by-injecting-casino-spam.html
source: Over Security - Cybersecurity news aggregator
date: 2025-02-27
fetch_date: 2025-10-06T20:37:21.985924
---

# Fake WordPress Plugin Impacts SEO by Injecting Casino Spam

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

# Fake WordPress Plugin Impacts SEO by Injecting Casino Spam

[![](https://secure.gravatar.com/avatar/da934b974fa8adb3975fd07757f8322b04202cc98f15a625259eb3b404c1532a?s=60&d=mm&r=g)](https://blog.sucuri.net/author/kayleigh)

[Kayleigh Martin](https://blog.sucuri.net/author/kayleigh)

* February 26, 2025

![Fake WordPress plugin impacts SEO by injecting casino spam](https://blog.sucuri.net/wp-content/uploads/2025/02/Fake-WordPress-plugin-impacts-SEO-by-injecting-casino-spam-820x385.png)

Injecting malware via a fake WordPress plugin has been a common tactic of attackers for some time. This clever method is often used to bypass detection as attackers exploit the fact that plugins are not part of the core files of a WordPress site, making integrity checks more difficult. Attackers often hide the malicious plugin from the WordPress dashboard as well, which can make them harder to track down. Additionally, when creating fake malicious plugins, attackers give the plugin an innocent sounding name so the directory is easily overlooked.

In recent days, we came across a client impacted by casino spam being injected into the footer of their website. A sample of this casino spam can be found below:

![casino spam sample](https://blog.sucuri.net/wp-content/uploads/2025/02/casino-spam-sample.png)

After a lengthy investigation, we determined a fake plugin was causing this spam injection, disguising itself as an innocent sounding plugin. The attackers used multiple stealthy methods to evade detection: naming the plugin an innocent sounding name, and hiding it in the WordPress plugins directory versus a core file to avoid being found by integrity checks.

Let’s take a look at the malicious code more in depth.

## Finding the fake plugin

We start by navigating to the **wp-content/plugins** directory and review the plugins there. To provide a visual example, below is a WordPress testing environment that shows a list of plugins:

![WP plugin list](https://blog.sucuri.net/wp-content/uploads/2025/02/wp-plugin-list.png)

At first glance, these plugins appear to be normal. This example list of plugins is relatively short, so going through them one by one wouldn’t be too difficult to narrow down the malicious one. However, a key clue can help us find the malicious plugin faster – by weeding out the commonly used plugins first and reviewing the ones that aren’t immediately recognizable. This helps us narrow down the outlier quickly because in this particular example, all plugins except for one are popular plugins used in many sites. This isn’t so easy with a WordPress site with many plugins and/or custom plugins that we may not see as often. That being said, after weeding out the common plugins, that leaves us with one:

![WP plugin list refined](https://blog.sucuri.net/wp-content/uploads/2025/02/wp-plugin-list-refined.png)

Would you look at that! This plugin name doesn’t appear to be related to a commonly used plugin, so we better take a look. Let’s look at the contents of the **wp-content/plugins/security-wordpress** directory to review further. Here’s what’s inside:

![security-wordpress directory](https://blog.sucuri.net/wp-content/uploads/2025/02/security-wordpress-directory-600x100.png)

That’s strange. Normally WordPress plugins have more than one file. This is another clue that this plugin is indeed fake. After opening the contents of the **security-wordpress.php** file, we can see this first chunk of code:

![security-wordpress file contents](https://blog.sucuri.net/wp-content/uploads/2025/02/security-wordpress-file-contents.png)

Followed by the rest:

![security-wordpress file contents 2](https://blog.sucuri.net/wp-content/uploads/2025/02/security-wordpress-file-contents-2.png)

There are multiple clues in this piece of code that set off red flags, like the usage of obfuscation and **cURL**. Now that we’ve likely found our culprit, let’s figure out what it is doing.

## Fake plugin in action

This malware sample is contained within one file, which makes interpreting it straight forward, as all necessary functions are in one place.

Reviewing the code shown in the first screenshot above, the malware first uses the **xor\_decrypt()** function to decrypt a string using **XOR encryption** with a provided key. (Lines 13-19).

![decrypt with XOR encryption](https://blog.sucuri.net/wp-content/uploads/2025/02/decrypt-with-xor-encryption.png)

Second, it uses **cURL** to fetch data from a remote URL. (Lines 22-37).

![cURL data fetch from remote...