---
title: Attackers Abuse UpdraftCentral Keys to Plant Backdoors on WordPress Sites
url: https://thehackernews.com/2026/10/attackers-abuse-updraftcentral-keys-to.html
source: The Hacker News
date: 2026-10-21
fetch_date: 2026-10-22T06:46:44.303143
---

# Attackers Abuse UpdraftCentral Keys to Plant Backdoors on WordPress Sites

#1 Trusted Cybersecurity News Platform

Followed by 5.70+ million[**](https://twitter.com/thehackersnews)
[**](https://www.linkedin.com/company/thehackernews/)
[**](https://www.facebook.com/thehackernews)

[![The Hacker News Logo](data:image/png;base64...)](/)

**

**

[** Get the Latest News](#email-outer)

* [Home](/)
* [Newsletter](#email-outer)
* [Webinars](/p/upcoming-hacker-news-webinars.html)

* [Home](/)
* [Threat Intelligence](/search/label/Threat%20Intelligence)
* [Vulnerabilities](/search/label/Vulnerability)
* [Cyber Attacks](/search/label/Cyber%20Attack)
* [Webinars](/p/upcoming-hacker-news-webinars.html)
* [Expert Insights](https://thehackernews.com/expert-insights/)
* [Awards](https://awards.thehackernews.com/)

**

**

**

Resources

* [Webinars](/p/upcoming-hacker-news-webinars.html)
* [Awards](https://awards.thehackernews.com/)
* [Free eBooks](https://thehackernews.tradepub.com)

About Site

* [About THN](/p/about-us.html)
* [Jobs](/p/careers-technical-writer-designer-and.html)
* [Advertise with us](/p/advertising-with-hacker-news.html)

Contact/Tip Us

[**

Reach out to get featured—contact us to send your exclusive story idea, research, hacks, or ask us a question or leave a comment/feedback!](/p/submit-news.html)

Follow Us On Social Media

[**](https://www.facebook.com/thehackernews)
[**](https://twitter.com/thehackersnews)
[**](https://www.linkedin.com/company/thehackernews/)
[**](https://www.youtube.com/c/thehackernews?sub_confirmation=1)
[**](https://www.instagram.com/thehackernews/)

[** RSS Feeds](https://feeds.feedburner.com/TheHackersNews)
[** Email Alerts](#email-outer)

[![cybersecurity](https://blogger.googleusercontent.com/img/b/R29vZ2xl/AVvXsEgpv5Y6QePil1MjgPiKuj9qVcOEzN1QdpjV55lFLD7Nyll1Wy1-rDkPzUxoUxZBjyhD74ycWms55yNl3nOcVfzpirEVdQnc0bfulwnXhfb5IAO5oii05bR8bzttfawsmnOSBqpuNre7TO6eDyDJn4FhPAsISdesN9Nsfq-7UgOE6XMHMH5tSwffhl-qhK9h/s728-nu-rw-lo-l85-e365/wiz-d.png)](https://thehackernews.uk/ai-threat-guide-d)

# [Attackers Abuse UpdraftCentral Keys to Plant Backdoors on WordPress Sites](https://thehackernews.com/2026/10/attackers-abuse-updraftcentral-keys-to.html)

**Ravie Lakshmanan**Oct 21, 2026Cyber Attack / Web Security

[![](data:image/png;base64...)](https://blogger.googleusercontent.com/img/b/R29vZ2xl/AVvXsEhdsSYB_dpfRL3wD0MeCT_VyPyFJS8HjQAW0VuBHSTviFY4WBOQfa8MCP79qyJR3zYyMBesIXiCtL8XwwtjjLGm9Stxdv_qoIkf3_Rpc7YGFwZuzVS974TbuDfF5GkLRJX2DxFaDudlMlXSDyiZ8fvoVGaKaA-tpCr_eAvvEsfQr1uyfdBk-8KyK4aisYgC/s1700-nu-rw-lo-l85-e365/wp-backdoor.jpg)

Unknown threat actors breached TeamUpdraft's website and potentially gained unauthorized access to customers' connection keys for UpdraftCentral, UpdraftVault, and UpdraftClone, using them to backdoor WordPress sites.

TeamUpdraft is the developer behind UpdraftPlus, a popular WordPress backup plugin with over four million active installations. The vendor also offers UpdraftCentral, a remote management service that's used for managing multiple sites remotely. A client component of UpdraftCentral is shipped within every copy of UpdraftPlus.

"Over the weekend of 17-18 October we identified unauthorized access to the teamupdraft.com website," TeamUpdraft [said](https://teamupdraft.com/blog/security-incident-october-2026/) in a statement. "Our team responded straight away and worked through the night to contain it – we closed the access route, signed out every account and replaced the keys and credentials that could have been affected."

As a result of the incident, threat actors are believed to have accessed its customer database, which holds the following information -

* Names, email addresses, billing addresses and order history
* Account passwords, stored only in hashed (scrambled) form and never in plain text
* Two-factor authentication (2FA) settings
* Connection keys for UpdraftCentral, UpdraftVault and UpdraftClone

TeamUpdraft said the database does not hold any financial information, and that they are handled by Stripe and PayPal. It also emphasized that the UpdraftPlus plugin, along with self-hosted versions of UpdraftCentral and backups sent to customers' own remote storage, are not impacted.

"However, if your site was accessed through UpdraftCentral, please also re-authorise your remote storage and change any storage access keys, as a precaution," it said.

[![Cybersecurity](data:image/png;base64...)](https://thehackernews.uk/ai-security-guide-d)

In addition, TeamUpdraft said it deployed a fix to address the underlying issue, signed out every teamupdraft.com account and reset login security across the site, and released UpdraftPlus 1.26.13 (free) and 2.26.13 (Premium) to automatically disconnect every UpdraftCentral connection made before 10 p.m. BST on October 18, 2026, to prevent the old keys from working.

Other steps taken by the developer are listed below -

* Disconnected every site from UpdraftVault and issued new credentials
* Replaced every UpdraftClone client key
* Rotated its keys with payment providers and other connected services
* Implemented additional monitoring in place
* Reported the incident to the U.K. Information Commissioner's Office (ICO) and other relevant authorities

Users who have a teamupdraft.com account are advised to change their password with immediate effect (and elsewhere, if the same password has been reused), reset 2FA settings, and exercise caution when receiving unexpected emails claiming to be from TeamUpdraft.

TeamUpdraft is also recommending that cloud customers of UpdraftCentral follow the steps below as soon as possible, since the connection keys can send commands to the connected sites -

* Log in to the site's own WordPress dashboard, not through UpdraftCentral.
* Update UpdraftPlus to version 1.26.12 (free) or 2.26.12 (Premium) or later.
* Disconnect it from UpdraftCentral: go to Settings > UpdraftPlus > Advanced Tools > UpdraftCentral and delete the connection key.
* Go to Users and check for any administrator accounts you don’t recognise. Remove them.
* Go to Plugins, including the Must-Use tab if you can see it, and check for anything you don’t recognise. Remove it.
* Change the passwords for all administrator accounts on the site.
* If you find anything suspicious, consider restoring the site from a backup taken before 17 October.
* Reconnect the site to UpdraftCentral.

UpdraftVault users are being urged to reconnect their sites to the backup service, and UpdraftClone users who have created a client key are required to copy the new keys from My Account > UpdraftClone > UpdraftClone Key Management and share them with their clients.

The development comes as WordPress security company Patchstack said it observed an attacker holding valid UpdraftCentral dashboard keys issuing commands to install backdoor plugins on connected WordPress sites. The campaign is said to have run continuously through an 18-hour window on October 18 and 19, 2026.

"The attacker sends a signed plugin.upload\_plugin command over the plugin's remote procedure call channel, which listens on ordinary POST requests to the site root. WordPress installs and activates the supplied plugin through its standard installer," Patchstack security researcher Dave Jong [said](https://patchstack.com/articles/updraftcentral-key-compromise-wordpress-backdoors/).

Slovakia-based penetration testing company Nethemba, which [first detected](https://nethemba.com/updraftcentral-backdoor-analysis/) the attack in the wild, has described the rogue plugin as a backdoor that hooks into every request to the site to check if the URL contains the parameter "?\_9f5696=" and compares it with a 32-character token.

If a matching token is detected, it creates a user "data-ops43" with the display name "Site Tools," assigns it the Editor role, and grants the account "manage\_options" and "install\_plugins" permissions, allowing the operator to upload arbitrary PHP plugins and open site settings.

"Enabling registration and setting the default role to administrat...