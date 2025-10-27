---
title: Fake GIF Leveraged in Multi-Stage Reverse-Proxy Card Skimming Attack
url: https://blog.sucuri.net/2025/04/fake-gif-leveraged-in-multi-stage-reverse-proxy-card-skimming-attack.html
source: Sucuri Blog
date: 2025-04-26
fetch_date: 2025-10-06T22:03:46.104370
---

# Fake GIF Leveraged in Multi-Stage Reverse-Proxy Card Skimming Attack

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

* [Magento Security](https://blog.sucuri.net/category/magento-security)
* [Security Advisory](https://blog.sucuri.net/category/security-advisory)
* [Website Malware Infections](https://blog.sucuri.net/category/website-malware-infections)

# Fake GIF Leveraged in Multi-Stage Reverse-Proxy Card Skimming Attack

[![](https://secure.gravatar.com/avatar/49a04d32074892dc04d9ed823aa114f8492a90e9c88852302b083c90aa322c21?s=60&d=mm&r=g)](https://blog.sucuri.net/author/benmartin)

[Ben Martin](https://blog.sucuri.net/author/benmartin)

* April 25, 2025

![Fake GIF Leveraged in Multi-Stage Reverse Proxy Card Skimming Attack](https://blog.sucuri.net/wp-content/uploads/2025/04/Fake-Gif-Leveraged-in-Multi-Stage-Reverse-Proxy-Card-Skimming-Attack-820x385.png)

In today’s post we’re going to review a sophisticated, multi-stage carding attack on a Magento eCommerce website. This malware leveraged a fake gif image file, local browser **sessionStorage** data, and tampered with the website traffic using a malicious reverse-proxy server to facilitate the theft of credit card data, login details, cookies, and other sensitive data from the compromised website.

The client was experiencing some strange behaviour on their checkout page, including clients unable to input their card details normally, and orders not going through. They contacted us for assistance. Thinking this would be a straightforward case of credit card theft instead what we found was actually a fascinating and rather advanced malware which we will explore in detail in this post.

## Out of Date Magento

First off, it’s worth mentioning that the website in question was using a *very out-of-date* Magento installation, specifically version **1.9.2.4**. This version of the Magento eCommerce platform is the last of its kind in the 1.X branch with Adobe having **ended its support** for it in June 2020, nearly half a decade ago.

However, there are a number of eCommerce websites still using this deprecated software platform despite the security risks involved due to lack of ongoing and official support from Adobe. Magento is *not an easy platform to manage* (when compared to other eCommerce platforms like WooCommerce/WordPress), and performing a full migration / site upgrade from Magento1 to Magento2 can be a time consuming and expensive endeavour. This is particularly true if the website administrator/store-owner is not themselves tech-savvy and instead reliant upon website developers to do their work for them.

As such it appears a number of website owners are content to reside in this old, deprecated software platform, cross their fingers and hope for the best. However, we cannot stress enough the importance of keeping your core CMS platform up to date, and be sure to apply all available security patches at the soonest possible opportunity.

Be sure to check out our new [guide](https://blog.sucuri.net/2025/03/quick-guide-to-magento-security-patches.html) on how to install Magento security patches!

## Questionable JavaScript

With that obligatory warning out of the way let’s dive into this infection shall we?

Naturally the first thing that we need to do when investigating a case of [MageCart](https://sucuri.net/guides/what-is-magecart/) malware is to inspect the page source for any questionable snippets of JavaScript that might be loading on the checkout page. While plenty of malware injections on Magento websites are backend/PHP based and not outwardly-visible, JavaScript injections still remain a favourite among attackers for its ease of use and ability to inject it from a simple admin panel compromise or SQLi attack.

This is when we came across the following code:

![questionable javascript](https://blog.sucuri.net/wp-content/uploads/2025/04/questionable-javascript.png)

This code was lodged between two **<!– Bing UET Tag –>** tags. At first glance it appeared that this was simply Bing’s conversion tracking code for their ads (not uncommon to see on a website) but something didn’t seem right about this particular string here:

```
bpumediabpumagentothembpuimgbpuline
```

Specifically the fact that lodged in the middle of this string was a *direct reference to* **magento**. This is not something that would be included in a generic Bing tracking code so we knew there must be something amiss, but what did it mean?

Let’s turn our attention to this portion of the JavaScript code:

```
('rep' || 'bing')['concat']('lace')](/bpu/g, '/')
```

The script uses some JavaScript tricks to dynamically build the method name “**replace**” by concatenating the strings `**rep**` with `**lace**` and sneaking the string `**bing**` in the middle to make it look more innocuous. The global flag ‘**g**‘ ensures that all occurrences of the subs...