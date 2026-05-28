---
title: Introducing EvidenceForge: Synthetic security logs that don’t look (as) fake
url: https://blog.talosintelligence.com/introducing-evidenceforge-synthetic-security-logs-that-dont-look-as-fake/
source: Over Security
date: 2026-05-27
fetch_date: 2026-05-28T06:03:02.299229
---

# Introducing EvidenceForge: Synthetic security logs that don’t look (as) fake

[Blog](/)

[ ]

* [Intelligence Center](https://talosintelligence.com/reputation)

  [ ]

  + [# Intelligence Center](https://talosintelligence.com/reputation)
  + BACK
  + [Intelligence Search](https://talosintelligence.com/reputation_center)
  + [Email & Spam Trends](https://talosintelligence.com/reputation_center/email_rep)
* [Vulnerability Research](https://talosintelligence.com/vulnerability_info)

  [ ]

  + [# Vulnerability Research](https://talosintelligence.com/vulnerability_info)
  + BACK
  + [Vulnerability Reports](https://talosintelligence.com/vulnerability_reports)
  + [Microsoft Advisories](https://talosintelligence.com/ms_advisories)
* [Incident Response](https://talosintelligence.com/incident_response)

  [ ]

  + [# Incident Response](/incident_response)
  + BACK
  + [Reactive Services](https://talosintelligence.com/incident_response/services#reactive-services)
  + [Proactive Services](https://talosintelligence.com/incident_response/services#proactive-services)
  + [Emergency Support](https://talosintelligence.com/incident_response/contact)
* [Blog](https://blog.talosintelligence.com)
* [Support](https://support.talosintelligence.com)

More

* Security Resources

  [ ]

  # Security Resources

  + BACK

  Security Resources
  + [Open Source Security Tools](https://talosintelligence.com/software)
  + [Intelligence Categories Reference](https://talosintelligence.com/categories)
  + [Secure Endpoint Naming Reference](https://talosintelligence.com/secure-endpoint-naming)
* Media

  [ ]

  # Media

  + BACK

  Media
  + [Talos Intelligence Blog](https://blog.talosintelligence.com)
  + [Threat Source Newsletter](https://blog.talosintelligence.com/category/threat-source-newsletter/)
  + [Beers with Talos Podcast](https://talosintelligence.com/podcasts/shows/beers_with_talos)
  + [Talos Takes Podcast](https://talosintelligence.com/podcasts/shows/talos_takes)
  + [Talos Videos](https://www.youtube.com/channel/UCPZ1DtzQkStYBSG3GTNoyfg/featured)
* Company

  [ ]

  # Company

  + BACK

  Company
  + [About Talos](https://talosintelligence.com/about)
  + [Careers](https://talosintelligence.com/careers)

# Introducing EvidenceForge: Synthetic security logs that don’t look (as) fake

By
[David J. Bianco](https://blog.talosintelligence.com/author/david-j-bianco/)

Wednesday, May 27, 2026 06:00

[Tool Talk](https://blog.talosintelligence.com/category/tool-talk/)

* Security teams need high-quality, labeled datasets to train threat hunters and incident responders, validate detection logic, and develop robust analytic models.
* EvidenceForge helps teams overcome the limitations of anonymized or stale public datasets, while avoiding the cost and complexity of setting up real infrastructure and performing manual attack simulations to create their own.
* The tool incorporates sophisticated timing models and assigns specific roles to users and systems, generating realistic malicious activity, background noise, and “red herrings” to optimize data realism.
* The tool generates correlated logs across 20+ Windows, Linux, and network monitoring formats using a canonical event model that ensures causal and temporal consistency.

---

## Good data is hard to find... and to create

A lot of important work in security depends on having realistic log data to work with, and a lot of that work gets blocked, watered down, or quietly skipped because the data just isn’t available. The use cases come up constantly: teaching threat hunters, incident responders, and detection engineers with datasets that have known ground truth; validating that a detection fires on the right activity without drowning in false positives; and training ML models that need labeled, balanced, multi-source telemetry at scale.

These are different problems with the same root cause. You need realistic, labeled security logs and you can’t get them easily. The options are limited:

* Real production telemetry is a compliance problem. Public datasets are often so heavily anonymized they no longer resemble the original log sources. The [LANL dataset](https://csr.lanl.gov/data/cyber1/) and [OpTC](https://github.com/FiveDirections/OpTC-data) are well-known examples of data scrubbed to the point of being generic event representations rather than actual telemetry. What isn’t anonymized is stale, narrow, and over-recycled.
* You can generate data yourself using attack simulation frameworks like [Atomic Red Team](https://github.com/redcanaryco/atomic-red-team) or [MITRE Caldera](https://github.com/mitre/caldera), but that requires real infrastructure, is time-consuming to operate, and scales poorly when you need variety.
* You can hire a red team, which trades complexity for money but still takes weeks and produces only the specific scenario they ran.

Synthetic generators seem like an obvious solution and [many](https://github.com/cruikshank25/Security-Log-Generator) [existing](https://github.com/summved/log-generator) [ones](https://github.com/Hu9o73/elasticsearch-data-generator) are genuinely useful tools, but they share a common architectural limitation: They generate events independently, one format at a time, with no shared state across log sources. The result is datasets where events don’t tell a coherent story. For example, a process in Sysmon doesn’t connect to the same process in standard Windows logs, or a network logon doesn’t leave a consistent connection trace. More capable tools support attack chains and MITRE ATT&CK mapping, but even then, they generate individual events rather than simulating something that happened, with all the prerequisite and consequent evidence that real activity would produce. Realistic background noise is largely absent.

What analysts detect when they call data synthetic is the absence of a coherent causal story. The logs don’t line up because they emit each log entry independently from the others, and they are not modeling a series of connected events.

## The answer: A new kind of synthetic data

EvidenceForge is a new o[pen-source project](https://github.com/Cisco-Talos/EvidenceForge) from Cisco Talos that approaches the problem differently. It features a single canonical event model, causal ordering, realistic background noise, and AI-assisted scenario authoring. The result is a synchronized dataset across 20+ log formats (Windows, Linux, network, and endpoint detection and response [EDR] telemetry), complete with ground truth documentation and an analyst briefing.

One honest note: No purely synthetic dataset will fool a seasoned analyst in every case, but that’s okay. The goal is fidelity that’s good enough to be useful, not something that’s indistinguishable from production.

### The core idea: One event, many formats

Most synthetic log generators are a collection of independent emitters. Each one knows how to produce its own format but doesn’t share state with the others. You can see the seams the moment you cross-reference across sources.

EvidenceForge inverts that. Every piece of evidence flows from a single canonical SecurityEvent object. That object carries a timestamp and event type, plus over 30 composable context objects populated as needed: ProcessContext (PID, parent PID, image, command line), NetworkContext (src/dst IP and port, Zeek UID, shared across Zeek, EDR, and SNORT®), AuthContext (username, LogonID, logon type, result), DnsContext and HttpContext (protocol-layer detail that fans out into the corresponding Zeek log types), and many more. Emitters read only the fields relevant to their format.

The consequence of shared contexts is that emitters cannot disagree. There is one PID, one LogonID, one timestamp, and one Zeek UID. The engine is also OS-aware: Windows hosts produce Security Events and Sysmon while Linux hosts produce syslog and bash history, each according to the OS assigned to each host in the scenario.

All of this is driven by a scenario configuration file: a YAML document describing the environment (hosts, users, network top...