---
title: Microsoft Windows Installer Folder Delete Privilege Escalation
url: https://blog.exodusintel.com/2026/07/06/microsoft-windows-installer-folder-delete-privilege-escalation/
source: Exodus Intelligence
date: 2026-07-06
fetch_date: 2026-07-07T06:03:20.430383
---

# Microsoft Windows Installer Folder Delete Privilege Escalation

[Skip to content](#content "Skip to content")

[![Exodus Intelligence](https://blog.exodusintel.com/wp-content/uploads/2018/10/exodus-final-logo-1_small.png "Exodus Intelligence")](https://blog.exodusintel.com/ "Exodus Intelligence")

Menu

* [Blog](https://blog.exodusintel.com/)
  + [Exploit Techniques](https://blog.exodusintel.com/category/exploit-techniques/)
  + [News](https://blog.exodusintel.com/category/news/)
  + [Training](https://blog.exodusintel.com/category/training/)
  + [Vulnerability Analysis](https://blog.exodusintel.com/category/vulnerability-analysis/)
  + [Other](https://blog.exodusintel.com/category/other/)
* [Offerings](https://exodusintel.com/index.html)
* [Company](https://exodusintel.com/about.html)
* [Capabilities](https://exodusintel.com/zeroday.html)
* [Training](https://exodusintel.com/training.html)
* [Advisories](https://blog.exodusintel.com/advisories-2/)

# EXODUS BLOG

---

## Microsoft Windows Installer Folder Delete Privilege Escalation

JULY 6, 2026
[Vulnerability Analysis](https://blog.exodusintel.com/category/vulnerability-analysis/), [Exploit Techniques](https://blog.exodusintel.com/category/exploit-techniques/), [General Research](https://blog.exodusintel.com/category/general-research/)

By Endri Domi

## Overview

This blog post details a **logic vulnerability** discovered internally in the COM interface exposed from the `msi.dll` binary. The vulnerability allows a low-privileged user to cause the MSI service to delete an arbitrary folder that the user has access to, by scheduling its path in the `TempPackages` registry key. The service does not validate that the folder being deleted was actually created by the installer, it blindly trusts whatever paths are stored in TempPackages. The vulnerability was patched in April 2025 and assigned CVE-2025-27727.

The Microsoft Windows Installer service (`msiexec.exe`) runs as SYSTEM and handles the installation, modification, and removal of Windows applications packaged as `.msi` files. It exposes its functionality to client processes through a COM interface, a `CMsiConfigurationManager` COM object registered with CLSID `{000C101C-0000-0000-C000-000000000046}` that implements the `IMsiServer` interface (IID `{000C101C-0000-0000-C000-000000000046}`).

The exploit technique described in this post (Phases 0–3) leverages this folder-deletion primitive to achieve SYSTEM code execution by planting malicious rollback scripts in a newly recreated `C:\Config.Msi` folder.

**Disclaimer:** All function names, struct layouts, and vtable assignments presented in this post were derived through reverse engineering of `msi.dll` and may not reflect Microsoft’s internal naming conventions.

## Background

In this section we give an overviewof the Windows installer COM architecture and the `CMsiConfigurationManager` Vtable relevant to this vulnerability.

### Windows Installer COM Architecture

The Windows Installer service (`msiexec.exe`) runs as SYSTEM and exposes its functionality through a COM interface. Client processes, regardless of their privilege level, communicate with the service via COM method calls that are marshalled across process boundaries by the RPC runtime.

The server-side entry point is `CreateMsiServer()`, which instantiates a `CMsiConfigurationManager` COM object. This object implements the `IMsiServer` interface (which inherits from `IUnknown`) and serves as the central dispatcher for all installer operations, including transaction management, folder registration, rollback script handling, and temp package cleanup.

#### CMsiConfigurationManager Vtable

The public COM interface exposed to callers consists of **28 methods**: 3 from `IUnknown`(offsets 0x00–0x10) and 25 custom methods (offsets 0x18–0xD8). Entries beyond offset 0xD8 are internal-only, they are not reachable through the COM interface and are used for intra-process dispatch within the MSI service.

| Index | Offset | Method Name | Signature |
| --- | --- | --- | --- |
| 0 | 0x00 | QueryInterface | `(GUID* riid, void** ppv)` |
| 1 | 0x08 | AddRef | `()` |
| 2 | 0x10 | Release | `()` |
| 3 | 0x18 | InstallFinalize | `(iesEnum, IMsiMessage*, uchar)` |
| 4 | 0x20 | SetLastUsedSource | `(HWND, ushort*, ushort*, uchar, uchar)` |
| 5 | 0x28 | Reboot | `()` |
| 6 | 0x30 | DoInstall | `(ireEnum, ushort*, ushort*, ushort*, ushort*, int, uchar, IMsiMessage*, iioEnum, ulong, HWND*, IMsiRecord*)` |
| 7 | 0x38 | IsServiceInstalling | `()` |
| 8 | 0x40 | RegisterUser | `(ushort*, ushort*, ushort*, ushort*)` |
| 9 | 0x48 | RemoveRunOnceEntry | `(ushort*)` |
| 10 | 0x50 | CleanupTempPackages | `(IMsiMessage*, uchar)` |
| 11 | 0x58 | SourceListClearByType | `(ushort*, ushort*, isrcEnum)` |
| 12 | 0x60 | SourceListAddSource | `(ushort*, ushort*, isrcEnum, ushort*)` |
| 13 | 0x68 | SourceListClearLastUsed | `(ushort*, ushort*)` |
| 14 | 0x70 | RegisterCustomActionServer | `(icacCustomActionContext*, uchar*, int, IMsiCustomAction*, ulong*, IMsiRemoteAPI**, ulong*)` |
| 15 | 0x78 | CreateCustomActionServer | `(icacCustomActionContext, ulong, IMsiRemoteAPI*, ushort*, ulong, ulong, uchar*, int*, IMsiCustomAction**, ulong*, uchar, ushort)` |
| 16 | 0x80 | SourceListUpdate | `(uchar, ushort*, ushort*, ulong, ulong, ulong, ushort*, ushort*, ulong, iSrcOpEnum)` |
| 17 | 0x88 | SourceListSetInfo | `(ushort*, ushort*, ulong, ulong, ushort*, ushort*)` |
| 18 | 0x90 | SetInstallParentWindow | `(HWND*)` |
| 19 | 0x98 | UninstallApplication | `(ushort*, uint)` |
| 20 | 0xA0 | MsiBeginTransactionW | `(ushort*, ulong, ulong*, ushort*)` |
| 21 | 0xA8 | MsiEndTransaction | `(ulong, IMsiMessage*)` |
| 22 | 0xB0 | MsiJoinTransaction | `(ulong, ulong, ulong*, ushort*)` |
| 23 | 0xB8 | GetTransactionAttributes | `()` |
| 24 | 0xC0 | SetChangeOfOwnerEvent | `()` |
| 25 | 0xC8 | SetEEUIDirectoryAndFilter | `(ushort*, ulong)` |
| 26 | 0xD0 | GetJoinEEUIInfo | `(ushort*, ulong*, icacCustomActionContext*)` |
| 27 | 0xD8 | SetEEUIServerDetails | `(IMsiCustomAction*, uchar*, ulong, icacCustomActionContext)` |

The three vtable entries that are relevant for the vulnerability’s path:

* **Offset 0xA0** (`MsiBeginTransactionW`)
* **Offset 0xC8** (`SetEEUIDirectoryAndFilter`)
* **Offset 0x50** (`CleanupTempPackages`)

## Vulnerability

The `CMsiConfigurationManager` COM interface exposes three methods that, when called in sequence, allow a low-privileged user to cause the MSI service (running as SYSTEM) to delete an arbitrary folder:

1. **`MsiBeginTransactionW()`** establishes an active transaction.
2. **`SetEEUIDirectoryAndFilter()`** schedules a user-accessible folder path in the `TempPackages` registry key. The only access check is that the caller has `DELETE`permission on the folder, there is no verification that the folder was created by the MSI service.
3. **`CleanupTempPackages()`** enumerates `TempPackages` and deletes the referenced folders as SYSTEM. There is no validation that the paths being deleted were actually created by the installer, the service blindly trusts the TempPackages registry contents.

The logic flaw is straightforward: the MSI service trusts the TempPackages registry as an authoritative record of folders it should clean up, but a low-privileged user can write arbitrary paths to this registry key via `SetEEUIDirectoryAndFilter()`. The only gatekeeping is a `DELETE` permission check on the folder, which is trivially satisfied if the user created the folder themselves with permissive ACLs. Once a path is in `TempPackage`, `CleanupTempPackages()` will delete it as SYSTEM, including `LockdownPath` fallback to override restrictive ACLs. The service assumes that `TempPackages` entries are created only by the installer itself, but the COM interface allows low-privileged users to inject arbitrary paths.

### CMsiConfigurationManager::MsiBeginTransactionW()

The `CMsiConfigurationManager::MsiBeginTransactionW()` method is the COM interface method at vtable offset `0xA0`:

```
__int64 __fastcall CMsiConfigurationManager::MsiBeginTrans...