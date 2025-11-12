---
title: 70 Clicks in 24 Hours: OneDrive Phish Explodes via Backblaze
url: https://pixmsecurity.com/blog/blog/70-clicks-in-24-hours-onedrive-phish-explodes-via-backblaze/
source: Over Security - Cybersecurity news aggregator
date: 2025-11-11
fetch_date: 2025-11-12T03:12:35.043209
---

# 70 Clicks in 24 Hours: OneDrive Phish Explodes via Backblaze

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

# 70 Clicks in 24 Hours: OneDrive Phish Explodes via Backblaze

![](https://pixmsecurity.com/wp-content/uploads/2025/11/header.png)

Mid October saw astonishingly widespread phishing campaigns, with a single OneDrive phishing link clicked by over 70 users within 24 hours. Similar to attacks reported in September and early October, these were hosted on Backblaze infrastructure and exfiltrated detailed information about their victims. The same period saw surges in Attack-in-the-Middle (AiTM) phishing, also hosted on legitimate infrastructure, as well as campaigns targeting e-commerce accounts on corporate devices. Here are some examples and highlights.

25b7fe36940249929256d55ca102d65e[.]0–1[.]biz

news-3[.]kryvoex[.]onl

greetingstes[.]de

partieinvia[.]de

1fbe59bdce8f457c90899860ac783d96[.]pennyhewitt[.]com

track[.]draipuhu[.]digital

divarshahr[.]com

home[.]eaprogram[.]org

f005[.]backblazeb2[.]com/file/seeeendeeed/onedr-updated.html

Starting on October 24, an astonishing 70+ users at several Kentucky organizations clicked the below OneDrive phishing attack hosted on Backblaze.

![](https://pixmsecurity.com/wp-content/uploads/2025/11/f005.backblazeb2.com_file_seeeendeeed_onedr-updated.jpg)

This widespread attack is hosted on legitimate infrastructure, backblazeb2[.]com, including images loaded from storage.googleapis.com. Prior to exfiltrating credentials, the page fetches the client’s IP address and geo-location in order to enrich the data. A huge number of functions are obfuscated with hex-based strings to conceal code and exfiltration logic from analysis.

Earlier attacks in October also leveraged legitimate infrastructure and were loaded with AiTM MFA bypass tools. On October 9, a staff member at an Illinois organization clicked the below Microsoft spear phish.

![](https://pixmsecurity.com/wp-content/uploads/2025/11/25b7fe36940249929256d55ca102d65e.0-1.biz_.jpg)

The phishing page used an AiTM multi-factor phishing kit and was hosted on Digital Ocean infrastructure. The attack operates across multiple subdomains of 0–1[.]biz, with the primary credential harvesting endpoint at 25b7fe36940249929256d55ca102d65e.0–1[.]biz. Other subdomains were used to carry out various authentication flows like OAuth and IWA SSO, illustrated in the below snippet:

25b7fe36940249929256d55ca102d65e.0–1.biz (landing, post endpoints, telemetry)

6e90e4c858414793ad5226e441ef2930.0–1.biz (oauth20\_authorize.srf, logout, “Sign up”)

28737ebf8d514ca1b678e68a3840e034.0–1.biz (cancel/error redirects)

269e22132a7a4d028877112376a18c9d.0–1.biz (fake “cdn” roots/bundles)

41b87ad5971b41568c131bfb41e5351e.0–1.biz (alt cdn root)

a3394990777d457c9ee63d205a93d329.0–1.biz (“fwlink” look-alike)

6108344e268a45738693586825f32444.0–1.biz (IWA SSO / edge redirect)

a6f89d750ab44ab1a73ede1e41b6f385.0–1.biz, aeb3fda06c01495e9f9f37c133642110.0–1.biz (reset flows)

On October 10, an employee at a Kentucky organization clicked the below Microsoft phishing attack.

![](https://pixmsecurity.com/wp-content/uploads/2025/11/news-3.kryvoex.onl_.jpg)

The page prompts the user for MFA codes and uses multiple detection evasion techniques, like splitting up suspicious words with HTML elements, like below.

“p<span>ass</span>w<span>or</span>d”, “Micr<span>osoft</span> Authenticator”, etc

On October 14, three Texas employees clicked on the below Hotmail phishing attack.

![](https://pixmsecurity.com/wp-content/uploads/2025/11/greetingstes.de_.jpg)

This page was delivered via a likely “you’re invited” Greenvelope lure page and is complete with multi-brand credential harvesting (Outlook/Gmail/Yahoo/AOL/etc.) and MFA bypass. It uses an OTP prompt combined with a timer to create more urgency, eg. “Time left: 4:53”, “You will receive an OTP within 1–5 minutes”, etc.

On October 15, a similar Paperless post phishing attack was clicked by a Minnesota employee.

![](https://pixmsecurity.com/wp-content/uploads/2025/11/partieinvia.de_.jpg)

This “View Invitation” lure uses a Paperless Post message combined with a “select email provider” to hook its victim, complete with Outlook/Office 365/Gmail/Yahoo/AOL/“Other brand options and MFA bypass.

On October 15, another Texas employee clicked on the below Microsoft phishing attack.

## ![](https://pixmsecurity.com/wp-content/uploads/2025/11/1fbe59bdce8f457c90899860ac783d96.pennyhewitt.com_.jpg)

This page also uses an OTP flow with a countdown to create urgency. Like others seen during this period, it involves dozens of subdomains of \*[.]pennyhewitt[.]com to deploy various authentication functions like OAuth, fake password reset handling, fake FIDO/passkey handlers, and fake signup endpoints among others.

On October 16, a staff member at a Kentucky organization clicked the below Microsoft phishing page.

![](https://pixmsecurity.com/wp-content/uploads/2025/11/track.draipuhu.digital.jpg)

The page included heavy client side obfuscation, with almost a megabyte of characters packed into a single variable const tw = “Ld03VJ…” and clipboard tampering to evade analysis.

On October 16th, a Kentucky employee clicked on the below Microsoft phishing attack.

![](https://pixmsecurity.com/wp-content/uploads/2025/11/divarshahr.com_.jpg)

In addition to MFA code harvesting, the URL parameters include targeted information about the recipient’s IP address and strongly suggest the use of QR codes via a “quishing” campaign “t=qr”.

The same period also saw phishing campaigns targeting e-commerce accounts on corporate employees’ work devices. On October 19, another Kentucky employee clicked on the below Amazon phishing attack.

![](https://pixmsecurity.com/wp-content/uploads/2025/11/home.eaprogram.org_.jpg)

The page includes MFA code capture and user tracking parameters in the URL, suggesting the use of targeted campaigns.

##

## **Mitigations**

* Block the specified domains on corporate firewalls and endpoint security solutions.
* Educate users about phishing risks even on pages that purport to use MFA
* Remind users of phishing risks for their personal accounts they access even if they are on corporate devices
* Enforce multi-factor authentication (MFA) on all corporate logins to reduce the risk of credential compromise.

If you are interested in seeing how PIXM can help prevent attacks like these for your organization, [book a demo here](https://pixmsecurity.com/request-demo/).

threatresearch@pixmsecurity.com

Search for:

#### Recent Posts

* [70 Clicks in 24 Hours: OneDrive Phish Explodes via Backblaze](https://pixmsecurity.com/blog/blog/70-clicks-in-24-hours-onedrive-phish-explodes-via-backblaze/)
* [Invoice Phish Tsunami: MFA-Bypassing Phish Sweep U.S. via OneDrive & Backblaze](https://pixmsecurity.com/blog/blog/invoice-phish-tsunami-mfa-bypassing-phish-sweep-us-via-onedrive-backblaze/)
* [AiTM Evolution and Cloud Abuse: September’s Backblaze-Driven Phishing Wave](https://pixmsecurity.com/blog/blog/aitm-evolution-and-cloud-abuse-septembers-backblaze-driven-phishing-wave/)
* [September ...