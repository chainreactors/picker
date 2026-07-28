---
title: From Virtual Share to Physical Shell: Leveraging Windows’ Inconsistent Access Control for LPE
url: https://blog.exodusintel.com/2026/07/27/from-virtual-share-to-physical-shell-leveraging-windows-inconsistent-access-control-for-lpe/
source: Exodus Intelligence
date: 2026-07-27
fetch_date: 2026-07-28T04:58:41.064737
---

# From Virtual Share to Physical Shell: Leveraging Windows’ Inconsistent Access Control for LPE

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

## From Virtual Share to Physical Shell: Leveraging Windows’ Inconsistent Access Control for LPE

JULY 27, 2026
[Vulnerability Analysis](https://blog.exodusintel.com/category/vulnerability-analysis/), [Exploit Techniques](https://blog.exodusintel.com/category/exploit-techniques/), [General Research](https://blog.exodusintel.com/category/general-research/)

*By Siddh Shah*

# Overview

This blog post describes exploiting two vulnerabilities patched in the Microsoft Windows December 2025 security updates. In the update, three CVEs were assigned to the vulnerable component, two of which, `CVE-2025-59517` and `CVE-2025-64673`, are covered in this post. Note that neither of these vulnerabilities were discovered by Exodus; we linked the CVEs to vulnerable functions based on the advisory provided by Microsoft. However, because all three CVEs address the same vulnerability class within the same driver and were patched in a single update, the advisory descriptions alone do not unambiguously map each CVE to a specific function. The attribution was established through reverse engineering of the patched binary, but it remains possible that the actual CVE-to-function assignment differs from what is presented here.

These two vulnerabilities, arising due to improper access control within the `storvsp.sys` kernel driver, can be chained together to escalate a low-privileged user to `NT AUTHORITY\SYSTEM` on the several affected versions of the Microsoft Windows Operating Systems.

**Disclaimer:** All structure and function definitions detailed in this post were deduced by reversing the `storvsp.sys` binary. Since source code is not available for this module, they may not accurately reflect Microsoft’s internal naming conventions.

# Background

This section provides an overview of the Virtual Server Message Block (vSMB) component and structures relevant to the vulnerability.

## Windows Virtual Server Message Block

The Microsoft Windows Storage Virtual Service Provider (VSP) driver (`storvsp.sys`) provides the *Virtual Server Message Block* (`vSMB`) functionality. It is a specialized, high-performance file-sharing mechanism used by Microsoft Windows to share files between the host operating system and virtualized environments running on the same machine (e.g., virtual machines, Windows Sandbox, containers, etc.).

A vSMB share represents a host filesystem path that has been exposed to a virtualized environment, allowing the guest to perform file operations on host files without relying on network-based file sharing protocols. For a broader understanding of the Windows Sandbox component the reader can refer to the [analysis](https://research.checkpoint.com/2021/playing-in-the-windows-sandbox/) by *Check Point Research* that shows how vSMB is leveraged to carry out file operations between the virtualized guest and the host system. This is not required to understand the vulnerability, but gives an example how vSMB is actually used by Windows internally.

The driver exposes a device object (`\Device\STORVSP`) with a symbolic link (`\GLOBAL??\STORVSP`), making it accessible from user-mode processes via the `\\.\STORVSP` path. When targeting a vSMB share, the path follows the format `\\.\STORVSP\VSMB\??\C:\path`, where the `\VSMB` prefix routes the request to vSMB-specific handling and the `??\C:\` segment is an NT object manager path that resolves to a drive letter and its specified directory.

The driver is only loaded when the `Virtual Machine Platform` Windows feature is enabled.

## vSMB Structures

The `storvsp.sys` kernel driver utilizes several internal structures: one to track persistent share state, and others to parse user-controlled input and output buffers during I/O control request processing. The following structures are relevant to the vulnerabilities described in this post.

### The VVSMB\_SHARE\_ROOT\_OBJECT Structure

The `VVSMB_SHARE_ROOT_OBJECT` structure serves as a persistent context for a vSMB file or directory share.
It is allocated when a handle is opened to a vSMB path and is retained in memory until no open device handles are associated with it.

```
typedef struct _VVSMB_SHARE_ROOT_OBJECT
{
  DWORD ObjectType;
  volatile DWORD State;
  EX_RUNDOWN_REF RundownProtect;
  BYTE IsInitialized;
  BYTE Padding01[7];
  PFILE_OBJECT BackingFileObject;
  HANDLE RootDirectoryHandle;
  BYTE HasAppendAccess;
  BYTE HasWriteAccess;
  BYTE HasReadAccess;
  BYTE Padding02[5];
  SECURITY_SUBJECT_CONTEXT SubjectContext;
  BYTE IsActive;
  BYTE Reserved_51[3];
  SECURITY_QUALITY_OF_SERVICE SecurityQoS;
  PVOID UnknownPtr;
  BYTE Reserved_68[16];
  DWORD FileSystemAttributes;
  DWORD ReservedEnd;
} VVSMB_SHARE_ROOT_OBJECT, PVSMB_SHARE_ROOT_OBJECT*;
```

### The VSTOR\_VSMB\_SET\_INFORMATION\_FILE\_REQUEST Structure

The `VSTOR_VSMB_SET_INFORMATION_FILE_REQUEST` structure is the input buffer format expected by I/O control requests with code 0x240330. The structure defines file information operations such as renaming or linking files.

```
typedef struct _VSTOR_VSMB_SET_INFORMATION_FILE_REQUEST {
    DWORD Version;
    DWORD Reserved04;
    UINT64 SourceHandle;
    DWORD InformationClass;
    DWORD BufferLength;
    BYTE Buffer[1];
} VSTOR_VSMB_SET_INFORMATION_FILE_REQUEST, *PVSTOR_VSMB_SET_INFORMATION_FILE_REQUEST;
```

# Vulnerability

The first primitive, assigned CVE-2025-59517, lies in the `VspVsmbFileCreate()` function of `storvsp.sys`. When a low-privileged attacker calls the `CreateFileW()` Windows API with a vSMB share path as its target, `VspVsmbFileCreate()` is invoked to open a handle to the underlying filesystem path. The function correctly impersonates the calling thread before opening the file, but fails to pass necessary flags to the `IoCreateFileEx()` kernel function that enforces access checks. Consequently, the Windows Object Manager bypasses NTFS ACL checks and opens the target path with kernel privileges, ignoring the impersonation token.

A low-privileged user can exploit this vulnerability to obtain a vSMB share handle to any directory on the system, such as `C:\Windows\System32`, with read, write, and deletion access rights. The granted access rights are stored as boolean flags in the `VVSMB_SHARE_ROOT_OBJECT`kernel object, including `HasWriteAccess`, which tracks whether the handle was opened with write permissions. A privileged vSMB share handle by itself isn’t as useful, but a second primitive can be chained with it to modify the actual on-disk files and directories.

The second vulnerability, assigned CVE-2025-64673, resides in the `VspVsmbHandleSetInformationFileRequest()` function, invoked when an I/O control request with the code `0x240330` is issued on an existing vSMB share handle, such as the one obtained above. This function processes file information operations based on the input buffer of type `_VSTOR_VSMB_SET_INFORMATION_FILE_REQUEST`. Its security behavior is governed by the `HasWriteAccess` flag on the share’s `VVSMB_SHARE_ROOT_OBJECT` context. If the share handle was opened with write permissions, the function impersonate...