---
title: Common Entra ID Security Assessment Findings – Part 1: Foreign Enterprise Applications With Privileged API Permissions
url: https://blog.compass-security.com/2026/03/common-entra-id-security-assessment-findings-part-1-foreign-enterprise-applications-with-privileged-api-permissions/
source: Over Security - Cybersecurity news aggregator
date: 2026-03-24
fetch_date: 2026-03-25T04:17:52.525620
---

# Common Entra ID Security Assessment Findings – Part 1: Foreign Enterprise Applications With Privileged API Permissions

## [Compass Security Blog](https://blog.compass-security.com "Compass Security Blog — Offensive Defense")

### Offensive Defense

* [Home](https://blog.compass-security.com/)
* [Archive](https://blog.compass-security.com/archive/)
* [Contact](https://blog.compass-security.com/contact/)
* [Newsletter](https://blog.compass-security.com/mailing-list-tigerinfo/)

* [Home](https://blog.compass-security.com/)
* [Archive](https://blog.compass-security.com/archive/)
* [Contact](https://blog.compass-security.com/contact/)
* [Newsletter](https://blog.compass-security.com/mailing-list-tigerinfo/)

# [Common Entra ID Security Assessment Findings – Part 1: Foreign Enterprise Applications With Privileged API Permissions](https://blog.compass-security.com/2026/03/common-entra-id-security-assessment-findings-part-1-foreign-enterprise-applications-with-privileged-api-permissions/ "Common Entra ID Security Assessment Findings – Part 1: Foreign Enterprise Applications With Privileged API Permissions")

[March 24, 2026](https://blog.compass-security.com/2026/03/common-entra-id-security-assessment-findings-part-1-foreign-enterprise-applications-with-privileged-api-permissions/ "Common Entra ID Security Assessment Findings – Part 1: Foreign Enterprise Applications With Privileged API Permissions")
 /
[Christian Feuchter](https://blog.compass-security.com/author/cfeuchte/ "Posts by Christian Feuchter")
 /
[0 Comments](https://blog.compass-security.com/2026/03/common-entra-id-security-assessment-findings-part-1-foreign-enterprise-applications-with-privileged-api-permissions/#respond)

*This post is part of a small blog series covering common Entra ID security findings observed during real-world assessments. Each article explores selected findings in more detail to support a clearer understanding of the underlying risks and practical implications.*

---

## Introduction

In the vast majority of tenants we [review](https://www.compass-security.com/en/services/security-reviews), there are enterprise applications that originate from another tenant (referred to here as *foreign*). While most of them do not have privileged Entra ID roles assigned, they often have extensive API permissions granted as application permissions. This can introduce risk because the operational security of those identities lies outside the direct control of the organization.

Let’s start from the beginning: what are enterprise applications and why are they required?

### What Are Enterprise Applications

An enterprise application is the service principal of an application within a tenant. In other words, it is the local identity created from an application object (app registration) and is represented in the Entra portal as an Enterprise Application. In the case of a foreign enterprise application, the globally unique app registration is located in another Entra ID tenant. Throughout this post, the term “enterprise application” will refer to the service principal object created in the tenant.

If a third-party Software as a Service (SaaS) application allows users from an Entra ID tenant to authenticate with their accounts, a corresponding foreign enterprise application must exist in the tenant. When users authenticate to such a multi-tenant application using their Entra ID identity, an enterprise application object is created automatically during consent, or it can be pre-provisioned by an administrator.

However, there is a second use case. Sometimes it is necessary to allow a third-party application or external organization to access tenant resources and perform actions without involving a user account. In such app-only scenarios, the enterprise application represents a service principal used for non-interactive authentication (conceptually comparable to a service account in Active Directory).

### What Are Application API Permissions in Entra ID

These third-party solutions use different Microsoft cloud APIs to perform the required actions. There are many APIs available. Some of them cover multiple services (for example, Microsoft Graph API), while others are specific to individual services (for example, SharePoint, Azure Key Vault, or Azure Resource Manager). Today, Microsoft Graph is most commonly used for tasks in Entra ID and Microsoft 365 services, which is why this post primarily focuses on that API.

To define which privileges an application has, granular API permissions (OAuth scopes)[1](#b7c97729-fbc1-481f-9ea8-34c12c7ac6fd) must be configured. Microsoft Graph allows permissions to be assigned at a very granular level and offers a large number of different permissions to choose from.

For most permissions, two variants exist:

* Delegated permissions[2](#6540c494-4f43-4f0f-a156-64e7f2d3f723): The enterprise application accesses the API in the context of a signed-in user.
* Application-only permissions[3](#43c2d800-8759-474c-8dcd-1859bc2788e2): The enterprise application runs as a background service without a signed-in user.

This blog post focuses on the second variant. As described, permissions can be defined relatively granularly. For example, if an enterprise application needs to access SharePoint sites, it is possible to choose between:

* Sites.Read.All — Read items in all site collections
* Sites.ReadWrite.All — Read and write items in all site collections
* Sites.FullControl.All — Full control of all site collections
* Sites.Archive.All — Archive or reactivate site collections without a signed-in user

### Understanding Application Authentication

When an application can act autonomously (without a user), it uses its own credentials to authenticate in the tenant and perform the required actions.

These credentials can be either a client secret (password) or a certificate. The credentials used to authenticate are typically:

* Present on the globally unique app registration object in the publisher’s tenant. These credentials allow authentication in every tenant worldwide where the corresponding enterprise application exists.
* In rare cases, credentials may be additionally added directly to the enterprise application in the consumer tenant. These credentials are not visible in the Entra admin portal but can be enumerated via API or tools such as [EntraFalcon](https://github.com/CompassSecurity/EntraFalcon).

Since the credentials for the application are controlled in the external tenant, they lie outside the direct control of the consumer organization. If the external tenant is not properly secured or monitored, attackers might be able to steal existing credentials or add new ones and then authenticate as the application in other tenants where the enterprise application is present.

It is important to understand that Conditional Access policies do not apply to sign-ins by foreign enterprise applications. While Microsoft Entra Workload ID Premium allows targeting single-tenant enterprise applications with Conditional Access, this is currently not supported for multi-tenant applications[4](#9e7b4d40-d30f-4e91-8326-ae21465272ca). Therefore, it is not possible, for example, to restrict access based on IP address.

The following simplified diagram illustrates the relationship between the app registration, the foreign-controlled enterprise application (service principal) created in the tenant, and the credentials used in multi-tenant scenarios:

[![Entra ID app registrations and enterprise applications in a multitenant setup](https://blog.compass-security.com/wp-content/uploads/2026/03/image-16.png)](https://blog.compass-security.com/wp-content/uploads/2026/03/image-16.png)

## Abuse Scenarios

The following examples demonstrate how extensive application permissions assigned to foreign enterprise applications could be abused.

### Example 1: Privileged Access to SharePoint

In this example, a foreign enterprise application with the following properties exists:

* Name: **SharePoint\_Helper**
* Application API Permission: **Sites.Read.All**
* Application / Client ID: **efa20d43-76f8-432d-b28...