---
title: What is php.ini? Where It’s Located, How to Edit & Common Directives
url: https://blog.sucuri.net/2023/07/what-is-php-ini-location-how-to-edit-common-directives.html
source: 
date: 2023-07-07
fetch_date: 2025-10-04T11:52:50.763620
---

# What is php.ini? Where It’s Located, How to Edit & Common Directives

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

* [Security Education](https://blog.sucuri.net/category/security-education)
* [Web Pros](https://blog.sucuri.net/category/web-pros)
* [Website Security](https://blog.sucuri.net/category/website-security)

# What is php.ini? Where It’s Located, How to Edit & Common Directives

[![](https://secure.gravatar.com/avatar/b2a47b57affd449fb66751c7eec943a5943c2ebaa128f8ba6926982c6e066627?s=60&d=mm&r=g)](https://blog.sucuri.net/author/rianna)

[Rianna MacLeod](https://blog.sucuri.net/author/rianna)

* Last Updated: March 14, 2024

![What is php.ini? Where It's Located, How to Edit & Common Directives](https://blog.sucuri.net/wp-content/uploads/2023/07/23-BlogPost_Feature-Image_1490x700_What-is-php.ini-Where-Its-Located-How-to-Edit-and-Malware-Signs-820x386.png)

The **php.ini file**, a critical configuration file containing your web server’s PHP settings, is integral to the functioning of your website.

Each time PHP initiates, your system hunts down this file to identify directives that will be applied to your site’s scripts. While your PHP initialization file comes pre-configured, there may be instances when you need to tweak the default settings to meet your specific requirements, such as modifying the memory limit or maximum execution time for scripts to run on your environment.

Website malware can impact the php.ini file, particularly on servers running older versions of PHP. In the first six months of 2023 alone, our team remediated **30,658** compromised php.ini files from infected websites.

In today’s post, we’ll walk you through what this file is, where it’s located, how to modify this file to change your PHP settings, how it’s used by attackers to execute malicious code, and how to harden your site to prevent attacks.

**Contents:**

* [What is the php.ini file](#what-is-php-ini)
* [Where is php.ini located?](#where-is-php-ini)
* [How can I change php.ini directives?](#how-to-change-php-ini)
* [What settings can I find in php.ini?](#php-ini-directives)
* [Can malware affect the php.ini file?](#php-ini-malware)

## What is the php.ini file?

The **php.ini** file, also referred to as PHP’s initialization file, is a crucial configuration file that governs your web server’s PHP settings. It allows you to manage your site’s PHP-specific regulations, such as defining the maximum size for file uploads, error displays, file timeouts, visibility of error messages, memory limits, and other server-management functionalities.

  ![Example of a php.ini file contents.](https://blog.sucuri.net/wp-content/uploads/2023/07/image3.png)

Example of a php.ini file.

By default, your server comes pre-configured with standard PHP settings. However, the php.ini file allows more customized control over these settings to optimize performance and enable certain functionalities.

## Where is php.ini located?

The php.ini file is read by PHP during server start-up, however the location of your php.ini file may differ based on your server’s configuration, operating system, and PHP version.

We’ve provided a list below of some of the most common default locations for the php initialization file:

### Default php.ini location for Linux

* /etc/php.ini
* /etc/php/X/apache2/php.ini (replace X with your PHP version)

### Default php.ini location for Windows

* C:\php\php.ini
* C:\Windows\php.ini

### How to locate the php.ini file via command line

If you’re comfortable with the command line interface, you can quickly locate your php.ini file using the **‘php –ini’** command.

Simply follow these instructions:

1. SSH onto your web server.
2. Type the following command:

```
php --ini | grep php.ini
```

3. Press enter.
4. A list of all actively used php.ini files along with their locations will be displayed.

![A list of all actively used php.ini files along with their locations in the command line.](https://blog.sucuri.net/wp-content/uploads/2023/07/image1-650x79.png)

#### Check with your hosting provider

If you’re using a shared hosting plan, your access to php.ini may be restricted. You’ll need to contact your hosting provider for assistance identifying the location of the file and making any changes to it.

## How can I change php.ini directives?

Even though default PHP settings are pre-installed on your server, you might need to create or edit a php.ini file to modify specific server settings. This can be accomplished by opening the file in your favorite text editor, modifying parameter values, saving them, and then [restarting your web server](https://www.cyberciti.biz/faq/how-to-reload-restart-php7-0-fpm-service-linux-unix/) to apply the changes.

  ![Examples of directives found in a php.ini file.](https://blog.sucuri.net/wp-content/uploads/2023/07/image2.png)

Examples of directives ...