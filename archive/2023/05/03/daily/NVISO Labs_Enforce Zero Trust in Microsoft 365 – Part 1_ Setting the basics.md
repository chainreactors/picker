---
title: Enforce Zero Trust in Microsoft 365 – Part 1: Setting the basics
url: https://blog.nviso.eu/2023/05/02/enforce-zero-trust-in-microsoft-365-part-1-setting-the-basics/
source: NVISO Labs
date: 2023-05-03
fetch_date: 2025-10-04T11:38:56.871263
---

# Enforce Zero Trust in Microsoft 365 – Part 1: Setting the basics

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

# Enforce Zero Trust in Microsoft 365 – Part 1: Setting the basics

[NVISO Blog](https://blog.nviso.eu/author/nviso-blog/ "Posts by NVISO Blog")

[Microsoft 365](https://blog.nviso.eu/category/cloud-security/microsoft-365/), [Cloud Security](https://blog.nviso.eu/category/cloud-security/)

May 2, 2023May 2, 2023
8 Minutes

This first blog post is part of a series of blog posts related to the implementation of Zero Trust approach in Microsoft 365. This series will first cover the basics and then deep dive into the different features such as Azure Active Directory (Azure AD) Conditional Access policies, Microsoft Defender for Cloud Apps policies, Information Protection and Microsoft Endpoint Manager, to only cite a few.

In this first part, we will go over the basics that can be implemented in a Microsoft 365 environment to get started with Zero Trust. For the purpose of the blog post, we will assume that our organization decided to migrate to the cloud. We just started investigating what are the quick wins that can be easily implemented, what are the features that will need to be configured to ensure security of identities and data, and what the more advanced features that could be used to meet specific use cases would be.

Of course, the journey to implement Zero Trust is not an easy one. Some important decisions will need to be made to ensure the relevant features are being used and correctly configured according to your business, compliance, and governance requirements without impacting user productivity. Therefore, the goal of this series of blog posts is to introduce you possible approaches to Zero Trust security in Microsoft 365.

## Introduction

However, before starting we need to set the scene by quickly going over some principles.

First, what is a Zero Trust security approach? Well, this security model says that you should never trust anyone and that each request should be verified regardless of where the request originates or what the accessed resource is. In other words, this model will assume that each request comes from an uncontrolled or compromised network. Microsoft provides this nice illustration to represent the primary elements that contribute to Zero Trust in a Microsoft 365 environment:

![Zero Trust approach in Microsoft 365](https://blog.nviso.eu/wp-content/uploads/2022/03/zero-trust-architecture-1-1024x576.png)

Zero Trust approach in Microsoft 365

We will go over these components as part of this blog post series.

You may wonder why I have decided to discuss Zero Trust in Microsoft 365. Because I think it is one of the most, if not the most, important aspects of a cloud environment. Indeed, with cloud environments, identities are considered as the new perimeter as these identities can be used to access Internet-facing administrative portals and applications from any Internet-connected device.

Furthermore, even when security controls are enforced, it does not mean that the environment is secure. There were many attacks these past few months/years that allowed attackers to bypass security controls through social engineering, and phishing attacks, for example. Therefore, the goal is more to reduce the potential impact of a security breach on the environment than to prevent attacks from succeeding.

Finally, let’s go over some Microsoft 365 principles. When an organization signs up for a subscription of Microsoft 365, an Azure AD tenant is created as part of the underlying services. For data residency requirements, Microsoft lets you choose the logical region where you want to deploy your instance of Azure AD. This region will determine the location of the data center where your data will be stored. Moreover, Microsoft 365 uses Azure AD to manage user identities. Azure AD offers the possibility to integrate with an on-premises Active Directory Domains Services (AD DS) but also to manage integrated applications. Therefore, you should/must/have to understand that most of the work to set up a Zero Trust approach will be done in Azure AD.

## Let’s get started!

Our organization just bought a paid Microsoft 365 subscription which comes with a free subscription to Microsoft Azure AD. The free Azure AD subscription includes some basic features that will allow us to get started with our journey. Let’s go over them!

### Security Defaults

The first capability is the Azure AD Security Defaults. The Security Defaults are a great first step to improve the security posture by enforcing specific access controls:

* Unified Multi-Factor Authentication (MFA) registration: All users in the tenant **must** register to MFA. With Security Defaults, users can only register for Azure AD Multi-Factory Authentication by using the Microsoft Authenticator app using a push notification. Note that once registered, users will have the possibility to use a verification code (Global Administrator will also have the possibility to register for phone call or SMS as second factor). Another important note is that disabling MFA methods may lead to locking users out of the tenant, including the administrator that configured the setting, if Security Defaults are being used;
* Protection of administrators: Because users that have privileged access have increased access to an environment, users that have been assigned to specific administrator roles are required to perform MFA each time they sign in;
* Protection of users: All users in the tenant are required to perform MFA whenever necessary. This is decided by Azure AD based on different factors such as location, device, and role. Note that this does not apply to the Azure AD Connect synchronization account in case of a hybrid deployment;
* Block the use of Legacy Authentication Protocols: Legacy authentication protocols refer to protocols that do not support Multi-Factor Authentication. Therefore, even if a policy is configured to require MFA, users will be allowed to bypass MFA if such protocols are used. In Microsoft 365, legacy authentication is made from clients that don’t use modern authentication such as Office versions prior to Office 2013 a mail protocols such as IMAP, SMTP, or POP3;
* Protection of privileged actions: Users that access the Azure Portal, Azure PowerShell or Azure CLI must complete MFA.

These features already allow to increase the security posture by enforcing strong authentication. Therefore, they can be considere...