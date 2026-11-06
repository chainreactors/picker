---
title: Moving an organization to passkeys without breaking access
url: https://www.darkoperator.com/blog/2026/11/5/moving-an-organization-to-passkeys-without-breaking-access
source: Shell is Only the Beginning
date: 2026-11-05
fetch_date: 2026-11-06T08:40:17.969412
---

# Moving an organization to passkeys without breaking access

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

# [Moving an organization to passkeys without breaking access](/blog/2026/11/5/moving-an-organization-to-passkeys-without-breaking-access)

[November 05, 2026](/blog/2026/11/5/moving-an-organization-to-passkeys-without-breaking-access)
[by Carlos Perez](/?author=5005b71ac4aa8b4d97616588)

### A phased roadmap, the SMS/voice retirement deadlines, metrics that prove progress, and a repeatable readiness report

*MFA to Passkeys in Microsoft Entra ID series · Part 7 of 7*

Parts 1 to 6 each covered one piece of the work: the threat model, the credential choice, enforcement, enrollment, session protection, and privileged access. This final part puts them in order.

Moving to passkeys takes more than changing an authentication method setting. The programme touches every user, the service desk, endpoint management, and incident response. A planned rollout cuts AiTM phishing risk sharply without a wave of lockouts. A rushed rollout, run against Microsoft's deadlines, floods the help desk with recovery calls, and attackers exploit that confusion.

![](https://images.squarespace-cdn.com/content/v1/52ad1d91e4b00a98a27ba20e/cc4b3d7a-e0d1-4125-925a-351d707ad0e5/rollout-steps.png)

## The clock: where we are at Q4 2026

From [Microsoft Learn: passkeys by default and SMS/voice retirement](https://learn.microsoft.com/en-us/entra/identity/authentication/concept-sms-voice-retirement):

* 1 Sep 2026 (done): passkeys became the default. SMS/voice-enabled users were auto-enabled for passkeys, and the registration campaign moved to Microsoft managed.
* 18 Sep 2026 (done): customer-managed telecom providers became available to review in the Microsoft Security Store.
* 30 Oct 2026 (this month): customer-managed telecom providers can be selected and configured.
* 1 Feb 2027 (upcoming): Microsoft-provided SMS/voice retires for everyone except Global Administrators and external users. SMS/voice-only users get a **blocking** passkey registration prompt, with no opt-out.
* 1 Jul 2027 (upcoming): the same applies to Global Administrators and external users.

The auto-enablement has already happened, and you have roughly four months until the first hard deadline.

![](https://images.squarespace-cdn.com/content/v1/52ad1d91e4b00a98a27ba20e/4fc88b5f-bf99-4196-a136-cf7e36efdbaf/gant.png)

Aim to have **every user in scope registered and using a passkey well before 1 February 2027.** Then Microsoft's blocking prompt reaches nobody who hasn't already gone through your own supported, communicated process.

The example plan assumes you start in the first week of October, so it's tighter than it would have been over the summer. If your start slips, shorten the pilot waves rather than enrollment and recovery, and use customer-managed telecom as a bridge for a documented population instead of rushing workforce enforcement.

## The seven phases

Microsoft's [deployment guide](https://learn.microsoft.com/en-us/entra/identity/authentication/how-to-deploy-phishing-resistant-passwordless-authentication) frames the same journey as onboarding, then enforcement, per persona:

![](https://images.squarespace-cdn.com/content/v1/52ad1d91e4b00a98a27ba20e/434e5073-0e73-4a5d-bcb3-ae66b4a1cfff/how-to-deploy-phishing-resistant-passwordless-authentication_planning-phases.png)

Microsoft's planning phases for phishing-resistant passwordless deployment

### Phase 1: Baseline (Part 1)

* Run `Export-EptReadinessReport` (below) and keep the output as your "before" picture.
* Run Microsoft's [SMS/voice usage analyzer](https://github.com/microsoft/entra-sms-voice-usage-analyzer) (Global Reader, Authentication Policy Administrator or Security Reader). Per the FAQ, *any non-zero result means you're in scope.*
* Keep three lists separate: users registered for telephony, users policy-enabled for telephony, and users who recently used telephony.
* Inventory the special populations: shared devices, kiosks, frontline workers without company phones, VDI and jump hosts, contractors, guests (no passkey support until later in 2026), and service accounts set up as user accounts.

### Phase 2: Target architecture and policy hygiene (Parts 2 and 3)

**Finish the Authentication methods policy migration.** In *Migration in progress*, both the legacy MFA/SSPR settings and the new policy are honored. In *Migration complete*, only the Authentication methods policy counts, so there's one source of truth. The change is reversible.

![](https://images.squarespace-cdn.com/content/v1/52ad1d91e4b00a98a27ba20e/46344ac5-24d6-4056-ba92-a00b977b99d8/how-to-authentication-methods-manage_migration-complete.png)

Manage migration: start the migration

Then build the rest of the architecture:

* Personas and passkey profiles for Tier 0, sensitive, workforce, and frontline users (Part 2).
* The built-in Phishing-resistant MFA authentication strength, plus a custom Tier 0 strength limited to approved AAGUIDs (Part 3).
* Conditional Access policies in report-only mode: CA010/011 (device code and authentication transfer), CA100 (admins), and CA110 (pilot).
* An exception register. Every exception needs an owner and an expiry date, and none are permanent.

### Phase 3: Enrollment and recovery (Part 4)

* Set up the TAP policy (one-time, short lifetime) and the Register security information Conditional Access policy.
* Document identity verification per tier, and train the service desk *before* nudges start.
* Decide on the registration campaign: keep **Microsoft managed** (unlimited snoozes) during the pilot, and switch to **Enabled** with limited snoozes for the push to completion.
* Test the four hard journeys: new hire, replacement device, lost everything, and no smartphone.

### Phase 4: Administrators first (Part 6)

* Issue two attested security keys per admin. Register them in person or through dual-control TAP.
* Enforce CA100/CA101 once `Get-EptPrivilegedUser | Test-EptPhishResistantCoverage` shows every admin as `Covered`.
* Remove phishable methods from the admin persona. Set up break-glass passkeys and sign-in alerts.

### Phase 5: Representative pilot waves

* Include every OS/browser combination you support, BYOD and corporate devices, remote and office staff, and at least one team of heavy Teams Rooms or shared-device users.
* For each wave, communicate, nudge, and measure registration. Then run the policy in report-only mode, enforce it, and measure usage.
* Microsoft recommends a communications cadence of 60, 45, 30, 15, 7 and 1 days before enforcement.

Microsoft's Passwordless workbook can list who is ready for enforcement per platform:

![](https://images.squarespace-cdn.com/content/v1/52ad1d91e4b00a98a27ba20e/6959f448-1c0d-4a01-94ee-d5c58bc805db/how-to-deploy-phishing-resistant-passwordless-authentication_workbook-enforcement-user-lists-1.png)

### Phase 6: Workforce enforcement

* Enforce by OS group, following Microsoft's recommendation of one Conditional Access policy per platform.
* Move the campaign to **Enabled** with limited snoozes for the remaining stragglers.
* Retire SMS/voice from the Authentication methods policy group by group as usage drops to zero. Don't leave telephony enabled "just in case". Telephony is the fallback attackers use.

### Phase 7: Sessions and continuous hardening (Part 5)

* Requi...