---
title: Common Entra ID Security Assessment Findings – Part 2: Privileged Unprotected Groups
url: https://blog.compass-security.com/2026/03/common-entra-id-security-assessment-findings-part-2-privileged-unprotected-groups/
source: Over Security - Cybersecurity news aggregator
date: 2026-03-31
fetch_date: 2026-04-01T04:47:36.680047
---

# Common Entra ID Security Assessment Findings – Part 2: Privileged Unprotected Groups

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

# [Common Entra ID Security Assessment Findings – Part 2: Privileged Unprotected Groups](https://blog.compass-security.com/2026/03/common-entra-id-security-assessment-findings-part-2-privileged-unprotected-groups/ "Common Entra ID Security Assessment Findings – Part 2: Privileged Unprotected Groups")

[March 31, 2026](https://blog.compass-security.com/2026/03/common-entra-id-security-assessment-findings-part-2-privileged-unprotected-groups/ "Common Entra ID Security Assessment Findings – Part 2: Privileged Unprotected Groups")
 /
[Christian Feuchter](https://blog.compass-security.com/author/cfeuchte/ "Posts by Christian Feuchter")
 /
[0 Comments](https://blog.compass-security.com/2026/03/common-entra-id-security-assessment-findings-part-2-privileged-unprotected-groups/#respond)

**This post is part of a small blog series covering common Entra ID security findings observed during real-world assessments. Each article explores selected findings in more detail to provide a clearer understanding of the underlying risks and practical implications.**

* Part 1: [Privileged Foreign Enterprise Applications](https://blog.compass-security.com/2026/03/common-entra-id-security-assessment-findings-part-1-foreign-enterprise-applications-with-privileged-api-permissions/)

## Introduction: What Are Unprotected Groups?

Groups in Entra ID have various properties, such as:

* **Group type:** Security, Microsoft 365 (Unified), or Dynamic
* **Security enabled:** Yes / No
* **Visibility:** Public / Private
* **Synced from on-premises:** Yes / No
* **Role-assignable:** Yes / No

These properties influence various aspects, such as whether Microsoft 365 resources are linked to the group, how membership is assigned, and how the group can be used for permission assignments. This blog post primarily focuses on security groups.

### Who Can Edit Security Groups?

Some of these properties also determine who can edit the membership of a group. By default, numerous administrative roles can edit the membership of security groups, such as:

* *User Administrator*
* *Groups Administrator*
* *Knowledge Administrator*
* *Knowledge Manager*
* *Windows 365 Administrator*
* *Intune Administrator*
* *Directory Writers*

In practice, these roles are sometimes assigned to lower-tier IT functions such as the Service Desk or 1st Level Support.

If a group does not have any of the following protective properties, it can be edited by members of the roles listed above:

* **Groups synced from on-premises:** These groups can only be modified in the on-premises environment.
* **Groups that are members of a Restricted Management Administrative Unit (RMAU)[1](#def21351-0afe-410e-a5ac-c6236116018d):** These groups can only be edited by identities that have an appropriate administrative role scoped to the corresponding Administrative Unit.
* **Role-assignable groups[2](#53362be7-bbdd-4d82-b13a-cfb24836251d):** These groups and their members are additionally protected by default to prevent privilege escalation:
  + Only high-tier administrative roles can manage the group. For example, a *Groups Administrator* cannot add owners or members to a role-assignable group. Applications with permissions such as `Group.ReadWrite.All` cannot modify role-assignable groups.
  + Owners and members of the group are also protected from modification by lower-tier administrators. For example, a *User Administrator* cannot reset the password of an owner of a role-assignable group.
  + Role-assignable groups can only contain nested groups that are also role-assignable.

Groups that do not meet the above conditions are referred to as *unprotected groups* in this post, since they can be edited by lower-tier administrators or applications. Note that the term *unprotected* is not an official Microsoft classification but is used by Compass Security in security assessments to describe groups without additional protective properties.

### What Is the Issue?

The issue arises when such unprotected groups are used to grant sensitive privileges or enforce critical security controls. This can allow internal or external lower-tier administrators, or even foreign enterprise applications, to perform sensitive actions or gain access to critical resources.

## Abuse Scenario

This section illustrates common issues related to unprotected groups that are frequently identified during security assessments.

### Issue 1: Conditional Access Policies Use Unprotected Groups

Conditional Access policies (CAPs) enforce critical security controls such as MFA and other restrictions based on device state, location, risk level, or authentication flow.

If users are included or excluded through unprotected groups, identities with lower-tier administrative roles can modify group membership. For example, a *Global Administrator* could be removed from a group used to enforce MFA via a Conditional Access policy, effectively disabling the intended control for that account.

[![Schema illustrating privilege escalation in Entra ID by excluding a Global Administrator from a Conditional Access policy via an unprotected group.](https://blog.compass-security.com/wp-content/uploads/2026/02/image-17-1024x433.png)](https://blog.compass-security.com/wp-content/uploads/2026/02/image-17.png)

Note: Conditional Access policies also allow the use of non–security-enabled Microsoft 365 groups, including groups with public visibility. In such cases, any internal user may be able to add themselves or other users to a group used for inclusion or exclusion in a policy, for example an MFA exclusion group. However, the use of such groups has not been observed during recent security assessments.

### Issue 2: Privileged Identity Management for Groups Using Unprotected Groups

The use of Privileged Identity Management (PIM) for Groups is not commonly observed. However, when implemented, it introduces structural risks, since it allows non–role-assignable groups to be configured as eligible members of a role-assignable group.

This introduces risk when unprotected groups are used as eligible members or owners. In the following example, a lower-tier administrator (with the role *Knowledge Manager*) is able to add themselves to a group (`PFG_EligibleMembers`) that is configured as an eligible member of a highly privileged role-assignable group (`PFG_GlobalAdmin`).

If no approval workflow is required, the administrator can activate their membership in the privileged group, which has the *Global Administrator* role assigned. This effectively grants administrative control over the tenant.

[![Schema showing privilege escalation through PIM for Groups, where an unprotected group is nested as eligible in a role-assignable group with Global Administrator rights.](https://blog.compass-security.com/wp-content/uploads/2026/02/image-25-1024x245.png)](https://blog.compass-security.com/wp-content/uploads/2026/02/image-25.png)

**Note:** Because service principals cannot activate PIM group memberships, an attacker controlling a service principal would first need to compromise another identity, such as a guest user. That identity could then be added to a group that is configured as eligible.

The following steps illustrate how an attacker can obtain *Global Administrator* privileges for a compromised internal user (`Internal Support`) who has the *Knowledge Manager* role assigned.

#### Step 1: Adding the Attacker ...