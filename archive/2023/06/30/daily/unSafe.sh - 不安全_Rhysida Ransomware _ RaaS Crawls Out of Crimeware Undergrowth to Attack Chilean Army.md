---
title: Rhysida Ransomware | RaaS Crawls Out of Crimeware Undergrowth to Attack Chilean Army
url: https://buaq.net/go-170827.html
source: unSafe.sh - 不安全
date: 2023-06-30
fetch_date: 2025-10-04T11:44:53.908992
---

# Rhysida Ransomware | RaaS Crawls Out of Crimeware Undergrowth to Attack Chilean Army

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

![](https://8aqnet.cdn.bcebos.com/dd012eb360ea442d4ca5117f0fcd324e.jpg)

Rhysida Ransomware | RaaS Crawls Out of Crimeware Undergrowth to Attack Chilean Army

The Rhysida ransomware-as-a-service (RaaS) group has gone from a dubious newcomer to a fully-fledge
*2023-6-29 21:55:17
Author: [www.sentinelone.com(查看原文)](/jump-170827.htm)
阅读量:65
收藏*

---

The Rhysida ransomware-as-a-service ([RaaS](https://www.sentinelone.com/blog/raas-hacking-made-easy/)) group has gone from a dubious newcomer to a fully-fledged ransomware operation. Despite the developer’s partial implementation of some features, the group emerged onto the scene at the end of May with a high-profile attack against the Chilean Army, continuing the ongoing [trend](https://www.recordedfuture.com/latin-american-governments-targeted-by-ransomware) of ransomware groups targeting Latin American government institutions. On June 15, the group [leaked](https://www.bleepingcomputer.com/news/security/rhysida-ransomware-leaks-documents-stolen-from-chilean-army/) the files stolen from the Chilean Army.

In this post, we provide a high-level overview of Rhysida ransomware activity and present technical details of the malware payloads, along with hunting rules and IoCs to aid threat hunters and security teams.

![](https://www.sentinelone.com/wp-content/uploads/2023/06/Rhysida-Ransomware-RaaS-Crawls-Out-of-Crimeware-Undergrowth-to-Attack-Chilean-Army-2.jpg)

## Recent Attacks Attributed to Rhysida

On May 29 2023, the Chilean Army [reported](https://www.cronup.com/ejercito-de-chile-es-atacado-por-la-nueva-banda-de-ransomware-rhysida/) that it had been the target of a cyberattack affecting the organization’s internal network on Saturday, May 27. The attack was later attributed to Rhysida.

Strategically, the Rhysida group’s attack against the army of Chile distinguishes this newcomer from the sea of ransomware newcomers. It should be noted that Rhysida is an apparently independent ransomware group: SentinelOne has not observed any overt connections to existing ransomware operations. As such, any potential geopolitical ramifications from attacking Chile’s government are as yet unclear. This is not the first time a Chilean governmental organization has been compromised by a new ransomware family, as demonstrated by the ARCrypter [attack](https://blogs.blackberry.com/en/2022/11/arcrypter-ransomware-expands-its-operations-from-latin-america-to-the-world) in November 2022.

The attack was followed by the leaking of data belonging to the army on June 15th. Through the week of June 19 2023, Rhysida’s leaks page displayed an influx of further victims, including multiple organizations in each of the following sectors:

* Education
* Government
* Manufacturing
* Technology and Managed Service Providers (MSP)

Victims are distributed throughout Western Europe, North & South America, and Australia, loosely aligning the group’s targeting with many ransomware operations that avoid targeting countries in Eastern Europe and Central Asia’s Commonwealth of Independent States. There are no Asian organizations posted at this time.

## Operational Overview

The Rhysida ransomware group was first observed in May of 2023, following the emergence of their victim support chat portal, hosted via TOR (`.onion`).  The name “Rhyshida” refers to a specific genus of centipede.  This is also reflected in the ‘branding’ on their victim blog.

![The genus Rhysida and the Rhysida ransomware logo](https://www.sentinelone.com/wp-content/uploads/2023/06/rhysida_4.jpg)

The genus Rhysida and the Rhysida ransomware logo

An Apache configuration status page reveals that the web server hosting the portal was first set up in March 2023. The group has since migrated their blog to a more ‘hardened’ instance of nginx, and these server configuration details and status are no longer visible. This move may have been prompted by the original IP address being exposed across various underground forums and markets.

![Rhysida RaaS: Leakage of original blog IP address](https://www.sentinelone.com/wp-content/uploads/2023/06/rhysida_2.jpg)

Rhysida RaaS: Leakage of original blog IP address

Rhysida is a privately marketed RaaS without known forum presence. The group positions themselves as a “cybersecurity team” who are doing their victims a favor by targeting their systems and highlighting the potential ramifications of the involved security issues. The group threatens victims with public distribution of the exfiltrated data, bringing them in line with modern-day multi-extortion groups.

The groups website also serves as a portal for Rhysida-centric news and media coverage, as well as details on how to contact the group should journalists, recovery firms or “fans” be inclined to do so.

![Rhysida’s ‘communication portal’](https://www.sentinelone.com/wp-content/uploads/2023/06/rhysida_3.jpg)

Rhysida’s ‘communication portal’

Victims are instructed to contact the attackers via their TOR-based portal, utilizing their unique identifier provided in the ransom notes. Rhysida accepts payment in Bitcoin only, providing information on the purchase and use of BTC on the victim portal as well. Upon providing their unique ID to the payment portal, an additional form is presented that allows victims to provide additional information to the attackers, such as authentication and contact details.

![Rhysida portal’s additional details form](https://www.sentinelone.com/wp-content/uploads/2023/06/rhysida_7.jpg)

Rhysida portal’s additional details form

## Technical Details

Rhysida is a 64-bit Portable Executable (PE) Windows cryptographic ransomware application compiled using MINGW/GCC. In each sample analyzed, the application’s program name is set to `Rhysida-0.1`, suggesting the tool is in early stages of development.

A notable characteristic of the tool is its plain-text strings revealing registry modification commands.

## Rhysida Encryption & File Processing

For encryption, Rhysida uses a 4096-bit RSA key with the ChaCha20 algorithm. Its `main` function initializes the ransomware’s overall runtime, including encryption specifics. The `main` function contains several nested if-else conditions that handle arguments that specify different encryption implementations. The `processFileEnc` function contains code blocks for other encryption methods, including Rijndael, though the preceding functions are prefixed “test”.

`processFileEnc` calls `init_prng`, which initializes the encryption routine’s pseudo-random number generator that is passed to the `chacha_crypt` function.

The `processFileEnc` function contains code that lists files and parses the current file name. Following encryption, Rhysida appends the `.rhysida` extension to the name of encrypted files.

After the encryption details are established, Rhysida enumerates files and folders connected to the system. The `main` function ends by calling PowerShell to delete the binary after encryption has completed.

![Rhysida main function encryption checks](https://www.sentinelone.com/wp-content/uploads/2023/06/rhysida_5.jpg)

Rhysida *main* function encryption checks

Rhysida uses a file exclusion list to avoid encrypting certain files. This check occurs in the `isFileExcluded` function, which compares the current file extension against `exclude_extensions`, an array that contains the following excluded file extensions:

```
[ bat, bin,
  cab, cmd, com, cur,
  diagcab, diagcfg, diagpkg, drv, dll,
  exe,
  hlp, hta,
  ico, ini, iso,
  lnk,
  msi,
  ocx,
  ps1, psm1,
  scr, sys,
  Thumbs-db,
  url
]
```

This function initializes two variables, `exclude_i` as 0 and `exclude_c...