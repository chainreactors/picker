---
title: Microsoft Purview – Evading Data Loss Prevention policies
url: https://blog.nviso.eu/2024/12/18/microsoft-purview-evading-data-loss-prevention-policies/
source: NVISO Labs
date: 2024-12-19
fetch_date: 2025-10-06T19:36:44.410049
---

# Microsoft Purview – Evading Data Loss Prevention policies

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

# Microsoft Purview – Evading Data Loss Prevention policies

[Matheo Boute](https://blog.nviso.eu/author/matheo-boute/ "Posts by Matheo Boute")

[Microsoft 365](https://blog.nviso.eu/category/cloud-security/microsoft-365/), [Cloud Security](https://blog.nviso.eu/category/cloud-security/)

December 18, 2024December 18, 2024
10 Minutes

## Introduction

Microsoft Purview is a comprehensive solution that helps organizations manage and protect their data across various environments, including on-premises, multi-cloud, and software-as-a-service (SaaS) platforms. It provides a unified data catalog, data classification, and data security capabilities, enabling organizations to gain insights into their data landscape, secure their data accordingly, and ensure compliance with regulatory requirements.

![Illustration of Microsoft Purview Pillars, showcasing its capabilities in managing and protecting data across on-premises, multi-cloud, and SaaS environments.](https://blog.nviso.eu/wp-content/uploads/2024/12/image.png)

Figure 1: Microsoft Purview pillars.

The data security toolset includes Sensitivity Labels and Data Loss Preventions, which are the tools that this blog post focuses on:

* Sensitivity labels are used to classify and protect data based on its content. These labels can be applied to documents and emails to enforce protection settings such as encryption and content marking. Sensitivity labels helps organizations classify their information, but also safeguard their sensitive information by ensuring that only authorized users can access and share it. On the technical side, the Sensitivity label is represented by additional metadata added to the file or email.
* Data Loss Prevention (DLP) refers to a set of policies and technologies designed to detect and prevent the unauthorized transmission of potentially sensitive data inside and outside an organization’s boundaries.

While Microsoft Purview provides interesting features related to data security, the solution remains prone to some very old and always relevant vulnerabilities: the human factor and bad design decisions.

This blog post explores an exfiltration scenario that highlights the importance of robust DLP policies within Microsoft Purview. We will examine how Sensitivity Labels function, why inadequate DLP measures can lead to data leaks, and we’ll introduce best practices for strengthening an organization’s data protection measures. If you are not familiar with Microsoft Purview, Sensitivity Labels, Data Loss Prevention, or Insider Risk Management, I recommend having a look at this other blog post: [Become Big Brother with Microsoft Purview – NVISO Labs](https://blog.nviso.eu/2024/03/06/become-big-brother-with-microsoft-purview/)

## Evasion scenario

### Context

Alex is an internal employee in the company Purview Territory. Alex has access to an Entra ID joined Windows 10 workstation that is managed in Intune. Through the device, Alex can access and sync files from SharePoint Online and emails from Exchange Online. Alex will try to exfiltrate docx and pdf files containing sensitive information via email and to upload the files to an online storage platform.

![Depiction of Alex, an employee at Purview Territory, using a Windows 10 workstation managed by Intune to access SharePoint and Exchange Online, attempting to exfiltrate sensitive docx and pdf files via email and online storage.](https://blog.nviso.eu/wp-content/uploads/2024/12/image-1.png)

Figure 2: Alex initial access.

### Protection in place

In Microsoft Purview, the sensitivity label ‘Super Secret’ can be applied to files and emails, it is the most sensitive level of information. Other sensitivity labels exist, and the policy that makes all labels available to Alex also enforces the application of a label in order to save a file or send an email, making the suppression of sensitivity label impossible in theory. Emails inherit the sensitivity label from the attachment if it has a higher level of sensitivity. In addition, Insider Risk Management is used to investigate and raise alerts if users downgrade sensitivity labels.

Two Data Loss Prevention policies exist with a unique rule for each with the following settings:

* DLP 1 – Rule 1: Files labeled with ‘Super Secret’ cannot be shared externally, and emails labeled with ‘Super Secret’ cannot be sent to external domains. This policy is processed in the Microsoft 365 ecosystem.
* DLP 2 – Rule 1: Files labeled with ‘Super Secret’ cannot be uploaded to unauthorized online storage. This policy is processed on the endpoint thanks to the Defender for Endpoint integration.

![Image illustrating two Data Loss Prevention (DLP) policies: DLP 1 prevents sharing 'Super Secret' files and emails externally within Microsoft 365, while DLP 2 blocks uploading such files to unauthorized online storage via Defender for Endpoint.](https://blog.nviso.eu/wp-content/uploads/2024/12/image-2.png)

Figure 3: Existing protection.

### Failed attempt

Alex tries first to exfiltrate the two files via email. The files are added as attachments and then sent to an external email address:

![GIF showing Alex attempting to exfiltrate two files by attaching them to an email and sending it to an external address.](https://blog.nviso.eu/wp-content/uploads/2024/12/Email_blocked_1920.gif)

Figure 4: Failed email exfiltration.

When Alex clicks “Send”, the action is blocked directly in the client and the policy tip defined in the DLP appears. Note: If the client cannot process the DLP rule for some reasons, it will be processed in Exchange Online and the email will bounce back with a delivery failure message instead.

Alex tries a second time to exfiltrate the two files via an online storage platform. The files are simply dragged and dropped into the website:

![GIF depicting Alex's second attempt to exfiltrate two files by dragging and dropping them into an online storage platform's website.](https://blog.nviso.eu/wp-content/uploads/2024/12/Block_online_demo-2.gif)

Figure 5: Failed online storage exfiltration.

When the file is dropped into the website, the Microsoft Purview Extension identifies the sensitivity label and prevents the action. This browser extension is enabled by default in Microsoft Edge and it can be added to Google Chrome and Firefox via Group Policy Object (GPO) or Intune Configuration Profile.

Overall, the exfiltration...