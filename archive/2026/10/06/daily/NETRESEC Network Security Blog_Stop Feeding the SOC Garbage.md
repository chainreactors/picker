---
title: Stop Feeding the SOC Garbage
url: https://www.netresec.com/?page=Blog&month=2026-10&post=Stop-Feeding-the-SOC-Garbage
source: NETRESEC Network Security Blog
date: 2026-10-06
fetch_date: 2026-10-07T07:55:22.367856
---

# Stop Feeding the SOC Garbage

Experts in network security monitoring and network forensics
[![Netresec](/images/Netresec_Logo_550x140.png)](https://www.netresec.com/)

[NETRESEC](/?page=Home)|

[Products](/?page=Products)|

[Training](/?page=Training)|

[Resources](/?page=Resources)|

[Blog](/?page=Blog)|

[About Netresec](/?page=AboutNetresec)

[NETRESEC](/)
»
[Blog](/?page=Blog)

Erik Hjelmvik

,

Tuesday, 06 October 2026 06:30:00 (UTC/GMT)

## [Stop Feeding the SOC Garbage](/?page=Blog&month=2026-10&post=Stop-Feeding-the-SOC-Garbage)

Security operations teams are handling increasing volumes of network events and security alerts. Whether those alerts are reviewed by human analysts, processed by AI, or handled through a combination of both, the result depends on the quality of the underlying detections.

![Feeding the SOC Garbage](https://media.netresec.com/images/SOC_garbage_2000x2000.webp)

No SOC can investigate an intrusion that never generated an alert. And if the incoming alerts are incomplete, noisy, or biased toward known attack patterns, the result is inefficient investigations and missed malicious activity.

Simply spending more on AI tokens will not solve this problem. AI can prioritize, correlate, and summarize the alerts it receives, but it cannot recover activity that was never detected or reliably compensate for systematically noisy inputs. Detection quality still depends on input quality. Or in other words, Garbage-In-Garbage-Out ([GIGO](https://en.wikipedia.org/wiki/Garbage_in%2C_garbage_out)) still applies.

**False positives and false negatives**

False positives are a constant pain for many SOCs. They waste analyst time, cause alert fatigue, and may lead teams to disable or ignore useful detections. So-called [benign alerts](https://blog.gigamon.com/2022/08/05/revisiting-the-idea-of-the-false-positive/) are almost just as bad. This image [shared by @cR0w](https://infosec.exchange/%40cR0w/117355609332532834) humorously captures the analyst experience.

[![Skeleton doing a squat with the text: My body is a machine that turns shitty EDR alerts into Closed - False Positive.](https://media.netresec.com/images/EDR-alerts-into-false-positives_1148x1371.webp)](https://infosec.exchange/%40cR0w/117355609332532834)

While false positives waste time, false negatives may waste nothing at all. That's an even bigger problem!

**A different way to identify protocols**

Traditional intrusion detection systems (IDS) are valuable, but they depend on static signatures and protocol-specific rules. Creating a reliable signature can require expertise and large PCAP datasets to test for false positives. Some protocols are especially difficult to detect with such techniques. They may be proprietary, undocumented, encrypted, obfuscated, or designed to resemble benign traffic.

![FlowCarp](https://media.netresec.com/images/FlowCarp_2000x2000.webp)

[FlowCarp](https://flowcarp.com/) takes a different approach. It identifies application-layer protocols by analyzing statistical characteristics of network traffic and comparing them with models of known protocols. This does not require a formal protocol specification. A protocol model can be created from example traffic, including traffic from a protocol that is difficult to express as a conventional IDS signature.

FlowCarp can identify both legitimate and malicious protocols, including protocols used for malware command-and-control (C2) traffic. It can also generate alerts and integrate with existing monitoring workflows.

**A complementary detection method**

FlowCarp is not intended to replace a traditional IDS. One of its key features is that it provides another view of network activity.

A traditional IDS signature may stop matching when an attacker changes an indicator. A parser may not support an undocumented protocol. A port-based rule may fail when traffic moves to an unexpected port. Because it identifies protocols based on statistical traffic characteristics, FlowCarp can provide an alternative when static signatures and protocol parsers are unavailable, insufficient, or unreliable.

The reverse can also be true: a conventional signature may be the better detector in a particular situation. Using different detection methods together can make monitoring more resilient.

This additional perspective is useful in any SOC. These alerts can provide additional investigative leads for analysts and additional evidence for automated triage systems. In both cases, the benefit depends on receiving alerts that are relevant and accurate.

**Better detection benefits every SOC**

The goal should not simply be to maximize the number of alerts a SOC can process. It should be to produce alerts that cover meaningful activity without overwhelming the people and systems responsible for investigating them.

Whether a SOC relies on human analysts, AI, or a combination of both, the foundation is the same: high-quality inputs lead to better detections. Before asking a SOC to handle higher alert volumes, it is worth asking whether those alerts provide an accurate view of the network and what might still be missing.

Posted by Erik Hjelmvik on Tuesday, 06 October 2026 06:30:00 (UTC/GMT)

Tags:
#[FlowCarp](/?page=Blog&tag=FlowCarp)​

Short URL:
<https://netresec.com/?b=26A42c0>

### Recent Posts

» [Stop Feeding the SOC Garbage](/?page=Blog&month=2026-10&post=Stop-Feeding-the-SOC-Garbage)

» [Unmasking Malware Families](/?page=Blog&month=2026-09&post=Unmasking-Malware-Families)

» [PolarProxy 2.0.2 Released](/?page=Blog&month=2026-09&post=PolarProxy-2-0-2-Released)

» [OT Networks Still Need Monitoring](/?page=Blog&month=2026-08&post=OT-Networks-Still-Need-Monitoring)

» [CNCMachineRMS C2 Protocol](/?page=Blog&month=2026-08&post=CNCMachineRMS-C2-Protocol)

» [PureLogs, PureRAT and misleading zgRAT](/?page=Blog&month=2026-07&post=PureLogs-PureRAT-and-misleading-zgRAT)

» [Ping32 RMM and ValleyRAT](/?page=Blog&month=2026-06&post=Ping32-RMM-and-ValleyRAT)

» [Maximizing IOC Impact](/?page=Blog&month=2026-06&post=Maximizing-IOC-Impact)

### Blog Archive

» [2026 Blog Posts](?page=Blog&year=2026)

» [2025 Blog Posts](?page=Blog&year=2025)

» [2024 Blog Posts](?page=Blog&year=2024)

» [2023 Blog Posts](?page=Blog&year=2023)

» [2022 Blog Posts](?page=Blog&year=2022)

» [2021 Blog Posts](?page=Blog&year=2021)

» [2020 Blog Posts](?page=Blog&year=2020)

» [2019 Blog Posts](?page=Blog&year=2019)

» [2018 Blog Posts](?page=Blog&year=2018)

» [2017 Blog Posts](?page=Blog&year=2017)

» [2016 Blog Posts](?page=Blog&year=2016)

» [2015 Blog Posts](?page=Blog&year=2015)

» [2014 Blog Posts](?page=Blog&year=2014)

» [2013 Blog Posts](?page=Blog&year=2013)

» [2012 Blog Posts](?page=Blog&year=2012)

» [2011 Blog Posts](?page=Blog&year=2011)

[List all blog posts](/?page=Blog&blogPostList=true)

[Video blog posts](/?page=Video)

### News Feeds

» [FeedBurner](https://feeds.feedburner.com/Netresec-Network-Security-Blog)

» [RSS Feed](https://www.netresec.com/rss.ashx)

![X / twitter](/images/X_100x90.png)

𝕏:
[@netresec](https://x.com/netresec)

---

![Bluesky](/images/bluesky_100x88.png)

Bluesky:
[@netresec.com](https://bsky.app/profile/netresec.com)

---

![Mastodon](/images/mastodon_100x107.png)

Mastodon:
[@netresec@infosec.exchange](https://infosec.exchange/%40netresec)

𝙽𝙴𝚃𝚁𝙴𝚂𝙴𝙲 |
[Contact](/?page=AboutNetresec)
|
[Privacy](/?page=Privacy)
|
[Mastodon](https://infosec.exchange/%40netresec)
|
[Bluesky](https://bsky.app/profile/netresec.com)
|
[𝕏](https://x.com/netresec)
|
[RSS](https://www.netresec.com/rss.ashx)