---
title: uCreator Android Spyware Can Steal Telegram 2FA Passwords and Clone WeChat Accounts
url: https://thehackernews.com/2026/10/ucreator-android-spyware-can-steal.html
source: The Hacker News
date: 2026-10-26
fetch_date: 2026-10-27T07:05:44.126360
---

# uCreator Android Spyware Can Steal Telegram 2FA Passwords and Clone WeChat Accounts

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

# [uCreator Android Spyware Can Steal Telegram 2FA Passwords and Clone WeChat Accounts](https://thehackernews.com/2026/10/ucreator-android-spyware-can-steal.html)

**Swati Khandelwal**Oct 26, 2026Cyber Espionage / Mobile Security

[![](data:image/png;base64...)](https://blogger.googleusercontent.com/img/b/R29vZ2xl/AVvXsEgdBBtFdo2KmBzapUDlLWoS0hh17lYfWUw0kOLWTfbgeNOTP5F5pEJPmWSzBHkjSv4HR-vwfJ-Ba38Tg_su11Zi4CDKXJ29BnlQdCrU-oU84jl7TAET_aPyWV2fRazSLy0hBz8sBP3EhFubGETPdPwpnAFAX0CSbEQfsA65JqQMob9R_4cPbbJRi91KAkY/s1700-nu-rw-lo-l85-e365/telegram-wechat.jpg)

A rentable Android spyware kit called **uCreator** takes over Telegram and WeChat accounts by hiding its code inside working copies of the two apps, [researcher Ovi found](https://www.0x0v1.com/ucreator-virtualization-based-android-spyware-platform-targeting-wechat-telegram-and-other-messaging-apps/). It only reaches people who install one of these tampered copies, spread outside the official app stores, or who run WeChat inside the kit makers' own container app.

The kit's Telegram part matches **Baohuo**, a backdoor that Doctor Web [reported in October 2025](https://thehackernews.com/2025/10/weekly-recap-wsus-exploited-lockbit-50.html). Doctor Web found Baohuo in tampered copies of Telegram X, an Android app from Telegram. At the time, the company estimated that more than 58,000 devices were infected.

The Hacker News compared the two reports. Doctor Web's [technical description](https://vms.drweb.com/virus/?i=30931101&lng=en) of Baohuo lists the same code namespace, `com.ucreator.tgjar`, the same command-and-control (C2) server, and matching command names as Ovi's analysis.

Ovi's analysis, published October 21, 2026, does not mention Doctor Web's findings, and Doctor Web did not name the kit. It is not clear whether the kit's makers or one of their customers ran the campaign Doctor Web tracked.

### Who Is Exposed

The tampered apps spread through sideloading, where a person installs an app file directly instead of from an app store, and through social engineering, Ovi found. He could not confirm how every victim was infected.

A second route is the kit makers' own container app, called 洋葱盒子 ("Onion Box"), which runs other apps inside itself.

Some of the tampered Telegram X copies use the same package name as the real app on Google Play, so the name alone does not give them away.

[![Cybersecurity](data:image/png;base64...)](https://thehackernews.uk/ai-governance-platform-d)

Doctor Web [found](https://news.drweb.com/show/?i=15076) that Baohuo copies had been spreading since mid-2024 through in-app ads that led to fake app store sites. Those sites promoted Telegram X as a dating and video chat app.

The sites' banners were available only in Portuguese, for users in Brazil, and in Indonesian. Even so, Doctor Web's 2025 map of infected devices by country put India first, at 22.8%, ahead of Brazil at 20.5% and Indonesia at 9.6%.

Baohuo copies also turned up in the third-party stores APKPure, ApkSum and AndroidP. On APKPure, one was listed under the official developer's name, although its digital signature was different.

Ovi got access to one of the kit's command servers. It held data on victims apparently located in China and the United States, but not enough for a reliable count. He calls his report "an analysis of technical capability, not a measurement of victim impact."

The apparent targets, still unconfirmed, are users of mobile wallets and messaging apps in China and Southeast Asia, including WeCom, QQ, WhatsApp, LINE, Zalo, KakaoTalk, Viber, GCash and MoMo. He found code supporting about 20 apps, but has published code only for Telegram and WeChat.

[![](data:image/png;base64...)](https://blogger.googleusercontent.com/img/b/R29vZ2xl/AVvXsEitJXosvRlYtX_oRzqMQ8hLtm5FdK27T9puWMjalZuBAirMlHqDFIs7ldcn6dGAwa7XmCIQgN4oS03houiSioiRhVj6sh9sqRuiN2C4y2rsZ3wmilCWoRpWt_I5xpbMJKRAmdXfeDpUjDBPplB2FN4NQb9qTVTvVGhSwSCsmotSAcYpN6ni1hY5eY0Q5QA/s1700-nu-rw-lo-l85-e365/chain.png)

The kit's hooking engine is the part that lets its code intercept an app's functions. Ovi checked it on a Pixel 10 Pro running Android 17. It could not find an internal Android function it relies on, because newer Android versions changed that function.

Another tool, Frida, could still hook apps the same way on that phone. Ovi therefore describes this as extra work for the kit's makers, not proof that Android 17 blocks the attack.

The newest sample, dated July 29, 2026, still carried the old engine. He recovered samples built for Android 16 but did not report testing that version. He has not tested phones from Chinese makers.

### How It Takes Over a Telegram Account

Inside a tampered Telegram app, the kit's code starts with the app and runs with the app's own identity and permissions, Ovi found. That gives it the same access as the signed-in app.

Each tampered app also runs a local command server inside itself. The code for each target app is downloaded after installation, which makes the installer file harder to analyze on its own.

Attackers can send any database query to the app's message store and get chat history back.

Telegram's two-step verification (2FA) password is entered in the app, which uses it to [generate a login proof on the phone](https://core.telegram.org/api/srp). The kit hooks that step and copies the password in readable form before the app hashes it.

With the password, the code can reset the account's logged-in sessions, change the linked phone number, or delete the account. Other parts of the code are designed to lock out the owner while keeping the attacker's session alive.

The code can also hide the attacker's session from the device list that the tampered app shows the user.

Doctor Web's description of Baohuo covers the same device-hiding. The backdoor also sends the account's phone number, name and password to its server every three minutes.

Neither Ovi nor Doctor Web says whether a hidden session still appears on the user's other, untampere...