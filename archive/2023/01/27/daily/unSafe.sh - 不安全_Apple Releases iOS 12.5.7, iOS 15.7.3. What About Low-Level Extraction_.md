---
title: Apple Releases iOS 12.5.7, iOS 15.7.3. What About Low-Level Extraction?
url: https://buaq.net/go-146763.html
source: unSafe.sh - 不安全
date: 2023-01-27
fetch_date: 2025-10-04T04:56:43.283686
---

# Apple Releases iOS 12.5.7, iOS 15.7.3. What About Low-Level Extraction?

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

![](https://8aqnet.cdn.bcebos.com/d1d26112ac30f1607c0c8dc014cae92a.jpg)

Apple Releases iOS 12.5.7, iOS 15.7.3. What About Low-Level Extraction?

Apple is known for a very long time they support th
*2023-1-26 19:14:1
Author: [blog.elcomsoft.com(查看原文)](/jump-146763.htm)
阅读量:23
收藏*

---

![](https://secure.gravatar.com/avatar/2664b2a09a29ddba5fe47c73f061d98c?s=60&d=mm&r=x)

Apple is known for a very long time they support their devices. On January 23, 2023, alongside with iOS 16.3 the company rolled out security patches to older devices, releasing iOS 12.5.7, iOS 15.7.3 and iPadOS 15.7.3. iOS 12 was the last major version of iOS supported on Apple A7, A8, and A8X devices, which includes the iPhone 5s and iPhone 6 and 6 Plus generations along with several iPad models. We tested low-level extraction with these security-patched builds, and made several discoveries.

## Low-level extraction methods

Low-level extraction can be done differently. For older hardware, which includes all models affected by the current security releases, the checkm8 extraction delivers the [cleanest results](https://blog.elcomsoft.com/2022/11/checkm8-extraction-cheat-sheet-iphone-and-ipad-devices/). our solution is unrivaled in providing truly forensically sound extractions for all compatible devices, which include a number of iPhone, iPad, Apple Watch and Apple TV devices. checkm8 extractions are great, but they aren’t compatible with newer devices. To deliver low-level extraction for newer iPhones and iPads, we developed an in-house extraction agent that comes as close to being forensically sound as possible. This method is highly dependent on kernel exploits, which are extremely difficult to implement. This is why low-level extraction almost never comes to the current, up-to-date and fully patched versions of iOS. For newer models starting with iPhone Xr/Xs, using the extraction agent is the only way to extract the file system and decrypt the keychain.

### iOS 12.5.7: low-level extraction available

iOS 12.5.7 targets devices based on the Apple A7, A8, and A8X chip sets, which includes the iPhone 5s, iPhone 6, iPhone 6 Plus, iPad Air, iPad mini 2, iPad mini 3, and iPod touch (6th generation). The official [release notes](https://support.apple.com/en-us/HT213597) only mention a single CVE-2022-42856, which relates to a vulnerability in WebKit. Both the **checkm8** and **extraction agent** methods are available for these devices.

**Agent: passed.** We tested a device running iOS 12.5.7 with iOS Forensic Toolkit 8, and discovered that our extraction agent is fully compatible the freshly patched iOS release with full file system extraction and keychain decryption support. This means that Apple did not fix the vulnerability that allows our extraction agent to escalate privileges and escape sandbox.

**checkm8: passed.** We have also tested checkm8 extraction of a device running iOS 12.5.7 with iOS Forensic Toolkit 8; the test passed. Full file system extraction and keychain decryption are both available.

[![](https://blog.elcomsoft.com/wp-content/uploads/2023/01/ios1257-agent.png)](https://blog.elcomsoft.com/wp-content/uploads/2023/01/ios1257-agent.png)

### iOS 15.7.3: checkm8 extraction

iOS 15.7.3 and iPadOS 15.7.3 target devices based on the A9/A9X and A10/A10X chip sets, which includes the iPhone 6s and iPhone 6s Plus, iPhone 7 and iPhone 7 Plus, iPhone SE (1st generation), iPad Air 2, iPad mini (4th generation), and iPod touch (7th generation). The list of security patches is longer, and we still not have a way of privilege escalation. However, all device models that received the security patch are built with chips affected by the bootloader vulnerability that can be exploited with **checkm8**.

**checkm8: passed.** We have tested checkm8 extraction of iOS 15.7.3 with iOS Forensic Toolkit. Full file system extraction and keychain decryption are both available.

There is a small note: since the current build of iOS Forensic Toolkit was released before iOS 15.7.3, it can neither detect the OS version nor display the correct download link for the iOS 15.7.3 image. As a reminder, our checkm8 extraction requires downloading parts of Apple original firmware in order to boot the device. We’ll add the download link with the next update; meanwhile, you can find the matching .ipsw image on Apple Web site and simply pass the URL as an argument when prompted. Alternatively, you can download the required .ipsw file and use the downloaded firmware image instead.

[![](https://blog.elcomsoft.com/wp-content/uploads/2023/01/1-eift-boot.png)](https://blog.elcomsoft.com/wp-content/uploads/2023/01/1-eift-boot.png) [![](https://blog.elcomsoft.com/wp-content/uploads/2023/01/2-eift-unlock.png)](https://blog.elcomsoft.com/wp-content/uploads/2023/01/2-eift-unlock.png) [![](https://blog.elcomsoft.com/wp-content/uploads/2023/01/3-eift-keychain.png)](https://blog.elcomsoft.com/wp-content/uploads/2023/01/3-eift-keychain.png)

We strived to make our checkm8 extraction process to be as robust as possible. The extraction process survives through minor iOS updates such as iOS/iPadOS 15.7.3, and supports most public and developer pre-release versions of iOS/iPadOS.

## New compatibility matrix

The updated compatibility matrix is published below. We added a note on iOS 12.5.7 agent-based and checkm8 extraction support. checkm8 extraction is supported for iOS/iPadOS 15.7.3, but the extraction agent is not.

[![](https://blog.elcomsoft.com/wp-content/uploads/2023/01/compatibility-1.png)](https://blog.elcomsoft.com/wp-content/uploads/2023/01/compatibility-1.png)

#### REFERENCES:

![](https://www.elcomsoft.com/images/bicons/eift.gif)

### Elcomsoft iOS Forensic Toolkit

Extract critical evidence from Apple iOS devices in real time. Gain access to phone secrets including passwords and encryption keys, and decrypt the file system image with or without the original passcode. Physical and logical acquisition options for all 64-bit devices running all versions of iOS.

[Elcomsoft iOS Forensic Toolkit official web page & downloads »](https://www.elcomsoft.com/eift.html)

文章来源: https://blog.elcomsoft.com/2023/01/apple-releases-ios-12-5-7-ios-15-7-3-what-about-low-level-extraction/
 如有侵权请联系:admin#unsafe.sh

© [unSafe.sh - 不安全](https://unsafe.sh) Powered By [PaperCache](https://github.com/code-scan/PaperCache)

* admin#unsafe.sh
* [安全马克](https://aq.mk)
* [星际黑客](https://xj.hk)
* [T00ls](https://t00ls.net)