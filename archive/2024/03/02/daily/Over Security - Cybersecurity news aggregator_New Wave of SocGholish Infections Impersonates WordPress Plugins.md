---
title: New Wave of SocGholish Infections Impersonates WordPress Plugins
url: https://blog.sucuri.net/2024/03/new-wave-of-socgholish-infections-impersonates-wordpress-plugins.html
source: Over Security - Cybersecurity news aggregator
date: 2024-03-02
fetch_date: 2025-10-04T12:12:06.156343
---

# New Wave of SocGholish Infections Impersonates WordPress Plugins

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

# New Wave of SocGholish Infections Impersonates WordPress Plugins

[![](https://secure.gravatar.com/avatar/49a04d32074892dc04d9ed823aa114f8492a90e9c88852302b083c90aa322c21?s=60&d=mm&r=g)](https://blog.sucuri.net/author/benmartin)

[Ben Martin](https://blog.sucuri.net/author/benmartin)

* March 1, 2024

![New Wave of SocGholish Infections Impersonates WordPress Plugins](https://blog.sucuri.net/wp-content/uploads/2024/03/Blog-Post-New-SocGholish-Variant-820x385.png)

[SocGholish malware](https://blog.sucuri.net/2022/08/socgholish-5-years-of-massive-website-infections.html), otherwise known as “fake browser updates”, is one of the most common types of malware infections that we see on hacked websites. This long-standing malware campaign leverages a JavaScript malware framework that has been in use since at least 2017. The malware attempts to trick unsuspecting users into downloading what is actually a [Remote Access Trojan (RAT)](https://blog.sucuri.net/2024/02/remote-access-trojan-rat-types-mitigation-removal.html) onto their computers, which is often the first stage in a ransomware infection.

Late last week our incident response team identified a fresh wave of SocGholish (fake browser update) infections targeting WordPress websites. The infected sites were compromised through hacked wp-admin administrator accounts, as we will demonstrate in this post. This is just one of countless examples of why [securing your administrator panel](https://blog.sucuri.net/2021/07/basic-wordpress-hardening.html) is of the utmost importance, regardless of whether you use WordPress or another CMS.

![Example of a SocGholish landing page commonly used to serve malicious downloads. ](https://blog.sucuri.net/wp-content/uploads/2024/03/example_socgholish_landing_page-650x436.png)

Example of a SocGholish fake browser updates landing page used to serve malicious downloads.

## Origins: <script> tags in wp\_postmeta

Let’s take a look at this particular variant of SocGholish: it was first identified last October, 2023, and was originally found injected using <script> tags into the **wp\_postmeta** table of the database of compromised WordPress websites:

![Injected script leverages malicious whitedrill.org domain](https://blog.sucuri.net/wp-content/uploads/2024/03/script_tag_injection-600x145.png)

Injected script leverages malicious whitedrill[.]org domain

The malicious **whitedrill[.]org** domain was registered shortly before we started seeing it injected into **wp\_postmeta** tables on infected websites.

```
$ whois whitedrill[.]org
Domain Name: whitedrill[.]org
Registry Domain ID: 5e6a5a662df24f2fbd4d5e1e17d57144-LROR
Registrar WHOIS Server: http://whois.reg.com
Registrar URL: http://www.reg.com
Updated Date: 2023-09-06T17:26:24Z
Creation Date: 2023-09-01T17:25:59Z
```

In the final quarter of 2023, this variant of Socgholish was detected by our [remote website scanner](https://sitecheck.sucuri.net/) SiteCheck over 1,400 times. By comparison, so far this year this malware has been identified in over 2,800 scans. This is a significant increase in detections — more than double the average monthly volume from last year.

The malicious JavaScript screen (captured above) in turn loads a second malicious JavaScript from another domain controlled by the attackers:

![Malicious javascript loads a second malicious JavaScript from another domain controlled by the attackers](https://blog.sucuri.net/wp-content/uploads/2024/03/malicious-javascript-650x85.png)

It appears that the stake[.]libertariancounterpoint subdomain is hosted at an entirely different IP address from the main domain.

```
$ host libertariancounterpoint[.]com
libertariancounterpoint[.]com has address 67.20.113.11

$ host stake[.]libertariancounterpoint[.]com
stake[.]libertariancounterpoint[.]com has address 185.158.251.240
```

This is quite typical for SocGholish malware campaigns and we have identified this type of “[domain shadowing](https://blog.sucuri.net/2022/08/socgholish-5-years-of-massive-website-infections.html#domain-shadowing)” technique before. Threat actors hosting their payloads on hacked domains is a common tactic they employ.

The first IP is hosted by Unified Layer in the United States, whereas the second appears to be a cloud hosting service “Servinga GmbH” in Germany.

## New wave of SocGholish found in bogus WordPress plugins

While we still see many well known SocGholish injections, last week, however, we began to see the same malware recycled in a slightly different ...