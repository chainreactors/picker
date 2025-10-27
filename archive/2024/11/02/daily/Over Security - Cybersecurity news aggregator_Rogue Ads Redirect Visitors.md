---
title: Rogue Ads Redirect Visitors
url: https://blog.sucuri.net/2024/10/rogue-ads-redirect-visitors.html
source: Over Security - Cybersecurity news aggregator
date: 2024-11-02
fetch_date: 2025-10-06T19:19:58.840365
---

# Rogue Ads Redirect Visitors

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
* [WordPress Security](https://blog.sucuri.net/category/wordpress-security)

# Rogue Ads Redirect Visitors

[![](https://secure.gravatar.com/avatar/067bd4ee574f53bb79d411d83b5cc84ea794c798f945cb84a001cbe05fee65df?s=60&d=mm&r=g)](https://blog.sucuri.net/author/matt-morrow)

[Matt Morrow](https://blog.sucuri.net/author/matt-morrow)

* October 31, 2024

![Rogue Ads Redirect Visitors](https://blog.sucuri.net/wp-content/uploads/2024/10/Rogue-Ads-Redirect-Visitors-820x385.png)

Ads are everywhere. They generate revenue for site owners and can present related content to the website being visited. As detailed in previous [articles](https://blog.sucuri.net/2017/03/vbulletin-used-show-malicious-advertisements.html), bad actors often take advantage of that functionality. Quite often rogue ad networks will be used to pull down malicious content, but recently we’ve seen a campaign where the threat actors are utilizing popular services like Github and Bitbucket to store their rogue ad sources.

## The injection

WordPress and other CMS will often utilize plugins to insert header content directly from the admin panel, making it easy for developers and non-developers alike to add functionality to their sites. In this case, we discovered a simple script that pulls down spam and phishing ads.

![header script](https://blog.sucuri.net/wp-content/uploads/2024/10/header-script.png)

Here we can see that a txt file, located on a personal BitBucket repository, is being assigned to the ***url*** variable and then passed to the ***fetch*** function, which when called returns a JSON dataset. The dataset **response** contains the text located at that remote location. In this case, if we load that URL directly we can see a suspicious domain.

![suspicious domain](https://blog.sucuri.net/wp-content/uploads/2024/10/suspicious-domain.png)

After the remote text has been retrieved, that is injected into the site’s header.

![injected header script](https://blog.sucuri.net/wp-content/uploads/2024/10/injected-header-script.png)

## The Result

Once the script has been injected into the header of the site, it inserts rogue ads that can potentially redirect visitors to additional malicious resources. If the attackers choose to do so, they could even insert silent malware like credit card and credential stealing scripts. Because the script content resides on an external server, the attackers have full control over when and if the script content changes.

## Wrapping up

It is important to vet all scripts and external resources loading on the site to prevent abuse. Javascript-based malware has accounted for almost 300,000 [cases we have investigated](https://sucuri.net/documentation/Sucuri-Mid-Year-2024.pdf) in 2024 alone. One way to check this is to use external scanners like [urlscan.io](http://urlscan.io) and [WebPageTest](https://www.webpagetest.org/) which will provide a comprehensive overview of all resources loading in the site along with their initiating sources.

There are a number of preventative measures that should be taken on all websites.

* **Keep your plugins, themes, and website software up-to-date.** Always patch to the latest version to help mitigate risk known [software vulnerabilities](https://blog.sucuri.net/category/vulnerability-disclosure). Website visitors should be sure to keep their browser and operating system up to date as well.
* **Regularly scan for backdoors and malware.** That means scanning at the [server and client level](https://blog.sucuri.net/2021/05/server-side-scans-and-file-integrity-monitoring.html) to identify any malicious injections, SEO spam, or backdoors that may be lurking on your site. Our [Website Security plans](https://sucuri.net/lp/sem/ga-website-security-platform/) include a [server-side scanner](https://docs.sucuri.net/website-monitoring/server-side-scanner/) that runs multiple times per day to check for changed files and injected malware.
* **Enforce [unique passwords](https://blog.sucuri.net/2022/08/how-to-create-secure-passwords-for-your-website.html) for all of your accounts.** That includes credentials for sFTP, database, cPanel, and admin users.
* **Monitor your logs for indicators of compromise.** Regularly check for unusual or suspicious behavior and consider using a [file integrity monitoring](https://sl.wordpress.org/plugins/sucuri-scanner/) system on your website.
* **Get a web application firewall (WAF).** Firewalls can help mitigate bad bots, [prevent brute force attacks,](https://sucuri.net/guides/what-is-brute-force-attack/) and detect attacks in your environment, which are features the Sucuri firewall provides.

And if you believe your site...