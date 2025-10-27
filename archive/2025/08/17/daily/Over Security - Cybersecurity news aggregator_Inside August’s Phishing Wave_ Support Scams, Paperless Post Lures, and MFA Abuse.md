---
title: Inside August’s Phishing Wave: Support Scams, Paperless Post Lures, and MFA Abuse
url: https://pixmsecurity.com/blog/blog/inside-augusts-phishing-wave-support-scams-paperless-post-lures-and-mfa-abuse/
source: Over Security - Cybersecurity news aggregator
date: 2025-08-17
fetch_date: 2025-10-07T00:47:45.244575
---

# Inside August’s Phishing Wave: Support Scams, Paperless Post Lures, and MFA Abuse

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

# Inside August’s Phishing Heat Wave: Support Scams, Paperless Post Lures, and MFA Abuse

![](https://pixmsecurity.com/wp-content/uploads/2025/08/paperless-post-3.png)

The first half of August has seen a major surge in Microsoft support scams using keyboard locks and other tactics to prod users to calling targeted call centers. Other Microsoft phishing attacks during this period made use of aggressive device fingerprinting, MFA relay tactics, and deliveries through event invites and PDFs. We also observed similar tactics in phishing targeting customers of financial services like Chase and US Bank. Here are some examples and highlights.

vdus28firf[.]z13[.]web[.]core[.]windows[.]net/win[.]html

enumeducomebachtorenewjouly[.]one

cb2732788f444a6eacc7e2c468dd4577[.]gloweverse[.]com

alternative-creations[.]com

dd53985e595c41068224351932364cd6[.]shedthelightnepal[.]org

adsfd2gyj[.]z19[.]web[.]core[.]windows[.]net

login[.]welvz[.]com

peachpuff-turtle-958085[.]hostingersite[.]com

signlepolnt[.]uspank[.]today

onedrive-microsoft[.]scene[.]com[.]de

securecenter09[.]com/x0/pc

## Microsoft Support Scams and Paperless Post Delivery

This period saw an uptick in support scams that target years with their IP, geolocation, and device details while locking their keyboard to get them to call a scam support number.

On August 1, a mental health professional at a Kentucky organization clicked the below phishing page.

![](https://pixmsecurity.com/wp-content/uploads/2025/08/vdus28firf.z13.web_.core_.windows.net_win.html.jpg)

This phishing page customizes itself based on the target’s IP address and uses URL parameters to swap the phone number to route different recipients to different call centers. The page locks the device keyboard, making many users feel that calling the support number is the only way to escape.

Similar attacks hit employees in many states like Illinois, Texas, and Georgia, like the below example that was clicked by an administrator on August 12th.

![](https://pixmsecurity.com/wp-content/uploads/2025/08/adsfd2gyj.z19.web_.core_.windows.net_.jpg)

Hackers are after more than credentials. The attack socially engineers the user to call the support number, where they will be tricked into installing fake remote desktop software, which can allow the bad actors to steal more sensitive data and install malware (eg. keyloggers, ransomware).

The period also had a number of Microsoft attacks delivered through unconventional channels like invitation platforms and document shares. The below Outlook phishing page, for example, was clicked through a Paperless Post invitation by a mental health practitioner at a Kentucky organization on August 11th.

![](https://pixmsecurity.com/wp-content/uploads/2025/08/paperless.jpg)![](https://pixmsecurity.com/wp-content/uploads/2025/08/enumeducomebachtorenewjouly.one_.jpg)

This phishing attack was not only delivered through an invitation platform, it included a Cloudflare CAPTHA, a fake MFA prompt, as well as options to steal credentials for multiple accounts like Outlook, Office 365, Yahoo, AOL, etc.

On August 14th, the below OneDrive phishing page was clicked by a Kentucky user via a PDF file share.

![](https://pixmsecurity.com/wp-content/uploads/2025/08/onedrive-microsoft.scene_.com_.de_.jpg)

In addition to stealing passwords, the site can possibly gain long-term access to victims’ email accounts through fake app permissions.

We also observed a Microsoft phishing attack hosted on a compromised non-profit website. On August 8th, an employee at a Kentucky organization clicked the below Microsoft phishing page that was hosted on a website for an Australian and Nepalese charity.

![](https://pixmsecurity.com/wp-content/uploads/2025/08/shedthelightnepal.org_.jpg)

![](https://pixmsecurity.com/wp-content/uploads/2025/08/dd53985e595c41068224351932364cd6.shedthelightnepal.org_.jpg)

The threat actor hosted dozens of similar pages consisting of 32-hex subdomains under ‘shedthelightnepal.org’ to act as fake Microsoft endpoints/CDNs. The phishing kit harvests MFA and OTP codes as well as password credentials.

Other Microsoft phishing showcased device fingerprinting and evasive techniques to various kinds of security scanners.

On August 14th, another Kentucky staff member clicked the below Microsoft phishing attack.

![](https://pixmsecurity.com/wp-content/uploads/2025/08/cb2732788f444a6eacc7e2c468dd4577.gloweverse.com_.jpg)

The attack uses aggressive device fingerprinting and includes extra fake MFA steps to phish one time codes and “pass keys”.

On August 14th, two staff members at a Washington organization clicked the below Microsoft phishing page.

![](https://pixmsecurity.com/wp-content/uploads/2025/08/alternative-creations.com_.jpg)

The HTML body is stuffed with unrelated, human-sounding event blurbs and random token strings, while the page title claims “Sign in to your account”—a classic mismatch used to fool scanners and reputation systems that only skim text.

## Financial Services Customers Targeted on Personal Devices

Early August also saw customers of popular banking services like Chase and US Bank targeted on their work issued laptops. Hackers employed similar tactics of device fingerprinting, MFA prompts and fake Captcha’s to avoid detection.

On August 14th, a staff member at a Minnesota organization clicked the below US Bank phishing page.

![](https://pixmsecurity.com/wp-content/uploads/2025/08/signlepolnt.uspank.today_.jpg)

Each visitor of this phishing page is tagged with a unique token so the criminals can track which lure worked, and the page uses fake errors and a “loading” overlay to coax you into trying your login again. When the target hits submit, the page quietly fingerprints the device (OS, browser, screen size, languages, even graphics card info) and tries to read site cookies—data that can help them evade defenses or impersonate the victim elsewhere.

On August 14th, an employee at a Kentucky organization clicked the below Chase Bank phishing attack on their work device.

![](https://pixmsecurity.com/wp-content/uploads/2025/08/securecenter09.com_x0_pc.jpg)

This phishing page had also had a two factor prompt to steal MFA codes. It included a CloudFlare captcha challenge to evade detection from various scanners.

**Mitigations**

* Block the specified domains on corporate firewalls and endpoint security solutions.
* Educate users about phishing risks even on pages that purport to use MFA
* Remind users of phishing risks for their personal accounts they access even if they are on corporate devices
* Enforce multi-factor authentication (MFA) on all corporate logins to reduce the risk of credential compromise.

threatresearch@pixmsecurity.com

Search for:

#### Recent Posts

* [AiTM Evolution and Cloud Abuse: September’s Backblaze-Driven Phishing Wave](https://pixmsecurity.com/blog/blog/aitm-evolution-and-cloud-abuse-septembers-backblaze-driven-phishing-wave/)
* [September Phishing Fires: Backblaze Ablaze with ...