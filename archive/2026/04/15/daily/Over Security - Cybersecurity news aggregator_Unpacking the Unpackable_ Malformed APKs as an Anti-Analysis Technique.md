---
title: Unpacking the Unpackable: Malformed APKs as an Anti-Analysis Technique
url: https://www.cleafy.com/cleafy-labs/malformed-apks-as-an-anti-analysis-technique-malfixer-tool
source: Over Security - Cybersecurity news aggregator
date: 2026-04-15
fetch_date: 2026-04-16T04:54:16.336752
---

# Unpacking the Unpackable: Malformed APKs as an Anti-Analysis Technique

![](https://cdn.prod.website-files.com/plugins/Basic/assets/placeholder.60f9b1840c.svg)

x

Read more

d[![](https://cdn.prod.website-files.com/plugins/Basic/assets/placeholder.60f9b1840c.svg)

x

Discover

NYX

Your Autonomous Cyber Fraud Fusion Center

|

Autonomous AI investigation by Cleafy -

in minutes, not hours.

Learn More

Read more

d](https://nyx.cleafy.com/)![](https://cdn.prod.website-files.com/plugins/Basic/assets/placeholder.60f9b1840c.svg)

x

Read more

d

[![Cleafy Logo](https://cdn.prod.website-files.com/6020129a813fe0c8f1e8053e/6031121f255fb120fa9d4d05_Cleafy-logo.svg)](/)

* [Platform](/platform)
* [Who it's for](/industries)
* [LABS](/threat-intelligence)
* Resources

  g

  [Documents](/resources/documents)[Insights](/resources/insights)[LABS Reports](/labs)[Webinars](/webinars)[Events](/events)

  Resources

  [Documents](/resources/documents)[Insights](/resources/insights)[LABS Reports](/labs)[Webinars](/webinars)[Events](/events)
* Company

  g

  [About us](/about-us)[Careers](/careers)[Partners](/partners)[Press](/press)[News](/news)

  Company

  [About us](/about-us)[Careers](/careers)[Partners](/partners)[Press](/press)[News](/news)
* [Support](https://support.cleafy.com/)
* [Get in touch](/get-in-touch)

[Support](https://support.cleafy.com/)[Get in touch](/get-in-touch)

Malware

Android

Trojan

# Unpacking the Unpackable: Malformed APKs as an Anti-Analysis Technique

###### Published:

###### 15/4/26

[![](https://cdn.prod.website-files.com/6020129a813fe0c8f1e8053e/67d2edc94c8ed8232523cefe_Cleafy-Labs.avif)](/labs)

Download the PDF version

### Download your PDF  guide to TeaBot

Get your free copy to your inbox now

Download PDF Version

### Key Points

* APK malformation is the intentional creation of technically broken or non-standard APK files that still install and run on Android, but confuse or break analysis tools.
* The use of APK malformation is rapidly becoming a standard tactic in modern Android malware campaigns. More and more malicious apps are being discovered with intentionally malformed structures—suggesting that threat actors now see this as a reliable and effective method to bypass static analysis tools and delay detection.
* Malfixer is a newly developed open-source tool from the Cleafy Threat Intelligence Team, designed to detect and fix malformed APKs, enabling analysts to properly examine them.
* Malfixer is publicly available as an open-source project on [GitHub](https://github.com/Cleafy/Malfixer), allowing security researchers and malware analysts worldwide to freely download, use, and contribute to the tool.

### Overview

As Android malware continues to evolve, **APK malformation has emerged as a key anti-analysis technique**, now seen [in over 3,000 Android malware samples](https://zimperium.com/blog/over-3000-android-malware-samples-using-multiple-techniques-to-bypass-detection) and increasingly employed across a broad range of malicious campaigns. By deliberately crafting broken or non-standard APK structures, attackers can **evade static analysis tools**, conceal malicious payloads, and delay detection. This tactic has already been observed in advanced malware families such as **Teabot**, **TrickMo**, and **SpyNote**, underlining its effectiveness in circumventing traditional defenses.

As APK malformation becomes a **standard feature of mobile threats**, there is a growing need for tools that can reliably detect and correct these structural evasions. This article explores how the technique works, why it is gaining attention, and introduces **Malfixer**—a powerful open-source utility designed to **identify and repair malformed APKs**, enabling more effective malware analysis and response.

### Why Malformations Work

The use of malformation as an anti-analysis technique was previously discussed in an [earlier article](https://www.cleafy.com/cleafy-labs/a-new-trickmo-saga-from-banking-trojan-to-victims-data-leak), where it initially prevented the classification of a sample that was later associated with TrickMo. This initial failure to classify the sample was directly linked to the APK’s use of malformation techniques, which hindered standard static analysis tools from correctly processing the file.

Malformations involve different aspects of an Android application, like the **APK file format**, its **Android Manifest** and **internal files**. To understand the first one, we must consider that an **APK** (Android Package) is essentially a **ZIP archive** that contains all the components needed for an Android app to install and run—such as the code, resources, and manifest file. This archive is expected to follow a **well-defined structure**, enabling analysis tools and security scanners to easily extract and inspect its contents.

![](https://cdn.prod.website-files.com/60201cc2b6249b0358f70f8a/69df5b474555589136cb8102_32f0ebad.png)

Figure 1 - APK/ZIP File Format

However, attackers have discovered ways to **intentionally corrupt or manipulate this internal structure** **without breaking the app's ability to function**. By exploiting the leniency of the Android installation system, which **tolerates certain structural inconsistencies**, they can craft malformed APKs that are perfectly valid from the device's point of view but **confuse or crash analysis tools** (e.g. JADX, ZIP extraction utilities, etc.).

This allows malicious apps to install and run normally while making reverse engineering and detection significantly more difficult for researchers and security products. To understand how this is possible, we need to look more closely at the internal structure of ZIP files, which we will explore in the next section.

## ZIP Structure 101

Inside this ZIP file, each file is stored with a small header (called the **Local** **File** **Header**) right before it, which contains important details about that file. Near the end of the APK, there is a special index called the **Central Directory**. This acts like a table of contents, listing information such as the **names of the files**, **where they are located** inside the archive, and **how they were compressed**.

![](https://cdn.prod.website-files.com/60201cc2b6249b0358f70f8a/69df5b474555589136cb810b_60ef0d52.png)

Figure 2 - ZIP File Format

For the latter, most APKs use a common compression method called **Deflate**, which reduces file size without losing any data; however, files are sometimes stored without compression (using the Stored method).

When attackers deliberately introduce errors in these structures—such as **conflicting information** **in the Local File Headers and the Central Directory**—it can confuse or crash tools that try to open and analyze the APK.

![](https://cdn.prod.website-files.com/60201cc2b6249b0358f70f8a/69df5b474555589136cb8105_0e759271.png)

Figure 3 -JADX errors processing a malformed sample

Despite these structural errors, Android devices are usually quite forgiving when it comes to installing apps. Unlike many analysis tools that expect files to be perfectly organized, the **Android system’s installer is designed to be flexible and tolerant of minor irregularities in the APK’s structure**. For example, Android **can avoid checking whether there is a match between the Local File Headers and the Central Directory and proceed with the installation, considering only** the value contained in one of these structures.

This means that even if the archive contains mistakes—such as incorrect file locations or confusing metadata—the device can still correctly find and load the components needed to install and run the app. Another example can regard the compression methods stored in the ZIP headers: if a file within the APK has an unrecognized compression method, the Android system **will automatically treat it as STORED** (that is, without compression), allowing the file to be accessed without issue. In contrast, analysis tools will often fail when attempting to retrieve such a file due to the unexpected com...