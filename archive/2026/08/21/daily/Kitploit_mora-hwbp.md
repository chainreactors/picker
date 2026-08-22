---
title: mora-hwbp
url: https://kitploit.com/en/tools/github/dovughs/mora-hwbp
source: Kitploit
date: 2026-08-21
fetch_date: 2026-08-22T02:51:04.470814
---

# mora-hwbp

[Skip to content](#main-content)

[![Kitploit](/_next/image?url=%2Flogo.png&w=64&q=75)KITPLOIT](/en)[Tools](/en/tools)[Blog](/en/blog)Categories

EN

[Submit](/en/submit)

[Tools](/en/tools)[Blog](/en/blog)Categories

[Submit](/en/submit)

EN

Hacking, PenTest, and Cybersecurity Tools for Your Security Arsenal!

Kitploit is a directory of hacking, cybersecurity, and pentesting tools. Discover the latest project updates to find vulnerabilities, analyze systems, automate testing, and strengthen your security.

·Analytics preferences·[Feeds](/en/feeds)·[Contact](/en/contact)·[Privacy](/en/privacy)·© 2026 Kitploit

Tool Directory

## Categories

[View all categories](/en/categories)

Loading categories

[Tools](/en/tools)/![GitHub](/providers/github.png)GitHub/dovughs/mora-hwbp

![](https://assets.kitploit.com/production/public/tools/50594/5cf99fadc07272ff598cbb9486ff7803a3234eb6aeaa8202684c27e97bd7e161.png)

[Defensive Tools](/en/categories/defensive-tools)[IDS/IPS Evasion](/en/categories/ids-ips-evasion)[Debuggers](/en/categories/debuggers)[Learning & Education](/en/categories/education)[Red Teaming](/en/categories/red-teaming)[Adversarial Attack](/en/categories/adversarial-attack)

![GitHub](/providers/github.png)dovughs/mora-hwbp

# mora-hwbp

Hardware Breakpoint (DR0-DR7) based patch-less user-mode hooking & telemetry instrumentation engine (AMSI, WLDP & ETW PoC).

[View Repository](https://github.com/dovughs/mora-hwbp)

102 days ago![Not yet reviewed](/_next/image?url=%2Fbadges%2Fkitploit_badge_not_reviewed_full.png&w=48&q=75)

### Most Popular

[View all →](/en/tools)

Discover the most used tools by our community.

Last 7 DaysLast 30 Days

Explore all tools

Browse our collection of tools

[View all tools →](/en/tools)

Share

# Mora-HWBP — AMSI / WLDP / ETW Telemetry Hooking via Hardware Breakpoints

**A security-research Proof-of-Concept (POC) demonstrating hardware-breakpoint (CPU debug register) based function hooking as an alternative to traditional in-memory code patching.**

> **Purpose & Scope**
>
> This repository is published **strictly for defensive security research, red-team/purple-team education, detection engineering, and academic study** of Windows internals. It demonstrates *how* an attacker could abuse processor debug registers to neutralize user-mode security telemetry — and, equally important, *what defenders should monitor for* in order to detect such techniques. The author is **not** responsible for any misuse of this code. Usage of this technique against systems without explicit authorization is illegal and violates the relevant computer-fraud and abuse laws in most jurisdictions. **Do not deploy this in any environment you do not own or have explicit written permission to test.**

---

## Table of Contents

1. [Overview](#overview)
2. [Background — Why Hardware Breakpoints?](#background--why-hardware-breakpoints)
3. [Targeted Security Components](#targeted-security-components)
4. [Architecture](#architecture)
5. [Technical Deep Dive](#technical-deep-dive)
   * [5.1 Hardware Breakpoints on x64](#51-hardware-breakpoints-on-x64)
   * [5.2 Debug Register Layout (DR0–DR7)](#52-debug-register-layout-dr0dr7)
   * [5.3 The Vectored Exception Handler (VEH)](#53-the-vectored-exception-handler-veh)
   * [5.4 Per-Component Interception Logic](#54-per-component-interception-logic)

- [5.5 Thread Management & Hook Persistence](#55-thread-management--hook-persistence)

- [Exported API](#exported-api)

- [Build Instructions](#build-instructions)

- [Injection & Usage Example](#injection--usage-example)

- [Detection & Mitigation (Blue Team)](#detection--mitigation-blue-team)

- [Known Limitations](#known-limitations)

- [References](#references)

---

## Overview

`mora_hwbp.c` implements a DLL that, once loaded/injected into a target process (e.g., a PowerShell host), hooks **four** user-mode functions **exclusively through CPU hardware breakpoints** stored in the architectural debug registers (`DR0`–`DR7`) of every thread in the process:

| Register | Hooked Function | Module | Purpose |
| --- | --- | --- | --- |
| `DR0` | `AmsiScanBuffer` | `amsi.dll` | Neutralize AMSI content scanning |
| `DR1` | `AmsiScanString` | `amsi.dll` | Neutralize AMSI string scanning |
| `DR2` | `WldpIsClassInApprovedList` | `wldp.dll` | Force WLDP class approval (Device Guard / WDAC) |
| `DR3` | `EtwEventWrite` | `ntdll.dll` | Suppress ETW event tracing |

A per-process **Vectored Exception Handler (VEH)** receives the `EXCEPTION_SINGLE_STEP` (0x80000004) faults raised by the debug registers, simulates the original function's *successful* return path by rewriting the exception context, and resumes execution — all **without modifying a single byte of executable memory**.

This makes the technique particularly interesting from both offensive and defensive perspectives:

* **Offensively**, it bypasses EDR/HIPS integrity checks that look for modified `.text` sections (classic inline hooking, `EAT`/`IAT` patching, or `Etwp*` stubbing).
* **Defensively**, hardware breakpoints leave highly distinctive forensic artifacts (debug-register contents, single-step exception density, VEH registration, `GetThreadContext`/`SetThreadContext` syscall patterns) that can be used for detection.

---

## Background — Why Hardware Breakpoints?

Traditional user-mode hooking approaches — inline detours (5–14 byte overwrites), import address table (IAT) hooking, and export address table (EAT) hooking — share a common weakness: **they modify memory that integrity scanners and ETW can observe.**

Modern AV/EDR products implement:

* **Memory scanning / AMSI scans** of PowerShell and .NET CLR buffers;
* **ETW-based telemetry** (Microsoft-Windows-PowerShell, .NET ETW, threat intelligence providers);
* **Kernel callbacks and user-mode integrity checks** that detect `pageguard`/`guard-page` tricks, `VirtualProtect` transitions to `PAGE_EXECUTE_READWRITE`, and section hash mismatches.

Hardware breakpoints sidestep all of this:

1. They are **CPU registers**, not memory — there is nothing to scan in `.text`.
2. They are set on a **per-thread** basis via the Windows API `SetThreadContext`, which does **not** trigger the classic "memory modified" signals used by integrity scanners.
3. The interception point is handled entirely by the **processor's exception dispatch**, which routes through the process VEH chain before any user-mode target function executes.

This POC explores the efficacy and detectability of this technique against **AMSI (Antimalware Scan Interface)**, **WLDP (Windows Lockdown Policy)**, and **ETW (Event Tracing for Windows)** — the three most widely relied-upon user-mode security primitives in the modern Windows security stack.

---

## Targeted Security Components

### AMSI — Antimalware Scan Interface

AMSI is the Windows platform integration point that allows applications (PowerShell, Office, VBScript, .NET hosts, etc.) to request content scanning from registered antimalware providers. Two entry points are of primary interest:

* `AmsiScanBuffer(HANDLE hamsiContext, PVOID buffer, ULONG length, LPCWSTR contentName, HANDLE hamsiSession, AMSI_RESULT *pResult)`
* `AmsiScanString(HANDLE hamsiContext, LPCWSTR string, LPCWSTR contentName, HANDLE hamsiSession, AMSI_RESULT *pResult)`

By forcing the returned `AMSI_RESULT` to `AMSI_RESULT_CLEAN (0)`, the script engine believes the content was inspected and found benign, so execution continues uninterrupted.

### WLDP — Windows Lockdown Policy

WLDP implements policy evaluation for Windows Defender Application Control (WDAC / Device Guard). `WldpIsClassInApprovedList` answers whether a given COM class (identified by GUID) is permitted under the current policy. AMSI internally consults WLDP to decide whether certain script/content classes are "trusted" (in the approved list). If the function reports the class as approved, AMSI may skip additional scrutiny for that content type.

The DLL sets the `isApproved` output parameter (`RDX...