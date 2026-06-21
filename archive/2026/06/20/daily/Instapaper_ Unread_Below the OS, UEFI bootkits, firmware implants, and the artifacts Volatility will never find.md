---
title: Below the OS, UEFI bootkits, firmware implants, and the artifacts Volatility will never find
url: https://andreafortuna.org/2026/06/12/uefi-bootkits/
source: Instapaper: Unread
date: 2026-06-20
fetch_date: 2026-06-21T06:50:18.384874
---

# Below the OS, UEFI bootkits, firmware implants, and the artifacts Volatility will never find

[Andrea Fortuna](/)
[ ]

[About](/about/)[Search](/search/)

Tools

[DFIR Toolkit](https://dfir-toolkit.andreafortuna.org)
[OSINT Toolkit](https://osint-toolkit.andreafortuna.org)

# Below the OS, UEFI bootkits, firmware implants, and the artifacts Volatility will never find

Jun 12, 2026

by [Andrea Fortuna](/about/)

The investigation was going well until it stopped making sense. The malware had been removed, the infected system reimaged, the hard drive replaced just to be safe. Two weeks later, the same indicators reappeared on the same machine. It was neither a network reinfection nor a backup restore gone wrong. The machine itself was still compromised, at a layer nobody had checked, in storage that survives disk replacement just as stubbornly.

![cover](/assets/2026/uefi-firmware-forensics.jpg)

This is the scenario that firmware implants and UEFI bootkits are built for: persistence so deep that the normal DFIR playbook of acquiring the disk, imaging the memory, analyzing, remediating, and reimaging simply does not reach it. It is not a new problem. The first UEFI rootkit documented in the wild appeared in 2018. What has changed is that the technique has moved from nation-state novelty to something approaching a tradecraft standard, and the forensic community’s response has not quite kept up.

## In brief

* UEFI bootkits and firmware implants persist below the operating system, in EFI System Partition boot components or in SPI flash memory on the motherboard itself.
* Known implants include **BlackLotus** (EFI bootkit, bypasses Secure Boot on patched Windows 11), **CosmicStrand** and **MosaicRegressor** (firmware-resident, survives disk replacement), and **FinSpy** bootkit (commercial spyware with pre-OS component).
* Standard DFIR tools (Volatility, disk imaging, EDR agents) are structurally blind to firmware-layer persistence.
* Detection requires a different toolkit: **CHIPSEC** for SPI flash analysis, **UEFITool** for EFI binary inspection, boot log analysis, and PCR value attestation via TPM.
* Remediation is non-trivial: EFI-resident implants may require ESP cleaning and Secure Boot re-enrollment; firmware implants may require a full BIOS reflash or, in extreme cases, hardware replacement.
* Forensic readiness for this threat class requires pre-incident baselines of firmware hashes and PCR values, artifacts you cannot reconstruct after the fact.

## The firmware layer and why it matters

Before cataloging what is exploitable, it helps to be precise about the architecture. **UEFI** (Unified Extensible Firmware Interface) replaced legacy BIOS on mainstream hardware from around 2010 onward. It is a complete pre-OS environment with its own networking stack, drivers, a file system (the EFI System Partition, or ESP), and a shell. It runs before any operating system component loads, which means anything it executes inherits an environment where no EDR agent, no AV engine, and no kernel patch guard exist yet.

The boot sequence on a modern UEFI system proceeds roughly like this: UEFI firmware (stored in SPI flash on the motherboard) initializes hardware, reads the ESP on the boot disk, loads the boot manager (`\EFI\Microsoft\Boot\bootmgfw.efi` on Windows), which in turn loads the OS loader, which loads the kernel. A bootkit can insert itself at any stage of this chain. The two most relevant levels for practical forensics are:

* **ESP-resident**: the implant lives on the EFI System Partition as a modified or additional EFI binary. It persists across OS reinstalls if the ESP is not explicitly wiped, and it can survive drive imaging if the ESP is not included in the acquisition scope.
* **Firmware-resident**: the implant is written directly to SPI flash on the motherboard. It persists across disk replacement, OS reinstall, and every other remediation step short of physically reflashing the chip.

The distinction matters for both detection and remediation. What these two classes have in common is that they are structurally invisible to anything that runs after the firmware has already executed, which includes every tool in a conventional DFIR toolkit.

## ESP and firmware implants at a glance

| Dimension | ESP-resident implant | Firmware-resident implant |
| --- | --- | --- |
| Persistence scope | Survives OS reinstall if ESP is not wiped | Survives OS reinstall and disk replacement |
| Typical storage location | EFI System Partition (FAT32) | SPI flash on motherboard |
| Typical artifacts | Unexpected EFI binaries, modified boot files, anomalous ESP paths | Modified DXE modules, altered firmware volumes, SPI write-protection anomalies |
| Visibility from endpoint tools | Low, usually visible only with targeted ESP acquisition | Very low, usually invisible to OS-level telemetry |
| Detection approach | ESP imaging, hash/signature checks, Secure Boot and DBX validation | CHIPSEC checks, SPI dump diff against baseline, firmware module analysis |
| Remediation complexity | Medium: clean ESP and rebuild trusted boot chain | High: reflash, verify integrity, and in some cases replace hardware |

## Known implants in the wild

The forensic understanding of UEFI-level threats is not theoretical. Several real-world implants have been analyzed in enough detail to guide forensic work.

**BlackLotus** is the most significant recent case, first publicly documented by [ESET in March 2023](https://www.welivesecurity.com/en/eset-research/blacklotus-uefi-bootkit-analysis/). It is a UEFI bootkit sold as a crimeware product (not exclusively nation-state) that can bypass Secure Boot on fully patched Windows 11 systems by exploiting a vulnerability in the Windows Boot Manager (CVE-2022-21894, also known as **Baton Drop**). BlackLotus installs a malicious EFI binary to the ESP, disables kernel protections including HVCI and Windows Defender, and deploys a kernel driver and a user-mode HTTP downloader. Even after Microsoft patched the underlying boot manager vulnerability, systems with a valid but vulnerable bootloader version still installed in their Secure Boot database remained exploitable, because the Secure Boot revocation list (the UEFI Forbidden Signature Database, or DBX) was not automatically updated.

The forensic artifacts of a BlackLotus infection on the ESP are reasonably concrete:

```
\EFI\Microsoft\Boot
├── bootmgfw.efi   # legitimate, but may be replaced
├── grubx64.efi    # BlackLotus drops this as its loader
├── winload.efi    # may be patched
└── system32\drivers
  └── [randomized].sys   # kernel driver
```

ESET documented the directory `\EFI\Microsoft\Boot\system32\` as a BlackLotus artifact on the ESP, a path that has no legitimate reason to exist in a standard Windows installation.

**CosmicStrand** is an order of magnitude more serious. [Kaspersky’s analysis](https://securelist.com/cosmicstrand-uefi-firmware-rootkit/106973/) published in 2022 describes a UEFI firmware rootkit attributed to a Chinese-speaking threat actor, found embedded in the firmware images of consumer-grade ASUS and Gigabyte motherboards. CosmicStrand hooks the CSMCORE DXE driver (a UEFI component) to intercept the Windows boot process, injects a shellcode kernel patch, and ultimately deploys a user-mode agent, all before Windows has loaded a single driver. From the OS’s perspective, the system looks clean. The implant is in the SPI flash chip soldered to the motherboard.

**MosaicRegressor** (attributed to APT41, documented by [Kaspersky in 2020](https://securelist.com/mosaicregressor-lurking-in-the-shadows-of-uefi/98017/)) used a modified version of the leaked **Hacking Team UEFI implant** source code, embedded in the UEFI firmware of victim laptops. It was found on systems used by organizations connected to North Korea-focused research. The infection vector involved physical access or supply-chain compromise. The implant drops a downloader component during the boot process.

**MoonBounce** ([Kaspersky, 2022](https://securelist.com/moonbounce-the-dark-side-of-uefi-firmwar...