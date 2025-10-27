---
title: Typhon Reborn With New Capabilities
url: https://buaq.net/go-135617.html
source: unSafe.sh - 不安全
date: 2022-11-15
fetch_date: 2025-10-03T22:42:30.895650
---

# Typhon Reborn With New Capabilities

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

![](https://8aqnet.cdn.bcebos.com/95d630b96484ffa5ed9fb93a4afd36a7.jpg)

Typhon Reborn With New Capabilities

Executive SummaryIn early Au
*2022-11-14 22:0:58
Author: [unit42.paloaltonetworks.com(查看原文)](/jump-135617.htm)
阅读量:27
收藏*

---

![Malware conceptual image, covering variants such as Typhon Reborn](https://unit42.paloaltonetworks.com/wp-content/uploads/2022/11/Malware-r3d2.png)

## **Executive Summary**

In early August 2022, Cyble Research Labs (a cybercrime monitoring service) uncovered a new crypto miner/stealer for hire that the malware author named Typhon Stealer. Shortly thereafter, they released an updated version called Typhon Reborn. Both versions have the ability to steal crypto wallets, monitor keystrokes in sensitive applications and evade antivirus products.

This new version has increased anti-analysis techniques and more malicious features. The threat actors have also improved their stealer and file grabber features.

Palo Alto Networks customers receive protections from malware families using similar anti-analysis techniques with [Cortex XDR](https://www.paloaltonetworks.com/cortex/cortex-xdr) or the [Next-Generation Firewall](https://www.paloaltonetworks.com/network-security/next-generation-firewall) with [cloud-delivered security services](https://www.paloaltonetworks.com/network-security/security-subscriptions) including [WildFire](https://www.paloaltonetworks.com/network-security/wildfire) and [Advanced Threat Prevention](https://www.paloaltonetworks.com/network-security/advanced-threat-prevention).

## Table of Contents

[Malware Sale and Advertisements](#post-125698-_qm9l80y0k299)

## Malware Sale and Advertisements

The threat actors behind Typhon Stealer were advertising their creation through an underground website as shown in Figure 1, while providing development and distribution updates through their existing Telegram channel.

![Website post showing the feature set for Typhon Stealer v.1.1.0 - July 17 update.](https://unit42.paloaltonetworks.com/wp-content/uploads/2022/11/word-image-18.png)

Figure 1. Screenshot of underground website for older version of Typhon Stealer.

## **Typhon Reborn: Stealer With New Features**

The original version of Typhon Stealer was updated and released with the new name of “Typhon Reborn.” This new version has increased anti-analysis techniques and it was modified to improve the stealer and file grabber features.

Figure 2 is a screenshot of the latest offerings, listed in a private Telegram channel.

![Telegram message listing new features and changes in Typhon Reborn.](https://unit42.paloaltonetworks.com/wp-content/uploads/2022/11/word-image-19.png)

Figure 2.Typhon Reborn’s new features as listed in a Telegram message.

In their Telegram channel, the malware author stated that the current price for this stealer is $100 for a lifetime subscription, as shown in Figure 3. They also have claimed that the final compressed Typhon Reborn payload size has been reduced to around 2.3 MB depending on the stealer's build configuration.

![Figure 3.Telegram post stating Typhon Reborn’s price.](https://unit42.paloaltonetworks.com/wp-content/uploads/2022/11/word-image-20.png)

Figure 3.Telegram post stating Typhon Reborn’s price.

In the Telegram post, we see that the author has added multiple new features and disabled a few old features (e.g. keylogger, clipper miner, etc.). These differences are visible by viewing the code blocks in Typhon 1.2 and the latest Reborn version. Figure 4 shows modules for block list and CryptoApps are present in the latest version.

![Module list for Typhon 1.2, to illustrate which have been added or removed between versions](https://unit42.paloaltonetworks.com/wp-content/uploads/2022/11/word-image-21.png)

Figure 4a. Typhon 1.2 code block showing available features. This can be compared to the Typhon Reborn code block in Figure 4b.

![Module list for Typhon Reborn, to illustrate which have been added or removed between versions](https://unit42.paloaltonetworks.com/wp-content/uploads/2022/11/word-image-22.png)

Figure 4b. Typhon Reborn code block showing available features. This can be compared to the Typhon 1.2 code block in Figure 4a.

## **Technical Analysis**

Typhon Reborn was released with multiple new features and configurable options. These new features include block listed usernames and countries, new message clients and a crypto-extension stealer for Google Chrome and Microsoft Edge. The author also removed a few existing features, including the keylogging ability as well as the clipboard stealing and crypto mining features.

Keylogging andcrypto mining code is typically easy to detect in dynamic analysis platforms. We speculate the removal of these features was to lower the chances of antivirus detections. The author stated in his release notes that the features that were removed, would be moved to their own projects in the future.

### **Anti-Analysis Techniques**

All of Typhon Reborn’s new anti-analysis checks, once triggered, run the cleverly named MeltSelf method, as shown in Figure 5. This method kills the threat’s process and deletes itself from the disk.

Typhon Reborn’s new anti-analysis techniques include the following:

* Checking for debugging arguments
* Detecting virtual machines
* Checking for debuggers
* Checking the size of the physical disk
* Checking for well known analysis processes (blocklisting)
* Checking for well known sandbox usernames
* Checking for victim country

![Anti-analysis checks that will run "MeltSelf," which terminates the threat's process and deletes itself from disk if it's triggered.](https://unit42.paloaltonetworks.com/wp-content/uploads/2022/11/word-image-23.png)

Figure 5. Anti-analysis functions.

#### Command Line Debugger

Typhon Reborn also checks the command line arguments included to launch the stealer. If the command line argument contains the –-debug keyword, the stealer will “MeltSelf,” as shown in Figure 6.

![Typhon Reborn checks the command line arguments included to launch the stealer, for the keyword –-debug.](https://unit42.paloaltonetworks.com/wp-content/uploads/2022/11/word-image-24.png)

Figure 6. Detection of command line debugging.

#### Disk Size for Various Operating Systems

While a disk size check is not a new evasion in general, it is a new feature added to Typhon Reborn (shown in Figure 7). It checks to ensure the disk space is of a certain size based on the operating system. If the current disk is below 30 GB for Windows versions 7 and 10, the stealer again runs “MeltSelf.”

|  |  |
| --- | --- |
| Windows 11 | 70 GB |
| Windows 10 | 30 GB |
| Windows 7 | 30 GB |

*Table 1. The stealer checks disk space based on the operating system.*

![Code snippet that checks to ensure the disk space is over a certain size based on the operating system.](https://unit42.paloaltonetworks.com/wp-content/uploads/2022/11/word-image-25.png)

Figure 7. Anti-analysis check based on disk size, on various operating systems.

#### Block List Processes

Typhon Reborn has included a larger list of potential analysis processes to check for. The process names included are all well known analysis tools, and if detected, Typhon Reborn will “MeltSelf”

|  |  |
| --- | --- |
| ollydbg processhacker  tcpview  autoruns  de4dot  ilspy  dnspy  autorunsc  filemon  procmon  regmon  idaq | idaq64 immunitydebugger  wireshark  dumpcap  hookexplorer  lordpe  petools  resourcehacker  x32dbg  x64dbg  fiddler |

*Table 2. Block list of processes.*

#### Block List of Usernames

Typhon Reborn has also added a username check to its anti-analysis techniques as shown in Figure 8. The usern...