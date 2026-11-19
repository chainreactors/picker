---
title: Bazuka: The Fraud Framework That Can Do It All
url: https://www.threatfabric.com/blogs/bazuka-the-fraud-framework-that-can-do-it-all
source: Over Security
date: 2026-11-18
fetch_date: 2026-11-19T09:47:16.209596
---

# Bazuka: The Fraud Framework That Can Do It All

[Skip to content](#main-content)

[![threatfabric-logo-light](https://www.threatfabric.com/hubfs/Threatfabric/logos/threatfabric-logo-light.svg "threatfabric-logo-light")](//www.threatfabric.com)

[![threatfabric-logo-light](https://www.threatfabric.com/hubfs/Threatfabric/logos/threatfabric-logo-light.svg "threatfabric-logo-light")](//www.threatfabric.com)

* OUR SOLUTIONS
  + [Mobile Threat Intelligence (MTI)](https://www.threatfabric.com/mti)
  + [Fraud Risk Suite (FRS)](https://www.threatfabric.com/frs)
* REGIONS
  + [Europe](https://www.threatfabric.com/regions/europe)
  + [Asia Pacific](https://www.threatfabric.com/regions/apac)
  + [Middle East & North Africa](https://www.threatfabric.com/regions/mena)
  + [Americas](https://www.threatfabric.com/regions/americas)
* USE CASES
  + [Social Engineering & Scams](https://www.threatfabric.com/usecases/social-engineering-scams)
  + [Account Takeover (ATO)](https://www.threatfabric.com/usecases/ato)
  + [Device Takeover (DTO)](https://www.threatfabric.com/usecases/dto)
  + [Hybrid Fraud](https://www.threatfabric.com/usecases/hybrid-fraud)
* [ARTICLES](https://www.threatfabric.com/blogs)
* RESOURCES
  + [WEBINARS](https://www.threatfabric.com/webinars)
  + [DATASHEETS & REPORTS](https://www.threatfabric.com/resources)
  + [IN THE NEWS](https://www.threatfabric.com/news)
  + [FUSION FIRESIDE](https://www.threatfabric.com/fusion-fireside)
* [Contact](https://www.threatfabric.com/contact)
* [Linkedin](https://www.linkedin.com/company/threatfabric)
* [Twitter](https://twitter.com/threatfabric)
* [Jobs](https://www.threatfabric.com/jobs)
* [Privacy](https://www.threatfabric.com/privacy)
* [Intel/PGP](https://www.threatfabric.com/contact)

[Contact](https://www.threatfabric.com/contact)

Research

## Bazuka: The Fraud Framework That Can Do It All

18 November 2026

![](https://www.threatfabric.com/hubfs/MTI_Bazooka.jpg)

### Jump to

In late October 2026, while investigating an incident involving an NFC card relay application, ThreatFabric's Mobile Threat Intelligence team encountered a new, previously unknown threat: Bazuka. The research unfolded a modular framework for fraudulent operations including LLM integration for victims' management and control.

In this article we explain the architecture of Bazuka framework, its capabilities and provide a sneak peek behind the curtains - control panel of the fraudulent tool.

## Context

It all started with the investigation of yet another NFC-relay banking Trojan. With the exception of the [RatOn case](/blogs/the-rise-of-raton-from-nfc-heists-to-remote-control-and-ats), where a remote access trojan downloaded an NFC relay application, NFC trojans generally have a fairly simple architecture: essentially, there are three components - a reader application, a card emulator application, and a server connecting them. The reader and card emulator applications typically share the same codebase. From an analysis perspective, researchers therefore only need to document a single application and possibly the control panel frontend, if one exists at all.

When we received the first Bazuka sample, this was exactly what we expected: a simple wrapper around yet another open-source project, perhaps with a custom network protocol added at most. However, Bazuka turned out to be an entire malware framework capable of carrying out a wide range of attacks, with the exception of automated payments. Moreover, the framework’s capabilities include LLM integration and ADB bridging - two technologies that arguably represent the cutting edge of mobile cyber threats.

During our research, we managed to uncover most of Bazuka’s components:

* Downloader/Dropper
* Core
* 23 modules

In Bazuka, we encountered an overlay technique we had not seen before: the trojan takes a screenshot of the home screen or lock screen and can display it as an overlay on command.

**Key takeaways**

* **Bazuka is a full malware framework.** A dropper/downloader, a core, and 23 modules cover overlays, keylogging, 2FA and SMS interception, remote control, and crypto-address swapping.
* **ADB bridging is becoming standard in banking trojans.** Bazuka might grant itself permissions covertly; we anticipate that malware in general might use it to deploy modules in a way that allows for surviving even if the host application is removed.
* **LLMs are now part of the criminal toolkit.** AI agents inside the control panel help operators pick out victims of interest and manage infections at scale.
* **Distribution is built to scale, including intention to go via Google Play.** Traffers lure victims with themes like adult content, while the dropper is configured with minimal permissions to potentially help it pass Google Play review.

## Technical analysis

### Distribution

During our analysis of the control panel, we found interface elements for creating accounts for traffers - cybercriminals responsible for attracting victims and getting them to download trojans.

![bzk9](https://www.threatfabric.com/hs-fs/hubfs/Threatfabric/images/blog/bazuka/bzk9.png?width=1752&height=1052&name=bzk9.png)

We also found dropper builder settings that specify minimal permissions in the manifest (without access to the Accessibility Services API).

![bzk10](https://www.threatfabric.com/hs-fs/hubfs/Threatfabric/images/blog/bazuka/bzk10.png?width=1994&height=546&name=bzk10.png)

![bzk13](https://www.threatfabric.com/hs-fs/hubfs/Threatfabric/images/blog/bazuka/bzk13.png?width=1192&height=276&name=bzk13.png)

This is done specifically to make it easier for the resulting APK to (potentially) pass Google Play’s review process. This intention by the authors is proved by other parts of the control panel, while we have not seen any signs of it being a real case. In any way, this suggests at least two distribution channels:

* Through traffers, who create dedicated landing pages and attract victims under a particular pretext (like [IPTV apps](/blogs/iptv-campaigns-target-football-fans-across-multiple-countries)). Eager to access the promised content, victims eventually agree to download the file.
* Through [Google Play](/blogs/anatsa-targets-north-america-uses-proven-mobile-campaign-process). Traffers may also participate in this scheme to bring in more victims, but Google hosts the dropper. And, of course, installing the dropper this way is much easier than downloading it from a traffer’s website.

We were able to document the first distribution channel by finding a file on VirusTotal with the SHA256 hash f046b50166c8229b49839eeebcc7fd14bf3f198e4ec1bfde8a5b271e1407dec5. The original APK filename had helpfully been preserved during upload: **TikTok18-Dropper-tiktok18-premium-1793332000-daf6efe2.apk**.

![bzk12](https://www.threatfabric.com/hs-fs/hubfs/Threatfabric/images/blog/bazuka/bzk12.png?width=1646&height=550&name=bzk12.png)

As the filename shows, the cybercriminals used adult content as a lure: TikTok18+ is currently a very common theme used by various groups.

We identified two variants of the Bazuka framework’s modus operandi:

* A dropper (SHA256: f046b50166c8229b49839eeebcc7fd14bf3f198e4ec1bfde8a5b271e1407dec5) downloaded the next stage, which was a separate APK.
* A downloader (SHA256: 4d572669d6000304a692874c1583021dfdb4f2f113ea487e470f7e4c486e503a) directly downloaded the payload core.

At the first stage, the victim interacts with either a dropper or a downloader.

The dropper asks the victim for permission to install applications from third-party sources, then downloads and installs an APK through the PackageManager session mechanism. In the dropper’s code, the APK being installed is referred to as the stager, and the package launched by the dropper is named com.tiktok.premium.pro.

![bzk35-1](https://www.threatfabric.com/hs-fs/hubfs/Threatfabric/images/blog/bazuka/bzk35-1.png?width=315&height=700&name=bzk35-1.png)![bzk36](https://www.threatfabric.com/hs-fs/hubfs/Threatfabric/images/blog/bazuka/bzk36.png?width=315&height=700&name=bzk36.p...