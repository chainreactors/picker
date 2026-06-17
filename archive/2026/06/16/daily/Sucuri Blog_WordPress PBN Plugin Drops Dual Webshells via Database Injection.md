---
title: WordPress PBN Plugin Drops Dual Webshells via Database Injection
url: https://blog.sucuri.net/2026/06/wordpress-pbn-plugin-drops-dual-webshells-via-database-injection.html
source: Sucuri Blog
date: 2026-06-16
fetch_date: 2026-06-17T07:02:17.423721
---

# WordPress PBN Plugin Drops Dual Webshells via Database Injection

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

# WordPress PBN Plugin Drops Dual Webshells via Database Injection

[![](https://secure.gravatar.com/avatar/3bb7fb42c6bf04c758d570c2f6bb217266c127e77766dc9d8e6754f15cdd5867?s=60&d=mm&r=g)](https://blog.sucuri.net/author/puja-srivastava)

[Puja Srivastava](https://blog.sucuri.net/author/puja-srivastava)

* June 16, 2026

![WordPress PBN Plugin Drops Dual Webshells via Database Injection](https://blog.sucuri.net/wp-content/uploads/2026/06/WordPress-PBN-Plugin-Drops-Dual-Webshells-via-Database-Injection-820x385.png)

During a recent incident response engagement, our team uncovered a multi-stage WordPress infection that goes beyond the usual file-based malware. The attacker combined a fake plugin, a remote command-and-control server, and two PHP web shells stored directly inside the WordPress database.

The campaign is operated by a Turkish-speaking threat actor and is built around a classic SEO monetization scheme: hidden backlink injection for a **Private Blog Network (PBN)**, most likely tied to the gambling and adult affiliate niche.

In this post, we walk through every component of the infection, the techniques used to stay hidden, and how site owners can detect and remove it.

## What did we discover?

The site was showing spam content. We found three distinct malicious components working together on the compromised website.

The first was a fake WordPress plugin named “Beloved PBN Entegrasyonu” installed at **`./wp-content/plugins/beloved-pbn/beloved-pbn.php`**.

![Fake plugin - Beloved PBN Entegrasyonu](https://blog.sucuri.net/wp-content/uploads/2026/06/Fake-plugin-Beloved-PBN-Entegrasyonu.png)

This plugin silently beaconed the site’s URL to an external API on every page load and injected whatever HTML or JavaScript the server returned directly into the page footer. The classic PBN link injection model used to manipulate search engine rankings across a network of compromised sites.

The second and third components were two PHP webshells stored as raw executable PHP code inside `wp_posts` database records. These were injected directly into the database and served as live scripts through a mechanism that allowed the attacker to interact with them over HTTP. Together, they gave the attacker unrestricted read/write access to the entire server filesystem with no authentication required.

## What was new this time?

Storing webshells inside the WordPress database rather than on disk is not unheard of. Though still relatively rare, the technique is notable for its ability to evade file-based malware scanners entirely.

Most security tools scan `wp-content/uploads`, plugin directories, and theme files. They focus primarily on the file system, leaving the database without the same level of scrutiny during an incident response sweep.

The attacker also paired the database shells with a plugin-based dropper that spoofed a Chrome 120 User-Agent header on every outbound request and explicitly commented in the source code that this was a FortiGuard bypass. By mimicking a common, legitimate browser signature, the malware’s outbound traffic blends in with normal web browsing activity, making it look like benign content.

### What is Fortiguard?

FortiGuard is Fortinet’s threat intelligence service, tracking malware, malicious domains, and attacker infrastructure across the internet. It is widely used by security teams to identify and block known threats in real time.

![FortiGuard](https://blog.sucuri.net/wp-content/uploads/2026/06/FortiGuard.png)

The combination of a legitimate-looking plugin name, database-resident payloads, and firewall evasion headers made this a notably layered infection that was engineered to stay hidden at multiple levels simultaneously.

## Domains involved in the infection

* `hxxps://wp-tracker[.]com/api[.]php` – Command-and-control / payload server
* `hxxps://destangelirvip[.]com` – Plugin URI listed in the fake plugin metadata

## Indicators of compromise

* **File path:** `wp-content/plugins/beloved-pbn/beloved-pbn.php`
* **Database table entries:** `wp_posts`.
* **Plugin Name:** Beloved PBN
* **Network indicators:** `POST` requests to `wp-tracker[.]com/api.php`

## Analysis of the malware

### The fake plugin: “Beloved PBN Entegrasyonu”

The plugin is short and looks harmless. Its only job is to call a remote server on every page load and echo the response into the site’s footer.

![call remote server on every page load and echo response](https://blog.sucuri.net/wp-content/uploads/2026/06/call-remote-serv...