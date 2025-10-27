---
title: TLPT & ME: Everything you need to know about Threat-Led Penetration Testing (TLPT) in a TIBER world.
url: https://blog.nviso.eu/2024/11/08/tlpt-me-everything-you-need-to-know-about-threat-led-penetration-testing-tlpt-in-a-tiber-world/
source: NVISO Labs
date: 2024-11-09
fetch_date: 2025-10-06T19:16:28.158113
---

# TLPT & ME: Everything you need to know about Threat-Led Penetration Testing (TLPT) in a TIBER world.

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

# TLPT & ME: Everything you need to know about Threat-Led Penetration Testing (TLPT) in a TIBER world.

[Jonas Bauters](https://blog.nviso.eu/author/jonas-bauters/ "Posts by Jonas Bauters")

[Purple Teaming](https://blog.nviso.eu/category/purple-teaming/), [Adversary Simulation](https://blog.nviso.eu/category/red-team/adversary-simulation/), [Purple Team](https://blog.nviso.eu/category/purple-team/), [Adversary Emulation](https://blog.nviso.eu/category/red-team/adversary-emulation/), [Red Team](https://blog.nviso.eu/category/red-team/)

November 8, 2024November 7, 2024
8 Minutes

# Introduction

In our [previous post](https://blog.nviso.eu/2024/08/29/the-big-tiber-encyclopedia/), we published an analysis of current TIBER implementations ahead of DORA’s TLPT requirements. To recap, this contained:

* An overview of existing TIBER implementations (situation mid-2024)
* A comparison of the respective guidance documents w.r.t. major building blocks, such as the generic threat landscape, purple teaming, leg-ups, scenario X
* Assurance that consistency across jurisdictions is guaranteed thanks to the overarching governance of the TIBER-EU guide.

We concluded part 1 by saying that Threat-led Penetration Testing as required by the DORA regulation will be specified in accordance with TIBER-EU and in agreement with the ECB. TIBER can be considered as the “How” to implement the “What” of the DORA (Digital Operational Resilience Act) Regulatory Technical Standard (RTS) on TLPT.

With the current post, we want to extend on the previous TIBER analysis and discuss particular requirements for the upcoming TLPT regulations as part of DORA that will *likely* result in an updated and more precise TIBER-EU framework.

The [draft RTS](https://eba.europa.eu/publications-and-media/events/consultation-joint-draft-rts-specifying-elements-related-threat-led-penetration-tests) has been in public consultation until March 4th 2024 and the European Supervisory Authorities (ESAs) submitted the [final draft RTS](https://eba.europa.eu/activities/single-rulebook/regulatory-activities/operational-resilience/joint-regulatory-technical-standards-specifying-elements-related-threat-led-penetration-tests) to the European Commission by 17 July 2024.

# TIBER to TLPT

Under DORA, 20 types of -mostly financial- entities (identified as systemically important institutions) will be required to perform a TLPT exercise at least once every 3 years. A TLPT involves targeting live production systems supporting critical functions of a financial entity according to the following high-level process, which is based on the TIBER framework:

* **Preparation**
  The process starts with the entity receiving a notification from the TLPT authority. The entity must assemble the Control Team (CT), submit initiation documents and scope specification following certain criteria for including critical functions. In addition, the CT must perform a risk assessment and risk management, and procurement of TI and RT providers.
* **Threat Intelligence**
  The TI provider will analyse generic and sector-specific threat intelligence relevant for the financial entity and perform reconnaissance against the entity. The TI report contains scenarios referencing specific threat actors targeting critical functions.
* **Red Team**
  The RT provider creates a red team test plan based on selected scenarios and executes the simulated attacks according to plan, communicating closely with the CT. Completion of the RT execution culminates in a red team report and initiates closure steps.
* **Closure**
  The closure phase initiates collaboration between red and blue teams, requiring a replay workshop and purple teaming. In addition, multiple deliverables are required, such as the test summary report and remediation plan to be provided by the CT. These steps are subject to thorough timing constraints.

If you are familiar with TIBER, this should all still be familiar ground. The only difference you may have noticed so far, is the terminology to refer to the White Team. In TLPT language, this team is now referred to as the Control Team, immediately indicating the role they have to fulfill. In terms of stakeholders, there is not much change either compared to TIBER participants:

|  |  |  |
| --- | --- | --- |
| **Financial Entity**  (to be targeted) | **Authority**  (regulator responsible for TLPT) | **Third-party Providers**  (executing the TLPT) |
| **Control Team**  Overall responsible for the exercise and all coordination, communication, planning, procurement, and risk control. | **TCT**  TLPT Cyber Team; staff within the authority responsible for TLPT-related matters. The TCT fulfills a supervisory role. | **Threat Intelligence**  Perform reconnaissance in terms of targets & threats to deliver the targeted threat intelligence report. |
| **Blue Team**  Uninformed. Performing their duties as usual defending the target entity with detection and response. | **Other authorities**  In case of a multi-jurisdictional test, other authorities (e.g. TCT member from another Member State’s TCT) can be involved. | **Red Team**  Execute the attack scenarios based on the red team test plan they created and attempt to compromise critical economic functions. |

> There may be a change in dynamic regarding the “power” of the TCT, who possibly go beyond a mere supporting role to having a stricter regulatory oversight duty.

So far, so good. However, there’s a few other particularities you may want to know about.

# What’s New?

The TLPT RTS also brings a few specifics and we have listed the most interesting ones below, based on our opinion and experience executing TIBER engagements across multiple jurisdictions.

## Internal Testers

TLPT allows the execution to be performed by internal testers. Instead of a third-party provider, internal testers can be used, with a number of caveats however:

* Every one in three tests should be performed by external testers;
* In case both internal and external testers are part of the team, this will be considered as a TLPT performed with internal testers w.r.t. previous statement;
* All members of the internal test team have been employed by the financial entity or by an ICT intra-group service provider for the preceding two years;
* Use of internal testers must be explicitly mentioned in TLPT-related documents, such as initiation documents or t...