---
title: Become Big Brother with Microsoft Purview
url: https://blog.nviso.eu/2024/03/06/become-big-brother-with-microsoft-purview/
source: NVISO Labs
date: 2024-03-07
fetch_date: 2025-10-06T17:08:42.523253
---

# Become Big Brother with Microsoft Purview

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

# Become Big Brother with Microsoft Purview

[Matheo Boute](https://blog.nviso.eu/author/matheo-boute/ "Posts by Matheo Boute")

[Microsoft 365](https://blog.nviso.eu/category/cloud-security/microsoft-365/)

March 6, 2024March 5, 2024
12 Minutes

## Introduction

With the never-ending amount of data we generate, process, and share within and between companies, and the value this information can hold – such as personal data, top secret documents, or even information related to national security – it is natural that one of the main interests in cybersecurity is data security. Let it be data discovery, classification, access control, encryption or Data Loss Prevention (DLP), it is often unclear in which direction to go or which product to use to start tackling the long journey of data security.

In this article, I will focus on Microsoft Purview and its data security capabilities, starting with an overview of the best practices. For those who do not know it yet, Microsoft Purview is a comprehensive set of solutions that aims to help companies in governing, protecting and managing data. Microsoft Purview was born from the merging of Azure Purview and Microsoft 365 compliance solutions.

![Microsoft Purview pillars.](https://blog.nviso.eu/wp-content/uploads/2024/03/image-16.png)

Figure 1: Microsoft Purview pillars

To demonstrate the credibility of Microsoft when it comes to data security, it is important to know that Microsoft was recognized as a leader in The Forrester Wave: Data Security Platforms, Q1 2023 and Microsoft Purview product integrates well with the rest of the Microsoft solutions, such as Entra ID and Microsoft 365. You can find the official statement from Microsoft here: [Microsoft a Leader in the 2023 Forrester Wave™ for Data Security Platforms | Microsoft Security Blog](https://www.microsoft.com/en-us/security/blog/2023/03/22/microsoft-recognized-as-a-leader-in-the-forrester-wave-data-security-platforms-q1-2023/)

## Theory and practice

As we all know now that theory will only take you this far, it is important to map the theoretical concept of information protection and practical solutions. It is commonly accepted that the four pillars that serve as a roadmap in information protection can be summarized as follows:

* **Know your data**: You want to know **what** data is being used and generated, and **how** it is used and generated.
* **Protect your data**: Following the what and how, you must create and maintain the **first line of defense** for your information by enforcing security and access controls.
* **Prevent data loss**: Intentional or accidental data leaks can and will happen sooner or later. Defining and enforcing the use cases to mitigate will represent the **last line of defense** for your data.
* **Govern your data**: On top of the three other pillars, it is important to put in place governance processes to **identify the gaps** that remain uncovered by your current solutions. Additionally, a good governance helps you with achieving compliance with the regulations applicable to your company. However, I will not extend myself further on this in this blog post as the focus is data security.

The good news is that Microsoft Purview does cover these four pillars, by providing the tools and solutions shown in the following picture:

![And example of the Microsoft Purview products mapped to the data security pillars.](https://blog.nviso.eu/wp-content/uploads/2024/03/image-2.png)

Figure 2: Microsoft Purview features mapping

*Note that the above is not an exhaustive list of all Microsoft Purview tools, but rather an example of the mapping between the theory and some aspects of Microsoft Purview.*

It must be noted that to use Microsoft Purview to the fullest extent possible, we strongly advise using the **Entra ID Premium P2 license** and providing users with **Microsoft 365 Enterprise E5** licenses is mandatory.

## Triangle of Paranoia

Now I would like to introduce you to the concept of the triangle of paranoia. In data protection, we want to know and control everything, everywhere, all at once. How to do so? Well, let’s have a look at the diagram below:

![The triangle of paranoia helps you understand the three main tool for data security in Microsoft Purview.](https://blog.nviso.eu/wp-content/uploads/2024/03/image-3.png)

Figure 3: Triangle of paranoia

On the top sits the **Data Classification**, where the goal is to discover and classify information. There are multiple ways to proceed with Data Classification. For example, it can be done manually using sensitivity labels (i.e., tags that the users apply to their documents and emails), or automatically by identifying the content of documents based on information types or regular expressions. It is crucial to understand the importance of knowing what data and how it is used across the company. Knowledge is power, and it is especially true when it comes to data protection.

On the left corner of the triangle, we have the **Data Loss Prevention (DLP)** policies. Each of these policies can contain multiple rules whose goal is to restrict or audit data transfers that are deemed forbidden. The DLP rules can be triggered upon identification of a sensitivity label, or when risky activities – such as copying files to an untrusted network drive – are identified and remediation actions can be taken in the Microsoft 365 suite or directly on the device (i.e., Endpoint DLP). The reason why one policy can contain multiple rules is to have different actions based on slightly different conditions within the same scope of the policy. For example, a single event consisting of an accidental leak of a document will only trigger a restriction and a medium severity alert. While the same kind of event but repeated hundreds of times might be an indicator of intentional and malicious leak of information, therefore additional actions can be triggered, the severity of the alerts will be higher, and notification would be sent to administrators via emails. And the two rules will be inside the same policy that aims to protect sensitive documents from being sent externally via emails.

On the right side of the triangle, **the Insider Risk Management (IRM)** aims to identify and reduce the risk caused by malicious insiders, by gathering and correlating indicators and applying policies to raise the risk level of a user. The policies...