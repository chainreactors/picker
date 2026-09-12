---
title: forti-research
url: https://kitploit.com/en/tools/github/mein-0/forti-research
source: Kitploit
date: 2026-09-11
fetch_date: 2026-09-12T06:48:12.872457
---

# forti-research

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

[Tools](/en/tools)/![GitHub](/providers/github.png)GitHub/mein-0/forti-research

![](https://assets.kitploit.com/production/public/tools/54731/0f5f95baa4e10238f1b299bf7f9e983e4fc6bbaaec885d5c7476b1804401c4c8-display-v1.webp)

[Defensive Tools](/en/categories/defensive-tools)[Privilege Escalation](/en/categories/privilege-escalation)[Vulnerability Analysis](/en/categories/vulnerability-analysis)[Exploitation](/en/categories/exploitation)[Binary Exploitation](/en/categories/binary-exploitation)

![GitHub](/providers/github.png)mein-0/forti-research

# forti-research

Proof-of-concept exploiting a Fortinet fortimon3\_74.sys kernel driver flaw to bypass PPL and terminate protected processes like lsass.exe via an unauthenticated kill command.

[View Repository](https://github.com/mein-0/forti-research)

22371 day ago![Not yet reviewed](/_next/image?url=%2Fbadges%2Fkitploit_badge_not_reviewed_full.png&w=48&q=75)

### Most Popular

[View all →](/en/tools)

Discover the most used tools by our community.

Last 7 DaysLast 30 Days

Explore all tools

Browse our collection of tools

[View all tools →](/en/tools)

Share

# Fortinet fortimon3\_74.sys - PPL Bypass via Unauthenticated Kill Command

## Overview

A vulnerability in Fortinet's `fortimon3_74.sys` kernel driver (FortiClient's "anti-exploit" minifilter) allows any local administrator to terminate **any** process - including PPL (Protected Process Light) protected processes like **Windows Defender (MsMpEng.exe)** and **lsass.exe** - by sending an 8-byte message to an unauthenticated communication port.

No buffer overflow. No heap spray. No ROP chain. Just 8 bytes.

## Vulnerability Details

| Field | Value |
| --- | --- |

|  |  |
| --- | --- |
| **Driver** | `fortimon3_74.sys` (FortiClient Anti-Exploit Minifilter) |
| **Port** | `\Fortimon3FilterAntiExploitPort` |
| **Impact** | PPL bypass, arbitrary process termination |
| **Access** | Local administrator |
| **Authentication** | None |
| **BYOVD Risk** | High - driver is signed by Fortinet |

The driver exposes a minifilter communication port with no caller authentication. It accepts a simple 8-byte message:

root@kitploit:~

```
struct {
    DWORD magic;  // 0x6C6C696B ("kill" in little-endian ASCII)
    DWORD pid;    // Target process ID
};
```

Upon receiving this message, the driver calls `ZwOpenProcess` with `PROCESS_ALL_ACCESS` from kernel mode (bypassing PPL checks), then `ZwTerminateProcess`. No validation is performed on the caller or target.

### Additional Issue: Handle Leak

The `ZwOpenProcess` handle is created in the **caller's handle table** (missing `OBJ_KERNEL_HANDLE` flag), creating a brief window where a usermode attacker could duplicate a `PROCESS_ALL_ACCESS` handle to a PPL-protected process like `lsass.exe` - enabling credential theft without killing the process.

## Root Causes

1. **No caller authentication** - any admin process can connect to the port
2. **No target validation** - any PID is accepted, including system-critical processes
3. **Excessive privilege** - `PROCESS_ALL_ACCESS` used instead of `PROCESS_TERMINATE`
4. **Handle table misuse** - missing `OBJ_KERNEL_HANDLE` flag exposes kernel handle to usermode

## Demo

### lsass.exe Kill (PPL-protected)

![LSASS Kill - System forced restart](https://assets.kitploit.com/production/public/readmes/54731/0f5f95baa4e10238f1b299bf7f9e983e4fc6bbaaec885d5c7476b1804401c4c8/608b906c18ab06b3c500e1fe13504e075ae7ed60c80ed5e85b83777e33dc90f9-display-v1.webp)

### Video Demo

[Watch the full demo](https://github.com/mein-0/forti-research/blob/main/forti.mp4) - demonstrates PPL bypass against protected processes.

## Files

| File | Description |
| --- | --- |
| `poc.c` | Proof of Concept - terminates any process by name via the vulnerable driver |
| `fortimon3_74.sys` | Vulnerable driver binary (Fortinet-signed) |
| `poc.jpg` | Screenshot - lsass.exe terminated, system restart triggered |
| `forti.mp4` | Video demo of the exploit |

## Build & Usage

root@kitploit:~

```
cl.exe poc.c /Fe:poc_kill.exe
poc_kill.exe MsMpEng.exe
```

Requires: local administrator privileges, `fortimon3_74.sys` loaded.

## Disclosure

* Reported to Fortinet PSIRT with full technical details, PoC, and video demo
* Status: **Duplicate** (another researcher reported the same issue)

*me1n*

[Download Tool](https://github.com/mein-0/forti-research)