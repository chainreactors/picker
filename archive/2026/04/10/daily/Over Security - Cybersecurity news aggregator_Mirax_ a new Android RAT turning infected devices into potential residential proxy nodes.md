---
title: Mirax: a new Android RAT turning infected devices into potential residential proxy nodes
url: https://www.cleafy.com/cleafy-labs/mirax-a-new-android-rat-turning-infected-devices-into-potential-residential-proxy-nodes
source: Over Security - Cybersecurity news aggregator
date: 2026-04-10
fetch_date: 2026-04-11T04:22:33.539726
---

# Mirax: a new Android RAT turning infected devices into potential residential proxy nodes

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

Android

RAT

# Mirax: a new Android RAT turning infected devices into potential residential proxy nodes

###### Published:

###### 10/4/26

[![](https://cdn.prod.website-files.com/6020129a813fe0c8f1e8053e/67d2edc94c8ed8232523cefe_Cleafy-Labs.avif)](/labs)

Download the PDF version

### Download your PDF  guide to TeaBot

Get your free copy to your inbox now

Download PDF Version

### Key Points

* **New Maas spreading:** Mirax has emerged as a sophisticated Malware-as-a-Service (MaaS) offering, specifically targeting Android devices across Europe. It is actively marketed and distributed through underground malware forums. At the time of writing, Cleafy Threat Intelligence Team has seen **multiple campaigns targeting Spanish-speaking countries** and reaching over 200.000 accounts through Meta advertisements.
* **Remote Access functionalities & Dynamic HTML Overlays:** Mirax integrates advanced Remote Access Trojan (RAT) capabilities, allowing threat actors to fully interact with compromised devices in real time. This includes executing commands, navigating the user interface, and monitoring activity. A key feature is its use of dynamically fetched HTML overlays from its command-and-control (C2) infrastructure, which are rendered over legitimate applications.
* **Expanding RAT with Residential Proxy:** Beyond traditional RAT behavior, Mirax enhances its operational value by turning infected devices into residential proxy nodes. Leveraging SOCKS5 protocol support and Yamux multiplexing, it establishes persistent proxy channels that allow attackers to route their traffic through the victim’s real IP address. This capability enables operators to bypass geolocation-based restrictions, evade fraud detection systems, and conduct malicious activities (such as account takeovers or transaction fraud) with increased anonymity and legitimacy.
* **Keylogging &  Keyguard exfiltration:** Mirax incorporates comprehensive surveillance features, including continuous keylogging to capture all user input across applications. In addition, it gathers detailed information about the device’s keyguard (lock screen), including PIN length, pattern structure, and biometric usage.

### Executive Summary

**Mirax** is a newly identified Android Remote Access Trojan (RAT) and banking malware that has rapidly gained traction within the cybercriminal ecosystem. Publicly promoted on underground forums since December 19, 2025, it has been actively monitored by the Cleafy Threat Intelligence team since March 2026, when **multiple campaigns targeting primarily Spanish-speaking regions were observed**. Unlike typical MaaS offerings, **Mirax is distributed through a highly controlled and exclusive model**, limited to a small number of affiliates. Access appears to be prioritized for Russian-speaking actors with established reputations in underground communities, indicating a deliberate effort to maintain operational security and campaign effectiveness.

From a capability standpoint, Mirax represents a significant evolution beyond traditional Android banking trojans. While retaining core RAT functionalities, it introduces a more structured, commercially driven “business model” featuring tiered subscription plans and ongoing feature development. **One of its most notable innovations is the integration of SOCKS-based residential proxy functionality** directly into the malware. This allows infected devices to be repurposed as proxy nodes, enabling threat actors to route malicious traffic through legitimate residential IP addresses and thereby evade geolocation restrictions and fraud detection mechanisms.

This convergence of RAT and proxy capabilities reflects a broader shift in the threat landscape. While residential proxy abuse has historically been associated with compromised IoT devices and low-cost Android hardware such as smart TVs, **Mirax marks a new phase by embedding this functionality within a full-featured banking trojan**. This approach not only increases the monetization potential of each infection but also expands the operational scope of attackers, who can now leverage compromised devices for both direct financial fraud and as infrastructure for wider cybercriminal activities.

### How Mirax is Distributed

Mirax distribution consists of multiple stages that reveal an interesting trend followed by other affiliates and threat actors. The dropper pages are promoted through Meta Advertisement. The victims are lured to click ads appearing on their social media applications (Facebook, Instagram, Messenger, Threads, …) and to download the malicious dropper. All the URLs implement multiple checks to verify that they are accessed from mobile devices, to prevent automated scans from revealing their nature. The droppers are hosted using GitHub releases, with different backup links and daily package updates. Upon successful installation, the dropper unpacks itself and installs the malicious payload. It leverages commercial-grade obfuscation via Golden Encryption (aka GoldCrypt) and starts operating via WebSockets.

![](https://cdn.prod.website-files.com/60201cc2b6249b0358f70f8a/69d8fd675c8c38ef9aabba5c_a7fe50a3.png)

Figure 1 - Mirax attack chain overview

The delivery websites are promoted through Meta Ads (Facebook and Instagram). This distribution vector has become a common choice for Android banking trojans, enabling threat actors to reach a large audience quickly and with less effort. Furthermore, the choice of decoy, an illegal sports streaming application, reveals a clear understanding of the target demographic: since these apps are not available on the Google Play Store, users are already conditioned to sideload APKs from unknown sources, which makes social engineering much easier.

The dropper is distributed via phishing websites claiming to offer IPTV application services. Downloads are restricted to mobile devices, enforced by checking specific HTTP headers and parameters.

![](https://cdn.prod.website-files.com/60201cc2b6249b0358f70f8a/69d8fd675c8c38ef9aabba5f_7e0a2889.png)

Figure 2 - Device checks on installation

The analysis showed that the **ADs had collectively reached more than 200,000 accounts**, as reported in the next Figure:

![](https://cdn.prod.website-files.com/60201cc2b6249b0358f70f8a/69d8fd675c8c38ef9aabba62_f73b46f6.png)

Figure 3 - Meta Advertisement reach

One interesting aspect of this delivery campaign is the **abuse of GitHub for hosting the dropper applications**. The affiliates leverage the Releases page to distribute and update their applications. Notably, new updates are pushed to pre-existing releases rather than creating new ones, likely as an ev...