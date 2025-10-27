---
title: Crypto-inspired Magecart skimmer surfaces via digital crime haven
url: https://buaq.net/go-144858.html
source: unSafe.sh - 不安全
date: 2023-01-10
fetch_date: 2025-10-04T03:22:57.421255
---

# Crypto-inspired Magecart skimmer surfaces via digital crime haven

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

![](https://8aqnet.cdn.bcebos.com/16a460ac99b85a66d0b5eefe00527a7d.jpg)

Crypto-inspired Magecart skimmer surfaces via digital crime haven

This blog post was authored by Jérôme SeguraOnline criminals rarely re
*2023-1-9 19:0:0
Author: [www.malwarebytes.com(查看原文)](/jump-144858.htm)
阅读量:19
收藏*

---

*This blog post was authored by Jérôme Segura*

Online criminals rarely reinvent the wheel, especially when they don't have to. From ransomware to password stealers, there are a number of toolkits available for purchase on various underground markets that allow just about anyone to get a jumpstart.

During one of our crawls, we spotted a skimmer using the 'Mr.SNIFFA' framework that targets e-commerce sites and their customers. In recent years, this skimmer has adopted various obfuscation techniques as well as steganography to load its malicious code and exfiltrate stolen credit card data. While Magecart threat actors usually pick domain names after third-party libraries, or Google Analytics, in this case they went with a crypto-inspired theme which we had not seen before.

Digging further into the skimmer's infrastructure on Russian-based hosting provider DDoS-Guard, we came across a digital crime haven for cryptocurrency scams, Bitcoin mixers, malware distribution sites and much more. This blog post will cover the technical details of the skimmer and its crime-filled ecosystem.

## Overview

When looking for malicious code on the web, we tend to inspect HTML code, JavaScript dependencies as well as redirects. What makes some attacks interesting is how they will purposely avoid leaving obvious signs, try to only load one time or maybe dynamically in some unsuspecting format.

In this case, we saw an e-commerce website that was injected with a link to an external website named after American Entrepreneur and BTC supporter Michael J. Saylor (saylor2xbtc[.]com). We should note that the sites we found injected with this skimmer had nothing to do with cryptocurrencies themselves. However, interest in targeting this industry has been shown before and likely such attacks are still happening.

![](https://www.malwarebytes.com/blog/threat-intelligence/2023/01/easset_upload_file7008_253896_e.png)

As the skimmer code is dynamically unpacked in the DOM it will harvest card payment details and exfiltrate those in a similar fashion. In the next section, we will show exactly what happens during this process of data collection and exfiltration.

![](https://www.malwarebytes.com/blog/threat-intelligence/2023/01/easset_upload_file34155_253896_e.png)*Figure 2: Fiddler traffic capture*

## Technical details

### Mr.SNIFFA skimmer

Back in the spring of 2020, an [advert](https://twitter.com/campuscodi/status/1264471311327387648?s=20&t=SGC7gSgPxxFgiNMBbudnTA) for a new skimmer was posted to a criminal forum. The product, called mr.SNIFFA, claims to have code that cannot be seen using browser tools and works across different browsers. More importantly, the author offers free bug fixes and 24/7 support.

![](https://www.malwarebytes.com/blog/threat-intelligence/2023/01/easset_upload_file9702_253896_e.png)*Figure 3: Tweet about new product being advertised*

It seems some of those promises were true as a clever feature that hides the skimmer was [implemented](https://twitter.com/AffableKraut/status/1380022959272787970?s=20&t=fnMayBQqn6nGvVSxcAxZMQ) later on:

![](https://www.malwarebytes.com/blog/threat-intelligence/2023/01/easset_upload_file85686_253896_e.png)

*Figure 4: Update to mr.SNIFFA's code*

### Loader

Going back to this latest skimming attack, the first interesting piece is the JavaScript loaded from elon2xmusk[.]com. You have to scroll down halfway through it and after a number of tab entries, you can finally see some lightly obfuscated code.

![](https://www.malwarebytes.com/blog/threat-intelligence/2023/01/easset_upload_file39287_253896_e.gif)*Figure 5: Loader with leading and tailing white space*

This loader is quite important with what happens next because it is meant to load a special CSS file hosted at (2xdepp[.]com/stylesheet.css). In effect, all these different parts are connected and needed for the skimmer to get properly loaded.

### Core

The beginning of the file contains standard CSS content, in this case code to render fonts. But we can also notice a lot of white space beneath and a very long side scroll bar.

![](https://www.malwarebytes.com/blog/threat-intelligence/2023/01/easset_upload_file20340_253896_e.png)*Figure 6: Skimmer hiding inside CSS file*

Turning on special characters in the text editor program reveals over 88k lines containing spaces, tabs and new line feeds. That encoded whitespace data is converted into binary code via the original loader (elon2xmusk[.]com/jquery.min.js).

This particular technique was previously [documented](https://blog.sucuri.net/2020/11/css-js-steganography-in-fake-flash-player-update-malware.html) by Denis Sinegubko and Eric Brandel in a [thread](https://twitter.com/AffableKraut/status/1380022959272787970?s=20&t=Eit7kWPKptx9I161_64hRg) about some new features in the Mr.Sniffa toolkit.

![](https://www.malwarebytes.com/blog/threat-intelligence/2023/01/easset_upload_file79741_253896_e.png)*Figure 7: White space encoding characteristic of Mr.SNIFFA skimmer*

When decoding this piece of the code we end up with the [same skimmer](https://gist.github.com/krautface/e5444c1bb9880518db0f128416c911e6) produced by Eric Brandel.

![](https://www.malwarebytes.com/blog/threat-intelligence/2023/01/easset_upload_file70413_253896_e.png)*Figure 8: Decoded skimmer identical to previously reported Mr.SNIFFA*

### Exfiltration

At the checkout page, we see the payment form injected by the skimmer. Note the grammar mistake at the bottom "*please enter your card details and will charge you later*". This is a small detail, but those who pay attention to details will view it as a sign of a fraudulent form.

Stolen credit card data will be exfiltrated back to the attackers using the same special character encoding and sent as an image file.

![](https://www.malwarebytes.com/blog/threat-intelligence/2023/01/easset_upload_file74866_253896_e.png)*Figure 9: Data exfiltration via encoded image file*

## Infrastructure overview

### DDoS-Guard hosting

The 3 domains involved in this skimmer campaign were or are hosted on DDoS-Guard infrastructure, a Russian company that provides DDoS protection, CDN and hosting among some of its services. It has [hosted controversial websites](https://krebsonsecurity.com/2021/01/hamas-may-be-threat-to-8chan-qanon-online/) and according to a [blog post by Group-IB](https://www.group-ib.com/media-center/press-releases/ddos-guard-database/) documenting a leak and source code dump, "*DDoS-Guard also provides computing capacities and obstructs the identification of website owners of hundreds of shady resources that are engaged in illicit goods sale, gambling, and copyright infringements*".

![](https://www.malwarebytes.com/blog/threat-intelligence/2023/01/easset_upload_file92808_253896_e.png)*Figure 10: VirusTotal graph showing connections to DDos-Guard*

We previously [wrote](https://www.malwarebytes.com/blog/news/2019/07/no-mans-land-how-a-magecart-group-is-running-a-web-skimming-operation-from-a-war-zone) about Magecart groups relying on bulletproof infrastructure such as the hoster in Ukraine's Luhansk region. The obvious advantage is that takedowns are practically impossible and criminals can grow their infrastructure undisturbed.

### Immediate neighbors

Often times criminals will buy and sell across different services. With stolen credit cards, the path to mon...