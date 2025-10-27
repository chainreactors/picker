---
title: Best Practices in Mobile Forensics: Separating Extraction and Analysis
url: https://buaq.net/go-173325.html
source: unSafe.sh - 不安全
date: 2023-08-01
fetch_date: 2025-10-06T16:59:35.316642
---

# Best Practices in Mobile Forensics: Separating Extraction and Analysis

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

Best Practices in Mobile Forensics: Separating Extraction and Analysis

In the ever-evolving landscape of digital investigations, m
*2023-7-31 23:34:34
Author: [blog.elcomsoft.com(查看原文)](/jump-173325.htm)
阅读量:27
收藏*

---

![](https://secure.gravatar.com/avatar/2664b2a09a29ddba5fe47c73f061d98c?s=60&d=mm&r=x)

In the ever-evolving landscape of digital investigations, mobile forensics has become a critical aspect of law enforcement work. The challenges of extracting, handling, and analyzing data obtained from various sources have led to a growing demand for universal solutions. We’d like to emphasize the importance of every stage of mobile forensics, the significance of extraction, and the critical importance of expertise in this field.

## Stages of Mobile Forensics

Mobile forensics involves several crucial stages that cannot be overlooked. These stages include preliminary tasks such as device isolation, transportation, and proper documentation. Following these, the actual extraction process takes place, which is then followed by analysis and generating reports for further investigation or archival purposes.

Extraction is a pivotal stage in mobile forensics as it can make or break an investigation. It is essential to choose the right extraction method to avoid damaging the device, missing critical data, or wasting time. A variety of extraction methods exists in mobile forensics, including advanced logical extraction, bootloader-based extraction, agent-based extraction, and cloud-based extraction. Each method has its advantages and limitations, so it’s crucial to understand them and have access to the necessary software. Please check out [this article](https://blog.elcomsoft.com/2022/11/approaching-ios-extractions-choosing-the-right-acquisition-method/) and follow our blog for updated information on selecting the appropriate extraction method, as the field constantly evolves.

## The Choice of Forensic Software

Choosing the right forensics software is crucial for successful data extraction. Consider factors like compatibility with different devices, reliability, speed, and the platform the software operates on. It is important to conduct thorough research before investing in any software to ensure it meets the specific requirements of your investigations. A proper research may not be easy, as forensic vendors tend to hide essential information from their customers (read [part 1](https://blog.elcomsoft.com/2023/06/what-forensic-vendors-dont-like-to-tell-their-customers-part-1/) and [part 2](https://blog.elcomsoft.com/2023/06/what-forensic-vendors-dont-like-to-tell-their-customers-part-2/)). It is crucial to understand that there is no single software solution that can fully meet the diverse needs of the DFIR field. Relying solely on press releases and marketing materials is ill-advised; always do your homework before trusting forensic software vendors’ claims.

## The Choice of Extraction Methods

A variety of extraction methods exists in mobile forensics, including advanced logical extraction, bootloader-based extraction, agent-based extraction, and cloud-based extraction. Each method has its advantages and limitations, so it’s crucial to understand them and have access to the necessary software.

For iOS devices, low-level extraction is the most effective method by a large margin that returns the full file system image and decrypts the keychain containing important data like passwords and encryption keys. Low-evel extraction remains the only way to access encrypted conversations in secure instant messengers (e.g. Signal). However, low-level extraction availability is limited to older devices or versions of iOS, leading to delays in supporting newer iOS releases. This rapid succession of updates and patches makes data extraction a continuous challenge for forensic experts.

When it comes to low-level extraction, bootloader-level extraction and [agent-based extraction](https://blog.elcomsoft.com/2023/02/behind-the-scenes-of-ios-data-extraction-exploring-the-extraction-agent/) are available. Bootloader-level extraction relies on vulnerabilities that exist in some devices’ bootloaders. For 64-bit Apple devices we’re using the checkm8 exploit, which, in our implementation, delivers [repeatable, verifiable and safe](https://blog.elcomsoft.com/2023/02/forensically-sound-checkm8-extraction-repeatable-verifiable-and-safe/) extractions. Bootloader-level extraction, however, is only available for older devices (up to and including the iPhone 8/8 Plus/iPhone X generation and other Apple devices based on similar chips); moreover, there are severe limitations to bootloader extractions introduced in recent versions of iOS due to [SEP hardening](https://blog.elcomsoft.com/2022/09/ios-16-sep-hardening-new-security-measures-and-their-forensic-implications/) and [other security measures](https://blog.elcomsoft.com/2022/12/checkm8-for-ios-16-2-and-windows-based-ios-low-level-extraction/).

If bootloader-level extraction is not available for a given device, yet another method based on the extraction agent may be used if the device is running a compatible version of iOS (at this time the highest OS version supported by the extraction agent is iOS 16.4, with support for newer releases in the works). The agent-based method is the second best after bootloader-based extraction. We published a comprehensive overview of the extraction agent in [Exploring the Extraction Agent](https://blog.elcomsoft.com/2023/02/behind-the-scenes-of-ios-data-extraction-exploring-the-extraction-agent/).

In cases where unsupported iOS versions are encountered, advanced logical extraction becomes the only viable option. While it allows the extraction of device backups, some system logs, media files and metadata, it may not retrieve critical data like email messages or conversation histories from popular instant messaging apps.

Last but not least, [cloud extraction](https://blog.elcomsoft.com/2023/07/apple-icloud-acquisition-a-lifeline-for-forensic-experts) may provide a viable solution, especially in situations where the physical device is inaccessible for data extraction. Such situations may include physical damage to the device, such as water damage or hardware failures, as well as instances where the device has undergone a factory reset or has been wiped clean may hinder data retrieval efforts. In all these cases [Elcomsoft Phone Breaker](https://www.elcomsoft.com/eppb.html)‘s cloud extraction option becomes the last resort, extracting all available information from Apple iCloud subject to authentication credentials.

## Common Mistakes and Their Consequences

In general, some of the most significant mistakes during or before the extraction process that lead to data loss include:

* The device goes online during extraction, which may cause unwanted synchronization and/or remove wipe or remote lock.
* Failing to capture the complete file system and only creating a backup when low-level extraction is available.
* Neglecting to check other potential data sources, such as old local backups, cloud backups, or other devices.
* Resetting the password, inadvertently locking out access to critical data.
* Relying solely on one software tool without cross-verification.

These errors can have severe consequences and result in the loss of crucial evidence. Therefore, it is essential to exercise caution, follow best practices, and consider all available data sources to ensure the success of mobile forensics investigations.

## The Analysis Stage

The analysis stage requires powerful hardware to process and interpret the extracted data effectively. Unli...