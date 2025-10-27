---
title: The Rise of RatOn: From NFC heists to remote control and ATS
url: https://www.threatfabric.com/blogs/the-rise-of-raton-from-nfc-heists-to-remote-control-and-ats
source: Over Security - Cybersecurity news aggregator
date: 2025-09-10
fetch_date: 2025-10-02T19:55:36.568632
---

# The Rise of RatOn: From NFC heists to remote control and ATS

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

## The Rise of RatOn: From NFC heists to remote control and ATS

09 September 2025

![](https://www.threatfabric.com/hubfs/TF_MTI_RatOn-01.jpg)

### Jump to

Remote Access Trojans (RATs) are a popular commodity on the dark web, particularly when offering full remote control of infected devices. Key features typically sought after include visual access to the device’s screen (in other words: screen casting), as well as a text-based interface that presents a pseudo-screen with textual descriptions of on-screen elements. The latter method offers more responsive and efficient control, as transmitting text consumes significantly fewer resources than streaming graphical data.

While the concept of combining a RAT with an NFC relay attack isn’t entirely new, documented cases are rare. Instances where a trojan evolves from a basic NFC relay tool into a sophisticated RAT with Automated Transfer System (ATS) capabilities are virtually unheard of. That’s why the discovery of the new trojan RatOn by ThreatFabric MTI analysts is particularly noteworthy. RatOn merges traditional overlay attacks with automatic money transfers and NFC relay functionality—making it a uniquely powerful threat.

## Discovery

While monitoring the [NFSkate](/blogs/ghost-tap-new-cash-out-tactic-with-nfc-relay) threat actor group activity, we came across a quite unique sample. What separated this sample from previous ones was the fact that it was not just a standalone APK file, but it was a part of a campaign involving more unique applications.

Our analysis of the campaign revealed a new fully functional banking trojan with device/account takeover capabilities, targeting cryptocurrency wallet applications. Besides that, the malware can perform automated money transfers abusing one specific bank application, as well as perform ransom using custom overlay pages and device locking.

In this report we will uncover the details about this previously unreported trojan which we dubbed as RatOn, based on the name threat actors used for group chat where their discussed the malware. We guess that RAT in the group name refers to Remote Access Tool or Trojan.

According to our telemetry the first related sample was assembled on 5th of July 2025 and the latest on 29th of August 2025. It means that threat actor group focusing on new malware developments for at least two months already. Some of the related samples still have minor detections on VirusTotal.

![scr1_cut](https://www.threatfabric.com/hs-fs/hubfs/Threatfabric/images/blog/Raton/scr1_cut.png?width=1638&height=207&name=scr1_cut.png)

## Initial access

Attackers registered domains with adult themes to infect victims. Such a domains contained TikTok18+ inside their name and directly hosted the malicious dropper application. The is no certainty on how exactly the attackers lure victims to visit such web sites. So far, we know that those pages targeted Czech and Slovakian speaking auditory.

![scr2](https://www.threatfabric.com/hs-fs/hubfs/Threatfabric/images/blog/Raton/scr2.png?width=330&height=230&name=scr2.png)

![scr3](https://www.threatfabric.com/hs-fs/hubfs/Threatfabric/images/blog/Raton/scr3.png?width=315&height=517&name=scr3.png)

## Technical details

We believe that the RatOn trojan was written from scratch, no code similarities were found with existing malware families. The account takeover and automated transfer features have shown that threat actor know the internals of the targeted applications quite well.

RatOn was designed, like many modern Android bankers, as a multi-stage process. and distributed by infecting the victim using a dropper. The dropper, which is designed as a third party software installer, will request the permission from the victim to install applications from third party sources. This step is needed to overcome Android restrictions for third party applications to abuse Accessibility services.

![scr4](https://www.threatfabric.com/hs-fs/hubfs/Threatfabric/images/blog/Raton/scr4.png?width=274&height=609&name=scr4.png)

![scr5](https://www.threatfabric.com/hs-fs/hubfs/Threatfabric/images/blog/Raton/scr5.png?width=274&height=609&name=scr5.png)

If the victim provides the permission to install other applications, the dropper will create a WebView with a hardcoded URL exporting the installApk function to that web page. The web page can call the installApk function if the victim presses corresponding button.

![scr6](https://www.threatfabric.com/hs-fs/hubfs/Threatfabric/images/blog/Raton/scr6.png?width=1888&height=722&name=scr6.png)

**The JavaScript code with Install button which will call function exported by Dropper.**

**![nf3](https://www.threatfabric.com/hs-fs/hubfs/Threatfabric/images/blog/Raton/nf3.png?width=274&height=609&name=nf3.png)**

**![nf4](https://www.threatfabric.com/hs-fs/hubfs/Threatfabric/images/blog/Raton/nf4.png?width=274&height=609&name=nf4.png)**

**Left: The web page with which calls installApk function. Right: Result of the installApk call.**

The installApk function will create an install session which will open the second stage payload APK file from the assets of the dropper and install that application into the system.

![scr7](https://www.threatfabric.com/hs-fs/hubfs/Threatfabric/images/blog/Raton/scr7.png?width=1780&height=794&name=scr7.png)

When the installation is finished the dropper will execute the payload using hardcoded package name and activity name:

![scr8](https://www.threatfabric.com/hs-fs/hubfs/Threatfabric/images/blog/Raton/scr8.png?width=1938&height=518&name=scr8.png)

After the successful installation, the second stage payload will be executed, and it will immediately ask for two main permissions that are crucial for performing fraud of the device: Accessibility service access and Device Admin privilege. To ask for Accessibility another WebView will be opened with URL which ends up with the path “access”. The page on that URL consist of the code with the button that will trigger exported from the payload function ask Accessibility that will ask victim to provide Accessibility service access.

![scr9](https://www.threatfabric.com/hs-fs/hubfs/Threatfabric/images/blog/Raton/scr9.png?width=1896&height=350&name=scr9.png)

![scr10](https://www.threatfabric.com/hs-fs/hubfs/Threatfabric/images/blog/Raton/scr10.png?width=274&height=609&name=scr10.png)

![scr11](https://www.threatfabric.com/hs-fs/hubfs/Threatfabric/images/blog/Raton/scr11.png?width=274&height=609&name=scr11.png)

On the final step, the trojan will ask for the permissions to read/write contacts and manage system settings. RatOn then will automatically accept corresponding permissions abusing the previously obtained Accessibility access. System settings management permission is needed to ringtone changing.

Starting from this moment, the trojan will start working in backgroun...