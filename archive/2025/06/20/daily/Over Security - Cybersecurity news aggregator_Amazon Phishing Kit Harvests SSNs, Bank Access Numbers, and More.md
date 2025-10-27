---
title: Amazon Phishing Kit Harvests SSNs, Bank Access Numbers, and More
url: https://pixmsecurity.com/blog/blog/amazon-phishing-kit-harvests-ssns-bank-access-numbers-and-more/
source: Over Security - Cybersecurity news aggregator
date: 2025-06-20
fetch_date: 2025-10-06T22:54:50.389043
---

# Amazon Phishing Kit Harvests SSNs, Bank Access Numbers, and More

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

# Amazon Phishing Kit Harvests SSNs, Bank Access Numbers, and More

![](https://pixmsecurity.com/wp-content/uploads/2025/06/amazon-wide.png)

Early-mid June saw a surge of phishing campaigns targeting Amazon, Microsoft and Netflix accounts, including phishing kits capable of harvesting extensive personal data, like social security numbers and bank access numbers. Many Microsoft-themed attacks employed advanced evasive tactics – such as heavily obfuscated scripts, anti-scanning measures, and simulated multi-factor authentication steps. Meanwhile, an Amazon phishing kit was found capable of harvesting extensive personal data beyond passwords, and Netflix phishing links included unique identifiers likely used to track campaign targets. Here are some examples and highlights

### Phishing URLs

loginmicrosoftcommon365authmked1c[.]bdfkfwwgyqon[.]es

xiotecltd[.]com/support/10be73e78

prime-siginauth[.]authecsbeaneyr[.]website

managesecure[.]log-in[.]information-reactivate-statement[.]memberprime[.]vlx[.]yeo[.]mybluehost[.]me

rmuba[.]ewetanign[.]ru

office[.]trustmark[.]cloud

gfmw[.]guestaccessportal[.]com

oneonline[.]chirping[.]it[.]com

###

### Amazon Phishing: SSN, Bank Access Numbers and More

On June 12th, a staff member at a Maryland organization clicked the below Amazon phishing attack on their work device.

![](https://pixmsecurity.com/wp-content/uploads/2025/06/prime-siginauth.authecsbeaneyr.website.jpg)

The page contained a data filtration configurations embedded deeply in it’s json:

![](https://pixmsecurity.com/wp-content/uploads/2025/06/config.png)

This indicates a configurable phishing kit capable of requesting sensitive identity and financial data, including:

* Social Security Number (SSN)
* National IDs
* Bank Account Numbers
* Online banking access numbers
* Passport & civil IDs
* Mother’s maiden name (MMN)

On June 12 a similar Amazon phishing attack was clicked by an employee at a Virginia organization, also targeting their personal account on their work device.

![](https://pixmsecurity.com/wp-content/uploads/2025/06/managesecure.log-in.jpg)

The login UI included an email validation that exactly mimics Amazon’s two step sign-in process. The mybluehost[.]me domain was also used in earlier Amazon phishing attacks reported on earlier.

### Microsoft O365 / Sharepoint Phishing: fake MFA, Voicemail Lures, and Evasive Javascript

On June 9, a user at a Kentucky organization clicked this Office 365 spearphish hosted on a Russian top level domain.

![](https://pixmsecurity.com/wp-content/uploads/2025/06/rmuba.ewetanign.ru_.jpg)

The HTML included tags that prevent web crawlers from caching or indexing the page and clip board interference that prevents analysts from copying content. It also included a ~1 million character javascript blob likely intended to thwart static analysis. On June 10, a another Kentucky staff member clicked this Microsoft phishing link via a voicemail lure.

![](https://pixmsecurity.com/wp-content/uploads/2025/06/oneonline.chirping.it_.com_.jpg)

The attack presented the user with multiple sign-in prompts and ultimately a message stating that a voice mail had “expired” and the user would be redirected to Microsoft. Voicemail lures like this are commonly used in business email compromise (BEC) campaigns to trick users into clicking malicious links.

On June 11, a Texas administrator clicked this spearphishing link. The page used advanced evasive scripting with encrypted payloads, anti-analysis techniques, and an obfuscated user interface.

![](https://pixmsecurity.com/wp-content/uploads/2025/06/loginmicrosoftcommon365authmked1c.bdfkfwwgyqon.es_.jpg)

The same day, an employee at an Iowa organization clicked this Microsoft 365 phishing link.

![](https://pixmsecurity.com/wp-content/uploads/2025/06/office.trustmark.cloud_.jpg)

The URL structure perfectly mimicked Microsoft’s OAuth flow. The phishing page also employed session tracking and device fingerprinting perhaps to track the effectiveness of the phishing campaign and gather intel on the user.

On June 17, a staff member at a Minnesota organization clicked this SharePoint-themed phishing attack, which simulated multiple MFA flows like push approvals, SMS verification, and authenticator app prompts.

![](https://pixmsecurity.com/wp-content/uploads/2025/06/gfmw.guestaccessportal.com_.jpg)

### Netlifx Phishing Campaigns and User Tracking

The same period also saw an uptick in Netflix phishing campaigns tracking click through rates and device information. For instance, on June 15th a staff member at a Texas organization clicked the below Netflix phishing link on their work device.

![](https://pixmsecurity.com/wp-content/uploads/2025/06/xiotecltd.com_.jpg)

The page included watermarking and campaign identifiers used to track individual campaign deployments or victim origin.

**Mitigations**

* Block the specified domains on corporate firewalls and endpoint security solutions.
* Educate users about phishing risks even on pages that purport to use MFA
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
* [December 2024](...