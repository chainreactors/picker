---
title: ICS Hard Knocks: Mitigations to Scenarios Found in ICS/OT Backdoors & Breaches
url: https://www.blackhillsinfosec.com/mitigations-to-scenarios-found-in-ics-ot-backdoors-and-breaches/
source: Black Hills Information Security
date: 2024-12-06
fetch_date: 2025-10-06T19:39:45.729587
---

# ICS Hard Knocks: Mitigations to Scenarios Found in ICS/OT Backdoors & Breaches

[![Black Hills Information Security, Inc.](https://www.blackhillsinfosec.com/wp-content/uploads/2025/03/BHIS_TEXT_BHIS.png)](https://www.blackhillsinfosec.com "Black Hills Information Security, Inc.")

[RSS](https://www.blackhillsinfosec.com/feed/)

* [All Services](https://www.blackhillsinfosec.com/services/)
  + [Complete Service Guide](https://www.blackhillsinfosec.com/services/complete-service-guide/)
  + [Active SOC](https://www.blackhillsinfosec.com/services/active-soc/)
  + [AI Security Assessments](https://www.blackhillsinfosec.com/services/ai-security-assessments/)
  + [Blockchain Security](https://www.blackhillsinfosec.com/services/blockchain-security/)
  + [Blue Team Services](https://www.blackhillsinfosec.com/services/blue-team-services/)
  + [Continuous Penetration Testing](https://www.blackhillsinfosec.com/services/antisoc/)
  + [High-Profile Risk Assessments](https://www.blackhillsinfosec.com/services/high-profile-risk-assessments/)
  + [Incident Response](https://www.blackhillsinfosec.com/services/incident-response/)
  + [Penetration Testing](https://www.blackhillsinfosec.com/services/)
* [Contact Us](https://www.blackhillsinfosec.com/contact-us/)
  + [Contact Us](https://www.blackhillsinfosec.com/contact-us/)
  + [Email Sign-Up](https://mailchi.mp/blackhillsinfosec.com/bhis-sign-up)
* [About Us](https://www.blackhillsinfosec.com/who-we-are/)
  + [Security Consultants](https://www.blackhillsinfosec.com/about/security-analysts/)
  + [Admin](https://www.blackhillsinfosec.com/about/admin-staff/)
  + [SOC Team](https://www.blackhillsinfosec.com/about/soc-team/)
  + [BHIS Family of Companies](https://www.blackhillsinfosec.com/bhis-tribe-of-companies/)
* [Free Resources](https://www.blackhillsinfosec.com/free-cybersecurity-tools/)
  + [Blogs](https://www.blackhillsinfosec.com/blog/)
  + [Free Cybersecurity Tools](https://www.blackhillsinfosec.com/free-cybersecurity-tools/)
  + [Free Cybersecurity Webcasts](https://www.blackhillsinfosec.com/free_cybersecurity_webcasts/)
  + [Podcasts](https://podcasts.apple.com/us/podcast/black-hills-information-security/id1410835265)
  + [RITA](https://www.activecountermeasures.com/free-tools/rita/)
* [Training](https://www.blackhillsinfosec.com/bhis-and-antisyphon-training/)
  + [BHIS & Antisyphon Training](https://www.blackhillsinfosec.com/bhis-and-antisyphon-training/)
  + [WWHF Conference](https://wildwesthackinfest.com)
* [Online Community](https://blackhillsinfosec.com/community)
  + [Discord](https://discord.gg/BHIS)
  + [LinkedIn](https://www.linkedin.com/company/black-hills-information-security/)
  + [YouTube](https://www.youtube.com/c/BlackHillsInformationSecurity/videos)
  + [Bluesky](https://bsky.app/profile/bhinfosecurity.bsky.social)
  + [Twitter/X](https://twitter.com/BHinfoSecurity)
  + [Upcoming Events](https://blackhillsinfosec.com/events)
* [Fun Stuff](https://spearphish-general-store.myshopify.com/)
  + [Backdoors & Breaches](https://www.blackhillsinfosec.com/tools/backdoorsandbreaches/)
  + [Merch, Zines & More](https://spearphish-general-store.myshopify.com/)
  + [PROMPT# Zine](https://www.blackhillsinfosec.com/prompt-zine/)
  + [REKCAH](https://www.blackhillsinfosec.com/rekcah/)
  + [Books](https://www.blackhillsinfosec.com/tools/books/)

5
Dec
2024

[Brian Ireland](https://www.blackhillsinfosec.com/category/author/brian-ireland/), [Informational](https://www.blackhillsinfosec.com/category/informational/), [InfoSec 201](https://www.blackhillsinfosec.com/category/infosec-201/)
[B&B](https://www.blackhillsinfosec.com/tag/bb/), [Backdoors & Breaches](https://www.blackhillsinfosec.com/tag/backdoors-breaches/), [ICS/SCADA](https://www.blackhillsinfosec.com/tag/ics-scada/), [Industrial Control Systems](https://www.blackhillsinfosec.com/tag/industrial-control-systems/), [Initial Compromise](https://www.blackhillsinfosec.com/tag/initial-compromise/)

# [ICS Hard Knocks: Mitigations to Scenarios Found in ICS/OT Backdoors & Breaches](https://www.blackhillsinfosec.com/mitigations-to-scenarios-found-in-ics-ot-backdoors-and-breaches/)

![](https://www.blackhillsinfosec.com/wp-content/uploads/2024/12/BIreland-150x150.png)

| [Brian Ireland](https://www.blackhillsinfosec.com/team/brian-ireland/)

![](https://www.blackhillsinfosec.com/wp-content/uploads/2024/12/BLOG_chalkboard_00700.png)

Hello, my name is Brian Ireland. I currently have over 14 years of experience in support of Energy Sector utility, NERC, CIP, and ICS protections. I spent those 14 years dealing with physical protections from door locks, cameras, and card readers, as well as cybersecurity design and implementation of network IDS, network isolation policy, SEIM, SOAR and AV deployment. Experienced in utilizing best practices and adhering closely to the Purdue Enterprise Reference Architecture (PERA), I was part of a small team that was able to create defensible, defense-in-depth OT/ICS (Operational Technologies/Industrial Control Systems) environments from 2009 to current.

This blog will be referencing the [ICS/OT Backdoors & Breaches](https://spearphish-general-store.myshopify.com/products/ics-ot-backdoors-breaches-core-deck-v1) expansion deck created by BHIS and Dragos. We will be reviewing the ICS-focused Initial Compromise cards that are used to simulate a cyber incident and suggest potential mitigations to what is presented.

### **Some Key Takeaways to a Successful ICS Security Program**

* OT/ICS operations inclusion: Cybersecurity has traditionally been an IT operations concern. OT/ICS operations are very production focused, and security is normally a bolt-on solution. ICS vendors traditionally will not offer security-based solutions unless asked for, so make sure security is baked into any project. Make sure you’re consulting with your ICS administrators and operators, as they are working with these systems on a daily basis and can be your best eyes and ears to learn about potential issues.

* OT/ICS technologies predate modern IT cyber software and devices; it’s not uncommon to see an RTU/PLC/HMI\* that is 10+ years old. Hardware and software devices within the ICS environments may be implemented and remain untouched from the upgrade/update perspective for several years, whether due to updates being unavailable or unsupported by the vendor.

* Isolation via secured enclaves will greatly reduce the impact and prevent scope creep. If you place your operational ICS environments at your greatest trust level and only allow outbound traffic, this will greatly aid in reducing threat vectors. The control plane should be contained within your highest trust level networks. You should never control access to your ICS network from a less trusted network, like corporate lan, for example.

* Adding cyber and physical security will have an impact on daily operations; the key is to work with OT to minimize impact and ensure there is mutual understanding of the benefits to securing these operations. If an ICS system is compromised, there may not be an operation to be performed until the threat is mitigated.

* Regulatory requirements should be the entry level to a good security program. A good security program will be compliant with most governing bodies; inversely, a good compliance program may NOT be very secure. As an example: NERC CIP-005 v3 R1.5 requires adherence to CIP-007 v3 R4 required antivirus on Electronic Security Perimeter (ESP) access control point devices (a layer3 boundary device would have to have AV solution installed) by strict adherence to the regulations, all ICS edge devices would have to allow AV software to be installed. Thus, excluding best of breed network edge devices in lieu of more vulnerable software-based devices or file for technical feasibility exception to requirement and list the compensating measures.

* Leadership buy-in: Without support from upper management affecting long standing OT/ICS operation process’ or developing a solid security practice will be next to impossible. There is little-to-no inc...