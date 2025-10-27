---
title: Simple Include Statement Hides Casino Spam
url: https://blog.sucuri.net/2024/11/simple-include-statement-hides-casino-spam.html
source: Over Security - Cybersecurity news aggregator
date: 2024-11-16
fetch_date: 2025-10-06T19:20:06.146617
---

# Simple Include Statement Hides Casino Spam

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
* [WordPress Security](https://blog.sucuri.net/category/wordpress-security)

# Simple Include Statement Hides Casino Spam

[![](https://secure.gravatar.com/avatar/da934b974fa8adb3975fd07757f8322b04202cc98f15a625259eb3b404c1532a?s=60&d=mm&r=g)](https://blog.sucuri.net/author/kayleigh)

[Kayleigh Martin](https://blog.sucuri.net/author/kayleigh)

* November 14, 2024

![Simple Include Statement Hides Casino Spam](https://blog.sucuri.net/wp-content/uploads/2024/11/Blog-Post-Simple-Include-Statement-Hides-Casino-Spam-820x385.png)

Just as there are countless types of websites on the internet, there are just as many attackers seeking to exploit them. These attackers develop malicious code that continuously evolves, constantly finding new ways to harm their next target. Sometimes, threat actors rely on heavy obfuscation to conceal their malicious code, while others use stealthier methods to disguise malware that is in plain sight.

We recently stumbled upon a WordPress infection where the victim’s website was hosting a spam doorway that included casino and slot links based out of Indonesia. Instead of the attackers obfuscating their malware, they hid their malicious doorway with a simple **include** injected into the theme. This “**include**” referenced a malicious file above the webroot to avoid detection. By placing the payload above the webroot, the malware cleared standard checks, making it difficult to detect.

Let’s go over this sneaky malware in depth.

## Spam doorways

A client approached us to investigate a spam doorway on their WordPress site, which was leading search engine traffic like GoogleBot to casino and slot spam pages.

A spam doorway is a blackhat SEO tactic attackers use which feeds search engine traffic from a legitimate website to potentially hundreds of malicious sites. The endpoint sites benefit from a victim’s higher search engine ranking and the attackers that inserted the doorway earn SEO value for the endpoint spammy sites.

While there are some spam doorways that impact legitimate visitors, this particular malware was only impacting bots and crawlers by displaying spammy casino sites. When spoofing the user agent in our web browser, example casino spam pages can be seen:

![casino spam page](https://blog.sucuri.net/wp-content/uploads/2024/11/casino-spam-page.png)

One of the most interesting characteristics of this malware is that it maintains the victim’s domain throughout the site, making it appear like the domain is in fact legitimately hosting a casino slot website. Towards the bottom, it contains several hardcoded links to casino spam domains to further direct traffic toward spammy websites:

![spam website](https://blog.sucuri.net/wp-content/uploads/2024/11/spam-website.png)

Why would a threat actor insert a doorway that only impacts bots, and not legitimate users as well? This tactic is done for many reasons, with notable examples like the following:

* **To avoid detection by humans:** Humans do not see the spam, only bots, so that makes replicating the malware harder to track down.
* **Influencing a search engine’s algorithm:** This technique can majorly increase the search engine ranking of the spam sites.
* **To manipulate search engine algorithms without impacting real visitors:** This helps the malware stay undetected for longer as no visitors will see the spam.

## Casino spam doorway in action

Now that there is a complete understanding of what malware is impacting the site, the investigations begin. I started by performing my usual checks and after coming up empty-handed, I began reviewing the usual culprits where I’ve previously found doorway spam. I confirmed that none of the WordPress core files were altered, which led me to investigate the theme and plugins. I moved on to investigating the recently modified files in the theme where I came across the **functions.php** file that was changed earlier in the week. Even more suspiciously, this was the only file modified within the theme recently. Would you like at that, a sneaky include at the top of the file:

```
<?php
/**
 *
 * The framework’s functions and definitions
 */
include '/var/lock/server.php';
```

## Inspecting the include

At first glance, the **include** statement appears harmless, as many themes and plugins use it to incorporate common functions or configuration settings from external files. However, the directory it is referencing combined with the recently modified timestamp makes this suspicious and worth investigating. Let’s open up the **/var/lock/server.php** file and take a look at what’s inside:

![](https://blog.sucuri.net/wp-content/uploads/2024/11/server-php...