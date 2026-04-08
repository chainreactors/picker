---
title: Common Entra ID Security Assessment Findings – Part 3: Weak Privileged Identity Management Configuration
url: https://blog.compass-security.com/2026/04/common-entra-id-security-assessment-findings-part-3-weak-privileged-identity-management-configuration/
source: Over Security - Cybersecurity news aggregator
date: 2026-04-07
fetch_date: 2026-04-08T04:38:55.889646
---

# Common Entra ID Security Assessment Findings – Part 3: Weak Privileged Identity Management Configuration

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

# [Common Entra ID Security Assessment Findings – Part 3: Weak Privileged Identity Management Configuration](https://blog.compass-security.com/2026/04/common-entra-id-security-assessment-findings-part-3-weak-privileged-identity-management-configuration/ "Common Entra ID Security Assessment Findings – Part 3: Weak Privileged Identity Management Configuration")

[April 7, 2026](https://blog.compass-security.com/2026/04/common-entra-id-security-assessment-findings-part-3-weak-privileged-identity-management-configuration/ "Common Entra ID Security Assessment Findings – Part 3: Weak Privileged Identity Management Configuration")
 /
[Christian Feuchter](https://blog.compass-security.com/author/cfeuchte/ "Posts by Christian Feuchter")
 /
[0 Comments](https://blog.compass-security.com/2026/04/common-entra-id-security-assessment-findings-part-3-weak-privileged-identity-management-configuration/#respond)

**This post is part of a small blog series covering common Entra ID security findings observed during real-world assessments. Each article explores selected findings in more detail to provide a clearer understanding of the underlying risks and practical implications.**

* Part 1: [Privileged Foreign Enterprise Applications](https://blog.compass-security.com/2026/03/common-entra-id-security-assessment-findings-part-1-foreign-enterprise-applications-with-privileged-api-permissions/)
* Part 2: [Privileged Unprotected Groups](https://blog.compass-security.com/2026/03/common-entra-id-security-assessment-findings-part-2-privileged-unprotected-groups/)

## What Is Privileged Identity Management?

Privileged Identity Management (PIM) is a service in Microsoft Entra ID that enables organizations to manage, control, and monitor privileged access.

The main features are:

* Provide just-in-time privileged access
* Assign time-bound access and end dates
* Require approval or multifactor authentication to activate privileged roles
* Require written justification for role activation
* Generate notifications when privileged roles are activated

A common use case is to avoid permanently assigning the Global Administrator role. Instead, users or group members are made eligible to activate the role only when needed and only for a limited period.

[![Illustration of PIM for Entra ID roles, including different assignment types and role settings](https://blog.compass-security.com/wp-content/uploads/2026/03/image-39-1024x466.png)](https://blog.compass-security.com/wp-content/uploads/2026/03/image-39.png)

The activation of a role can be protected by additional requirements such as MFA, approval, or justification. For stronger protection, activation can also require an Authentication Context[1](#1f4fe2f3-a0ab-4a2d-9e46-7fa8b99061d9), which allows Conditional Access policies to enforce specific controls again at activation time.

PIM is available for:

* Entra ID role assignments
* Group assignments (member or owner)
* Azure role assignments

This blog post focuses on PIM for Entra ID roles, but the same principles also apply to PIM for Groups and PIM for Azure roles.

## Common Weaknesses in PIM Configuration

During security assessments, we frequently observe the same weak PIM configurations. In some cases, the use of PIM is sometimes even used to justify the absence of other important hardening measures, based on the assumption that administrators are already “protected by PIM.” In this chapter, we look at several weak configurations that can occur in practice and explain why PIM may provide less protection than expected when it is configured too permissively.

### PIM Not Used

In some environments, PIM is not used at all, even though the required Entra ID P2 licenses are available. As a result, highly privileged roles such as Global Administrator remain assigned permanently. If such an account is compromised, for example through a phishing attack, an attacker can immediately obtain privileged access to the tenant.

### High-Privilege Roles Missing from PIM Protection

Another common issue is that PIM is used for well-known sensitive roles such as Global Administrator, while other highly privileged roles remain permanently assigned.

### MFA Requirement Relies Only on Built-In Azure MFA

In many environments, even highly privileged roles such as Global Administrator are protected only by the built-in Azure MFA requirement:

[![Screenshot of a PIM configuration where the Global Administrator role requires only Azure MFA for activation](https://blog.compass-security.com/wp-content/uploads/2026/03/image-23.png)](https://blog.compass-security.com/wp-content/uploads/2026/03/image-23.png)

If an attacker can steal tokens that were issued after MFA authentication and therefore already contain the MFA claim, they may be able to activate the role themselves without an additional MFA step-up.

Another important aspect is that PIM only adds protection at the moment of role activation. If an attacker has stolen a user’s refresh token, they can wait for the legitimate user to activate the privileged role and then use the stolen refresh token to obtain a new access token with the elevated privileges.

### Permanent Active Assignments Are Allowed

If permanent active assignments are allowed, privileged roles can be assigned without an expiration date, increasing the risk of long-term privileged access.

### Missing Notifications

Highly privileged roles are usually not needed for day-to-day operations. Notifications for role assignments and activations can help detect unusual or unexpected use, for example outside normal working hours.

### Excessive Activation Duration

Highly privileged roles are usually only needed for short administrative tasks, such as assigning other privileged roles. They should therefore only be activated for a limited time. In many environments, however, the maximum activation duration is set to more than four hours. Although users can select a shorter duration, these settings are often left unchanged in practice, which increases the exposure window.

## Attack Examples

The following examples show the consequences of relying solely on the built-in Azure MFA requirement. In these scenarios, we assume that an attacker has obtained authentication tokens for the Azure portal, for example through phishing.

### Example 1: Satisfying the Built-In Azure MFA Requirement

In this example, we assume that no further restrictions for administrators are enforced through Conditional Access policies and that only MFA is required. The admin user Alice has an eligible assignment for the Entra ID role Conditional Access Administrator. In the PIM role settings, only Azure MFA is required and no approval is necessary for activation.

[![Diagram of a scenario where only Azure MFA is required to activate the eligible Conditional Access Administrator role](https://blog.compass-security.com/wp-content/uploads/2026/03/image-30-1024x402.png)](https://blog.compass-security.com/wp-content/uploads/2026/03/image-30.png)

The stolen access token contains the value `mfa` in the `amr` claim. This indicates that the user Alice authenticated using MFA:

```
PS> invoke-parseJwt $tokens.access_token

aud                 : https://graph.microsoft.com
amr                 : {pwd, mfa}
app_displayname     : Azure Portal
appid               : c44b4083-3bb0-49c1-b47d-974e53cbdf3c
idtyp               : user
name              ...