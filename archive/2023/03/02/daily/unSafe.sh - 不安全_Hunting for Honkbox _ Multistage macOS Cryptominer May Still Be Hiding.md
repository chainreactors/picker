---
title: Hunting for Honkbox | Multistage macOS Cryptominer May Still Be Hiding
url: https://buaq.net/go-151595.html
source: unSafe.sh - 不安全
date: 2023-03-02
fetch_date: 2025-10-04T08:25:22.370579
---

# Hunting for Honkbox | Multistage macOS Cryptominer May Still Be Hiding

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

![](https://8aqnet.cdn.bcebos.com/6fa0a55d684849d1edf3c61a9d2cd8ed.jpg)

Hunting for Honkbox | Multistage macOS Cryptominer May Still Be Hiding

For the first time since November 2022, Apple last week released an update to its internal YARA-bas
*2023-3-1 22:52:0
Author: [www.sentinelone.com(查看原文)](/jump-151595.htm)
阅读量:41
收藏*

---

For the first time since November 2022, Apple last week released an update to its internal YARA-based malware file blocking service, [XProtect](https://support.apple.com/en-gb/guide/security/sec469d47bd8/web). Version 2166 added several new signatures for a threat it labels “Honkbox”, a cryptominer characterized by its leverage of XMRig and the “Invisible Internet Project” (*aka* I2P). Apple’s update comes on the back of new research from Jamf, which itself builds on earlier research from other sources.

Honkbox is an active threat with at least three variants and multiple components, some of which have not been previously documented. In this post, we describe Honkbox from a threat hunter’s point of view, providing a comprehensive breakdown of file characteristics, unique behavior and sample hashes that analysts and SOC teams can ingest to further aid their detection and response.

![](https://www.sentinelone.com/wp-content/uploads/2023/03/Hunting-for-Honkbox-Multistage-macOS-Cryptominer-May-Still-Be-Hiding-10.jpg)

## Honkbox Cryptominer Background

Apple updated XProtect last week in light of a [publication](https://www.jamf.com/blog/cryptojacking-macos-malware-discovered-by-jamf-threat-labs/) by researchers at JAMF describing a known but relatively undocumented macOS malware.

The new signatures departed from Apple’s recent practice and used human-readable malware names instead of their usual short base 16 strings. Apple’s YARA rules dubbed the malware ‘Honkbox’ (*aka* HONKBOX, but we’ll spare your eyes).

![XProtect update v2166 includes three signatures for Honkbox](https://www.sentinelone.com/wp-content/uploads/2023/03/Honkbox_-XProtect_2166-update.jpg)

XProtect update v2166 includes three signatures for Honkbox

Honkbox is a multistage cryptominer with three identified variants that make novel use of the I2P network. The malware has been distributed on the PirateBay in cracked apps for at least three years by user `wtfisthat34698409672`.  Many of the samples originate from trojanized versions of Logic Pro, but other popular creative applications have been abused including Adobe Zii, Photoshop, Illustrator and Ableton Live.

Honkbox has been circulating since at least 2019 and was likely first spotted in the wild by a [reddit user](https://www.reddit.com/r/MacOSBeta/comments/dq39s6/anyone_else_getting_comappleaccnetwork_requesting/) questioning why what appeared to be Apple software was tripping over the macOS firewall.

![](https://www.sentinelone.com/wp-content/uploads/2023/03/Honkbox-reddit.jpg)

As the research by Jamf and previously by [Trend Micro](https://www.trendmicro.com/en_us/research/22/b/latest-mac-coinminer-utilizes-open-source-binaries-and-the-i2p-network.html) on one of the earlier variants described, [com.apple.acc.network](https://www.virustotal.com/gui/file/b2e135c6c6c3851599b436c172f84a301ad9646f7f4a4ac6c268c135925cd538) is in fact a masquerade for the [I2P](https://geti2p.net/en/) command line tool.

![i2p used by macos malware honk box](https://www.sentinelone.com/wp-content/uploads/2023/03/Honkbox_-i2p.jpg)

Honkbox is the first known macOS malware to make use of I2P, which in effect functions as an alternative to the better known TOR/Onion router for hiding internet traffic and content. I2P describes itself as “a fully encrypted private network layer [that] protects your activity and location…No one can see where traffic is coming from, where it is going, or what the contents are.”

Traffic inside I2P doesn’t interact with the Internet directly and uses encrypted unidirectional tunnels between anonymous peers. It’s this tunnel traffic that tripped the macOS application firewall reported by the reddit user.

Despite being known to researchers for some time, the recent variants of Honkbox seem to have managed to fly under the radar with a number of samples having low reputation scores on VirusTotal. According to JAMF’s report, the samples they tested also evaded Apple’s built-in security mechanisms.

![Some Honkbox variants remain unknown to VirusTotal reputation engines](https://www.sentinelone.com/wp-content/uploads/2023/03/Honkbox_-samples-still-unrecognized-on-VT.jpg)

Some Honkbox variants remain unknown to VirusTotal reputation engines

That situation was corrected last week with the v2166 update to XProtect, which added three signatures Apple labeled “HONKBOX\_A”, “HONKBOX\_B”, and “HONKBOX\_C”.

## Honkbox | Distinctive File Characteristics

In [radare2](https://www.sentinelone.com/labs/6-pro-tricks-for-rapid-macos-malware-triage-with-radare2/) and with YARA installed, we can see if a file under analysis is known to XProtect with the following command:

```
!yara -w /Library/Apple/System/Library/CoreServices/XProtect.bundle/Contents/Resources/XProtect.yara `i~file~0[1]`
```

Taking a sample each of Honkbox\_A, \_B and \_C and using [custom power-ups](https://www.sentinelone.com/labs/the-art-and-science-of-macos-malware-hunting-with-radare2-leveraging-xrefs-yara-and-zignatures/) to invoke XProtect and search for IP address regexes, we can observe that the strings related to the `localhost` address are hard coded in the binary. However, the number of occurrences changes in each variant: four times in A, five in B and three in Honkbox\_C.

![honkbox variants ports](https://www.sentinelone.com/wp-content/uploads/2023/03/Honkbox_xp-and-ip-address-comparisons.jpg)

In addition, variants A and B share in common the use of port `4546`, whereas variants B and C share in common the use of ports `4545` and `4543`.

A typo that occurs only in variant B misspells the string “Continue process” as “Constinue process”.

![A characteristic seen in Honkbox_B variants is the typo “Constinue process”](https://www.sentinelone.com/wp-content/uploads/2023/03/Honkbokx-typo-v2.jpg)

A characteristic seen in Honkbox\_B variants is the typo “Constinue process”

Honkbox\_A also hard codes a number of I2P-related URLs. These are not seen in variants B and C.

![A characteristic of Honkbox_A is the hard coded “reseed” and other URLs](https://www.sentinelone.com/wp-content/uploads/2023/03/Honkbox_A-urls.jpg)

A characteristic of Honkbox\_A is the hard coded “reseed” and other URLs

Perhaps the most distinctive file characteristic of the newer Honkbox variants is the many 2044-byte `_cstrings` that together constitute the encrypted blob the malware uses to write and execute a working copy of the cracked software that the victim downloaded, along with other components of the malware itself.

The samples of Honkbox\_B we analyzed had upwards of 16,000 individual 2044 byte `_cstrings` embedded in the binaries. All of these were base64-encoded data, save for the last one, which is the plain text execution script passed to the shell via the `system()` command.

![Honkbox_B embeds thousands of individual 2044-byte strings](https://www.sentinelone.com/wp-content/uploads/2023/03/Honkbox_B-blob-and-script-strings.jpg)

Honkbox\_B embeds thousands of individual 2044-byte strings

Our sample of Honkbox\_C, on the other hand, contained a comparatively smaller number of these strings, just over 650.

![Honkbox_C has over 650 2044-byte base64-encoded _cstrings](https://www.sentinelone.com/wp-content/uploads/2023/03/Honkbox_C-2044b-cstrings.jpg)

Honkbox\_C has over 650 2044-byte base6...