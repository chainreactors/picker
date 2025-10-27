---
title: New Guide on Secure VPS Configuration
url: https://blog.sucuri.net/2023/07/new-guide-on-secure-vps-configuration.html
source: Over Security - Cybersecurity news aggregator
date: 2023-07-05
fetch_date: 2025-10-04T11:55:09.641056
---

# New Guide on Secure VPS Configuration

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

* [Security Education](https://blog.sucuri.net/category/security-education)
* [Web Pros](https://blog.sucuri.net/category/web-pros)
* [Website Security](https://blog.sucuri.net/category/website-security)
* [WordPress Security](https://blog.sucuri.net/category/wordpress-security)

# New Guide on Secure VPS Configuration

[![](https://secure.gravatar.com/avatar/49a04d32074892dc04d9ed823aa114f8492a90e9c88852302b083c90aa322c21?s=60&d=mm&r=g)](https://blog.sucuri.net/author/benmartin)

[Ben Martin](https://blog.sucuri.net/author/benmartin)

* July 4, 2023

![VPS Security Guide](https://blog.sucuri.net/wp-content/uploads/2023/07/sucuri_vps-820x383.png)

One of the most common problems that we observe among many of our clients is the persistent threat of cross contamination – that is, malware that spreads from one website to another when they are hosted in the same environment. This is particularly common within cPanel environments when add-on domains are used, or within improperly configured Virtual Private Servers (VPS). While we have been warning clients about the risks posed by cross contamination for many years, we haven’t yet produced any content instructing website owners on exactly how to avoid it. Fortunately, today that changes with the release of our new secure VPS configuration guide!

[![Read the Full Guide](https://blog.sucuri.net/wp-content/uploads/2022/06/22-sucuri-blog-read-the-full-guide-download-button_1-e1656437020583.png)](https://sucuri.net/guides/php-fpm-vps-security-for-multiple-websites/)

## What is cross-contamination?

When website owners first configure their hosting environment security is not always the first thing on their minds. They’re excited to get their brand new websites up and running, why would they be thinking about hackers? In fact, most often security doesn’t even cross a website owners’ minds until after they get hacked and their website is belching out malware and [blocked by Google](https://sucuri.net/guides/how-to-remove-google-blocklist-warning/).

Oftentimes website owners opt for the most easy, cheap, and convenient route to get their websites configured, after all why wouldn’t they? However, when multiple websites are all crammed into the same cPanel instance or all just thrown into the default directory of their hosting server (owned by the same user, no less) this can create a perfect environment for malware to spread between websites.

What can end up happening is that a single compromised administrator user on a WordPress site can bring down your entire fleet of websites and cause a major headache (and cost a lot of money to get repaired). Believe us, we have seen it happen many times!

Fortunately, with a little bit of know-how you can configure a secure VPS hosting environment where cross contamination is not possible, and we can do so by leveraging PHP-FPM.

## What is PHP-FPM?

PHP-FPM is an advanced FastCGI process manager for PHP, providing a significant performance boost over traditional CGI-based methods. It provides a robust and scalable architecture for PHP applications, allowing a secure separation of different websites running on the same server. This isolation is particularly useful when you’re trying to avoid cross-contamination of malware, a common issue when hosting multiple sites on the same VPS.

With a simple LEMP stack (Linux, NGINX, MySql/MariaDB, PHP), we can use NGINX in conjunction with PHP-FPM for a scalable environment to house multiple websites in a secure fashion. File permissions and ownership are only half the battle – what’s essential is that the underlying PHP process running on the server are run by **separate users**. This is the key to avoiding cross contamination!

Ideally, you’ll need to be comfy using a command line interface and SSH. But don’t worry, if you’re not familiar with that then now is the perfect time to learn!

[![Read the Full Guide](https://blog.sucuri.net/wp-content/uploads/2022/06/22-sucuri-blog-read-the-full-guide-download-button_1-e1656437020583.png)](https://sucuri.net/guides/php-fpm-vps-security-for-multiple-websites/)

## Conclusion

In the realm of cybersecurity, there’s no such thing as a ‘one-size-fits-all’ solution. However, using PHP-FPM on your VPS offers a robust and effective measure for ensuring that a security issue with one website doesn’t spill over and affect others. This setup allows us to combat the menace of cross-contamination, creating a safer, more secure digital environment.

Remember, setting up a secure environment is just the beginning. Regular monitoring and updating of your systems will help you stay ahead of potential security threats. This configuration will help prevent the spread of malware *between websites*, but it won’t prevent...