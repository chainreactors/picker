---
title: RedWing MaaS Packages Android Bank Fraud as a Telegram Rental Service
url: https://thehackernews.com/2026/07/redwing-maas-packages-android-bank.html
source: The Hacker News
date: 2026-07-07
fetch_date: 2026-07-08T05:05:52.403486
---

# RedWing MaaS Packages Android Bank Fraud as a Telegram Rental Service

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

[![cybersecurity](https://blogger.googleusercontent.com/img/b/R29vZ2xl/AVvXsEgrKWHErc__Wn0forfQ5eJ5sIR1hVKCHCTeNQOaAX4lbygJ8S1Xpemx6JXl78dpwiT65DDBGURp48A3EemKzmli-jXPI3v1928MnJm-1j2ZPUaFXCvuySFhyphenhyphenKR-Li6fAinFT2bhLgsqUSNUR_ggMAnOHi3jD1qYWHXvueX8WdtxAd6GYety9cBGYABo18hX/s728-e100/tt-d.jpg)](https://thehackernews.uk/ai-zero-trust-h-d)

# [RedWing MaaS Packages Android Bank Fraud as a Telegram Rental Service](https://thehackernews.com/2026/07/redwing-maas-packages-android-bank.html)

**Swati Khandelwal**Jul 07, 2026Malware / Mobile Security

[![](data:image/png;base64...)](https://blogger.googleusercontent.com/img/b/R29vZ2xl/AVvXsEjdqPEGRKkKA7pjGNpR8hijHzJLPvyPD1g1C8bTt91eLUOFdu6Jw99i8LFybvHG9SP3syQ8shdXpC6EhinlQoB9aTgBMtejiCWAzVhhTi0o3nCTKZeKNnwDY0J_Lbf9LGN-KIQIoJ7-GW2op-JUcBg64uz5Actwh7TsFEstwNx9fXnLj4SODskUpnX9TPE/s1700-e365/android-trojan-telegram.jpg)

A new Android malware operation called **RedWing** is being rented out on Telegram as a ready-made bank-fraud service. It lets even low-skill criminals take over a victim's phone, steal their banking logins, and capture the one-time codes that protect their accounts.

[Zimperium's zLabs](https://zimperium.com/blog/redwing-a-mobile-malware-as-a-service-operation), which found the operation, says it looks like a new variant of [Oblivion](https://www.certosoftware.com/insights/oblivion-the-new-300-android-rat-that-beats-every-major-phone-manufacturers-security/), a $300-a-month rent-a-malware tool documented earlier this year.

RedWing is sold as a complete product, in subscription tiers with referral discounts, guides, and how-to videos, so a buyer needs no malware-writing skill. A Telegram bot builds each buyer a custom app on demand.

Researchers say a substantial number of the resulting droppers and payloads currently evade conventional security tools.

Infection starts with a phishing link that opens a fake app-store page. The kit's dropper builder can mimic Google Play, the Galaxy Store, and AppGallery, or build fully custom pages, complete with fake ratings, reviews, and download counts. The page then coaxes the user into installing the app from outside the official store and approving its permissions.

[![Cybersecurity](data:image/png;base64...)](https://thehackernews.uk/ai-vuln-protection-d)

The app stages its permission requests one screen at a time. A harmless-looking web page sits in the background while pop-up cards request permissions framed as routine: turn off battery limits, set the app as the default text-message handler, and switch on notifications.

It also asks to turn on Android's Accessibility service, which malware abuses to read the screen and control the phone.

[![](data:image/png;base64...)](https://blogger.googleusercontent.com/img/b/R29vZ2xl/AVvXsEgM7gb4IRJtFXb8hXtojEJcGQaq58gbp7FWBCsZLe0as3OsB8ovqx7u8ZwCXvPNfZLC5bC-vf1QlAR_aP0mVlDyW9h8zUJQv8y6ECUrRUMijE5rQejkmsgMoWx5xxyuTtQ4MC-bxFK2CDKeMzE5WDsz-wxBwUPTC3Ch1Yn9oH0rnBax4s0E-tphK_hPegI/s1700-e365/banking-trojan.jpg)

With those permissions, RedWing has broad control of the phone. Its capabilities include:

* Fake login screens, called overlays, that appear over real banking and cryptocurrency apps to steal passwords.
* Reading incoming texts for one-time passcodes, and using Accessibility to lift codes, card numbers, and PINs off the screen as they appear.
* Silently switching the victim's incoming calls over to the attacker, using a hidden carrier code (\*21\*) to turn on call forwarding, which knocks out phone-based verification and bank fraud-check calls.
* Live screen streaming and a keylogger, so operators can watch and control the phone in real time.
* Switching on the camera and microphone, reading files, stealing contacts and call logs, and tracking location.
* Pooling infected phones to flood a target website with traffic, a denial-of-service attack.

Buyers choose their own targets, and the malware splits its targeting into two. The apps it watches through Accessibility are baked into each copy, which points to a fresh app being built to order once a buyer picks targets. The overlay targets, by contrast, can be changed later from the control panel without pushing out a new app.

[![](data:image/png;base64...)](https://blogger.googleusercontent.com/img/b/R29vZ2xl/AVvXsEh1SxTZ6shODE18HlIh4xQPYkcKz6oMkClCVQ4XYfF6oL3FULMwFUN5UroHcPnEZyffpP_RmTZfwo0NudPkbVXJ0egQMVu_seJb2ldRqnHGEG6DbshsRbe19hU5IJcB_tLZJI5IxJKsRBQpY1Y13tAAmCuqe81w6Ayq6xQ8VkwqsMqapAezBOPvAPsRDRE/s1700-e365/mobile-apps.jpg)

Zimperium counted 82 targeted institutions across several sectors, with a strong focus on Russian financial firms, though that list can shift at any time. The evidence points to the Russian market: one sample used a fake page for Russia's RuStore. Experts say the operation appears linked to Russian threat actors but stops short of confirming it.

RedWing fits a wider move in Android crime toward on-device fraud, where attackers operate inside the victim's own banking session instead of stealing a password to use elsewhere.

[![Cybersecurity](https://blogger.googleusercontent.com/img/b/R29vZ2xl/AVvXsEhr7HGzx4ULDSqwnN820pPGxlPxqqVxKgIrI5II1iWdspOL6yHZsdB5lWoXU3LmhIU4dtnph89fLZ0CxrQSs-ufs6Mo4eD-d-Cpx-DsV1G15eC-phLACF7hyaKSIH1zIdj3AuD7lHSHnVelmKVMoVV-_zvtJuodsSIDKu6uSRfU6fZBkO-2PERqKSfIn6dA/s728-e100/sygnia-d-2.jpg)](https://thehackernews.uk/sygnia-cyber-response-d-2)

Researchers flagged a near-identical Russian-market rental kit, [Fantasy Hub](https://thehackernews.com/2025/11/android-trojan-fantasy-hub-malware.html), last year. The same techniques turn up in [Albiriox](https://thehackernews.com/2025/12/new-albiriox-maas-malware-targets-400.html), aimed at more than 400 finance apps, and [Klopatra](https://thehackernews.com/2025/10/new-android-banking-trojan-klopatra.html), which used hidden remote control and fake overlays to drain accounts while victims slept.

RedWing needs no Android exploit. It works only when a user installs the app from outside an official store and approves the prompts, so the first line of defense is what happens at install time. For individuals:

* Install apps only from official stores, and treat any "update" that arrives by link or text message as suspect.
* Do not turn on "install from unknown sources," and do not grant Accessibility, default text-message handler, or battery-exemption...