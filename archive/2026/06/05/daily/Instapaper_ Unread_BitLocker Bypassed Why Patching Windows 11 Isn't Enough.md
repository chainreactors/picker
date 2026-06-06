---
title: BitLocker Bypassed Why Patching Windows 11 Isn't Enough
url: https://blog.sekurity.de/blog/bitlocker-bypass-winre/
source: Instapaper: Unread
date: 2026-06-05
fetch_date: 2026-06-06T05:51:31.781365
---

# BitLocker Bypassed Why Patching Windows 11 Isn't Enough

[Skip to main content](#main-content)

[![SEKurity GmbH Logo](/SEKurityLogo-OuterGlow.png)](/)     [Home](/)  [Blog](/blog)  [Categories](/categories)  [Tags](/tags)  [About](/about)  [SEKurity.de ↗](https://sekurity.de)

EN

[EN English](/blog/bitlocker-bypass-winre/)  [DE Deutsch](/de/blog/bitlocker-bypass-winre/)

[Home](/)  [Blog](/blog)  [Categories](/categories)  [Tags](/tags)  [About](/about)  [SEKurity.de ↗](https://sekurity.de)

Language

EN

[EN English](/blog/bitlocker-bypass-winre/)  [DE Deutsch](/de/blog/bitlocker-bypass-winre/)

Theme

[Home](/)    [Blog](/blog)     [General](/categories/general)     BitLocker Bypassed – Why a Fully Patched Windows 11 Isn't Enough

General

# BitLocker Bypassed – Why a Fully Patched Windows 11 Isn't Enough

BitUnlocker and YellowKey show that BitLocker bypasses don't break cryptography — they exploit the trust chain around WinRE, TPM, and Secure Boot.

Alexander Sturz

Founder & Red Team Lead

Published May 29, 2026  12 min read

Share:

## Executive Summary

In mid-2025, Microsoft’s STORM team presented BitUnlocker — four vulnerabilities that showed how BitLocker can be bypassed via the Windows Recovery Environment (WinRE). The patches shipped in July 2025; the public disclosure followed at Black Hat USA and DEF CON 33 in August 2025. In May 2026, YellowKey (CVE-2026-45585) added another vulnerability on the same attack surface.

What is remarkable here is not the existence of individual vulnerabilities. What is remarkable is that both disclosures build on the same design decision: for Windows to be repairable, BitLocker must trust the recovery environment.

Anyone who wants to understand why a fully patched Windows system can still be vulnerable has to understand how TPM, PCRs, Secure Boot, WinRE and the recovery partition interact.

---

## BitLocker Does Not Protect the Disk

Many administrators describe BitLocker, in simplified terms, as disk encryption.

Technically that is not wrong, but it is incomplete.

The real security question is not:

> Is the data encrypted?

But rather:

> Under what conditions is the key released?

Breaking the XTS-AES used by BitLocker (128-bit by default, optionally 256-bit) is practically impossible, provided no trivial key is used. This is why modern attacks do not target the cryptography, but the mechanism that decides when the key may be used.

This is exactly where the TPM comes in.

---

## TPM, PCRs and the Actual Chain of Trust

A common simplification is:

> The TPM secures the key.

Technically, something different happens.

During startup, firmware and boot components each measure the next component in the boot chain. The resulting hash values are written into the TPM’s Platform Configuration Registers (PCRs) via so-called PCR-Extend operations.

Simplified:

```
UEFI Firmware
      |
      |-- measures next component
      |
      |-- computes hash
      |
      +-- PCR Extend
               |
               v
          TPM PCR Register
```

The TPM does not assess whether something is “secure” or “insecure”.

It merely stores the measurements in a tamper-resistant manner.

The decisive factor is which of these registers BitLocker actually includes in its sealing. The **default profile of modern Windows installations with Secure Boot covers PCR 7 and PCR 11**:

```
PCR7  -> Secure Boot state
         (policies, certificates)

PCR11 -> BitLocker access control
         (seal/unseal state machine)
```

PCR 11 is the actual “lock” against which BitLocker seals the key.

In addition, there is an **extended profile** that also measures early boot components:

```
PCR0  -> CRTM and firmware measurements

PCR2  -> Option ROMs

PCR4  -> Boot Manager / Boot Loader
```

These three registers are **not** part of the BitLocker policy by default. This becomes relevant for the attacks later: anyone who re-adds PCR 0/2/4 makes the TPM notice a change to the firmware and boot-manager chain — and that is precisely what blocks the downgrade variant described further below. Which PCRs are actually used depends on hardware, firmware and configuration.

---

## Sealing and Unsealing: What BitLocker Actually Does

When BitLocker is enabled, the Volume Master Key is not simply stored on the disk.

Instead, it is sealed against a defined PCR state.

Simplified:

```
Volume Master Key
        |
        v
TPM Seal Operation
        |
        v
Released only on matching PCR values
```

At system start, Windows then tries to unseal the key again.

If the PCR values are identical to the state at sealing time, the key is released.

Otherwise, the BitLocker recovery prompt appears.

```
PCR values match
        |
        v
Unseal successful
        |
        v
Windows boots

PCR values differ
        |
        v
Recovery key required
```

Important:

The TPM does not check whether Windows has been compromised.

It only checks whether the measured boot chain matches the expected state.

---

## Why BitLocker Must Trust WinRE

This is where the actual problem begins.

With WinRE, Windows has a recovery environment for repairs, resets and diagnostics.

When Windows no longer boots, WinRE should still be able to access the encrypted operating system.

Without this capability, many repair operations would be impossible.

Microsoft therefore had to make a design decision:

```
Normal boot
    |
    v
Windows

Recovery boot
    |
    v
WinRE
```

Both paths must be able to gain access to the encrypted operating system.

It is precisely from this that the later attack surface arises.

---

## The Recovery Partition: The Actual Attack Point

A typical Windows system looks, simplified, roughly like this:

```
+--------------------------------+
| EFI System Partition           |
+--------------------------------+

+--------------------------------+
| Recovery Partition             |
|                                |
| WinRE.wim                      |
| ReAgent.xml                    |
| Boot.sdi                       |
| BCD                            |
| ResetConfig.xml                |
+--------------------------------+

+--------------------------------+
| BitLocker Volume (C:)          |
|                                |
| Windows                        |
| Users                          |
| Applications                   |
+--------------------------------+
```

Many administrators overlook an important point here:

The recovery partition is normally not BitLocker-protected.

This is not a misconfiguration.

It *could* technically be encrypted — after all, the boot manager also unlocks the operating-system volume.

But it deliberately is not: if the recovery environment were bound to the same encryption, it would be unavailable precisely when the OS volume can no longer be unlocked — that is, in the repair scenario.

WinRE is therefore kept on its own partition, which is not covered by the BitLocker policy of the operating-system drive — independent of the unlock state of C:.

---

## Why Secure Boot Does Not Solve the Problem

The next common assumption is:

> But that’s what Secure Boot is for.

Secure Boot, however, solves a different problem.

Secure Boot verifies whether loaded components originate from a trusted signature chain.

The flow looks, simplified, like this:

```
UEFI
 |
 v
Secure Boot
 |
 v
Boot Manager
 |
 v
WinRE
 |
 v
BitLocker Unseal
 |
 v
Vulnerability
```

The attacks do not occur before Secure Boot.

They occur after successful Secure Boot validation, inside an already trusted environment.

Secure Boot therefore works correctly.

It merely protects against a different class of attack.

There is, however, a more subtle interaction: Secure Boot trusts not only the current Microsoft components, but also **older ones that are still validly signed**. It is precisely this property that makes the downgrade attack described below possible — there, Secure Boot is not bypassed; rather, its trust in old, not-yet-revoked signatures is exploited.

---

## BitUnlocker: Four Vuln...