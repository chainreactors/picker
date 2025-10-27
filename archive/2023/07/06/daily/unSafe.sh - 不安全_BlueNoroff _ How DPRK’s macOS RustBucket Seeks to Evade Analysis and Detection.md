---
title: BlueNoroff | How DPRK’s macOS RustBucket Seeks to Evade Analysis and Detection
url: https://buaq.net/go-171295.html
source: unSafe.sh - 不安全
date: 2023-07-06
fetch_date: 2025-10-04T11:51:23.195950
---

# BlueNoroff | How DPRK’s macOS RustBucket Seeks to Evade Analysis and Detection

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

![](https://8aqnet.cdn.bcebos.com/bb52646d19b1de351b3df87cd8ca46e5.jpg)

BlueNoroff | How DPRK’s macOS RustBucket Seeks to Evade Analysis and Detection

Back in April, researchers at JAMF detailed a sophisticated APT campaign targeting macOS users with
*2023-7-5 21:59:43
Author: [www.sentinelone.com(查看原文)](/jump-171295.htm)
阅读量:52
收藏*

---

Back in April, researchers at [JAMF](https://www.jamf.com/blog/bluenoroff-apt-targets-macos-rustbucket-malware/) detailed a sophisticated APT campaign targeting macOS users with multi-stage malware that culminated in a Rust backdoor capable of downloading and executing further malware on infected devices. ‘RustBucket’, as they labeled it, was attributed with strong confidence to the BlueNoroff APT, generally assumed to be a subsidiary of the wider DPRK cyber attack group known as [Lazarus](https://www.sentinelone.com/blog/lazarus-operation-interception-targets-macos-users-dreaming-of-jobs-in-crypto/).

In May, [ESET](https://twitter.com/ESETresearch/status/1656385173968019456?s=20) tweeted details of a second RustBucket variant targeting macOS users, followed in June by [Elastic](https://www.elastic.co/security-labs/DPRK-strikes-using-a-new-variant-of-rustbucket)’s discovery of a third variant that included previously unseen persistence capabilities.

RustBucket is noteworthy for the range and type of anti-evasion and anti-analysis measures seen in various stages of the malware. In this post, we review the multiple malware payloads used in the campaign and highlight the novel techniques RustBucket deploys to evade analysis and detection.

![](https://www.sentinelone.com/wp-content/uploads/2023/07/BlueNoroff-How-DPRKs-macOS-RustBucket-Seeks-to-Evade-Analysis-and-Detection-4.jpg)

## RustBucket Stage 1 | AppleScript Dropper

The attack begins with an Applet that masquerades as a PDF Viewer app. An Applet is simply a compiled [AppleScript](https://attack.mitre.org/techniques/T1059/002/) that is saved in a `.app` format. Unlike regular macOS applications, Applets typically lack a user interface and function merely as a convenient way for developers to distribute AppleScripts to users.

The threat actors chose not to save the script as [run-only](https://www.sentinelone.com/labs/fade-dead-adventures-in-reversing-malicious-run-only-applescripts/), which allows us to easily decompile the script with the built-on `osadecompile` tool (this is, effectively, what Apple’s GUI Script Editor runs in the background when viewing compiled scripts).

![Stage 1 executes three ‘do shell script’ commands to set up Stage 2](https://www.sentinelone.com/wp-content/uploads/2023/07/RustBucket_6.jpg)

Stage 1 executes three ‘do shell script’ commands to set up Stage 2

The script contains three [do shell script](https://developer.apple.com/library/archive/documentation/AppleScript/Conceptual/AppleScriptLangGuide/reference/ASLR_cmds.html#//apple_ref/doc/uid/TP40000983-CH216-SW40) commands, which serve to download and execute the next stage. In the variant described by JAMF, this was a barebones PDF viewer called  `Internal PDF Viewer`. We will forgo the details here as researchers have previously described this in detail.

Stage 1 writes the second stage to the `/Users/Shared/` folder, which does not require permissions and is accessible to malware without having to circumvent [TCC](https://www.sentinelone.com/labs/bypassing-macos-tcc-user-privacy-protections-by-accident-and-design/). The Stage 1 variant described by Elastic differs in that it writes the second stage as a hidden file to `/Users/Shared/.pd`.

The Stage 1 is easily the least sophisticated and easily detected part of the attack chain. The arguments of the `do shell script` commands should appear in the Mac’s unified logs and as output from command line tools such as the `ps` utility.

Success of the Stage 1 relies heavily on how well the threat actor employs social engineering tactics. In the case described by JAMF, the threat actors used an elaborate ruse of requiring an “internal” PDF reader to read a supposedly confidential or ‘protected’ document. Victims were required to execute the Stage 1 believing it to be capable of reading the PDF they had received. In fact, the Stage 1 was only a dropper, designed to protect the Stage 2 should anyone without the malicious PDF stumble on it.

## RustBucket Stage 2 | Payloads Written in Swift and Objective-C

We have found a number of different Stage 2 payloads, some written in Swift, some in Objective-C, and both compiled for Intel and Apple silicon architectures (see IoCs at the end of the post). The sizes and code artifacts of the Stage 2 samples vary. The universal ‘fat’ binaries vary between 160Kb and 210Kb.

![Samples of RustBucket Stage 2 vary in size](https://www.sentinelone.com/wp-content/uploads/2023/07/RustBucket_11.jpg)

Samples of RustBucket Stage 2 vary in size

Across the samples, various username strings can be found. Those we have observed in Stage 2 binaries so far include:

```
/Users/carey/
/Users/eric/
/Users/henrypatel/
/Users/hero/
```

Despite the differences in size and code artifacts, the Stage 2 payloads have in common the task of retrieving the Stage 3 from the command and control server. The Stage 2 payload requires a specially-crafted PDF to unlock the code which would lead to the downloading of the Stage 3 and provide an XOR’d key to decode the obfuscated C2 appended to the end of the PDF.

In some variants, this data is executed in the `downAndExecute` function as described by previous researchers; in others, we note that download of the next stage is performed in the aptly-named `down_update_run` function. This function itself varies across samples. In `b02922869e86ad06ff6380e8ec0be8db38f5002b`, for example, it runs a hardcoded command via `system()`.

![Stage 2 executes a shell command via the system() call to retrieve and run Stage 3](https://www.sentinelone.com/wp-content/uploads/2023/07/RustBucket_2.jpg)

Stage 2 executes a shell command via the *system()* call to retrieve and run Stage 3

However, the same function in other samples, (e.g., `d5971e8a3e8577dbb6f5a9aad248c842a33e7a26`) use NSURL APIs and entirely different logic.

![Code varies widely among samples, possibly suggesting different developers](https://www.sentinelone.com/wp-content/uploads/2023/07/RustBucket_12.jpg)

Code varies widely among samples, possibly suggesting different developers

Researchers at Elastic noted, further, that in one newer variant of Stage 2 written in Swift, the User-Agent string is all lowercase, whereas in the earlier Objective-C samples they are not.

![User-Agent string is subtly changed from the Objective-C to Swift versions of Stage 2](https://www.sentinelone.com/wp-content/uploads/2023/07/RustBucket_10.jpg)

User-Agent string is subtly changed from the Objective-C to Swift versions of Stage 2

Although user agent strings are not inherently case sensitive, if this was a deliberate change it is possible the threat actors are parsing the user agent strings on the server side to weed out unwanted calls to the c2.

In the most recent samples, the payload retrieved by Stage 2 is written to disk as“ErrorCheck.zip” in `_CS_DARWIN_USER_TEMP` (*aka* `$TMPDIR` typically at `/var/folders/…/../T/`) before being executed on the victim’s device.

## RustBucket Stage 3 | New Variant Drops Persistence LaunchAgent

The Stage 3 payload has so far been seen in two distinct variants:

* A: 182760cbe11fa0316abfb8b7b00b63f83159f5aa Stage3
* B: b74702c9b82f23ebf76805f1853bc72236bee57c ErrorCheck, System Update

Both variants are Mach-O universal binaries compiled from Rust source c...