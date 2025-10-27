---
title: Advanced UEFI Analysis with Binary Ninja
url: https://binary.ninja/2024/08/23/uefi-firmware-analysis.html
source: Binary Ninja
date: 2024-08-24
fetch_date: 2025-10-06T18:04:51.245483
---

# Advanced UEFI Analysis with Binary Ninja

[![](/images/binary-ninja-logo.svg)](/)

* [Features](/features/)
* [Enterprise](/enterprise/)
* [Sidekick](https://sidekick.binary.ninja)
* [Cloud](https://cloud.binary.ninja)
* [Training](/training/)
* [Support](/support/)

  [Extended Support](/support/extended.html)
  [Documentation](/support/#documentation)
  [License/Installer Recovery](/recover/)
  [Renew Current License](/renew/)
  [Slack Signup](https://slack.binary.ninja/)
  [FAQ](/faq/)
  [Sponsorship Information](/sponsorship/)
  [Portal](https://portal.binary.ninja/)
  [Contact Us](/support/)
* [Blog](/blog/)
* [Gear](https://shop.binary.ninja)

[Free](/free)
[Purchase](/purchase)

Participate in our [Reverse Engineering Survey](/survey/) to win free licenses or admission to [RE//verse](https://re-verse.io/)!

# Binary Ninja Blog

## Advanced UEFI Analysis with Binary Ninja

* [Brandon Miller](https://github.com/zznop)
* [Zichuan Li](https://github.com/river-li)
* 2024-08-23
* [reversing](/tag/reversing), [meta](/tag/meta)

The Unified Extensible Firmware Interface (UEFI) is a specification that defines the architecture of firmware used for
booting computers. It contains the initial code that runs on most modern PCs and mobile devices, operating at the
highest privilege levels before the operating system loads. This makes UEFI a fascinating area for reverse engineering.

Letâs delve into some firmware samples and demonstrate how Binary Ninja and our official EFI Resolver plugin can
automate the analysis of UEFI binaries. The features highlighted in this blog post represent a culmination of efforts
that began prior to the release of Binary Ninja 3.5. This ongoing work includes recent contributions by Zichuan, one of
our summer interns!

## Brief Overview of UEFI

UEFI was designed to replace the Basic Input/Output System (BIOS) and is now widely adopted by leading vendors such as
Intel, Apple, and Google for booting operating systems like Windows, Linux, and macOS. This section offers a brief
overview of UEFI design; however, for a complete understanding, we recommend you review the full 2205-page [UEFI
specification](https://uefi.org/sites/default/files/resources/UEFI_Spec_2_10_A_July_16.pdf) before you proceed. Donât
worry, this blog will still be here in a few weeks when youâre finished.

### UEFI Phases

UEFI firmware consists of (7) primary phases:

* **Security Phase (SEC)** - This phase is regarded as the software root-of-trust (RoT) on systems that boot UEFI.
  However, many systems use hardware-based RoT mechanisms, such as Intel BootGuard, to verify SEC and PEI. SEC execution
  often starts at the reset vector, directly from Flash. It sets up initial memory and is also responsible for the
  initial handling of sleep states. SEC can also verify PEI, prior to handing off execution.
* **Pre-EFI Initialization (PEI)** - This phase is responsible for initializing the system hardware (chipset, RAM,
  etc.). Like SEC, PEI code often runs directly from Flash in a resource-constrained environment. During PEI, PEI
  modules (PEIM) are discovered and dispatched by the PEI Foundation. PEI modules interact with the system hardware,
  install PEIM-to-PEIM interfaces (PPI) to share functionality, and prepare the system for the DXE phase.
* **Driver Execution Environment (DXE)** - This phase is where the majority of the system initialization is performed.
  The DXE Dispatcher is responsible for finding and loading DXE modules in the correct order. The DXE drivers provide
  services for console and boot devices. DXE works together with Boot Device Selection (BDS) to boot the operating
  system.
* **Boot Device Selection (BDS)** - This phase is responsible for identifying and selecting the boot device and
  enforcing the platform boot policy.
* **Transient System Load (TSL)** - This phase is often where the boot loader runs and terminates UEFI boot services.
  However, some systems skip this phase and the operating system terminates boot services.
* **Runtime (RT)** - This phase is where UEFI hands off execution to the operating system. The UEFI runtime services
  remain available to support the operating system. Runtime services trap System Management Interrupts (SMI) as the
  operating system attempts to interact with OEM hardware in System Management Mode (SMM).
* **After Life (AL)** - Nobody knows what happens in the after lifeâ¦

![UEFI Phases](/blog/images/uefi/boot-phases.png)

(Image from [Tianocore documentation](https://github.com/tianocore/tianocore.github.io/wiki/PI-Boot-Flow))

### Firmware File System (FFS)

UEFI binaries are bundled in a container format known as the Firmware File System (FFS). FFS consists of many components
and layers including volumes, files and sections. Within FFS file sections reside the interesting binaries such as
Pre-EFI Initialization (PEI) modules and Driver Execution Environment (DXE) modules. There are many tools that can be
used to parse FFS files and extract UEFI binaries. The most commonly used tool is
[UEFITool](https://github.com/LongSoft/UEFITool) though of course weâre partial to [EFI Inspector](https://github.com/zznop/efi-inspector),
an unofficial Binary Ninja plugin.

![EFI Inspector](/blog/images/uefi/efi-inspector.png)

### UEFI Binary File Formats

UEFI PEI and DXE modules are most commonly in either Portable Executable (PE) or Terse Executable (TE) format. Binary
Ninja has supported the PE file format since its inception. The TE format is designed to reduce the overhead of the
PE/COFF headers in PE images. This allows for smaller file sizes for PEI modules that run early in boot and must reside
in Flash (uncompressed). TE files are nothing more than modified PE files. The toolchains that create TE files first
emit a PE. Then they strip the PE/COFF headers and replace them with a smaller TE header. With the release of Binary
Ninja 4.1, we added a BinaryView for loading Terse Executables. Like all of our other BinaryViews, the [TE
View](https://github.com/Vector35/binaryninja-api/blob/dev/view/pe/teview.cpp) is open source!

![TE View](/blog/images/uefi/te-view.png)

### UEFI Protocols

To modularize UEFI firmware, the UEFI specification introduces protocols and services. UEFI services provide system-wide
functionality for accessing NVRAM variables, locating and registering protocol interfaces and more. UEFI protocols are
interfaces that are registered for use by external modules and drivers. These interfaces include PEIM-to-PEIM interfaces
(PPI), DXE protocol interfaces, SMM protocol interfaces and more. UEFI protocols are registered with PEI and boot
services using a 16-byte globally unique identifier (GUID) by calling functions such as `InstallProtocolInterface`,
which is provided by EFI boot services and Management Mode (MM) System Table. PEI modules use `InstallPpi`, which is
provided by PEI services. Other functions can register multiple protocols, and other APIs query the pointer to protocol
interfaces (`LocateProtocol`, `LocatePpi`, etc.).

## Binary Ninja EFI Platforms and Types

Native EFI platforms have been implemented in Binary Ninja for UEFI module analysis. Binary Ninja platforms have the
ability to auto-recognize the platform from file format metadata, define supported calling conventions and populate the
binary view with platform types on load of the binary. UEFI platforms for x86, x86-64, AArch64, ARMv7 and Thumb-2 were
introduced in Binary Ninja 3.5. With the addition of new EFI platforms, Binary Ninja will automatically recognize UEFI
modules on load.

Platform types have also been added to Binary Ninja for EFI platforms. The first set of EFI types was added to Binary
Ninja 3.5 and included core EFI types as well as types associated with EFI runtime services, boot services and DXE
protocols. Binary Ninja 4.1 introduced types for System Management Mode (SMM), PEI services and PEIM-to-PEIM Protocol
Interfaces (PPI). These types can be explored in the Binary Ninja type browser after loading a binary for an EFI
pl...