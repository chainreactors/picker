---
title: August Phish Flood Warning: Credential Attacks Raining Down From Cloudflare
url: https://pixmsecurity.com/blog/blog/summer-phishing-floodwarning-credential-attacks-raining-down-from-cloudflare/
source: Over Security - Cybersecurity news aggregator
date: 2025-08-31
fetch_date: 2025-10-07T00:17:57.114739
---

# August Phish Flood Warning: Credential Attacks Raining Down From Cloudflare

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

# August Phish Flood Warning: Credential Attacks Raining Down from Cloudflare

![](https://pixmsecurity.com/wp-content/uploads/2025/08/cloud-2-1.png)![](https://pixmsecurity.com/wp-content/uploads/2025/08/cloud.png)

Later August saw records of phishing activity spanning Microsoft support scams, Adobe file shares and Paperless Post deliveries. Tactics involved MFA relay kits and usage of CloudFlare infrastructure to evade detection. The same period saw continued targeting of personal accounts like Amazon and Yahoo on work devices. Below are some examples and highlights.

tgcj86gcjyp[.]z13[.]web[.]core[.]windows[.]net

hdbn46dhu[.]z13[.]web[.]core[.]windows[.]net

vtgg97gvy[.]z13[.]web[.]core[.]windows[.]net

asdfdgfcb17ygkjhmb[.]z13[.]web[.]core[.]windows[.]net

sfgd9jthg[.]z13[.]web[.]core[.]windows[.]net

hdbn46dhu[.]z13[.]web[.]core[.]windows[.]net

asfzdxgc7jh[.]z13[.]web[.]core[.]windows[.]net

adsdgfc12dgfc[.]z13[.]web[.]core[.]windows[.]net

erf86efgf[.]z13[.]web[.]core[.]windows[.]net

softviewt[.]de/desk/

darkgreen-crocodile-418773[.]hostingersite[.]com

lexinfoinvite[.]online

xed[.]draigoodro[.]com[.]de

peachpuff-turtle-958085[.]hostingersite[.]com

lph5gcy[.]8izfv5f65u[.]workers[.]dev

underclothes[.]primesicilia[.]it[.]com

ekenewrthanmoupasdertghumused[.]net

comforthcruisebookcrise[.]one

## Microsoft Spearphish and Support Scams

On August 17th, a Texas staff member clicked on the below Microsoft spearphish.

![](https://pixmsecurity.com/wp-content/uploads/2025/08/softviewt.de_.jpg)

This offers the victim multiple options for logging in with different accounts, eg. Outlook, AOL, Office 365, Yahoo etc. and additionally phishes the target’s OTP code to bypass multi factor authentication. It also includes a fake CloudeFlare challenge in order to evade traditional scanners.

On August 18th, three administrators at the same organization clicked on a cluster of Microsoft support scams similar to others observed earlier in August.

![](https://pixmsecurity.com/wp-content/uploads/2025/08/tgcj86gcjyp.z13.web_.core_.windows.net_.jpg)

Like earlier instances, these pages are customized based on the target’s IP address and use URL parameters to swap the phone number to route different recipients to different call centers. The pages lock the device keyboard, making many users feel that calling the support number is the only way to escape. Others identical attacks targeting the organization include:-

**hdbn46dhu[.]z13[.]web[.]core[.]windows[.]net**

**vtgg97gvy[.]z13[.]web[.]core[.]windows[.]net**

On August 19th, a similar attack was clicked by an administrator at a Kentucky organization, where we note the phone number adjusting based on a different Geography.

![](https://pixmsecurity.com/wp-content/uploads/2025/08/asdfdgfcb17ygkjhmb.z13.web_.core_.windows.net_.jpg)

Other clusters were clicked around the country, like the below examples targeting administrators in Colorado and Georgia on August 18th.

![](https://pixmsecurity.com/wp-content/uploads/2025/08/sfgd9jthg.z13.web_.core_.windows.net_.jpg)![](https://pixmsecurity.com/wp-content/uploads/2025/08/hdbn46dhu.z13.web_.core_.windows.net_.jpg)

On August 17th, the below Adobe Cloud phishing attack was clicked by a California staff member.

![](https://pixmsecurity.com/wp-content/uploads/2025/08/lexinfoinvite.online.jpg)

In addition to leveraging an Adobe file share to evade mailbox inspection, the page itself contained almost 1M characters to evade various sandbox inspection tools.

On August 18th, a Kentucky staff member clicked the below Microsoft spearphishing attack.

![](https://pixmsecurity.com/wp-content/uploads/2025/08/xed.draigoodro.com_.de_.jpg)

This page uses a packed JS loader and an anti-analysis clipboard hook—both common in modern phishing kits—plus a long per-victim id token for tracking.

On August 18th, two administrators at a Kentucky organization clicked Microsoft phishing pages that hosted on primesicilia[.]it[.]com.

![](https://pixmsecurity.com/wp-content/uploads/2025/08/underclothes.primesicilia.it_.com_.jpg)

![](https://pixmsecurity.com/wp-content/uploads/2025/08/leaved.primesicilia.it_.com_.jpg)

The pages prompt for 6-digit MFA codes, enabling real-time relay or OTP capture. The text is obfuscated with invisible spans between letters, defeating naive scanners that look for phrases like “Enter password” or “Sign in.” And most graphics are embedded as data URIs, so the page makes almost no external requests, making it harder to detect.

On August 12th, a staff member at a Massachusetts organization clicked the below phishing site impersonating Microsoft and Google.

![](https://pixmsecurity.com/wp-content/uploads/2025/08/peachpuff-turtle-958085.hostingersite.com_-1.jpg)

It’s hosted on a throwaway Hostinger subdomain (\*.hostingersite.com), a cheap, disposable setup attackers churn through to dodge domain blocks and takedowns. It also embeds at least one image as a base64 data URI directly in the HTML, which reduces external requests, keeps everything self-contained, making it harder to detect.

On August 21, another Kentucky staff member clicked the below Microsoft phishing link that also leveraged third party infrastructure, this time from CloudFlare

![](https://pixmsecurity.com/wp-content/uploads/2025/08/lph5gcy.8izfv5f65u.workers.dev_.jpg)

The site uses Cloudflare Workers, a platform that lets anyone quickly deploy a site under a \*.workers.dev subdomain, with HTTPS, CDN edge delivery, and Cloudflare IPs by default. Phishers like it because they don’t need their own hosting or certificates, the site inherits the reputation/performance of a major provider, and they can rotate throwaway subdomains quickly to evade domain-age and blocklist checks.

The same period saw continued targeting of corporate credentials with Paperless Post deliveries, which also leveraged CloudFlare infrastructure, like the two pages below that were clicked by Kentucky staff members.

![](https://pixmsecurity.com/wp-content/uploads/2025/08/ekenewrthanmoupasdertghumused.net_.jpg)

![](https://pixmsecurity.com/wp-content/uploads/2025/08/comforthcruisebookcrise.one_.jpg)

The attacks likely used the same kit that includes a multi-brand credential harvester that lets victims “sign in” with Outlook/Office 365/Yahoo/AOL (tracking the chosen brand via a hidden ID). It uses a two-stage flow and an OTP prompt to phish MFA codes. The first site also includes a Cloudflare challenge (challenge script//cdn-cgi/…), likely to mask the true hosting and borrow Cloudflare’s reputation and TLS.

## E-Commerce Accounts Targeted on Work Devices

The same period saw continued targeting of personal accounts on work devices that again used CloudFlare infrastructure. For example, on August 26th, a staff member at an Illinois organization clicked the below Yahoo phishing attack on their work device.

![](https://pixmsecurity.com/wp-content/uploads/2025/08/login.envvite.top_.jpg)

The page’s HTML explicitly indicates a redirect from...