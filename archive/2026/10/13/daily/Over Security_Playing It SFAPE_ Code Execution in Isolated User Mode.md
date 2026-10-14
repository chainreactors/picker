---
title: Playing It SFAPE: Code Execution in Isolated User Mode
url: https://blog.doyensec.com/2026/10/13/Sfape.html
source: Over Security
date: 2026-10-13
fetch_date: 2026-10-14T06:53:11.091559
---

# Playing It SFAPE: Code Execution in Isolated User Mode

[

](https://doyensec.com/img/home-video.mp4)

[![](/public/images/doyensec-logo.svg)](/index.html)

[![](/public/images/logo.svg)](/index.html)

#### ABOUT US

We are [**security engineers**](https://doyensec.com) who break bits and tell stories.

Visit us
[doyensec.com](https://doyensec.com)

Follow us
[@doyensec](https://twitter.com/doyensec)

Engage us
info@doyensec.com

#### Blog Archive

* 2026
* 2025
* 2024
* 2023
* 2022
* 2021
* 2020
* 2019
* 2018
* 2017

© 2026 [Doyensec LLC](https://doyensec.com) [![](/public/images/rss.png)](/atom.xml "RSS")

# Playing It SFAPE: Code Execution in Isolated User Mode

13 Oct 2026 - Posted by Adrian Denkiewicz

It is tempting to think of Windows in terms of a simple model: user mode and kernel mode. If a bug lets a user-mode process gain control of the kernel, itâs game over.

Well, for a long time it used to be like that. Protected processes, SMEP, PatchGuard and other mitigations surely raised the bar, but it was [Virtualization-Based Security](https://learn.microsoft.com/en-us/windows-hardware/design/device-experiences/oem-vbs) that added another dimension to that model and made the whole design a lot more complex. Some code does not merely cross from user mode to kernel mode. It crosses into another Virtual Trust Level (VTL), where the normal kernel is no longer the most trusted component in the system. From a VTL0 perspective, the call may look like it disappears into a region whose private memory cannot be inspected even with kernel privileges.

VBS uses the Windows hypervisor to split the system into Virtual Trust Levels. This separation is orthogonal to the user-mode/kernel-mode distinction. On x64, both VTLs can contain ring 3 and ring 0 code. In the VTL1 world, we are talking about Isolated User Mode (IUM) and the Secure Kernel (SK), respectively.

This part of Windows has existed for years now, primarily to support really powerful features such as Hypervisor-Protected Code Integrity and Credential Guard. However, until recently, VTL1 was also pretty exclusive to Microsoftâs code. We are not aware of any third-party trustlets. Technically, a trustlet is just yet another PE file with a special policy, metadata and a signature. Yet, the signature part is a problem - Microsoft simply doesnât offer a way to properly sign custom trustlets.

Things changed when Microsoft [introduced support for third-party VBS enclaves](https://techcommunity.microsoft.com/blog/windowsosplatform/securely-design-your-applications-and-protect-your-sensitive-data-with-vbs-encla/4179543). These are custom libraries loaded by a normal VTL0 process but running within an isolated address space in VTL1. The host process controls when the library is loaded and which exports are called, but it cannot directly read or write the enclaveâs private memory. Those libraries also require a special signature, but this time there is an official path to acquire one through Azure Artifact Signing (formerly Trusted Signing). Itâs still a rather picky process and maybe thatâs why we couldnât find any widely known third-party enclaves. On the other hand, several Windows components started relying on enclave DLLs for host attestation, data sealing, etc.

In this post, we examine security vulnerabilities in one of the VBS enclaves shipped with Windows. We will demonstrate how a simple primitive was used for a memory corruption attack that enabled multiple other primitives and effectively led to full control over the enclave instance. The ability to reuse existing VTL1 code makes it a powerful tool for experimenting with hidden parts of the operating system, exploring IUM, and potentially attacking Secure Kernel.

## VBS Enclaves

Letâs start by diving into the world of VBS enclaves.

A VBS enclave provides a small isolated execution unit. It belongs to an ordinary VTL0 host process, but its code executes in IUM and its private memory is protected from direct access by VTL0 code. Microsoft describes it as a software-based trusted execution environment. It does not require Intel SGX or an NPU. The only relevant hardware dependency is what VBS itself requires.

![Diagram of the VBS Enclaves trusted execution environment, src: https://learn.microsoft.com/en-us/windows/win32/trusted-execution/vbs-enclaves](../../../public/images/trusted-execution-enclaves-diagram.png)

From the applicationâs point of view, the enclave is a specially built DLL. The host creates, loads, initializes, and calls the enclave using the following simplified API sequence:

```
CreateEnclave
    -> LoadEnclaveImageW
        -> InitializeEnclave
            -> CallEnclave(export, one_parameter)
```

The host process creates an enclave allocation, loads one primary image (the main enclave DLL) and its approved dependencies, initializes the VTL1 threads, and invokes exported functions through [`CallEnclave`](https://learn.microsoft.com/en-us/windows/win32/api/enclaveapi/nf-enclaveapi-callenclave).

Secondary images provide the restricted runtime, low-level operating-system interfaces used inside the enclave, and some cryptography capabilities. The main dependency is `vertdll.dll`, which plays a role roughly analogous to `ntdll.dll` for enclave code. It contains the VTL1 call dispatcher, runtime helpers, and wrappers for Secure Kernel services. Other common secondary images include `ucrtbase_enclave.dll` and enclave-specific cryptographic libraries. The enclave API surface is very restricted: it does not directly expose file-system, networking, or cross-process communication APIs. Enclave code must delegate such operations to its VTL0 host through callouts. This significantly limits the attack surface from the enclave DLL context.

Even though an enclave DLL could potentially reject an unfamiliar host process, in practice, most of the analyzed enclaves do not do that. Therefore, a host process can perform all kinds of experiments on an enclave DLL and feed malicious input data to its exports.

One must remember that the host process running in VTL0 cannot simply access enclave memory. It must treat the enclave like a remote service and pass request structures through exported calls. The memory relationship is asymmetric. Unless restricted by an enclave policy, the enclave code can freely read and write memory belonging to its VTL0 host, just like a normal DLL would. Usually, the host process provides pointers and the enclave works on the data. This also means that an enclave receives data from a less trusted world and must check whether every pointer and nested buffer really points to the expected data. Mistakes can lead to time-of-check/time-of-use (TOCTOU) bugs: for example, a host-controlled structure may be modified after validation. A nested pointer may point at VTL1 data. Length arithmetic may wrap, and so on.

With that model in place, letâs look at earlier research on the offensive use of VBS enclaves.

## Bring Your Own Vulnerable Enclave

In 2023, Alex Gough of Googleâs Chrome Platform Security Team reported [CVE-2023-36880](https://github.com/google/security-research/security/advisories/GHSA-wwr4-v5mr-3x9w) in Edgeâs `prefs_enclave_x64.dll`. Its `SealSettings` and `UnsealSettings` exports accepted pointers without checking whether they referred to VTL0 or private enclave memory. Chaining the two operations provided arbitrary read and write primitives inside the enclave. That meant unrestricted access to VTL0 and VTL1 portions of the process memory. A later fix was insufficient and left a TOCTOU issue, reported separately as [CVE-2024-21423](https://github.com/google/security-research/security/advisories/GHSA-2phx-8mf9-fq24).

Even though the latest `prefs_enclave_x64.dll` version patched both vulnerabilities, ânothing is ever lost on the internetâ. Thanks to the VirusTotal file archive, the old vulnerable enclave is not lost either. For now, Windows does not expose a dedicated vulnerable-enclave blocklist comparable to the Microsoft Vulnerable...