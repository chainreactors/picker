---
title: Magbo Spam Injection Encoded with hex2bin
url: https://blog.sucuri.net/2023/03/magbo-spam-injection-encoded-with-hex2bin.html
source: Sucuri Blog
date: 2023-03-04
fetch_date: 2025-10-04T08:37:24.785310
---

# Magbo Spam Injection Encoded with hex2bin

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

# Magbo Spam Injection Encoded with hex2bin

[![](https://secure.gravatar.com/avatar/49a04d32074892dc04d9ed823aa114f8492a90e9c88852302b083c90aa322c21?s=60&d=mm&r=g)](https://blog.sucuri.net/author/benmartin)

[Ben Martin](https://blog.sucuri.net/author/benmartin)

* March 3, 2023

![Magbo spam injection encoded with hex2bin](https://blog.sucuri.net/wp-content/uploads/2023/03/23-BlogPost_Feature-Image_1490x700_Magbo-Spam-Injection-Encoded-with-hex2bin1-820x385.jpg)

We recently had a new client come to us with a rather peculiar issue on their WordPress website: They were receiving unwanted popup advertisements but only when the website was accessed through links posted on FaceBook*.* Initially we thought that this must be a rogue ad coming through an otherwise legitimate advertising network but it turned out to be a very well crafted and hidden spam injection.

In this post we will review this infection, outline the steps we took to find it, and explain how to prevent your website from falling victim to spam injections.

## Identifying the infection

Other than the reported behavior it was a very difficult infection to reproduce.

The ads wouldn’t appear all of the time and were very inconsistent. Some users reported that it would only appear on mobile devices, while others were certain it was displaying for other user agents as well. What is certain is that this behavior is fairly consistent with bogus advertisements.

However, once we clicked on one of the links from their FaceBook page we were greeted with exactly what the client was reporting: ![](https://blog.sucuri.net/wp-content/uploads/2023/03/magbo_spam.png)

Reproducing the behavior and viewing the symptoms is an important part of the remediation process: It allows us to monitor and inspect the network traffic which might lead us to find out where it originates. It also enables us to confirm that the issue resides on the website itself and not anything on the client’s end such as an infected browser or workstation.

## Integrity check reveals injected code

One of the most useful tools in our arsenal for identifying new malware samples is the [integrity check](https://docs.sucuri.net/plugins/core-integrity-check/): a verification process by which we verify the integrity of the core, plugin and themes.

In this case we noticed that the following file had a mismatched checksum:

* **./wp-content/plugins/really-simple-ssl/rlrsssl-really-simple-ssl.php**

With over five million installations the **really-simple-ssl** WordPress plugin is an enormously popular plugin which helps WordPress website administrators configure their websites to use HTTPS encryption. There are no known vulnerabilities with this plugin ever recorded by [WPScan](https://wpscan.com/plugin/really-simple-ssl), however just like any other piece of software it can be modified by attackers to make it do things it’s not supposed to do (in this case, unwanted spam popups).

Sure enough, when inspecting the file and comparing it to a known good copy we identified an injected chunk of code:

[![Integrity check reveals injected code in really-simple-ssl plugin](https://blog.sucuri.net/wp-content/uploads/2023/03/diff.png)](https://blog.sucuri.net/wp-content/uploads/2023/03/diff.png)

Integrity file check diff for really-simple-ssl plugin

Let’s take a closer look at this code and see what it’s doing!

## Injection analysis

It would be easy to overlook this during a cursory review — there’s no big, ugly encoded chunks of data nor any obfuscation in use as is common with website malware.

[![ register_activation_hook_rsssl injection in wordpress plugin](https://blog.sucuri.net/wp-content/uploads/2023/03/register_activation_hook_rsssl.png)](https://blog.sucuri.net/wp-content/uploads/2023/03/register_activation_hook_rsssl.png)

However, further inspection reveals it’s doing some questionable things that certainly has nothing to do with helping WordPress website owners deploy SSL/HTTPS encryption.

We can see that it’s probing for suitable directories to upload temporary files using file\_put\_contents. Most questionable of all, though, is this part right here:

```
define ('ph_stream', pack ("H*", $wpdb->get_var("SELECT option_value FROM ct_options WHERE option_id=719")));
```

Similar code was also found in two additional files in the environment:

* ./wp-content/themes/clientstheme/inc/**runtime.php**
* ./wp-content/mu-plugins/health-check-troubleshooting-mode/**health-check-troubleshooting-mode.php**

The pack (...