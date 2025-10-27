---
title: Forensically Sound checkm8 Extraction: Repeatable, Verifiable and Safe
url: https://buaq.net/go-147565.html
source: unSafe.sh - 不安全
date: 2023-02-02
fetch_date: 2025-10-04T05:28:00.199227
---

# Forensically Sound checkm8 Extraction: Repeatable, Verifiable and Safe

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

![]()

Forensically Sound checkm8 Extraction: Repeatable, Verifiable and Safe

What does “forensically sound extraction” mean? The
*2023-2-1 21:52:35
Author: [blog.elcomsoft.com(查看原文)](/jump-147565.htm)
阅读量:24
收藏*

---

![](https://secure.gravatar.com/avatar/2664b2a09a29ddba5fe47c73f061d98c?s=60&d=mm&r=x)

What does “forensically sound extraction” mean? The classic definition of forensically sound extraction means both repeatable and verifiable results. However, there is more to it. We believe that forensically sound extractions should not only be verifiable and repeatable, but verifiable in a safe, error-proof manner, so we tweaked our product to deliver just that.

## TL&DR

During checkm8 extractions of supported iOS/iPadOS devices, iOS Forensic Toolkit 8 automatically disables auto-boot behavior of the device, which ensures that the device boots into Recovery on subsequent power-on and restart events. The flag is stored in the device’s NVRAM and is not automatically removed even between reboots and power-offs. Experts must manually set auto-boot to True before releasing the device to its owner; otherwise a “broken device” complaint is more than likely.

## Forensically sound extractions must be verifiable

Forensically sound extractions must deliver results that are both repeatable and verifiable. Forensically sound extraction methods are designed to preserve digital evidence from the first point of data collection and establish chain of custody to ensure that digital evidence collected during the investigation remains court admissible.

First and foremost, a forensically sound extraction must deliver results that can be securely verified. Verifiable results prove authenticity of the extraction, certifying that the data obtained from the device had not been manipulated post extraction.

To do that, experts routinely document the extraction process, producing and saving (sometimes on paper) a digital signature, hash or checksum of the extracted data. The use of hashing at the time of extraction helps establish digital chain of custody, producing results that can be verified in the future. Our low-level extraction tool, Elcomsoft iOS Forensic Toolkit, calculates a cryptographic hash value that can be used to validate the image’s authenticity later on. We published a quick how-to guide in the following article: [Forensically Sound Extraction for iPhone 5s, 6, 6s and SE](https://blog.elcomsoft.com/2021/11/forensically-sound-extraction-for-iphone-5s-6-6s-and-se/). In addition, check out [checkm8 Extraction Cheat Sheet: iPhone and iPad Devices](https://blog.elcomsoft.com/2022/11/checkm8-extraction-cheat-sheet-iphone-and-ipad-devices/).

**Applicability**: when it comes to mobile forensics, all extraction methods including logical acquisition can be made verifiable. However, only select few methods can deliver repeatable results; see next chapter.

## Forensically sound extractions must be repeatable

A file system image can be checked against its hash value to prove the data had not been manipulated with after the extraction. What about a proof that the data was extracted from a particular device? A second extraction can be performed from the same device. The “repeatable” part means that any subsequent extraction from the same device shall match all previous extractions. To prove that the two data sets match, one can calculate the hash values of the new extraction and compare it with the hash value of the originally extracted data. Due to the nature of cryptographic hashes, even a single flipped bit in the data results in a drastically different hash value. If the hashes do match, you can be sure that the two images are identical.

**Applicability**: for iOS devices, only bootloader-based extractions (such as the checkm8 extraction method implemented in Elcomsoft iOS Forensic Toolkit) can deliver repeatable results. Note that not every checkm8-based extraction is repeatable depending on your workflow and the choice of tools.

Our checkm8 solution delivers forensically sound extractions; subsequent images will match the original if the device itself was not allowed to boot into iOS between extractions. Which, in turn, is more of a problem than we initially expected.

## Repeatable extractions aren’t that easy

When the device boots into the installed OS, it inevitably makes multiple modifications into the user partition. Even if the device is isolated from all wireless networks, and even if it is not unlocked after a restart, iOS will add records to log files and change multiple timestamps. As we know, flipping a single bit in the dataset will result in a very different hash value being computed. The two images will no longer match.

Why would one allow the device to boot into iOS in the first place? Often, this happens as an accident. Placing iOS devices into DFU is a tricky process that requires precise timings. Press a button for too long or too short, and the device may start booting into the system. Since repeat extractions may be handled by a different expert, such an outcome is more than likely.

We tried to make the extractions more secure by offering an option that alters the boot behavior of iOS devices.

## Our solution: flipping the ‘autoboot’ flag

First and foremost, experts can manually flip the ‘autoboot’ flag with the following command executed while the device was in Recovery:

```
./EIFT_cmd tools autobootFalse
```

Once executed, this command modifies device behavior during the boot sequence. If the device is powered on or if the device is restarted, with ‘autobootFalse’ it will load the Recovery instead of the main OS. Booting into recovery is safe as nothing in the user data is modified. The flag is stored in the device’s NVRAM, and survives reboots and power-offs.

We suggested keeping the device in the ‘autobootFalse’ state until the moment the device was released and returned to the owner, in which case another command would restore the ability to boot iOS:

```
./EIFT_cmd tools autobootTrue
```

Note that iOS Forensic Toolkit 8 automatically sets auto-boot value to False at some point after sending iboot, but before sending kernel and booting the ramdisk.

This behavior effectively secures the user data against accidental modifications caused by user error when entering DFU. An important consequence: the device will have the ‘autobootFalse’ flag still enabled after you finish the extraction. This means that any subsequent power-on or reboot will make the device launch Recovery instead of starting the installed operating system. We recommend keeping this flag enabled all the time while the device is retained as evidence, and only reverting to ‘autobootTrue’ immediately before the device is returned to its owner.

What happens if the expert does not reset the autoboot flag? In this case, the owner will receive an unbootable device that constantly boots into Recovery. This is not the original working state of the device, and one may receive a complaint. The situation is easily avoidable: simply use the ‘autobootTrue’ command prior to returning the device to its owner.

## The auto-boot flag and forensically sound extractions

Flipping the auto-boot flag does not affect the forensically sound status of the extraction for two reasons.

1. The user data is not affected.
2. The system partition is not affected because the flag is stored in the device’s NVRAM.

Regardless, experts should always request permission to modify device content. checkm8 extractions are not always possible, while all other extraction methods alter the content of the device in one way or another.

## If the batter...