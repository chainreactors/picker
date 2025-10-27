---
title: Another Fake Cloudflare Verification Targets WordPress Sites
url: https://blog.sucuri.net/2025/05/another-fake-cloudflare-verification-targets-wordpress-sites.html
source: Over Security - Cybersecurity news aggregator
date: 2025-05-22
fetch_date: 2025-10-06T22:30:15.369637
---

# Another Fake Cloudflare Verification Targets WordPress Sites

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

# Another Fake Cloudflare Verification Targets WordPress Sites

[![](https://secure.gravatar.com/avatar/da934b974fa8adb3975fd07757f8322b04202cc98f15a625259eb3b404c1532a?s=60&d=mm&r=g)](https://blog.sucuri.net/author/kayleigh)

[Kayleigh Martin](https://blog.sucuri.net/author/kayleigh)

* May 21, 2025

![Another Fake CloudFlare Infection Targets WordPress](https://blog.sucuri.net/wp-content/uploads/2025/05/Another-Fake-CloudFlare-Infection-Targets-WordPress-820x385.png)

A new Cloudflare infection has once again been targeting WordPress sites. This new iteration of malware mimics a legitimate-looking Cloudflare verification page, which then tricks victims into following various commands and downloading malware.

This style of malware is not new – our researcher [Ben Martin](https://blog.sucuri.net/author/benmartin) wrote about a [similar campaign](https://blog.sucuri.net/2025/03/fake-cloudflare-verification-results-in-lummastealer-trojan-infections.html) targeting WordPress sites back in March. The difference between this new infection and previous ones is the location of where the malware is located – spread out among multiple themes and fake plugins. Additionally, this variant is delivered in three stages, which helps the attacker avoid detection and maintain control over what is delivered at each step.

Below is the classic fake Cloudflare page:

![fake cloudflare verification](https://blog.sucuri.net/wp-content/uploads/2025/05/fake-cloudflare-verification-e1747863003142.png)

Let’s dive into where this malware is located and what it does.

## High level analysis of the fake Cloudflare infection

First, let’s review the basics of this malware and its behavior.

The infection starts off by mimicking a legitimate Cloudflare verification page, which asks users to perform the following actions:

* Asks the user to verify they are human with a **checkbox**.
* Directs the user to **Press Win + R to open Run**.
* Asks the user to Copy and paste a malicious command.

If the victim follows the instructions, they will ultimately download a malicious Windows executable file that then infects their machine.

This style of infection is especially dangerous due to the following features:

1. The style of the fake Cloudflare page looks nearly identical to a real Cloudflare prompt.
2. The payload is delivered via an obfuscated Powershell command, which can evade basic antivirus tools.
3. The prompt appears harmless, which increases the likelihood that users with limited technical knowledge will follow the malware’s instructions.
4. Many desktops run Windows, which could target a large audience.

Now that we know the basic behavior of the infection, let’s review the details.

## Location and detailed analysis of the fake Cloudflare infection

We’ll begin by examining the location of the malware. This infection is embedded across all installed themes, with the malicious code injected into the **header.php** file. This file then references a separate file named **verification.html**. Because all themes are affected, removal can be challenging, and the infection may easily evade detection.

The **header.php** file contains a script calling to the verification.html file, while **verification.html** contains the full HTML and styling used to mimic a legitimate Cloudflare verification screen. Below is the **header.php** file:

![header.php contents](https://blog.sucuri.net/wp-content/uploads/2025/05/header-php-contents.png)  *(**header.php** file within the theme)*

The **verification.html** file contains many elements. Let’s break it down chunk by chunk.

### Code Analysis Part 1:

Below is the first piece of code we will review:

![verification.html contents](https://blog.sucuri.net/wp-content/uploads/2025/05/verification-html-contents.png)  *(**verification.html** file within the theme part 1)*

There are three main elements to focus on in the first chunk of this file:

* **Fake Cloudflare warning with a human verification prompt:** The page begins by displaying a “*Verify you are human*” message inside of a *<div>* tag. This message is then followed by a Cloudflare logo with other Cloudflare-like elements making this malware appear legitimate to the end user.
* **Masquerading security explanation and instructions:** The fake page then presents an explanation stating that unusual web traffic has been detected from the user’s IP address. *Unusual Web Traffic Detected* is highlighted in red to emphasize the urgency, prompting the user to act qui...