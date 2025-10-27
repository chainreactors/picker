---
title: 2024 Credit Card Theft Season Arrives
url: https://blog.sucuri.net/2024/11/2024-credit-card-theft-season-arrives.html
source: Sucuri Blog
date: 2024-11-08
fetch_date: 2025-10-06T19:15:15.965051
---

# 2024 Credit Card Theft Season Arrives

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

* [Ecommerce Security](https://blog.sucuri.net/category/ecommerce-security)
* [Magento Security](https://blog.sucuri.net/category/magento-security)
* [Website Malware Infections](https://blog.sucuri.net/category/website-malware-infections)
* [WordPress Security](https://blog.sucuri.net/category/wordpress-security)

# 2024 Credit Card Theft Season Arrives

[![](https://secure.gravatar.com/avatar/49a04d32074892dc04d9ed823aa114f8492a90e9c88852302b083c90aa322c21?s=60&d=mm&r=g)](https://blog.sucuri.net/author/benmartin)

[Ben Martin](https://blog.sucuri.net/author/benmartin)

* November 7, 2024

![2024 Credit Card Theft Season Arrives](https://blog.sucuri.net/wp-content/uploads/2024/11/2024-Credit-Card-Theft-Season-Arrives-820x385.png)

The holiday shopping season is just around the corner, and it’s the time of year the eCommerce website owners need to be most on their guard. Credit card stealing malware, commonly referred to as “MageCart”, is most rampant during the holiday shopping season. Attackers are always aiming to maximize their profits. As such, they know that if they focus their time and efforts at the last quarter of the year they’ll have more stolen card details to sell on the dark web when the time comes to cash in on their ill-gotten gains.

We’ve dug through our SiteCheck and malware remediation logs to identify some of the most commonly identified card skimming attacks over the course of the last few months. In today’s post we’re going to perform a malware analysis of the most common MageCart injections identified so that eCommerce website owners can better understand the risks, and (hopefully) protect themselves, their websites, and their customers from attackers.

Let’s get started, shall we?

## WebSocket skimmer

In checking the most common MageCart injections since August 1st of this year, this **web socket skimmer** tops our SiteCheck detections, having been identified on 432 websites. WebSocket card skimming infections appear to be getting more and more [popular](https://blog.sucuri.net/2023/11/skimming-credit-cards-with-websockets.html) these days, even though the attackers need more specialised server software installed in order to administer them.

Identified eCommerce CMS platforms include WordPress, Magento and OpenCart. There are quite a few variations of this malware and portions of it appear to contain randomised characters, but they all start with the following string:

```
<script>const …
```

The full injection looks like the following:

![full injection](https://blog.sucuri.net/wp-content/uploads/2024/11/full-injection.png)

Not all variations of this malware use the same characters, but they do use the same format and encoding. We can see the WebSocket loading some characters obfuscated with the **fromCharCode** function (one of the attackers favourites, it seems). However, simply entering that string into a simple **fromCharCode** deobfuscator returns only gibberish. In the above sample we also observe the following string:

```
const bzpy = 42
```

This is, in fact, an **XOR** value. Readers of this blog are likely familiar with [XOR](https://en.wikipedia.org/wiki/XOR_cipher) encryption: A simple additive cipher which can be reversed by applying the same value to the string. In this case, when we apply the number 42 as the XOR value we get our exfiltration domain:

```
wss://cdn[.]iconstaff[.]top/common?source=
```

This is not the first time we’ve noticed the number **42** used as an XOR cipher in malware injections (in fact, I think at this point I’ve lost count). This number actually pops up a lot in various tech and programming contexts! It is in fact a geeky nod to Douglas Adams well-known novel The Hitchhiker’s Guide to the Galaxy, famously being referenced as “*the Answer to the Ultimate Question of Life, the Universe, and [Everything](https://en.wikipedia.org/wiki/42_%28number%29)*“.

## jquery hex skimmer

Next up we have a hex-encoded skimmer identified on both Magento and WordPress, with roughly equal distribution between the two platforms. This has been flagged on 325 separate ecommerce websites since August 1st. Readers of this blog will recall that there’s been a steady trend over the last years of attackers “recycling” MageCart malware originally intended for Magento and porting it over to WooCommerce websites.

The first samples of this malware that we identified were lodged inside of the **core\_config\_data** database table in Magento (where miscellaneous scripts such as Google Tag Manager and Facebook tracking pixels are often placed by the website owner) and, interestingly, loaded inside **<svg tags** (scalable vector graphic) and executed in the victim’s browser using the **onload** function:

![malware sample]...