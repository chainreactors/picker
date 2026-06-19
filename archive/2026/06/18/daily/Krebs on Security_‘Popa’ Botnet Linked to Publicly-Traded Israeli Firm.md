---
title: ‘Popa’ Botnet Linked to Publicly-Traded Israeli Firm
url: https://krebsonsecurity.com/2026/06/popa-botnet-linked-to-publicly-traded-israeli-firm/
source: Krebs on Security
date: 2026-06-18
fetch_date: 2026-06-19T07:09:18.776680
---

# ‘Popa’ Botnet Linked to Publicly-Traded Israeli Firm

Advertisement

[![](/b-knowbe4/48.jpg)](https://www.knowbe4.com/training-humans-ai-agents?utm_source=krebs&utm_medium=display&utm_campaign=traininghumansandai&utm_content=bannerai)

Advertisement

[![](/b-keeper/18.png)](https://www.keepersecurity.com/free-data-breach-scan.html?utm_source=Krebs&utm_medium=display+ad&utm_campaign=Krebs_ads)

[![Krebs on Security](https://krebsonsecurity.com/wp-content/uploads/2021/03/kos-27-03-2021.jpg)](https://krebsonsecurity.com/ "Krebs on Security")

[Skip to content](#content "Skip to content")

* [Home](https://krebsonsecurity.com/)
* [About the Author](https://krebsonsecurity.com/about/)
* [Advertising/Speaking](https://krebsonsecurity.com/cpm/)

# ‘Popa’ Botnet Linked to Publicly-Traded Israeli Firm

June 18, 2026

[3 Comments](https://krebsonsecurity.com/2026/06/popa-botnet-linked-to-publicly-traded-israeli-firm/#comments)

For the past four years, a sprawling Android-based botnet called **Popa** has forced millions of consumer TV boxes to relay Internet traffic linked to advertising fraud, account takeovers, and mass data-scraping efforts. This week, researchers from multiple security firms concluded that the Popa botnet is linked to **NetNut**, a “residential proxy” provider operated by the publicly-traded Israeli firm **Alarum Technologies Ltd** [NASDAQ: ALAR].

![Malicious streaming devices sold online that enroll the user's home Internet address in a residential proxy service. Image: Synthient. Pictured are 8 different TV boxes, including the X96 Mini Box, stick, and other no-name brands.](https://krebsonsecurity.com/wp-content/uploads/2026/06/tvboxes-proxy.png)

Malicious streaming devices sold online that enroll the user’s home Internet address in a residential proxy service. Image: HUMAN Security.

Popa is a massive botnet, but by all accounts it is unlike traditional botnets that enlist compromised systems in destructive activities, such as coordinating huge distributed denial-of-service attacks. Rather, Popa appears designed with a singular purpose: Implementing a persistent communications layer capable of registering a device, maintaining long-lived encrypted connections, and opening communication tunnels on demand.

Experts say Popa is a plugin component associated with the **Vo1d** botnet, a large-scale malware campaign targeting unofficial Android-based TV boxes. These devices, which are marketed under thousands of brand names and model numbers and broadly available for purchase at top e-commerce destinations, all advertise the ability to stream hundreds of subscription video services for an up front one-time fee.

But as the FBI and security industry experts have warned repeatedly, these streaming boxes typically [bundle or come pre-installed with software](https://krebsonsecurity.com/2025/11/is-your-android-tv-streaming-box-part-of-a-botnet/) that turns the user’s TV into a “[residential proxy](https://synthient.com/blog/who-are-the-victims-of-residential-proxies)” — allowing anyone to route their Internet traffic through that device for as long as it remains plugged into a wall socket and connected to a local network. More concerning, some of these proxy networks do little to stop malicious customers from communicating with and even compromising systems on the local network of the unsuspecting device owner.

The first clues about Popa’s origins came in [a 2025 report](https://blog.xlab.qianxin.com/long-live-the-vo1d_botnet/) from the Chinese security company **XLAB**, which flagged at least nine domain names that were used to register and direct the activities of compromised devices. In [a report](https://www.qurium.org/forensics/finding-popa/) released today, the security firm **Qurium** described how it stumbled on some of those same domains while investigating a series of disruptive and expensive data scraping events targeting the company’s hosted organizations in May 2026, in which the scraping activity was scattered evenly across more than 1.4 million Internet addresses.

Qurium said it found several dozen domains used to control Popa that were all hosted in lockstep across multiple Internet addresses over time, including **gmslb[.]net**, safernetwork[.]io, tera-home[.]com, and **ninjatech[.]io**. Digging deeper, Qurium discovered gmslb[.]net was referenced in dozens of pirated or modded video content streaming apps, such as **CRICFy**, **DooFlix**, **Sprozfy**, **RTS Tv**, **Flixoid**, **CyberFlix**, **Rapid Streamz**, **TvMob** and **HD/OceanStreams**.

Qurium’s report notes that most of the domains long used to control the Popa botnet were [seized or dismantled in July 2025](https://blog.google/innovation-and-ai/technology/safety-security/google-taking-legal-action-against-the-badbox-20-botnet/), after **Google**, **HUMAN Security** and **Trend Micro** teamed up to disrupt **Badbox 2.0**, a botnet that is closely associated with Vo1d. Qurium said that immediately after that disruption, several dozen new domains were registered to serve as controllers for the Popa botnet, but that one of those control domains was not new: **ninjatech[.]io**.

Ninjatech is a company founded by **Moishi Kramer**, whose [LinkedIn profile](https://www.linkedin.com/in/moishikramer/) says he is vice president of research and development at NetNut. That resume credits Kramer for helping NetNut to build from the “ground up,” “designing the architecture,” and “scaling the NetNut” before the company was acquired by Alarum Technologies. A self-created listing at the job board **F6S** [references Kramer](https://www.f6s.com/company/ninjatech.io) as the sole owner of the Ninjatech domain (a screen capture of it is pictured below).

![](https://krebsonsecurity.com/wp-content/uploads/2026/06/f6s-kramer-1.png)

Image: F6S.com.

Responding via email, Mr. Kramer said Ninjatech ceased operations approximately five years ago, when the company sold a software development kit (SDK) called Popa that was designed to use a small portion of a device’s bandwidth and to run only after the host application obtained user consent.

“That code was sold and licensed to third parties including resellers years ago,” Kramer said. “Once software is distributed that way, the original developer has no control over how others later modify, rebrand, or deploy it.”

Kramer said neither he nor NetNut builds, operates or maintains the infrastructure being described as Popa, nor does he control the Ninjatech domain.

“I didn’t register the June 2025 domains you mention, and I don’t know who did,” he continued. “I have no control over, or visibility into, that infrastructure. I can only tell you it isn’t operated by me or by NetNut.”

But in [a separate Popa research report](https://synthient.com/blog/popa-from-sourcing-to-distribution) released today, the proxy-tracking company **Synthient** said a recent analysis of the Popa SDK revealed outbound traffic clearly associated with NetNut.

“The research team assesses with high confidence that devices running Popa forward traffic from Netnut clients,” Synthient wrote. “This proves without a shadow of a doubt that Popa actively continues to be used by NetNut as part of their proxy pool.”

![](https://krebsonsecurity.com/wp-content/uploads/2026/06/synthient-flixview.png)

Synthient’s platform receiving outbound traffic from Popa. Image: Synthient.com.

Alarum Technologies, NetNut’s Tel Aviv-based parent company, said the reports by Synthient and Qurium contained “demonstrably inaccurate assertions and flawed deductions rather than verified facts.” Alarum shared a statement saying they reject the basic characterization of the SDKs and technologies discussed in the reports as a “botnet.”

“The SDKs at issue are designed to facilitate bandwidth-sharing functionality and do not transform user devices into malware-controlled systems or otherwise compromise the devices on which they operate,” the statement reads. “Netnut operates a commercial proxy network and maintains policies, procedures, and technolog...