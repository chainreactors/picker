---
title: LightSpy: Implant for iOS
url: https://www.threatfabric.com/blogs/lightspy-implant-for-ios
source: Over Security - Cybersecurity news aggregator
date: 2024-10-30
fetch_date: 2025-10-06T18:55:16.670697
---

# LightSpy: Implant for iOS

[Skip to content](#main-content)

[![threatfabric-logo-light](https://www.threatfabric.com/hubfs/Threatfabric/logos/threatfabric-logo-light.svg "threatfabric-logo-light")](//www.threatfabric.com/)

[![threatfabric-logo-light](https://www.threatfabric.com/hubfs/Threatfabric/logos/threatfabric-logo-light.svg "threatfabric-logo-light")](//www.threatfabric.com/)

* OUR SOLUTIONS
  + [Mobile Threat Intelligence (MTI)](https://www.threatfabric.com/mti)
  + [Fraud Risk Suite (FRS)](https://www.threatfabric.com/frs)
* [PARTNERS](https://www.threatfabric.com/partners)
* [WEBINARS](https://www.threatfabric.com/webinars)
* [ARTICLES](https://www.threatfabric.com/blogs)
* RESOURCES
  + [DATASHEETS & REPORTS](https://www.threatfabric.com/resources)
  + [IN THE NEWS](https://www.threatfabric.com/news)
* [Contact](https://www.threatfabric.com/contact)
* [Linkedin](https://www.linkedin.com/company/threatfabric)
* [Twitter](https://twitter.com/threatfabric)
* [Jobs](https://www.threatfabric.com/jobs)
* [Privacy](https://www.threatfabric.com/privacy)
* [Intel/PGP](https://www.threatfabric.com/contact)

[Contact](https://www.threatfabric.com/contact)

Research

## LightSpy: Implant for iOS

29 October 2024

![](https://www.threatfabric.com/hubfs/TF_LightSpyiOS.jpg)

### Jump to

In May 2024, ThreatFabric published a [report](https://www.threatfabric.com/blogs/lightspy-implant-for-macos) about LightSpy for macOS. During that investigation, we discovered that the threat actor was using the same server for both macOS and iOS campaigns.

Thanks to this, we were also able to obtain the most recent samples of LightSpy for iOS. After a brief analysis of the obtained files, we concluded that this version slightly differs from the version discussed by [researchers in 2020](https://documents.trendmicro.com/assets/Tech-Brief-Operation-Poisoned-News-Hong-Kong-Users-Targeted-with-Mobile-Malware-via-Local-News-Links.pdf).

The previously documented version of LightSpy's Core for iOS was identified as "6.0.0." However, the version we obtained from this server was "7.9.0." The updates extended beyond the Core itself—the plugin set increased significantly from 12 to 28 plugins. Notably, seven of these plugins have destructive capabilities that can interfere with the device’s boot process.

In this report, we will examine the latest version of LightSpy for iOS, along with its associated plugins.

## Research summary

The threat actor expanded support for the iOS platform, targeting up to version 13.3. They utilized the publicly available Safari exploit CVE-2020-9802 for initial access and CVE-2020-3837 for privilege escalation.

The actor ran multiple campaigns with varying sets of plugins. One particular campaign included plugins that could disrupt the operating system’s stability, with capabilities to freeze the device or even prevent it from booting up.

## Background

During our analysis, we discovered that the threat actor continued to rely on publicly available exploits and jailbreak kits to gain access to devices and escalate privileges. We believe this threat actor is also deeply involved with jailbreak code integration within the spyware's structure, which supports its modular architecture. Additionally, we found that some core binary files of the spyware were signed with the same certificate used in jailbreak kits.

Our investigation revealed five active command-and-control (C2) servers associated with the LightSpy iOS campaign. Each server returned a JSON file containing what appeared to be deployment dates for the spyware, with the latest observed date being October 26, 2022. Notably, the remote code execution vulnerability used to deliver LightSpy to iOS victims was actually patched in 2020.

This raises the question of why infrastructure hosting outdated malware is still maintained. Since some samples contained the label “DEMO,” it’s possible the infrastructure is used for demonstration purposes, showcasing LightSpy's malicious capabilities to potential customers. However, we found no evidence that LightSpy is being promoted as malware-as-a-service (MaaS) on any known attacker forums.

We also observed many code similarities between the macOS and iOS versions of the LightSpy implant, particularly in the core functions and plugins. These similarities strongly suggest that both versions were developed by the same team.

While the iOS implant delivery method closely mirrors that of the macOS version, the post-exploitation and privilege escalation stages differ significantly due to platform differences.

Based on our findings, we were able to map out the following attack chain:

![LightSpy-iOS-Layout](https://www.threatfabric.com/hubfs/LightSpy-iOS-Layout.bmp)

## Technical analysis

### Initial stage: index.html

The threat actor followed the previously observed approach to gain access to the target device: a WebKit [vulnerability](https://googleprojectzero.blogspot.com/2020/09/jitsploitation-one.html) was used as an initial attack vector. This time it was CVE-2020-9802, which was fixed in iOS 13.5, while two of the mitigation bypasses, CVE-2020-9870 and CVE-2020-9910, were fixed in iOS 13.6. In both macOS and iOS campaigns the exploits, which were used by threat actors, were published by the same security researcher.

The URL of the exploit contained the same magic number as was used in Android and macOS campaigns: hxxp://103.27.109[.]217:52202/**963852741**/ios/**IOS123-133**/index.html

For the iOS versions lower than 12.3 different URL path was used hxxp://103.27.109[.]217:52202/963852741/ios/**ios120-122**/index.html

The usage of the newer WebKit exploit gave the threat actor the possibility to extend the list of supported iOS versions including version 13.3.

|  |  |
| --- | --- |
| **Device** | **Supported iOS version** |
| iPhone 6 | 12.3 - 12.4.1 |
| iPhone 6+ | 12.3 - 12.4.1 |
| iPhone 6S | 12.3 - 12.4.1, 13.0 - 13.3 |
| iPhone 6S+ | 12.3 - 12.4.1, 13.0 - 13.3 |
| iPhone 7 | 12.3 - 12.4.1, 13.0 - 13.3 |
| iPhone 7+ | 12.3 - 12.4.1, 13.0 - 13.3 |
| iPhone 8 | 12.3 - 12.4.1, 13.0 - 13.3 |
| iPhone 8+ | 12.3 - 12.4.1, 13.0 - 13.3 |
| iPhone X | 12.3 - 12.4.1, 13.0 - 13.3 |

The exploit consisted of 7 files, the main one was index.html:

* index.html
* offsets.js
* device.js
* binary.js
* primitives130401.js
* wrapper.js
* gadget.js

In case of successful exploitation, index.html will drop in the system a file with a “.png” extension which is a Mach-O binary executable.

![Screenshot 2024-07-17 at 13.33.40](https://www.threatfabric.com/hs-fs/hubfs/Screenshot%202024-07-17%20at%2013.33.40.png?width=982&height=358&name=Screenshot%202024-07-17%20at%2013.33.40.png)

The name of the file depends on the version of iOS: "20012001330.png" in case the victim had iOS version 13 and above, "20012001241.png" for any older iOS versions.

### Stage 1: Jailbreak

From the code perspective, "20012001330.png" and "20012001241.png" are identical; the only difference is the embedded encrypted blob which contains URLs that point to supporting files and the next stage downloader. "20012001241.png" will download file "aaa12", "20012001330.png" will download "aaa13".

The threat actor created "20012001330.png" to trigger vulnerability [CVE-2020-3837](https://nvd.nist.gov/vuln/detail/CVE-2020-3837) using a [“time\_waste”](https://github.com/jakeajames/time_waste) exploit and a corresponding [jailbreak kit.](https://github.com/jakeajames/jelbrekLib) Technically, "20012001330.png" is fully based on the source code which is publicly available on GitHub. The unique feature is that "20012001330.png" will decrypt 0x340 bytes from its own body (by file offset 0x560d8) and will use the results as URLs. It will download files from these URLs, decrypt and save them using hardcoded file names.

![Screenshot 2024-07-17 at 18.00.56](https://www.threatfabric.com/hs-fs/hubfs/Screenshot%202024-07-17%20at%2018.00.56.png?width=1376&height=1156&name=Screenshot%202024-07-17%20at%2018.00.56.png)

**Stage 1 main ...