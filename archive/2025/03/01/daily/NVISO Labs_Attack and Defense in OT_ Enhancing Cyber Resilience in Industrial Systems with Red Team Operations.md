---
title: Attack and Defense in OT: Enhancing Cyber Resilience in Industrial Systems with Red Team Operations
url: https://blog.nviso.eu/2025/02/28/attack-and-defense-in-ot-enhancing-cyber-resilience-in-industrial-systems-with-red-team-operations/
source: NVISO Labs
date: 2025-03-01
fetch_date: 2025-10-06T21:57:35.544731
---

# Attack and Defense in OT: Enhancing Cyber Resilience in Industrial Systems with Red Team Operations

[Skip to content](#content)

[![NVISO Labs](https://blog.nviso.eu/wp-content/uploads/2022/12/cropped-abn-zcrj_400x400-1.png)](https://blog.nviso.eu/)

[NVISO Labs](https://blog.nviso.eu/)

Cyber security research, straight from the lab! 🐀

* [twitter](https://twitter.com/NVISO_Labs)
* [linkedin](https://www.linkedin.com/company/nviso-cyber)
* mail us
* [our company](https://www.nviso.eu)
* [SSO](https://blog.nviso.eu/wp-admin/edit.php)

Menu

* [All](https://blog.nviso.eu/)
* [Blue Team](https://blog.nviso.eu/category/blue-team/)
* [Cloud Security](https://blog.nviso.eu/category/cloud-security/)
  + [AWS](https://blog.nviso.eu/category/cloud-security/aws/)
  + [Azure](https://blog.nviso.eu/category/cloud-security/azure/)
  + [GCP](https://blog.nviso.eu/category/cloud-security/gcp/)
  + [Microsoft 365](https://blog.nviso.eu/category/cloud-security/microsoft-365/)
* [Awareness](https://blog.nviso.eu/category/awareness/)
* [Forensics](https://blog.nviso.eu/category/forensics/)
* Other
  + [Application Security](https://blog.nviso.eu/category/application-security/)
  + [IoT Security](https://blog.nviso.eu/category/iot-security/)
  + [Web Security](https://blog.nviso.eu/category/web-security/)
  + [Industrial Security](https://blog.nviso.eu/category/industrial-security/)
  + [Mobile Security](https://blog.nviso.eu/category/mobile-security/)
  + [Cyber Strategy](https://blog.nviso.eu/category/cyber-strategy/)
  + [Purple Team](https://blog.nviso.eu/category/purple-team/)
  + [Red Team](https://blog.nviso.eu/category/red-team/)
  + [Events](https://blog.nviso.eu/category/events/)

# Attack and Defense in OT: Enhancing Cyber Resilience in Industrial Systems with Red Team Operations

[Sarah Mader](https://blog.nviso.eu/author/sarah-mader/ "Posts by Sarah Mader")

[Adversary Simulation](https://blog.nviso.eu/category/red-team/adversary-simulation/), [ICS](https://blog.nviso.eu/category/ics/), [Uncategorized](https://blog.nviso.eu/category/uncategorized/), [Operational Technology (OT)](https://blog.nviso.eu/category/uncategorized/operational-technology-ot/), [Red Team](https://blog.nviso.eu/category/red-team/)

February 28, 2025March 6, 2025
12 Minutes

In today’s rapidly evolving industrial landscape, securing Operational Technology (OT) is more critical than ever due to increased connectivity and sophisticated cyber threats. Throughout this blog post series, we will dive into the world of Operational Technology Security.

This edition of the series focuses on how Red Team assessments can assist companies in identifying and mitigating threats in OT environments. After giving some background about the current threat landscape and terminology, we start by explaining how an external attacker gains an initial foothold in the network. Next, we explore the methods attackers use to gain access to OT systems, illustrated through two case stories targeting critical components such as SCADA (Supervisory Control and Data Acquisition), PLCs (Programmable Logic Controllers), and HMIs (Human-Machine Interfaces).

## **Operational Technology and Industrial Control Systems**

First, let’s clarify some terminology. The [NIST Computer Security Resource Center](https://csrc.nist.gov/) defines [Operational Technology (OT)](https://csrc.nist.gov/glossary/term/operational_technology) as “Programmable systems or devices that interact with the physical environment (or manage devices that interact with the physical environment). These systems/devices detect or cause a direct change through the monitoring and/or control of devices, processes, and events. Examples include industrial control systems, building management systems, fire control systems, and physical access control mechanisms.”

[Industrial Control Systems (ICS)](https://csrc.nist.gov/glossary/term/industrial_control_system) are further defined as “An information system used to control industrial processes such as manufacturing, product handling, production, and distribution. Industrial control systems include supervisory control and data acquisition systems used to control geographically dispersed assets, as well as distributed control systems and smaller control systems using programmable logic controllers to control localized processes.” In context of this blog post series the term OT will be used to describe infrastructure in which OT is deployed.

## **Red Team Assessments & APTs**

Unlike regular penetration testing, which focuses on identifying and exploiting vulnerabilities within a specific scope, Red Team operations are driven by specific objectives that are defined for the unique environment. In OT settings, these objectives are often a proof of the access to field devices or the IT-to-OT boundary. For further details about Red Team operations refer to this [description](https://www.ibm.com/think/topics/red-teaming).

A Red Team operation simulates realistic attacks based on adversary tactics, techniques, and procedures (TTPs) used by known [Advanced Persistent Threats (APTs)](https://csrc.nist.gov/glossary/term/advanced_persistent_threat). A Red Team operation supports a company to assess their own people, processes, and technology in terms of prevention, detection and response to determine the impact of a realistic attack and identify improvement areas.

A notable APT in the context of OT is [Electrum](https://attack.mitre.org/groups/G0034/), known for its role in the 2016 Kiev power outage within the [CRASHOVERRIDE](https://attack.mitre.org/campaigns/C0025/) incident, which highlights the real-world impact of OT-targeted attacks. The corresponding CRASHOVERRIDE malware is a framework containing multiple modules to interact with different ICS network protocols as for example IEC 101, IEC 104, IEC 61850, and OPC. During the power outage in 2016, the group used malware to attack circuit breakers on Remote Terminal Units (RTUs), which are devices that connect to physical equipment in substations, resulting in the de-energizing of these substations. The group is known for its sophisticated techniques and operational role in disrupting critical infrastructure. According to recent reports, the group is still active and may also target regions beyond Ukraine.

![Wiring PLC Control panel with wires in cabinet for machine industrial factory](https://blog.nviso.eu/wp-content/uploads/2025/02/84939774_m-1024x683.jpg)

Another outstanding event is the ICS malware FrostyGoop. FrostyGoop is engineered to exploit the ModbusTCP protocol, commonly used in industrial control systems, to manipulate control system operations. This malware highlights the increasing threats faced by critical infrastructure sectors. FrostyGoop allows adversaries to inject unauthorized commands, causing disruptions such as the de-energizing of substations or malfunctioning of heating systems. For a detailed description, see [FrostyGoop: The Latest ICS Malware Targeting Critical Infrastructure.](https://www.sans.org/blog/whats-the-scoop-on-frostygoop-the-latest-ics-malware-and-ics-controls-considerations/)

## **Why OT Security is More Critical Than Ever**

The reasons behind the increasing need and interest for OT security can be summarized in three points:

* Increased Connectivity
* Worsening Threat Landscape
* Regulations

### **Increased Connectivity**

Many benefits, as greater efficiencies and lower costs, can be achieved with modernization of OT, but this in turn also often increases the attack surface of the environment. With the development of the technology, many previously air-gapped or isolated systems now become interconnected, and many of these devices were never designed for this connectivity, which makes securing them even more challenging.

### **Worsening Threat Landscape**

The importance of adequate safety measures has long been clear. The need is strengthened by the surge in global tension, which led to increased cyber threat activity. The worldwide conflicts in Ukraine-Russia, Israel-Hamas, and the South China Sea region encourag...