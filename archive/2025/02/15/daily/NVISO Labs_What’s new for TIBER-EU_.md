---
title: What’s new for TIBER-EU?
url: https://blog.nviso.eu/2025/02/14/whats-new-for-tiber-eu/
source: NVISO Labs
date: 2025-02-15
fetch_date: 2025-10-06T20:35:17.123375
---

# What’s new for TIBER-EU?

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

# What’s new for TIBER-EU?

[Jonas Bauters](https://blog.nviso.eu/author/jonas-bauters/ "Posts by Jonas Bauters")

[Red Team](https://blog.nviso.eu/category/red-team/), [Adversary Simulation](https://blog.nviso.eu/category/red-team/adversary-simulation/), [Cyber Resilience](https://blog.nviso.eu/category/cyber-resilience/), [Adversary Emulation](https://blog.nviso.eu/category/red-team/adversary-emulation/)

February 14, 2025February 14, 2025
4 Minutes

## **A brief look at the updated TIBER-EU framework with DORA TLPT coming into play.**

In our [previous post](https://blog.nviso.eu/2024/11/08/tlpt-me-everything-you-need-to-know-about-threat-led-penetration-testing-tlpt-in-a-tiber-world/), we have discussed the “transition” from TIBER to TLPT (Threat-Led Penetration Testing), highlighting some differences between the previous TIBER specification and the requirements as indicated by DORA. This is mostly just a change in terminology. We concluded however by stating that adopting TIBER-EU would help to fulfill DORA’s TLPT requirements and predicted a TIBER-EU 2.0 to be published for additional convergence. That day has come, so let’s take a look at the updated TIBER-EU framework, how it compares to the previous version, and how it incorporates the new regulatory requirements.

### **CF vs CIF**

The 2018 version refers to “Critical Functions (CFs),” whereas the 2025 version uses “Critical or Important Functions (CIFs)”, as specified in DORA. What’s more interesting is the guidance on the number of CIF to be included in the scope: “a maximum number of 10 CIFs per tested entity is adequate” & “for each system in scope, the CT should set at least one “flag” to be captured during the test”.

### **Roles & Responsibilities**

The updated version provides a more extensive overview of the responsibilities of the different stakeholders, in particular for the TIBER Cyber Team (TCT) and Test Manager (TM), whose role is more prominent. In addition, the requirements and limitations for use of internal testers is also detailed, since this was a novel idea under DORA TLPT. There is also the recommendation to have at least an experienced external RT test manager join the internal testers to bring a fresh and independent perspective to the test.

### **Multi-Party & Multi-Jurisdiction**

Previous version already explained “cross-jurisdictional” testing for geographically dispersed entities that would include authorities from different jurisdictions in an exercise. This concept has not changed, although it is now referred to as “multi-jurisdictional” testing instead. Added to the new version is “multi-party” testing, in-line with DORA’s TLPT regulations for “pooled testing”, an exercise where the entity relies on common ICT infrastructure by a service provider. Guidance on this matter is fairly limited however.

### **Test Process & Phases**

With the new and improved version, we can see the reflection of DORA’s regulatory requirements, since the TIBER-EU testing process is detailed in greater depth, along with having specific milestones, deliverables, and timings/deadlines. Additional guidance documents are available as well, providing useful operational input.

### **Scenarios & Threat Intelligence Report**

In terms of scenario creation, we are seeing one of the biggest updates compared to the previous version of the TIBER-EU document, which did not provide specific input on the exact type or number of scenarios. The updated version requires a scenario shortlist consisting of at least three end-to-end threat scenarios for the threat profiles who exhibit the highest threat severity scores. They should all describe end-to-end attack paths (i.e. consisting of an IN, THROUGH, and OUT phase) and shall include, at least one scenario that includes, but is not limited to:

* compromised service **availability**;
* compromised data **integrity**;
* compromised information **confidentiality**

Optionally, it may also contain a scenario-X.

In terms of scenario selection for execution, a maximum of one scenario (out of the three selected scenarios) per TIBER test may be non-threat-led. This refers to the scenario-X, which allows for the investigation of future or otherwise relevant attack vectors. In case no separate scenario-X was specified, it’s allowed to “transform” one of the other selected scenario into a scenario-X during the red team execution phase, on condition that all involved stakeholders agree.

An interesting point to note is the potential “discrepancy” between the DORA TLPT RTS and the TIBER-EU specification w.r.t. CIFs and scoping:

* RTS – The proposed scenarios shall differ with reference to the identified threat actors and associated tactics, techniques and procedures and **shall target each and every critical or important functions in the scope of the TLPT**.
* TIBER-EU – **Although not all CIFs in the scope need to be targeted in the scenarios shortlist**, there should be breadth and depth in the CIFs targeted.

### **Purple Teaming**

As expected, purple teaming is now included as a mandatory step. The TIBER-EU framework document only covers purple teaming as part of the Closure Phase, to be performed after the replay workshop. However, the Purple Teaming Guidance document provides additional options and covers all your purple teaming needs. It distinguishes two options for purple teaming:

* Limited purple teaming – performed during the red team execution phase under very specific circumstances and in agreement with the Test Manager.
* Purple teaming – conducted during the closure phase, no later than 10 weeks after the end of the active red team testing phase.

In addition, the guidance document provides considerations for both options and input on different types of purple teaming, making it a valuable resource.

What remains unclear is whether the limited purple teaming sufficiently covers the requirements or whether a purple team in the closure phase is needed nonetheless.

### **Conclusion**

Unsurprisingly, the new TIBER-EU framework contains the required updates for convergence towards the DORA TLPT specifications. Even though minor open points remain, it is an additional guarantee that adopting TIBER is the way to perform a TLPT. This framework aims to be a handbook or set of detailed guidelines (i.e. the “HOW”) on completing DORA TLPT (i.e. the “WHAT”) in a qualitative, con...