---
title: Optimizing IOC Retention Time
url: https://www.netresec.com/?page=Blog&month=2025-11&post=Optimizing-IOC-Retention-Time
source: NETRESEC Network Security Blog
date: 2025-11-06
fetch_date: 2025-11-07T03:11:43.282388
---

# Optimizing IOC Retention Time

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

Thursday, 06 November 2025 12:05:00 (UTC/GMT)

## [Optimizing IOC Retention Time](/?page=Blog&month=2025-11&post=Optimizing-IOC-Retention-Time)

Are you importing indicators of compromise (IOC) in the form of domain names and IP addresses into your [SIEM](https://en.wikipedia.org/wiki/Security_information_and_event_management), [NDR](https://en.wikipedia.org/wiki/Network_detection_and_response) or [IDS](https://en.wikipedia.org/wiki/Intrusion_detection_system)? If so, have you considered for how long you should keep looking for those IOCs?

An [IoT botnet study](https://pure.tudelft.nl/ws/portalfiles/portal/147286793/30_577.pdf) from 2022 found that 90% of C2 servers had a lifetime of less than 5 days and 93% had a lifetime shorter than 14 days. Additionally, a recent [writeup from Censys](https://censys.com/blog/2025-state-of-the-internet-c2-time-to-live) concludes that the median lifespan of Cobalt Strike C2 servers is 5 days. Both these studies indicate that IP and domain name indicators are short lived, yet many organizations cling on to old IOCs for much longer than so. Monitoring for too many old indicators not only costs money, it can even inhibit detection of real intrusions.

**Pyramid of Pain**

David J. Bianco's [pyramid of pain](https://detect-respond.blogspot.com/2013/03/the-pyramid-of-pain.html) illustrates how much pain is caused to an adversary if their malicious actions are hindered by defenders blocking various indicators.

![IOC Pyramid of Pain](https://media.netresec.com/images/IOC-Pyramid-of-Pain_2048x1123.webp)

Indicators at the bottom of the pyramid are trivial for an adversary to replace, which is why IOCs like hashes and IP addresses tend to be very short lived. The indicator types close to the pyramid’s base are also the ones that typically are shared in threat intel feeds.

It would be nice to detect adversaries with indicators higher up in David’s pyramid of pain, but it is often difficult to craft reliable detection mechanisms for such indicators. The simple indicators at the bottom, like domains, IPs and hashes, are on the other hand very exact and practical for us defenders to work with. So in this sense the pyramid of pain applies to defenders as well, where indicators at the bottom are trivial to use and the [complexity increases](https://www.rfc-editor.org/rfc/rfc9424.html#name-ioc-types-and-the-pyramid-o) as we go further up. In this sense the Pyramid of Pain can also be viewed as the “Pyramid of Detection Complexity”.

**Chasing Ghosts**

Many IOCs are “dead” even before you get them. This IOC delay is particularly noticeable when looking at writeups of malware and botnets published by security researchers, in which the IPs and domain names shared in their IOC lists often haven’t been used for several weeks by the time the report gets published. It’s understandable that it takes time to reverse engineer a new piece of malware, compose a blog post and to get the writeup approved for publishing. Nevertheless, those old IOCs often get picked up, redistributed, and used as if they were fresh indicators. Recorded Future [observed](https://www.recordedfuture.com/research/2022-adversary-infrastructure-report) a 33-day average lead time between when their scans found a C2 server and when it is reported in other sources. Thirty-three days! Only a very small fraction of those C2 servers can be expected to still be active by the time those IOCs are shared by various threat intel providers. All the other C2 servers are dead indicators, or “Ghost IOCs” as I like to call them. Attempting to detect such Ghost IOCs in live network traffic is a waste of resources.

**IOC Costs**

Most network intrusion detection systems (IDS) only support a certain number of active rules or signatures, which effectively limits the number of IOCs you can look for. Other products charge the user based on the number of monitored IOCs. As an example, Tostes et al.’s paper covering the [shelf life of an IOC](https://arxiv.org/abs/2307.16852) says that Azure Sentinel Threat Intelligence charges $2.46 per ingested GB. This type of direct cost can then be compared to the cost of not alerting on a known malicious IOC that has timed out. Simplified comparisons like this typically result in poor and misleading guidance to keep using IOCs for much longer than necessary, often hundreds of days or even perpetually.

One important factor that is missing in such simplified reasoning is the cost for false positive alerts, which increases significantly when monitoring for ghost IOCs. An IP address that is being used as a botnet C2 server one week might be running a totally legitimate service another week. The risk for false positives is smaller for domain names compared to IP addresses, but hacked websites is one example where domain names often cause false positive alerts as well. One common cause for such domain IOC false positives is the frequent misuse of hacked websites for malware distribution. Such illicit use is often detected and rectified within a couple of days, in particular when this happens to a website belonging to a medium to large sized company or organization. Alerting on DNS based IOCs for a long time after last confirmed sighting therefore also increases the risk for false positives.

![The boy who cried wolf](https://media.netresec.com/images/boy-cry-wolf_1024x1024.webp)

The cost of false positives is difficult to estimate, as it involves the time analysts spend in vain trying to verify if a particular alert was a false positive or not. Too many false positives can also cause [alert fatigue](https://www.ibm.com/think/topics/alert-fatigue) or [alarm burnout](https://www.usenix.org/system/files/sec22-alahmadi.pdf), much in the same way as in Aesop’s ancient fable about the boy who cried wolf.

This implies that monitoring for too many old IOCs actually increases the risk of actual sightings of malicious indicators being missed or overlooked due to alert fatigue. This line of thinking might seem contradictory and is often overlooked in research related to the shelf life of indicators. I would personally prefer to use an IOC scoring model that aims to [reduce the number of false positives](https://rp.os3.nl/2019-2020/p55/report.pdf) rather than using one that attempts to minimize the direct cost of IOC monitoring.

**Pruning old IOCs**

[RFC 9424](https://datatracker.ietf.org/doc/rfc9424/) states that “IOCs should be removed from detection at the end of their life to reduce the likelihood of false positives”. But how do we know if an IOC has reached end of life?

I’ve previously mentioned that researchers have found that most C2 servers are used for 5 days or less. The optimal number of days to monitor for an IOC depends on several factors, but in general we’re talking about a couple of weeks since last sighting for an IP address and maybe a little longer for domain names. The obvious exception here is [DGA](https://en.wikipedia.org/wiki/Domain_generation_algorithm) and [RDGA](https://blogs.infoblox.com/threat-intelligence/rdgas-the-new-face-of-dgas/) domains, which typically have a lifetime of just 24 hours.

The research paper [Taxonomy driven indicator scoring in MISP threat intelligence platforms](https://arxiv.org/pdf/1902.03914) introduces an interesting concept, where a score is calculated for each IOC based on factors like confidence, age and decay rate. The IOC can be considered dead or expired when the score reaches zero or if it goes below a specified threshold. The following graph from the MISP paper shows an example of how the score for an IP address IOC could decay ...