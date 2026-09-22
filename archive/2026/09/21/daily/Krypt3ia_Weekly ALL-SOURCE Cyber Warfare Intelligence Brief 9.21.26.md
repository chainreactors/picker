---
title: Weekly ALL-SOURCE Cyber Warfare Intelligence Brief 9.21.26
url: https://krypt3ia.wordpress.com/2026/09/21/weekly-all-source-cyber-warfare-intelligence-brief-9-21-26/
source: Krypt3ia
date: 2026-09-21
fetch_date: 2026-09-22T07:05:06.045698
---

# Weekly ALL-SOURCE Cyber Warfare Intelligence Brief 9.21.26

# [Krypt3ia](https://krypt3ia.wordpress.com/)

(Greek: κρυπτεία / krupteía, from κρυπτός / kruptós, “hidden, secret things”)

## Weekly ALL-SOURCE Cyber Warfare Intelligence Brief 9.21.26

[leave a comment »](https://krypt3ia.wordpress.com/2026/09/21/weekly-all-source-cyber-warfare-intelligence-brief-9-21-26/#respond)

**Reporting period:** September 14–21, 2026
**Assessment cutoff:** September 21, 2026
**Scope:** State and state-aligned cyber operations, APT campaigns, technical intelligence, active exploitation, critical-infrastructure risk, and cyber-enabled intelligence activity.

## Executive assessment

This reporting period produced four developments of immediate intelligence significance.

Iranian MOIS cyber activity is now more tightly connected to physical-world counterintelligence and repression. A joint UK-U.S.-Dutch disclosure on September 15 exposed CHOSEN BRICK, while a parallel FBI technical release substantially expanded analysis of the related HEAVYGRAM malware ecosystem. The campaigns target dissidents, journalists, activists, and other perceived opponents of the Iranian government. Collection includes communications, contacts, email, screenshots, microphone audio, location/pattern-of-life information, and social-media data. The agencies explicitly note that Iranian intelligence has previously plotted kidnapping and lethal operations against perceived enemies abroad. ([FBI](https://www.fbi.gov/investigate/cyber/alerts/2026/iranian-cyber-targeting-of-dissidents-activists-and-journalists))

China-aligned FamousSparrow has concentrated approximately 90% of its observed recent targeting on Latin America and replaced SparrowDoor with a substantially redesigned implant, SparroWocky. Government entities in Argentina, Ecuador, Guatemala, Honduras, Panama, Peru, Puerto Rico, and Venezuela were affected. The geographic concentration is unusual for this actor and plausibly reflects Beijing’s growing intelligence requirements concerning U.S. political and economic competition in the region. ([ESET](https://www.eset.com/us/about/newsroom/research/eset-research-china-aligned-famoussparrow-expands-operations-in-latin-america-targets-governments-with-new-backdoor/))

North Korea’s Contagious Interview ecosystem has been formally attributed and quantified by four governments. The September 18 multinational advisory identifies the actor as WaterPlum, reports at least 30,000 compromised PCs in more than 100 countries, and connects the campaign to theft or compromise involving more than 7,000 cryptocurrency wallets. The operation is important beyond cryptocurrency theft because developer compromise can expose enterprise credentials, source code, cloud environments, and intellectual property. ([Cyber.gov.au](https://www.cyber.gov.au/about-us/view-all-content/alerts-and-advisories/north-korean-waterplum-commonly-referred-to-as-contagious-interview-cyber-actor-group-targeting-it-professionals))

**Two actively exploited vulnerabilities in security infrastructure require immediate defensive attention, although neither currently has a defensible nation-state attribution.** CVE-2026-76461 permits unauthenticated root-level command execution against Cisco Secure Email Gateway simply through malicious email processing. CVE-2026-76460 permits unauthenticated bypass of Cisco Identity Services Engine authentication. Both affect systems positioned at unusually sensitive trust boundaries. ([Cisco](https://www.cisco.com/c/en/us/support/docs/csa/cisco-sa-esa-inj-2bLVGmhX.html?utm_source=chatgpt.com))

The week’s broader intelligence trend is:

> *State cyber operations are increasingly exploiting the boundary between a target’s personal life and its institutional security perimeter.*

Iran targets personal devices after corporate defenses interfere. North Korea approaches developers as private job seekers. Chinese espionage increasingly targets governmental infrastructure in regions where political and commercial intelligence requirements overlap. At the same time, active exploitation is moving directly against identity and email-security infrastructure.

# Iran: CHOSEN BRICK / HEAVYGRAM and MOIS transnational targeting

**Priority:** CRITICAL
**Actor:** Iranian state cyber actors acting for the Ministry of Intelligence and Security
**Malware:** CHOSEN BRICK / HEAVYGRAM ecosystem
**Objective:** Counterintelligence, surveillance, data theft, harassment, potentially physical targeting support
**Attribution confidence:** **High**

On September 15, the UK National Cyber Security Centre, FBI, and Netherlands AIVD jointly disclosed technical details concerning CHOSEN BRICK, malware used by Iranian state actors against dissidents, activists, and journalists in the United Kingdom, United States, Netherlands, and elsewhere. The NCSC says the malware has been used since at least 2025; the FBI’s broader HEAVYGRAM investigation traces related activity to autumn 2023. ([FBI](https://www.fbi.gov/investigate/cyber/alerts/2026/iranian-cyber-targeting-of-dissidents-activists-and-journalists))

The intelligence significance exceeds conventional cyberespionage. The NCSC states that collected information can reveal contacts, location, and pattern of life. Some stolen personal information subsequently appeared on pro-Iranian leak sites. The advisory further notes that Iranian intelligence has previously plotted kidnapping or lethal operations against perceived regime enemies abroad. ([FBI](https://www.fbi.gov/investigate/cyber/alerts/2026/iranian-cyber-targeting-of-dissidents-activists-and-journalists))

This creates a potential chain:

[![](https://krypt3ia.wordpress.com/wp-content/uploads/2026/09/graphviz263.png?w=805)](https://krypt3ia.wordpress.com/wp-content/uploads/2026/09/graphviz263.png)

The last stages are not demonstrated for every CHOSEN BRICK victim, but the intelligence utility is clear.

[FBI Cyber Alerts](https://www.fbi.gov/investigate/cyber/alerts)

## Initial access and social engineering

Operators conduct substantial target research before engagement.

Initial contact occurs through:

* Telegram.
* WhatsApp.
* Other messaging/social platforms.

The actor impersonates trusted acquaintances, organizations, or technical-support personnel and develops rapport before delivering the malicious payload.

Observed disguises include:

* Pictory.
* RunwayML.
* Norton Antivirus.
* Telegram.
* Adobe Flash Player.
* KeePass.
* Fabricated MRI scan results.

One particularly important operational behavior is security-boundary migration. When delivery against a corporate device fails or appears likely to trigger detection, the operator attempts to convince the victim to move the activity onto a personal computer. This is allows a bypass of enterprise security architecture through social engineering.

## Persistence and defense evasion

CHOSEN BRICK commonly persists through:

`HKCU\Software\Microsoft\Windows\CurrentVersion\Run`

Observed values include:

`SMQDService`

`winappx`

The implant can also add exclusions to Microsoft Defender.

Observed mutexes include:

`ytyjyujyu`

`noi672pp434awkc12f`

The FBI observed PowerShell commands invoking:

`Add-MpPreference -ExclusionPath`

bypassing against malware directories and even the victim’s Telegram Desktop download directory.

## Command and control

CHOSEN BRICK communicates using **Telegram** **bots**.

More importantly, each infected machine receives a different Telegram Bot ID. That design limits infrastructure correlation across victims and reduces the consequences of discovering one bot. Recent variants additionally obscure Telegram communications through commercial HTTPS/SOCKS5 proxies.

Relevant services include:

`iproyal[.]com`

`lightningproxies[.]net`

Exfiltration also uses legitimate object-storage services:

`backblazeb2[.]com`

`vultrobjects[.]com`

`storjshare[.]io`

This is another example of the continuing movement toward legitimate-service C2 and exfiltration.

## Collection capabilities

Observed capabilities ...