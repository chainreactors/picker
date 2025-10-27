---
title: Fake WordPress Caching Plugin Used to Steal Admin Credentials
url: https://blog.sucuri.net/2025/06/fake-wordpress-caching-plugin-used-to-steal-admin-credentials.html
source: Over Security - Cybersecurity news aggregator
date: 2025-06-06
fetch_date: 2025-10-06T22:56:49.951648
---

# Fake WordPress Caching Plugin Used to Steal Admin Credentials

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

* [Security Advisory](https://blog.sucuri.net/category/security-advisory)
* [Website Malware Infections](https://blog.sucuri.net/category/website-malware-infections)
* [WordPress Security](https://blog.sucuri.net/category/wordpress-security)

# Fake WordPress Caching Plugin Used to Steal Admin Credentials

[![](https://secure.gravatar.com/avatar/067bd4ee574f53bb79d411d83b5cc84ea794c798f945cb84a001cbe05fee65df?s=60&d=mm&r=g)](https://blog.sucuri.net/author/matt-morrow)

[Matt Morrow](https://blog.sucuri.net/author/matt-morrow)

* June 4, 2025

![Fake WordPress Caching Plugin Used to Steal Admin Credentials](https://blog.sucuri.net/wp-content/uploads/2025/06/Fake-WordPress-Caching-Plugin-Used-to-Steal-Admin-Credentials-820x385.png)

A common trend we see is that [bad actors](https://blog.sucuri.net/2025/05/what-motivates-website-malware-attacks.html) will upload malicious plugins to WordPress sites. These plugins serve a wide variety of functions from injecting spam to redirecting sites to other malicious content. In this article we will examine a more dangerous method where plugins can be used to steal admin credentials.

# Identifying the malware

During a routine malware scan we noticed a plugin labeled **wp-runtime-cache** in the wp-content/plugins directory. Seems innocent enough, right? After all, just about every site has at least one layer of cache to help with performance. When caching plugins are installed, you’ll usually find some menu to manage that at the top of the wp-admin panel or there will be some option under **Settings** on the left menu when logged in.

![typical caching plugin settings](https://blog.sucuri.net/wp-content/uploads/2025/06/caching-plugin-settings-e1749075699940-600x565.png)

We did not see any options for clearing cache and the plugin didn’t show up in the installed plugins list inside of wp-admin. It’s not uncommon for attackers to hide malicious plugins so this definitely warranted a further investigation.

Taking a look at the **wp-runtime-cache** directory, we could see one file: **wp-runtime-cache.php**. That’s also quite unusual since any valid plugin is going to utilize additional PHP and JS files for functionality. I mentioned we have seen a trend of utilizing malicious plugins, and in many cases those malicious plugin directories only include one file containing the malicious code.

Let’s take a look at the plugin.

![fake cache plugin](https://blog.sucuri.net/wp-content/uploads/2025/06/fake-cache-plugin.png)

Right off the bat we can see a few red flags.

* The plugin description, author and URL are empty. In any valid plugin the vendor will identify themselves and will usually provide the plugin source URL or at least a location to a support page.
* We see some base64 content, a trademark of malware
* The plugin is utilizing random variable names, like **woocomHeic0971** and **pbes2PITR0339**. We also see an interesting variable: **infiltrateDocumentStore0460**. I can’t think of any single legitimate case where a valid plugin would want to secretly infiltrate any content.

Just a bit of clarification here: it’s not extremely uncommon for software vendors to use base64 obfuscation in premium plugins and themes. Typically, however, either the majority of the code will be obfuscated or they will obfuscate a specific line containing a license key and the line containing that obfuscation will be labeled as such.

# Working through the plugin

Because this malware is running as a plugin it is executed every time the site loads on any page, including wp-admin. The first line of code instructs the plugin to run a set of tasks in the **octopusJson50286** function whenever someone logs in to wp-admin.

**add\_action(‘wp\_login’, ‘octopusJson50286’, 10, 2);**

That function accepts two variables, **woocomHeic0971** and **ntpExcerpt0821**.

**function octopusJson50286($woocomHeic0971, $ntpExcerpt0821)**

Let’s work out what values those variables are storing. Further down the malicious function, we can see it is building an array of data from the user login details.

![data array from user login details](https://blog.sucuri.net/wp-content/uploads/2025/06/data-array-from-user-login-details.png)

Here we can see the first variable passed to the function – **woocomHeic0971** – when it is called at login stores the submitted username. The second variable, **ntpExcerpt0821**, is defined as an object to contain an array of predefined user capabilities or roles. We also see a variable defining very specific roles to be checked for.

![checking for specific roles](https://blog.sucuri.net/wp-content/uploads/2025/06/checking-for-specific-roles-scaled.png)

Decoding those two base64 values, we come up with the following.

* **bWFuYWdlX29wdGlv...