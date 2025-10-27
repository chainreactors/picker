---
title: iOS Forensic Toolkit 8 Apple Watch S3 checkm8 Extraction Cheat Sheet
url: https://buaq.net/go-137787.html
source: unSafe.sh - 不安全
date: 2022-11-30
fetch_date: 2025-10-04T00:02:55.420418
---

# iOS Forensic Toolkit 8 Apple Watch S3 checkm8 Extraction Cheat Sheet

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

![](https://8aqnet.cdn.bcebos.com/1f39f902e539e084efad03b6cea9e599.jpg)

iOS Forensic Toolkit 8 Apple Watch S3 checkm8 Extraction Cheat Sheet

checkm8 is the only extraction method available for
*2022-11-29 23:9:3
Author: [blog.elcomsoft.com(查看原文)](/jump-137787.htm)
阅读量:22
收藏*

---

![](https://secure.gravatar.com/avatar/2664b2a09a29ddba5fe47c73f061d98c?s=60&d=mm&r=x)

checkm8 is the only extraction method available for the Apple Watch S3 allowing full access to essential evidence stored in the device. In this guide, we will talk about connecting the Apple Watch S3 to the computer, placing the watch into DFU mode, applying the checkm8 exploit and extracting the file system from the device with iOS Forensic Toolkit 8.0.

The Apple Watch Series 3 has set a record as the longest smartwatch that Apple kept around. Initially introduced in September 2017, this model remained on sale for five years until it was finally discontinued in 2022. This model is the last Apple Watch device compatible with the checkm8 exploit.

Please note: steps listed in this guide are provided for the release version of iOS Forensic Toolkit 8.0. The older article [checkm8 Extraction of Apple Watch Series 3](https://blog.elcomsoft.com/2022/02/checkm8-extraction-of-apple-watch-series-3/) is based on the fifth beta version of the tool, and has slightly outdated instructions. While the old instructions still work, please refer to this publication for all future Apple Watch extractions.

## Before you begin

Unlike other Apple devices, the Apple Watch does not have a built-in USB port. The hidden diagnostic pins are available and can be used to attach the watch to the computer with an appropriate adapter. Make sure you have everything handy before you begin.

1. **A Mac computer**. You will need a Mac to install the exploit and perform the extraction. We support both Intel and M1-based Macs with a universal build of iOS Forensic Toolkit. At this time, Windows is not supported.
2. **iOS Forensic Toolkit 8.0 for Mac**. Currently, EIFT 8.0 is only available for Mac.
3. **Apple Watch Series 3**. The watch must be functional enough to be placed into DFU mode.
4. Apple Watch **passcode** must be known or empty. Otherwise, limited BFU extraction may be available, but very little information can be obtained this way.
5. A compatible **USB adapter** to connect the watch to the computer.
6. You must be able to download the official Apple firmware (download link will be provided during the extraction) that matches watchOS version installed on the device.

**Note**: while Apple had partially patched the vulnerability in iOS 14 and 15, watchOS 7 and 8, which are based on those versions of iOS, did not receive the same treatment. As a result, you will not have to remove the watch screen lock passcode in order to apply the exploit. We are not quite sure what’s going on here, but it does appear the patch was simply forgotten.

## USB adapter

There are several types of Apple Watch adapters on the market that can be easily sourced from multiple vendors. We tested several adapters, and currently recommend one named S-Dock:

[![](https://blog.elcomsoft.com/wp-content/uploads/2022/02/aw1-413x550.jpg)](https://blog.elcomsoft.com/wp-content/uploads/2022/02/aw1-413x550.jpg)

Note that some adapters may not support DFU mode. We recommend one of the adapters we tested in [Apple Watch Forensics: The Adapters](https://blog.elcomsoft.com/2021/08/apple-watch-forensics-the-adapters/) and [Apple Watch Forensics: More on Adapters](https://blog.elcomsoft.com/2021/11/apple-watch-forensics-more-on-adapters/), which includes models by S-BUS, MagicAWRT and iBUS.

## Cheat sheet: checkm8 extraction of Apple Watch 3

When extracting the Apple Watch, follow these steps:

1. Launch iOS Forensic Toolkit 8.0
2. Connect the Apple Watch 3 to the computer via a USB adapter (in a powered-off state)
3. Run ./EIFT\_cmd boot -w
4. Place the Watch into DFU
5. iOS Forensic Toolkit will detect the watch and apply the exploit
6. Run ./EIFT\_cmd ramdisk loadnfcd
7. Run ./EIFT\_cmd ramdisk unlockdata -s (enter passcode when prompted, or ENTER if you don’t know the passcode)
8. Run ./EIFT\_cmd ramdisk keychain -o {filename} to extract the keychain
9. Run ./EIFT\_cmd ramdisk tar -o {filename} to extract the file system
10. Run ./EIFT\_cmd ssh halt to power off the Apple Watch

## Step by step instructions

Launch iOS Forensic Toolkit, then connect the Apple Watch to the computer by using a commercially available adapter. At this time, the watch must be powered down.

On the computer, launch EIFT in wait mode:

```
./EIFT_cmd boot -w
```

Then, **place the watch into DFU**. To do that, press and hold both the Digital Crown and the Side button for ten seconds, then release the Side button while still holding the Digital Crown for 10 more seconds. There will be no indication on the watch; the display should remain black. If you see an Apple logo, the timings were wrong, and you’ll have to repeat the procedure.

Once the watch is in DFU mode, the tool code detects the OS version installed on the watch, and provides a download link. If there are multiple potential matches, several download links will be displayed; we recommend taking the last link from the list. Download the file from the link, and drop it onto the console window, then press ENTER. **Alternatively**, you can simply paste the firmware download link instead. If you do that, the tool will only download parts of the firmware image that are required to apply the exploit and boot the watch. It may take several attempts to place the device into DFU.

Notably, full IPSW images for Apple Watch devices are scarce. Our tool can use OTA update images for the purpose of applying the exploit.

Once the exploit is applied, the watch screen will display the “**Booting**” message.

> *In many cases, the watchOS version will be detected automatically by EIFT during the first stage of the exploit. The detection is based on the detected iBoot version and device hardware. However, in some cases the iBoot version may correspond to several OS builds. If the wrong build is used, you will have an option to either repeat the process with a different version of firmware, or continue with the current firmware image (which works in many cases).*

If the process was successful, you will see a confirmation.

The Watch will display the following screen:

```
./EIFT_cmd ramdisk unlockdata -s
```

This command unlocks the data partition and mounts it read-only. You may be prompted for the passcode; enter the passcode if you know it, or press ENTER to skip (limited DFU extraction will be performed in that case).

If you enter the wrong passcode, an error will be displayed. With correct passcode, the volume is fully unlocked and you can proceed with data (keychain and file system) extraction). If you don’t know the passcode, press ENTER on the screen below. In this case, a very limited BFU extraction will be performed.1

```
./EIFT_cmd ramdisk keychain -o {filename}
```

This command extracts and decrypts the keychain. If no path is specified, it will be saved into the current folder.

```
./EIFT_cmd ramdisk tar -o {filename}
```

This command images file system. The checksum (hash value) is calculated on the fly and displayed once the extraction is finished.

The SoC and USB controller in the Apple Watch are significantly slower than their iPhone counterparts, which results in comparatively slow extraction speeds of approximately 3 MB/s.

**Limited BFU extraction**

If you do not know the screen lock passcode, just press ENTER when prompted. Despite “Device is not un...