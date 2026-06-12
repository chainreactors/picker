---
title: Threat Intelligence Report: APT10 / FUNKY FLAGPOLE / MenuPass / Stone Panda
url: https://krypt3ia.wordpress.com/2026/06/11/threat-intelligence-report-apt10-funky-flagpole-menupass-stone-panda/
source: Krypt3ia
date: 2026-06-11
fetch_date: 2026-06-12T06:27:30.652863
---

# Threat Intelligence Report: APT10 / FUNKY FLAGPOLE / MenuPass / Stone Panda

# [Krypt3ia](https://krypt3ia.wordpress.com/)

(Greek: κρυπτεία / krupteía, from κρυπτός / kruptós, “hidden, secret things”)

## Threat Intelligence Report: APT10 / FUNKY FLAGPOLE / MenuPass / Stone Panda

[with one comment](https://krypt3ia.wordpress.com/2026/06/11/threat-intelligence-report-apt10-funky-flagpole-menupass-stone-panda/#comments)

### Executive Assessment

APT10 is a long-running China-nexus cyber-espionage actor associated in public U.S. government attribution with China’s Ministry of State Security, specifically the Tianjin State Security Bureau, and with contractors at Huaying Haitai Science and Technology Development Company. Public reporting places APT10 activity as active from at least 2006 or 2009, depending on the source taxonomy, with a strategic focus on intellectual property theft, government intelligence collection, and access through managed service providers. ([Department of Justice](https://www.justice.gov/archives/opa/pr/two-chinese-hackers-associated-ministry-state-security-charged-global-computer-intrusion))

APT10’s defining operational pattern is not a single malware family but an access strategy: compromise organizations with privileged access into other organizations, especially MSPs and IT service providers, then use those trusted relationships to reach downstream targets. Operation Cloud Hopper remains the canonical case study for this model, with APT10 using MSP access to compromise client environments across multiple sectors and geographies. ([Department of Justice](https://www.justice.gov/archives/opa/pr/two-chinese-hackers-associated-ministry-state-security-charged-global-computer-intrusion))

The actor’s historical targeting aligns with Chinese state requirements for economic, defense, technological, diplomatic, and strategic intelligence. Public sources describe targeting of healthcare, defense, aerospace, finance, maritime, biotechnology, energy, government, IT services, manufacturing, mining, telecommunications, satellite technology, and other advanced technology sectors. ([MITRE ATT&CK](https://attack.mitre.org/groups/G0045/))

### Attribution and Naming

APT10 is tracked under multiple names across the CTI ecosystem: MenuPass, Stone Panda, Red Apollo, FUNKY FLAGPOLE, CVNX, POTASSIUM, Cicada, HOGFISH, BRONZE RIVERSIDE, Granite Taurus, and Purple Typhoon, among others. MITRE ATT&CK tracks the group as G0045 / menuPass, while public threat-card repositories also map APT10 to overlapping vendor labels such as Stone Panda, Red Apollo, CVNX, POTASSIUM, Earth Kasha, and Cuckoo Spear. ([MITRE ATT&CK](https://attack.mitre.org/groups/G0045/))

[![](https://krypt3ia.wordpress.com/wp-content/uploads/2026/06/graphviz-151.png?w=1024)](https://krypt3ia.wordpress.com/wp-content/uploads/2026/06/graphviz-151.png)

Attribution confidence for the historic APT10 core intrusion set is high because of the 2018 U.S. Department of Justice indictment naming Zhu Hua and Zhang Shilong, alleging their association with the Tianjin State Security Bureau and Huaying Haitai. Attribution becomes less clean when discussing newer “APT10 umbrella” activity, especially Earth Kasha, LODEINFO, and Cuckoo Spear reporting, where some vendors distinguish related intrusion sets rather than treating them as identical to legacy APT10. ([Department of Justice](https://www.justice.gov/archives/opa/pr/two-chinese-hackers-associated-ministry-state-security-charged-global-computer-intrusion))

### Strategic Intent

APT10’s operational objective is best assessed as strategic espionage. The group has repeatedly targeted intellectual property, confidential business information, government data, defense-related information, and technology-sector secrets. DOJ reporting states that the group targeted more than 45 technology companies and MSPs, while NCSC reporting identifies broad sector targeting for likely intellectual property theft. ([Department of Justice](https://www.justice.gov/archives/opa/pr/two-chinese-hackers-associated-ministry-state-security-charged-global-computer-intrusion))

[![](https://krypt3ia.wordpress.com/wp-content/uploads/2026/06/graphviz-152.png?w=1024)](https://krypt3ia.wordpress.com/wp-content/uploads/2026/06/graphviz-152.png)

The MSP targeting model materially increases strategic value because a single compromise can provide access to multiple client environments. This approach reduces the need for direct intrusion against every final target and creates opportunities for broad collection, credential reuse, lateral movement, and persistent downstream access. ([Department of Justice](https://www.justice.gov/archives/opa/pr/two-chinese-hackers-associated-ministry-state-security-charged-global-computer-intrusion))

### Operational History

From roughly 2006 through 2018, U.S. authorities allege that APT10 conducted global computer intrusion campaigns targeting intellectual property and confidential business information. The indictment specifically describes targeting of MSPs, more than 45 technology companies, and U.S. government agencies, including theft of personally identifiable information relating to more than 100,000 U.S. Navy personnel. ([Department of Justice](https://www.justice.gov/archives/opa/pr/two-chinese-hackers-associated-ministry-state-security-charged-global-computer-intrusion))

In 2016 and 2017, APT10 activity surged globally. FireEye/Mandiant reporting described activity across six continents and targeting of manufacturing companies in India, Japan, and Northern Europe, a South American mining company, and multiple IT service providers. That same reporting identified new or expanded tooling, including HAYMAKER, SNUGRIDE, BUGJUICE, SOGU, and customized QUASARRAT. ([Google Cloud](https://cloud.google.com/blog/topics/threat-intelligence/apt10-menupass-group))

[![](https://krypt3ia.wordpress.com/wp-content/uploads/2026/06/graphviz-153.png?w=1024)](https://krypt3ia.wordpress.com/wp-content/uploads/2026/06/graphviz-153.png)

By late 2018, the UK NCSC assessed that APT10 continued to affect UK organizations across a broad range of sectors and that this activity was likely facilitated by targeting of MSPs and other outsourcing providers. NCSC also noted that infections could spread onward to customers or supply-chain entities, which reinforces the group’s trusted-access operational model.

More recent reporting introduces a related but more nuanced picture. Trend Micro tracks Earth Kasha as related to the “APT10 Umbrella” but not necessarily identical to APT10; its 2024 reporting noted LODEINFO use against Japan, Taiwan, and India, including exploitation of public-facing applications such as SSL-VPN and file-storage services. In March 2025, Trend Micro observed Earth Kasha targeting Taiwan and Japan using spear-phishing, malicious Excel content, ANEL, possible SharpHide use, and NOOPDOOR as a second-stage backdoor. ([www.trendmicro.com](https://www.trendmicro.com/en_us/research/24/k/lodeinfo-campaign-of-earth-kasha.html))

Cybereason’s Cuckoo Spear reporting ties multiple incidents to the APT10 intrusion set and describes long-duration stealthy persistence in Japanese victim networks, with NOOPDOOR and NOOPLDR as important elements of the newer arsenal. This should be treated as moderate-to-high confidence for linkage to the broader APT10 ecosystem, but not as simple evidence that every LODEINFO or Earth Kasha event is legacy APT10. ([Cybereason](https://www.cybereason.com/blog/cuckoo-spear-analyzing-noopdoor))

## Tactics, Techniques, and Procedures

### Initial Access

[![](https://krypt3ia.wordpress.com/wp-content/uploads/2026/06/graphviz-153-1.png?w=1024)](https://krypt3ia.wordpress.com/wp-content/uploads/2026/06/graphviz-153-1.png)

APT10 has used spear-phishing with malicious Office documents, executables disguised as documents, and malicious files requiring user execution. MITRE maps this behavior to T1566.001 Spearphishing Attachment and T1204.002 User Execution: Malicious File. ([MITRE ATT&CK](https://attack.m...