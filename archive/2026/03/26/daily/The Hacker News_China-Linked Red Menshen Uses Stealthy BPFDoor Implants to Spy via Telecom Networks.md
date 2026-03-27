---
title: China-Linked Red Menshen Uses Stealthy BPFDoor Implants to Spy via Telecom Networks
url: https://thehackernews.com/2026/03/china-linked-red-menshen-uses-stealthy.html
source: The Hacker News
date: 2026-03-26
fetch_date: 2026-03-27T04:33:40.078595
---

# China-Linked Red Menshen Uses Stealthy BPFDoor Implants to Spy via Telecom Networks

#1 Trusted Cybersecurity News Platform

Followed by 5.20+ million[**](https://twitter.com/thehackersnews)
[**](https://www.linkedin.com/company/thehackernews/)
[**](https://www.facebook.com/thehackernews)

[![The Hacker News Logo](data:image/png;base64...)](/)

**

**

[** Subscribe – Get Latest News](#email-outer)

* [** Home](/)
* [** Newsletter](#email-outer)
* [** Webinars](/p/upcoming-hacker-news-webinars.html)

* [Home](/)
* [Threat Intelligence](/search/label/Threat%20Intelligence)
* [Vulnerabilities](/search/label/Vulnerability)
* [Cyber Attacks](/search/label/Cyber%20Attack)
* [Webinars](/p/upcoming-hacker-news-webinars.html)
* [Expert Insights](https://thehackernews.com/expert-insights/)
* [Awards](https://awards.thehackernews.com/)

**

**

**

Resources

* [Webinars](/p/upcoming-hacker-news-webinars.html)
* [Awards](https://awards.thehackernews.com/)
* [Free eBooks](https://thehackernews.tradepub.com)

About Site

* [About THN](/p/about-us.html)
* [Jobs](/p/careers-technical-writer-designer-and.html)
* [Advertise with us](/p/advertising-with-hacker-news.html)

Contact/Tip Us

[**

Reach out to get featured—contact us to send your exclusive story idea, research, hacks, or ask us a question or leave a comment/feedback!](/p/submit-news.html)

Follow Us On Social Media

[**](https://www.facebook.com/thehackernews)
[**](https://twitter.com/thehackersnews)
[**](https://www.linkedin.com/company/thehackernews/)
[**](https://www.youtube.com/c/thehackernews?sub_confirmation=1)
[**](https://www.instagram.com/thehackernews/)

[** RSS Feeds](https://feeds.feedburner.com/TheHackersNews)
[** Email Alerts](#email-outer)

[![Security Service Edge](https://blogger.googleusercontent.com/img/b/R29vZ2xl/AVvXsEguiZ85S7494GyqhFt9uP48C8ggEnb3bp9Qmsdv4LOYjNWfa98MKx17Dk7o1nJrEV3ai3edIGIgwt6oO5iJMmYLcyu6PojcvJnO4IfLhVK2dzGKFyEroFjKQhnp2hd5Cc6G4CynJRfb55aclnGwj7rse9jMncn_vu_tFqQZtHZH3Sb5dMXwRKN-kSVYUMzD/s1700-e365/ai-d.png)](https://thehackernews.uk/wiz-ai-security-d)

# [China-Linked Red Menshen Uses Stealthy BPFDoor Implants to Spy via Telecom Networks](https://thehackernews.com/2026/03/china-linked-red-menshen-uses-stealthy.html)

**Ravie Lakshmanan**Mar 26, 2026Cyber Espionage / Network Security

[![](data:image/png;base64...)](https://blogger.googleusercontent.com/img/b/R29vZ2xl/AVvXsEgDsXRdaBMsOY-JUezvB02i5xzt_pSMJYGGGmt3ujh5C7VDZ7YLODicjiwDHF0vR9Y6P7XfPJJ-sIzu3aElQOfOExYn15O9tjCrOubY531cg1hKVN7U1aGCq5avhsEBdxu0qCTuwgXQEHS4mkHExgUQbsR8iU2CS7fBZAlTyXlD9o0hmU0oJ8jCip_fok4G/s1700-e365/tower-hack.jpg)

A long-term and ongoing campaign attributed to a China-nexus threat actor has embedded itself in telecom networks to conduct espionage against government networks.

The strategic positioning activity, which involves implanting and maintaining stealthy access mechanisms within critical environments, has been attributed to **[Red Menshen](https://thehackernews.com/2025/04/new-bpfdoor-controller-enables-stealthy.html)**, a threat cluster that's also tracked as Earth Bluecrow, DecisiveArchitect, and Red Dev 18. The group has a track record of striking telecom providers across the Middle East and Asia since at least 2021.

Rapid7 described the covert access mechanisms as "some of the stealthiest digital sleeper cells" ever encountered in telecommunications networks.

The campaign is characterized by the use of kernel-level implants, passive backdoors, credential-harvesting utilities, and cross-platform command frameworks, giving the threat actor the ability to persistently inhabit networks of interest. One of the most recognized tools in its malware arsenal is a Linux backdoor called [BPFDoor](https://thehackernews.com/2023/05/new-variant-of-linux-backdoor-bpfdoor.html).

"Unlike conventional malware, BPFdoor does not expose listening ports or maintain visible command-and-control channels," Rapid7 Labs [said](https://www.rapid7.com/blog/post/tr-bpfdoor-telecom-networks-sleeper-cells-threat-research-report/) in a report shared with The Hacker News. "Instead, it abuses Berkeley Packet Filter (BPF) functionality to inspect network traffic directly inside the kernel, activating only when it receives a specifically crafted trigger packet."

[![Cybersecurity](data:image/png;base64...)](https://thehackernews.uk/not-fast-enough-d)

"There is no persistent listener or obvious beaconing. The result is a hidden trapdoor embedded within the operating system itself."

The attack chains begin with the threat actor targeting internet-facing infrastructure and exposed edge services, such as VPN appliances, firewalls, and web-facing platforms associated with Ivanti, Cisco, Juniper Networks, Fortinet, VMware, Palo Alto Networks, and Apache Struts, to obtain initial access.

Upon gaining a successful foothold, Linux-compatible beacon frameworks such as [CrossC2](https://thehackernews.com/2025/08/researchers-warn-crossc2-expands-cobalt.html) are deployed to facilitate post-exploitation activities. Also dropped are [Sliver](https://thehackernews.com/2023/01/threat-actors-turn-to-sliver-as-open.html), [TinyShell](https://thehackernews.com/2024/11/china-backed-hackers-leverage-sigtran.html) (a [Unix backdoor](https://sect.iij.ad.jp/en/2025/12/tinyshell-based-malware-from-unc5325/)), keyloggers, and brute-force utilities to facilitate credential harvesting and lateral movement.

Central to Red Menshen's operations, however, is BPFDoor. It features two distinct components: One is a passive backdoor deployed on the compromised Linux system to inspect incoming traffic for a predefined "magic" packet by installing a BPF filter and spawning a remote shell upon receiving such a packet. The other integral part of the framework is a controller that's administered by the attacker and is responsible for sending the specially formatted packets.

[![](data:image/png;base64...)](https://blogger.googleusercontent.com/img/b/R29vZ2xl/AVvXsEjmoA13bxEiCxXQ7y_80JUhUROwreEEINlqTG7ZRBmxMfc2c4S7U2NrXrzPugxEh67ru-jEasyPTdb_ps9-jAOEm6LkntH94JxZKQJmlzP68U9Bx2vMHfyOqPzbEnkgqMBVJ9ktwY7vaTsGuCffooZNT5WV3JI8jgzyjGalQavApfPsLzfgyQZYyyo1JbES/s1700-e365/BPFdoor.png)

"The controller is also designed to operate within the victim’s environment itself," Rapid7 explained. "In this mode, it can masquerade as legitimate system processes and trigger additional implants across internal hosts by sending activation packets or by opening a local listener to receive shell connections, effectively enabling controlled lateral movement between compromised systems."

What's more, certain BPFDoor artifacts have been found to support the Stream Control Transmission Protocol ([SCTP](https://en.wikipedia.org/wiki/Stream_Control_Transmission_Protocol)), potentially enabling the adversary to monitor telecom-native protocols and gain visibility into subscriber behavior and location, and even track individuals of interest.

These aspects demonstrate that the functionality of BPFdoor goes beyond a stealthy Linux backdoor. "BPFdoor functions as an access layer embedded within the telecom backbone, providing long-term, low-noise visibility into critical network operations," the security vendor added.

It doesn't end there. A previously undocumented variant of BPFdoor incorporates architectural changes to make it more evasive and stay undetected for prolonged periods in modern enterprise and telecom environments. These include concealing the trigger packet within seemingly legitimate HTTPS traffic and introducing a novel parsing mechanism that ensures the string "9999" appears at a fixed byte offset within the request.

[![Cybersecurity](data:image/png;base64...)](https://thehackernews.uk/ciso-risk-comm-cert-dr-d)

This camouflage, in turn, allows the magic packet to stay hidden inside HTTPS traffic and avoid causing shifts to the position of data inside the request, and allows the implant to always check for the marker at a specific byte offset and, if it's present, interpret it as the activation command.

The newly discovered s...