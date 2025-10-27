---
title: Securing Microsoft Entra ID: Lessons from the Field – Part 1
url: https://blog.nviso.eu/2025/09/25/securing-microsoft-entra-id-lessons-from-the-field-part-1/
source: NVISO Labs
date: 2025-09-26
fetch_date: 2025-10-02T20:42:40.360433
---

# Securing Microsoft Entra ID: Lessons from the Field – Part 1

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

# Securing Microsoft Entra ID: Lessons from the Field – Part 1

[Christos Gourzoulidis](https://blog.nviso.eu/author/christos-gourzoulidis/ "Posts by Christos Gourzoulidis")

[Azure](https://blog.nviso.eu/category/cloud-security/azure/), [Blue Team](https://blog.nviso.eu/category/blue-team/), [cloud](https://blog.nviso.eu/category/cloud/), [Cloud Security](https://blog.nviso.eu/category/cloud-security/), [Microsoft Entra ID](https://blog.nviso.eu/category/cloud-security/microsoft-entra-id/)

September 25, 2025September 25, 2025
9 Minutes

---

![](https://blog.nviso.eu/wp-content/uploads/2025/07/Securing-Microsoft-Entra-ID-–-Lessons-from-the-Field-1024x512.png)

This multipart blog series is focused on the real-world lessons learned while securing Microsoft Entra ID. Based on hands-on experience across various environments and organizations, we’ll explore the practical, high-impact strategies that work and more importantly, the common misconfigurations, overlooked settings, and pitfalls that can expose your identity perimeter.

Throughout the series, we’ll cover both foundational and advanced topics: from hardening your hybrid identity configuration, to addressing Conditional Access misconfigurations, securing Privileged Access assignments, and much more.

To start, we’ll align on what “securing Entra ID” really means. This includes understanding the threat model behind identity-based attacks, what Microsoft provides out-of-the-box, and where gaps or misconfigurations often exist, even in mature environments.

## What is Entra ID and why do adversaries target it?

> Microsoft Entra ID is a product family name for Microsoft’s identity and access management solutions. It is **not** a replacement for Active Directory but rather a cloud-based identity and access management service that enables employees to securely access resources. These resources include Microsoft 365, the Azure Portal, SaaS applications, and even on-premises applications.

Attackers target identity as the first layer of defense, using methods like phishing, token theft, or exploiting misconfigured Conditional Access. Once they compromise identity, they can access the environment and employ techniques like lateral movement and privilege escalation to expand their foothold.

In the screenshot below we will see an overview of an attack process:

![](https://blog.nviso.eu/wp-content/uploads/2025/07/image-26-1024x119.png)

In a typical attack process, it often begins with a phishing email, where the attacker creates a message aimed at tricking the recipient into clicking on a malicious link. Once the victim clicks on that link, credential theft occurs, allowing the attacker to harvest usernames and passwords, granting them initial access to the network. Moving forward, the attacker engages in lateral movement, navigating through the network to access multiple devices or accounts, expanding their foothold. As the attack progresses, the attacker seeks privilege escalation, upgrading their access rights to obtain higher-level privileges, such as administrative rights, enabling them to gain control over more critical resources within the network.

In cloud environments, lateral movement frequently occurs in the identity and access management (IAM) layer rather than across networks. Adversaries may capture session or refresh tokens (for example via Adversary-in-the-Middle phishing), impersonate users, bypass multi-factor authentication and Conditional Access, abuse service principals or misconfigured roles, or even register “ghost” devices. In this model, attackers pivot through cloud resources and IAM relationships, making identity the primary attack surface.

> According to IBM’s Threat Intelligence Index [1], there has been a significant rise in the delivery of infostealers via phishing emails, with an increase of 84% per week. Moreover, identity-based attacks now constitute 30% of total intrusions, highlighting the critical need for enhanced security measures to protect against unauthorized access and data breaches.

Let’s start diving into the main concepts of securing our Entra ID environment, especially when we have a modern hybrid working environment.

## Hybrid Identity in the Modern Workplace

A hybrid identity is one that spans on both on-premises infrastructure and cloud-based services, enabling users to access resources across environments with a single identity. For many organizations, this model is still the one that is most commonly used.

To bridge these two worlds, Microsoft provides **Entra Connect**, which comes in two options: Connect Sync and Cloud Sync. Both of these are very useful and powerful, but they also introduce complexity and with complexity, risk comes. In real-world environments, we’ve frequently seen hybrid identity setups misconfigured, with issues like unnecessary Seamless SSO, stale or unrotated Kerberos decryption keys, and silent directory sync errors that can go unnoticed for extended periods.

This section unpacks those common pitfalls, explains what to watch out for, and helps you align your hybrid identity strategy with secure, modern best practices.

### **New application based authentication in Entra ID for stronger security**

Microsoft has streamlined the upgrade process. Now, you can download the latest version of Entra Connect and benefit from the application-based authentication, moving away from the traditional username/password previously used for syncing identities to the cloud.

![](https://blog.nviso.eu/wp-content/uploads/2025/09/image-40.png)

However, while certificate-based authentication is indeed more secure and helps reduce the overall attack surface, it introduces a new layer of risk. The service principalthat authenticates using the certificate becomes a critical identity and any strange behavior should be monitored carefully, as it operates silently in the background and may be overlooked in traditional security audits.

There are three options to choose for certificate and application management:

1. Managed by Microsoft Entra Connect
2. Bringing your own application
3. Bringing your own certificate

If you don’t already manage your own certificates, use the recommended Microsoft-managed option which offers both security and little administrative overhead.

![](https://blog.nviso.eu/wp-content/uploads/2025/07/image-56-1024x614.png)

The certificate is stored...