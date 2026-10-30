---
title: Session security, token protection, continuous access evaluation, and measuring what users ACTUALLY sign in with
url: https://www.darkoperator.com/blog/2026/10/29/w5qsv4977w92qgoxoethi861dzud1l
source: Shell is Only the Beginning
date: 2026-10-29
fetch_date: 2026-10-30T07:54:27.937424
---

# Session security, token protection, continuous access evaluation, and measuring what users ACTUALLY sign in with

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

# [Session security, token protection, continuous access evaluation, and measuring what users ACTUALLY sign in with](/blog/2026/10/29/w5qsv4977w92qgoxoethi861dzud1l)

[October 29, 2026](/blog/2026/10/29/w5qsv4977w92qgoxoethi861dzud1l)
[by Carlos Perez](/?author=5005b71ac4aa8b4d97616588)

*MFA to Passkeys in Microsoft Entra ID series · Part 5 of 7*

A passkey proves who the user is at the moment of sign-in. Then Entra ID hands out tokens so the user doesn't have to prove it again for every email, file and Teams message. Those tokens are what attackers want in the end, and some of the ways to steal them never touch the sign-in page.

This doesn't weaken the case for passkeys. It defines where passkeys stop and other controls take over.

## Authentication and sessions are different problems

| Artifact | What it is | Lifetime (typical) | Stolen by |
| --- | --- | --- | --- |
| Session cookie (ESTSAUTH…) | Browser session with Entra ID | Hours to days; rolling | AiTM proxy, infostealer |
| Refresh token | Lets an app get new access tokens silently | Up to 90 days, rolling | Infostealer, malicious app, device code phishing |
| Primary Refresh Token (PRT) | Device-level SSO token on joined/registered Windows, macOS, iOS | Up to 14 days, renewed | Malware with local admin / TPM bypass attempts |
| Access token | Presented to Exchange, SharePoint, Graph… | ~60–90 minutes (longer with CAE) | Any of the above, or a compromised app |

Match each attack to what stops it:

| Attack | Passkey stops it? | Controls that help |
| --- | --- | --- |
| AiTM proxy relays sign-in, steals the cookie | Yes. The proxy can't complete a passkey ceremony | Phishing-resistant strength (Part 3) |
| Device code phishing | No. The user signs in on the real site | Block device code flow (Part 3) |
| Infostealer copies browser cookies / refresh tokens | No. The sign-in was legitimate | Compliant device, token protection, EDR, CAE, detection |
| Malicious OAuth app consent | No | Admin consent workflow, app governance |
| Help desk registers the attacker's passkey | No | Registration controls (Part 4) |

![](https://images.squarespace-cdn.com/content/v1/52ad1d91e4b00a98a27ba20e/ff476401-5d5a-4994-8f1f-d80f845bdd37/flowchart2.png)

## Layer 1: tie access to trusted devices

A Conditional Access policy that requires a compliant (Intune) or Microsoft Entra hybrid joined device for sensitive apps makes a stolen cookie much less useful. When it's replayed from the attacker's laptop, the device claim fails.

This is the single most effective control against token replay today. Its limits are coverage: BYOD, contractors, and browser access from unmanaged devices. Combine it with app-enforced restrictions or session controls for those populations.

## Layer 2: token protection

[Token protection](https://learn.microsoft.com/en-us/entra/identity/conditional-access/concept-token-protection) is a Conditional Access session control, *Require token protection for sign-in sessions*. It cryptographically binds the sign-in session token to the device, so a token copied to another machine is rejected. It requires Entra ID P1.

| Platform | Native apps | Browser apps |
| --- | --- | --- |
| Windows | Generally available | Preview, supported web apps accessing Azure Resource Manager |
| macOS | Generally available | Preview, Azure Resource Manager web apps |
| iOS / iPadOS | Generally available | Not supported |

*As published on Microsoft Learn, September 2026. Some sections of the same page still label Apple platforms as preview, so check the current matrix before relying on it.*

Supported resources for native apps:

* Exchange Online
* SharePoint Online
* Microsoft Teams
* On Windows only: Azure Virtual Desktop and Windows 365

Apple devices need macOS 14+ or iOS 16+ with the Enterprise SSO plug-in, on MDM-managed devices.

How to deploy it ([deployment guide](https://learn.microsoft.com/en-us/entra/identity/conditional-access/deployment-guide-token-protection-windows)):

* Target Exchange, SharePoint and Teams individually. Microsoft warns that selecting the whole *Office 365* app group "might result in unintended failures".
* Scope client apps to *Mobile apps and desktop clients*.
* Run it in report-only first and read the **Token Protection – Sign In Session** field in the sign-in log. The status codes tell you why a request was *Unbound*:
  + 1002: no device state
  + 1003: device doesn't meet requirements
  + 1006: unsupported OS
  + 1008: client not integrated with the broker (WAM)

![](https://images.squarespace-cdn.com/content/v1/52ad1d91e4b00a98a27ba20e/fb8c2538-8ab9-4b62-bf25-0fd6c5094d26/conditional-access_deployment-guide-token-protection-windows_sign-in-log-sample-unbound-status-code-1002.png)

Sign-in log showing an unbound token protection session with status 1002

Token protection is valuable but **not universal**. It covers specific clients, platforms and resources. Plan it as one layer, not as "the fix for token theft".

## Layer 3: continuous access evaluation and session lifetime

Continuous access evaluation (CAE) lets supporting resources (Exchange, SharePoint, Teams, Graph) react in near real time to critical events instead of waiting for a token to expire ([CAE](https://learn.microsoft.com/en-us/entra/identity/conditional-access/concept-continuous-access-evaluation)). The critical events are:

* the account is deleted or disabled;
* the password is changed or reset;
* MFA is enabled for the user;
* an administrator explicitly revokes all refresh tokens;
* Identity Protection detects high user risk.

Critical event evaluation doesn't depend on Conditional Access policies, so it works in every tenant. SharePoint doesn't support user-risk events.

Sign-in frequency controls how often users must re-authenticate. The default is a rolling 90-day window. Shorter frequencies for high-risk apps or unmanaged devices limit how long a stolen token stays useful. Remember the known issue from Part 3: authentication strength and sign-in frequency can be satisfied at two different times.

## Layer 4: detection and response

Keep monitoring after the passkey rollout:

* Identity Protection risk detections, including anomalous token and token issuer anomalies, unfamiliar sign-in properties, and attacker-in-the-middle detections.
* Defender for Endpoint and Defender XDR infostealer and credential-access alerts. Correlate them with the user's sign-ins.
* **Sign-ins whose method class changed.** A user who has signed in with a passkey for months and suddenly satisfies MFA with SMS deserves a look.

### Response order matters

![](https://images.squarespace-cdn.com/content/v1/52ad1d91e4b00a98a27ba20e/3bde2653-839e-42f9-998a-ef48455758da/responseflow.png)

If you revoke sessions **first**, an attacker who still has a registered method or a working credential signs in again. Revocation also leaves existing access tokens alone. If the resource doesn't support CAE, those tokens stay valid until they expire. And it [doesn't revoke sessions for external users](https://learn.microsoft.com/en-us/graph/api/user-revokesigninsessions?view=graph-rest-1.0) in your tenant.

## Hands-on: measure real usage and respond

```
Connect-MgGraph -TenantId $tenantId -ContextScope Process -NoWelcome `
 ...