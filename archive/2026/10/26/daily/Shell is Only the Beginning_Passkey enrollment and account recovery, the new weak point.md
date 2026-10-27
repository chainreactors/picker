---
title: Passkey enrollment and account recovery, the new weak point
url: https://www.darkoperator.com/blog/2026/10/26/passkey-enrollment-and-account-recovery-the-new-weak-point
source: Shell is Only the Beginning
date: 2026-10-26
fetch_date: 2026-10-27T07:04:23.561062
---

# Passkey enrollment and account recovery, the new weak point

# [Shell is Only the Beginning](/ "Shell is Only the Beginning")

When getting shell is only the start of the journey.

* [Blog](/)
* [Infosec Tactico Podcast](/infosec-tactico-podcast)
* [Search](/searchpage)
* Blog Series

  + [PowerShell Basics](/powershellbasics)
* MSF Installation Guides

  + [Installing Metasploit in Ubuntu and Debian](/installing-metasploit-in-ubunt)
  + [Installing Metasploit Framework in OS X](/installing-metasploit-framewor)
* [Projects](https://github.com/darkoperator)
* [About Me](/about-me)

Navigation
Blog
Infosec Tactico Podcast
Search
Blog Series
PowerShell Basics
MSF Installation Guides
Installing Metasploit in Ubuntu and Debian
Installing Metasploit Framework in OS X
Projects
About Me

# [Passkey enrollment and account recovery, the new weak point](/blog/2026/10/26/passkey-enrollment-and-account-recovery-the-new-weak-point)

[October 26, 2026](/blog/2026/10/26/passkey-enrollment-and-account-recovery-the-new-weak-point)
[by Carlos Perez](/?author=5005b71ac4aa8b4d97616588)

### Registration campaigns, Temporary Access Pass, protecting security-info registration, and a help-desk recovery process that doesn't become a bypass

*MFA to Passkeys in Microsoft Entra ID series · Part 4 of 7*

Passkeys make the sign-in ceremony very hard to phish, so attackers go after the process that issues new credentials instead.

The most damaging identity intrusions of the last few years didn't break cryptography. The attackers called the service desk, impersonated an employee, sometimes with a spoofed number or an AI-generated voice, and asked for an MFA reset or a new device registration. Once the help desk registered a method the attacker controlled, every phishing-resistant control downstream worked as designed and protected the attacker's access.

So for passkeys, **the security of the account equals the security of the weakest way to get a new credential onto it.** This part covers four such ways, and how to close each:

1. Self-service registration (Security info), protected by Conditional Access. This includes the BYOD trap where your *own* policies block registration.
2. The first credential for new hires and users with no strong method, issued as a Temporary Access Pass.
3. Registration campaigns that nudge users at sign-in.
4. Recovery when someone loses every device.

## Why enrollment is a high-risk action

Registering a passkey creates a long-lived credential. If an attacker who has a password plus a phishable second factor (or a stolen session) can add their own passkey, they have turned a temporary foothold into durable, phishing-resistant access. That access survives password resets.

Campaign season makes this worse. When the whole company is getting emails about "setting up your passkey", a phishing email about setting up your passkey looks perfectly normal.

## 1. Protect *Register security information* with Conditional Access

Conditional Access can target the user action *Register security information* (`urn:user:registersecurityinfo`). Microsoft's [recommended policy](https://learn.microsoft.com/en-us/entra/identity/conditional-access/policy-all-users-security-info-registration) requires strong conditions for any security-info change. A common design:

* **Users.** All users. Exclude guests (TAP doesn't work for guests) and break-glass accounts.
* **Target.** User actions → *Register security information*.
* **Grant.** Require MFA (or an authentication strength that includes TAP), or a compliant or hybrid-joined device, depending on your design. Many organizations also add a trusted-location condition for first-time registration.

Details that matter:

* TAP satisfies MFA requirements in Conditional Access. That's how a new hire with nothing registered gets through a policy that demands MFA to register.
* **Since 6 July 2026**, policies targeting *Register security information* also apply during Windows Hello for Business and macOS Platform SSO credential registration. If WHfB provisioning started failing on managed devices in July, check this policy first.
* **Report-only is not supported** for user-action policies. Test with a pilot group instead.
* Watch for self-inflicted loops. If the registration policy demands phishing-resistant MFA, a user without a passkey can never register one. Use an authentication strength that includes TAP, or the MFA grant.

## 1a. When your own Conditional Access blocks registration (the BYOD trap)

This failure mode catches teams who have done everything else right. You protect mobile access with *Require app protection policy* (or *Require approved client app*) targeting *All resources*, which is standard BYOD hygiene. Then users on personal phones try to register a passkey in Microsoft Authenticator, and it fails with an error that points nowhere useful.

The cause is that **Microsoft Authenticator doesn't support app protection policies** on iOS or Android. Microsoft documents the symptom on the [Authenticator passkey page](https://learn.microsoft.com/en-us/entra/identity/authentication/how-to-enable-authenticator-passkey), along with several workarounds:

1. Use [application filters](https://learn.microsoft.com/en-us/entra/identity/conditional-access/concept-filter-for-applications) to move the policy from *All resources* to specific applications.
2. Use *Require device to be marked as compliant* instead, if MDM fully manages the device. This isn't an option for true BYOD.
3. Grant a temporary, time-boxed exemption, with compensating controls such as a trusted-location or compliant-device requirement.
4. Split the policy by device platform and allow a TAP or passkey on mobile, so no loop occurs.

### Why it breaks even when your registration policy looks correct

**Registration doesn't happen entirely inside the *Register security information* user action.** The flow also authenticates against other resources, so a policy scoped to *All resources* still applies, even though the user satisfied the policy you wrote for security-info registration.

Read your own sign-in logs and you'll see it. Filter to the affected user around the failed attempt, and look at the Resource field on each entry rather than only the application. The registration flow involves resources such as:

| Resource | App ID |
| --- | --- |
| Azure Credential Configuration Endpoint Service | `ea890292-c8c8-4433-b5ea-b09d0668e1a6` |
| Windows Azure Active Directory | `00000002-0000-0000-c000-000000000000` |
| Microsoft Graph | `00000003-0000-0000-c000-000000000000` |

The Azure Credential Configuration Endpoint Service handles registration of security information gathered by apps such as Microsoft Authenticator and the My Sign-ins portal. When the app-protection policy blocks *that* call, registration fails.

`Get-EptRegistrationBlock` does this triage for you. It reads the beta sign-in logs, keeps only sign-ins against credential-registration resources, and names the Conditional Access policy that produced the failure:

```
function Get-EptRegistrationBlock {
    <#
    .SYNOPSIS
        Finds sign-ins where Conditional Access blocked or challenged a credential-registration resource.
    .DESCRIPTION
        Passkey registration does not happen entirely inside the "Register security information" user
        action. The flow also calls resources such as the Azure Credential Configuration Endpoint
        Service. A policy targeting All resources (for example "Require app protection policy" or
        "Require approved client app" on mobile) therefore blocks registration, usually with a
        confusing error in Microsoft Authenticator.

        This function reads the beta sign-in logs, keeps sign-ins against known registration resources
        (or any resource matched by -ResourceName), and reports which Conditional Access policies
        produced a failure or challenge, so you can see exactly which policy to adjust.

        Read-only. Requires AuditLog.Read.All plus Policy.Read.All to see appliedConditi...