---
title: When Spam Hides In Plain Sight
url: https://blog.sucuri.net/2025/02/when-spam-hides-in-plain-sight.html
source: Over Security - Cybersecurity news aggregator
date: 2025-02-20
fetch_date: 2025-10-06T20:36:55.894573
---

# When Spam Hides In Plain Sight

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

# When Spam Hides In Plain Sight

[![](https://secure.gravatar.com/avatar/067bd4ee574f53bb79d411d83b5cc84ea794c798f945cb84a001cbe05fee65df?s=60&d=mm&r=g)](https://blog.sucuri.net/author/matt-morrow)

[Matt Morrow](https://blog.sucuri.net/author/matt-morrow)

* February 19, 2025

![When Spam Hides In Plain Sight](https://blog.sucuri.net/wp-content/uploads/2025/02/When-Spam-Hides-In-Plain-Sight-820x385.png)

We recently worked on an interesting case where Casino spam was visible in the page source, but couldn’t be located in any of the usual database rows or site files. Sitecheck flagged this as well.

![SiteCheck](https://blog.sucuri.net/wp-content/uploads/2025/02/sitecheck.png)

Casino and gambling spam is one of the most common types of spam attackers use. They are hoping that victims will submit personal information and credit card data on those pages. When search engines crawl infected sites, the spam pages will be indexed leading to malicious gambling pages appearing in search results that visitors may be tempted to click.

## Hunting the Malware Down

My first step was to search the database and files for a key identifier, in this case **-142311px**. Since that didn’t turn up anything, and by taking a look in wp-admin I already knew that the site was using [Fusion Builder](https://wordpress.com/plugins/fusion), a popular page builder for WordPress, I turned to inspecting the database contents directly. As is often the case with page builder plugins, I assumed the content might be base64 encoded. However, upon examining the database row of the infected page I couldn’t find anything containing the spam content.

When editing pages in wp-admin built with page builder plugins, you’ll usually need to use the edit links specific to the plugin in order to gain access to any widgets and other components that the plugin uses. After inspecting the page with the Fusion Builder utility, I still couldn’t find the spam content so I decided to fall back to the default WordPress editor.

![WP Default Editor](https://blog.sucuri.net/wp-content/uploads/2025/02/WP-Default-Editor.png)

In most cases, doing this will only provide access to settings like the permalink name and some generic utilities for defining how the page is categorized. Interestingly, I found that the Fusion Builder plugin allows for some additional widget customizations and code blocks not directly accessible in the page builder.

***Note:** It is best practice to create a backup before making any changes in these areas.*

![code block](https://blog.sucuri.net/wp-content/uploads/2025/02/code-block.png)

Upon editing the code block, I was able to see the spam in plain text.

![spam in code block](https://blog.sucuri.net/wp-content/uploads/2025/02/spam-in-code-block.png)

## Take Away

Attackers are always looking for ways to circumvent malware scans and better hide their injections. As we can see here, they took advantage of a simple trick that would be easy to overlook.

In addition to stealing personal and financial details, spam injections are one of the most common methods attackers use to redirect traffic to their own sites for further malicious activity and to further boost their own ratings by leveraging easy traffic hits, and that spam can destroy a site’s SEO ratings.

## Prevention

As a website owner, it’s important to take a proactive approach to security to mitigate risk from threats:

1. Regularly audit the plugins and themes in use and remove any that are no longer needed. Keep all plugins and themes up to date.
2. Generate [strong and unique passwords](https://blog.sucuri.net/2024/01/how-to-make-strong-password.html) for all of your accounts, including website administrators, FTP, database, and hosting.
3. M[onitor your website](https://sucuri.net/malware-detection-scanning/) and check for suspicious activity or unexpected website admin users.
4. Consider using [2FA](https://blog.sucuri.net/2022/04/the-case-for-2fa-by-default-for-wordpress.html) and [restricting access to your WordPress admin and sensitive pages](https://docs.sucuri.net/website-firewall/whitelist-and-blacklist/protected-page/) to allow access to only trusted IP addresses.
5. Use a [web application firewall](https://sucuri.net/website-firewall/) to help prevent vulnerability exploits, malicious code, and hack attempts.

If you think your website has been infected with malware but you’re not sure what to do next, we can help! Reach out to us on [chat](https://sucuri.net/live-chat/). Our expe...