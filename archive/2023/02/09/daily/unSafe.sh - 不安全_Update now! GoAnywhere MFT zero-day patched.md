---
title: Update now! GoAnywhere MFT zero-day patched
url: https://buaq.net/go-148584.html
source: unSafe.sh - 不安全
date: 2023-02-09
fetch_date: 2025-10-04T06:05:18.081540
---

# Update now! GoAnywhere MFT zero-day patched

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

![](https://8aqnet.cdn.bcebos.com/81ea16dcb2b1d00b8d9227850c4ddb82.jpg)

Update now! GoAnywhere MFT zero-day patched

An emergency patch (7.1.2) has been released for an actively exploited
*2023-2-8 18:0:0
Author: [www.malwarebytes.com(查看原文)](/jump-148584.htm)
阅读量:26
收藏*

---

An emergency patch (7.1.2) has been [released](https://www.bleepingcomputer.com/news/security/actively-exploited-goanywhere-mft-zero-day-gets-emergency-patch/) for an actively exploited zero-day vulnerability found in the GoAnywhere MFT administrator console.

GoAnywhere MFT, which stands for managed file transfer, is a software solution that allows businesses to manage and exchange files in a secure and compliant way. According to its website, it caters to [more than 3,000](https://www.goanywhere.com/about) organizations, [mostly](https://enlyft.com/tech/products/goanywhere-mft) those with more than 10,000 employees and 1B USD in revenue.

Some of these organizations are part of vital infrastructures; such as local governments, financial companies, healthcare organizations, energy firms; and technology manufacturers. A breach resulting from a GoAnywhere exploitation would lead to a serious supply chain attack.

Fortra (formerly HelpSystems), the company behind GoAnwhere MFT and [Cobalt Strike](https://www.malwarebytes.com/blog/news/2021/06/cobalt-strike-a-penetration-testing-tool-popular-among-criminals), released the patch to finally secure the vulnerability, which allows an attacker to perform unauthenticated remote code execution during instances when the administrator console is made accessible in the public internet. Florian Hauser ([@frycos](https://twitter.com/frycos)), IT security consultant at Code White, released a [proof-of-concept (PoC) exploit](https://www.bleepingcomputer.com/news/security/exploit-released-for-actively-exploited-goanywhere-mft-zero-day/) for the vulnerability on Monday.

Brian Krebs of KrebsOnSecurity graciously [shared](https://cyberplace.social/%40briankrebs%40infosec.exchange/109795711251567498) what Fortra said in its advisory, which can only be accessed by creating a free account:

> "The attack vector of this exploit requires access to the administrative console of the application, which in most cases is accessible only from within a private company network, through VPN, or by allow-listed IP addresses (when running in cloud environments, such as Azure or AWS)." However, a scan using Shodan, the search engine for internet-connected devices, revealed [more or less a thousand instances](https://beta.shodan.io/search?query=http.favicon.hash%3A1484947000) of exposed GoAnywhere admin panels, the majority of which were found in Europe and the US.

![](https://www.malwarebytes.com/blog/news/2023/02/easset_upload_file52763_258910_e.png)

Fortra urges clients to apply emergency patch 7.1.2 as quickly as possible. If for some reason you can't, Fortra says you should follow the mitigation steps it put out days before, which involves implementing some access control wherein the administrator console interface should only be accessed from trusted sources, or disabling the licensing service altogether. There is also a technical mitigation configuration shared in the [advisory](https://www.bleepingcomputer.com/news/security/exploit-released-for-actively-exploited-goanywhere-mft-zero-day/).

Furthermore, clients must take the following additional steps after applying the mitigation steps if they suspect that attackers have already compromised their systems:

* Rotate the master encryption key.
* Reset credentials.
* Review audit logs and delete suspicious admin or user accounts.
* Contact Fortra support by going to its [portal](https://my.goanywhere.com/), emailing technicians at [[email protected]](https://www.malwarebytes.com/cdn-cgi/l/email-protection#dabdb5bbb4a3adb2bfa8bff4a9afaaaab5a8ae9ab2bfb6aaa9a3a9aebfb7a9f4b9b5b7), or phoning them up at 402-944-4242.

---

文章来源: https://www.malwarebytes.com/blog/news/2023/02/update-now-goanywhere-mft-zero-day-patched
 如有侵权请联系:admin#unsafe.sh

© [unSafe.sh - 不安全](https://unsafe.sh) Powered By [PaperCache](https://github.com/code-scan/PaperCache)

* admin#unsafe.sh
* [安全马克](https://aq.mk)
* [星际黑客](https://xj.hk)
* [T00ls](https://t00ls.net)