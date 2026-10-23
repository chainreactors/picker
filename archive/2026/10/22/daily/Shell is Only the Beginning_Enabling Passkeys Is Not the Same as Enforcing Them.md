---
title: Enabling Passkeys Is Not the Same as Enforcing Them
url: https://www.darkoperator.com/blog/2026/10/22/enabling-passkeys-is-not-the-same-as-enforcing-them
source: Shell is Only the Beginning
date: 2026-10-22
fetch_date: 2026-10-23T06:45:05.033017
---

# Enabling Passkeys Is Not the Same as Enforcing Them

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

# [Enabling Passkeys Is Not the Same as Enforcing Them](/blog/2026/10/22/enabling-passkeys-is-not-the-same-as-enforcing-them)

[October 22, 2026](/blog/2026/10/22/enabling-passkeys-is-not-the-same-as-enforcing-them)
[by Carlos Perez](/?author=5005b71ac4aa8b4d97616588)

### Authentication strengths, Conditional Access design, and closing the weak-fallback and device-code gaps

*MFA to Passkeys in Microsoft Entra ID series · Part 3 of 7*

ok lets start with a scenario that plays out in real tenants. An administrator registers a shiny new FIDO2 security key. The security team marks the account as "phishing-resistant". Three months later the account is compromised through an AiTM phishing page. The attacker didn't touch the key. They sent a push notification, because **push was still an acceptable way to satisfy every Conditional Access policy that applied to that account.**

A stronger credential doesn't remove weaker paths. Entra ID has two separate policy engines, and you need both:

| Engine | Answers the question | Where |
| --- | --- | --- |
| **Authentication methods policy** | Which methods may this user *register and use at all*? | Entra ID → Authentication methods → Policies |
| **Conditional Access + authentication strengths** | Which methods are *required* to reach this resource, under these conditions? | Entra ID → Conditional Access |

Part 2 configured the first engine. This part configures the second, and then proves it works.

## Authentication strengths

An authentication strength is a named list of acceptable method combinations. A Conditional Access policy can demand a strength instead of the generic "Require multifactor authentication" grant. Entra ID has three built-in strengths, identical in every tenant and maintained by Microsoft as new methods ship:

| Built-in strength | ID | Allowed combinations (summary) |
| --- | --- | --- |
| Multifactor authentication | `00000000-0000-0000-0000-000000000002` | Everything below, **plus** password + SMS/voice/push/OATH, Temporary Access Pass, federated MFA… |
| Passwordless MFA | `00000000-0000-0000-0000-000000000003` | WHfB, FIDO2, multifactor CBA, Authenticator phone sign-in (`deviceBasedPush`) |
| **Phishing-resistant MFA** | `00000000-0000-0000-0000-000000000004` | `windowsHelloForBusiness`, `fido2`, `x509CertificateMultiFactor` |

![](https://images.squarespace-cdn.com/content/v1/52ad1d91e4b00a98a27ba20e/c716ea65-ae3c-4dcb-af46-f2883a0a12e7/authentication_concept-authentication-strengths_authentication-strength-definitions.png)

Built-in phishing-resistant MFA strength definition

**Custom strengths** (up to 15 per tenant) let you go further. The most valuable use is pinning passkeys to approved models. Under **Passkeys (FIDO2) → Advanced options** you can list the AAGUIDs a strength accepts:

![](https://images.squarespace-cdn.com/content/v1/52ad1d91e4b00a98a27ba20e/32baecb8-c667-44bc-b600-94a099664b7e/authentication_concept-authentication-strengths_guid.png)

Adding an AAGUID in authentication strength advanced options

A user who signs in with a passkey outside the list sees *"You can't get there from here"*:

![](https://images.squarespace-cdn.com/content/v1/52ad1d91e4b00a98a27ba20e/f4307338-6cd0-400b-a93c-33d160e3da21/authentication_troubleshoot-authentication-strengths_restricted-security-key.png)

Sign-in error when a passkey is not allowed by the strength

### Limitations to plan around

Each item below is from [Microsoft Learn: authentication strengths](https://learn.microsoft.com/en-us/entra/identity/authentication/concept-authentication-strengths):

* **You can't combine** *Require multifactor authentication* and *Require authentication strength* in the same policy.
* **Strengths don't restrict the first factor.** Conditional Access evaluates *after* initial authentication. A user can still type a password first, then be asked to step up with a passkey.
* **Temporary Access Pass satisfies only the built-in MFA strength**, not Passwordless or Phishing-resistant. That matters for onboarding (Part 4).
* **External authentication methods** are currently incompatible with authentication strengths.
* **Known issue with sign-in frequency:** users "can satisfy both requirements at two different times". A passkey sign-in yesterday plus a Windows Hello unlock today can together satisfy a one-hour sign-in frequency.
* **Only built-in directory roles** are honored in Conditional Access user targeting. Administrative-unit-scoped and custom roles are not. Target admin **groups** if you use custom roles.
* **Microsoft Authenticator passkey registration loop:** a policy requiring phishing-resistant MFA on **All resources** can stop users from registering an Authenticator passkey. So can policies requiring an approved client app or app protection policy, because Authenticator doesn't support app protection policies on iOS or Android. This bites hardest on BYOD phones, and the failure is easy to misdiagnose because registration touches resources beyond the *Register security information* user action. Part 4 has the diagnosis (`Get-EptRegistrationBlock`) and the targeted fix.

## A reference Conditional Access design

Name policies so they sort and read well in sign-in logs. A minimal phishing-resistant rollout needs these:

| Policy | Users | Resources | Grant / condition | Start state |
| --- | --- | --- | --- | --- |
| **CA010** Block device code flow | All users, exclude break-glass + documented exceptions | All resources | Authentication flows = device code flow → **Block** | Report-only |
| **CA011** Block authentication transfer | All users, exclude break-glass | All resources | Authentication flows = authentication transfer → **Block** | Report-only |
| **CA100** Admins require phishing-resistant MFA | 14 privileged directory roles, exclude break-glass | All resources | Authentication strength = Phishing-resistant MFA (or custom Tier 0 strength) | Report-only → On |
| **CA110** Pilot require phishing-resistant MFA | Pilot group(s), exclude break-glass | All resources | Authentication strength = Phishing-resistant MFA | Report-only → On |
| **CA120** Secure security-info registration | All users, exclude guests + break-glass | User action: *Register security information* | Trusted conditions or TAP/MFA (Part 4) | **On** (report-only isn't supported for user actions) |

Microsoft's deployment guide goes further for the enforcement phase and recommends **one policy per OS group** (Windows, macOS, iOS, Android, Other). You can then enforce platform by platform as each passes its pilot ([deployment guide](https://learn.microsoft.com/en-us/entra/identity/authentication/how-to-deploy-phishing-resistant-passwordless-authentication)).

### Build the policy in the portal

**Entra ID → Conditional Access → Policies → New policy**:

1. **Users:** include the pilot group or the directory roles. Under *Exclude*, add the emergency-access group.
2. **Target resources:** All resources.
3. **Grant:** *Grant access → Require authentication strength → Phishing-resistant MFA*.
4. **Enable policy:** **Report-only**.

![](https://images.squarespace-cdn.com/content/v1/52ad1d91e4b00a98a27ba20e/6c6bcc28-50bf-4085-b144-ad7c80abae5b/authentication_concept-authentication-strengths_conditional-acce...