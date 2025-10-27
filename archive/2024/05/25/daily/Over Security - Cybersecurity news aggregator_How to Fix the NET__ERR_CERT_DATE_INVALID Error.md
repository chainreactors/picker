---
title: How to Fix the NET::ERR_CERT_DATE_INVALID Error
url: https://blog.sucuri.net/2024/05/fix-err_cert_date_invalid_error.html
source: Over Security - Cybersecurity news aggregator
date: 2024-05-25
fetch_date: 2025-10-06T17:18:44.410302
---

# How to Fix the NET::ERR_CERT_DATE_INVALID Error

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
* [Website Security](https://blog.sucuri.net/category/website-security)

# How to Fix the NET::ERR\_CERT\_DATE\_INVALID Error

[![](https://secure.gravatar.com/avatar/b2a47b57affd449fb66751c7eec943a5943c2ebaa128f8ba6926982c6e066627?s=60&d=mm&r=g)](https://blog.sucuri.net/author/rianna)

[Rianna MacLeod](https://blog.sucuri.net/author/rianna)

* May 24, 2024

![](https://blog.sucuri.net/wp-content/uploads/2024/05/Blog-Post-NET__ERR_CERT_DATE_INVALID-820x385.png)

Encountering the NET::ERR\_CERT\_DATE\_INVALID error can be frustrating, but it’s important to address it promptly to ensure your website remains secure and trustworthy. This error typically indicates an issue with your website’s SSL/TLS certificate, which is essential for encrypting data and ensuring a secure connection between your website and its visitors. When this error occurs, users might be deterred from visiting your site, potentially harming your reputation and causing a loss of traffic.

Understanding and resolving this error is important — not just for the security of your website but also for maintaining the confidence of your users.

In this post, we’ll explain the different types of this error across various browsers and provide step-by-step solutions to fix it. Whether you’re a seasoned website owner or new to managing a site, these tips will help you troubleshoot and resolve the NET::ERR\_CERT\_DATE\_INVALID error.

**Contents:**

* [What is the NET::ERR\_CERT\_DATE\_INVALID error?](#what-is-err_cert_date_invalid_error)
* [Common causes of NET::ERR\_CERT\_DATE\_INVALID](#common-causes)
* [How to fix the NET::ERR\_CERT\_DATE\_INVALID Error](#how-to-fix)
* [Troubleshooting steps for website owners](#troubleshooting-website)
* [NET::ERR\_CERT\_DATE\_INVALID and Let’s Encrypt](#lets-encrypt)

## What is the NET::ERR\_CERT\_DATE\_INVALID error?

The NET::ERR\_CERT\_DATE\_INVALID error is a common SSL/TLS certificate error that occurs when your browser cannot verify the security certificate of the website you are trying to visit. This error typically indicates that the SSL/TLS certificate is either expired, not yet valid, or its validity period does not match the current date and time settings on your device.

SSL/TLS certificates are essential for establishing a secure connection between a web server and a browser. They encrypt data exchanged between the user and the website, ensuring privacy and security. When there is an issue with the certificate, browsers like Chrome, Firefox, Edge, and Safari will display the NET::ERR\_CERT\_DATE\_INVALID error to warn users that their connection might not be secure.

![Example of an NET::ERR_CERT_DATE_INVALID error. ](https://blog.sucuri.net/wp-content/uploads/2024/05/err-ssl.png)

Example of an NET::ERR\_CERT\_DATE\_INVALID error.

## Common Causes of the NET::ERR\_CERT\_DATE\_INVALID Error

This error can arise from various causes, such as an expired certificate, incorrect system date and time, misconfigured server settings, or problems with intermediate certificates.

### Expired SSL/TLS certificate

SSL/TLS certificates have a validity period and must be renewed regularly. When a certificate expires, the browser can no longer verify that your website is secure, leading to the NET::ERR\_CERT\_DATE\_INVALID error. It’s essential to monitor your certificate’s expiration date and renew it before it lapses to avoid this issue.

### Incorrect system date and time

Your browser relies on your computer’s clock to verify SSL/TLS certificates. If your system’s date and time are incorrect, it can cause your browser to think the certificate is invalid, even if it’s not. Ensuring your computer’s date and time are accurate can prevent this error.

### Misconfigured server settings

Sometimes, server settings can be misconfigured, leading to SSL/TLS certificate errors. This can include incorrect domain names, missing intermediate certificates, or outdated server software. Regularly checking and updating your server settings can help prevent these configuration issues.

### Intermediate certificate issues

SSL/TLS certificates often rely on intermediate certificates to establish a chain of trust from the certificate authority to your website. If these intermediate certificates are missing or incorrectly installed, your browser might not trust your SSL certificate, resulting in the NET::ERR\_CERT\_DATE\_INVALID error. Ensuring all necessary intermediate certificates are properly installed on your server can resolve this issue.

## How to fix the NET::ERR\_CERT\_DATE\_INVALID error

Now, let’s get to work on fixing this error. Here are eleven steps you can try:

### 1. Click the Advanced button ...