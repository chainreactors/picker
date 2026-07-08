---
title: Reducing Microsoft Sentinel Costs Without Compromising Detection – Part 2: The Firewall Quest
url: https://blog.nviso.eu/2026/07/07/reducing-microsoft-sentinel-costs-without-compromising-detection-part-2-the-firewall-quest/
source: NVISO Labs
date: 2026-07-07
fetch_date: 2026-07-08T05:04:10.531992
---

# Reducing Microsoft Sentinel Costs Without Compromising Detection – Part 2: The Firewall Quest

[Skip to content](#content)

[![NVISO Labs](https://blog.nviso.eu/wp-content/uploads/2022/12/cropped-abn-zcrj_400x400-1.png)](https://blog.nviso.eu/)

[NVISO Labs](https://blog.nviso.eu/)

Cyber security research, straight from the lab! 🐀

* [linkedin](https://www.linkedin.com/company/nviso-cyber)
* mail us
* [our company](https://www.nviso.eu)
* [SSO](https://blog.nviso.eu/wp-admin/edit.php)
* Search for:Search Button

Menu

* [All](https://blog.nviso.eu/)
* [Prevent](https://blog.nviso.eu/category/prevent/)
  + [Application Security](https://blog.nviso.eu/category/prevent/application-security/)
    - [IoT Security](https://blog.nviso.eu/category/prevent/iot-security/)
    - [Web Security](https://blog.nviso.eu/category/prevent/web-security/)
    - [Mobile Security](https://blog.nviso.eu/category/prevent/mobile-security/)
    - [Industrial Security](https://blog.nviso.eu/category/prevent/industrial-security/)
    - [AI Security](https://blog.nviso.eu/category/prevent/application-security/ai-security/)
  + [Cloud Security](https://blog.nviso.eu/category/prevent/cloud-security/)
    - [AWS](https://blog.nviso.eu/category/prevent/cloud-security/aws/)
    - [Azure](https://blog.nviso.eu/category/prevent/cloud-security/azure/)
    - [GCP](https://blog.nviso.eu/category/prevent/cloud-security/gcp/)
    - [Microsoft 365](https://blog.nviso.eu/category/prevent/cloud-security/microsoft-365/)
  + [Awareness](https://blog.nviso.eu/category/prevent/awareness/)
  + [Cyber Strategy](https://blog.nviso.eu/category/prevent/cyber-strategy/)
  + [Red Team](https://blog.nviso.eu/category/prevent/red-team/)
* [Detect](https://blog.nviso.eu/category/detect/)
  + [Blue Team](https://blog.nviso.eu/category/detect/blue-team/)
  + [Purple Team](https://blog.nviso.eu/category/detect/purple-team/)
* [Respond](https://blog.nviso.eu/category/respond/)
  + [Forensics](https://blog.nviso.eu/category/respond/forensics/)
* Other
  + [Events](https://blog.nviso.eu/category/events/)

# Reducing Microsoft Sentinel Costs Without Compromising Detection – Part 2: The Firewall Quest

[Christos Giampoulakis](https://blog.nviso.eu/author/christos-giampoulakis/)

[Blue Team](https://blog.nviso.eu/category/detect/blue-team/), [Detection Engineering](https://blog.nviso.eu/category/detection-engineering/), [Sentinel](https://blog.nviso.eu/category/prevent/cloud-security/sentinel/)

July 7, 2026July 7, 2026
10 Minutes

This entry is part 2 in the series [Reducing Microsoft Sentinel Costs Without Compromising Detection](https://blog.nviso.eu/series/reducing-microsoft-sentinel-costs-without-compromising-detection/ "Reducing Microsoft Sentinel Costs Without Compromising Detection")

---

By

[Christos Giampoulakis](https://blog.nviso.eu/author/christos-giampoulakis/) , [Theodoros Polyzos](https://blog.nviso.eu/author/theodoros-polyzos/)

July 7, 2026

Continuing our journey through Sentinel ingestion cost reduction, this part focuses on one of the most expensive log sources: firewalls, and more specifically, network traffic events.

Network traffic logs from firewalls are highly voluminous and often become the largest contributor to data ingestion costs. At the same time, they remain a valuable source of information during Incident Response or while developing Threat Detection use cases, as they provide a centralized view of network activity across the environment. This creates a familiar dilemma for many Security Teams: *should firewall traffic logs be ingested into Sentinel?*

The objective of this part is to examine how Summary Rules can help reduce the cost of ingesting firewall traffic events while maintaining the visibility needed to support Detection and Incident Response.

## Detect Threats through Network Events

### Detection Types

Firewall traffic events can enable multiple detection scenarios, particularly related to network-based attack behavior. Typical examples include reconnaissance activity such as port scanning and port sweeping, where a source system attempts to probe multiple ports or hosts in a short period of time.

They can also be used to identify communication with known malicious or suspicious destinations through correlation with Threat Intelligence feeds. This includes communication with known command-and-control infrastructure or anonymization services such as Tor. Depending on the environment, these patterns can support the detection of malware activity, lateral movement, or policy evasion.

### Ingestion Cost

To illustrate the financial impact, consider a typical Microsoft Sentinel environment using the pay-as-you-go pricing model at $5.59 per GB ([price for West Europe at the time of writing](https://www.microsoft.com/en-us/security/pricing/microsoft-sentinel/#section-master-oc2d43)[1](#b61d4ef6-a515-47c2-868d-79f61b2d9d8d)). In an average environment, ingesting 50 GB of firewall traffic logs per day into the Analytics tier would cost approximately $8,500 per month. For a more accurate view of expected costs in your own environment, Microsoft provides the [Sentinel Cost Estimator app](https://www.microsoft.com/en-us/security/pricing/microsoft-sentinel/cost-estimator)[2](#6973ac01-9243-43ec-add6-53b75767ceb3).

Over the next sections, we will present a practical solution to this challenge and provide a technical implementation that reduces cost without compromising the visibility these logs can offer.

## Summary-Based Network Scan Detection

### Understanding Network Scans

To demonstrate the approach presented in this article, we will focus on the detection of network scanning activity. Before diving into the implementation details, it is important to understand what a network scan is and how this behavior appears in firewall traffic logs.

A network scan is a reconnaissance technique used to discover live hosts and enumerate exposed services within a network. In practice, this usually involves sending connection attempts to multiple ports or hosts, or both, in order to identify reachable systems and determine which services are listening. This information can be used to map the environment and identify potential attack paths.

From a logging perspective, a network scan appears as a deviation from the normal traffic flow generated by an endpoint. Under typical conditions, a workstation browsing the internet will establish multiple outbound TCP connections, most commonly over ports 80 and 443. For a domain-joined system, it will also regularly communicate with internal infrastructure such as Domain Controllers over expected services like Kerberos, LDAP, DNS, or SMB.

What is less typical is an endpoint attempting connections to a larger number of ports in a very short period of time, especially when targeting the same destination. For example, if a workstation attempts to connect to ports 1 through 1024 on the same destination in under one minute, this would be a strong indicator of *vertical scanning*. Likewise, repeated connection attempts to the same port across many different hosts may indicate *horizontal scanning*.

### Lab Infrastructure Setup

[In the first part of this series](https://blog.nviso.eu/2026/06/17/reducing-microsoft-sentinel-costs-without-compromising-detection-part-1-the-summary-rules-quest/), we explored split transformation rules and how they can be used to redirect part of the ingestion stream to the Data Lake. For this showcase, we keep the setup simple: a Windows server ingesting [Windows Filtering Platform (Windows Firewall)](https://learn.microsoft.com/en-us/windows/win32/fwp/windows-filtering-platform-start-page)[3](#dbee9004-47c6-4a09-b5eb-6c013e4527c2) events in Microsoft Sentinel into the **Data Lake** directly.

Although Windows Filtering Platform can generate logs for a broader range of activities, this demonstration focuses on two core connection events:

* [EID 5156 for *permitted* connections](https://learn.microsoft.com/en-us/previous-versions/windows/it-pro/windows-10/security/threat-protection/auditing/event-5156)[4](#5277...