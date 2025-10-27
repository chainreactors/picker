---
title: Emotet Returns... Again
url: https://buaq.net/go-134928.html
source: unSafe.sh - 不安全
date: 2022-11-10
fetch_date: 2025-10-03T22:12:51.279436
---

# Emotet Returns... Again

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

![](https://8aqnet.cdn.bcebos.com/8b76e72149e13df2259672ebaa803cf8.jpg)

Emotet Returns... Again

Emotet is a long established piece of malware that was originally developed as a ba
*2022-11-9 21:47:40
Author: [www.forcepoint.com(查看原文)](/jump-134928.htm)
阅读量:17
收藏*

---

Emotet is a long established piece of malware that was originally developed as a banking Trojan. Since it’s invention, it has expanded it’s core targets beyond just financial institutions to enterprises, SMEs as well as government organisations, agencies and private individuals. Emotet has become so adept at bypassing detection technology, it’s now widely used by ransomware groups as “Malware as a service”. In late 2022, Emotet has emerged from a 4-month hiatus with a whole new campaign.

## **What you need to know**

Forcepoint [**blogged about Emotet**](https://www.forcepoint.com/blog/x-labs/thanks-giving-emotet) back in 2018, and since then, the core method of infection hasn’t changed much. Emotet relies upon loose or unconfigured Macro policies within organisations to allow its Macros to run.

Back in 2018, the attack vector was a Word 97 .DOC file, launching a Macro, which in turn launches a PowerShell script and finally launches a shell payload.

Over the course of the next four years, the core attack vector of Emotet hasn’t changed much. Emotet in late 2022 still uses Macros as it’s central infiltration mechanism, but thanks to some enhanced security features, it relies upon some social engineering to coerce the user into dropping Macros into a trusted folder where it [**can hen be executed**](https://www.bleepingcomputer.com/news/security/emotet-botnet-starts-blasting-malware-again-after-4-month-break/):

![Malicious Emotet Excel Document - Source - Bleeping Computer](https://www.forcepoint.com/sites/default/files/malicious-emotet-bleeping-computer.jpg)

By moving a file to a trusted location, it **[bypasses all Macros-related policies](https://learn.microsoft.com/en-us/deployoffice/security/trusted-locations)** that are configured. So whilst this attack involves more social engineering, the attack vector creates a huge problem for enterprises. Most organisations have a mature Macros policy, either they are disabled on all documents or only enabled for a subset of users. However, many of these organisations do not know about trusted locations at all, or if they do, they do not understand the potential implications of leaving the trusted location policy as default.

## **So, what can be done about it?**

The obvious answer is for immediate protection would be to configure a trusted locations policy, whether that is a limited location employees cannot configure or disabled completely. However, this does not solve the underlying issue, which as we have seen with the longevity of the Emotet Trojan, Macros are a huge attack vector for any organisation. Rather than configuring policy and waiting for the next bypass/attack vector to come along, look for a permanent solution that will simply clean all documents as they enter the organisation.

[Forcepoint’s Zero Trust CDR](https://www.forcepoint.com/product/zero-trust-cdr) can plug in on the email flow and clean documents to make sure that no document contains Macros or any other document based malware, whilst still ensuring that “power users” who may need to receive those Macros can do so. Forcepoint's Zero Trust CDR ensures the perfect security whilst not compromising upon user experience.

Read our **[whitepaper on Zero Trust CDR](https://www.forcepoint.com/resources/whitepapers/enhance-your-email-security-zero-trust-cdr)** for Mail solution for more.

![](https://www.forcepoint.com/sites/default/files/styles/profile_list/public/aaron_mulgrew.jpg?itok=gyYQHI0i)

## [Aaron Mulgrew](https://www.forcepoint.com/company/biographies/aaron-mulgrew)

Aaron works with central government departments in the UK and abroad to secure their systems, as well as working alongside critical national infrastructure providers to make sure they aren’t an easy route to compromise. With a specialism in cryptocurrency...

[Read more articles by Aaron Mulgrew](https://www.forcepoint.com/company/biographies/aaron-mulgrew "More articles from Aaron Mulgrew")

Forcepoint is the leading user and data protection cybersecurity company, entrusted to safeguard organizations while driving digital transformation and growth. Our solutions adapt in real-time to how people interact with data, providing secure access while enabling employees to create value.

文章来源: https://www.forcepoint.com/blog/x-labs/emotet-returns-again
 如有侵权请联系:admin#unsafe.sh

© [unSafe.sh - 不安全](https://unsafe.sh) Powered By [PaperCache](https://github.com/code-scan/PaperCache)

* admin#unsafe.sh
* [安全马克](https://aq.mk)
* [星际黑客](https://xj.hk)
* [T00ls](https://t00ls.net)