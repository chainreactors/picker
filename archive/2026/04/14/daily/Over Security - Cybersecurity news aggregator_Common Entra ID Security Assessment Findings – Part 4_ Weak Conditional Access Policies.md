---
title: Common Entra ID Security Assessment Findings – Part 4: Weak Conditional Access Policies
url: https://blog.compass-security.com/2026/04/common-entra-id-security-assessment-findings-part-4-weak-conditional-access-policies/
source: Over Security - Cybersecurity news aggregator
date: 2026-04-14
fetch_date: 2026-04-15T04:43:58.343823
---

# Common Entra ID Security Assessment Findings – Part 4: Weak Conditional Access Policies

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

# [Common Entra ID Security Assessment Findings – Part 4: Weak Conditional Access Policies](https://blog.compass-security.com/2026/04/common-entra-id-security-assessment-findings-part-4-weak-conditional-access-policies/ "Common Entra ID Security Assessment Findings – Part 4: Weak Conditional Access Policies")

[April 14, 2026](https://blog.compass-security.com/2026/04/common-entra-id-security-assessment-findings-part-4-weak-conditional-access-policies/ "Common Entra ID Security Assessment Findings – Part 4: Weak Conditional Access Policies")
 /
[Christian Feuchter](https://blog.compass-security.com/author/cfeuchte/ "Posts by Christian Feuchter")
 /
[0 Comments](https://blog.compass-security.com/2026/04/common-entra-id-security-assessment-findings-part-4-weak-conditional-access-policies/#respond)

**This post is part of a small blog series covering common Entra ID security findings observed during real-world assessments. Each article explores selected findings in more detail to provide a clearer understanding of the underlying risks and practical implications.**

* Part 1: [Privileged Foreign Enterprise Applications](https://blog.compass-security.com/2026/03/common-entra-id-security-assessment-findings-part-1-foreign-enterprise-applications-with-privileged-api-permissions/)
* Part 2: [Privileged Unprotected Groups](https://blog.compass-security.com/2026/03/common-entra-id-security-assessment-findings-part-2-privileged-unprotected-groups/)
* Part 3: [Weak Privileged Identity Management Configuration](https://blog.compass-security.com/2026/04/common-entra-id-security-assessment-findings-part-3-weak-privileged-identity-management-configuration/)

## Conditional Access Policies

Conditional Access policies are among the most important security controls in Entra ID. As the name suggests, they define under which conditions access is allowed within a tenant. They are used to enforce protections such as MFA, restrict access based on device state or location, and apply stronger controls to sensitive applications or privileged accounts.

At the same time, Conditional Access is a broad and complex topic. The security benefits depend not only on whether policies exist, but also on how well they are designed, scoped, and maintained over time.

A full discussion would easily justify a separate blog post series. Therefore, this post takes a higher-level view and focuses on general weaknesses and commonly occurring issues.

## Common Issues in Conditional Access Policy Design and Configuration

Reviewing existing Conditional Access policies is one of the most important tasks in an Entra ID security assessment. This section highlights common issues that we regularly observe in practice, including coverage gaps and design weaknesses that reduce the intended security benefits.

### Issues in Identity Targeting

Each Conditional Access policy must define which identities it applies to. Weaknesses in this area that can leave relevant users insufficiently protected.

#### Targeting Users via Groups

A common approach is to scope important Conditional Access policies, for example policies enforcing MFA, to specific groups. In principle, this can work well. In practice, however, we often find that not all relevant users are actually members of the targeted groups. As a result, some users remain outside the scope of the policy and are therefore not protected as intended.

#### Issues in Role-Based Targeting

Conditional Access policies often target administrative accounts based on Entra ID roles. This is generally a sensible approach, but in practice we regularly see tenants where privileged roles are in use that are not included in the relevant Conditional Access policies. This can leave administrative accounts less protected than originally intended.

In addition, there is an important Microsoft limitation to be aware of: scoped role assignments are not considered in Conditional Access role targeting[1](#846ee48e-8046-4f3b-96d5-53dae008d324). For example, if a user has the *User Administrator* role scoped only to an Administrative Unit, that user is not included when a policy targets the role.

### Targeting Specific Resources in Basic Protection Policies

Another issue we sometimes observe is that important protection mechanisms are scoped only to specific resources. One example is requiring phishing-resistant MFA only for Microsoft Admin Portals.

The problem is that these resources often do not provide the coverage administrators expect. For example, Microsoft Admin Portals only covers the web-based admin portals, while sensitive actions may also be performed directly on the Microsoft Graph API[2](#b04b10b6-c78c-4c5b-85cc-b02922d90060).

### Too Many Conditions

Conditional Access is sometimes referred to as an identity firewall. However, that comparison can be misleading. Unlike many traditional firewall designs, Conditional Access does not provide a simple default-deny model for all authentication activity. Access is generally allowed unless a policy applies to the sign-in and enforces a control or block.

This makes policy scope highly important. Every additional condition (e.g. network locations, device platform, client apps) in a Conditional Access policy reduces the number of authentication events to which it applies. While conditions are often needed, too many of them can unintentionally create gaps in protection. In practice, we regularly see policies that are narrower than the administrators expect, leaving many authentication events outside the intended protection.

A commonly observed example is a Conditional Access policy that includes both *Sign-in risk* and *User risk* as conditions. Because these conditions are combined using a logical AND, both must apply at the same time for the policy to take effect. However, the two conditions often do not overlap for the same sign-in: *Sign-in risk* is evaluated as part of the authentication process, while *User risk* is usually calculated separately in the background and may only be raised later through offline detection[3](#3e6dc8b6-f599-4fa2-92bc-806f2a029820). Consequently, such a policy may be triggered only rarely in practice and may therefore provide less protection than expected.

### Built-In Bypasses

Even if Conditional Access policies target *all users* and *all resources*, this does not necessarily mean that every relevant action is covered.

Some actions, such as registering security information or joining a device, must be addressed in a dedicated policy to be covered. In addition, Microsoft has implemented several built-in bypasses and exceptions. These are likely required to avoid breaking important platform functionality. The difficulty is that they are not always clearly documented, which can lead to incorrect assumptions about the actual protection in place. A well-known example is a built-in bypass for policies that require only a compliant device[4](#09b7674a-cb50-45b5-996c-af7672d7e43b), which still allows limited actions such as reading device information.

As a result, even broadly scoped Conditional Access policies should not automatically be assumed to cover every relevant action.

### Missing Policies

Based on our observations, most tenants now enforce MFA through Conditional Access policies. However, during assessments we still regularly find that other important Conditional Access policies are missing.
...