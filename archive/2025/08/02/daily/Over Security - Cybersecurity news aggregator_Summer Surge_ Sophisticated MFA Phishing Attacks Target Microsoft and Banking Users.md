---
title: Summer Surge: Sophisticated MFA Phishing Attacks Target Microsoft and Banking Users
url: https://pixmsecurity.com/blog/blog/summer-surge-sophisticated-mfa-phishing-attacks-target-microsoft-and-banking-users/
source: Over Security - Cybersecurity news aggregator
date: 2025-08-02
fetch_date: 2025-10-07T00:50:51.983678
---

# Summer Surge: Sophisticated MFA Phishing Attacks Target Microsoft and Banking Users

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

# Summer Surge: Sophisticated MFA Phishing Attacks Target Microsoft and Banking Users

![](https://pixmsecurity.com/wp-content/uploads/2025/08/mfa-blade-1000.png)

Phishing targeting users on work devices is not slowing down over the summer, with many employees taking their laptops home for the summer vacation months. The second half of July saw a pronounced surge in Microsoft and Outlook spearphish that demonstrated a number of interesting tactics, including multi-factor authentication phishing kits and distributed phishing content hosted across multiple trusted CDN servers. The same period also saw an increase in phishing pages targeting consumer banking services like Bank of America and American Express. MFA phishing included options to phish SMS codes as well as authentication app codes. Below are some examples and highlights.

cure[.]ru[.]com/Gr6t/

jzma[.]izpes[.]es

andrealong0510[.]blob[.]core[.]windows[.]net

amuricanxpress[.]com

login[.]officekeydesk[.]top

secure-en[.]com

my-php-app-production-cf6c[.]up[.]railway[.]app

chyisieaa[.]z20[.]web[.]core[.]windows[.]net

scalper[.]stackengine[.]sa[.]com

## **Microsoft and Outlook spearphish**

On July 16, a user at a Kentucky organization clicked the below Microsoft spearphish.

![](https://pixmsecurity.com/wp-content/uploads/2025/08/my-php-app-production-cf6c.up_.railway.app_.jpg)

The page was hosted on a reputable hosting service, leveraging its good DNS reputation. The page also included a multi-stage credential harvest, offering the victim multiple MFA options like SMS and authenticator code.

On July 18, a Texas user clicked the below Microsoft scareware phishing attack.

![](https://pixmsecurity.com/wp-content/uploads/2025/08/chyisieaa.z20.web_.core_.windows.net_.jpg)

This scam site fingerprints the target device, using their IP, geo-location and browser details, to customize the popup. It then “locks” the browser with coercive tricks, including auto-playing alarm sounds—so the user feels trapped. Finally, a counterfeit Windows-Defender dashboard runs a fake quick-scan and flashes red warnings, all designed to convince victims their PC is infected and prod them into calling the fake support number.

On July 18th, a user at a Kentucky organization clicked the below Microsoft spearphish.

![](https://pixmsecurity.com/wp-content/uploads/2025/08/login.officekeydesk.top_.jpg)

In order to evade detection, the page source is uploaded across several trusted CDN servers, like AWS, Akamai and Fastly, rather than being hosted on a single phishing server. Adding to its conviction, the page carefully mirrors Microsoft’s authentication flow.

![](https://pixmsecurity.com/wp-content/uploads/2025/08/multi-cdn.png)

On July 22, an employee at a Florida organization clicked the below MIcrosoft phishing attack.

![](https://pixmsecurity.com/wp-content/uploads/2025/08/scalper.stackengine.sa_.com_.jpg)

The URL loads behind a Cloudflare Captcha to avoid automated scanners. The phishing server blocks requests from non-browser user agents to further evade detection mechanisms.

On July 21, an employee at a Kentucky organization clicked the below Outlook phishing attack in a document share application.

![](https://pixmsecurity.com/wp-content/uploads/2025/08/cure.ru_.com_.jpg)

The phishing attack includes buttons for Outlook, Office 365, Yahoo, AOL, and “Other Mail. It further includes a one time password pop up to intercept a 6 digit code SMS or authenticator code in real time, enabling full session hijack. Later that day, another employee clicked on the below Microsoft phishing attack.

![](https://pixmsecurity.com/wp-content/uploads/2025/08/jzma.izpes_.es_.jpg)

The page included an encrypted payload to hide from static scanners and clip board hijacking to thwart incident response efforts.

On July 30, an employee at a Georgia organization clicked the below Microsoft phishing attack.

![](https://pixmsecurity.com/wp-content/uploads/2025/08/andrealong0510.blob_.core_.windows.net_.jpg)

The page also used tools to avoid automated analysis and block manual inspection.

## **Phishing Targeting Consumer Banking Services**

The same period saw a marked increase in phishing attacks targeting Bank of America and American Express customers on their work devices. Below are a couple of examples.

On July 17, an employee at a Kentucky organization clicked the below Bank of America phishing attack.

![](https://pixmsecurity.com/wp-content/uploads/2025/08/secure-en.com_.jpg)

This is a pixel perfect replica of the Bank of America login page. It included a secondary stage prompting the user for a 2FA code, SSN, or other security questions after credentials.

On July 23, a user at another Georgia organization clicked the below American Express phishing attack.

![](https://pixmsecurity.com/wp-content/uploads/2025/08/amuricanxpress.com_.jpg)

The user was prompted by an email or text message saying “​​Fraud alert on your Amex card – log in here to verify”. The URL also targets users via typo-squatting and includes user tracking parameters.

## **Mitigations**

* Block the specified domains on corporate firewalls and endpoint security solutions.
* Educate users about phishing risks even on pages that purport to use MFA
* Remind users of phishing risks for their personal accounts they access even if they are on corporate devices
* Enforce multi-factor authentication (MFA) on all corporate logins to reduce the risk of credential compromise.

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
* [January 2025](https:/...