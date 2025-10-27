---
title: May 2025 Phishing Surge: Stealth MFA-Bypass Attacks Target Microsoft & Webmail Users
url: https://pixmsecurity.com/blog/blog/may-2025-phishing-surge-stealth-mfa-bypass-attacks-target-microsoft-and-webmail-users/
source: Over Security - Cybersecurity news aggregator
date: 2025-05-14
fetch_date: 2025-10-06T22:29:42.312743
---

# May 2025 Phishing Surge: Stealth MFA-Bypass Attacks Target Microsoft & Webmail Users

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

# May 2025 Phishing Surge: Stealth MFA-Bypass Attacks Target Microsoft & Webmail Users

The first half of May saw a continued surge in stealthy zero-day phishing attacks bypassing MFA. Between April 25 and May 8, attackers targeted both corporate email accounts (Microsoft 365/Outlook) and personal web services (e-commerce, streaming, personal email) used by employees. Many of these spear phishing pages employed multi-step login flows, fake multi-factor authentication (MFA) prompts, device fingerprinting, and even legitimate cloud hosting or subdomains to appear convincing. As a result, the majority of these phishing links went entirely undetected by traditional security vendors at the time of clicks. Here are some examples and highlights.

### Phishing URLs

login[.]advancedenergysolutionscorp[.]directory

julinvitepeople[.]es/today/AcrobatN/

upenn[.]it[.]com/index[.]html

bootynugget[.]hitremixes[.]com/a

image[.]landbfashion[.]com/index[.]html

update-billing[.]information[.]homatell[.]com

aeufiebvz[.]oeafiygyaeefn[.]130-51-180-103[.]cprapid[.]com

evitespree[.]info

war-6-bevgj[.]ondigitalocean[.]app

h3etffphlwabwkizjrof[.]ewetanign[.]ru

###

### Microsoft and Outlook Credential Phishing

On May 7th, a staff member at a Texas organization clicked the below Outlook spearphish delivered via an online invitation platform.

![](https://pixmsecurity.com/wp-content/uploads/2025/05/julinvitepeople.es_today_AcrobatN_.jpg)

The phishing site presented a multi-step login sequence – including an intermediary fake OTP verification step – to harvest the user’s email credentials and bypass MFA. Notably, the page was not limited to Outlook; it featured multi-brand impersonation (Outlook, Gmail, Yahoo logos) to capture whatever login the victim provided. By operating through a trusted-looking event invite link and mimicking an MFA workflow, this attack completely flanked traditional email defenses.

On May 6th and 7th, two staff members at an Idaho organization fell victim to an Outlook phishing link sent via a PDF document lure.

![](https://pixmsecurity.com/wp-content/uploads/2025/05/evitespree.info_.jpg)

The scam used what appeared to be an Adobe or DocuSign file share, prompting the user to log in with their email account in order to view a PDF. If the user entered their credentials (often twice for confirmation), the phishing flow escalated to drop malware – after harvesting the login, it redirected the victim to download a malicious executable under the guise of a PDF viewer. This multi-step attack combined credential theft with malware delivery, increasing the potential damage beyond account compromise.

Another attack on April 29th targeted a Washington organization with an advanced Microsoft 365 credential harvester.

![](https://pixmsecurity.com/wp-content/uploads/2025/05/war-6-bevgj.ondigitalocean.app_.jpg)

The phishing page simulated all major MFA options – it displayed fake prompts for Microsoft Authenticator push approvals, SMS codes, authenticator app codes, etc., complete with interval polling and animated “verifying” indicators to imitate a real Office 365 login experience. The site even employed a <noscript> fallback: if scripts were blocked or the page was loaded in a non-standard way, it would silently redirect the browser to a benign Wikipedia page.

On May 8th, three different users at a Texas organization clicked the below Microsoft spearphish, which was hosted on a deceptive subdomain “upenn.it.com.”

![](https://pixmsecurity.com/wp-content/uploads/2025/05/upenn.it_.com_index.html.jpg)

This domain masqueraded as an official University of Pennsylvania IT site, exploiting trust in a respected educational institution. The phishing site itself was extremely polished: it pulled in real Microsoft content from official CDN URLs (e.g. aadcdn.msftauth.net) to load styling and images, making the fake login page virtually indistinguishable from a legitimate Microsoft login. Additionally, hidden telemetry scripts mimicked Microsoft’s own OneDS instrumentation, likely to fingerprint the device and track user interaction in real time. Despite these novel TTPs, none of the security scanners on VirusTotal flagged the upenn.it.com phishing URL at the time (showing a 0/97 detection score), illustrating how well these attacks evaded traditional detection.

###

### Personal Account Phishing

On May 5th, a staff member at a Texas organization was spear phished with a Yahoo Mail account lure.

![](https://pixmsecurity.com/wp-content/uploads/2025/05/login.advancedenergysolutionscorp.directory.jpg)

This phishing page employed several advanced evasive techniques: device fingerprinting to tailor the content per victim, per-user unique URLs (so that the link would only work once per target), and heavy obfuscation/anti-analysis scripting to prevent security tools from examining the site. All of these measures enhanced the attack’s credibility and stealth.

On April 28th, a staff member at a Georgia organization clicked the below eBay phishing attack.

![](https://pixmsecurity.com/wp-content/uploads/2025/05/bootynugget.hitremixes.com_a.jpg)

The site displayed fake “Continue with Google/Facebook/Apple” buttons, mimicking popular OAuth single sign-on options. If clicked, these buttons would likely lead the victim through a spoofed OAuth flow to capture OAuth tokens or credentials for those providers as well.

Personal e-commerce and streaming services were targeted as well during this period. On May 5th, a Georgia employee fell for an Amazon account phishing page that included a hard-coded phone number displayed on the site, likely a recycled scam number from a previous lure or breach.

![](https://pixmsecurity.com/wp-content/uploads/2025/05/aeufiebvz.oeafiygyaeefn.130-51-180-103.cprapid.com_.jpg)

Earlier, on April 25th, an **HR staff member in Maryland clicked a Netflix phishing link**, which prompted for the user’s Netflix credentials (likely under the pretense of fixing a billing or account issue).

![](https://pixmsecurity.com/wp-content/uploads/2025/05/update-billing.information.homatell.com_.jpg)

These Netflix and Amazon attacks underscore how employees’ personal services (from shopping to streaming) are being phished alongside their corporate accounts. Such attacks often occur on work devices but outside corporate email, bypassing standard security filters and relying on the user’s trust in familiar brands.

### Mitigations

* Block the specific phishing domains (listed above) at corporate firewalls, web gateways, and endpoint security solutions to prevent any further access.
* Educate users that phishing is not just an email threat – attackers now use file shares, document services, social media, and even fake event invitations to deliver malicious links.
* Remind staff that their personal accounts (webmail, shopping, banking, streaming, etc.), when accessed on work devices, are in scope for these attacks. Emphasize that a phishing page can impersonate any service, not on...