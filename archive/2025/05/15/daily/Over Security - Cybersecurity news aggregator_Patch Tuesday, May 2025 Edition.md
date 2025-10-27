---
title: Patch Tuesday, May 2025 Edition
url: https://krebsonsecurity.com/2025/05/patch-tuesday-may-2025-edition/
source: Over Security - Cybersecurity news aggregator
date: 2025-05-15
fetch_date: 2025-10-06T22:28:32.635536
---

# Patch Tuesday, May 2025 Edition

Advertisement

[![](/b-gartner/7.jpg)](https://www.gartner.com/en/conferences/na/identity-access-management-us?utm_source=krebs&utm_medium=banner&utm_campaign=EVT_NA_2025_IAM20_PP_MP6_KREBSONSECURITY)

Advertisement

[![](/b-action1/2.jpg)](https://action1.com/double-endpoints-free-cam2025/?utm_source=paidmedia&refid=Display_CAM_Krebs)

[![Krebs on Security](https://krebsonsecurity.com/wp-content/uploads/2021/03/kos-27-03-2021.jpg)](https://krebsonsecurity.com/ "Krebs on Security")

[Skip to content](#content "Skip to content")

* [Home](https://krebsonsecurity.com/)
* [About the Author](https://krebsonsecurity.com/about/)
* [Advertising/Speaking](https://krebsonsecurity.com/cpm/)

# Patch Tuesday, May 2025 Edition

May 14, 2025

[25 Comments](https://krebsonsecurity.com/2025/05/patch-tuesday-may-2025-edition/#comments)

**Microsoft** on Tuesday released software updates to fix at least 70 vulnerabilities in **Windows** and related products, including *five zero-day flaws that are already seeing active exploitation*. Adding to the sense of urgency with this month’s patch batch from Redmond are fixes for two other weaknesses that now have public proof-of-concept exploits available.

![](https://krebsonsecurity.com/wp-content/uploads/2022/07/winupdatedate.png)

Microsoft and several security firms have disclosed that attackers are exploiting a pair of bugs in the **Windows Common Log File System** (CLFS) driver that allow attackers to elevate their privileges on a vulnerable device. The Windows CLFS is a critical Windows component responsible for logging services, and is widely used by Windows system services and third-party applications for logging. Tracked as [CVE-2025-32701](https://msrc.microsoft.com/update-guide/en-US/advisory/CVE-2025-32701) & [CVE-2025-32706](https://msrc.microsoft.com/update-guide/en-US/advisory/CVE-2025-32706), these flaws are present in all supported versions of Windows 10 and 11, as well as their server versions.

**Kev Breen**, senior director of threat research at **Immersive Labs**, said privilege escalation bugs assume an attacker already has initial access to a compromised host, typically through a phishing attack or by using stolen credentials. But if that access already exists, Breen said, attackers can gain access to the much more powerful Windows SYSTEM account, which can disable security tooling or even gain domain administration level permissions using credential harvesting tools.

“The patch notes don’t provide technical details on how this is being exploited, and no Indicators of Compromise (IOCs) are shared, meaning the only mitigation security teams have is to apply these patches immediately,” he said. “The average time from public disclosure to exploitation at scale is less than five days, with threat actors, ransomware groups, and affiliates quick to leverage these vulnerabilities.”

Two other zero-days patched by Microsoft today also were elevation of privilege flaws: [CVE-2025-32709](https://msrc.microsoft.com/update-guide/en-US/advisory/CVE-2025-32709), which concerns afd.sys, the **Windows Ancillary Function Driver** that enables Windows applications to connect to the Internet; and [CVE-2025-30400](https://msrc.microsoft.com/update-guide/en-US/advisory/CVE-2025-30400), a weakness in the **Desktop Window Manager** (DWM) library for Windows. As **Adam Barnett** at **Rapid7** notes, tomorrow marks the [one-year anniversary](https://www.rapid7.com/blog/post/2024/05/14/patch-tuesday-may-2024/) of [CVE-2024-30051](https://portal.msrc.microsoft.com/en-US/security-guidance/advisory/CVE-2024-30051), a previous zero-day elevation of privilege vulnerability in this same DWM component.

The fifth zero-day patched today is [CVE-2025-30397](https://msrc.microsoft.com/update-guide/en-US/advisory/CVE-2025-30397), a flaw in the **Microsoft Scripting Engine**, a key component used by **Internet Explorer** and **Internet Explorer mode** in **Microsoft Edge**.

**Chris Goettl** at **Ivanti** points out that the Windows 11 and Server 2025 updates include some new AI features that carry a lot of baggage and weigh in at around 4 gigabytes. Said baggage includes new artificial intelligence (AI) capabilities, including the controversial **Recall** feature, which constantly takes screenshots of what users are doing on Windows CoPilot-enabled computers.

Microsoft went back to the drawing board on Recall after a fountain of negative feedback from security experts, who warned it would present an attractive target and a potential gold mine for attackers. Microsoft appears to have made some efforts to prevent Recall from scooping up sensitive financial information, but privacy and security concerns still linger. Former Microsoftie **Kevin Beaumont** has [a good teardown](https://cyberplace.social/%40GossiTheDog/114360483150635243) on Microsoft’s updates to Recall.

In any case, **windowslatest.com** reports that **Windows 11 version 24H2** shows up ready for downloads, even if you don’t want it.

“It will now show up for ‘download and install’ automatically if you go to Settings > Windows Update and click Check for updates, but only when your device does not have a compatibility hold,” the publication [reported](https://www.windowslatest.com/2025/05/05/windows-11-24h2-now-fully-ready-downloads-even-if-you-dont-want-it/). “Even if you don’t check for updates, Windows 11 24H2 will automatically download at some point.”

Apple users likely have their own patching to do. On May 12 Apple released security updates to fix at least 30 vulnerabilities in **iOS** and **iPadOS** (the updated version [is 18.5](https://support.apple.com/en-us/122404)). **TechCrunch** [writes](https://techcrunch.com/2025/05/12/apple-brings-emergency-satellite-features-to-iphone-13-with-ios-18-5/) that iOS 18.5 also expands emergency satellite capabilities to iPhone 13 owners for the first time (previously it was only available on iPhone 14 or later).

Apple also [released updates](https://support.apple.com/en-us/100100) for **macOS Sequoia**, **macOS Sonoma**, **macOS Ventura**, **WatchOS**, **tvOS** and **visionOS**. Apple said there is no indication of active exploitation for any of the vulnerabilities fixed this month.

As always, please back up your device and/or important data before attempting any updates. And please feel free to sound off in the comments if you run into any problems applying any of these fixes.

*This entry was posted on Wednesday 14th of May 2025 07:57 AM*

[Latest Warnings](https://krebsonsecurity.com/category/latest-warnings/) [The Coming Storm](https://krebsonsecurity.com/category/comingstorm/) [Time to Patch](https://krebsonsecurity.com/category/patches/)

[Adam Barnett](https://krebsonsecurity.com/tag/adam-barnett/) [CVE-2025-30397](https://krebsonsecurity.com/tag/cve-2025-30397/) [CVE-2025-30400](https://krebsonsecurity.com/tag/cve-2025-30400/) [CVE-2025-32701](https://krebsonsecurity.com/tag/cve-2025-32701/) [CVE-2025-32706](https://krebsonsecurity.com/tag/cve-2025-32706/) [CVE-2025-32709](https://krebsonsecurity.com/tag/cve-2025-32709/) [Immersive Labs](https://krebsonsecurity.com/tag/immersive-labs/) [Kev Breen](https://krebsonsecurity.com/tag/kev-breen/) [Microsoft Patch Tuesday May 2025](https://krebsonsecurity.com/tag/microsoft-patch-tuesday-may-2025/) [Rapid7](https://krebsonsecurity.com/tag/rapid7/) [Windows Common Log File System](https://krebsonsecurity.com/tag/windows-common-log-file-system/)

Post navigation

[← Pakistani Firm Shipped Fentanyl Analogs, Scams to US](https://krebsonsecurity.com/2025/05/pakistani-firm-shipped-fentanyl-analogs-scams-to-us/)
[Breachforums Boss to Pay $700k in Healthcare Breach →](https://krebsonsecurity.com/2025/05/breachforums-boss-to-pay-700k-in-healthcare-breach/)

## 25 thoughts on “Patch Tuesday, May 2025 Edition”

1. Mahhn [May 14, 2025](https://krebsonsecurity.com/2025/05/patch-tuesday-may-2025-edition/#comment-625986)

   MS has made it clear, privacy is a huge no no.

   1. Jaymo [M...