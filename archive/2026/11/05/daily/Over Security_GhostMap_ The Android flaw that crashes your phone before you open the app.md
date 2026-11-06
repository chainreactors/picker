---
title: GhostMap: The Android flaw that crashes your phone before you open the app
url: https://www.bitdefender.com/en-us/blog/labs/ghostmap-android
source: Over Security
date: 2026-11-05
fetch_date: 2026-11-06T08:41:33.989293
---

# GhostMap: The Android flaw that crashes your phone before you open the app

* [Company](/en-us/company/ "Company")
* [Blog](/en-us/blog/ "Blog")
* Login

  ##### Your account

  + [Bitdefender Central](https://login.bitdefender.com/central/login.html?lang=en_US&redirect_url=https:%2F%2Fcentral.bitdefender.com)
  + [GravityZone CLOUD Control Center](https://gravityzone.bitdefender.com/)
  + [MDR Portal](https://auth.mdr.bitdefender.com/login)

[For Home](/en-us/consumer/ "For Home")[For Business](/en-us/business/ "For Business")[For Partners](/en-us/partners/ "For Partners")

[Consumer Insights](/en-us/blog/hotforsecurity/ "Consumer Insights")[Labs](/en-us/blog/labs/ "Labs")[Business Insights](/en-us/blog/businessinsights/ "Business Insights")

[Anti-Malware Research](/en-us/blog/labs/tag/antimalware-research "Anti-Malware Research")

16 min read

# GhostMap: The Android flaw that crashes your phone before you open the app

[![Alecsandru Cătălin DAJ](https://blogapp.bitdefender.com/labs/content/images/size/w100/2025/03/1000016262.jpg "Alecsandru Cătălin DAJ")](/en-us/blog/labs/author/alecsandru-daj "Alecsandru Cătălin DAJ")

[Alecsandru Cătălin DAJ](/en-us/blog/labs/author/alecsandru-daj "Alecsandru Cătălin DAJ")

November 05, 2026

  ![GhostMap: The Android flaw that crashes your phone before you open the app](https://blogapp.bitdefender.com/labs/content/images/size/w600/2026/11/Smartphone-trapped-in-a-restart-loop--1-.png "GhostMap: The Android flaw that crashes your phone before you open the app")

*Bitdefender Labs researchers found that installing a specially crafted app can leave an Android phone stuck in a crash loop, even if you never open it or grant it a single permission. The app contains no code and never needs to run.*

After installation, a core system process crashes, restarts, and crashes again, leaving the phone stuck in a boot loop. Restarting doesn't help, and neither does safe mode.

To get the phone working again, you need a factory reset, which erases the user's data. If, by chance, USB debugging had already been enabled, you could use a computer with ADB (Android Debug Bridge) to delete the file before the phone reboots.

We began investigating on Aug. 12, 2026, when an APK collected from the wild crashed emulators in our analysis infrastructure. The sample was a banking dropper that never ran and crashed during installation.

When we looked closer to find out why, we found the problem wasn't the malware—it was the Android itself. The operating system mishandles two fields inside a ZIP entry, the compression method and the declared uncompressed length. Reading such an entry causes a SIGBUS (a signal sent by the CPU to stop a process that accesses an invalid memory space) in whichever process touches the file.

We call it **GhostMap**: the malformed entry causes Android to map the file across memory that was never allocated, and the crash occurs when a process reads from that empty space.

Based on our testing, we consider the risk posed by this bug to be significant. In theory, an attacker could hide this technique in a fake app to disable a victim’s phone, or use the threat of a factory reset and data loss as leverage for extortion. Malformed APKs could also disrupt tools that inspect Android applications. We have not observed any of these scenarios in the wild.

## Key findings

* An app you never open can render your phone unusable. Simply installing the crafted app is enough to trigger the crash loop. It requests no permissions and contains no executable code.
* Restarting the phone doesn’t solve the problem. The crash loop persists after a reboot and continues in safe mode. Restoring the phone may require a factory reset, which erases locally stored data.
* Running on the latest Android version. Researchers reproduced the failure on a Pixel 10 running Android 17 with the Aug. 5, 2026 security patch. It affects all Android versions from Android 10 and above.
* The discovery began with an APK found in the wild. It crashed Bitdefender’s analysis emulators, prompting the investigation. Researchers later developed a demonstration of the persistent crash loop.
* Google assessed the issue as outside the scope of a security fix. Bitdefender reported the findings on Aug. 20 and Aug. 25, 2026. According to Google’s second response, the issue will not be addressed through a security update and was referred to a feature team for possible consideration in a future version.

The banking dropper was wrapped by a packer. This is a tool that rewrites an APK's internal structure so reverse-engineering tools can't read it. It’s very common in modern Android malware.

In this case, the same rewrite also broke the Android component that parses an app during installation. That’s why the installation crashed in the first place and why our emulators failed on it. The good news is that nothing in the sample suggests the author knew the file would crash anything.

The sample did no more than that—a failed install. The underlying flaw runs deeper. We found that the same mistake can be aimed at a core system service instead of the installer, and there it produces the repeating crash loop described above, with no way back except a factory reset. That escalation is our own work; we have not seen it used against anyone.

The underlying problem concerns how Android trusts size and compression information in APK files, and it’s not limited to malformed ZIP files.

## Disclosure timeline and Google’s response

We reported the issue to Google twice through the Android & Devices Vulnerability Reward Program, expanding the second submission after further testing confirmed a persistent system crash loop.

**August 12, 2026 — Initial discovery.** An APK collected from the wild crashed emulators in our analysis infrastructure during installation. Our investigation traced the failure to Android’s handling of ZIP entry compression methods and declared uncompressed length.

We also found that applications using Android’s native APIs to parse APKs could crash when reading them.

We reproduced the bug and made more discoveries. Every attempt to install that APK crashed the OS and caused a reboot:

1. If the file was parsed as an APK by third-party apps using Android's native APIs (including our BMS), the parsing process crashed.
2. The file couldn’t be deleted without ADB (Android Debug Bridge), not even in safe mode, because file-manager processes crashed when they tried to parse it.

**Aug. 20, 2026 — First report to Google.** We submitted these findings, documenting installation-triggered crashes and failures in applications parsing the malformed APK. Google closed the report shortly afterwards with the status *Won’t Fix (Not Reproducible)*. Its accompanying response described the submission as outside the program’s scope.

**Further investigation — Persistent denial of service.** We continued testing and found an APK that installed successfully but caused a system service to crash when it automatically read an application resource. The resulting crash loop prevented access to the interface and continued in safe mode. Recovery could require a factory reset.

We started investigating further after that. We found that we could also malform other files that are not parsed at install time, and that some Android system services try to parse them automatically. This meant the loop followed the regular path: crash, reboot, parse again, and then get stuck in a boot loop once more.

The boot loop we caused would also disable safe-mode access, and the only recovery methods we identified were a factory reset or, in limited conditions, ADB-based scripts racing with the system-server crashes.

Interestingly, Google has already patched a weaker version of this defect. From the November 2016 bulletin, **CVE-2016-6724**:

> *A denial of service vulnerability in the Input Manager Service could enable a local malicious application to cause the device to continually reboot. This issue is rated as Moderate because it is a temporary denial of service that re...