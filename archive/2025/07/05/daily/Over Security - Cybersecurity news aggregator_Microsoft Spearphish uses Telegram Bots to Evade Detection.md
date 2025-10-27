---
title: Microsoft Spearphish uses Telegram Bots to Evade Detection
url: https://pixmsecurity.com/blog/blog/microsoft-spearphish-use-telegram-bots-to-evade-detection/
source: Over Security - Cybersecurity news aggregator
date: 2025-07-05
fetch_date: 2025-10-06T23:26:22.832637
---

# Microsoft Spearphish uses Telegram Bots to Evade Detection

[![Pixm Security Logo](https://pixmsecurity.com/wp-content/themes/Divi-Child/images/pixm-logo-header-white.png)](https://pixmsecurity.com)

* [About](https://pixmsecurity.com/about/)
* [About Us](https://pixmsecurity.com/about-us/)
* [Partners](https://pixmsecurity.com/partners/)
* Resources
  + [Blog](https://pixmsecurity.com/blog/)
  + [News](/news)
* [Login](https://app.pixm.net)
* [Book a Demo](https://pixmsecurity.com/request-demo/)
* [Free Install](https://chrome.google.com/webstore/detail/pixm-phishing-protection/flomofhkchlalfciiibgbfcpolhmglai?hl=en)
* [Free Install](https://apps.apple.com/app/pixm-phishing-protection/id1622871362)
* [Free Install](https://addons.mozilla.org/en-US/firefox/addon/pixm-web/)

Have a question for us?

Contact support at support@pixm.net

[Book a Demo](/request-free-trial/)

Open Menu

## Request Your Demo

"\*" indicates required fields

### Contact Information

First Name\*

Last Name\*

Company\*

Email\*

Work Phone

CAPTCHA

Request Demo

# Microsoft Spearphish uses Telegram Bots to Evade Detection

![](https://pixmsecurity.com/wp-content/uploads/2025/07/telegram.png)

The last week of June and early July saw a surge in zero-day phishing attacks targeting both corporate Microsoft/Outlook logins and personal web services (e-commerce, streaming, and email) on work devices.  Threat actors employed sophisticated tactics – from obfuscated JavaScript and fake OAuth login flows to Telegram-based exfiltration – allowing many of these phishing pages to evade traditional detection measures. Here are some examples and highlights.

### Phishing URLs

boa[.]devicehub[.]co/login

s3[.]lax[.]sharktech[.]net

ru0[.]eotskyj[.]es

zolotayanora[.]com

nextflyerpub[.]store

cpcontacts[.]164-92-78-92[.]cprapid[.]com

fhi9o09i5[.]uywpk[.]es

j43okxouoz0[.]franksdarmatology[.]com

webmail[.]50-6-111-88[.]cprapid[.]com

###

## Microsoft Spearphish and Telegram Bot Exfiltration

This period witnessed a number of interesting attacker techniques like the use of Telegram Bot APIs and clever techniques to conceal page content.

On July 2, a staff member at a Texas organization clicked a Microsoft Outlook spear-phish delivered via a file share link.

![](https://pixmsecurity.com/wp-content/uploads/2025/07/s3.lax_.sharktech.net_.jpg)

The stolen credentials were not sent to a typical web server; instead, the page used the Telegram Bot API to exfiltrate captured passwords and user data in real time. This tactic provides the attacker with an anonymous, easy channel for data theft while helping the phish bypass traditional defenses. Another Texas employee the same day fell for a similar Microsoft 365 phish**.**

![](https://pixmsecurity.com/wp-content/uploads/2025/07/ru0.eotskyj.es_.jpg)

This page hid a massive block of obfuscated JavaScript in its code – likely to conceal malicious tracking or keystroke logging scripts, making static analysis difficult.

On June 24, a Kentucky employee clicked the below link to an Office 365 sign-in page.

![](https://pixmsecurity.com/wp-content/uploads/2025/07/zolotayanora.com_.jpg)

The phishing page’s HTML was entirely encoded into a single string passed to a document.write(unescape(…)) function. This meant the page’s content was only rendered at runtime, helping it evade detection from security scanners that rely on static HTML analysis.

In early July, another Kentucky user was lured to a fraudulent Outlook Web Access page that employed multiple evasive techniques.

![](https://pixmsecurity.com/wp-content/uploads/2025/07/fhi9o09i5.uywpk_.es_.jpg)

The HTML payload was encrypted and only decrypted in-browser to reveal the fake login form. It also contained scripts to hijack the user’s clipboard and prevent copying of content. It further set special meta tags to prevent caching or sandboxing by web crawlers.

On June 23, an employee at a Washington organization clicked the below spear-phishing page, which loaded several resources from legitimate Microsoft content delivery networks (such as aadcdn.msauth.net and aadcdn.msftauth.net) and even referenced Microsoft’s own “Watson” telemetry service in its code.

![](https://pixmsecurity.com/wp-content/uploads/2025/07/j43okxouoz0.franksdarmatology.com_.jpg)

## E-commerce and Streaming Phishing on Personal Devices

This mid summer period saw a surge in spearphishing targeting corporate users on their personal accounts, particularly Amazon account phishing.

On June 30, a Texas employee clicked a fake Amazon login page on their work device, including fake “Sign in with Google” and “Sign in with Facebook” authentication flows, designed to steal multiple types of identity credentials.

![](https://pixmsecurity.com/wp-content/uploads/2025/07/boa.devicehub.co_.jpg)

Another Amazon credential harvester was clicked on June 29 targeting a Kentucky user, employing a carbon copy of Amazon’s multi-stage login flow.

![](https://pixmsecurity.com/wp-content/uploads/2025/07/webmail.50-6-111-88.cprapid.com_.jpg)

Behind the scenes, a suspicious JavaScript function was executing silently every few milliseconds, sending stolen data back to a remote command-and-control server. This aggressive data-capture mechanism allowed the attacker to siphon additional information (potentially session data or two-factor tokens) beyond just the username and password.

The period also included Netflix and AOL spearphish targeting corporate users in Kentucky, with tactics including aggressive device fingerprinting and fake Google Captchas.

![](https://pixmsecurity.com/wp-content/uploads/2025/07/cpcontacts.164-92-78-92.cprapid.com_.jpg)

![](https://pixmsecurity.com/wp-content/uploads/2025/07/nextflyerpub.store_.jpg)

**Mitigations**

* Block the specified domains on corporate firewalls and endpoint security solutions.
* Remind users of phishing risks for their personal accounts they access even if they are on corporate devices
* Enforce multi-factor authentication (MFA) on all corporate logins to reduce the risk of credential compromise.
* Protect your users from the next wave of zero day phishing attacks and [schedule a demo](https://pixmsecurity.com/request-demo/).

threatresearch@pixmsecurity.com

Search for:

#### Recent Posts

* [AiTM Evolution and Cloud Abuse: September’s Backblaze-Driven Phishing Wave](https://pixmsecurity.com/blog/blog/aitm-evolution-and-cloud-abuse-septembers-backblaze-driven-phishing-wave/)
* [September Phishing Fires: Backblaze Ablaze with OneDrive Credential Attacks](https://pixmsecurity.com/blog/blog/september-phishing-fires-backblaze-ablaze-with-onedrive-credential-attacks/)
* [August Phish Flood Warning: Credential Attacks Raining Down from Cloudflare](https://pixmsecurity.com/blog/blog/summer-phishing-floodwarning-credential-attacks-raining-down-from-cloudflare/)
* [Inside August’s Phishing Heat Wave: Support Scams, Paperless Post Lures, and MFA Abuse](https://pixmsecurity.com/blog/blog/inside-augusts-phishing-heat-wave-support-scams-paperless-post-lures-and-mfa-abuse/)
* [Summer Surge: Sophisticated MFA Phishing Attacks Target Microsoft and Banking Users](https://pixmsecurity.com/blog/blog/summer-surge-sophisticated-mfa-phishing-attacks-target-microsoft-and-banking-users/)

#### Recent Comments

#### Archives

* [September 2025](https://pixmsecurity.com/blog/2025/09/)
* [August 2025](https://pixmsecurity.com/blog/2025/08/)
* [July 2025](https://pixmsecurity.com/blog/2025/07/)
* [June 2025](https://pixmsecurity.com/blog/2025/06/)
* [May 2025](https://pixmsecurity.com/blog/2025/05/)
* [April 2025](https://pixmsecurity.com/blog/2025/04/)
* [March 2025](https://pixmsecurity.com/blog/2025/03/)
* [February 2025](https://pixmsecurity.com/blog/2025/02/)
* [January 2025](https://pixmsecurity.com/blog/2025/01/)
* [December 2024](https://pixmsecurity.com/blog/2024/12/)
* [March 2024](https://pixmsecurity.com/blog/2024/03/)
* [March 2023](https://pixmsecurity.com/blog/2023/03/)
* [November 2022](https://pixmsecurity.com/blog/2022/11/)
* [August 2022](https://pixmsecu...