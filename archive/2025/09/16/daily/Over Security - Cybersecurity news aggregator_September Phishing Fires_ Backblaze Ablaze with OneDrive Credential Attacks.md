---
title: September Phishing Fires: Backblaze Ablaze with OneDrive Credential Attacks
url: https://pixmsecurity.com/blog/blog/september-phishing-fires-backblaze-ablaze-with-onedrive-credential-attacks/
source: Over Security - Cybersecurity news aggregator
date: 2025-09-16
fetch_date: 2025-10-02T20:12:11.184132
---

# September Phishing Fires: Backblaze Ablaze with OneDrive Credential Attacks

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

# September Phishing Fires: Backblaze Ablaze with OneDrive Credential Attacks

![](https://pixmsecurity.com/wp-content/uploads/2025/09/Phishing-Attack-in-Rainy-City-1.png)

The first half of September witnessed yet new records of Microsoft spearphish volume, with threat actors employing advanced evasion techniques, including payload encryption, device fingerprinting, and infrastructure abuse of reputable hosts like Backblaze, Hostinger, and Telegram’s Bot API. The same period saw sustained phishing targeting of personal accounts on work devices like American Express and AOL. Here are some examples and highlights.

stab[.]ru[.]com

e0ba4b4c729c46bda371ea8244d7a314[.]hanbookupdatecompliance[.]online

ameuricnapesires[.]com

slateblue-fox-104423[.]hostingersite[.]com

f005[.]backblazeb2[.]com

login[.]stawment[.]icu

apis-f7c[.]novabrightlab[.]ru[.]com

harbor-6eb[.]groovix[.]sa[.]com

cityofmorehead[.]blessing[.]com[.]de

vtkrdwha[.]hootouloo[.]sa[.]com

baylineliving[.]it[.]com

## **Microsoft and OneDrive on Backblaze**

Standing out during this period was a widespread campaign targeting users at Minnesota and Kentucky organizations. The below Microsoft spearphish was first clicked on Sep 10 by an administrator at a Minnesota organization with a lure about a document share via OneDrive.

![](https://pixmsecurity.com/wp-content/uploads/2025/09/f005.backblazeb2.com_.jpg)

The attack references multiple PDFs–*PO393882.pdf* and *Item-list.pdf*–suggesting the lure was regarding a purchase order and targeting procurement personnel. The page was hosted on Backblaze B2 for free TLS/CDN and reputation cover, similar to prior attacks leveraging the same with CloudFlare.

The site notably uses Telegram’s Bot API to exfiltrate credentials and sends them to multiple recipients for redundancy.

*https://api.telegram.org/bot…/sendMessage?chat\_id=…&text=…*

This removes the need for costly attacker infrastructure like domains and TLS certificates needed to exfiltrate credentials. Instead, attackers get real time alerts on their phones or desktops, while the traffic leaving the victim’s network moves through an otherwise reputable [api.telegram.org](http://api.telegram.org) channel.

The page further grabs geographic information of the user to send along with compromised credentials for additional targeting efforts. The same attack was clicked by 6 other staff members at the same organization on the same day, as well as employees at a Kentucky organization on September 11.

Also leveraging legitimate infrastructure was an attack targeting a staff member at another Minnesota organization, who clicked the below Microsoft spear phish on September 9 that used Hostinger’s official \*.hostingersite.com builder domain—-a legitimate third-party hosting service.

![](https://pixmsecurity.com/wp-content/uploads/2025/09/slateblue-fox-104423.hostingersite.com_.jpg)

The period saw a number of Microsoft spearphish using evasive techniques. On Sep 4th, a staff member at a Kentucky organization clicked the below Microsoft spearphish.

![](https://pixmsecurity.com/wp-content/uploads/2025/09/stab.ru_.com_.jpg)

The page included a couple of evasive techniques, like keeping its code in a completely encrypted state until loaded inside the browser to avoid web scanners. It also checks what kind of device or browser it’s on (e.g., signs of a test/virtual environment) and will go blank or stop running if it thinks it’s being analyzed. On September 10th, an administrator at the same Kentucky organization clicked the below phishing page.

![](https://pixmsecurity.com/wp-content/uploads/2025/09/e0ba4b4c729c46bda371ea8244d7a314.hanbookupdatecompliance.online.jpg)

It uses similar encryption techniques to the prior example to evade detection. It also steals session tokens and device details from the browser as well as regular credentials in order to login elsewhere without triggering a multi-factor event.

We also saw a number of campaigns hosting phishing attacks across a large number of servers in order to quickly redirect and switch upon detection. On September 10, a staff member at a Colorado organization clicked the below Microsoft spear phish.

![](https://pixmsecurity.com/wp-content/uploads/2025/09/login.stawment.icu_.jpg)

The phishing attack is part of a large cluster of subdomains of \*.statwment[.]icu, so that the page can quietly switch to a different server if one gets blocked.

*newnewdomnewdefijbfjhi[.]stawment[.]icu*

*newnewdomnewbjbfcjfidd[.]stawment[.]icu*

*newnewdomnewcaiaibhdji[.]stawment[.]icu*

*newnewdomnewbdechaigda[.]stawment[.]icu*

The page is built to run inside other pages or in-app browsers via iframes, and it rewrites cookie settings so its login data still works across their look-alike sites—even as browsers phase out third-party cookies.

In addition to stealing passwords, a concerning tactic we saw during the period involved stealthily obtaining consent from users for full access to their mailboxes. On September 4, a director at a Kentucky organization clicked the below Microsoft spearphish.

![](https://pixmsecurity.com/wp-content/uploads/2025/09/cityofmorehead.blessing.com_.de_.jpg)

Upon harvesting a victim’s credentials, the page will redirect the user to the legitimate [office.com](http://office.com) page. In addition to stealing credentials, the page also asks for permissions to read and send messages from the user’s email, including the ability to do so when the user is offline. This effectively gives the attacker multiple keys to the victim’s mail.

The same period saw threat actors harvesting credentials on Russian servers, using aggressive device fingerprinting for enhanced targeting, and soliciting 6 digit MFA codes. On September 8, an administrator at a Kentucky organization clicked the below Microsoft spearphish.

![](https://pixmsecurity.com/wp-content/uploads/2025/09/vtkrdwha.hootouloo.sa_.com_.jpg)

The page includes payload encryption and prompts users for multiple types of 6 digit MFA codes, eg. SMS, authenticator app etc. On September 10, a staff member at a Kentucky organization clicked the below Microsoft spearphish.

![](https://pixmsecurity.com/wp-content/uploads/2025/09/apis-f7c.novabrightlab.ru_.com_.jpg)

The page exfiltrates credentials to a Russian domain: *alchemypromoh[.]ru*. The page cleverly conceals plaintext like “Enter password,” “Approve a request,” etc, by splitting characters with invisible HTML span elements, so they would not be detected by various scanning tools. On September 11, a staff member at a Kentucky organization clicked the below Microsoft spearphish.

![](https://pixmsecurity.com/wp-content/uploads/2025/09/harbor-6eb.groovix.sa_.com_.jpg)

Like other Microsoft impersonations seen during this period, the attack conceals its code in an encrypted format until loaded into the browser and features aggressive browser fingerprinting.

## **Personal Accounts Targeted on Work Devices**

The period saw personal accounts targeted on work d...