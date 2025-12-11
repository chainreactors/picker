---
title: WordPress Auto-Login Backdoor Disguised as JavaScript Data File
url: https://blog.sucuri.net/2025/12/wordpress-auto-login-backdoor-disguised-as-javascript-data-file.html
source: Over Security - Cybersecurity news aggregator
date: 2025-12-10
fetch_date: 2025-12-11T03:24:37.364529
---

# WordPress Auto-Login Backdoor Disguised as JavaScript Data File

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

# WordPress Auto-Login Backdoor Disguised as JavaScript Data File

[![](https://secure.gravatar.com/avatar/3bb7fb42c6bf04c758d570c2f6bb217266c127e77766dc9d8e6754f15cdd5867?s=60&d=mm&r=g)](https://blog.sucuri.net/author/puja-srivastava)

[Puja Srivastava](https://blog.sucuri.net/author/puja-srivastava)

* December 10, 2025

![Auto-Login Backdoor Disguised as JavaScript Data File](https://blog.sucuri.net/wp-content/uploads/2025/12/Auto-Login-Backdoor-Disguised-as-JavaScript-Data-File-820x385.png)

During a recent investigation, we discovered a sophisticated WordPress backdoor hidden in what appears to be a JavaScript data file. This malware automatically logs attackers into administrator accounts without requiring any credentials.

In September, we published an article showcasing [another WordPress backdoor that creates admin accounts](https://blog.sucuri.net/2025/09/hidden-wordpress-backdoors-creating-admin-accounts.html). This new variant takes a different approach by hijacking existing administrator sessions instead of creating new accounts, making it harder to detect through user audits.

## What turned up during our review

The file was disguised as a JavaScript asset in a PHP file located in the WordPress admin wp-admin/js directory, but it was really all PHP. If you hit it directly in a browser, it would hunt for the WordPress `wp-config.php`, load the whole environment, pick an administrator account, log you in automatically, and then send you straight to the dashboard.

Anyone who knew the file’s URL `wp-admin/js/mr_skk/data.php` could instantly become an admin.

The file also tried to blend in with normal WordPress behavior by loading the standard template loader at the end, which made the request look like a regular page load instead of some obvious attack script.

## Infection path and key indicators

### File System Indicators

The malicious file is at `wp-admin/js/mr_skk/data.php`. That’s really suspicious, since PHP files just shouldn’t be in the JavaScript directory. The `mr_skk/` subdirectory isn’t part of the normal WordPress core, and the file named data.php is disguised to look like some harmless data handler.

### Code Signatures

The backdoor contains two custom functions named `auto_login()` and `get_user_id()`. These functions abuse legitimate WordPress functions, including `wp_set_current_user()`, `wp_set_auth_cookie()`, and `get_users(['role' => 'administrator'])`, to hijack administrator sessions. The code performs directory traversal searching for `wp-config.php`, loads `wp-load.php` from the discovered path, and includes `template-loader.php` from WordPress core.

![backdoor custom functions](https://blog.sucuri.net/wp-content/uploads/2025/12/backdoor-custom-functions.png)

### Network Indicators

The backdoor redirects to admin URLs containing the parameter `?platform=000webhost`. This tracking parameter appears in admin redirects and may indicate the compromise origin. Access patterns include direct requests to `/wp-admin/js/mr_skk/data.php`, immediate creation of an administrator session, and admin panel access without corresponding login events in server logs.

![network indicators](https://blog.sucuri.net/wp-content/uploads/2025/12/network-indicators.png)

## Effects on the compromised site

This type of backdoor gives the attacker complete control. Once they’re logged in as an administrator, they can install rogue plugins, drop additional payloads, modify theme files, create new backdoors, or even delete legitimate user accounts. Because the script logs them in as a real administrator, no suspicious usernames show up in the dashboard.

The login process also triggers normal WordPress hooks, which means any security plugin that relies on the `wp_login` action may record a legitimate-looking login rather than flag it as malicious. This makes the intrusion extremely stealthy and easy to miss.

The backdoor creates valid authentication cookies, allowing attackers to maintain access even after closing their browser and repeatedly returning to the compromised site without re-authenticating for the entire cookie lifetime, which is typically 14 days by default. Unlike backdoors that create new admin accounts, this malware leaves no new user accounts in the database, doesn’t modify existing user passwords, appears as normal admin activity in access logs, and bypasses account creation email notifications that might alert the real site owner.

## Inside the malicious workflow

### Locating the WordPress ...