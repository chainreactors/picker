---
title: DarkGate reloaded via malvertising and SEO poisoning campaigns
url: https://buaq.net/go-175229.html
source: unSafe.sh - 不安全
date: 2023-08-24
fetch_date: 2025-10-04T11:58:52.787507
---

# DarkGate reloaded via malvertising and SEO poisoning campaigns

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

![](https://8aqnet.cdn.bcebos.com/f9c9c8c4b19011240594ae94f1db059a.jpg)

DarkGate reloaded via malvertising and SEO poisoning campaigns

In July 2023, we observed a malvertising campaign that lured potential
*2023-8-23 21:0:0
Author: [www.malwarebytes.com(查看原文)](/jump-175229.htm)
阅读量:25
收藏*

---

In July 2023, we observed a malvertising campaign that lured potential victims to a fraudulent site for a Windows IT management tool. Unlike previous similar attacks, the final payload was packaged differently and not immediately recognizable.

The decoy file came as an MSI installer containing an AutoIT script where the payload was obfuscated to avoid detection. Upon analysis and comparison, we determined that this sample was an updated version of DarkGate, a multi purpose malware toolkit first identified in 2018.

Since the malware's obfuscation and encryption features have been recently documented by other researchers, we will focus on two of its web delivery methods, namely the use of malicious ads and search engine poisoning.

The campaigns we observed coincide with an announcement from DarkGate's developer in June as well, boasting about the malware's new capabilities and limited customer seats.

## New DarkGate

In its debut back in 2018 and later in 2020, DarkGate (also known as [MehCrypter](https://decoded.avast.io/janrubin/complex-obfuscation-meh/)) was distributed via torrent sites and mostly focused on [European victims and Spanish users](https://decoded.avast.io/janrubin/meh-2-2/) in particular. The original [blog post](https://www.fortinet.com/blog/threat-research/enter-the-darkgate-new-cryptocurrency-mining-and-ransomware-campaign) from enSilo (now Fortinet) also notes that its author may have been using email to spread malicious attachments.

In June 2023, a threat actor going by the handle RastaFarEye posted an advertisement in the XSS underground forum about a project known as DarkGate. As [detailed](https://www.zerofox.com/blog/the-underground-economist-volume-3-issue-12/) by the ZeroFox Dark Ops intelligence team, the new version includes certain key features to evade detection while offering the expected credential stealing capabilities. The cost ($100K/year) and limited availability (10 customers) make DarkGate somewhat of an elusive toolkit.

[![Ad from DarkGate developper](https://www.malwarebytes.com/blog/threat-intelligence/2023/08/easset_upload_file49548_275963_e.png)](https://www.malwarebytes.com/blog/threat-intelligence/2023/08/easset_upload_file49548_275963_e.png)

Photo credit: [ZeroFox Dark Ops intelligence team](https://www.zerofox.com/blog/the-underground-economist-volume-3-issue-12/)

Two blog posts came out in early August, identifying new DarkGate attacks:

* Aon's Stroz Friedberg Incident Response Services [details](https://www.aon.com/cyber-solutions/aon_cyber_labs/darkgate-keylogger-analysis-masterofnone/) how they encountered a recent incident from a group similar to ScatteredSpider (UNC3944) that was using this new version of DarkGate.
* Researcher 0xToxin [wrote](https://0xtoxin.github.io/threat%20breakdown/DarkGate-Camapign-Analysis/) about phishing emails distributing a loader leading to DarkGate, with a complete technical analysis of the malware.

## Malvertising

While investigating malvertising campaigns, we observed the following Google ad on on July 13, 2023:

![Google Ad](https://www.malwarebytes.com/blog/threat-intelligence/2023/08/easset_upload_file6536_275963_e.png)

Advanced IP Scanner is a popular tool used by IT administrators. Victims who click on the ad are presented with a decoy site:

![Decoy page](https://www.malwarebytes.com/blog/threat-intelligence/2023/08/easset_upload_file32728_275963_e.png)

The downloaded file (*Advanced\_IP\_Scanner\_2.5.4594.1.msi*) is an installer that contains the legitimate Advanced IP Scanner binary but also some extra files that are unpacked in the %temp% folder upon execution:

![Payload](https://www.malwarebytes.com/blog/threat-intelligence/2023/08/easset_upload_file16684_275963_e.png)

We recognize the familiar use of AutoIT which was already present in the very early versions of DarkGate.

Note: The same threat actor was also serving malicious ads via Bing as [documented](https://medium.com/%40thrunter/bing-malvertisements-for-sysadmin-tool-deliver-darkgate-5b82f5e2a925) by Cyberuptive on August 8, 2023.

## SEO poisoning

SEO poisoning is an old technique used by various threat actors and scammers who attempt to game search engines' ranking system. Although it takes a little more time to roll out, it is an effective way to trick users into visiting malicious sites.

The following search result appeared on Google:

![](https://www.malwarebytes.com/blog/threat-intelligence/2023/08/easset_upload_file52601_275963_e.png)

The domain advancedscanner[.]link was created on 2023-07-28 and is used to redirect to the decoy page hosted at ipadvancedscanner[.]com. The downloaded file, IPAVSCAN\_win\_vers\_1.1.3.msi, also has the same AutoIt encrypted payload:

![](https://www.malwarebytes.com/blog/threat-intelligence/2023/08/easset_upload_file13495_275963_e.png)

## Anti-VM and other checks

We noticed that several of the newly registered domains associated with these campaigns had implemented advanced fingerprinting checks. We recently [documented](https://www.malwarebytes.com/blog/threat-intelligence/2023/08/malvertisers-up-the-game-against-researchers) this trend which could soon become the norm due to its ease of use.

Here's another lure, this time for Angry IP Scanner, with a domain (ipangry[.]com registered 2023-07-29):

![](https://www.malwarebytes.com/blog/threat-intelligence/2023/08/easset_upload_file10541_275963_e.png)

The payload, angry\_win\_0.47\_installer.msi and its AutoIt script:

![](https://www.malwarebytes.com/blog/threat-intelligence/2023/08/easset_upload_file72275_275963_e.png)

By using a combination of evasion techniques, the threat actors behind these campaigns are able to distribute DarkGate with a minimal system footprint. They are also diversifying their delivery techniques by leveraging malspam, malvertising and SEO poisoning.

Malwarebytes' anti-malware engine detects this malware as Backdoor.DarkGate and our web protection blocks its known command and control servers.

[Malwarebytes for Business](https://www.malwarebytes.com/business) (EDR) customers may also see the following alerts:

[![](https://www.malwarebytes.com/blog/threat-intelligence/2023/08/easset_upload_file27029_275963_e.png)](https://www.malwarebytes.com/blog/threat-intelligence/2023/08/easset_upload_file27029_275963_e.png)

## Indicators of Compromise

**Malvertising campaign**

```
top[.]advscan[.]com
```

**SEO poisoning campaign**

```
advancedscanner[.]link
ipadvancedscanner[.]com
185.224.137[.]54
185.11.61[.]65
```

**DarkGate samples**

```
e5ca3a8732a4645de632d0a6edfaf064bdd34a4824102fbc2b328a974350db8f
206042ec2b6bc377296c8b7901ce1a00c393df89e7c4cbbb1b8da1a86a153b67
9a7db0204847d26515ed249f9ed577220326f63a724a2e0fb6bb1d8cd33508a3
```

**DarkGate C2s**

```
80.66.88[.]145
107.181.161[.]200
```

## Additional resources

* [0xToxin's payload decryptor](https://gist.github.com/0xToxin/43e25700510ad3cc6268994b56c9a710)
* [RussianPanda's DarkGate config extractor](https://github.com/esThreatIntelligence/RussianPanda/blob/main/darkgate_config_extractor.py)

文章来源: https://www.malwarebytes.com/blog/threat-intelligence/2023/08/darkgate-reloaded-via-malvertising-campaigns
 如有侵权请联系:admin#unsafe.sh

© [unSafe.sh - 不安全](https://unsafe.sh) Powered By [PaperCache](https://github.com/code-scan/PaperCache)

* admin#unsafe.sh
* [安全马克](https://...