---
title: Critical Security Update for Magento Open Source & Adobe Commerce
url: https://blog.sucuri.net/2023/08/critical-security-update-for-magento-adobe-commerce.html
source: Over Security - Cybersecurity news aggregator
date: 2023-08-18
fetch_date: 2025-10-04T12:00:31.284473
---

# Critical Security Update for Magento Open Source & Adobe Commerce

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
* [Magento Security](https://blog.sucuri.net/category/magento-security)
* [Vulnerability Disclosure](https://blog.sucuri.net/category/vulnerability-disclosure)

# Critical Security Update for Magento Open Source & Adobe Commerce

[![](https://secure.gravatar.com/avatar/49a04d32074892dc04d9ed823aa114f8492a90e9c88852302b083c90aa322c21?s=60&d=mm&r=g)](https://blog.sucuri.net/author/benmartin)

[Ben Martin](https://blog.sucuri.net/author/benmartin)

* August 16, 2023

![Critical Security Update for Magento Open Source & Adobe Commerce](https://blog.sucuri.net/wp-content/uploads/2023/08/Security-Update-820x385.png)

Last week on August 8th, 2023, Adobe released a [critical security patch](https://helpx.adobe.com/security/products/magento/apsb23-42.html) for Adobe Commerce and the Magento Open Source CMS. The patch provides fixes for three [zero-day vulnerabilities](https://blog.sucuri.net/2024/04/what-is-a-zero-day-vulnerability.html) which affect the popular ecommerce platforms. Successful exploitation could lead to arbitrary code execution, privilege escalation and arbitrary file system read.

Affected versions of Magento Open Source are as follows:

* 2.4.6-p1 and earlier
* 2.4.5-p3 and earlier
* 2.4.4-p4 and earlier

Website administrators are advised to update their software immediately to mitigate risk to their Magento and Adobe Commerce environments.

## Vulnerability details

### OS Command Injection

```
Security Risk: Critical
Base Score: 9.1
Exploitation Level: Requires Admin authentication.
Vulnerability: Arbitrary Code Execution
CVE: CVE-2023-38208
```

Originally reported to Adobe by researcher **Blaklis**, CVE-2023-38208 is the most severe vulnerability fixed in this latest update. If left unpatched, it can lead to arbitrary code execution by an authenticated Admin user, potentially allowing a bad actor to execute commands in the targeted environment.

It’s not uncommon for attackers to create malicious administrator accounts within compromised Magento environments. If an attacker is already able to authenticate into an admin account then the environment is already compromised, but this vulnerability would allow attackers even more leeway and control over the environment.

---

### Improper Access Control

```
Security Risk: Medium
Base score: 6.5
Exploitation Level: Requires low-level authentication.
Vulnerability: Privilege Escalation
CVE: CVE-2023-38209
```

Originally reported to Adobe by researcher **wohlie**, CVE-2023-38209 is a medium level vulnerability that occurs due to improper access restrictions for unauthorized users. If left unpatched, it can allow low-privilege users to access other user’s data within the Magento environment.

---

### XML Injection / Blind XPath Injection

```
Security Risk: Medium
Base score: 5.3
Exploitation Level: No authentication required.
Vulnerability: Arbitrary File System Read
CVE: CVE-2023-38207
```

Originally reported to Adobe by researcher **wohlie**, CVE-2023-38207 is a medium level vulnerability that occurs because special elements used in XML are not properly neutralized. If left unpatched, it can lead to minor arbitrary file system read in the Magento environment.

---

## Mitigation steps

All three of these vulnerabilities could result in exploitation by attackers if left unpatched. Updating Adobe Commerce and Magento Open Source to the latest security release will help fix these security flaws and mitigate risk to your Magento environment.

Magento users should update their software to the following versions:

* **Magento Open Source 2.4.6-p2** for versions **2.4.6** and earlier
* **Magento Open Source 2.4.5-p4** for versions **2.4.5-p3** and earlier
* **Magento Open Source 2.4.4-p5** for versions **2.4.4-p3** and earlier

If you believe your Magento environment has already been compromised or infected with malware, we can help. Reach out to our team to [chat with our remediation specialists](https://sucuri.net/live-chat/).

[![](https://secure.gravatar.com/avatar/49a04d32074892dc04d9ed823aa114f8492a90e9c88852302b083c90aa322c21?s=120&d=mm&r=g)](https://blog.sucuri.net/author/benmartin)

##### [Ben Martin](https://blog.sucuri.net/author/benmartin)

Ben Martin is a security analyst and researcher who joined the company in 2013. Ben's main responsibilities include finding new undetected malware, identifying trends in the website security world, and, of course, cleaning websites. His professional experience covers more than a decade of working with infected websites of every variety with a special focus on eCommerce / credit card theft malware. When Ben isn't slaying malware you might find him producing music, gardening, or skateb...