---
title: Phishing-resistant MFA where it matters most, and finding the privileged identities your role report misses
url: https://www.darkoperator.com/blog/2026/11/2/cwdl3e3gk4d6uiyor7ack9sdzvqvjj
source: Shell is Only the Beginning
date: 2026-11-02
fetch_date: 2026-11-03T08:50:06.844138
---

# Phishing-resistant MFA where it matters most, and finding the privileged identities your role report misses

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

# [Phishing-resistant MFA where it matters most, and finding the privileged identities your role report misses](/blog/2026/11/2/cwdl3e3gk4d6uiyor7ack9sdzvqvjj)

[November 02, 2026](/blog/2026/11/2/cwdl3e3gk4d6uiyor7ack9sdzvqvjj)
[by Carlos Perez](/?author=5005b71ac4aa8b4d97616588)

*MFA to Passkeys in Microsoft Entra ID series · Part 6 of 7*

If you can only do one thing from this series this quarter, focus on doing it for your administrators. A phished Global Administrator account gives the attacker the whole tenant. The attacker can:

* rewrite Conditional Access,
* register their own credentials on any account,
* grant themselves application permissions that no user MFA ever touches,
* turn off your logging.

Microsoft's guidance requires **phishing-resistant** MFA for administrators. Its phishing-resistant deployment guide puts admins in their own persona, with FIDO2 security keys as the recommended portable credential. This part turns that guidance into a working program. It starts with the hardest step, which is working out who your admins are.

## Who is privileged? More people than your role report says

| Where privilege lives | Example of privilege | Covered by Entra role reports? |
| --- | --- | --- |
| Entra directory roles, **active** | Global Administrator, Privileged Role Administrator… | Yes |
| Entra directory roles, **PIM-eligible** | Can activate Global Admin in minutes | Only if you query eligibility |
| Role-assignable groups | Membership grants a role | Only if you expand groups |
| Application owners | Can add a secret to an app holding `Directory.ReadWrite.All` | No |
| Azure RBAC | Owner on the subscription running your domain controllers | No |
| Intune RBAC | Can push a script to every device | No |
| Defender RBAC | Live response: run commands on endpoints | No |
| Purview role groups | eDiscovery: export any mailbox, including Copilot interactions | No |
| Exchange / SharePoint RBAC | Mailbox full access, site collection admin | No |

Build the privileged cohort around **capabilities**, not job titles. The toolkit covers the first four rows. The others need their own product's RBAC review, and you should list those reviews in the project plan so nobody assumes the Entra report covered them.

## Admin account prerequisites

Phishing-resistant MFA on the wrong account design still leaves gaps. Microsoft's privileged access guidance boils down to:

1. **Separate admin accounts.** Make them cloud-only, with no mailbox, no Teams and no web browsing. Nobody reads phishing email with the account that owns Conditional Access.
2. **Just-in-time access with PIM.** Make role assignments eligible instead of permanent for everyone except break-glass accounts. Require approval for Tier 0 roles. Also require re-authentication on activation, using a Conditional Access authentication context that demands your Tier 0 strength.
3. **Privileged Access Workstations (PAW).** If you can't deploy PAWs, use compliant, dedicated admin devices at minimum. Require a compliant device for admin portals.
4. **Device-bound, attested passkeys.** Issue security keys from an approved AAGUID list and enforce attestation (Part 2). Give each admin **two keys**, stored separately.
5. **No phishable methods on admin accounts.** Remove SMS, voice, OATH and push from the admin persona in the authentication methods policy once keys are registered. Even unused, they are a help-desk social-engineering target (Part 4).
6. **Target custom roles through groups.** Conditional Access role targeting honors only built-in roles. If you use custom or AU-scoped roles, target a group of those admins instead.

## Emergency access (break-glass) accounts

Microsoft's [emergency access guidance](https://learn.microsoft.com/en-us/entra/identity/role-based-access-control/security-emergency-access) now covers phishing-resistant methods:

* Two or more cloud-only accounts on the `*.onmicrosoft.com` domain, with Global Administrator assigned as **permanent active** in PIM, not eligible.
* Passwordless, phishing-resistant authentication, either *"Passkey (FIDO2) (Recommended)"* or certificate-based authentication. Use methods that differ from your normal admin accounts, so a problem with one method or one key vendor can't lock out both.
* **Mandatory MFA applies to break-glass accounts too.** There is no exemption from the Azure and admin-portal MFA enforcement, which is another reason to give them passkeys.
* Use a dedicated group to exclude them from Conditional Access policies that can block sign-in. Report-only policies don't need the exclusion.
* Alert on every sign-in (threshold > 0) with Azure Monitor or Sentinel, and validate the accounts at least every 90 days.

![](https://images.squarespace-cdn.com/content/v1/52ad1d91e4b00a98a27ba20e/b469ba6a-d152-4106-9a19-f5e0bfd6e454/role-based-access-control_security-emergency-access_alert-logic.png)

Azure Monitor alert logic for emergency account sign-ins

Store the break-glass security keys in two physically separate safes, with a documented, dual-control retrieval process. Test that process, not just the keys.

## The admin policy set

Building on Part 3's reference design:

| Policy | Target | Control |
| --- | --- | --- |
| CA100 | 14 privileged roles (Microsoft template list) | Phishing-resistant MFA strength, or custom Tier 0 strength |
| CA101 | Tier 0 admins group (covers custom and AU-scoped roles) | Custom Tier 0 strength (approved AAGUIDs) |
| CA102 | Admin portals (*Microsoft Admin Portals* app) for all admins | Compliant device |
| CA103 | PIM activation (authentication context `c1`) | Tier 0 strength, sign-in frequency *every time* |

## Hidden admins: application owners and workload identities

An **application owner** can add a client secret or certificate to that app. If the app holds high-privilege application permissions (for example `Directory.ReadWrite.All`, `RoleManagement.ReadWrite.Directory`, `Mail.ReadWrite`), the owner can mint app-only tokens that:

* never involve a user sign-in,
* never meet a passkey prompt,
* never trigger user-based Conditional Access.

User MFA doesn't turn an app-only token request into an interactive sign-in. Treat these owners as privileged:

* inventory app registrations, their owners and their credentials;
* remove owners who don't need to manage credentials, and prefer certificates or federated credentials over secrets;
* review high-privilege application permissions and consent grants on the enterprise app (service principal) side;
* consider Conditional Access for workload identities (location- and risk-based) for the most powerful single-tenant apps.

## Hands-on: build the privileged cohort and test it

```
Connect-MgGraph -TenantId $tenantId -ContextScope Process -NoWelcome -Scopes `
    'RoleManagement.Read.Directory', 'GroupMember.Read.All', 'AuditLog.Read.All', 'Policy.Read.All', `
    'UserAuthenticationMethod.Read.All', 'Application.Read.All'
```

### Every privileged user, active and eligible: `Get-EptPrivilegedUser`

This reads active role assignments and PIM eligibility (`roleEligibilityScheduleInstances`), expands role-assignable groups to their transitive user members, and returns **one object per user** with their roles, assignment types, and the g...