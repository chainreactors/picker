---
title: iOS Forensic Toolkit 8: Apple TV 3, 4, and 4K checkm8 Extraction Cheat Sheet
url: https://buaq.net/go-138300.html
source: unSafe.sh - 不安全
date: 2022-12-03
fetch_date: 2025-10-04T00:23:00.610420
---

# iOS Forensic Toolkit 8: Apple TV 3, 4, and 4K checkm8 Extraction Cheat Sheet

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

![](https://8aqnet.cdn.bcebos.com/61d0a3ef543181c15f2140631957785d.jpg)

iOS Forensic Toolkit 8: Apple TV 3, 4, and 4K checkm8 Extraction Cheat Sheet

Several generations of Apple TV devices have a boot
*2022-12-2 20:48:37
Author: [blog.elcomsoft.com(查看原文)](/jump-138300.htm)
阅读量:31
收藏*

---

![](https://secure.gravatar.com/avatar/2664b2a09a29ddba5fe47c73f061d98c?s=60&d=mm&r=x)

Several generations of Apple TV devices have a bootloader vulnerability that can be exploited with checkm8 to extract information from the device. The vulnerability exists in the Apple TV 3 (2012 and 2013), Apple TV HD (formerly Apple TV 4) 2015 and 2021, and Apple TV 4K (2017). Newer generations of Apple TV do not have the vulnerability. This guide lists the tools and steps required to fully extract a compatible Apple TV device.

[![](https://blog.elcomsoft.com/wp-content/uploads/2022/11/Image00001.jpg)](https://blog.elcomsoft.com/wp-content/uploads/2022/11/Image00001.jpg)

## Apple TV: cheat sheet

To extract data from an Apple TV box, follow these steps:

1. Launch iOS Forensic Toolkit 8.0 (Mac)
2. Connect the device to the computer with a USB cable (you will need a custom adapter for connecting the Apple TV 4K device)
3. Place the Apple TV into DFU (see below)
4. Run **./EIFT\_cmd boot**
5. Run **./EIFT\_cmd unlockdata -s**
6. Run **./EIFT\_cmd ramdisk keychain -o {filename}** to extract the keychain
7. Run **./EIFT\_cmd ramdisk tar -o {filename}** to pull the file system image
8. Run **./EIFT\_cmd ssh halt** to power off the device

## Placing Apple TV devices to DFU

Placing the three generations of Apple TV into DFU requires different steps. The Apple TV 3 can be placed into DFU with a matching IR remote, while the Apple TV HD (formerly Apple TV 4) require a Siri remote. Apple TV 4K requires an additional adapter to connect it to the computer (due to the lack of USB port). You will need yet another adapter to place the device to DFU, but once you have it, simply connecting the adapter to the box is enough to make it boot into DFU. Please refer to the following article for instructions: [How to Put Apple TV 3 (2012-2013), Apple TV 4/HD (2015) and Apple TV 4K (2017) into DFU](https://blog.elcomsoft.com/2022/10/how-to-put-apple-tv-3-2012-2013-apple-tv-hd-2015-and-apple-tv-4k-2017-into-dfu/)

## Apple TV extraction steps explained

Once you connect the Apple TV device to the computer, place the device into DFU as explained in the previous chapter. Then apply the exploit with iOS Forensic Toolkit by running the following command:

```
./EIFT_cmd boot
```

iOS Forensic Toolkit will detect the Apple TV in DFU mode and automatically apply the exploit. The toolkit detects the tvOS version installed on the device, and provides a download link to an Apple firmware image. If there are multiple potential matches, several download links will be displayed; we recommend taking the last link from the list. Download the file from the link, and drop it onto the console window, then press ENTER. **Alternatively**, you can simply paste the firmware download link instead. If you do that, the tool will only download parts of the firmware image that are required to apply the exploit and boot the Apple TV. It may take several attempts to place the device into DFU.

Notably, full IPSW images for Apple TV devices are scarce. Our tool can use OTA update images for the purpose of applying the exploit.

> *In many cases, the tvOS version will be detected automatically by EIFT during the first stage of the exploit. The detection is based on the detected iBoot version and device hardware. However, in some cases the iBoot version may correspond to several OS builds. If the wrong build is used, you will have an option to either repeat the process with a different version of firmware, or continue with the current firmware image (which works in many cases).*

**Please note**: applying the checkm8 exploit on the **first-generation** Apple TV 3 (A1427) requires a [Raspberry Pi Pico board](https://blog.elcomsoft.com/2022/05/checkm8-unlocking-and-imaging-the-iphone-4s/). The workflow is similar to the iPhone 4s. The newer Apple TV 3 (A1469) does not require an external microcontroller.

```
./EIFT_cmd ramdisk unlockdata -s
```

This command unlocks the data partition and mounts it read-only. Since the Apple TV does not have a passcode, you will not need to provide one.

```
./EIFT_cmd ramdisk keychain -o {filename}
```

This command extracts and decrypts the keychain. If no path is specified, it will be saved into the current folder. Note that the number of keychain records extracted can be limited compared to the content of an iPhone or iPad device. Since the Apple TV cannot have a passcode, the Apple TV devices cannot access any end-to-end encrypted data in iCloud, which includes the iCloud keychain. Any keychain records extracted from the Apple TV are going to be local, entered by the user on a specific device.

```
./EIFT_cmd ramdisk tar -o {filename}
```

This command images file system. The checksum (hash value) is calculated on the fly and displayed once the extraction is finished.

## Analyzing Apple TV data

After extracting the data, load the file system image and a copy of the keychain in the forensic tool of your choice. For the time being, few if any third-party forensic tools have been optimized to support TV-specific data sets. Elcomsoft Phone Viewer fully supports Apple TV images. Alternatively, you can manually analyze the file system image by unpacking the resulting .tar archive. Please refer to [Apple TV Forensics 03: Analysis](https://blog.elcomsoft.com/2019/09/apple-tv-forensics-03-analysis/) for details.

#### REFERENCES:

![](https://www.elcomsoft.com/images/bicons/eift.gif)

### Elcomsoft iOS Forensic Toolkit

Extract critical evidence from Apple iOS devices in real time. Gain access to phone secrets including passwords and encryption keys, and decrypt the file system image with or without the original passcode. Physical and logical acquisition options for all 64-bit devices running all versions of iOS.

[Elcomsoft iOS Forensic Toolkit official web page & downloads »](https://www.elcomsoft.com/eift.html)

文章来源: https://blog.elcomsoft.com/2022/12/ios-forensic-toolkit-8-apple-tv-3-4-and-4k-checkm8-extraction-cheat-sheet/
 如有侵权请联系:admin#unsafe.sh

© [unSafe.sh - 不安全](https://unsafe.sh) Powered By [PaperCache](https://github.com/code-scan/PaperCache)

* admin#unsafe.sh
* [安全马克](https://aq.mk)
* [星际黑客](https://xj.hk)
* [T00ls](https://t00ls.net)