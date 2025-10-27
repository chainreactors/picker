---
title: Secure Enclaves for Offensive Operations (Part I)
url: https://www.outflank.nl/blog/2025/02/03/secure-enclaves-for-offensive-operations-part-i/
source: Publications | Outflank
date: 2025-02-04
fetch_date: 2025-10-06T20:35:39.026401
---

# Secure Enclaves for Offensive Operations (Part I)

[Skip to the content](#content)

[logo](https://www.outflank.nl)
Experts in red teaming

* [Red Team Tools](/products/)
  + [Outflank Security Tooling](/products/outflank-security-tooling/)
    - [Outflank C2](https://www.outflank.nl/products/outflank-security-tooling/outflank-c2/)
    - [Payload Generator](/products/outflank-security-tooling/pe-payload-generator/)
    - [Tooling](/products/outflank-security-tooling/ost-tool-list/)
    - [Tradecraft](/products/outflank-security-tooling/tradecraft/)
    - [Demo Videos](/videos/ost-demo-videos/)
  + [Cobalt Strike](/products/cobalt-strike/)
  + [Red Team Bundle](/datasheets/red-team-bundle/)
  + [Advanced Red Team Bundle](/datasheets/advanced-red-team-bundle/)
* [Red Team Services](/services/red-teaming/)
* Blog & Resources
  + [Outflank Blog](/blog/)
  + [Community](/products/outflank-security-tooling/ost-community/)
  + [Datasheets](/datasheets/)
  + [OST Demo Videos](/videos/ost-demo-videos/)
  + [OST Releases](/services/outflank-security-tooling/releases/)
  + [Upcoming Events](https://www.outflank.nl/upcoming-events/)
* [About Us](/company/)
  + [Our Company](/company/)
  + [OST Testimonials](/company/outflank-security-tooling-testimonials/)
  + [Contact Us](/contact/)
* [Schedule a Demo](/demo-request/)
* [REQUEST QUOTEREQUEST QUOTE](/request-a-quote/)

# Publications

# [Secure Enclaves for Offensive Operations (Part I)](https://www.outflank.nl/blog/2025/02/03/secure-enclaves-for-offensive-operations-part-i/ "Secure Enclaves for Offensive Operations (Part I)")

[Cedric Van Bockhaven](https://www.outflank.nl/blog/author/cedric/ "Posts by Cedric Van Bockhaven")
 |
February 3, 2025

*This blog post was co-authored by Matteo Malvica (*Researcher at OffSec** and *External OST developer) and [Cedric Van Bockhaven](https://www.outflank.nl/company/cedric-van-bockhaven/) (OST developer and researcher at Outflank).*

This article is the first in a two-part series in which we investigate the anatomy of Virtualization-Based Security (VBS) enclaves, their internals, and the unique ways they could be leveraged for offensive operations on Windows systems.

Enclaves provide a software-based Trusted Execution Environment (TEE) and are isolated memory regions. Only code that runs within the enclave can access data within the same enclave. TEEs protect sensitive operations in computing and are designed to keep unauthorized actors away from confidential information, whether that actor is malware with user-mode or kernel-mode access or even someone with physical access to the data center.

You can imagine that being able to hide away data and code into an enclave is a powerful capability and could also be used for offensive purposes, and that’s exactly what this series will explore. Note that using enclaves for offensive operations is not new. The concept has been presented before at [DEF CON 29 by Dimity ‘Op Nomad’ Snezhkov in their talk, “Use Of Offensive Enclaves in Adversarial Operations”](https://www.youtube.com/watch?v=WWGkaGBtn2Q). Their talk was focused on the use of Intel SGX enclaves. With Intel deprecating SGX technology for workstations in 2021, we will be investigating the use of VBS enclaves instead.

This blog series will not address vulnerabilities in the architecture or implementation of the Secure Kernel that is used by VBS enclaves. However, there is a great presentation on this topic: [BlackHat USA 2020 by Saar Amar and Daniel King on “Breaking VSM by Attacking Secure Kernel”](https://i.blackhat.com/USA-20/Thursday/us-20-Amar-Breaking-VSM-By-Attacking-SecureKernal.pdf). Instead, we will focus on the practical use of VBS enclaves.

**From an offensive perspective, the appeal of enclaves lies in their ability to securely store (and process) data, creating an opportunity for attackers to embed malicious data or logic in areas where defenders are unlikely to look – or are unable to look at all.**

For red team engagements, we could see enclaves as a vector for slipping malicious code into a secure region to gain a foothold that is harder for EDR solutions to inspect. Even EDRs with kernel access cannot inspect VBS enclaves that are running in isolated user mode.

Let us preface by saying that functionality of VBS enclaves is restricted – you are able to operate on data but won’t have regular Windows APIs available within the enclave to set up TCP sockets or even open files on the file system.

## Virtualization-Based Security and Enclaves

In short: VBS enclaves provide a software-based TEE and were added as an extension to isolated user mode in the VBS environment.

[VBS](https://learn.microsoft.com/en-us/windows-hardware/design/device-experiences/oem-vbs) utilizes the Hyper-V hypervisor to create isolated environments. Like VM isolation, the hypervisor sets memory protections to isolate this environment from the rest of the system kernel via SLAT (second-level address translation).

VBS is the technology that enables Credential Guard to protect credentials by storing them in isolated memory. [Microsoft extended](https://techcommunity.microsoft.com/blog/windowsosplatform/securely-design-your-applications-and-protect-your-sensitive-data-with-vbs-encla/4179543) the isolated user mode in the VBS environment to allow developers to protect portions of application data in a software-based TEE known as a VBS enclave. A basic premise of TEEs is that code and data residing within these isolated pockets of memory are protected from the rest of the system.

In hardware-backed TEEs like [Intel SGX](https://www.intel.com/content/www/us/en/architecture-and-technology/software-guard-extensions.html), the CPU enforces these privileges.  In software-based TEEs like Microsoft’s [VBS Enclaves](https://learn.microsoft.com/en-us/windows/win32/trusted-execution/vbs-enclaves), the Secure Kernel (running in a separate virtualization stack) takes responsibility for ensuring that no process or even the Windows OS kernel can tamper with enclave-protected memory.

Virtualization is used to enforce isolation. This protective boundary is typically enforced using page-table manipulations and heavily restricted APIs to load and run enclave modules.

If you’ve worked with Intel SGX, you know that enclaves introduce some complexities in [development and debugging](https://cdrdv2-public.intel.com/671079/debugging-intel-sgx-enclaves-in-windows.pdf), including limitations on standard memory inspection tools.

Microsoft’s VBS enclaves, although more flexible than hardware enclaves, share a similar level of opacity and bring in additional challenges like production-signing your enclave.

The architectural design of VBS enclaves allows the protection of secrets, intellectual property, or secret operations inside the enclave.Here are two examples of how VBS enclaves are currently used by Microsoft:

* Enhanced Phishing Protection in Microsoft Defender SmartScreen makes use of secure enclaves. This mechanism records keystrokes and clipboard data to check whether you enter your password in untrusted resources. For this, your password is intercepted at login and stored in hashed format in an enclave ([SFAPE.dll](https://github.com/EvanMcBroom/lsa-whisperer/wiki/sfapm#secret-filter-ap)).
* SQL Server 2019+ and Azure SQL Database can make use of secure enclaves through its [Always Encrypted](https://learn.microsoft.com/en-us/sql/relational-databases/security/encryption/always-encrypted-enclaves) feature.

As enclaves can provide a secure processing environment, they could also make a good fit for DRM processing or [anti-cheat purposes](https://tulach.cc/using-vbs-enclaves-for-anti-cheat-purposes/).

## Anatomy and Operations

VBS enclaves operate within a multi-layered architecture that enforces strict isolation using Virtual Trust Levels (VTLs). These levels allow the separation of standard user-mode processes (VTL0) and isolated secure environments (VTL1) managed by the Secure Kernel.

The diagram below illustrates how this architecture is ...