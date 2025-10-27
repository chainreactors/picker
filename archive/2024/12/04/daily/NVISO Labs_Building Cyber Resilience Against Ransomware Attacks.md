---
title: Building Cyber Resilience Against Ransomware Attacks
url: https://blog.nviso.eu/2024/12/03/building-cyber-resilience-against-ransomware-attacks/
source: NVISO Labs
date: 2024-12-04
fetch_date: 2025-10-06T19:37:31.528799
---

# Building Cyber Resilience Against Ransomware Attacks

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

# Building Cyber Resilience Against Ransomware Attacks

[Filippos Raditsas](https://blog.nviso.eu/author/filippos-raditsas/ "Posts by Filippos Raditsas")

[Cyber Resilience](https://blog.nviso.eu/category/cyber-resilience/), [Incident & Crisis Management](https://blog.nviso.eu/category/incident-crisis-management/), [Cybersecurity](https://blog.nviso.eu/category/cybersecurity/)

December 3, 2024December 3, 2024
11 Minutes

## **Or, “Yet another ransomware blog post?”**

“Yet another ransomware blog post?” I hear you asking.

Well, yes! Besides, Ransomware attacks have been on the rise again costing affected organizations and industries more than ever. Let’s dive into some numbers to set the stage:

According to [IBM and Ponemon institute](https://www.ibm.com/reports/data-breach), in 2024, the average cost of a ransomware attack climbed to USD 5.24 million. This rise in cost reflects the growing sophistication of ransomware attacks, including the use of ransomware-as-a-service and the targeting of supply chains, which can extend the impact beyond the initial victim to additional networks and systems.

To top it off, this resulted in quite a few changes in the regulatory landscape, resulting in more robust regulatory frameworks such as the NIS2 Directive, the CRA (Cyber Resilience Act) – These regulations, while valuable, pose challenges for organizations trying to comply. Many are left wondering, “Another regulation? What do we need to do now? How do we increase our resilience against threats like ransomware while meeting compliance?”

At NVISO we want to view security as a business enabler, so we ask ourselves “*could we meet organizations at their current readiness level* and help them identify tangible next steps to take to develop actual resilience against ransomware, while attaining compliance requirements?” This led us to create a series of blog posts to guide organizations in building resilience against ransomware attacks while meeting regulatory requirements.

This is the first blogpost in this series. Its aim is twofold: to enable organizations embarking on a journey to build resilience against ransomware to recognize *common misconceptions hindering readiness efforts and offer a conceptual framework to guide effective resilience building*.

## **The “headless chicken” effect**

For the purposes of this blog post, let’s consider how a ransomware attack typically plays out in an underprepared organization.

This scenario is examined from three distinct points of view:

* The end-user who inadvertently initiates the attack
* The senior management grappling with the crisis
* The technology team attempting to contain the damage

By exploring these perspectives, we can identify common misconceptions around building resilience against such attacks, all of which contribute to the “headless chicken effect.”

ANY similarity to actual persons or entities, living or dead, is PURELY coincidental.

### **The End-User**

In a recent ransomware incident, an organization fell victim to a sophisticated attack orchestrated by a ransomware group. The attack began with a phishing email that tricked an employee, an end-user who had not received regular security training, into downloading a malicious attachment; don’t get us wrong here, there are cases where people that have been extensively trained can fall for it due to a short lapse in judgement or momentary carelessness. Now back to our story…

Unaware of the proper steps to take when encountering suspicious emails, the end-user clicked on the link, initiating the infection chain. Once the ransomware was inside the network, it rapidly spread, encrypting files and disrupting essential services. The end-user soon realized their endpoint and data were inaccessible. Panicked and unsure of what to do, the end-user acted in an uncoordinated manner, disconnecting their system from the network without a strategic plan and without informing the IT. This haphazard action allowed the ransomware to spread further before containment measures were effectively implemented.

This story could easily play out quite differently; the user could just blame IT for everything and fail to realize a cyber-attack is actually ongoing.

### **Senior Management**

As the ransomware attack unfolded, senior management experienced the crisis from a different perspective. They were inundated with questions and concerns, expecting immediate answers. “I thought we had backups?” asked one executive, only to find out that the backups were not regularly tested or stored securely, leading to significant data loss when the ransomware deleted shadow copies. Another manager questioned, “What is the contractor we are paying so much for the IR retainer doing?” It became evident that having an Incident Response (IR) retainer was not sufficient on its own, as critical systems were not isolated in a timely manner.

Senior management grappled with understanding the full impact of the attack. They were concerned about the financial and reputational damage, asking, “What does this mean financially and reputationally?” and “Should we pay the ransom?” Faced with the pressure of encrypted data and operational disruption, some decision-makers considered paying the ransom, believing it would be a quicker and cheaper solution. However, there was no guarantee that the attackers would provide the decryption key or that they wouldn’t strike again, which could lead to further financial loss, adding to the budget required for actual mitigation measures.

Adding to the chaos, the media had somehow found out about the breach, before the organization could have any control over the narrative, leading to further questions from management: “How did the media find out?” There was no pre-established crisis communication plan, resulting in delays in informing stakeholders, including customers, partners, and authorities about the breach.

### **Technology Team**

From the technology team’s perspective, the situation was a firefight without clear procedures or roles. Overwhelmed and under-resourced, the IT team struggled to contain the ransomware. They were not sure of the specific steps to take, leading to haphazard actions and further spread of the malware.

The IT team also faced the challenge of communicating effectively. The team did not have designated secure channels to coordinate their response effort...