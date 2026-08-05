---
title: What the P.E.T. guide teaches digital forensics investigators
url: https://andreafortuna.org/2026/08/03/pet-guide-forensics/
source: Instapaper: Unread
date: 2026-08-04
fetch_date: 2026-08-05T04:59:25.969395
---

# What the P.E.T. guide teaches digital forensics investigators

[Andrea Fortuna](/)
[ ]

[About](/about/)[Search](/search/)

Tools

[DFIR Toolkit](https://dfir-toolkit.andreafortuna.org)
[OSINT Toolkit](https://osint-toolkit.andreafortuna.org)

# What the P.E.T. guide teaches digital forensics investigators

Aug 3, 2026

by [Andrea Fortuna](/about/)

There is an old principle in counterintelligence that I find equally applicable to digital forensics: to understand how someone covers their tracks, you first need to understand exactly how they think about covering tracks. It is easy to spend years developing extraction techniques, learning artifact locations, and mastering mobile acquisition workflows. It is less common to sit down and read the documentation written for the people you are investigating.

![cover](/assets/2026/pet-guide-forensics.jpg)

The [P.E.T. Guide](https://itsgoingdown.org/wp-content/uploads/2022/10/petguide_read.pdf) (Peer-to-peer, Encrypted, Tor) is one of those documents. Published in 2022, it was written with an explicit political orientation and for purposes entirely separate from law enforcement. I have no interest in that context here. What interests me is that it is a technically detailed, surprisingly well-structured manual describing exactly how a subject attempting to minimize their digital footprint would approach communication security. That makes it required reading for anyone doing DFIR work in environments where privacy-aware subjects are the norm rather than the exception.

## In brief

* The P.E.T. Guide covers encrypted messaging, Tor integration, P2P architectures, and metadata minimization — all topics with direct forensic relevance.
* Different platforms expose very different metadata profiles: Signal centralizes some server-side data, while apps like Briar and Cwtch route everything through Tor with no central point of contact.
* Understanding which data is concealed and which inevitably leaks is the foundation of any realistic acquisition and attribution strategy.
* The guide’s analysis of threat models maps almost directly onto what digital forensics investigators need to think about when designing investigative approaches.
* A 2026 update titled “Signal Problems” (published on AnarchistNews) refreshes the guide’s recommendations, introducing SimpleX Chat and revising assessments of Briar and Cwtch.
* The combination of original guide and recent update provides an unusually clear picture of the current private communications landscape.

## The forensic value of a privacy manual

The guide’s framing is adversarial toward surveillance, which means it approaches the question of metadata with unusual rigor. Rather than reassuring its readers that a given app is “secure,” it asks specifically: what does this service know about you, what does your phone retain, what can an adversary with access to the network observe, and what happens if the platform itself is compromised or compelled to produce records?

These are, almost verbatim, the questions a forensic investigator should ask when evaluating what evidence is recoverable from a given communications platform. The P.E.T. Guide treats **metadata** as a first-class concern rather than an afterthought. It distinguishes between message content (which end-to-end encryption generally protects well) and communications metadata: who contacted whom, when, how frequently, from which network location, using which device identifiers. This distinction is critical in the field. As I noted in my analysis of [Signal notifications and FBI forensic access](https://andreafortuna.org/2026/04/11/signal-fbi-iphone-notifications-forensics/), encryption protects the channel; it does not necessarily protect the metadata layer or what the operating system does with content once it arrives.

The guide also addresses **operational security failures** with a candor that vendors rarely match. It explains that using an encrypted messenger from a device tied to your real identity, on a network that logs connection times, largely defeats the purpose of the encryption. This is precisely the kind of behavioral residue that investigators find most useful.

## Messaging platforms through a forensic lens

The guide dedicates substantial space to analyzing specific messaging platforms, and this section is where it becomes most directly useful for investigators. It examines **Signal**, **Molly** (a hardened Signal fork for Android), **Ricochet Refresh**, **Telegram**, **Briar**, and **Cwtch** through the lens of centralization, metadata exposure, Tor integration, and threat model fit.

**Signal** receives a nuanced assessment. The guide acknowledges its strong cryptographic foundation while noting that it requires a phone number for registration (linking identity), that Signal’s servers log contact discovery and account creation timestamps, and that sealed sender only partially addresses metadata leakage. From a forensic perspective, this is significant: Signal leaves a more recoverable artifact trail than its reputation suggests, something I have explored in depth in the context of [Telegram forensics](https://andreafortuna.org/2026/05/25/telegram-forensics/) and broader messaging analysis. The earlier post on [why WhatsApp and Telegram messages are not really private](https://andreafortuna.org/2019/08/12/why-whatsapp-and-telegram-messages-are-not-really-private/) covers some of the same ground and remains relevant.

**Telegram** receives a more critical treatment. The guide correctly identifies that Telegram’s default mode does not use end-to-end encryption, that Secret Chats (which do) leave no server-side copy but are device-specific, and that Telegram’s cloud-based architecture makes it a rich source for investigators who obtain legal process against the platform. On that front, the forensic picture has shifted considerably as Telegram has become more cooperative with law enforcement requests since 2024.

**Briar** and **Cwtch** represent the other end of the spectrum. Both route all traffic through Tor and operate on a pure peer-to-peer model with no central server. Briar can even fall back to Bluetooth and Wi-Fi direct connections, functioning as a mesh network in environments without internet access. From a forensic standpoint, this architecture is genuinely challenging: there is no service provider to compel, no server logs, and contact graph information exists only on devices. Recovery depends entirely on physical or logical access to the endpoint, where the forensic analysis of the device itself becomes the only viable path. The [iOS forensics without jailbreak guide](https://andreafortuna.org/2026/02/04/ios-forensics-without-jailbreak-a-practical-guide-to-modern-mobile-evidence-acquisition/) and the [iOS Lockdown Mode forensics post](https://andreafortuna.org/2026/03/29/ios-lockdown-mode-forensics/) are relevant here, since subjects using these tools are often also using hardened device configurations.

## Tor, P2P architectures, and what they mean for attribution

The guide’s treatment of **Tor** is technically sound and directly relevant to understanding investigative constraints. It explains the onion routing model accurately: traffic enters the network through a guard node, passes through a middle relay, and exits through an exit node, with each hop knowing only its neighbors in the chain. Content is encrypted in layers. The exit node can see the destination but not the source; the guard node can see the source but not the destination. No single node has the full picture.

For investigators, the practical implication is that traffic analysis attacks against Tor require global network observation capabilities that most actors do not have. What remains exploitable at the endpoint level is considerable, however. Browser fingerprinting, application-layer identifiers, timing correlations, and operational security failures (logging into a real account while using Tor, for example) have been responsible for most documented Tor de-anonymization cases. ...