---
title: From Enumeration to Findings: The Security Findings Report in EntraFalcon
url: https://blog.compass-security.com/2026/03/from-enumeration-to-findings-the-security-findings-report-in-entrafalcon/
source: Over Security - Cybersecurity news aggregator
date: 2026-03-17
fetch_date: 2026-03-18T04:22:35.780707
---

# From Enumeration to Findings: The Security Findings Report in EntraFalcon

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

# [From Enumeration to Findings: The Security Findings Report in EntraFalcon](https://blog.compass-security.com/2026/03/from-enumeration-to-findings-the-security-findings-report-in-entrafalcon/ "From Enumeration to Findings: The Security Findings Report in EntraFalcon")

[March 17, 2026](https://blog.compass-security.com/2026/03/from-enumeration-to-findings-the-security-findings-report-in-entrafalcon/ "From Enumeration to Findings: The Security Findings Report in EntraFalcon")
 /
[Christian Feuchter](https://blog.compass-security.com/author/cfeuchte/ "Posts by Christian Feuchter")
 /
[0 Comments](https://blog.compass-security.com/2026/03/from-enumeration-to-findings-the-security-findings-report-in-entrafalcon/#respond)

> **TL;DR:** We just released a big update for EntraFalcon. The new Security Findings Report adds an interactive HTML overview to EntraFalcon that consolidates tenant settings and object-based checks into structured security findings. Over 60 checks, graphical charts, filtering, export, and more options are now available.
>
> Get it from: <https://github.com/CompassSecurity/EntraFalcon>

Following this post, we will publish a small blog series covering common Entra ID security findings that we frequently observe during assessments. The articles will examine specific issues in more detail and explain how they can be identified using EntraFalcon.

---

In April 2025, we released EntraFalcon, a tool intended to assist the community in reviewing Entra ID environments. Since then, we have used it in numerous security assessments. In parallel, development has continued with regular bug fixes, performance improvements, new features, and extended enumeration capabilities.

The tool is strongly object-focused (users, groups, enterprise applications, etc.) and provides predefined filters to help identify privileged objects and misconfigurations. This approach works well in smaller tenants but can become overwhelming in larger environments. In addition, beyond individual objects, weak configurations in tenant settings (for example, guest invitation settings) were previously not visible within the tool.

## The Security Findings Report

We have now released a significant addition since last year’s launch: the Security Findings Report. The goal is to consolidate the collected data into a structured overview that highlights relevant security issues in a more direct and actionable way.

A key aspect of the Security Findings Report is that it builds on EntraFalcon’s detailed object enumeration and the relationships between those objects. This allows checks that go beyond the configuration of individual objects.

The top section of the report provides a graphical overview of the findings, including severity levels and affected areas. In addition, it offers a weighted score based on the severity of the issues, helping to prioritize remediation efforts. The charts update dynamically based on the applied filters and tags, always reflecting the current state of the remediation process.

[![EntraFalcon Security Findings Report overview in a Microsoft Entra ID assessment.](https://blog.compass-security.com/wp-content/uploads/2026/03/image-11-1024x789.png)](https://blog.compass-security.com/wp-content/uploads/2026/03/image-11.png)

## **Scope of the Checks**

Currently, 63 checks are performed. These checks include weak tenant configurations such as:

* Permissive guest invitation settings
* Guest access restriction configurations
* User app consent settings
* Application creation settings

In addition to tenant-wide settings, EntraFalcon evaluates all enumerated objects to identify identities and resources with extensive permissions or risky configurations. This allows identification of issues such as:

* Foreign enterprise applications with dangerous or high API privileges
* Inactive enterprise applications
* Missing or misconfigured Conditional Access policies
* Privileged applications owned by non–tier-0 users
* Managed identities with extensive permissions in Entra ID
* Hybrid users with tier-0 Entra ID roles
* Unprotected high-tier groups
* Dynamic groups with potentially dangerous queries
* Public M365 groups

The implemented checks are not tied to a single external framework. Instead, they are based on our research, practical assessment experience, and what we consider reasonable security best practices observed across real-world environments.

[![EntraFalcon Security Findings (Enterprise Applications)](https://blog.compass-security.com/wp-content/uploads/2026/03/image-9-1024x502.png)](https://blog.compass-security.com/wp-content/uploads/2026/03/image-9.png)

Each finding contains a description of the issue, an explanation of how it could be abused by attackers, and high-level remediation guidance. For findings that affect specific objects, all related objects are listed accordingly. As examples, two findings related to enterprise applications are shown below:

[![Screenshot of EntraFalcon Security Findings Report showing Finding ENT-009 for internal enterprise applications with extensive application API privileges in Microsoft Entra ID.](https://blog.compass-security.com/wp-content/uploads/2026/03/image-12-1024x579.png)](https://blog.compass-security.com/wp-content/uploads/2026/03/image-12.png)
[![EntraFalcon report view highlighting ENT-003 for enterprise applications owned by non–Tier-0 identities in Entra ID](https://blog.compass-security.com/wp-content/uploads/2026/03/image-18-1024x445.png)](https://blog.compass-security.com/wp-content/uploads/2026/03/image-18.png)

## **Working With the Report**

The filter menu allows filtering, grouping, and searching across findings, and supports exporting the results as JSON, CSV, or PDF.

[![](https://blog.compass-security.com/wp-content/uploads/2026/03/image-15-1024x335.png)](https://blog.compass-security.com/wp-content/uploads/2026/03/image-15.png)

It is also possible to mark findings as false positives, important, fixed, or with similar tags. These attributes can be used during filtering, and come in handy in internal reviews and remediation workflows and are also included in exported results.

## **How To Get It**

The tool and further instructions are available on our GitHub page: <https://github.com/CompassSecurity/EntraFalcon>

Please note that the Security Findings Report is currently in a beta state. Checks, scoring, and detection logic may evolve over time. The report will continue to improve over the coming months, and feedback is welcome, preferably through GitHub Issues.

[Entra ID](https://blog.compass-security.com/category/entra-id/), [Tools](https://blog.compass-security.com/category/tools/)

[Azure](https://blog.compass-security.com/tag/azure/)[cloud](https://blog.compass-security.com/tag/cloud/)[Entra](https://blog.compass-security.com/tag/entra/)[EntraFalcon](https://blog.compass-security.com/tag/entrafalcon/)[EntraID](https://blog.compass-security.com/tag/entraid/)[enumeration](https://blog.compass-security.com/tag/enumeration/)[PowerShell](https://blog.compass-security.com/tag/powershell/)

[##### Previous post

WinGet Desired State: Initial Access Established](https://blog.compass-security.com/2026/03/winget-desired-state-initial-access-established/ "Previous post: WinGet Desired State: Initial Access Established")

### Leave a Reply [Cancel reply](/2026/03/from-enumeration-to-findings-the-security-...