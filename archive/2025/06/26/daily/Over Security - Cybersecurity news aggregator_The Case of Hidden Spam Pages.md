---
title: The Case of Hidden Spam Pages
url: https://blog.sucuri.net/2025/06/the-case-of-hidden-spam-pages.html
source: Over Security - Cybersecurity news aggregator
date: 2025-06-26
fetch_date: 2025-10-06T22:54:33.544874
---

# The Case of Hidden Spam Pages

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

# The Case of Hidden Spam Pages

[![](https://secure.gravatar.com/avatar/49a04d32074892dc04d9ed823aa114f8492a90e9c88852302b083c90aa322c21?s=60&d=mm&r=g)](https://blog.sucuri.net/author/benmartin)

[Ben Martin](https://blog.sucuri.net/author/benmartin)

* June 25, 2025

![The Case of Hidden Spam Pages](https://blog.sucuri.net/wp-content/uploads/2025/06/The-Case-of-Hidden-Spam-Pages-820x385.png)

Spammy posts and pages being placed on WordPress websites is one of the most common infections that we come across. The reason being is that the attack is very low-level in terms of sophistication: All that is required of the attacker is to brute force their way into the wp-admin panel; from there they just have their scripts/bots post spam posts and pages effectively achieving a [blackhat SEO](https://blog.sucuri.net/2023/02/what-is-black-hat-seo.html) attack. Since an [out-of-the-box WordPress website](https://blog.sucuri.net/2023/10/optimizing-wordpress-security-beyond-default-configurations.html) contains no protection on admin access other than a password (with no limit on the number of failed login attempts), and the admin users can often be [discovered](https://blog.sucuri.net/2024/07/wordpress-user-enumeration.html) via enumeration, this remains a very popular type of spam infection on the platform.

![spammy posts](https://blog.sucuri.net/wp-content/uploads/2025/06/spammy-posts.png)

This spam attack is so simple and so common that we actually wrote an entire [guide](https://sucuri.net/guides/how-to-find-remove-wordpress-spam-posts/) on how to effectively remove it. Not all WordPress websites function as blogs, so many admin users don’t even access the posts section of wp-admin at all. For this reason, by the time the spam is discovered the posts/pages can number in the tens or sometimes even hundreds of thousands, making its removal time consuming without the usage of a little SQL command magic.

Normally it’s quite straightforward, but in this particular case we found some spam posts where the attackers went the extra mile to keep their blackhat SEO concealed.

## Regular Analysis

When removing malware from a compromised website it’s necessary to scan both the file structure and the database. Spam infections can be present in both but it’s especially common in the database since it’s so text-heavy. Querying the database for spam terms like *viagra, cialis, online casino,* and *essay writing* are part of our regular checks, and in this case there were many instances of questionable online casino spam terms coming up. Checking the database directly we could clearly see the posts/pages in question:

![casino spam pages](https://blog.sucuri.net/wp-content/uploads/2025/06/casino-spam-pages.png)

Additionally, the spam was very much publicly visible as we could see it being indexed by search engines:

![casino spam pages indexed](https://blog.sucuri.net/wp-content/uploads/2025/06/casino-spam-pages-indexed.png)

It must have been having a negative impact on the website’s SEO since online casino is not exactly an SEO-friendly term to have on your website. Normally in such cases we just hop into wp-admin and send the posts to the trash. That way if there happens to be any legitimate posts mixed in they can be easily restored (doesn’t happen very often, but you can’t be too careful).

However, the posts were nowhere to be seen. When we queried the posts and pages section of wp-admin for specific keywords like “*casino*” nothing showed up either:

![posts not found in wp admin](https://blog.sucuri.net/wp-content/uploads/2025/06/posts-not-found-in-wp-admin.png)

I noticed something, though: Normally when you query a dashboard for a page or post and nothing matches what you’re searching for it returns *No pages found* like this:

![typical no pages found result](https://blog.sucuri.net/wp-content/uploads/2025/06/typical-no-pages-found-result.png)

And that was nowhere to be found. Instead it looked like something was truncated. Something was hiding the spam pages.

## Sanity Check

When you see weird behaviour like this it’s always good to investigate further. After all the number one rule in tech support is “*Trust, but verify*“.

I tested to see if I could load up any of the spam pages within wp-admin itself, rather than just looking at rows and columns in a database manager.

In WordPress all pages and posts are stored in the **wp\_posts** table and every page/post has a corresponding identification number. We can see this in the bro...