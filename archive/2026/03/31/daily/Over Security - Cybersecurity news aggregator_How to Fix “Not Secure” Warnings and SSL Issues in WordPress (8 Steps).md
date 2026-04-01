---
title: How to Fix “Not Secure” Warnings and SSL Issues in WordPress (8 Steps)
url: https://blog.sucuri.net/2026/03/how-to-fix-not-secure-warnings-and-ssl-issues-in-wordpress-8-steps.html
source: Over Security - Cybersecurity news aggregator
date: 2026-03-31
fetch_date: 2026-04-01T04:47:26.777090
---

# How to Fix “Not Secure” Warnings and SSL Issues in WordPress (8 Steps)

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

# How to Fix “Not Secure” Warnings and SSL Issues in WordPress (8 Steps)

[![](https://secure.gravatar.com/avatar/3bb7fb42c6bf04c758d570c2f6bb217266c127e77766dc9d8e6754f15cdd5867?s=60&d=mm&r=g)](https://blog.sucuri.net/author/puja-srivastava)

[Puja Srivastava](https://blog.sucuri.net/author/puja-srivastava)

* Last Updated: March 31, 2026

![How to Fix Not Secure Warnings and SSL Issues in WordPress](https://blog.sucuri.net/wp-content/uploads/2023/09/Blog-Post-How-to-Fix-_Not-Secure_-Warnings-and-SSL-Issues-in-WordPress-8-Steps-820x385.png)

If you own a WordPress website and ever encountered the “**Not Secure**” warning, you might have worried that visitors would perceive your site as spam or fraudulent. Not only does this warning impact user trust, but it can also create technical search issues when both HTTP and HTTPS versions of your pages remain accessible or when redirects, canonicals, and sitemaps point to different URL versions. Browsers show the visible security warning, while search engines rely on permanent redirects, canonical URLs, and updated sitemaps to understand your preferred HTTPS pages.

## Understanding the **‘**Connection Not Secure**‘** warning

When users visit your website, data is transferred between their browsers and your servers. If sent via HTTP (HyperText Transfer Protocol), this data is vulnerable to interception since it is sent in plain text. When plain text information is intercepted by bad actors, it can be misused — leading to security breaches and loss of sensitive data for both you and your website visitors.

To fix this, you need to [implement HTTPS](https://sucuri.net/guides/how-to-install-ssl-certificate/), which encrypts data with an SSL certificate. If a hacker intercepts any information as it passes to and from your site, it will appear as incomprehensible gibberish, protecting sensitive information like login credentials, form submissions, and credit card information.

Implementing SSL also comes with some SEO benefits as well, since Google and other search engines flag sites without HTTPS and SSL as insecure. In essence a missing SSL certificate can ultimately lead to unwanted “**Connection** not secure” browser warnings.

[![Example of Not Secure warning in browser. ](https://blog.sucuri.net/wp-content/uploads/2023/09/example-not-secure-warning-browser-600x194.png)](https://blog.sucuri.net/wp-content/uploads/2023/09/example-not-secure-warning-browser.png)

Example of “Not Secure” warning in browser.

## Why WordPress shows ‘Not Secure’ warnings

The primary reason your WordPress website might be displaying a “Not Secure” warning is due to the lack of a valid SSL (Secure Sockets Layer) certificate.

A certificate can also be present and still fail if it is expired, revoked, self-signed on a public site, installed for the wrong hostname, or served with an incomplete certificate chain. Common examples include a certificate that covers example.com but not `www.example.com`, or an origin server behind a CDN that is not configured for end-to-end HTTPS. Another possibility could be that your website needs updating. WordPress updates often include security patches, so ensuring your site is up-to-date could help resolve this issue.

In some cases, a faulty plugin could be causing your site to appear insecure. If you’ve recently added or updated a plugin and the “Not Secure” warning has appeared, this could be the source of the problem. You can test this by removing the suspected plugin and checking if the warning goes away. That said, routine updates rarely solve a certificate warning by themselves unless the real issue is mixed content, a bad redirect, or a theme/plugin conflict that is still outputting HTTP URLs.

Most commonly, the issue is directly related to the SSL certificate. If your WordPress site is displaying a “Not Secure” warning, it’s important to verify that you have an active, suitable SSL certificate. This will help safeguard your website, data, and visitors from potential security breaches – however, it won’t prevent your site from being hacked in the first place.

If SSL is present but is not configured properly or the webpage has mixed content, then you might also encounter a warning like this one:

## [![Parts of this page are not secure mixed content](https://blog.sucuri.net/wp-content/uploads/2023/09/parts-of-this-page-not-secure-images-warning-600x369.png)](https://blog.sucuri.net/wp-content/uploads/2023/09/parts-of-this-page-not-secure-images-warning.png)What is a mixed content w...