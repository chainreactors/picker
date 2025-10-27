---
title: Essential Tools for Gathering and Analyzing IOCs
url: https://andreafortuna.org/2023/03/13/essential-tools-for-gathering-and-analyzing-iocs
source: Instapaper: Unread
date: 2023-03-16
fetch_date: 2025-10-04T09:48:07.674071
---

# Essential Tools for Gathering and Analyzing IOCs

[Andrea Fortuna](/)
[ ]

[About](/about/)[Rss](/feed.xml)

# Essential Tools for Gathering and Analyzing IOCs

Mar 13, 2023

In Cyber Threat Intelligence, the collection and analysis of Indicators of Compromise (IOCs) is critical because they provide valuable information that can help organisations detect and respond to cyber threats more effectively.

IOCs are pieces of evidence or artefacts that indicate the presence of a threat, such as a virus, malware or malicious activity, within a system or network. Examples of IOCs include IP addresses, domain names, file hashes, URLs and email addresses. By collecting and analysing these IOCs, CTI analysts can identify patterns, trends and characteristics of cyber threats, which can help in the development of defensive measures.

Harvesting IOCs involves collecting data from a variety of sources, such as threat intelligence feeds, open source intelligence, and malware repositories. Once collected, these IOCs are analysed to determine their relevance, the severity of the threat, and the potential impact on the organisation’s systems and networks.

In the following list, I have compiled some useful tools for harvesting and analysing IOCs, ranging from open source tools to commercial solutions.

### [AbuseHelper](https://github.com/abusesa/abusehelper)

An open-source framework for receiving and redistributing abuse feeds and threat intel.

### [AlienVault Open Threat Exchange](https://otx.alienvault.com/)

Share and collaborate in developing Threat Intelligence.

### [Combine](https://github.com/mlsecproject/combine)

Tool to gather Threat Intelligence indicators from publicly available sources.

### [Fileintel](https://github.com/keithjjones/fileintel)

Pull intelligence per file hash. The output is in CSV format and sent to STDOUT so the data can be saved or piped into another program.

### [Hostintel](https://github.com/keithjjones/hostintel)

Pull intelligence per host. Like Fileintel, the output is in CSV format and sent to STDOUT so the data can be saved or piped into another program.

### [IntelMQ](https://github.com/certtools/intelmq)

![Logo_Intel_MQ.svg](https://github.com/certtools/intelmq/raw/develop/docs/_static/Logo_Intel_MQ.svg)

A tool for CERTs for processing incident data using a message queue.IntelMQ can be used for - automated incident handling - situational awareness - automated notifications - as data collector for other tools - etc.

### [IOC Editor](https://fireeye.market/apps/S7cWpi9W)

A free editor from Fireeyefor XML IOC files, that allows:

* Manipulation of the logical structures that define the IOC
* Application of meta-information to IOCs, including detailed descriptions or arbitrary labels
* Conversion of IOCs into XPath filters
* Management of lists of “terms” used within IOCs

### [iocextract](https://github.com/InQuest/python-iocextract)

Advanced Indicator of Compromise (IOC) extractor, Python library and command-line tool: extracts URLs, IP addresses, MD5/SHA hashes, email addresses, and YARA rules from text corpora. It includes some encoded and “defanged” IOCs in the output, and optionally decodes/refangs them.

### [ioc\_writer](https://github.com/mandiant/ioc_writer)

Python library for working with OpenIOC objects, from Mandiant.

### [MalPipe](https://github.com/silascutler/MalPipe)

Malware/IOC ingestion and processing engine, that enriches collected data.

At this time, the following feeds are supported:

* VirusTotal ([https://www.virustotal.com](https://www.virustotal.com/))
* MalShare (<https://malshare.com/>)
* BambenekFeeds (osint.bambenekconsulting.com/feeds/)
* FeodoBlockList ([https://feodotracker.abuse.ch](https://feodotracker.abuse.ch/))
* Malc0deIPList (<http://malc0de.com/>)
* NoThinkIPFeeds ([www.nothink.org/](http://www.nothink.org/))
* OpenPhishURLs ([https://openphish.com](https://openphish.com/))
* TorNodes ([https://torstatus.blutmagie.de](https://torstatus.blutmagie.de/))

### [MISP](https://www.misp-project.org/)

![misp-logo.png](https://github.com/MISP/MISP/raw/2.4/INSTALL/logos/misp-logo.png?raw=true)

Malware Information Sharing Platform curated by The MISP Project. The objective of MISP is to foster the sharing of structured information within the security community and abroad. MISP provides functionalities to support the exchange of information but also the consumption of said information by Network Intrusion Detection Systems (NIDS), LIDS but also log analysis tools, SIEMs.

### [Pulsedive](https://pulsedive.com/)

Free, community-driven threat intelligence platform collecting IOCs from open-source feeds.

### [Microsoft Defender Threat Intelligence](https://ti.defender.microsoft.com/)

Formerly RiskIQ: research, connect, tag and share IPs and domains.

### [threataggregator](https://github.com/jpsenior/threataggregator)

Aggregates security threats from a number of sources, and outputs to Syslog CEF, Snort Signatures, Iptables rules, hosts.deny, etc.

### [ThreatIngestor](https://github.com/InQuest/ThreatIngestor)

![threatingest](https://camo.githubusercontent.com/afdfbc8e1d21fbdd17a1f971b985b0bfa2ba94aa2277909b59ae410e66dc0305/68747470733a2f2f696e71756573742e72656164746865646f63732e696f2f70726f6a656374732f746872656174696e676573746f722f656e2f6c61746573742f5f696d616765732f6d65726d6169642d6d756c7469706c652d6f70657261746f72732e706e67)

Build automated threat intel pipelines sourcing from Twitter, RSS, GitHub, and more.

### [ThreatTracker](https://github.com/michael-yip/ThreatTracker)

A Python script to monitor and generate alerts based on IOCs indexed by a set of Google Custom Search Engines.

### [TIQ-test](https://github.com/mlsecproject/tiq-test)

Data visualization and statistical analysis of Threat Intelligence feeds.

Please enable JavaScript to view the [comments powered by Disqus.](https://disqus.com/?ref_noscript)

## Andrea Fortuna

* Andrea Fortuna
* andrea@andreafortuna.org

* [andreafortuna](https://github.com/andreafortuna)
* [andreafortunaig](https://instagram.com/andreafortunaig)
* [andrea-fortuna](https://www.linkedin.com/in/andrea-fortuna)
* [andrea](https://social.privacytools.click/%40andrea)
* [andreafortunatw](https://www.twitter.com/andreafortunatw)

Cybersecurity expert, software developer, experienced digital forensic analyst, musician