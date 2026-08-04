---
title: What cybersecurity experts are talking about in 2026
url: https://www.virusbulletin.com/blog/2026/08/what-cybersecurity-experts-are-talking-about-2026/
source: Virus Bulletin's blog
date: 2026-08-03
fetch_date: 2026-08-04T05:01:05.559868
---

# What cybersecurity experts are talking about in 2026

[![](/files/4614/4535/7515/logo-big.png)](/)

* [Newsletter](/newsletter/)
* [VB Conference](/conference/)
* [VB Testing](/testing/)
* [Bulletin](/virusbulletin/)
* [Blog](/blog/)

# What cybersecurity experts are talking about in 2026

> Posted by    on   *Aug 3, 2026*

Cybersecurity research in 2026 is revealing a threat landscape shaped by increasingly specialized actors, trusted platforms being turned into attack vectors, and emerging technologies creating entirely new risks. The five topics highlighted below span cyber-mercenary activity, reservation fraud, mobile spyware, targeted espionage, and the security of agentic AI systems. Together, they provide a snapshot of the challenges researchers and defenders are confronting today, along with the investigative approaches being used to understand and address them.

![vb2026_blog_ad.png](/files/cache/a21d20866a4eaa3e1da557724dd54e14_f5704.png)

## Threat intelligence-driven clustering: identifying a new cyber-mercenary intrusion set

by **Maher Yamout & Fatih Şensoy** (Kaspersky)

The Griffith intrusion set represents a persistent threat to the fintech and iGaming sectors, encompassing both the established VB6-based DarkMe malware family and a newly emerged C++-based implant, dubbed GriffithRAT. A tabletop analysis shows how threat intelligence can be used to cluster seemingly disparate malware families into a unified intrusion set. Kaspersky researchers have been investigating this activity since late 2024, observing consistent intrusion techniques – including initial access via Telegram and Skype – and victim profiles.

A comparative analysis of DarkMe and GriffithRAT details their respective TTPs, infrastructure, and code characteristics. A side-by-side comparison of key features – including persistence mechanisms, data exfiltration techniques, and remote access capabilities – shows how overlapping TTPs and consistent targeting establish a clear link despite differences in implementation (VB6 vs. C++), supporting the classification of both malware families as part of the Griffith intrusion set. The analysis of GriffithRAT also examines its inner workings, including a custom-developed remote-desktop controller, keylogger, file-grabber, and persistence components, as well as signed delivery and execution methods. During the investigation, the researchers observed potential bots attempting to influence VirusTotal results through manipulated comments. Their findings indicate that Griffith is a cyber-mercenary-type actor conducting campaigns against users of specific trading platforms. The research offers a practical view of threat attribution methodologies, actionable indicators of compromise for both DarkMe and GriffithRAT, and the evolving tactics of a persistent threat actor.

## From hotel account compromise to guest payment fraud: the reservation hijack attack chain

by **Martin Chlumecký & Luis Corrons** (Gen Digital)

Travel scams are evolving beyond generic phishing into something operationally far more mature. Martin Chlumecký and Luis Corrons describe the Reservation Hijack attack chain: a multi-stage fraud workflow in which attackers first target hospitality businesses, then pivot to real guests using stolen booking context, compromised partner access, and trusted communication channels.

The investigation began with guest-facing payment verification messages tied to real reservations, often containing accurate booking details, stay dates, hotel names, and exact amounts due. Further analysis showed that these lures were only the visible end of a broader intrusion and fraud workflow. In multiple cases, the attack began with phishing aimed at hotel staff or accommodation partners. Once credentials were stolen, attackers abused legitimate hospitality platforms and booking-related workflows to access reservation data, contact upcoming travellers, and, in some cases, host parts of the phishing flow on trusted infrastructure.

The attack chain spans partner-targeted phishing, compromised hotel-side accounts, abuse of platforms such as Booking.com and Cloudbeds, and guest-facing fraud delivered through platform messaging, SMS, WhatsApp, and email.

The research also goes beyond the visible fraud workflow itself. By tracing infrastructure, artefacts, and behavioural overlaps, the team examined the actors and operations behind these campaigns. The findings identify signals suggesting coordination across multiple stages of the activity, outline the limits of current attribution confidence, and highlight the investigative pivots that connected hotel-side compromise with downstream guest fraud.

The work focuses on the mechanics, infrastructure, and defender implications of this scam family, including why traditional phishing indicators become less reliable when fraud arrives wrapped in authentic operational context. It offers a practical view of how these attacks work, how they scale, and where meaningful opportunities for detection and disruption still exist.

## Hunting LANDFALL: from overlooked images to state-linked mobile spyware

by **Itay Cohen** (Palo Alto Networks Unit 42)

In mid-2024, a set of malformed DNG image files carrying fully featured Android spyware was uploaded to VirusTotal from Iraq, Iran, and Morocco. The files remained there, undetected, for over a year. Inside was LANDFALL, a previously unknown commercial-grade Android spyware framework that exploited a zero-day vulnerability in Samsung's image-processing library to achieve zero-click compromise of Galaxy devices, likely through weaponized images delivered via WhatsApp.

Reverse engineering LANDFALL revealed that one of its components calls itself "Bridge Head", a term used by certain private-sector offensive companies for first-stage loaders. The implant it loads delivers full-scale surveillance capabilities. Infrastructure indicators extracted from the binary pointed to aged domains acquired through secondary-market transfers. That infrastructure matched Windows-based intrusions that Unit 42 researchers were independently tracking across government and financial targets in the Middle East. The researchers attribute the activity to a UAE-linked threat actor running parallel Android and Windows campaigns.

The investigation covers the full arc of the LANDFALL research, including details omitted from the public report. It traces Unit 42's hunt for DNG exploit samples following Apple and WhatsApp's disclosure of the exploit chain in August 2025; the reverse engineering of LANDFALL's loader to extract hidden configurations and obtain the full implant; the infrastructure pivots that connected the mobile campaign to Windows-based intrusions across the Middle East and North Africa; and the differential scanner analysis that exposed the actor's entire C2 fleet. The findings also place LANDFALL within the growing ecosystem of mobile exploitation by private-sector offensive companies, alongside recently documented exploit kits such as Coruna and DarkSword.

## Gorbag: Orcs at the border

by **Damien Schaeffer** (ESET)

ESET researchers use the name Gorbag for a newly identified, Russia-aligned cyber-espionage group conducting highly targeted operations against Ukrainian military, law enforcement, defence-industry, and local-government entities since early 2025.

ESET's investigation reveals a focused intelligence-collection mission centred on one-time data theft rather than long-term persistence. Gorbag obtains initial access almost exclusively through spear-phishing emails sent from compromised legitimate accounts, using lure documents themed around military conscription, administrative processes, and drone procurement.

Once opened, these malicious files decode and deploy one of two custom payloads: a PowerShell backdoor or a rapidly evolving custom infostealer designed to extract browser credentials, files, and other sensitive data. The stolen data is then exfiltrated, and the malware deletes itself to hinder forensic investiga...