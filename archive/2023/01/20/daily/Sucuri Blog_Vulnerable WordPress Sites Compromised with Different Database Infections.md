---
title: Vulnerable WordPress Sites Compromised with Different Database Infections
url: https://blog.sucuri.net/2023/01/vulnerable-wordpress-sites-compromised-with-different-database-infections.html
source: Sucuri Blog
date: 2023-01-20
fetch_date: 2025-10-04T04:21:12.679284
---

# Vulnerable WordPress Sites Compromised with Different Database Infections

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

* [Website Security](https://blog.sucuri.net/category/website-security)
* [WordPress Security](https://blog.sucuri.net/category/wordpress-security)

# Vulnerable WordPress Sites Compromised with Different Database Infections

[![](https://secure.gravatar.com/avatar/da934b974fa8adb3975fd07757f8322b04202cc98f15a625259eb3b404c1532a?s=60&d=mm&r=g)](https://blog.sucuri.net/author/kayleigh)

[Kayleigh Martin](https://blog.sucuri.net/author/kayleigh)

* January 19, 2023

![Vulnerable WordPress Sites Compromised Database Injections](https://blog.sucuri.net/wp-content/uploads/2023/01/BlogPost_Feature-Image_1490x700_Vulnerable-WordPress-Sites-Compromised-820x386.png)

Vulnerabilities within WordPress can lead to compromise, and oftentimes known vulnerabilities are utilized to infect WordPress sites with more than one infection. It is common for out of date websites to be attacked by multiple threat actors or targeted by the same attacker using multiple different channels.

We recently came across a database injection that has two different pieces of malware accomplishing two unrelated goals. The first injection redirects users to a spammy sports website and the second injection boosts authority of a spammy casino website within search engines.

So far, roughly 270 sites have been impacted by the first injection, while 82 sites have been impacted by the second. Both pieces of malware can be found scattered throughout a WordPress database but they each accomplish different tasks.

Let’s look at the two injections.

## Database Redirect & Casino Site Authority Boosting

The first injection can be found sprinkled throughout a [hacked WordPress database](https://sucuri.net/guides/how-to-clean-malware-from-hacked-database/):

```
<meta http-equiv="Refresh" content="60; URL=hxxp://redirect4[.]xyz/">
```

Let’s review what this injection is doing.

The domain found on the first line is not the final destination of the attack, it simply performs the heavy lifting of the redirect. First, the browser is instructed to wait 60 seconds, then a redirect occurs to the domain hxxp://redirect4[.]xyz. Then, the unknowing user is redirected again and lands on the following spam domain after the first redirect completes:

```
hxxp://pontiarmada[.]com
```

The spam site **hxxp://pontiarmada[.]com** has [injected iframes to disseminate malware](https://labs.sucuri.net/blacklist/info/?domain=pontiarmada.com) to unknowing visitors.

[![pontiarmada spam website](https://blog.sucuri.net/wp-content/uploads/2023/01/pontiar_media.png)](https://blog.sucuri.net/wp-content/uploads/2023/01/pontiar_media.png)

The second injection can also be found sprinkled throughout the WordPress database:

```
<style type="text/css"> dofollow { display: none; } </style> <dofollow><a href="hxxp://nomortogelku[.]xyz/" rel="external" alt="nomortogelku" title="nomortogelku">nomortogelku[.]xyz</a> <a href="http://207[.]106[.]22[.]48/" rel="external" alt="Nomor Togel Hari Ini" title="Nomor Togel Hari Ini">Nomor Togel Hari Ini</a></dofollow>
```

Let’s discuss what this database injection is doing.

The domain **hxxp://nomortogelku[.]xyz** is a gambling casino site using a common method to boost its authority in search engines. The black hat SEO tactic this attacker used places an invisible link throughout the compromised website to increase its domain authority and appear more legitimate.

Both of these injections are found scattered throughout WordPress databases, oftentimes found in the **posts** table. Below is the site:

[![Indonesian sports betting site ](https://blog.sucuri.net/wp-content/uploads/2023/01/sports_betting.png)](https://blog.sucuri.net/wp-content/uploads/2023/01/sports_betting.png)

One characteristic both injections have in common is the domain extension used, **.xyz*.*** The **.xyz** domain extension is commonly used by attackers and the number of malicious domains using this extension increases everyday. Threat actors cycle through domains often — and domains with the **.xyz** extension tend to be cheap for the first year, which is a leading theory as to why this extension is widely used.

These two infections found on the same site provide an example of how threat actors can disseminate different types of malware through the same site, or how different attackers can take advantage of the same vulnerability to infect the same WordPress site.

## Two Infections for the Price of One

WordPress sites are often taken advantage of by threat actors when a vulnerability is present or an admin user is compromised. Once an attacker gains access to a website they can easily disseminate malware, and oftentimes they use their leverage to distribute malware through multiple channels.

Many threat actors even monetize ...