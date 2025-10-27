---
title: Validate your Windows Audit Policy Configuration with KQL
url: https://blog.nviso.eu/2024/09/05/validate-your-windows-audit-policy-configuration-with-kql/
source: NVISO Labs
date: 2024-09-06
fetch_date: 2025-10-06T18:25:57.029130
---

# Validate your Windows Audit Policy Configuration with KQL

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

# Validate your Windows Audit Policy Configuration with KQL

[Stamatis Chatzimangou](https://blog.nviso.eu/author/stamatis-chatzimangou/ "Posts by Stamatis Chatzimangou")

[SOC](https://blog.nviso.eu/category/soc/), [Azure](https://blog.nviso.eu/category/cloud-security/azure/), [Blue Team](https://blog.nviso.eu/category/blue-team/), [Cloud Security](https://blog.nviso.eu/category/cloud-security/), [Sentinel](https://blog.nviso.eu/category/cloud-security/sentinel/), [Logging](https://blog.nviso.eu/category/logging/), [Audit Policy](https://blog.nviso.eu/category/audit-policy/), [Windows](https://blog.nviso.eu/category/windows/), [Kusto Query Language](https://blog.nviso.eu/category/kusto-kql/), [SIEM](https://blog.nviso.eu/category/siem/)

September 5, 2024September 3, 2024
16 Minutes

Defining an audit policy in Windows is crucial for making sure that the appropriate security events are logged and monitored. A well defined audit policy facilitates the detection of security incidents, improves incident response capabilities and ensures compliance with regulatory requirements. There is an abundance of best practices guides and documentation out there for the configuration of the Windows audit policy.

However, simply configuring the audit policy is not enough. You should also verify that the configuration is being applied correctly and consistently in your environment so that the correct events will be available when required. An improper implementation of the audit policy configuration can lead to visibility gaps and can potentially result in missing critical security incidents. Conversely, auditing more events than required can lead to unnecessary noise during investigations and unwanted side effects for your tools, like overloading the SIEM, increasing the cost of storage and requiring more computational power for correlation.

Verifying that the audit policy is applied consistently throughout the environment can be a challenge, especially if you are approaching the problem from the perspective of an MSSP or even if you work in an internal SOC with limited access to the environment you are monitoring. Tools like auditpol are available, but running them at a large scale and presenting the output may be a challenge some times. Even so, auditpol would display the configuration of the system and not what is actually being received by the SIEM. In this blog post we will look into the idea of leveraging the capabilities of Kusto Query Language (KQL) using Microsoft Sentinel to provide a quick and practical way of identifying discrepancies in the audit policy.

## Validation Criteria

In order to assess whether a windows audit policy is applied correctly in a monitored environment we focus on the following vectors:

* **Status** (enabled/disabled) of each audit policy subcategory compared to what is expected.
* **Volume** per enabled audit policy subcategory, measured in number of events and billed size.
* **Coverage** of each audit policy subcategory, measured in number of computers where that audit policy category is identified or missing.

These 3 vectors should provide us with enough insight to begin troubleshooting discrepancies in the application of the defined audit policy.

## Kusto Query

We will use the following query to examine all of these vectors. For testing purposes the query is parameterized based on the audit policy recommendations for windows servers by Microsoft [1][2].

We will however explain how to customize the query to match your organization’s defined audit policy in the section “Query Customization” at the very end of this blog post, but first we will break down the output of the query and provide some information on how to interpret it.

```
// LookbackTime of the queries.
let LookbackTime = 30d;
// As of July 2024 the SecurityEvent table contains Audit Success and Audit Failure (https://rodtrent.substack.com/p/microsoft-sentinel-updated-securityevent).
let KeywordsPopulated = true;
// The defined/applied/expected audit policy of the environment. This variable should be customized to match the configuration of the environment the query is run against.
let AppliedAuditPolicy = datatable(
    Task: int,
    Category: string,
    Subcategory: string,
    AuditSuccess: bool,
    AuditFailure: bool,
    Comment: string
) [
    14336, "Account Logon", "Credential Validation", true, true, "",
    14339, "Account Logon", "Kerberos Authentication Service", true, true, "This subcategory makes sense only on domain controllers.",
    14337, "Account Logon", "Kerberos Service Ticket Operations", true, true, "This subcategory makes sense only on domain controllers.",
    14338, "Account Logon", "Other Account Logon Events", false, false, "Should not contain any events. Reserved for future usage.",
    13828, "Account Management", "Application Group Management", false, false, "Application Group Management subcategory events may not exist because Authorization Manager is very rarely in use and it is deprecated starting from Windows Server 2012.",
    13825, "Account Management", "Computer Account Management", true, false, "This subcategory generates events only on domain controllers. This subcategory doesn’t have Failure events.",
    13827, "Account Management", "Distribution Group Management", false, false, "This subcategory generates events only on domain controllers. This subcategory doesn’t have Failure events.",
    13829, "Account Management", "Other Account Management Events", true, false, "This subcategory doesn’t have Failure events.",
    13826, "Account Management", "Security Group Management", true, false, "This subcategory doesn’t have Failure events.",
    13824, "Account Management", "User Account Management", true, true, "",
    13314, "Detailed Tracking", "DPAPI Activity", false, false, "It’s mainly used for DPAPI troubleshooting.",
    13316, "Detailed Tracking", "PnP Activity", false, false, "This subcategory doesn’t have Failure events.",
    13312, "Detailed Tracking", "Process Creation", true, false, "This subcategory doesn’t have Failure events.",
    13313, "Detailed Tracking", "Process Termination", false, false, "This subcategory doesn’t have Failure events.",
    13315, "Detailed Tracking", "RPC Events", false, false, "Events in this subcategory occur rarely.",
    13317, "Detailed Tracking", "Token Right Adjusted", false, false, "This subcatego...