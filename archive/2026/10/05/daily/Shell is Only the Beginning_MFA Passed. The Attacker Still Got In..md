---
title: MFA Passed. The Attacker Still Got In.
url: https://www.darkoperator.com/blog/2026/10/5/mfa-passed-the-attacker-still-got-in
source: Shell is Only the Beginning
date: 2026-10-05
fetch_date: 2026-10-06T08:24:37.362827
---

# MFA Passed. The Attacker Still Got In.

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

# [MFA Passed. The Attacker Still Got In.](/blog/2026/10/5/mfa-passed-the-attacker-still-got-in)

[October 05, 2026](/blog/2026/10/5/mfa-passed-the-attacker-still-got-in)
[by Carlos Perez](/?author=5005b71ac4aa8b4d97616588)
in [Blue Team](/blog/category/Blue%2BTeam)

## \*MFA to Passkeys in Microsoft Entra ID series · Part 1 of 7

As long as I can remember, "turn on MFA" has been the single most repeated piece of identity security advice, heck I repeat this phrase on regular basis to customers at work, and for good reason. The security community has seen and experience has long shown that MFA blocks the overwhelming majority of password-based account compromise. But when we look at incident reports from the last two years and a pattern starts showing up: **the user completed MFA, and the attacker still got in.**

That is not a contradiction. MFA is not a single security property, even when we give the advise we lump it as one. It is a *category* of authentication methods, and those methods behave very differently under attack. An SMS code, an authenticator OTP, a push approval, and a FIDO2 passkey all satisfy a checkbox labeled "MFA". Only one of them is designed so that a convincing fake sign-in page cannot use it.

This first part of a series of blog post, this first one sets the foundation for the rest of the series:

* Why traditional MFA fails against modern phishing kits,
* What "phishing-resistant" actually means,
* Why Microsoft's 2026–2027 changes make this urgent,
* How to measure your tenant's real starting point with PowerShell.

![](https://images.squarespace-cdn.com/content/v1/52ad1d91e4b00a98a27ba20e/a08097ba-4b4f-44e2-ae97-cd8e296fea35/secure-sign-in.png)

*Passkeys protect the sign-in ceremony. Parts 5 and 6 cover what happens after it.*

## The series at a glance

| Part | Title | What you walk away with |
| --- | --- | --- |
| **1** | MFA Passed. The Attacker Still Got In. | Threat model, method strength ladder, baseline measurement |
| 2 | Passkeys Explained, and Choosing the Right Model | How WebAuthn stops phishing, device-bound vs. synced, passkey profiles |
| 3 | Enabling Passkeys Is Not Enforcing Them | Authentication strengths, Conditional Access, blocking device code flow |
| 4 | Enrollment and Recovery: The New Weak Point | TAP, securing registration, help desk procedures, audit monitoring |
| 5 | Passkeys Stop Phishing, Not Every Token Theft | Session protection, token protection, sign-in analytics, incident response |
| 6 | Protecting Privileged Access | Admin personas, break-glass accounts, app owners and other hidden admins |
| 7 | The Migration Roadmap | Phased plan, SMS/voice retirement, metrics, checklist |

Every part ships PowerShell **advanced functions** from a companion module, **EntraPasskeyToolkit** (You know me I have to add some PowerShell in to the mix :) ). The functions are built to pipe into each other. For example, `Get-EptPrivilegedUser | Test-EptPhishResistantCoverage` takes every admin in your tenant and tells you whether a phishing-resistant policy actually covers them.

## MFA is a category, not a control

Start by lining the methods up by what they actually resist:

| Method | Resists password spray / reuse | Resists real-time phishing (AiTM) | Resists SIM swap | Satisfies the built-in *Phishing-resistant MFA* strength |
| --- | --- | --- | --- | --- |
| Password only | No | No | n/a | No |
| SMS / voice call | Yes | No | No | No |
| Authenticator OTP / hardware OATH | Yes | No | Yes | No |
| Authenticator push with number matching | Yes | No (relay still works) | Yes | No |
| Authenticator passwordless phone sign-in | Yes | No | Yes | No (satisfies *Passwordless MFA*) |
| **Passkey (FIDO2)**: security key, Authenticator, synced, Entra passkey on Windows | Yes | Yes | Yes | Yes |
| **Windows Hello for Business / platform credential** | Yes | Yes | Yes | Yes |
| **Certificate-based authentication (multifactor)** | Yes | Yes | Yes | Yes |

In the table the last column matters most. Entra ID's built-in **Phishing-resistant MFA** authentication strength accepts exactly three families of methods:

* Windows Hello for Business or platform credential
* Passkeys (FIDO2)
* Multifactor certificate-based authentication ([Microsoft Learn: authentication strengths](https://learn.microsoft.com/en-us/entra/identity/authentication/concept-authentication-strengths)).

Everything above them in the table can be phished.

> **Number matching is good, but it is not phishing resistance.** It kills MFA-fatigue "spam until they approve" attacks, this is why Microsoft enforces it for Authenticator push. It does nothing against an adversary-in-the-middle proxy, because the victim is looking at the attacker's page and dutifully types the number that page shows.

## Four ways attackers get past MFA

### 1. Adversary-in-the-middle (AiTM) phishing

This is the technique behind most if not all of the modern Microsoft 365 business email compromise that we see. Kits like Evilginx, and the phishing-as-a-service platforms built on the same idea, run a reverse proxy between the victim and the real `login.microsoftonline.com`.

![](https://images.squarespace-cdn.com/content/v1/52ad1d91e4b00a98a27ba20e/763b8dba-08ee-4579-9621-c071b1739050/Attacker+MFA.jpg)

MFA did not fail. The real user really did complete the challenge. Where weakness lies is that nothing in an OTP, SMS or push response is tied to the **website** the user was looking at, so the proxy can relay it. The prize is the session cookie. The attacker replays it from their own browser and never has to authenticate again until it expires or is revoked.

### 2. MFA fatigue and social engineering

These are push bombing and "Hi, it's the IT help desk, please approve the prompt I'm about to send". Number matching and additional context (app name, location) mostly neutralized raw push bombing. Help-desk impersonation moved elsewhere: attackers now call the **service desk** and talk their way into a new registration or a password reset. Part 4 covers that.

### 3. SIM swap and telephony interception

SMS and voice depend on the security of the mobile carrier's customer-service process and the SS7 network. A successful SIM swap redirects every code to the attacker. This is a major reason Microsoft is retiring Microsoft-provided SMS and voice for Entra MFA (see the timeline below).

### 4. Device code phishing

The attacker starts a legitimate OAuth *device code flow*, then sends the victim the real `https://microsoft.com/devicelogin` URL with a code: "Enter this code to view the shared document". The victim authenticates on a **genuine Microsoft page**, with whatever MFA they have, and the tokens go to the attacker's device. Passkeys do not help here: the victim really is on the real site, approving a sign-in for someone else's device. The fix is a Conditional Access policy that blocks device code flow, which Microsoft explicitly recommends "wherever possible" ([Microsoft Learn: authentication flows](https://learn.microsoft.com/en-us/entra/identity/conditional-access/concept-authentication-flows)). Part 3 builds that policy.

### And after sign-in: token theft

Infostealer malware on an endpoint doesn't need to phish anyone. It copies the browser's cookie store ...