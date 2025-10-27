---
title: Instagram Lures, Microsoft Spoofs, and SIM Swaps: A Mid-May Phishing Breakdown
url: https://pixmsecurity.com/blog/blog/instagram-lures-microsoft-spoofs-and-sim-swaps-a-mid-may-phishing-breakdown/
source: Over Security - Cybersecurity news aggregator
date: 2025-05-30
fetch_date: 2025-10-06T22:28:01.921890
---

# Instagram Lures, Microsoft Spoofs, and SIM Swaps: A Mid-May Phishing Breakdown

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

# Instagram Lures, Microsoft Spoofs, and SIM Swaps: A Mid-May Phishing Breakdown

![](https://pixmsecurity.com/wp-content/uploads/2025/05/may-22-image.png)

A surge of sophisticated **zero-day phishing campaigns** was observed in mid-May 2025, targeting a wide range of services including social media, e-commerce, enterprise email, telecommunications, and streaming platforms. Attackers leveraged **legitimate cloud services and compromised infrastructure** – from professional learning platforms to web hosting and cloud app environments – to lend credibility to their phishing pages. Here are some examples and highlights.

### Phishing URLs

manage[.]nay[.]qxk[.]mybluehost[.]me

googleiinfluencerhub[.]ct[.]ws

czoin[.]dzdyf[.]es

newspaceitenow[.]tech/Gran1/

sign[.]account[.]srver[.]at[.]bel[.]0auth[.]165-154-199-230[.]cprapid[.]com

my-php-app-production-7f57[.]up[.]railway[.]app

log-in[.]billing-information[.]netflix-id[.]cc[.]valterjavaroni[.]com[.]br

greatbtinternet[.]in/vparty/

###

### Instagram Influencer

This Instagram phishing attack was clicked by a Texas user on May 11 on their work device, where threat actors created a fake **“Google Influencer Hub”** webpage to target Instagram users’ login credentials.

![](https://pixmsecurity.com/wp-content/uploads/2025/05/googleiinfluencerhub.ct_.ws-url-300x300.png)

The lure likely promised users an opportunity to join a **Google-sponsored influencer program**, tricking them into entering their Instagram credentials. Once entered, the credentials would be captured via the site’s script (which submitted the username and password to the attacker’s server). Such messages are often delivered within the native Instagram app, completely outside the scope of corporate email security.

The attack also includes a 2FA prompt stage, asking the user for a 6 digit code after entering their password.

### Office 365 and Okta Spearphish

On May 21, a Kentucky employee clicked the below Microsoft spearphish.

![](https://pixmsecurity.com/wp-content/uploads/2025/05/czoin.dzdyf_.es-url-300x300.png)

This attack targeted Microsoft Office 365 credentials, using a phishing page hosted on czoin[.]dzdyf[.]es (a Spanish domain). Additionally, the HTML suggests that the phishing kit appears to integrate elements of **Okta**, as seen by references to Okta in the HTML code.

### “Adobe Document Cloud” Spearphish

On May 13th, a staff member at an Idaho organization clicked the below phishing attack on an “Adobe Document Cloud” lure.

![](https://pixmsecurity.com/wp-content/uploads/2025/05/newspaceitenow.tech-url-300x300.png)

The original phishing page presented an Adobe Document Viewer, which prompted the user to select their email type (Outlook in this case). The attack contains the assurance “We’ll never share your email with anyone else”.

The phishing kit behind this page actually catered to multiple email providers: besides Outlook, the kit also offered options to sign in with Yahoo, AOL, Office 365, or “Other Mail”.

A similar phishing kit to the one on newspaceitenow.tech was observed on greatbtinternet[.]in/vparty/ a week later (May 21) targeting a user in Kentucky

### AT&T Wireless Login Phish on cPanel Site

On May 13th, an Idaho employee clicked the below AT&T phishing attack on their work device.

![](https://pixmsecurity.com/wp-content/uploads/2025/05/sign.account.srver_.at_.bel_.0auth.165-154-199-230.cprapid.com-url-300x300.png)

Attacks targeting AT&T customers like this are often delivered through SMS, mimicking AT&T’s regular communications for services and marketing. Compromised AT&T accounts give hackers access to critical device and billing information, allowing them the ability to manage SIM cards and eSIMs and execute SIM swaps.

### Microsoft Spearphish on Railway Cloud App

On May 15th, a user at a Minnesota organization clicked the below Microsoft spearphish.

![](https://pixmsecurity.com/wp-content/uploads/2025/05/my-php-app-production-7f57.up_.railway.app-url-300x300.png)

This attack was hosted on the Railway.app cloud platform, which provides free hosting for web applications. By deploying on Railway.app, the attacker took advantage of a legitimate cloud domain (up.railway.app). The text on this phishing page reads: “Because you’re accessing sensitive info, you need to verify your password,” which matches Microsoft wording in real scenarios (like re-confirming credentials for sensitive account changes).

### Netflix Billing Phish via Compromised Brazilian Site

On May 21, an employee at a Colorado organization clicked the below Netflix billing phish.

![](https://pixmsecurity.com/wp-content/uploads/2025/05/log-in.billing-information.netflix-id.cc.valterjavaroni.com_.br-url-300x300.png)

The attack is hosted on a legitimate domain of a legitimate Brazilian business, that was near certain compromised and unwittingly hosting this phishing attack. Leveraging the reputation of a reputable third party domain, this attack can easily fly under the radar

### Amazon Phish on Spoofed Hosting

On May 18th, another Texas staff member clicked the below Amazon phishing attack on their work device.

![](https://pixmsecurity.com/wp-content/uploads/2025/05/manage.nay_.qxk_.mybluehost.me-url-300x300.png)

The domain mybluehost[.]me likely impersonated the legitimate hosting domain [bluehost.com](http://bluehost.com). Examples like this speak to the risks of users accessing personal email accounts on work devices.

**Mitigations**

* Block the specified domains on corporate firewalls and endpoint security solutions.
* Educate users about phishing risks in file sharing applications outside email like Adobe
* Remind users of phishing risks for their personal accounts they access even if they are on corporate devices
* Enforce multi-factor authentication (MFA) on all corporate logins to reduce the risk of credential compromise.

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

* [September 2025](https://pixmse...