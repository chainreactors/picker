---
title: How to Harden WordPress With wp-config.php & Avoid Data Exposure
url: https://blog.sucuri.net/2023/07/tips-for-wp-config-how-to-avoid-sensitive-data-exposure.html
source: Over Security - Cybersecurity news aggregator
date: 2023-07-12
fetch_date: 2025-10-04T11:57:36.342481
---

# How to Harden WordPress With wp-config.php & Avoid Data Exposure

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
* [Website Security](https://blog.sucuri.net/category/website-security)
* [WordPress Security](https://blog.sucuri.net/category/wordpress-security)

# How to Harden WordPress With WP-Config & Avoid Data Exposure

[![](https://secure.gravatar.com/avatar/1c366df979e3ab3b3f9add08268c19141d3202ba8b885d1fcbfd106e7f2f7aba?s=60&d=mm&r=g)](https://blog.sucuri.net/author/luke)

[Luke Leal](https://blog.sucuri.net/author/luke)

* Last Updated: April 16, 2024

![Tips for WP-CONFIG to avoid sensitive data exposure](https://blog.sucuri.net/wp-content/uploads/2022/06/BlogPost_FeatureImage_1490x700_Renaming-WP-CONFIG.PHP-Leads-to-Sensitive-Data-Exposure-820x386.jpg)

## What is wp-config.php?

The **wp-config.php** file is a powerful core WordPress file that is vital for running your website. It contains important configuration settings for WordPress, including details on where to find the database, login credentials, name and host. This config file is also used to define advanced options for database elements, security keys, and developer options.

In this post, we’ll outline some important website hardening recommendations for your wp-config file and explain exactly how to safely update it to avoid sensitive data exposure.

## How to harden WordPress with wp-config.php

There are a few tricks that you can implement for your **wp-config.php** file that can help you improve your security and harden your WordPress website.

### 1 – Restrict access to wp-config.php

New WordPress owners will always want to start with restricting access to wp-config in the first place.

Move your wp-config file one directory level above the root folder to prevent it from being accessible to the internet. If wp-config does not exist in the root folder, WordPress will [automatically look for this file in the folder above the root directory](https://wordpress.org/support/article/hardening-wordpress/#securing-wp-config-php).

If you use a server with **.htaccess**, you can add a rule at the very top to deny access to anyone surfing for it.

Here are the directives for Apache 2.4:

```
<FilesMatch "wp-config\.php">
  Require all denied
</FilesMatch">
```

### 2 – Enable automatic WordPress updates

Enabling automatic updates will ensure that your WordPress site always contains the latest security patches. Simply add the following snippet to your wp-config:

```
define( ‘WP_AUTO_UPDATE_CORE’, true );
```

Be sure to implement automatic backups so that you can easily recover your website in the event of an emergency or in the off-chance that an update causes issues.

### 3 – Setup salts and keys

The **wp-config.php** file includes a section dedicated to authentication [salts and keys](https://blog.sucuri.net/2023/06/what-are-wordpress-salts-security-keys.html) which can improve the security of cookies and passwords that are in transit between your browser and the web server.

You can set up your keys by including or editing these lines after the other define statements in your **wp-config.php** file:

```
define(‘AUTH_KEY’, ‘include salt here’);

define(‘SECURE_AUTH_KEY’, ‘include salt here’);

define(‘LOGGED_IN_KEY’, ‘include salt here’);

define(‘NONCE_KEY’, ‘include salt here’);
```

You can easily generate salts by navigating to the [wordpress.org salt generator](https://api.wordpress.org/secret-key/1.1/salt/) or using the reset salts + keys option in the [Sucuri WordPress Plugin](https://sucuri.net/wordpress-security-plugin/).

### 4 – Set file permissions for wp-config.php

Since the **wp-config.php** file contains incredibly sensitive information, you’ll want to ensure that file permissions are defined to prevent unauthorized access and modification. Something along the lines of **600** should be sufficient, but you can start with **400** with the understanding that you might need to escalate permissions if you run into problems.

A good rule of thumb is to start with the least permissive configuration and only escalate permissions when necessary. You should never set permissions for anything to **777** unless you are an expert or have a really good reason for doing so.

### 5 – Disable plugin and theme installers

You can also use **wp-config.php** to define essential information about WordPress plugins or themes.

For example, website owners may want to use wp-config to disable both the theme and plugin file editors and installers by simply adding the following lines to their wp-config file.\*\*

```
define( 'DISALLOW_FILE_EDIT', true ); //disables file editor

define( 'DISALLOW_FILE_MODS', true ); //disables both file editor and installer
```

*\*\* It’s important to note that this will also prevent plugin updates. You ...