---
title: Introducing EntraFalcon – A Tool to Enumerate Entra ID Objects and Assignments
url: https://blog.compass-security.com/2025/04/introducing-entrafalcon-a-tool-to-enumerate-entra-id-objects-and-assignments/
source: Over Security - Cybersecurity news aggregator
date: 2025-04-30
fetch_date: 2025-10-06T22:06:52.010236
---

# Introducing EntraFalcon – A Tool to Enumerate Entra ID Objects and Assignments

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

# [Introducing EntraFalcon – A Tool to Enumerate Entra ID Objects and Assignments](https://blog.compass-security.com/2025/04/introducing-entrafalcon-a-tool-to-enumerate-entra-id-objects-and-assignments/ "Introducing EntraFalcon – A Tool to Enumerate Entra ID Objects and Assignments")

[April 29, 2025](https://blog.compass-security.com/2025/04/introducing-entrafalcon-a-tool-to-enumerate-entra-id-objects-and-assignments/ "Introducing EntraFalcon – A Tool to Enumerate Entra ID Objects and Assignments")
 /
[Christian Feuchter](https://blog.compass-security.com/author/cfeuchte/ "Posts by Christian Feuchter")
 /
[1 Comment](https://blog.compass-security.com/2025/04/introducing-entrafalcon-a-tool-to-enumerate-entra-id-objects-and-assignments/#comments)

> **TL;DR**: PowerShell tool to enumerate Entra ID objects, assignments and identify highly privileged objects or risky configurations.
>
> <https://github.com/CompassSecurity/EntraFalcon>

Entra ID environments can contain thousands of objects – users, groups, service principals, and more – each with unique properties and complex relationships. While manual reviews through the Entra portal might be feasible in smaller environments, they become a tedious task in larger, complex environments.

There are already several free tools available for enumerating Entra ID data. However, some of them typically focus only on dumping data, without offering much support for identifying highly privileged objects or potentially risky object configurations. Other tools do not enumerate certain objects, properties or assignments like Administrative Units, Application app lock configurations, M365 groups or Privileged Identity Management (PIM) eligible assignments.

This is why we built EntraFalcon, a PowerShell tool designed to help security analysts, penetration testers, and sysadmins review Entra ID environments. It highlights potentially risky object configurations and privileged assignments that are often overlooked.

**Key Features**

* Enumerates Entra ID objects, including:
  + Users, Groups (incl. PIM-eligible assignments), App Registrations, Enterprise Apps, Managed Identities, Administrative Units
  + Role assignments: Entra roles, Azure roles (active and PIM-eligible)
  + Conditional Access Policies
* Applies a simple scoring model to each object, assigning impact, likelihood, and risk scores to help prioritize findings. Interesting configurations or highly elevated privileges are highlighted with warnings
* Generates interactive HTML reports that are sortable, filterable and exportable
* Simple and flexible to use:
  + No dependencies: pure PowerShell compatible with both PowerShell 5.1 and 7 (Windows and Linux)
  + Built-in authentication supporting different authentication flows
  + Bypasses Microsoft Graph API consent – using Microsoft first-party apps with pre-consented API permissions for authentication

**Example Findings**

Some examples EntraFalcon helps to identify:

* Users with control over highly privileged groups or applications
* Foreign or internal enterprise applications with excessive permissions (e.g., Microsoft Graph API, Entra/Azure role assignments)
* Users assigned Azure IAM roles directly on resources
* Highly privileged accounts that are synchronized from on-premises directories
* Inactive accounts or users without MFA capability
* Unprotected groups used in sensitive assignments (e.g., Conditional Access exclusions, subscription ownership, or eligible member of a privileged group)
* Missing or misconfigured Conditional Access Policies – such as combining user risk and sign-in risk in a single policy.

**Report Samples**

[![](https://blog.compass-security.com/wp-content/uploads/2025/04/image-8-1024x490.png)](https://blog.compass-security.com/wp-content/uploads/2025/04/image-8.png)

Main overview with sortable, filterable, and customizable columns.

[![](https://blog.compass-security.com/wp-content/uploads/2025/04/image-4.png)](https://blog.compass-security.com/wp-content/uploads/2025/04/image-4.png)

Reports include preset filters and column layouts to find interesting objects.

[![](https://blog.compass-security.com/wp-content/uploads/2025/04/image-11.png)](https://blog.compass-security.com/wp-content/uploads/2025/04/image-11.png)

Display detailed information for each object, e.g., for Enterprise Applications.

[![](https://blog.compass-security.com/wp-content/uploads/2025/04/image-1-1024x340.png)](https://blog.compass-security.com/wp-content/uploads/2025/04/image-1.png)

Conditional Access report highlighting potential misconfigurations and missing policies.

[![](https://blog.compass-security.com/wp-content/uploads/2025/04/image-3.png)](https://blog.compass-security.com/wp-content/uploads/2025/04/image-3.png)

Detailed view of Conditional Access policies with links to referenced objects.

[![](https://blog.compass-security.com/wp-content/uploads/2025/04/image-772x1024.png)](https://blog.compass-security.com/wp-content/uploads/2025/04/image.png)

Summary of discovered objects and role assignments.

**Required Permissions**

To collect data from Entra ID, the user executing the tool requires at least *Global Reader* permissions.

To include Azure IAM data (optional but recommended), the *Reader* role is needed for each relevant Management Group or Subscription.

**Limitations**

While EntraFalcon helps surface potential issues, manual analysis is still essential to fully understand the impact of each finding. Furthermore, the risk scores provided are intended as indicators, not definitive assessments – they should be reviewed in context as part of a broader investigation.

**Get Started**

To get started with EntraFalcon, visit our [GitHub repository](https://github.com/CompassSecurity/EntraFalcon) for usage instructions, examples, and additional details.

[Entra ID](https://blog.compass-security.com/category/entra-id/), [Penetration Test](https://blog.compass-security.com/category/penetration-test/), [Tools](https://blog.compass-security.com/category/tools/)

[Azure](https://blog.compass-security.com/tag/azure/)[cloud](https://blog.compass-security.com/tag/cloud/)[Entra](https://blog.compass-security.com/tag/entra/)[EntraID](https://blog.compass-security.com/tag/entraid/)[enumeration](https://blog.compass-security.com/tag/enumeration/)[PowerShell](https://blog.compass-security.com/tag/powershell/)

[##### Previous post

300 Milliseconds to Admin: Mastering DLL Hijacking and Hooking to Win the Race (CVE-2025-24076 and CVE-2025-24994)](https://blog.compass-security.com/2025/04/3-milliseconds-to-admin-mastering-dll-hijacking-and-hooking-to-win-the-race-cve-2025-24076-and-cve-2025-24994/ "Previous post: 300 Milliseconds to Admin: Mastering DLL Hijacking and Hooking to Win the Race (CVE-2025-24076 and CVE-2025-24994)")
[##### Next post

Bypassing BitLocker Encryption: Bitpixie PoC and WinPE Edition](https://blog.compass-security.com/2025/05/bypassing-bitlocker-encryption-bitpixie-poc-and-winpe-edition/ "Next post: Bypassing BitLocker Encryption: Bitpixie PoC and WinPE Edition")

## 1 Comment

1. Ian

   May 23, 2025 at 12:24

   This is a fantastic tool. All credit to you.

   [Reply](https://blog.compass-security.com/2025/04/introducing-entrafalcon-a-tool-to-enumerate-entra-id-objects-and-assignments/?replytocom=387234#respond)

### Leave a Reply [Cancel reply](/2025/04/introducing-entrafalcon-a-tool-to-e...