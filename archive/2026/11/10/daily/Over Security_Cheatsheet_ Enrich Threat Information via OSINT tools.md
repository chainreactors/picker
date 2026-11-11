---
title: Cheatsheet: Enrich Threat Information via OSINT tools
url: https://fareedfauzi.github.io/2024/11/04/Enrich-TI-OSINT.html
source: Over Security
date: 2026-11-10
fetch_date: 2026-11-11T08:35:24.591655
---

# Cheatsheet: Enrich Threat Information via OSINT tools

xml version="1.0" standalone="no"?

[root@fareed:~#](/ "Personal blog for research, education and note purpose.
")

* [Archive](/archive.html)
* [About](/about.html)

# Cheatsheet: Enrich Threat Information via OSINT tools

* [Threat-Intelligence](/archive.html?tag=Threat-Intelligence)

* Nov 04, 2024

Hi hi! So, this is another cheat sheet for security analysts and researchers which often rely on OSINT (Open Source Intelligence) tools to investigate malware samples and gather actionable insights about potential threats. These tools provide information on malware samples, network communications, domain and IP reputation, as well as any related indicators of compromise (IOCs). This guide will help you to get more information for your threat intelligence needs.

# Malware Sample

| Tool | File Hash | Upload | Detection | File Path | File Names | Similarity | Download | Cmd Line | Details | String/Int | Bytes | Relation | Behavior | Network | YARA | New | PCAP | Mem Dump | S’box | MultiAV | Src Code |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| [VirusTotal](https://www.virustotal.com/gui/home/search) | 🟢 | 🟢 | 🟢 | 🟢 | 🟢 | 🟢 | 🟡 | 🟢 | 🟢 | 🟢 | 🟢 | 🟢 | 🟢 | 🟢 | 🟢 | 🟢 | 🟢 | 🟢 | 🟢 | 🟢 | 🔴 |
| [Threatbook](https://s.threatbook.com/) | 🟢 | 🟢 | 🟢 | 🟢 | 🟢 | 🔴 | 🟡 | 🟢 | 🟢 | 🔴 | 🔴 | 🟢 | 🟢 | 🟢 | 🔴 | 🔴 | 🟢 | 🟢 | 🔴 | 🟢 | 🔴 |
| [Tri.age](https://tria.ge/) | 🟢 | 🟢 | 🟢 | 🟢 | 🟢 | 🔴 | 🟢 | 🟢 | 🟢 | 🟢 | 🔴 | 🟢 | 🟢 | 🟢 | 🔴 | 🔴 | 🟢 | 🟢 | 🟢 | 🟢 | 🔴 |
| [Any.Run](https://app.any.run/submissions) | 🟢 | 🟢 | 🟢 | 🟢 | 🟢 | 🔴 | 🟢 | 🟢 | 🟢 | 🟢 | 🟢 | 🟢 | 🟢 | 🟢 | 🔴 | 🔴 | 🟢 | 🟢 | 🟢 | 🔴 | 🔴 |
| [HybridAnalysis](https://www.hybrid-analysis.com/) | 🟢 | 🟢 | 🟢 | 🟢 | 🟢 | 🔴 | 🟡 | 🟢 | 🟢 | 🟢 | 🟢 | 🔴 | 🟢 | 🟢 | 🟢 | 🔴 | 🟢 | 🟢 | 🟢 | 🟢 | 🔴 |
| [Joe Sandbox](https://www.joesandbox.com/) | 🟢 | 🟢 | 🟢 | 🟢 | 🟢 | 🔴 | 🔴 | 🟢 | 🟢 | 🟢 | 🟢 | 🟢 | 🟢 | 🟢 | 🔴 | 🔴 | 🟢 | 🟢 | 🟢 | 🟢 | 🔴 |
| [OpenTIP](https://opentip.kaspersky.com/) | 🟢 | 🟢 | 🟢 | 🟡 | 🟢 | 🔴 | 🔴 | 🟡 | 🟢 | 🟡 | 🔴 | 🔴 | 🟢 | 🟢 | 🔴 | 🔴 | 🟢 | 🟢 | 🟢 | 🔴 | 🔴 |
| [Filescan](https://www.filescan.io/) | 🟢 | 🟢 | 🟢 | 🟢 | 🟢 | 🔴 | 🔴 | 🟢 | 🟢 | 🔴 | 🔴 | 🔴 | 🟢 | 🟢 | 🔴 | 🔴 | 🔴 | 🔴 | 🟢 | 🟢 | 🔴 |
| [Jotti](https://virusscan.jotti.org/en-US/search/hash) | 🟢 | 🟢 | 🟢 | 🟢 | 🟢 | 🔴 | 🔴 | 🔴 | 🔴 | 🔴 | 🔴 | 🔴 | 🔴 | 🔴 | 🔴 | 🔴 | 🔴 | 🔴 | 🔴 | 🟢 | 🔴 |
| [AlienVault](https://otx.alienvault.com/) | 🟢 | 🔴 | 🟢 | 🔴 | 🔴 | 🔴 | 🔴 | 🔴 | 🔴 | 🔴 | 🔴 | 🟢 | 🔴 | 🔴 | 🔴 | 🔴 | 🔴 | 🔴 | 🔴 | 🟢 | 🔴 |
| [ThreatFox](https://threatfox.abuse.ch/browse/) | 🟢 | 🔴 | 🟢 | 🔴 | 🔴 | 🔴 | 🔴 | 🔴 | 🔴 | 🔴 | 🔴 | 🔴 | 🔴 | 🔴 | 🔴 | 🔴 | 🔴 | 🔴 | 🔴 | 🔴 | 🔴 |
| [Talos Intel](https://talosintelligence.com/) | 🟢 | 🔴 | 🟢 | 🔴 | 🔴 | 🔴 | 🔴 | 🔴 | 🔴 | 🔴 | 🔴 | 🔴 | 🔴 | 🔴 | 🔴 | 🔴 | 🔴 | 🔴 | 🔴 | 🔴 | 🔴 |
| [X-Force](https://exchange.xforce.ibmcloud.com/) | 🟢 | 🔴 | 🟢 | 🔴 | 🔴 | 🔴 | 🔴 | 🔴 | 🔴 | 🔴 | 🔴 | 🔴 | 🔴 | 🟢 | 🔴 | 🔴 | 🔴 | 🔴 | 🔴 | 🔴 | 🔴 |
| [Malshare](https://malshare.com/) | 🟢 | 🟢 | 🔴 | 🔴 | 🔴 | 🔴 | 🟢 | 🔴 | 🔴 | 🔴 | 🔴 | 🔴 | 🔴 | 🔴 | 🟢 | 🔴 | 🔴 | 🔴 | 🟢 | 🟢 | 🔴 |
| [ThreatMiner](https://www.threatminer.org/) | 🟢 | 🔴 | 🔴 | 🔴 | 🔴 | 🔴 | 🔴 | 🔴 | 🔴 | 🔴 | 🔴 | 🔴 | 🔴 | 🟢 | 🔴 | 🔴 | 🔴 | 🔴 | 🔴 | 🔴 | 🔴 |
| [Qianxin](https://ti.qianxin.com/) | 🟢 | 🔴 | 🟢 | 🔴 | 🔴 | 🔴 | 🔴 | 🟢 | 🟢 | 🟢 | 🟢 | 🟢 | 🟢 | 🟢 | 🟢 | 🔴 | 🟢 | 🟢 | 🔴 | 🟢 | 🔴 |
| [GH Search](https://github.com/search/advanced) or [grep.app](https://grep.app/) | 🟢 | 🔴 | 🔴 | 🔴 | 🔴 | 🔴 | 🔴 | 🔴 | 🔴 | 🟢 | 🔴 | 🔴 | 🔴 | 🔴 | 🔴 | 🔴 | 🔴 | 🔴 | 🔴 | 🔴 | 🟢 |
| [Google](https://www.google.com/) / [X](https://x.com/search-advanced?lang=en) | 🟢 | 🔴 | 🔴 | 🟢 | 🟢 | 🔴 | 🔴 | 🟢 | 🔴 | 🟢 | 🔴 | 🔴 | 🔴 | 🔴 | 🔴 | 🔴 | 🔴 | 🔴 | 🔴 | 🔴 | 🟢 |
| [MalwareBazaar](https://bazaar.abuse.ch/browse/) | 🟢 | 🟢 | 🟢 | 🔴 | 🔴 | 🔴 | 🔴 | 🔴 | 🔴 | 🔴 | 🔴 | 🔴 | 🔴 | 🔴 | 🟢 | 🔴 | 🔴 | 🔴 | 🔴 | 🔴 | 🔴 |
| [VX](https://virus.exchange/samples) | 🟢 | 🔴 | 🔴 | 🔴 | 🔴 | 🔴 | 🟢 | 🔴 | 🔴 | 🔴 | 🔴 | 🔴 | 🔴 | 🔴 | 🔴 | 🔴 | 🔴 | 🔴 | 🔴 | 🔴 | 🔴 |
| [Wayback](https://web.archive.org/) | 🟢 | 🔴 | 🔴 | 🔴 | 🔴 | 🔴 | 🟢 | 🔴 | 🔴 | 🟢 | 🔴 | 🔴 | 🔴 | 🔴 | 🔴 | 🔴 | 🔴 | 🔴 | 🔴 | 🔴 | 🟢 |

# Network: Domain, IP, Cert

| Tool | Whois | IP | DNS | URLs | Certs | C2 Hunting |
| --- | --- | --- | --- | --- | --- | --- |
| [VirusTotal](https://www.virustotal.com/gui/home/search) | 🟢 | 🟢 | 🟢 | 🟢 | 🟢 | 🟢 |
| [Threatbook](https://s.threatbook.com/) | 🟢 | 🟢 | 🟢 | 🟢 | 🔴 | 🔴 |
| [OpenTIP](https://opentip.kaspersky.com/) | 🟢 | 🟢 | 🟢 | 🟢 | 🔴 | 🔴 |
| [Tri.age](https://tria.ge/) | 🔴 | 🔴 | 🔴 | 🟢 | 🔴 | 🔴 |
| [Any.Run](https://app.any.run/submissions) | 🔴 | 🟢 | 🟢 | 🟢 | 🔴 | 🔴 |
| [HybridAnalysis](https://www.hybrid-analysis.com/) | 🔴 | 🟢 | 🟢 | 🟢 | 🔴 | 🔴 |
| [Joe Sandbox](https://www.joesandbox.com/) | 🔴 | 🟢 | 🟢 | 🟢 | 🔴 | 🔴 |
| [Filescan](https://www.filescan.io/) | 🔴 | 🟢 | 🟢 | 🟢 | 🔴 | 🔴 |
| [AlienVault](https://otx.alienvault.com/) | 🔴 | 🟢 | 🟢 | 🔴 | 🔴 | 🔴 |
| [ThreatFox](https://threatfox.abuse.ch/browse/) | 🔴 | 🟢 | 🟢 | 🟢 | 🔴 | 🔴 |
| [Talos Intel](https://talosintelligence.com/) | 🟢 | 🟢 | 🟢 | 🔴 | 🔴 | 🔴 |
| [X-Force](https://exchange.xforce.ibmcloud.com/) | 🔴 | 🟢 | 🟢 | 🟢 | 🔴 | 🔴 |
| [Pulsedive](https://pulsedive.com/dashboard/) | 🔴 | 🟢 | 🟢 | 🔴 | 🟢 | 🔴 |
| [ThreatMiner](https://www.threatminer.org/) | 🔴 | 🟢 | 🟢 | 🟢 | 🔴 | 🔴 |
| [Qianxin](https://ti.qianxin.com/) | 🔴 | 🟢 | 🟢 | 🟢 | 🟢 | 🔴 |
| [Google](https://www.google.com/) / [X](https://x.com/search-advanced?lang=en) | 🔴 | 🟢 | 🟢 | 🟢 | 🔴 | 🔴 |
| [Censys](https://search.censys.io/) | 🔴 | 🟢 | 🟢 | 🟢 | 🟢 | 🟢 |
| [Shodan](https://www.shodan.io/) | 🔴 | 🟢 | 🟢 | 🟢 | 🟢 | 🟢 |
| [FOFA](https://en.fofa.info/) | 🔴 | 🟢 | 🟢 | 🔴 | 🟢 | 🟢 |
| [Validin](https://app.validin.com/) | 🟢 | 🟢 | 🟢 | 🔴 | 🟢 | 🟢 |
| [DNSlytics](https://search.dnslytics.com/) | 🟢 | 🟢 | 🟢 | 🔴 | 🔴 | 🔴 |
| [RiskIQ](https://community.riskiq.com/home) | 🟢 | 🟢 | 🟢 | 🔴 | 🟢 | 🔴 |
| [Driftnet](https://driftnet.io/) | 🟢 | 🟢 | 🟢 | 🟢 | 🟢 | 🔴 |
| [SilentPush](https://explore.silentpush.com/) | 🟢 | 🟢 | 🟢 | 🟢 | 🔴 | 🔴 |
| [BinaryEdge](https://app.binaryedge.io/services/query) | 🔴 | 🟢 | 🔴 | 🔴 | 🔴 | 🟢 |
| [Hunt.io](https://app.hunt.io/) | 🔴 | 🟢 | 🔴 | 🔴 | 🔴 | 🟢 |
| [ZoomEye](https://www.zoomeye.hk/) | 🔴 | 🟢 | 🟢 | 🔴 | 🟢 | 🔴 |
| [crt.sh](https://crt.sh/) | 🔴 | 🔴 | 🟢 | 🔴 | 🟢 | 🔴 |
| [GreyNoise](https://viz.greynoise.io/) | 🔴 | 🟢 | 🔴 | 🔴 | 🔴 | 🔴 |
| [URLScan](https://urlscan.io/) | 🔴 | 🔴 | 🔴 | 🟢 | 🔴 | 🔴 |
| [Wayback Machine](https://web.archive.org/) | 🔴 | 🔴 | 🔴 | 🟢 | 🔴 | 🔴 |
| [URLHaus](https://urlhaus.abuse.ch/browse/) | 🔴 | 🔴 | 🔴 | 🟢 | 🔴 | 🔴 |
| [Criminal IP](https://www.criminalip.io/) | 🔴 | 🟢 | 🟢 | 🔴 | 🔴 | 🔴 |
| [APIVoid](https://www.apivoid.com/tools/ip-reputation-check/) | 🔴 | 🟢 | 🔴 | 🔴 | 🔴 | 🔴 |
| [SSLBlacklist](https://sslbl.abuse.ch/) | 🔴 | 🔴 | 🔴 | 🔴 | 🟢 | 🔴 |
| [FeodoTracker](https://feodotracker.abuse.ch/browse/) | 🔴 | 🟢 | 🔴 | 🔴 | 🔴 | 🔴 |
| [DNSDumpster](https://dnsdumpster.com/) | 🔴 | 🔴 | 🟢 | 🔴 | 🔴 | 🔴 |
| [AbuseIPDB](https://www.abuseipdb.com/) | 🔴 | 🟢 | 🔴 | 🔴 | 🔴 | 🔴 |
| [Gordon](https://cybergordon.com/) | 🔴 | 🟢 | 🟢 | 🔴 | 🔴 | 🔴 |

# Ransomware

| Tool | Data Leak | Ransomware | Stealer | Credential |
| --- | --- | --- | --- | --- |
| [Twitter](https://x.com/search-advanced?lang=en) | 🟢 | 🟢 | 🟢 | 🟢 |
| [Ransomwatch](https://ransomwatch.telemetry.ltd/#/recentposts) | 🔴 | 🟢 | 🔴 | 🔴 |
| [RansomLook](https://www.ransomlook.io/recent) | 🔴 | 🟢 | 🔴 | 🔴 |
| [Ransom-db](https://www.ransom-db.com/real-time-updates) | 🔴 | 🟢 | 🔴 | 🔴 |
| [Ransomware.live](https://www.ransomware.live/#/recent) | 🔴 | 🟢 | 🔴 | 🔴 |

# Email Data

| Tool | Email Sender | Email Object | Email Header |
| --- | --- | --- | --- |
| [Google Toolbox](https://toolbox.googleapps.com/apps/messageheader/) | 🔴 | 🔴 | 🟢 |
| [thatsthem](https://thatsthem.com/) | 🟢 | 🔴 | 🔴 |
| [Qianxin](https://ti.qianxin.com/) | 🟢 | 🔴 | 🔴 |
| [OSINT Industries](https://app.osint.industries/) | 🟢 | 🔴 | 🔴 |

PREVIOUS[Dive into PEB Walk in Malware Analysis](/2024/07/13/PEB-Walk.html)

NEXT[Cheatsheet: Threat Attribution in Threat Intelligence](/2025/08/16/Threat-Attribution.html)

© root@fareed:~# 2021

Search

Cancel