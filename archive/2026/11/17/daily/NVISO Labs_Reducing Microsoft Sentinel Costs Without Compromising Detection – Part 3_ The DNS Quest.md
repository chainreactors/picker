---
title: Reducing Microsoft Sentinel Costs Without Compromising Detection – Part 3: The DNS Quest
url: https://blog.nviso.eu/2026/11/17/reducing-microsoft-sentinel-costs-without-compromising-detection-part-3-the-dns-quest/
source: NVISO Labs
date: 2026-11-17
fetch_date: 2026-11-18T09:21:15.043420
---

# Reducing Microsoft Sentinel Costs Without Compromising Detection – Part 3: The DNS Quest

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

# Reducing Microsoft Sentinel Costs Without Compromising Detection – Part 3: The DNS Quest

[Theodoros Polyzos](https://blog.nviso.eu/author/theodoros-polyzos/)

[Blue Team](https://blog.nviso.eu/category/detect/blue-team/), [Detection Engineering](https://blog.nviso.eu/category/detection-engineering/), [Sentinel](https://blog.nviso.eu/category/prevent/cloud-security/sentinel/)

November 17, 2026November 17, 2026
10 Minutes

This entry is part 3 in the series [Reducing Microsoft Sentinel Costs Without Compromising Detection](https://blog.nviso.eu/series/reducing-microsoft-sentinel-costs-without-compromising-detection/ "Reducing Microsoft Sentinel Costs Without Compromising Detection")

---

By

[Theodoros Polyzos](https://blog.nviso.eu/author/theodoros-polyzos/) , [Christos Giampoulakis](https://blog.nviso.eu/author/christos-giampoulakis/)

November 17, 2026

In our previous blog, *[Reducing Microsoft Sentinel Costs Without Compromising Detection – Part 2: The Firewall Quest](https://blog.nviso.eu/2026/07/07/reducing-microsoft-sentinel-costs-without-compromising-detection-part-2-the-firewall-quest/)*, we described the application of Summary rules to Firewall events. In this part of our blog series, we focus on another expensive log source, DNS. We will explore DNS events and how Summary Rules can be leveraged in this high-volume log source to effectively reduce Sentinel costs while maintaining detection capabilities.

DNS is one of the crucial log sources in terms of security monitoring. In an environment, DNS events offer detailed visibility of queries and responses originating from workstations and servers. From a security perspective, this telemetry is highly valuable for threat monitoring, as DNS activity frequently reveals early or post-infection indicators of compromise. During incident response, DNS logs help reconstruct attacker activity, identify affected hosts and establish timelines with greater precision. In practice, maintaining this level of logging strengthens detection capabilities, improves investigative depth, and supports faster, evidence-based containment and remediation decisions.

## Detect Threats through DNS Events

### Detection Types

DNS telemetry supports a range of detection and threat-hunting scenarios, including DNS tunneling, [command-and-control beaconing](https://www.extrahop.com/resources/attacks/c-c-beaconing)[1](#ff6b8599-6182-4daf-88b8-a056cdbb3aef), malicious domain lookups identified through threat intelligence, DNS-based data exfiltration, and communications with newly observed or otherwise suspicious domains. In DNS events there are specific fields that contain interesting information for our detections. Fields like `Dns Query content`, `Dns Query Type`, `Dns Response code` can be leveraged for numerous detection use cases.

## Summary-Based DNS Threat Detections

In the previous blog, we presented a way to use firewall events for detecting network scan attacks based on the aggregated information that is being generated by the summary rules. This was done by aggregating events which have similar characteristics on fields like `Source IP`, `Destination IP`, `Destination Port` and `Protocol`. For the DNS approach, we will propose and analyze a different approach. We will use Summary Rules to filter DNS events ingested into an [Auxiliary/Data Lake](https://learn.microsoft.com/en-us/azure/sentinel/datalake/sentinel-lake-overview)[2](#dfd21ee2-ab3d-4dbd-b230-ce8de2f892d2) table to identify patterns that indicate a suspicious or malicious DNS query, or a different behavioral anomaly in the DNS events that are generated by our servers. Based on a detection logic, an event of the suspicious traffic will be generated by the Summary Rule and stored in the newly generated Analytic Tier table that is used by the Summary Rule. Finally, we will use this event in this table to generate an alert using an Analytic Rule.

To demonstrate our Summary based DNS threat detection, we will focus on a common technique used by adversaries, DNS Tunneling.

### What is DNS Tunneling ?

[DNS Tunneling](https://www.paloaltonetworks.com/cyberpedia/what-is-dns-tunneling)[3](#1e999767-20a6-474f-9d01-c7c8ec619ae5) attack is a technique used by adversaries for command & control of infected devices, exfiltration by transferring data out of the network

DNS tunneling attack is a technique that abuses the Domain Name System (DNS) to secretly transfer and exfiltrate data or communicate with a compromised device for command & control purposes, and even bypassing firewall or proxy restrictions by a covert channel of communication. To shortly describe this technique, an attacker starts by compromising a device inside an organization. The malware that has been deployed on the device, encodes information gathered from the host (credentials, files, or even just host or network information) into subdomain request. The device then sends DNS queries to a domain controlled by the attacker, enabling the attacker to collect and decode the information while also using the same channel to send commands to the compromised host. An example of encoding for DNS tunneling is the usage [base32](https://en.wikipedia.org/wiki/Base32)[4](#c1982b5b-72eb-4933-9caf-05fca1adf976) to encode a message which is then used as the subdomain of the request. [Sliver C2](https://sliver.sh/docs/?name=DNS+C2)[5](#10bb6b92-d867-46fe-aed7-f1d67f539f78) is an example of an offensive tool that uses base32 for its DNS C2 activities.

### Lab Infrastructure Setup

As we mentioned in the [First and Second blog of this series](https://blog.nviso.eu/series/reducing-microsoft-sentinel-costs-without-compromising-detection/), we have presented the split transformation rules. These rules are used to redirect a part of the ingestion stream to the Data Lake. However, for DNS events, we will go one step further, by ingesting all Microsoft DNS Analytical events to Data Lake. For this showcase we will focus on [Microsoft DNS Analytical](https://learn.mic...