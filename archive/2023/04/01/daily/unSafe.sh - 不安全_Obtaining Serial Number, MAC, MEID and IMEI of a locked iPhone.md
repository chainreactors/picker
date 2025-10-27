---
title: Obtaining Serial Number, MAC, MEID and IMEI of a locked iPhone
url: https://buaq.net/go-156328.html
source: unSafe.sh - 不安全
date: 2023-04-01
fetch_date: 2025-10-04T11:19:30.180918
---

# Obtaining Serial Number, MAC, MEID and IMEI of a locked iPhone

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

![](https://8aqnet.cdn.bcebos.com/ba75205967783169e68aa16c0d7ee4d5.jpg)

Obtaining Serial Number, MAC, MEID and IMEI of a locked iPhone

Obtaining information from a locked iPhone can be c
*2023-3-31 20:16:45
Author: [blog.elcomsoft.com(查看原文)](/jump-156328.htm)
阅读量:76
收藏*

---

![](https://secure.gravatar.com/avatar/2664b2a09a29ddba5fe47c73f061d98c?s=60&d=mm&r=x)

Obtaining information from a locked iPhone can be challenging, particularly when the device is passcode-protected. However, four critical pieces of information that can aid forensic analysis are the device’s International Mobile Equipment Identity (IMEI), Mobile Equipment IDentifier (MEID), MAC address of the device’s Wi-Fi adapter, and its serial number. These unique identifiers can provide valuable insights into a device’s history, including its manufacture date, hardware specifications, and carrier information.

In forensic investigations, accessing this information can be crucial for tracing a device’s ownership, determining if it has been stolen or involved in criminal activity, and retrieving important data for legal or investigative purposes. This article will explore the various methods available to forensic investigators for obtaining the device’s MAC address, MEID, IMEI, and serial number information from a locked iPhone.

## Method 1: iPhone Diagnostic Mode

The iPhone diagnostic mode reveals essential information about the device such as its serial number, IMEI, and MEID numbers. Additional information such as the exact model identification, iOS version and MAC address of the device’s Wi-Fi adapter is accessible with third-party software such as [iOS Forensic Toolkit](https://www.elcomsoft.com/eift.html). Importantly, the diagnostic mode can be invoked even if the iPhone is passcode-protected or locked.

To enter iPhone Diagnostic Mode follow these steps.

1. Press and hold both the **volume up** and **volume down** buttons.
2. While holding the two buttons, plug the Lightning cable into the iPhone‌ and connect it to a computer or power adapter.
3. Wait for the Apple logo to appear, then release the buttons.

[![](https://blog.elcomsoft.com/wp-content/uploads/2023/03/diag1.jpg)](https://blog.elcomsoft.com/wp-content/uploads/2023/03/diag1.jpg)

The following screen will display the device’s serial number, MEID, and IMEI numbers.[![](https://blog.elcomsoft.com/wp-content/uploads/2023/03/diag2.jpg)](https://blog.elcomsoft.com/wp-content/uploads/2023/03/diag2.jpg)

If you use iOS Forensic Toolkit while the iPhone is in Diagnostic Mode, you will be able to access additional information that does not appear on the device’s display, such as:

* Exact model number and color of the iPhone
* Wi-Fi MAC address
* iOS version number and built number
* IDs of certain hardware
* Some additional information, which will be exported as an XML

[![](https://blog.elcomsoft.com/wp-content/uploads/2023/03/eift_diag.png)](https://blog.elcomsoft.com/wp-content/uploads/2023/03/eift_diag.png)

## Method 2: Recovery Mode

In iOS, Recovery is a failsafe method for recovering devices if they become unresponsive. The Recovery mode, also known as “second-stage loader”, boots the device in iBoot (bootloader) mode. iBoot can be used to flash the device with a new OS. iBoot responds to a limited number of commands, and can return some limited information about the device. As iBoot does not load iOS, it also does not carry many iOS restrictions. In particular, iBoot/Recovery mode allows connecting the device to the computer even if USB data transfers are disabled, the device is locked, or the screen lock passcode is unknown.

Compared to Diagnostic Mode, Recovery provides even less information about the device. In particular, the following data is available:

* Device model: two representations of the device model, e.g. iPhone7,2 (n61ap), iPhone10,6 (d221ap) etc.
* ECID (UCID). The ECID (Exclusive Chip Identification) or Unique Chip ID is an identifier unique to every unit, or more accurately, to every SoC.
* Serial number

Read more about the Recovery mode:

[The True Meaning of iOS Recovery, DFU and SOS Modes for Mobile Forensics](https://blog.elcomsoft.com/2020/01/ios-recovery-dfu-and-sos-modes-forensics/)

[![](https://blog.elcomsoft.com/wp-content/uploads/2023/03/eift_recovery.png)](https://blog.elcomsoft.com/wp-content/uploads/2023/03/eift_recovery.png)

## Method 3: DFU mode

Unlike Recovery, DFU mode was never intended for general use. This mode lacks proper documentation, and requires precise timing for every step (otherwise the device will simply reboot). As a result, entering DFU mode can be difficult even for experts, especially if the device has one or more [buttons broken](https://blog.elcomsoft.com/2021/09/how-to-put-an-ios-device-with-broken-buttons-in-dfu-mode/).

The DFU mode returns even less information compared to the Recovery mode, and significantly less information than Diagnostic mode.

* Device model: two representations of the device model, e.g. iPhone7,2 (n61ap), iPhone10,6 (d221ap) etc.
* ECID/Unique Chip ID: XXXXXXXXXXXXXXXX

Serial number and IMEI number are never available in DFU. DFU does not return iOS version number; however, **iBoot version number** is available through DFU, which allows guesstimating iOS version number.

Read more about information available in DFU mode and steps to enter DFU on various Apple devices:

[The True Meaning of iOS Recovery, DFU and SOS Modes for Mobile Forensics](https://blog.elcomsoft.com/2020/01/ios-recovery-dfu-and-sos-modes-forensics/)

[![](https://blog.elcomsoft.com/wp-content/uploads/2023/03/eift_dfu.png)](https://blog.elcomsoft.com/wp-content/uploads/2023/03/eift_dfu.png)

## Conclusion

The IMEI, MEID, MAC address, and serial number of the device are crucial pieces of information that can aid forensic investigations in understanding an iPhone’s history, ownership, and involvement in criminal activities. While obtaining this information from a locked iPhone can be challenging, various methods are available to forensic investigators, including iPhone Diagnostic Mode, Recovery Mode, and DFU Mode. Each method provides different levels of information, with iPhone Diagnostic Mode providing the most comprehensive details.

#### REFERENCES:

![](https://www.elcomsoft.com/images/bicons/eift.gif)

### Elcomsoft iOS Forensic Toolkit

Extract critical evidence from Apple iOS devices in real time. Gain access to phone secrets including passwords and encryption keys, and decrypt the file system image with or without the original passcode. Physical and logical acquisition options for all 64-bit devices running all versions of iOS.

[Elcomsoft iOS Forensic Toolkit official web page & downloads »](https://www.elcomsoft.com/eift.html)

文章来源: https://blog.elcomsoft.com/2023/03/obtaining-serial-number-mac-meid-and-imei-of-a-locked-iphone/
 如有侵权请联系:admin#unsafe.sh

© [unSafe.sh - 不安全](https://unsafe.sh) Powered By [PaperCache](https://github.com/code-scan/PaperCache)

* admin#unsafe.sh
* [安全马克](https://aq.mk)
* [星际黑客](https://xj.hk)
* [T00ls](https://t00ls.net)