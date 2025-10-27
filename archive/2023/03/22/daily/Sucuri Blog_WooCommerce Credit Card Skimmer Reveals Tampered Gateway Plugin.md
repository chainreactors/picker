---
title: WooCommerce Credit Card Skimmer Reveals Tampered Gateway Plugin
url: https://blog.sucuri.net/2023/03/woocommerce-skimmer-reveals-tampered-gateway-plugin.html
source: Sucuri Blog
date: 2023-03-22
fetch_date: 2025-10-04T10:13:58.170734
---

# WooCommerce Credit Card Skimmer Reveals Tampered Gateway Plugin

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
* [Website Security](https://blog.sucuri.net/category/website-security)
* [WordPress Security](https://blog.sucuri.net/category/wordpress-security)

# WooCommerce Credit Card Skimmer Reveals Tampered Plugin

[![](https://secure.gravatar.com/avatar/49a04d32074892dc04d9ed823aa114f8492a90e9c88852302b083c90aa322c21?s=60&d=mm&r=g)](https://blog.sucuri.net/author/benmartin)

[Ben Martin](https://blog.sucuri.net/author/benmartin)

* March 21, 2023

![](https://blog.sucuri.net/wp-content/uploads/2022/08/BlogPost_Feature-Image_1490x700_Examining-Less-Common-WordPress-Credit-Card-Skimmers-820x386.png)

```
Disclaimer: The malware infection described in this article does not affect the software plugin as a whole and does not indicate any vulnerabilities or security flaws within WooCommerce or any associated WooCommerce plugin extensions. Overall they are both robust and secure payment platforms that are perfectly safe to use. Instead, this article highlights the importance of maintaining good security posture and keeping environments locked down to prevent tampering from threat actors.
```

[#MageCart](https://sucuri.net/guides/what-is-magecart/) is a type of malware that steals credit card data from eCommerce websites. Its name is derived from its origins on the Magento eCommerce platform. However, since the end of 2019, we have observed that this malware has been repurposed for WordPress environments, specifically those using WooCommerce. As a result, the overwhelming majority of credit card skimming malware we find on compromised eCommerce environments now targets WooCommerce.

WooCommerce is an excellent and highly customizable eCommerce platform used by over 40% of [all known online stores](https://barn2.com/blog/woocommerce-stats/). It can be used in conjunction with a wide variety of payment gateways. Plugin and payment gateway are generally considered to be secure for processing payments and safe to use, however in this blog post we will explore how even the most secure software applications can be tampered with by malicious actors to suit their own criminal goals.

## Indicators of compromise

Fraud can undermine consumer confidence in the financial system and even currencies themselves which is why it’s an important responsibility of financial institutions such as credit card companies to combat it.

Recently, a new client received a warning from their bank that their website was identified as potentially compromised: cards that had been used legitimately on their website had later been used fraudulently over the holidays (the time of year when online credit card usage and theft is most rampant). They came to us for help rectifying the issue and we got to work identifying how these cards were being stolen.

After our initial scans came up clean, we then confirmed when the first card was reported stolen, thus giving us a rough time frame as to when the compromise may have occurred. Sure enough, when inspecting some files that were modified roughly one month before the first reported card theft we found some questionable items.

```
2022-09-21 19:36:52 [REDACTED].com: Warning: File modified (multiple changes):
./wp-content/plugins/woocommerce-gateway-[redacted]/assets/js/frontend/wc-[redacted].min.js (old size: 9082; new size: 9575)
./wp-content/plugins/woocommerce-gateway-[redacted]/class-wc-[redacted].php (old size: 22680; new size: 33396).
```

The files were related to the one single payment gateway that the client was using to process payments

Just like any other piece of software, if malicious actors compromise an environment they can tamper with existing controls. For example, late last year we identified [malware](https://blog.sucuri.net/2022/10/wordfence-evasion-malware-conceals-backdoors.html) which modified a WordPress security plugin on one client’s website which prevented the plugin from issuing any malware or security warnings to the website owner, the very thing that it is expressly designed to do.

## PHP malware analysis

Let’s first inspect the following file which was tampered with by the attackers:

./wp-content/plugins/woocommerce-gateway-[redacted]/**class-wc-[redacted].php**

This is one of the primary files for a payment gateway extension for WooCommerce and facilitates the secure handling of payments within WordPress / WooCommerce environments. Injected into the bottom of the file we see this highly questionable code:

![wc_authorize_net_cim](https://blog.sucuri.net/wp-content/uploads/2023/03/Authorize_Net.png)

Something about this just doesn’t seem right. In particular, the fact that it’s mentioning a very specific .jpg file within the wp-content/uploads directory ...