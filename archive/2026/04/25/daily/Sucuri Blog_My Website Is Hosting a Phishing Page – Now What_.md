---
title: My Website Is Hosting a Phishing Page – Now What?
url: https://blog.sucuri.net/2026/04/my-website-is-hosting-a-phishing-page-now-what.html
source: Sucuri Blog
date: 2026-04-25
fetch_date: 2026-04-26T05:02:50.796896
---

# My Website Is Hosting a Phishing Page – Now What?

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

# My Website Is Hosting a Phishing Page – Now What?

[![](https://blog.sucuri.net/wp-content/uploads/2026/01/avatar_user_116_1769198545-60x60.png)](https://blog.sucuri.net/author/sucuriblog)

[Sucuri](https://blog.sucuri.net/author/sucuriblog)

* April 24, 2026

![My Website Is Hosting a Phishing Page - Now What?](https://blog.sucuri.net/wp-content/uploads/2026/04/My-Website-Is-Hosting-a-Phishing-Page-Now-What-820x385.png)

Most phishing advice is written for the person staring at a suspicious email. This guide is for the other kind of victim: The website owner whose legitimate site has been quietly turned into the attacker’s weapon.

You didn’t send the message or build the fake login page. You just woke up to a browser warning, a suspended hosting account, or a polite note from someone’s security team asking why your domain is requesting Apple ID credentials. What follows is how to find the phishing content, clean it up without inviting the attacker straight back in, and recover your reputation afterward.

## It’s not always you they’re phishing

It’s common to find directories on legitimate sites with names like login-apple-account or secure-paypal-verify, serving pixel-perfect clones of real login pages. In one case we’ve [written about before](https://blog.sucuri.net/2018/09/wordpress-database-upgrade-phishing-campaign.html), a hacked WordPress site was used to host a fake “database upgrade” notice that redirected users to a spoofed WordPress login page designed to harvest admin credentials.

In many of these cases, the site owner isn’t the target. The attacker is borrowing the site’s clean reputation as camouflage. A legitimate domain, working HTTPS, and a clean record with Google Safe Browsing let a phishing page last longer, reach more inboxes, and fool more people than one hosted on a throwaway domain. That’s why this particular outcome is one of the more damaging things that can follow a successful compromise.

## How you usually find out

Very few owners discover this on their own. The first sign is almost always external. This could be a browser warning from Google Safe Browsing or Microsoft SmartScreen, an abuse notice or suspension from your host, or the realization that your outbound mail is bouncing because your domain has landed on a spam blocklist.

  ![Google safe browsing phishing warning example](https://blog.sucuri.net/wp-content/uploads/2026/04/safebrowsing-phishing-warning-example.png)

*Example of a Google Safe Browsing phishing warning*

Sometimes the alert comes from a customer, a partner, or the security team of the brand being impersonated. Occasionally, it arrives as a sharp drop in search visibility or traffic after browsers and search authorities begin warning users away from the site.

Whichever channel brings the news, the page has usually been live for some time by the time you hear about it. The sooner you start, the less damage accumulates, both for the people being phished and for your own domain’s reputation.

## How it got there

Before you start removing files, spend a few minutes narrowing down the root cause. Clean up the phishing kit but miss the entry point and you’ll be doing this again in two weeks. The usual suspects fall into a few buckets:

* A vulnerable or outdated plugin, theme, or CMS core is, by a wide margin, the most common cause of issues on WordPress sites.
* Stolen or brute-forced admin credentials are often harvested by a phishing attack against someone on your team.
* Compromised SFTP, FTP, cPanel, or hosting control panel passwords, especially ones reused across services.
* Cross-contamination on shared hosting, where a compromise on a neighboring site got used to pivot sideways onto yours.
* Forgotten staging environments, abandoned subdomains, or unmaintained sub-installations nobody has patched in years.
* Nulled or tampered plugins and themes from unofficial sources, which sometimes ship with backdoors preinstalled.

Keep that shortlist in mind as you investigate. You’re looking for the answer to “how did they get in?” and “what did they leave behind?”

## Finding the phishing kit

Phishing kits leave a recognizable footprint, and a targeted search usually surfaces them faster than a full site audit.

1. Start by looking for directories whose names impersonate well-known brands, like **`login-apple-account`**, **`secure-paypal`**, **`office365-verify`**, **`chase-update`**, etc., most often in the web root or inside `wp-content/uploads/`. The uploads directory deserves a second pass specifically for `.php` files, since legitimate uploads almost never c...