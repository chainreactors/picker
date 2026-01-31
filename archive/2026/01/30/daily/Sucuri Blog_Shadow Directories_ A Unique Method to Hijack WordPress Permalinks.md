---
title: Shadow Directories: A Unique Method to Hijack WordPress Permalinks
url: https://blog.sucuri.net/2026/01/shadow-directories-a-unique-method-to-hijack-wordpress-permalinks.html
source: Sucuri Blog
date: 2026-01-30
fetch_date: 2026-01-31T04:03:27.014064
---

# Shadow Directories: A Unique Method to Hijack WordPress Permalinks

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

# Shadow Directories: A Unique Method to Hijack WordPress Permalinks

[![](https://secure.gravatar.com/avatar/3bb7fb42c6bf04c758d570c2f6bb217266c127e77766dc9d8e6754f15cdd5867?s=60&d=mm&r=g)](https://blog.sucuri.net/author/puja-srivastava)

[Puja Srivastava](https://blog.sucuri.net/author/puja-srivastava)

* January 30, 2026

![Shadow Directories - A Unique Method to Hijack WordPress Permalinks](https://blog.sucuri.net/wp-content/uploads/2026/01/Shadow-Directories-A-Unique-Method-to-Hijack-WordPress-Permalinks-820x385.png)

Last month, while working on a WordPress cleanup case, a customer reached out with a strange complaint: their website looked completely normal to them and their visitors, but Google search results were showing something *very* different.

Instead of normal titles and descriptions, Google was displaying casino and gambling-related content. We have been seeing [rising cases of spam on WordPress websites](https://blog.sucuri.net/2025/11/slot-gacor-the-rise-of-online-casino-spam.html). What made this even more confusing was where the spam was appearing. It was not showing on the homepage or blog posts, but on pages like About Us, Contact Us, Privacy Policy, and Terms & Conditions.

These are pages that usually stay untouched for years. Seeing spam there immediately raised concern.

The permalink for the “About Us” page was exactly what it should be, and the content was legitimate. However, as soon as we changed our browser’s User-Agent to mimic a search engine crawler, the spam appeared.

![spam page seen from search engine User-Agent](https://blog.sucuri.net/wp-content/uploads/2026/01/spam-page-seen-from-search-engine-User-Agent.png)

## What are permalinks?

A WordPress permalink is the permanent web address (URL) of a post, page, or piece of content.

It’s what people type or click to visit that content.

* A hard-coded link is a fixed URL written manually, like `https://REDACTED/?p=103`, which can break if the site structure changes.
* A permalink is WordPress’s permanent, SEO-friendly URL, like `https://REDACTED/about-us/`, and it updates automatically with WordPress settings.

Permalinks usually include words from the title to make them easy to read and SEO-friendly.

## What did we find?

We started by checking the affected pages through the WordPress admin panel. The About Us page had a standard permalink and the content inside the editor looked completely clean. There was no visible spam, no suspicious links, and no injected scripts. To be sure, we also checked the database directly. The corresponding entry inside the wp\_posts table matched exactly what was shown in the admin dashboard.

At this stage, there was no clear explanation for why Google was indexing spam content. The page source looked legitimate, the database was clean, and nothing stood out inside WordPress itself.

The breakthrough came when we loaded the same page again, but this time using a browser configured with a Googlebot User-Agent. As soon as we did that, the page content changed. Instead of the normal About Us text, the browser displayed a full page of casino-related spam.

That confirmed the site was behaving differently depending on the visitor.

## What made this case different?

Upon inspecting the site’s file system via the file manager, we found something highly irregular. The attacker had not modified the WordPress database or the legitimate page content. Instead, they created physical directories on the server with names that exactly matched the WordPress permalinks.

The “new” element here was the use of directory shadowing. For example, since the “About Us” page had the permalink **`https://REDACTED/about-us/`**, the attacker created a folder named **`/about-us/`** in the root directory. Because of how web servers like Apache and Nginx are configured, they prioritize serving a physical directory and its index.php file over the virtual permalinks handled by the WordPress index.php file. This allowed the attacker to fully hijack specific pages without modifying the actual WordPress configuration.

Inside each of these “shadow” folders, we found three specific files:

* **index.php** – The controller that decided what content to show.
* **indexx.php** – A static, clean copy of the original page’s source code.
* **readme.txt** – A file containing the full source code for the spam page.

This technique stood out because it completely bypassed WordPress’s page rendering process without altering the page content in the admin...