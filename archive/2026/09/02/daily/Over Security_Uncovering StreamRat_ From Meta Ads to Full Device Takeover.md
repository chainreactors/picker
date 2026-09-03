---
title: Uncovering StreamRat: From Meta Ads to Full Device Takeover
url: https://www.threatfabric.com/blogs/from-meta-ads-to-full-device-takeover-uncovering-streamrat
source: Over Security
date: 2026-09-02
fetch_date: 2026-09-03T07:02:50.780954
---

# Uncovering StreamRat: From Meta Ads to Full Device Takeover

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
Global
Europe

## Uncovering StreamRat: From Meta Ads to Full Device Takeover

02 September 2026

![](https://www.threatfabric.com/hubfs/MTI_StreamRat.jpg)

### Jump to

ThreatFabric researchers have uncovered StreamRat, a new Android banking trojan promoted to Spanish-speaking users through Meta and TikTok advertisements impersonating a free TV-streaming service, with the campaign reaching approximately 570,000 potential victims. Following a two-stage installation, StreamRat abuses Accessibility Services and MediaProjection to provide operators with near-complete control over infected devices, combining VNC and hidden-screen control, UI-tree collection, keylogging, credential-stealing overlays, internet and screen-blocking capabilities.

In late July 2026, while monitoring advertisers within the Meta ecosystem that were using [TV streaming-themed lures](/blogs/iptv-campaigns-target-football-fans-across-multiple-countries) already familiar to us, we identified a campaign named **“Steamtv Esp.”** The threat actor had deployed a phishing website targeting Spanish-speaking users.

If a victim proceeded with the file download, the payload was retrieved from a GitHub repository belonging to the same user who had previously distributed the **Mirax** trojan. The downloaded file was a dropper closely resembling the one previously used to deploy the Mirax payload. In this case, however, the final payload was a previously unseen trojan, which we named **StreamRat**.

In this report, we provide details on StreamRat’s distribution mechanisms and technical capabilities.

Key takeaways from this report:

* The vast majority of observed victims were located in Spain.
* The threat actor has used at least three different financial malware families, including **GodFather, Mirax, and StreamRat**.
* Based on the code of the trojan’s control panel, **StreamRat appears to have been developed as a Malware-as-a-Service (MaaS) offering**.
* The **StreamRat dropper** implements an Internet-blocking mechanism - a relatively new TTP that has already been observed across multiple droppers and appears to be gaining popularity.

## Modus Operandi

The infection process consists of several stages.

### Stage 1: Preparing the advertising campaign in the Meta ecosystem as well as in TikTok.

At this stage, the cybercriminals deploy a website that will later be promoted through their advertising campaigns. They also purchase Meta ads themed around streaming services. One such campaign reached approximately **570,000 Meta users** between **11 June 2026 and 3 July 2026**.

![StreamRat1](https://www.threatfabric.com/hs-fs/hubfs/Threatfabric/images/blog/2026-StreamRat/pngs/StreamRat1.png?width=3450&height=1941&name=StreamRat1.png)

Based on the advertising campaign data, the primary targets were Meta users in Spain. We cannot determine which specific Meta platform was the main focus of the campaign; however, the same advertising banners were likely displayed on both **Facebook and Instagram**.

### Stage 2: Redirecting the victim to the malicious website

If a victim interacts with the social media lure and visits the specially crafted website, they are required to complete several additional steps before downloading StreamRat.

![StreamRat2](https://www.threatfabric.com/hs-fs/hubfs/Threatfabric/images/blog/2026-StreamRat/pngs/StreamRat2.png?width=3450&height=1941&name=StreamRat2.png)

First, the website uses JavaScript to determine whether the victim is using an Android device.

If another operating system is detected, the website displays an error and prevents the download by simply hiding the download button.

![StreamRat3](https://www.threatfabric.com/hs-fs/hubfs/Threatfabric/images/blog/2026-StreamRat/pngs/StreamRat3.png?width=3450&height=1941&name=StreamRat3.png)

 If the device is identified as Android, however, an application download button becomes available. When the victim clicks it, they are redirected to another page named "r1edmi.html". At the same time, the page script calls a backend API that sends a notification via a Telegram.

![StreamRat4](https://www.threatfabric.com/hs-fs/hubfs/Threatfabric/images/blog/2026-StreamRat/pngs/StreamRat4.png?width=3450&height=1941&name=StreamRat4.png)

The purpose of r1edmi.html is to determine which application the victim used to open the lure website: **Instagram, TikTok, Facebook, or a standalone browser**. The instructions shown to the victim depend on this result. By default, the page displays a six-step instruction for Chrome.

Unsurprisingly, the instructions guide the victim through enabling the installation of applications from unknown sources in Chrome and granting access to **Accessibility Services**.

![StreamRat5](https://www.threatfabric.com/hs-fs/hubfs/Threatfabric/images/blog/2026-StreamRat/pngs/StreamRat5.png?width=3450&height=1941&name=StreamRat5.png)

While displaying these instructions, the webpage also queries the backend API for the currently active malware download URL.

An interesting detail is that the distribution website has its own dedicated control panel.

![StreamRat6](https://www.threatfabric.com/hs-fs/hubfs/Threatfabric/images/blog/2026-StreamRat/pngs/StreamRat6.png?width=3450&height=1941&name=StreamRat6.png)

Once the URL is received, the script instructs the victim’s browser to download a file named app.apk.

### Stage 3: Dropper execution

Once the victim downloads and launches the APK, the dropper interface is displayed.

![str3](https://www.threatfabric.com/hs-fs/hubfs/Threatfabric/images/blog/2026-StreamRat/pngs/str3.png?width=313&height=696&name=str3.png)One notable aspect of the dropper is that its interface consists of several interconnected HTML pages containing embedded JavaScript:

* **Index.html**
* **Set\_launcher.html**
* **Vpn\_required.html**

Each page is loaded at a specific stage of the infection process.

The first page, set\_launcher.html, checks whether the dropper is configured as the device’s default Home application. If it is not, the victim is prompted to set the dropper as the default launcher. From that point onward, whenever the victim presses the **HOME** button, they are redirected back to the dropper interface.

The dropper then loads its m...