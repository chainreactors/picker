---
title: Threat Intelligence Report: MANGO SANDSTORM Dindoor / Fakeset Campaign
url: https://krypt3ia.wordpress.com/2026/03/20/threat-intelligence-report-mango-sandstorm-indoor-fakeset-activity/
source: Krypt3ia
date: 2026-03-20
fetch_date: 2026-03-21T04:08:34.062803
---

# Threat Intelligence Report: MANGO SANDSTORM Dindoor / Fakeset Campaign

# [Krypt3ia](https://krypt3ia.wordpress.com/)

(Greek: κρυπτεία / krupteía, from κρυπτός / kruptós, “hidden, secret things”)

## Threat Intelligence Report: MANGO SANDSTORM Dindoor / Fakeset Campaign

[with one comment](https://krypt3ia.wordpress.com/2026/03/20/threat-intelligence-report-mango-sandstorm-indoor-fakeset-activity/#comments)

**Date:** March 2026
**By:** Krypt3ia

### Executive Summary

In early February 2026, the Iranian state-aligned cyber espionage group MuddyWate**r** (also tracked as Seedworm, MERCURY, Static Kitten, MOIST KEYCHAIN, and Mango Sandstorm) conducted a coordinated intrusion campaign targeting a small but strategically significant set of organizations across the United States, Israel, and Canada. The campaign, publicly disclosed in early March 2026, leveraged two malware families Dindoor, a backdoor utilizing the Deno runtime, and Fakeset, a Python-based implant alongside legitimate tooling and cloud infrastructure to establish persistent access and enable data exfiltration.

The available evidence supports a high-confidence assessment that this activity was conducted in support of Iran’s Ministry of Intelligence and Security (MOIS) and is best characterized as a strategic pre-positioning and intelligence collection operation conducted during a period of geopolitical escalation following U.S. and Israeli military actions against Iran. The campaign demonstrates a continued evolution in MuddyWater’s operational model toward low-signature, behavior-driven intrusion techniques, reduced reliance on traditional command-and-control infrastructure, and increased use of legitimate cloud services to obscure activity.

Critically, the absence of detailed atomic indicators such as file hashes, command-and-control domains, and persistence artifacts indicates that the operation is either ongoing, intentionally redacted by reporting entities, or both. This absence itself is analytically significant and suggests a higher-tier intelligence operation in which preserving visibility into adversary activity outweighs the immediate value of broad indicator disclosure.

### Actor Overview

MuddyWater has operated since at least 2017 as a persistent Iranian cyber espionage actor aligned with MOIS. The group has historically targeted government, telecommunications, defense, energy, and financial sectors across the Middle East, Europe, Asia, Africa, and North America. Its tradecraft has consistently combined custom malware with dual-use administrative tools, including PowerShell, remote management frameworks, and credential harvesting utilities.

[![](https://krypt3ia.wordpress.com/wp-content/uploads/2026/03/graphviz-100.png?w=1024)](https://krypt3ia.wordpress.com/wp-content/uploads/2026/03/graphviz-100.png)

Previous campaigns have employed malware families such as PowGoop, Small Sieve, Mori, POWERSTATS, Canopy/Starwhale, and more recently MuddyViper and GhostBackDoor variants. These campaigns typically rely on spearphishing, exploitation of known vulnerabilities, DLL sideloading, and script-based execution to establish initial access and persistence.

### Campaign Overview

The intrusion activity observed between February and March 2026 resulted in confirmed compromises across a narrowly scoped but strategically meaningful set of targets. These included a United States based financial institution, a U.S. airport, a Canadian non-profit organization, and the Israeli subsidiary of a U.S. software company supporting defense and aerospace customers. The selection of these entities reflects a deliberate focus on sectors that provide both intelligence value and potential downstream operational leverage, particularly in the context of heightened geopolitical tensions.

Within these environments, operators associated with MuddyWater established and maintained access through the deployment of the Dindoor backdoor and the Fakeset Python-based implant. These tools enabled persistent footholds while minimizing overt indicators of compromise. In at least one instance, the operators attempted to exfiltrate data using Rclone, directing collected information to a Wasabi cloud storage bucket. Supporting infrastructure tied to malware delivery and staging was also observed leveraging Backblaze B2 storage services.

This pattern of activity is consistent with a broader operational model in which legitimate cloud platforms are repurposed to support intrusion workflows, allowing adversaries to blend malicious traffic with routine enterprise network activity and thereby reduce the likelihood of detection. with a broader shift toward leveraging legitimate infrastructure to minimize detection and complicate attribution.

### Malware and Tooling Analysis

Dindoor constitutes the most notable technical evolution observed in this campaign. Its reliance on the Deno runtime a JavaScript and TypeScript execution environment that remains uncommon within enterprise malware ecosystems reflects a deliberate attempt to bypass detection controls calibrated for more traditional scripting frameworks such as PowerShell and Python. By shifting into a less-monitored execution context, the operators gain both increased operational flexibility and a measurable reduction in the probability of triggering established behavioral analytics.

[![](https://krypt3ia.wordpress.com/wp-content/uploads/2026/03/graphviz-101.png?w=1024)](https://krypt3ia.wordpress.com/wp-content/uploads/2026/03/graphviz-101.png)

Fakeset, by contrast, adheres to a more conventional design as a Python-based backdoor. Its significance is not rooted in novelty, but in attribution. The reuse of code-signing certificates previously associated with MuddyWater malware families, specifically Stagecomp and Darkcomp, creates a direct lineage between legacy and current tooling. This continuity materially strengthens attribution confidence, linking the present operation to established development pipelines and operator tradecraft.

The incorporation of Rclone for data exfiltration further illustrates MuddyWater’s preference for leveraging legitimate, widely deployed utilities to obscure malicious activity. By transmitting exfiltrated data to cloud storage platforms such as Wasabi, the operators eliminate the need for bespoke command-and-control infrastructure. This approach reduces their network signature, complicates detection, and allows malicious traffic to blend seamlessly with routine enterprise cloud usage.

### Targeting Analysis

The observed victimology is limited in scale but exhibits clear intentionality in its composition. Each targeted entity occupies a distinct functional layer within the broader architecture of Western and allied systems, suggesting a selection process driven by systemic value rather than opportunistic access.

The compromised financial institution provides insight into financial flows, customer identities, and inter-organizational relationships. Access of this nature yields both immediate intelligence value and potential leverage for future economic disruption or coercive activity. It enables mapping of capital movement, identification of high-value individuals or entities, and the possibility of downstream financial manipulation.

[![](https://krypt3ia.wordpress.com/wp-content/uploads/2026/03/graphviz-102.png?w=1024)](https://krypt3ia.wordpress.com/wp-content/uploads/2026/03/graphviz-102.png)

The airport represents a critical node within transportation infrastructure. Intrusion into this environment offers access to passenger data, logistics systems, and, in some cases, elements of physical security control. Such positioning supports surveillance objectives, including movement tracking and pattern analysis, while also creating latent options for disruption under escalation conditions.

The Israeli subsidiary of a U.S. defense-aligned software company constitutes the highest-value target within the set. Access at this level introduces potential exposure to defense supply chains, partner ecosyst...