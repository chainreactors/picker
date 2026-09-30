---
title: 101 Malicious npm Packages Add Developers' WhatsApp Accounts to Groups Without Consent
url: https://thehackernews.com/2026/09/101-malicious-npm-packages-add.html
source: The Hacker News
date: 2026-09-29
fetch_date: 2026-09-30T07:42:59.609683
---

# 101 Malicious npm Packages Add Developers' WhatsApp Accounts to Groups Without Consent

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

[![cybersecurity](https://blogger.googleusercontent.com/img/b/R29vZ2xl/AVvXsEj2IlqZRz59oSh813xvx6J6LZwp36zTJVBxQ-PeUsJRUAsFcG59ozpg3_EkL6lxZPOdBGD_o8YVUq2CVyutLmT7SgKt513yyCnRmX1J8e5b358cLIneCtSSp46pMvfQ-md9-VagqDnUxxJPuU1CFx7hjpZv75B2E77SI400cPs5PKE4H0uWsGfvEwg_lfzn/s728-nu-rw-lo-l85-e365/prompt-injection-response-d.png)](https://thehackernews.uk/prompt-injection-response-d)

# [101 Malicious npm Packages Add Developers' WhatsApp Accounts to Groups Without Consent](https://thehackernews.com/2026/09/101-malicious-npm-packages-add.html)

**Ravie Lakshmanan**Sep 29, 2026Supply Chain / Malware

[![](data:image/png;base64...)](https://blogger.googleusercontent.com/img/b/R29vZ2xl/AVvXsEhhUmW5o4XCEsBlPE2MKecTG-IHCrk1WHeLajiNnRTpGtT-DDhpYVID3Pon7cseFiJN24GulDnjR7TPRe6h-kQEuJBPRl87atgBytMvKbiRV4h_DHWtxQEtogyy3U-aAD6ErNCrYiOQV-tHvHcw_P4W8z37PpR-jo70sePvtLIvMwKx7MJuE8Fazhyphenhyphen7_KI5/s1700-nu-rw-lo-l85-e365/npm-whatsapp.jpg)

Cybersecurity researchers have identified a cluster of 101 npm packages that are used to trap developers into a WhatsApp group subscriber campaign dubbed **PhantomSub**.

"The malicious packages abuse the 'Baileys' WhatsApp open source project to add the victims to groups without their consent," OX Security researchers Nir Zadok, Moshe Siman Tov Bustan, and Vitalii Chepurko [said](https://www.ox.security/blog/phantomsub-malicious-npm-campaign-secretly-adds-users-to-whatsapp-spam-channels/) in a technical write-up published Monday.

These packages have been collectively downloaded 490,000 times, out of which 116,000 occurred in the last 30 days. The names of some of the packages are below -

* ourin-baileys
* @nexustechpro/baileys
* @badzz88/baileys
* @ostyado/baileys
* levvleys
* @vanzxy/baileys
* @yudzxml/baileys
* @chatunity/baileys
* @kelvdra/baileys
* neuralwhatsapp
* lilys-baileys
* @fyxzpediaa/baileys
* noxleyss
* @xrelly-stack/bails
* alipclutch-baileys
* kurobails
* eliteprotech-baileys
* @xayz/baileys
* chromestaff-baileys
* @sanzoffc/baileys
* @sairidev/baileys-new
* cloud-baileys
* @nyzzpediaa/baileys-new
* ishumdz-bail
* nishiki-bail
* diezyclutch-baileys
* oktz-baileys
* my-auto-follow

Details of the activity first emerged in August 2026, when SafeDep [said](https://thehackernews.com/2026/08/16-typosquatted-rubygems-packages-steal.html) it identified a set of Baileys npm forks that were found to engage in malicious behaviors, such as stealthily making the installer's WhatsApp account follow channels the package author controls and injecting the author's advertising URL into every image and video the bot sends.

[![Cybersecurity](data:image/png;base64...)](https://thehackernews.uk/trust-world-update-d)

Then, earlier this month, the Xygeni Security Research Team disclosed details of another Baileys mod named "[@dappaoffc/baileys-mod](https://xygeni.io/blog/malicious-npm-package-in-baileys-fork-skyzopedia-case/)" that was also found to subscribe the developer's authenticated WhatsApp bot session to attacker-controlled newsletter channels.

OX Security's analysis has uncovered three different variants of the malware, each implementing different ways of handling the subscription routine -

* Variant 1 (19 packages), which fetches channel IDs from GitHub at runtime
* Variant 2 (60 packages), which embeds channel IDs in its source code in cleartext
* Variant 3 (14 packages), which embeds channel IDs in its source code in encoded and obfuscated form

One of the WhatsApp groups is assessed to be based in Indonesia and advertises accounts for mobile games and applications, such as Mobile Legends: Bang Bang and TikTok. These posts also specify a phone number that's linked to an Indonesian business WhatsApp account named "Dan."

Some of the other identified groups and channels are listed below -

* Neural (798 followers), which markets Resource Supplies (RSS) sales using JualanRSS, an online marketplace that sells in-game resources such as food, ore, stone, timber, and gold.
* MONTE – BMG (1,000 followers)
* CORTANA TECH (1,300 followers)
* Fyxzpedia.ID – Utama (4,800 followers)

"The channels we could identify are mostly small bot-seller and 'market' channels, largely Indonesian, where follower counts serve as social proof for selling bot scripts, bot-building services, 'premium' APKs and social-media boosting," OX Security said.

[![Cybersecurity](data:image/png;base64...)](https://thehackernews.uk/ai-security-guide-b)

"Many packages in this campaign are not independent. The same channel IDs, the same remote channel lists, and the same GitHub accounts appear across packages with different names and publishers. A shared channel means a shared beneficiary: whoever owns the channel collects followers from every package that targets it, whoever published the package."

Developers are advised to check if they have been added to the WhatsApp groups, block them, configure detection rules for blocking the malicious npm Baileys packages, and refrain from using packages that require the personal WhatsApp account to be connected.

Found this article interesting? Follow us on [Google News](https://news.google.com/publications/CAAqLQgKIidDQklTRndnTWFoTUtFWFJvWldoaFkydGxjbTVsZDNNdVkyOXRLQUFQAQ), [Twitter](https://twitter.com/thehackersnews) and [LinkedIn](https://www.linkedin.com/company/thehackernews/) to read more exclusive content we post.

SHARE
[**](#link_share)
[**](#link_share)
[**](#link_share)
**

[**Tweet](#link_share)

[**Share](#link_share)

[**Share](#link_share)

**Share

**
[**Share on Facebook](#link_share)
[**Share on Twitter](#link_share)
[**Share on Linkedin](#link_share)
[**Share on Reddit](#link_share)
[**Share on Hacker News](#link_share)
[**Share on Email](#link_share)
[**Share on WhatsApp](#link_share)
[![Facebook Messenger](data:image/png;base64...)Share on Facebook Messenger](#link_share)
[**Share on Telegram](#link_share)

SHARE **

[Malware](https://thehackernews.com/search/label/Malware), [Open Source Security](https://thehackernews.com/search/label/Open%20Source%20Security), [Supply Chain](https://thehackernews.com/search/label/Supply%20Chain), [WhatsApp
Tag Pairs](https://thehackernews.com/search/label/WhatsApp%0ATag%20Pairs)

⚡ Top Stories This Week

[![The Hacker News](data:image/svg+xml;base64...)

Roundcube Pre-Auth SQL Injection Flaw Actively Exploited in the Wild](https:/...