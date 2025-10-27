---
title: Hidden WordPress Backdoors Creating Admin Accounts
url: https://blog.sucuri.net/2025/09/hidden-wordpress-backdoors-creating-admin-accounts.html
source: Over Security - Cybersecurity news aggregator
date: 2025-09-25
fetch_date: 2025-10-02T20:39:53.133180
---

# Hidden WordPress Backdoors Creating Admin Accounts

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

# Hidden WordPress Backdoors Creating Admin Accounts

[![](https://secure.gravatar.com/avatar/3bb7fb42c6bf04c758d570c2f6bb217266c127e77766dc9d8e6754f15cdd5867?s=60&d=mm&r=g)](https://blog.sucuri.net/author/puja-srivastava)

[Puja Srivastava](https://blog.sucuri.net/author/puja-srivastava)

* September 23, 2025

![Hidden WordPress Backdoors Creating Admin Accounts](https://blog.sucuri.net/wp-content/uploads/2025/09/Hidden-WordPress-Backdoors-Creating-Admin-Accounts-820x385.png)

During a recent cleanup of a compromised WordPress website, we discovered two different malicious files designed to silently manipulate administrator accounts. Attackers often inject such backdoors to maintain persistent access to a site, even if their other malware is detected and removed. These files were disguised to look like regular WordPress components, but their functionality told a different story.

## What did we find?

We found two highly suspicious files that immediately caught our attention. Each played a crucial role in maintaining unauthorized access for the attackers.

**1) ./wp-content/plugins/DebugMaster/DebugMaster.php:** This file tried to look like a legitimate plugin, naming itself “DebugMaster Pro”. However, its contents were heavily scrambled and clearly malicious.

![DebugMaster](https://blog.sucuri.net/wp-content/uploads/2025/09/DebugMaster.png)

**2) ./wp-user.php:** This file was found masquerading as a core WordPress file. It’s much simpler but no less dangerous.

![wp-user.php](https://blog.sucuri.net/wp-content/uploads/2025/09/wp-user.png)

## What Was the Malware Doing?

Both of these files had one main goal: to make sure the attackers always had a way back into the WordPress site as an administrator.

The **DebugMaster.php** file was a complex, hidden backdoor. It created a secret admin user.

The **wp-user.php** file was simpler but aggressive. It made sure a specific admin user with a known password was always present. If you tried to delete this user, it would simply recreate it!

Together, these files created a robust system for persistent access, allowing attackers to control the site, potentially inject spam, redirect visitors, or steal information.

## Analysis of the Malware

### 1. Fake Plugin i.e. DebugMaster Pro

This “DebugMaster Pro” plugin disguised itself as a legitimate developer tool, but its hidden functions created an administrator user with hardcoded credentials. It also included code to hide itself from plugin listings and could send stolen information to a remote server. In short, it acted as a stealthy backdoor while pretending to be harmless.

The first file was disguised as a plugin with fake metadata. However, deeper inside the file, we found code responsible for creating a new administrator account:

![code creating new admin](https://blog.sucuri.net/wp-content/uploads/2025/09/code-creating-new-admin.png)

This decodes to:

![code creating new admin decoded](https://blog.sucuri.net/wp-content/uploads/2025/09/admin-creation-decoded.png)

This snippet forces WordPress to create a new user named help with the role of administrator. If the user already exists, the script ensures it has administrator privileges restored.

This simple trick allows attackers to slip in unnoticed by posing as a plugin that administrators might ignore.

To remain hidden, the plugin removed itself from plugin listings and filtered user queries to hide the newly created admin account:

![hiding admin account](https://blog.sucuri.net/wp-content/uploads/2025/09/hiding-admin-account.png)

This decodes to:

![hiding admin account decoded](https://blog.sucuri.net/wp-content/uploads/2025/09/hiding-admin-account-decoded.png)

### 2. Communicates with a Command & Control (C2) Server

The malware sends the new administrator account’s details to an external server controlled by the attackers.

![sending to external server](https://blog.sucuri.net/wp-content/uploads/2025/09/sending-to-external-server.png)

This decodes to:

![sending to external server decoded](https://blog.sucuri.net/wp-content/uploads/2025/09/sending-to-external-server-decoded.png)

It encodes the generated username, password, email, and the server’s IP into JSON, then Base64-encodes it.

It then sends this information to a remote endpoint. The endpoint URL is also obfuscated using base64 encoding which decodes to something like **hxxps://kickstar-xbloom[.]info/collect[.]php**. This allows the attackers to immediately know the credentials of the new admin user.

T...