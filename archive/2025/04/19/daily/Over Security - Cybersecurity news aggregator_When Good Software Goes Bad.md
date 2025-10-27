---
title: When Good Software Goes Bad
url: https://blog.sucuri.net/2025/04/when-good-software-goes-bad.html
source: Over Security - Cybersecurity news aggregator
date: 2025-04-19
fetch_date: 2025-10-06T22:07:28.578082
---

# When Good Software Goes Bad

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
* [WordPress Security](https://blog.sucuri.net/category/wordpress-security)

# When Good Software Goes Bad

[![](https://secure.gravatar.com/avatar/067bd4ee574f53bb79d411d83b5cc84ea794c798f945cb84a001cbe05fee65df?s=60&d=mm&r=g)](https://blog.sucuri.net/author/matt-morrow)

[Matt Morrow](https://blog.sucuri.net/author/matt-morrow)

* April 17, 2025

![When Good Software Goes Bad](https://blog.sucuri.net/wp-content/uploads/2025/04/When-Good-Software-Goes-Bad-820x385.png)

Most often bad actors try their best to hide their activities by using obfuscated code or by uploading fake plugins or themes that inject simple but malicious scripts into a site. Every now and then we encounter a case where legitimate software is used for malicious purposes.

We recently uncovered a case where [Sypex Dumper](https://sypex.net/), a valid database backup utility, was injected into the WordPress files. When checking the core WordPress integrity, we noticed a file at **wp-content/fonts/font.php**. A couple of things immediately made this suspicious – WordPress doesn’t store any fonts in the wp-content directory, and the file name seems to have been used to look similar to a valid **fonts.php** that would usually be found at **wp-includes/fonts.php**. Attackers will often use naming conventions that might easily be overlooked or hide in the mix of other valid files.

Upon examining the file, it was clear that this was a modified copy of the official Sypex utility intended to create a backdoor into the site.

![modified Sypex in fonts.php](https://blog.sucuri.net/wp-content/uploads/2025/04/modified-sypex-in-fonts-php.png)

When downloading an official copy of the Sypex utility, we find a number of files like **sxd.js** and **cfg.php** which provide functionality to the utility. Our attackers have taken each of these files and embedded them into a single file.

![combined file](https://blog.sucuri.net/wp-content/uploads/2025/04/combined-file.png)

When **wp-content/fonts/font.php** is loaded, a function is called that creates individual files from the encoded contents, replicating the original structure of the Sypex utility.

![function called](https://blog.sucuri.net/wp-content/uploads/2025/04/function-called.png)

Another point of interest is that Sypex Dumper no longer appears to be maintained as we can see in the original version.

![Sypex Dumper version](https://blog.sucuri.net/wp-content/uploads/2025/04/sypex-dumper-version.png)

Attackers often make use of old or outdated software since they often lack current security fixes.

## Legitimate Tools as Attack Vectors

This compromise of a simple utility is not an isolated incident but part of a broader pattern. Legitimate tools can become dangerous attack vectors when vulnerabilities, misconfigurations, or neglect come into play. For example, [outdated Adminer scripts](https://blog.sucuri.net/2019/11/vulnerable-versions-of-adminer-as-a-universal-infection-vector.html) have been exploited to steal database credentials and inject malicious code across sites, while a [development oversight in the File Manager plugin](https://blog.sucuri.net/2020/09/critical-vulnerability-file-manager-affecting-700k-wordpress-websites.html) left over 700,00 WordPress sites vulnerable to a complete takeover.

While software like this does not have a direct impact on the functionality of a site, it can be used to extract sensitive data like the site’s database which can later be used for additional attacks or to extract details like admin users and passwords.

One of the most important steps to maintaining a clean and secure site is to regularly check plugins, themes and other software that has been added to the site. This can be done with various tools like [Sucuri Security](https://wordpress.org/plugins/sucuri-scanner/) which will notify for changes to core files and when plugins were installed or modified. Other [plugins](https://wordpress.org/plugins/user-activity-log/) can be used to record when users log in to wp-admin.

## Wrapping Up

There are a number of steps that should be taken regularly to ensure the safety of your site.

* Keep all software (themes. Plugins, core files) up to date. Attackers are always looking for vulnerabilities and can often exploit even undocumented vulnerabilities
* Review all admin users periodically to ensure that old unwanted accounts are no longer left behind, and that no new unwanted users have been added
* Regularly change passwords for any admin account – wp-admin or other administrative panels, FTP/sFTP, CPanel and other locations where someone can login to the backend of the site or server
* Place your site behind a [Firewall](https://sucu...