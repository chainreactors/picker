---
title: ThreatsDay: 296K IoT Botnet, 100+ Water Systems Targeted, SharePoint RCE Chain + 27 New Stories
url: https://thehackernews.com/2026/08/threatsday-296k-iot-botnet-100-water.html
source: The Hacker News
date: 2026-08-27
fetch_date: 2026-08-28T13:37:58.555583
---

# ThreatsDay: 296K IoT Botnet, 100+ Water Systems Targeted, SharePoint RCE Chain + 27 New Stories

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

[![cybersecurity](https://blogger.googleusercontent.com/img/b/R29vZ2xl/AVvXsEipoZWeZ29mSf60rRpMZ3Ucnm7oeWBfslPFPT6xADBsdvBtjd20ovH2yLscUo8pS6OTK0ItATC25VeavJh73IgqJM6Nb3apqobQ9zEVISE-d0wEFAimLYUcnffWCTowCCqs5LofRTQP25xB32KzYhlTO8lUnkZfmtELv23LlgdeKY3nyS2etYQXGdPIQtnh/s728-e100/wiz-d.png)](https://thehackernews.uk/ai-security-playbook-d)

# [ThreatsDay: 296K IoT Botnet, 100+ Water Systems Targeted, SharePoint RCE Chain + 27 New Stories](https://thehackernews.com/2026/08/threatsday-296k-iot-botnet-100-water.html)

**Ravie Lakshmanan**Aug 27, 2026Hacking News / Cybersecurity News

[![](data:image/png;base64...)](https://blogger.googleusercontent.com/img/b/R29vZ2xl/AVvXsEiwWCb2shFhaav60Wjr2-8DoStCVaQrYqkE6EBZ8F5sREap-Khi19y-w9NVmFHyHosV6xVB0fTeN_DcSpGIyCZ621SnjqZozRVG70ceOey_D8djA5r5rpP9tFkRSESgs4kHZilTMoz2y8uqX-iTLR0JjjZkhypYjCCAEvQKzyU7xarQpt3sYvJc-fnWSWlb/s1700-e365/threats.jpg)

A fake login page. A fake security scan. A fake productivity app. Apparently, pretending to be useful is still one of the easier ways into a machine.

The rest of the week gets stranger: botnets borrowing AI, command traffic hiding in public infrastructure, malicious tools waiting before showing their real behavior, exposed systems getting scanned, and exploit windows shrinking again. Different tricks, same advantage: attackers keep finding places where trust is cheap and friction is low.

That sets the tone. Here’s the full list of what surfaced this week.

**The threats change every week. Subscribe, and we’ll alert you when each new ThreatsDay Bulletin is out.**

1. Social engineering attempt fails

   [ReliaQuest Targeted in Failed Extortion Attack](https://reliaquest.com/blog/threat-spotlight-social-engineering-attempt-against-reliaquest-what-we-found/)

   Cybersecurity company ReliaQuest has confirmed that one of its employees was targeted in a social engineering attack after hackers impersonated a member of the security team. The incident took place on August 22, 2026. "The threat actor registered a lookalike domain and stood up a fake ReliaQuest single sign-on (SSO) page behind a content delivery network," the company [said](https://reliaquest.com/blog/threat-spotlight-social-engineering-attempt-against-reliaquest-what-we-found/). "The threat actor then called multiple ReliaQuest teammates, each time posing as a security employee by name in an attempt to steer them towards the fake page. One teammate entered their password and approved the push notification on their phone. That handed the attacker a brief session on our identity dashboard." ReliaQuest said the extent of the access was view only, and that no applications or systems were accessed, and no customer data was ever touched. Although the company did not attribute the incident to a particular threat actor, it noted the playbook aligns with tactics adopted by ShinyHunters and other extortion crews, such as "an impersonation call, a throwaway lookalike domain registered and burned within the hour, a harvesting page behind a content delivery network, MFA push abuse, and a rapid attempt to enroll a new authenticator." The [development](https://socradar.io/blog/shinyhunters-reliaquest-breach/) comes as ShinyHunters listed the company on its dark web portal. Last week, ReliaQuest said it's tracking a ShinyHunters campaign using domains that follow the "company[.]claims" pattern, including "reliaquest[.]claims."
2. Trojanized productivity apps

   [Fake Websites Deliver Malware](https://blog.gdatasoftware.com/2026/08/38468-projextor-abusing-electron)

   Fake websites advertising productivity software are being used to [lure users into downloading](https://blog.gdatasoftware.com/2026/08/38468-projextor-abusing-electron) a deceptively functioning program that contains malware. The Electron-based applications, such as Kitchen Canvas, Food or Meal Formula, DocConvertWizard, and other PDF conversion tools under different names, gain the ability to dynamically execute injected scripts and access desktop capture functionality through Electron APIs.
3. Live operator-driven phishing

   [JWR Phishing Framework Spotted](https://blog.talosintelligence.com/dissecting-the-jwr-phishing-framework/)

   An undocumented phishing framework, internally branded "JWR" by its developer, is designed to convincingly impersonate checkout and login pages across major payment and shopping platforms. "The client engine of the JWR phishing framework is a real-time, operator-driven system that, rather than merely logging form submissions like a static credential-stealing page, keeps an AES-CTR encrypted WebSocket open to the threat actor so they can steer each victim's session live," Cisco Talos [said](https://blog.talosintelligence.com/dissecting-the-jwr-phishing-framework/). "The victim data targeted by the actor using JWR extends well beyond payment data, encompassing identity documents, Social Security numbers, passport and driver's license images, website and PayPal credentials, 2FA codes, and full device fingerprints, all committed to the actor's server once a session ends." The JWR phishing framework is assessed to be a variant of The Outsider phishing-as-a-service (PhaaS) platform, based on several similarities in the client engine scripts and functionalities of the two PhaaS platforms.
4. Android fraud bot for rent

   [Octagon Android Banking Malware Sold on Underground Forums](https://iverify.io/blog/octagon-android-bot-crypto-wallets-banking-apps)

   Cybersecurity researchers have disclosed Octagon, a previously undocumented Android on-device fraud bot sold as malware-as-a-service (MaaS) by the Russian-speaking actor AndroidKitKat. "The operator advertises Octagon for $1,400 a month, giving buyers accessibility overlays, hidden VNC, SMS and one-time password interception, unlock-pattern capture, and on-screen balance reading," iVerify [said](https://iverify.io/blog/octagon-android-bot-crypto-wallets-banking-apps). "It targets crypto wallets and banking apps after installation, while the delivery app can use an unrelated theme."
5. Rust backdoor tied to ransomware

   [C2Looper Likely Used by Ransomware Group](https://www.zscaler.com/blogs/security-research/c2looper-new-backdoor-likely-tied-ransomware-github-c2)

   A new Rust-based malware family dubbed C2Looper is likely leveraged by a ransomware-related threat act...