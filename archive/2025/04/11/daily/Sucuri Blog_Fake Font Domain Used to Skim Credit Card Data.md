---
title: Fake Font Domain Used to Skim Credit Card Data
url: https://blog.sucuri.net/2025/04/fake-font-domain-used-to-skim-credit-card-data.html
source: Sucuri Blog
date: 2025-04-11
fetch_date: 2025-10-06T22:03:59.843091
---

# Fake Font Domain Used to Skim Credit Card Data

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
* [Security Advisory](https://blog.sucuri.net/category/security-advisory)
* [WordPress Security](https://blog.sucuri.net/category/wordpress-security)

# Fake Font Domain Used to Skim Credit Card Data

[![](https://secure.gravatar.com/avatar/da934b974fa8adb3975fd07757f8322b04202cc98f15a625259eb3b404c1532a?s=60&d=mm&r=g)](https://blog.sucuri.net/author/kayleigh)

[Kayleigh Martin](https://blog.sucuri.net/author/kayleigh)

* April 10, 2025

![Fake Font Domain Used to Skim Credit Card Data](https://blog.sucuri.net/wp-content/uploads/2025/04/Fake-Font-Domain-Used-to-Skim-Credit-Card-Data-820x385.png)

Recently, a client of ours came to us concerned about credit card theft on their WordPress site. The client’s users reported that their credit card data had become compromised shortly after purchasing products on our client’s website.

When investigating the site, two suspicious symptoms appeared: A strange credit card form, and an unfamiliar domain, which appeared on the website’s checkout page. The suspicious domain loading on the website was **italicfonts**[**.**]**org**, which at first glance looks like a domain used for fonts. However, a quick search online didn’t show evidence of this domain being used for legitimate purposes, so it required an additional investigation.

## Investigating the suspicious domain

When searching the files for this domain, a heavily obfuscated script appeared at the bottom of the theme’s **footer.php** file, with the suspicious domain included. Additionally, the last modified date of this file was recently, which differed from the rest of the files located in the theme.

Below is the script in question:

![obfuscated footer script](https://blog.sucuri.net/wp-content/uploads/2025/04/obfuscated-footer-script.png)

Note: This is only a partial snapshot of the code.

![obfuscated footer script 2](https://blog.sucuri.net/wp-content/uploads/2025/04/obfuscated-footer-script-2.png)

Note: This is only a partial snapshot of the code.

Not only was the suspicious domain found in this code, elements of creating a credit card form were present as well. This warrants additional investigation.

Let’s break down how the code works, along with the impact it has on the site.

## How the skimmer works

First, let’s discuss the key elements found in the script:

1. The attacker injects a script into the checkout page, which includes the malicious domain italicfonts[.]org.
2. The code then creates a fake credit card form.
3. The skimmer listens for input events on the credit card fields and stores the data in various variables.
4. After capturing the credit card details, the data is then sent to the attacker’s server.

Now let’s examine the important malware’s structure and behavior in depth.

### 1) Injecting the malicious domain italicfonts[.]org into the site:

![injected malicious domain](https://blog.sucuri.net/wp-content/uploads/2025/04/injected-malicious-domain.png)

This script is loaded from the malicious domain and runs when the page is accessed. There are clues to help determine if the domain italicfonts[.]org is indeed malicious. One clue we can use is to search for the domain itself by using Google. We can input site:italicfonts[.]org into the search engine to see if there are any indexed pages of the domain. If spammy results come up, or none at all, that can be questionable. Here are the results for this particular domain on Google:

![google domain search](https://blog.sucuri.net/wp-content/uploads/2025/04/google-domain-search.png)

Another clue to narrow down our investigation is to look when the domain was registered. New domains can be a sign of malicious behavior as attackers cycle through domains quickly to avoid detection as long as possible. The domain italicfonts[.]org was registered just a few months ago:

![malicious domain whois](https://blog.sucuri.net/wp-content/uploads/2025/04/malicious-domain-whois.png)

Three variables can be good indicators this domain is being used for malicious purposes.

1. The domain was registered recently
2. No indexed results appear for this domain
3. It is located within a fake credit card form

To avoid detection even further, the attacker chose a domain mimicking a real font website. This can easily go unnoticed because at first glance the domain appears legitimate.

We now can determine this domain is malicious, and this is likely where the exfiltrated credit card details are being sent to. Next, let’s review the fake credit card form that is created.

### 2) Creating the fake credit card form

Let’s review the fake credit card form. Below is a chunk of the script that builds the form and includes fields like billing postc...