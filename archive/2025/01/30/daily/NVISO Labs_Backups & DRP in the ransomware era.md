---
title: Backups & DRP in the ransomware era
url: https://blog.nviso.eu/2025/01/29/backups-drp-in-the-ransomware-era/
source: NVISO Labs
date: 2025-01-30
fetch_date: 2025-10-06T20:09:01.647455
---

# Backups & DRP in the ransomware era

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

# Backups & DRP in the ransomware era

[NVISO Blog](https://blog.nviso.eu/author/nviso-blog/ "Posts by NVISO Blog")

[Cyber Architecture](https://blog.nviso.eu/category/cyber-architecture/), [Ransomware](https://blog.nviso.eu/category/ransomware/)

January 29, 2025January 29, 2025
5 Minutes

In today’s digital landscape, the threat of ransomware has forced organizations to reevaluate their disaster recovery plans. Traditional approaches to data protection were focused primarily on high availability and are no longer sufficient. As cyber threats evolve, so must our strategies for safeguarding critical information. This blog post explores the principles and architectures needed to build a robust, ransomware-resilient backup and recovery infrastructure that ensures data integrity and availability during business-critical incidents.

## Ransomware makes us rethink the way we do DRP

It’s important to understand that backups are not synonymous with high availability. While data replication and system redundancy are crucial, they do not equal the ability to restore an environment to a previous state. High availability protects against system failures and power outages but can still be compromised by ransomware attacks as they typically do not cause downtime, meaning systems remain available from a redundancy perspective. The key distinction here is between system availability and data availability. As a result, backup and recovery capabilities are essential for preventing data loss during ransomware incidents.

![traditional DRP vs ransomware](https://blog.nviso.eu/wp-content/uploads/2024/12/drp-1024x391.png)

## Old best practices still apply today

In this section, we will explore how to create a ransomware-resilient backup solution. Although there is no universal solution or design, three core principles should be applied to every environment:

1. **3-2-1 Backup Strategy**: Maintain at least three copies of your backup data, with two stored on different types of media, and one stored offsite in a different physical location. This way, at least one copy is always protected against failures of the storage medium and external factors such as disasters.
2. **Segmentation o****f** **Data**: Store your backups in a logically separate environment that is not permanently connected to the rest of the environment. Additionally, a storage rotation scheme can be implemented to add an extra layer of data protection (e.g., online fast storage, offline fast storage, offline slow storage, long-term archival storage). This principle will help to protect the backup data from being breached during an intrusion.
3. **Isolation of Accounts**: Implement an independent access control system for the backup environment (e.g., no integration with your main Active Directory) and enforce least privilege access policies. Just as the previous principle, this will prevent adversaries from trivially breaching the backup environment with compromised credentials.

Based on these principles, we can create a high-level reference architecture. This involves building an isolated and independent backup and recovery zone with its own resources and access controls. This zone serves as the primary secure storage location for all backup data, which is transferred from various digital environments such as workplace devices, server parks, and cloud services. Ideally, this backup zone should be divided into three sub zones: one for the backup infrastructure, one for the data storage, and one for the dedicated recovery infrastructure.

So far, the issue has just been moved, however. Because how can this isolated backup zone be protected? While there is no single solution again, several options are available to suit different needs:

* **Periodic Air-Gap**: Periodically connect storage devices to the network for backup purposes and then disconnect them. Physical access to the premises would be needed to access the backup environment, drastically lowering the likelihood for adversaries to infect this data during a breach.
* **Tapes and Removable Media**: Write backup data to magnetic tapes or removable media and store them offline. The same approach as above, but instead with the data carriers themselves rather than the whole backup environment.
* **Fully** **Separate** **Network Zone**: Create a segmented and isolated network zone, forming an independent network bubble. By implementing this strategy, adversaries can reach the backup environment but will not be able to enter and infect it.
* **Third-Party/Cloud Storage**: Store backups in a third-party independent site and/or in the cloud with adequate isolation. The same approach as the option above, but hosted at a third-party.
* **Immutable Backups**: Use technology that employs “Write Once, Read Many” (WORM) systems to guarantee that data cannot be modified once written to the storage medium. As a result, adversaries will not be able to overwrite or remove the original data.

![on-premises backup reference architecture design](https://blog.nviso.eu/wp-content/uploads/2025/01/onprem-1024x775.png)

## How does it work?

During an incident, the isolated backup zone acts as a safe haven while all other systems may be compromised. Once the restoration order of your systems and services has been confirmed, the recovery infrastructure can start restoring data from the backups. It is crucial that the recovery zone can only pull data from the isolated backup zone, with no data being pushed into the recovery zone to avoid data tampering. The restored data or systems should then be tested and validated for integrity to ensure the effectiveness of your backup and recovery solution. To verify this, consider the following questions:

* Is the data accurate and captured at the correct time?
* Does the data have the expected volume and is it in the appropriate format?
* Can the data be accessed and utilized when required?
* Is the data clean, uninfected, and unaltered, ensuring it can be fully trusted?

Once verified, the data can be reintroduced into the original environment (ensuring no reinfection) or into a new, clean “green-field” setup, possibly in the cloud.

***A side note on backup types***
While it is not the goal to reiterate the advantages and disadvantages of incremental, differential, and full backups, it is important to highlight that the choice of backup type will influence t...