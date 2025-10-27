---
title: Malicious WordPress Plugin Creates Hidden Admin User Backdoor
url: https://blog.sucuri.net/2025/06/malicious-wordpress-plugin-creates-hidden-admin-user-backdoor.html
source: Over Security - Cybersecurity news aggregator
date: 2025-06-22
fetch_date: 2025-10-06T22:53:05.427080
---

# Malicious WordPress Plugin Creates Hidden Admin User Backdoor

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

# Malicious WordPress Plugin Creates Hidden Admin User Backdoor

[![](https://secure.gravatar.com/avatar/067bd4ee574f53bb79d411d83b5cc84ea794c798f945cb84a001cbe05fee65df?s=60&d=mm&r=g)](https://blog.sucuri.net/author/matt-morrow)

[Matt Morrow](https://blog.sucuri.net/author/matt-morrow)

* June 20, 2025

![Malicious WordPress Plugin Creates Hidden Admin User Backdoor](https://blog.sucuri.net/wp-content/uploads/2025/06/Fake-Admin-Plugin-820x385.png)

I recently [wrote about a case](https://blog.sucuri.net/2025/06/fake-wordpress-caching-plugin-used-to-steal-admin-credentials.html) where a malicious plugin was used to steal admin credentials. Here we will examine yet another malicious plugin that creates a malicious admin user right in the website.

# Examining the malware

While examining the site, we noticed a plugin located at wp-content/plugins labeled **php-ini.php**. This is strange since directories generally don’t contain extensions, especially one like **.php** since those are reserves for files. The plugin contained one file, also named **php-ini.php**. Upon checking the plugin file, we immediately noticed that the plugin description and author did not match the plugin name.

![suspicious plugin file](https://blog.sucuri.net/wp-content/uploads/2025/06/suspicious-plugin-file-scaled.png)

While the plugin at **[wpforms.com](http://wpforms.com)** is a premium version, we can find a free version of the plugin in the [WordPress repositories](https://wordpress.org/plugins/wpforms-lite/). We can see from there that the official plugin contains much more content than a single file, including an appropriately named **wpforms.php**, which is standard for valid plugins. A common trend for bad actors is to copy real plugins and either insert malicious code or completely replace all of the PHP content with their own code so that it will be more difficult to identify fake or maliciously altered plugins.

![wpforms files](https://blog.sucuri.net/wp-content/uploads/2025/06/wpforms-files.png)

The attackers didn’t put much effort into this attack, they commented out the majority of the file and left their malware in just a few lines in the center of the file.

![malware in the center](https://blog.sucuri.net/wp-content/uploads/2025/06/malware-in-the-center.png)

# Breaking it down

[**add\_action()**](https://developer.wordpress.org/reference/functions/add_action/) is a core WordPress function that launches specific code or functionality at various points in the site. Because this is placed in a plugin, the action would be launched whenever the plugin is loaded, typically on every page. The call to **add\_action()** here invokes the content located in the **SECURITYDB** function just below that line and places that in the header of the site – **wp\_head**.

The first line in the **SECURITYDB** function checks to see if the URL being called contains the parameter **?5394552785=SECURITY\_DB**. In this way, the malicious admin user isn’t created every time the site loads but only when that specific URL is called. This condition may have been chosen to better hide the attacker’s intent – if the admin user is always present then a real admin user of the site may notice the new malicious user.

Interestingly, we see the attackers included the core WordPress file **wp-includes/registration.php**. While the file still exists in current WordPress versions, the use of that file was deprecated in WordPress 3.0 with that functionality being moved to **wp-includes/user.php**. We can only guess the attackers called that file so that the malware will work regardless of which WordPress version is being attacked.

The code then checks for the existence of the **mr\_administartor** and if that user doesn’t exist, proceeds to create a user with a hard coded password and administrator privileges. It is somewhat humorous that the attackers misspelled **administrator** but this flows with their lack of any attempt to better hide the malware. This is probably one of the laziest attacks we’ve seen in a while. They didn’t even include any code to hide the plugin from the wp-admin plugins list.

# Cleaning Up

This malware was straightforward to remediate, we just removed the plugin and deleted the malicious WordPress admin.

Because this malware was included in a plugin, there is a chance the attackers compromised an FTP or sFTP account to upload that directly to the server though there is a possibility that was uploaded via the wp-admin panel using an existi...