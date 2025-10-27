---
title: Threat spotlight: Hydra
url: https://buaq.net/go-149537.html
source: unSafe.sh - 不安全
date: 2023-02-16
fetch_date: 2025-10-04T06:44:53.354727
---

# Threat spotlight: Hydra

* [unSafe.sh - 不安全](https://unsafe.sh)
* [我的收藏](/user/collects)
* [今日热榜](/?hot=true)
* [公众号文章](/?gzh=true)
* [导航](/nav/index)
* [Github CVE](/cve)
* [Github Tools](/tools)
* [编码/解码](/encode)
* [文件传输](/share/index)
* [Twitter Bot](https://twitter.com/buaqbot)
* [Telegram Bot](https://t.me/aqinfo)
* [Search](/search/search)

[Rss](/rss.xml)

[ ]
黑夜模式

![](https://8aqnet.cdn.bcebos.com/803e1c25bc5c3b7b418469e88e6031ca.jpg)

Threat spotlight: Hydra

This publication is part of our Annual Threat Monitor report that was released on the 8th of Feb
*2023-2-15 21:31:15
Author: [blog.fox-it.com(查看原文)](/jump-149537.htm)
阅读量:32
收藏*

---

*This publication is part of our Annual Threat Monitor report that was released on the 8th of Febuary 2023*. *The Annual threat Monitor report can be found [here](https://www.nccgroup.com/us/annual-threat-monitor-report-2022/)*.

**Authored by** Alberto Segura

## Introduction

Hydra, also known as BianLian, has been one of the most active mobile banking malware families in 2022, alongside [Sharkbot](https://blog.fox-it.com/2022/09/02/sharkbot-is-back-in-google-play/) and [Flubot](https://blog.fox-it.com/2022/06/29/flubot-the-evolution-of-a-notorious-android-banking-malware/) (until Flubot was takedown by Law Enforcement at the end of May 2022).

The features implemented in this banking malware are present in most of the banking malware families: injections/overlays, keylogging (listening to Accessibility events) and, since June 2022, Hydra has even introduced a cookie-stealing feature which targeted several banking entities in Spain.

It is interesting to see that lately different banking malware families are introducing the possibility to steal cookies. This could originate from cybercriminals being more eager to rent banking malware with this capability, hence giving the malware author more revenue when implemented.

During our research, we found that an important number of the command-and-control (C2) servers are located in the Netherlands. This is an interesting pattern, especially since threat actors (TAs) active in mobile malware have been frequently hosting their infrastructure in Russia and China.

## **Credential-stealing Features**

Hydra is an Android banking malware whose main goal is stealing credentials, so TAs can access those accounts and monetize them directly or indirectly by selling them to third parties. Hydra steals credentials using the following two strategies:

* **Overlays/Injections**, at the beginning of the infection, it sends a few requests to the C2 server, and receives a list of targeted applications and a URL that points to a ZIP file which contains the corresponding injections. The targets consist mostly of banks and cryptocurrency wallets. Hydra saves these injections locally and shows them as soon as it detects a user opening a banking application. That way, the victim thinks it is the official application that requests credentials or credit card information.

[![](https://i0.wp.com/blog.fox-it.com/wp-content/uploads/2023/02/injects_zip_response.png?resize=800%2C359&ssl=1)](https://i0.wp.com/blog.fox-it.com/wp-content/uploads/2023/02/injects_zip_response.png?ssl=1)

*Server response with a configuration including the URL to download a ZIP file containing all the injections*

[![](https://i0.wp.com/blog.fox-it.com/wp-content/uploads/2023/02/injects_zip_content.png?resize=800%2C171&ssl=1)](https://i0.wp.com/blog.fox-it.com/wp-content/uploads/2023/02/injects_zip_content.png?ssl=1)

*Contents of the ZIP file with the injections*

When the injection is shown and the victim enters his credentials, the malware uses JavaScript’s “Console.Log” function to send the credentials to the native Java code of the application. This function is reimplemented by the malware to send credentials to the C2 server, which is shown in the figure below.

[![](https://i0.wp.com/blog.fox-it.com/wp-content/uploads/2023/02/consolelog_save_creds.png?resize=800%2C323&ssl=1)](https://i0.wp.com/blog.fox-it.com/wp-content/uploads/2023/02/consolelog_save_creds.png?ssl=1)

*Decompiled code used to save the stolen credentials*

[![](https://i0.wp.com/blog.fox-it.com/wp-content/uploads/2023/02/senddata_creds.png?resize=800%2C486&ssl=1)](https://i0.wp.com/blog.fox-it.com/wp-content/uploads/2023/02/senddata_creds.png?ssl=1)

*Decompiled code used to send the stolen credentials to the C2 server*

* **Keylogging**,Hydra abuses the Accessibility permissions to set up an Accessibility service that receives every Accessibility event happening on the infected device. This way the malware receives change events for TextFields (to steal usernames and passwords) and button clicks.

[![](https://i0.wp.com/blog.fox-it.com/wp-content/uploads/2023/02/keylogger.png?resize=800%2C484&ssl=1)](https://i0.wp.com/blog.fox-it.com/wp-content/uploads/2023/02/keylogger.png?ssl=1)

*Keylogger code*

In order to complement the credential-stealing features, Hydra includes a screencast component that sends screenshots to the C2 server and receives commands used to simulate Accessibility events (click buttons, enter text in TextFields, etc.). This way the TAs can manipulate the target application on the victim’s device to monetize the account associated with that application. This is a good way to bypass antifraud security measures focused on checking IP addresses or devices that log in to the accounts or make transfers.

[![](https://i0.wp.com/blog.fox-it.com/wp-content/uploads/2023/02/screencast_start_call.png?resize=800%2C384&ssl=1)](https://i0.wp.com/blog.fox-it.com/wp-content/uploads/2023/02/screencast_start_call.png?ssl=1)

*Screencast feature starting code*

Besides credential-stealing features, Hydra implements features to steal other information from the infected device. Especially information required for successful account takeovers and monetization of accounts, such as received SMS messages for OTP codes, a list of installed applications, or the unlock code of the device which can be used to unlock the device and start the screencast feature.

Apart from the previously mentioned features, Hydra developers introduced a new and interesting feature around June 2022: ***stealing cookies***. With this new feature, the malware can steal cookies from sessions linked to bank accounts of victims, avoiding the need of credentials when logging in.

### **New features: Stealing Cookies**

Around June 2022 we found new samples introducing this new feature used to steal cookies from sessions after the victims log in to their accounts. Since the beginning until now, there are not that many targeted banks or other applications targeted by this feature, but the list has been increasing in the past months.

It started targeting a few applications – Google Mail and BBVA Spain -, as we can see in the following image:

[![](https://i0.wp.com/blog.fox-it.com/wp-content/uploads/2023/02/steal_cookies_targets_june.png?resize=800%2C168&ssl=1)](https://i0.wp.com/blog.fox-it.com/wp-content/uploads/2023/02/steal_cookies_targets_june.png?ssl=1)

*Targeted applications in the first versions including the cookie-stealing feature*

But after some months, TAs included two more targets – Facebook and Davivienda – to steal credentials:

[![](https://i0.wp.com/blog.fox-it.com/wp-content/uploads/2023/02/steal_cookies_targets_last.png?resize=800%2C291&ssl=1)](https://i0.wp.com/blog.fox-it.com/wp-content/uploads/2023/02/steal_cookies_targets_last.png?ssl=1)

*Targeted applications in the latest version*

As we can see in the previous pictures of the decompiled code, to implement this feature, TAs include the package name of the targeted applications alongside the URLs to the mobile login website. This way, a WebView can show the victim the official login page and, after the victim successfully logs in to his account, the cookies of the loaded website in the WebView are forwarded to the C2 server.

[![](https://i0.wp.com/blog.fox-it.com/wp-content/uploads/2023/02/send_stolen_credentials_a...