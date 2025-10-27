---
title: What is XML-RPC? Security Risks & How to Disable
url: https://blog.sucuri.net/2023/05/what-is-xml-rpc-security-risks-how-to-disable.html
source: 
date: 2023-05-05
fetch_date: 2025-10-04T11:38:49.048491
---

# What is XML-RPC? Security Risks & How to Disable

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

# What is XML-RPC? Security Risks & How to Disable

[![](https://secure.gravatar.com/avatar/b2a47b57affd449fb66751c7eec943a5943c2ebaa128f8ba6926982c6e066627?s=60&d=mm&r=g)](https://blog.sucuri.net/author/rianna)

[Rianna MacLeod](https://blog.sucuri.net/author/rianna)

* May 4, 2023

![](https://blog.sucuri.net/wp-content/uploads/2023/05/23-BlogPost_Feature-Image_1490x700_What-is-XML-RPC_A-Guide-to-xml-rpc.php_Security-Risks-How-to-Disable-820x386.jpg)

XML-RPC is a protocol designed for WordPress to standardize communication between different systems, allowing external applications (such as other blogging platforms and desktop clients) to interact with WordPress. This feature has been a part of WordPress since its early days, enabling seamless integration with the rest of the online world.

However, the **xmlrpc.php** file, which is responsible for implementing the XML-RPC protocol in WordPress, has its drawbacks. It can introduce vulnerabilities to your WordPress site and has now been largely replaced by the more advanced and secure [WordPress REST API](https://developer.wordpress.org/rest-api/), which also facilitates communication between WordPress and other applications.

In this article, we will discuss what xmlrpc.php is, why disabling it can improve your website’s security, and how to determine if it’s currently active on your WordPress site.

## What is the xmlrpc.php file?

XML-RPC is a protocol that facilitates communication between WordPress and other systems by standardizing these interactions, utilizing HTTP for transport and XML for encoding. This specification predates WordPress itself, as it was initially present in the b2 blogging software, which eventually evolved into WordPress in 2003. The code for this system resides in a file named **xmlrpc.php**, located in the root directory of a WordPress website. Although XML-RPC is now largely outdated, it continues to exist in WordPress installations.

[![Contents of xmlrpc.php file](https://blog.sucuri.net/wp-content/uploads/2023/05/xml-rpc-contents.png)](https://blog.sucuri.net/wp-content/uploads/2023/05/xml-rpc-contents.png)

Contents of xmlrpc.php

In the early iterations of WordPress, XML-RPC was disabled by default. However, starting with version 3.5, it became enabled by default to allow the WordPress mobile app to communicate with WordPress installations. Before this version, users needed to enable XML-RPC on their websites for the mobile app to post content, as the app functioned as a separate entity communicating with the WordPress site via **xmlrpc.php**.

XML-RPC was not limited to the mobile app; it also facilitated communication between WordPress and other blogging platforms, enabled trackbacks and pingbacks, and powered the Jetpack plugin connecting self-hosted WordPress sites to wordpress.com. However, with the integration of the REST API into WordPress core, the use of **xmlrpc.php** for communication has become obsolete — the REST API offers significantly more compatibilities and flexibility.

Due to the REST API’s broader capabilities and its replacement of XML-RPC, it is now recommended to disable **xmlrpc.php** on your website to mitigate risk. Let’s explore the reasons for this change.

## Reasons to disable xml-rpc.php on WordPress

With the advent of the REST API, XML-RPC is no longer needed for external communication in WordPress, making it wise to disable it as it can introduce security vulnerabilities and be the target of various attacks.

Let’s delve deeper into the specific vulnerabilities associated with the **xmlrpc.php** file.

### Brute force via xmlrpc.php

[Brute force attacks](https://sucuri.net/guides/what-is-brute-force-attack/) involve hackers attempting to gain access to a website’s backend by trying thousands of username and password combinations until they find the correct credentials. Websites with weak admin passwords and lacking multi-factor authentication are particularly vulnerable to such attacks.

Attackers can use automated tools to find and list all valid usernames for a website. Once they have this information, they can exploit the **xmlrpc.php** file to carry out a brute force attack by sending requests with various password combinations. If a website’s security measures are inadequate, hackers don’t even need to bypass reCaptchas or worry about limited login attempts. This could potentially allow hackers to gain unauthorized access to your site, posing a significant securit...