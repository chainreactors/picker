---
title: JA4+ - Suite Of Network Fingerprinting Standards
url: https://buaq.net/go-241582.html
source: unSafe.sh - 不安全
date: 2024-05-26
fetch_date: 2025-10-06T16:49:03.925550
---

# JA4+ - Suite Of Network Fingerprinting Standards

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

![](https://8aqnet.cdn.bcebos.com/cc1c0f0f22c8f9de9c17cb5472711b56.jpg)

JA4+ - Suite Of Network Fingerprinting Standards

JA4+ is a suite of network Fingerprinting methods that are easy to use and easy to share. The
*2024-5-25 20:30:0
Author: [www.kitploit.com(查看原文)](/jump-241582.htm)
阅读量:16
收藏*

---

[![](https://blogger.googleusercontent.com/img/b/R29vZ2xl/AVvXsEjXdOCRL8eYvFXLYoFuppXXJ1tgugO_mjSVDv6D7wsV0BSe1X_hm2_auPD-_b2tKxs7URzM6DXjCFsCNEuP7mNT6nTXipE772sjrC4S5gbxUSaZFaK7YobWx6Uh2pIc7Y7LAjGN8HI6YJG5R4UdnTMH4M3CTjBeqQ5ZJzKaoEVVaXluXCFOKe1nYMUY_NFr/w640-h368/JA4.png)](https://blogger.googleusercontent.com/img/b/R29vZ2xl/AVvXsEjXdOCRL8eYvFXLYoFuppXXJ1tgugO_mjSVDv6D7wsV0BSe1X_hm2_auPD-_b2tKxs7URzM6DXjCFsCNEuP7mNT6nTXipE772sjrC4S5gbxUSaZFaK7YobWx6Uh2pIc7Y7LAjGN8HI6YJG5R4UdnTMH4M3CTjBeqQ5ZJzKaoEVVaXluXCFOKe1nYMUY_NFr/s2003/JA4.png)

JA4+ is a suite of network Fingerprinting methods that are easy to use and easy to share. These methods are both human and machine readable to facilitate more effective threat-hunting and analysis. The use-cases for these fingerprints include scanning for threat actors, malware detection, session hijacking prevention, [compliance](https://www.kitploit.com/search/label/Compliance "compliance") automation, location tracking, DDoS detection, grouping of threat actors, reverse shell detection, and many more.

Please read our blogs for details on how JA4+ works, why it works, and examples of what can be detected/prevented with it:

To understand how to read JA4+ fingerprints, see [Technical Details](https://github.com/FoxIO-LLC/ja4/blob/main/technical_details/README.md "Technical Details")

This repo includes JA4+ Python, Rust, Zeek and C, as a Wireshark plugin.

JA4/JA4+ support is being added to:
 [GreyNoise](https://www.greynoise.io/ "GreyNoise")
 [Hunt](https://hunt.io/ "Hunt")
 [Driftnet](https://driftnet.io/ "Driftnet")
 [DarkSail](https://darksail.ai "DarkSail")
 [Arkime](https://arkime.com/ "Arkime")
 [GoLang](https://github.com/driftnet-io/go-ja4x "GoLang") (JA4X)
 [Suricata](https://docs.suricata.io/en/latest/rules/ja-keywords.html#ja4-hash "Suricata")
 [Wireshark](https://github.com/FoxIO-LLC/ja4/tree/main/wireshark "Wireshark")
 [Zeek](https://github.com/FoxIO-LLC/ja4/tree/main/zeek "Zeek")
 [nzyme](https://www.nzyme.org/ "nzyme")
 [Netresec's CapLoader](https://www.netresec.com/?page=Blog&month=2023-11&post=CapLoader-1-9-6-Released "Netresec's CapLoader")
 [NetworkMiner](https://www.netresec.com/?page=<a href= "NetworkMiner")">Netresec's [NetworkMiner](https://www.kitploit.com/search/label/NetworkMiner "NetworkMiner")
 [NGINX](https://github.com/FoxIO-LLC/ja4-nginx-module "NGINX")
 [F5 BIG-IP](https://github.com/f5devcentral/f5-ja4 "F5 BIG-IP")
 [nfdump](https://github.com/phaag/nfdump "nfdump")
 [ntop's ntopng](https://github.com/ntop/ntopng "ntop's ntopng")
 [ntop's nDPI](https://github.com/ntop/nDPI "ntop's nDPI")
 [Team Cymru](https://www.team-cymru.com/ "Team Cymru")
 [NetQuest](https://netquestcorp.com/ "NetQuest")
 [Censys](https://censys.com/ "Censys")
 [Exploit.org's Netryx](https://github.com/OWASP/www-project-netryx "Exploit.org's Netryx")
 [cloudflare](https://developers.<a href= "cloudflare").com/bots/concepts/ja3-ja4-fingerprint/">Cloudflare
 [fastly](https://www.fastly.com/documentation/reference/vcl/variables/client-connection/tls-client-ja4/ "fastly")
 with more to be announced...

## Examples

| Application | JA4+ Fingerprints |
| --- | --- |
| Chrome | `JA4=t13d1516h2_8daaf6152771_02713d6af862` (TCP)   `JA4=q13d0312h3_55b375c5d22e_06cda9e17597` (QUIC)   `JA4=t13d1517h2_8daaf6152771_b0da82dd1658` (pre-shared key)   `JA4=t13d1517h2_8daaf6152771_b1ff8ab2d16f` (no key) |
| IcedID Malware Dropper | `JA4H=ge11cn020000_9ed1ff1f7b03_cd8dafe26982` |
| IcedID Malware | `JA4=t13d201100_2b729b4bf6f3_9e7b989ebec8`   `JA4S=t120300_c030_5e2616a54c73` |
| Sliver Malware | `JA4=t13d190900_9dc949149365_97f8aa674fd9`   `JA4S=t130200_1301_a56c5b993250`   `JA4X=000000000000_4f24da86fad6_bf0f0589fc03`   `JA4X=000000000000_7c32fa18c13e_bf0f0589fc03` |
| Cobalt Strike | `JA4H=ge11cn060000_4e59edc1297a_4da5efaf0cbd`   `JA4X=2166164053c1_2166164053c1_30d204a01551` |
| SoftEther VPN | `JA4=t13d880900_fcb5b95cb75a_b0d3b4ac2a14` (client)   `JA4S=t130200_1302_a56c5b993250`   `JA4X=d55f458d5a6c_d55f458d5a6c_0fc8c171b6ae` |
| Qakbot | `JA4X=2bab15409345_af684594efb4_000000000000` |
| Pikabot | `JA4X=1a59268f55e5_1a59268f55e5_795797892f9c` |
| Darkgate | `JA4H=po10nn060000_cdb958d032b0` |
| LummaC2 | `JA4H=po11nn050000_d253db9d024b` |
| Evilginx | `JA4=t13d191000_9dc949149365_e7c285222651` |
| Reverse SSH Shell | `JA4SSH=c76s76_c71s59_c0s70` |
| Windows 10 | `JA4T=64240_2-1-3-1-1-4_1460_8` |
| Epson Printer | `JA4TScan=28960_2-4-8-1-3_1460_3_1-4-8-16` |

For more, see [ja4plus-mapping.csv](https://github.com/FoxIO-LLC/ja4/blob/main/ja4plus-mapping.csv "ja4plus-mapping.csv")
 The mapping file is unlicensed and free to use. Feel free to do a pull request with any JA4+ data you find.

## Plugins

[Wireshark](https://github.com/FoxIO-LLC/ja4/tree/main/wireshark "Wireshark")
 [Zeek](https://github.com/FoxIO-LLC/ja4/tree/main/zeek "Zeek")
 [Arkime](https://arkime.com/settings#ja4plus "Arkime")

## Binaries

Recommended to have tshark version 4.0.6 or later for full functionality. See: https://pkgs.org/search/?q=tshark

Download the latest JA4 binaries from: [Releases](https://github.com/FoxIO-LLC/ja4/releases "Releases").

### JA4+ on Ubuntu

```
sudo apt install tshark
./ja4 [options] [pcap]
```

### JA4+ on Mac

1) Install Wireshark https://www.wireshark.org/download.html which will install tshark 2) Add tshark to $PATH

```
ln -s /Applications/Wireshark.app/Contents/MacOS/tshark /usr/local/bin/tshark
./ja4 [options] [pcap]
```

### JA4+ on Windows

1) Install Wireshark for Windows from https://www.wireshark.org/download.html which will install tshark.exe
 tshark.exe is at the location where wireshark is installed, for example: C:\Program Files\Wireshark\thsark.exe
 2) Add the location of tshark to your "PATH" environment variable in Windows.
 (System properties > Environment Variables... > Edit Path)
 3) Open cmd, navigate the ja4 folder

```
ja4 [options] [pcap]
```

## Database

An official JA4+ database of fingerprints, associated applications and recommended detection logic is in the process of being built.

In the meantime, see [ja4plus-mapping.csv](https://github.com/FoxIO-LLC/ja4/blob/main/ja4plus-mapping.csv "ja4plus-mapping.csv")

Feel free to do a pull request with any JA4+ data you find.

## JA4+ Details

JA4+ is a set of simple yet powerful network fingerprints for multiple protocols that are both human and machine readable, facilitating improved threat-hunting and security analysis. If you are unfamiliar with network fingerprinting, I encourage you to read my blogs releasing JA3 [here](https://medium.com/salesforce-engineering/tls-fingerprinting-with-ja3-and-ja3s-247362855967 "here"), JARM [here](https://medium.com/salesforce-engineering/easily-identify-malicious-servers-on-the-internet-with-jarm-e095edac525a "here"), and this excellent blog by Fastly on the [State of TLS Fingerprinting](https://www.fastly.com/blog/the-state-of-tls-fingerprinting-whats-working-what-isnt-and-whats-next "State of TLS Fingerprinting") which outlines the history of the aforementioned along with their problems. JA4+ brings dedicated support, keeping the methods up-to-date as the industry changes.

All JA4+ fingerprints have an a\_b\_c format, delimiting the different sections that make up the fingerprint. This allows for hunting and detection utilizing just ab or ac or c only. If one wanted t...