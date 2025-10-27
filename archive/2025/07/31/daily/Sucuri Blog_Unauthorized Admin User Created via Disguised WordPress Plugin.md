---
title: Unauthorized Admin User Created via Disguised WordPress Plugin
url: https://blog.sucuri.net/2025/07/unauthorized-admin-user-created-via-disguised-wordpress-plugin.html
source: Sucuri Blog
date: 2025-07-31
fetch_date: 2025-10-06T23:17:44.808791
---

# Unauthorized Admin User Created via Disguised WordPress Plugin

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

# Unauthorized Admin User Created via Disguised WordPress Plugin

[![](https://secure.gravatar.com/avatar/3bb7fb42c6bf04c758d570c2f6bb217266c127e77766dc9d8e6754f15cdd5867?s=60&d=mm&r=g)](https://blog.sucuri.net/author/puja-srivastava)

[Puja Srivastava](https://blog.sucuri.net/author/puja-srivastava)

* July 29, 2025

![Unauthorized Admin User Created via Disguised Wordpress Plugin](https://blog.sucuri.net/wp-content/uploads/2025/07/Unauthorized-Admin-User-Created-via-Disguised-Wordpress-Plugin-820x386.png)

Recently at Sucuri, we investigated a malware case reported by one of our clients. Their WordPress site was compromised, and the attacker had installed a fake plugin. Upon analysis revealed that it was a sophisticated backdoor plugin designed to create a persistent and hidden administrator account.

## What Did We Find?

The infection was located inside the WordPress plugins directory:

```
./wp-content/plugins/wp-compat/wp-compat.php
```

The plugin claimed to fix compatibility issues with newer WordPress and PHP versions. But in reality, it silently created an admin user and actively concealed it from the WordPress admin dashboard.

![fake plugin details](https://blog.sucuri.net/wp-content/uploads/2025/07/fake-plugin-details.png)

## Attack Vector & Indicators of Compromise

The attacker manually or programmatically uploaded the fake plugin into the plugins folder. Because it used a legitimate-looking name and metadata (WP Compatibility Patch), it could easily evade detection during a superficial plugin review.

**Some key indicators of compromise (IoCs):**

* + A fake plugin folder named: `wp-compat`
  + A suspicious administrator user: `adminbackup`
  + Email address: `adminbackup@wordpress.org`
  + Option stored in database: `_pre_user_id`

## Analysis of the Malware

### Creating the Admin User

On every page load, it checks if a user named “adminbackup” exists. If the user doesn’t exist, the code creates them. If the user already exists but has a different email, the plugin resets the password and updates the email address.

![Creating the Admin User](https://blog.sucuri.net/wp-content/uploads/2025/07/Creating-the-Admin-User.png)

## Hiding the User from Admin Views

To prevent detection, the malware uses multiple WordPress hooks to hide the malicious user. It filters out the malicious admin from user listings in the admin dashboard. Then it modifies the user role counts (e.g., number of admins) to make the hidden user less obvious.

![Hiding the User from Admin Views](https://blog.sucuri.net/wp-content/uploads/2025/07/Hiding-the-User-from-Admin-Views.png)

### Blocking Edits and Deletion

To maintain persistence, the malware prevents the malicious account from being deleted or edited and kills any attempt to delete the user from the admin panel.

![Blocking Edits and Deletion](https://blog.sucuri.net/wp-content/uploads/2025/07/Blocking-Edits-and-Deletion.png)

### Kill Switch Check via Cookie

To avoid being spotted in the plugins list, it hides itself so that even though the plugin is active, it doesn’t show up under the “Plugins” menu in wp-admin.

Lastly, the malware includes a conditional check that terminates page execution if a specific cookie is set. This likely serves as a kill switch or confirmation mechanism for the attacker.

![Kill Switch Check via Cookie](https://blog.sucuri.net/wp-content/uploads/2025/07/Kill-Switch-Check-via-Cookie.png)

## Impact of the Malware

This malware allows attackers to create a backdoor administrator user with full control over the site and hide that user from other administrators in the dashboard.

It persists across user deletions or password resets and not just this, it also avoids visibility in the plugins list.

If undetected, the attacker can return at any time to reinfect the site, install further payloads, or exfiltrate data.

## Remediation Steps

* Delete any unused plugins from your plugins directory.
* Review and remove any administrator user that you do not recognize.
* Change all passwords
* Use a [website firewall](https://sucuri.net/website-firewall/) like Sucuri to block future attacks and zero-days.
* Update WordPress and all plugins.

## Conclusion

This fake plugin is a powerful reminder of how malware authors can use subtle tactics to hide in plain sight. The attacker took care to blend into the WordPress ecosystem and used legitimate-looking metadata to avoid suspicion.

If your WordPress site has been acting strange, or you notice unknown users, it’s...