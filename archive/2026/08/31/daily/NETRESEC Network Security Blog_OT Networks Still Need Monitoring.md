---
title: OT Networks Still Need Monitoring
url: https://www.netresec.com/?page=Blog&month=2026-08&post=OT-Networks-Still-Need-Monitoring
source: NETRESEC Network Security Blog
date: 2026-08-31
fetch_date: 2026-09-01T07:01:17.129325
---

# OT Networks Still Need Monitoring

Experts in network security monitoring and network forensics
[![Netresec](/images/Netresec_Logo_550x140.png)](https://www.netresec.com/)

[NETRESEC](/?page=Home)|

[Products](/?page=Products)|

[Training](/?page=Training)|

[Resources](/?page=Resources)|

[Blog](/?page=Blog)|

[About Netresec](/?page=AboutNetresec)

[NETRESEC](/)
»
[Blog](/?page=Blog)

Erik Hjelmvik

,

Monday, 31 August 2026 11:50:00 (UTC/GMT)

## [OT Networks Still Need Monitoring](/?page=Blog&month=2026-08&post=OT-Networks-Still-Need-Monitoring)

CERT Polska recently published a [follow-up report](https://cert.pl/uploads/docs/CERT_Polska_Energy_Sector_Incident_Follow_up_Report_2025.pdf) detailing the hack of a Polish combined heat and power (CHP) plant in December 2025.

CERT Polska’s report concludes with several important recommendations, including protecting OT systems through network segmentation and monitoring traffic entering and leaving OT networks. It has now been more than 15 years since I first publicly advocated almost exactly these same two recommendations in my blog post [Monitor Those Control System Networks](https://netresec.com/?b=1185A14).

One might get the impression that nothing has changed during those 15 years, but I can attest that many OT systems now have effective perimeter protection. Operators of critical infrastructure are also beginning to embrace the concept of network security monitoring for OT systems.

Unfortunately, it appears that the hacked CHP plant in Poland did not have sufficient perimeter protection or network security monitoring in place. The apparent lack of monitoring and logging also left CERT Polska with very limited forensic data. As the report states, “Due to the lack of logs, our investigation relied on the development and testing of hypotheses.” Despite these limitations, I am very impressed by the level of technical detail that CERT Polska were able to reconstruct during their investigation of the CHP hack.

**Attack Path**

As CERT Polska outline in their report, the attackers’ initial access vector was an Internet-facing FortiGate VPN at a wind farm. From the VPN device, they pivoted via a Teltonika cellular 5G router into a WAGO PLC, which ultimately gave them access to the control system network of a CHP plant.

![Attack path from the Internet to the CHP network](https://media.netresec.com/images/CHP-PL_ascii-attack-path_v2_1624x500.png)

*Image: Attack path from the Internet to the CHP network*

The lack of perimeter protection, which would otherwise have prevented direct connections between different remote sites, gave the attackers access to the PLCs and other industrial equipment that directly controlled the physical process at the CHP plant.

With that type of access, attackers do not need to exploit a vulnerability. They can simply issue “normal” commands over the OT network to shut down the process at the plant. In this specific case, the attackers performed the following operations, apparently in an attempt to cause maximum disruption:

* Switched multiple Siemens S7 PLCs to STOP mode
* Enabled password protection on Siemens S7 PLCs to prevent operators from switching them back to RUN mode
* Changed the configurations of several industrial serial device servers and network switches, making them inaccessible from the network

![Siemens S7-1500 PLC in STOP mode, from CERT Polska’s report](https://media.netresec.com/images/CERT-PL_SIMATIC_S7-1500_STOP-mode_960x1036.webp)

*Image: Siemens S7-1500 PLC in STOP mode, from CERT Polska’s report*

As a result of the attack, a steam turbine and the system used to produce process water in the CHP plant were both shut down on December 29.

**Network Security Monitoring**

Better perimeter protection might have prevented the initial access path used against the Polish CHP plant. However, it is not always easy for asset owners and operators to identify every boundary around an OT environment or segment it without affecting operations. This is where network security monitoring plays an important role.

OT networks are often well suited to passive monitoring. Most industrial protocols are unencrypted, communication patterns are more deterministic than those in enterprise networks, and traffic volumes are often modest.
By monitoring OT network traffic and alerting on suspicious or anomalous behavior and known attack techniques, defenders may be able to detect an intrusion early enough to investigate, contain, and stop it before destructive actions are carried out.

Examples of useful detections include:

* Reconnaissance activity, such as TCP SYN scans
* Attempts to access canary or honeypot systems that normal operations should not touch
* Connections from unexpected systems to ICS-specific ports, such as TCP ports 102, 502, 2404, 5094, 20000, 44818 and 47808
* Potentially dangerous protocol commands, such as putting a PLC into STOP mode, changing its operating mode, downloading a new program, or modifying its configuration outside a scheduled maintenance window
* New communication paths, such as traffic between IP address pairs that have not previously communicated

The Polish incident illustrates the value of detecting reconnaissance activity, not just the final destructive commands. The disruptive actions occurred on December 29, but CERT Polska uncovered malicious activity as early as December 18.

![Log from the Teltonika RUTX50 cellular router](https://media.netresec.com/images/CERT-PL_Teltonika-ssh-log_901x310.webp)

*Image: Log from the Teltonika RUTX50 cellular router*

This suggests that the attackers had access to the environment more than 10 days before the destructive actions. This period is known as the dwell time: the time between an attacker gaining access to an environment and being detected or taking disruptive action.

Had the intrusion been detected early, this dwell time would have provided multiple opportunities for defenders to contain it before the attackers carried out their disruptive actions.

Long dwell times are common in attacks against OT systems. Attackers may spend weeks or months learning about the environment, identifying important assets, and determining how to disrupt the physical process. In some cases, access to critical infrastructure is established as part of pre-positioning, where a state-sponsored threat actor gains and maintains access to an OT environment without immediately causing disruption, preserving the ability to deliver a destructive payload at a later point. This makes early detection especially important, even when an intrusion does not initially appear to be affecting plant operations.

Captured network traffic, preferably stored as PCAP files, is one of the most valuable sources of evidence when analyzing a suspected attack against an OT system. It can help investigators reconstruct the attacker’s activity, validate alerts, and identify affected systems. If the captured traffic is stored on a system that is not accessible from the OT network, the risk of an attacker tampering with the evidence is reduced.

This is one reason we have been teaching [Network Forensics for Industrial Control Systems](https://www.netresec.com/?page=TrainingICS) for more than 10 years. Feel free to [reach out](https://www.netresec.com/?page=AboutNetresec) if you want to learn more about our network forensics training.

**Siemens S7 Advisory**

On a related note, the NSA, CISA, FBI, DOE, and EPA published a joint cybersecurity advisory titled [Defending Against an Active Threat to Siemens S7 Series PLCs](https://www.cisa.gov/news-events/cybersecurity-advisories/aa26-231a) on August 19 ([PDF](https://media.defense.gov/2026/Aug/18/2003983494/-1/-1/0/CSA_Active_Threat_to_Siemens_S7_Series_PLCs.PDF)). In the advisory, the authoring agencies called for mitigation measures such as verifying network segmentation and monitoring network traffic to detect and alert on anomalous or malicious activity. These recommendations are very much in line with what CERT Po...