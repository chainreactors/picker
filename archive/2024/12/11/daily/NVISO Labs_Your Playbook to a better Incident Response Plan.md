---
title: Your Playbook to a better Incident Response Plan
url: https://blog.nviso.eu/2024/12/10/your-playbook-to-a-better-incident-response-plan/
source: NVISO Labs
date: 2024-12-11
fetch_date: 2025-10-06T19:39:41.699791
---

# Your Playbook to a better Incident Response Plan

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

# Your Playbook to a better Incident Response Plan

[Damien Gremes](https://blog.nviso.eu/author/damien-gremes/ "Posts by Damien Gremes")

[Cyber Resilience](https://blog.nviso.eu/category/cyber-resilience/), [Incident & Crisis Management](https://blog.nviso.eu/category/incident-crisis-management/), [Uncategorized](https://blog.nviso.eu/category/uncategorized/), [Cyber Strategy](https://blog.nviso.eu/category/cyber-strategy/)

December 10, 2024May 21, 2025
10 Minutes

In 2023, [1271 incidents were reported to European Authorities via EIDAS, NISD, and EECC](https://ciras.enisa.europa.eu/), a 20% increase compared to the previous year. With more and more regulations entering into force in the next few years (such as NIS2 and CRA), a larger number of organisations will be forced to report their incidents too due to the increase of organisations in scope for this mandatory reporting, which will most likely make this number increase even more. Maybe you will be among these and are wondering how to prepare yourself.

In the previous entry in this series, we introduced the 3 pillars for building resilience: Respond, Sustain, and Recover. In this blogpost, we will explore the first pillar: Respond, the dimension that is crucial for mitigating the impact of an incident, particularly in the case of a ransomware attack.

![3 pillars for building resilience: Respond, Sustain, and Recover](https://blog.nviso.eu/wp-content/uploads/2024/11/image.png)

Why exactly should we prepare for a potential incident? Why not wait after our first incident, once we have more experience to learn from and therefore lose less time on the theory and research? While there is merit in learning and adapting your response based on previous incidents, proactive preparation can significantly mitigate the impact of an such incident in the first place. Some of these benefits include:

* Minimising the downtime of your core business by giving your Incident Response Team appropriate tools and measures to tackle the incident as soon as possible,
* Defining clear communication guidelines and plans for both internal and external stakeholders to help safeguard your company’s reputation,
* Ensuring regulatory compliance with an ever-evolving set of acts, regulations, and directives requiring very specific reporting at very specific intervals,
* Improving response times and reducing likelihood of an incident by finding areas where automation or improvements can be made.

How and where can you start your incident preparedness journey? In this blogpost, we will cover some of the most important aspects you can work on before facing an incident.

## Build your foundation and scope

As already depicted previously in this series of blogpost, when dealing with a crisis or incident, multiple teams operate, with very different but important objectives. Depending on the incident and its impact on the Business, one, multiple, or all teams may be involved. Each company has a different structure, different governance, and different standards and regulations to comply with. This inevitably has an impact on how incidents are handled. Therefore, you need to define the scope of your (Cybersecurity) Incident Response Process:

* do you have an overall incident management team handling all types of incidents (e.g., your Incident Management Team handles CyberSecurity incidents as well as Physical, IT, Business, and other types of incidents)?
* do you handle cyber incidents separately, or as part of the Major Incident Management Process (e.g., your Major Incident Management Team oversees teams handling all incidents types, including your Cyber Security Incident Management Team)?
* do you have external stakeholders playing a role in your incident response (e.g., retainer with external Incident Response provider)?
* do you provide your incident response process capability to other teams internally or externally (e.g., a subsidiary or remote branch)?

All of these points will drastically change the scope of your incident management process, and defining it correctly is the first step to ensure you do not interfere with another team’s process.

With this scope in mind, you can start determining and drafting the documents that you need. Among these potential documents, we recommend two in particular: the incident Response Plan, and Incident Response Playbooks.

* The Incident Response Plan will be your main governance document, defining your process and relevant information surrounding it: incident taxonomy and classification, people involved, and steps of the overall process to only name a few.
* Your Incident Response Playbook(s) will go further than your Plan, and will highlight the steps to be taken for particular incidents. These steps might have similarities between incidents types, but other will change drastically (the way you manage a Denial of Service incident will require different steps than a Data Exfiltration incident). These Playbooks will be particularly helpful for defining a common response process for your different Incident handlers, but also for training and briefing new members in your team.

## Determine how to trigger your Incident Response process

Now that you have defined the scope of your Incident Response Process, we need to figure out how to trigger it. This also raises the question of defining “What is an Incident?”. This seems easy, but has a lot of components to it:

* What is the threshold for an event to become an incident?
* When does the incident become part of something bigger, such as a crisis?
* Who triggers the Incident Response process?
* How can someone report a potential incident?
* Where, how, and to whom do we communicate during the Incident handling process?

You may also want to have different types of Incident severity or priority based on specific criteria, such as the type of Incident (this is where an Incident Taxonomy can be useful, such as the [ENISA RSIT](https://www.enisa.europa.eu/publications/reference-incident-classification-taxonomy)), the scale of the attack, the criticality of the systems impacted, or even the type of user impacted. By defining these criteria, you can start forming a table or matrix defining types of incidents:

| Incident Severity | Potential criteria | Examples |
| --- | --- | --- |
| Low | – Only one user or device impacted – Very low impact to Business – Pertains to an ...