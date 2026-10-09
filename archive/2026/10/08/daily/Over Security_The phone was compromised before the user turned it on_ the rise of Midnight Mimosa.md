---
title: The phone was compromised before the user turned it on: the rise of Midnight Mimosa
url: https://www.bitdefender.com/en-us/blog/labs/midnight-mimosa-malware
source: Over Security
date: 2026-10-08
fetch_date: 2026-10-09T08:12:05.154187
---

# The phone was compromised before the user turned it on: the rise of Midnight Mimosa

* [Company](/en-us/company/ "Company")
* [Blog](/en-us/blog/ "Blog")

[For Home](/en-us/consumer/ "For Home")[For Business](/en-us/business/ "For Business")[For Partners](/en-us/partners/ "For Partners")

[Consumer Insights](/en-us/blog/hotforsecurity/ "Consumer Insights")[Labs](/en-us/blog/labs/ "Labs")[Business Insights](/en-us/blog/businessinsights/ "Business Insights")

[Anti-Malware Research](/en-us/blog/labs/tag/antimalware-research "Anti-Malware Research")

31 min read

# The phone was compromised before the user turned it on: the rise of Midnight Mimosa

[![Adrian Mihai GOZOB](https://blogapp.bitdefender.com/labs/content/images/size/w100/2022/05/adrian-mihai-gozob.jpg "Adrian Mihai GOZOB")](/en-us/blog/labs/author/agozob "Adrian Mihai GOZOB")[![Alex BACIU](https://blogapp.bitdefender.com/labs/content/images/size/w100/2022/08/20220817_120008.jpg "Alex BACIU")](/en-us/blog/labs/author/albaciu "Alex BACIU")

[Adrian Mihai GOZOB](/en-us/blog/labs/author/agozob "Adrian Mihai GOZOB")[Alex BACIU](/en-us/blog/labs/author/albaciu "Alex BACIU")

October 08, 2026

  ![The phone was compromised before the user turned it on: the rise of Midnight Mimosa](https://blogapp.bitdefender.com/labs/content/images/size/w600/2026/10/Midnight-Mimosa-Circuit-Bloom--1-.jpg "The phone was compromised before the user turned it on: the rise of Midnight Mimosa")

*Bitdefender's security researchers have identified a malware campaign (dubbed Midnight Mimosa) running on low-cost, multi-brand Android devices built on MediaTek platforms.*

The malware ships preinstalled in the device firmware, and we found multiple system packages involved, depending on the device. It’s on the phone before the owner switches it on for the first time, and it can’t be uninstalled.

The malware runs with system-level privileges that allow it to silently install and remove apps, grant permissions, and load arbitrary code supplied remotely. This essentially means its operators could install and delete apps at will, tuning each device to their needs, including making them part of large botnets.

This scheme is likely designed mainly to generate revenue. The operators carry out ad and click fraud, collect device and installed-app information, and turn infected devices into residential-proxy relay nodes, making them zombies in botnets. This creates an additional revenue stream, as access to botnets for DDoS attacks is a hot commodity. The larger the botnet, the more money they can charge.

The system app itself doesn’t register the fraudulent impressions and clicks. The revenue engine is driven by the dropped cover apps, including real-looking weather, app-lock, note, and OCR apps, which load genuine ads through a legitimate ad SDK. The goal is simple: to load an invisible window on top of apps that registers ads being shown.

This system app - com.android.system.lite - was the first one identified, but it turned out to be the tip of the iceberg. As the investigation continued, we identified the same malware core shipping under a rotating set of system-sounding names, including com.android.sys.prot, com.android.sys.gmsprot and com.android.sys.bcprot.

Each is a different build; some carry different signing certificates, and even different names. The package name is not the threat. The shared core underneath it is.

To top it off, we also discovered 13 apps currently present on Google Play that communicate with the same servers that control the malware. While these apps don’t have the rights that would allow them to be as malicious as the preinstalled packages, they are dangerous nonetheless.

## Key findings

* The core of the infection chain is a platform-signed, persistent system application found pre-installed on affected Android devices.
* The enabler silently deploys a rotating family of at least 32 unique disguised apps, including fake AppLock, weather, file-manager, icon-tool, OCR, and audio-editors.
* It grants itself dangerous permissions such as Accessibility, Notification Access and SMS read/write - we noticed neither of these to be used in practice, but they're available to the operator on demand (arbitrary remote code loading). Our insights also show that Accessibility and Notification Access are automatically and repeatedly granted and ungranted after a short while.
* The malware disables the Google Play Store app just before installing a payload app (probably attempting to avoid a potential Play Protect detection). After the payload runs, the Google Play Store app is re-enabled. There's also a safety net that re-enables the app when the user is present, to avoid triggering suspicions.
* Payloads perform hidden ad fraud and automated click fraud or turn the device just another part of large botnets.
* The system app and payload family use shared infrastructure, including a command-and-control service disguised as a weather API.
* The enabler is not a single package. The same core ships under several system-sounding names across different builds and signing certificates.
* The same ad-fraud code was also found in thirteen applications published on Google Play, under at least two developer accounts and thirteen separate signing certificates.

The investigation began with App Anomaly Detection, a technology in Bitdefender Mobile Security, which flagged com.android.system.lite: a package carrying the name and appearance of a core system component while behaving like nothing of the sort.

![](https://blogapp.bitdefender.com/labs/content/images/2026/10/Picture1-1.png)

Most mobile security still runs on a single assumption: scan an app, and if it's deemed clean, it's safe. Bitdefender's App Anomaly Detection (introduced in 2023) exists because, in practice, the theory often doesn’t hold up.

Apps can sit dormant and turn hostile weeks later, sometimes only if certain conditions are met (targeted malware). Such apps can pass every static check, only to later pull their real payload from a server or cleverly unpack it from native code.

App Anomaly Detection closes this gap by watching what apps do, continuously, on the device itself - combining on-device machine learning, real-time behavioral analysis, and a range of other signals. It doesn't rely on whether an app looked clean yesterday; it reacts to the behavior itself, catching apps red-handed the moment they cross the line from benign to malicious.

That real-time behavioral analysis made all the difference. The application was preinstalled as a system app (platform-signed). It’s impossible to uninstall; there’s no store review, and it’s not the user’s choice. Every user-facing defense had already been bypassed by the time the phone was switched on. Behavior was the only thing left to catch it by.

From there, Bitdefender's insights showed what it had been doing. The system app was silently installing and removing a rotating set of payloads on the same devices, among them com.mobile.applock.wt, an app presenting itself as an App Lock tool, while missing the functionality its name suggested.

There’s no interface or code that would let it work as the name suggests, and it was completely hidden from the user. This was, in fact, a highly obfuscated Dropper malware in its own right - but it was not the root cause of the infection.

That is exactly how this investigation began. On paper, nothing about com.android.system.lite invited a careful second look: a platform-signed component disguised as part of the operating system, with no icon and no visible behavior, its actual machinery buried in a native library that only came to life at runtime.

 App Anomaly Detection flagged com.android.system.lite because while it posed as a core Android component, it didn’t behave like one. It repeatedly enabled sensitive access, including Accessibility and Notification Access, and silently installed and removed unrelated applications.

By following these highly suggestive crumbs, the researchers discovered the malware’s source: a persistent, pre-installed s...