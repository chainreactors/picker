---
title: How to Securely Debug WordPress Errors on Your Website
url: https://blog.sucuri.net/2022/10/how-to-securely-debug-wordpress-errors-on-your-website.html
source: Sucuri Blog
date: 2022-10-14
fetch_date: 2025-10-03T19:48:36.169633
---

# How to Securely Debug WordPress Errors on Your Website

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

# How to (Securely) Debug WordPress Errors on Your Website

[![](https://secure.gravatar.com/avatar/31118f76d9e502e944e2dcd61f84cc08daa2d1cbbd830ae60cb1e1e669ef8398?s=60&d=mm&r=g)](https://blog.sucuri.net/author/kaushal)

[Kaushal Bhavsar](https://blog.sucuri.net/author/kaushal)

* October 13, 2022

![How to Securely Debug & Check WordPress Errors on Your Website](https://blog.sucuri.net/wp-content/uploads/2022/10/BlogPost_Feature-Image_1490x700_How-to-Securely-Check-Debug-WordPress-Errors-on-Your-Website-820x386.png)

While working on or maintaining your WordPress website, you’ll inevitably encounter an error that prevents it from properly functioning. Knowing how to securely debug and troubleshoot WordPress is an exceptionally important skill. But there’s one important step you’ll want to take to prevent sensitive data exposure on your website.

In this article, we’ll explore how to securely check and debug errors on WordPress so you can quickly (and safely) spot problems on your site.

## What is debugging in WordPress?

Debugging is defined as the act of finding and resolving bugs or errors – usually in your website’s code. As a final step, you’ll need to perform QA to test the code and ensure that it’s resolved on your site.

WordPress websites come bundled with a WordPress debug tool that makes it easy to see root causes for website errors – a feature known as **WP\_DEBUG**. Let’s dive in to how it can lead to security issues and how to properly use it.

## How WP\_DEBUG can lead to security issues

If not performed correctly, debugging your website *can* inadvertently lead to sensitive data exposure on your website.

For example — you might encounter a situation where WordPress displays an Error page, sometimes referred to as a “White Screen of Death”. Naturally, you’ll want to troubleshoot the problem to figure out what is breaking the website and debug the issue.

The conventional solution is to modify the **wp-config.php** file and change the following parameters to enable debugging in WordPress: **define(‘WP\_DEBUG’, true);**

![Debug True](https://blog.sucuri.net/wp-content/uploads/2022/10/debug_true.png)

However, if you enable the debug log with this parameter, **it will cause the errors to display on the website homepage for everyone**. This exposes sensitive data about outdated software, location of files, PHP errors caused by plugins, themes, or custom code, and other sensitive information about your environment. And according the OWASP Top 10, this [can be classified](https://owasp.org/Top10/A05_2021-Security_Misconfiguration/) as a “Security Misconfiguration”.

> *“Error handling reveals stack traces or other overly informative error messages to users.”*

As a result, it’s not recommended to use **WP\_DEBUG** on a live website for this reason – it’s meant for local test environment or staging installations.

## How to enable debugging on WordPress

If you need to enable debugging on a live website and you don’t have a test environment handy, WordPress allows us to enable debug mode on the website without displaying debug results publicly.

To activate secure debugging in WordPress, follow these instructions:

### 1. Open your wp-config.php file

Log in to your FTP account and search for **wp-config.php** in your root WordPress directory.

### 2. Check for **WP\_DEBUG**

Navigate to the line in your wp-config file where WP\_DEBUG has been defined. It is usually disabled and looks like this:

```
define('WP_DEBUG', false);
```

### 3. Replace **WP\_DEBUG** with the following code:

```
define('WP_DEBUG', true);
define('WP_DEBUG_DISPLAY', false);
define('WP_DEBUG_LOG', true);
```

This essentially asks WordPress to log the errors to a debug log file and prohibits it from displaying on the webpages of your site.

![Secure Debug Enabled](https://blog.sucuri.net/wp-content/uploads/2022/10/secure-debug-code.png)

The parameter **define(‘WP\_DEBUG\_LOG’, true);** creates a file **debug.log** in the **./wp-content directory**. Furthermore, the format of this file is just like the **error\_log** file so we can easily find what we need.

## How can I check my WordPress debug mode results?

Once you’ve enabled secure debugging, you can check your WordPress debug log results in a few short steps:

1. Navigate to **/wp-content/**
2. Locate the **debug.log** file
3. Analyze the contents for errors, warnings, and notifications.

You can download, view and edit this file at your leisure. It’s incredibly useful for reviewing debug results at ...