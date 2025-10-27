---
title: Threat Spotlight – Hydra
url: https://buaq.net/go-149908.html
source: unSafe.sh - 不安全
date: 2023-02-18
fetch_date: 2025-10-04T07:20:02.898977
---

# Threat Spotlight – Hydra

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

![](https://8aqnet.cdn.bcebos.com/cca3930c64703219ae44fa70085c54aa.jpg)

Threat Spotlight – Hydra

This publication is part of our Annual Threat Monitor report that was released on the 8th of
*2023-2-17 23:30:38
Author: [research.nccgroup.com(查看原文)](/jump-149908.htm)
阅读量:35
收藏*

---

This publication is part of our Annual Threat Monitor report that was released on the 8th of Febuary 2023. The Annual threat Monitor report can be found [here](https://www.nccgroup.com/us/annual-threat-monitor-report-2022/).

**Authored by** Alberto Segura

## Introduction

Hydra, also known as BianLian, has been one of the most active mobile banking malware families in 2022, alongside [Sharkbot](https://blog.fox-it.com/2022/09/02/sharkbot-is-back-in-google-play/) and [Flubot](https://blog.fox-it.com/2022/06/29/flubot-the-evolution-of-a-notorious-android-banking-malware/) (until Flubot was takedown by Law Enforcement at the end of May 2022).

The features implemented in this banking malware are present in most of the banking malware families: injections/overlays, keylogging (listening to Accessibility events) and, since June 2022, Hydra has even introduced a cookie-stealing feature which targeted several banking entities in Spain.

It is interesting to see that lately different banking malware families are introducing the possibility to steal cookies. This could originate from cybercriminals being more eager to rent banking malware with this capability, hence giving the malware author more revenue when implemented.

During our research, we found that an important number of the command-and-control (C2) servers are located in the Netherlands. This is an interesting pattern, especially since threat actors (TAs) active in mobile malware have been frequently hosting their infrastructure in Russia and China.

## Credential-stealing Features

Hydra is an Android banking malware whose main goal is stealing credentials, so TAs can access those accounts and monetize them directly or indirectly by selling them to third parties. Hydra steals credentials using the following two strategies:

**Overlays/Injections**: At the beginning of the infection, it sends a few requests to the C2 server, and receives a list of targeted applications and a URL that points to a ZIP file which contains the corresponding injections. The targets consist mostly of banks and cryptocurrency wallets. Hydra saves these injections locally and shows them as soon as it detects a user opening a banking application. That way, the victim thinks it is the official application that requests credentials or credit card information.

![](https://i0.wp.com/research.nccgroup.com/wp-content/uploads/2023/02/injects_zip_response.png?resize=1024%2C460&ssl=1)
![](https://i0.wp.com/research.nccgroup.com/wp-content/uploads/2023/02/injects_zip_content.png?resize=770%2C164&ssl=1)

Contents of the ZIP file with the injections

When the injection is shown and the victim enters his credentials, the malware uses JavaScript’s “Console.Log” function to send the credentials to the native Java code of the application. This function is reimplemented by the malware to send credentials to the C2 server, which is shown in the figure below.

![](https://i0.wp.com/research.nccgroup.com/wp-content/uploads/2023/02/consolelog_save_creds.png?resize=1024%2C414&ssl=1)

Decompiled code used to save the stolen credentials

---

文章来源: https://research.nccgroup.com/2023/02/17/threat-spotlight-hydra/
 如有侵权请联系:admin#unsafe.sh

© [unSafe.sh - 不安全](https://unsafe.sh) Powered By [PaperCache](https://github.com/code-scan/PaperCache)

* admin#unsafe.sh
* [安全马克](https://aq.mk)
* [星际黑客](https://xj.hk)
* [T00ls](https://t00ls.net)