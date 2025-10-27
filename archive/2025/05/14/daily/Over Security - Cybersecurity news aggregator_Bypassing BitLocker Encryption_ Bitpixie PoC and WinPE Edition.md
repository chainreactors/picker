---
title: Bypassing BitLocker Encryption: Bitpixie PoC and WinPE Edition
url: https://blog.compass-security.com/2025/05/bypassing-bitlocker-encryption-bitpixie-poc-and-winpe-edition/
source: Over Security - Cybersecurity news aggregator
date: 2025-05-14
fetch_date: 2025-10-06T22:30:55.097179
---

# Bypassing BitLocker Encryption: Bitpixie PoC and WinPE Edition

## [Compass Security Blog](https://blog.compass-security.com "Compass Security Blog — Offensive Defense")

### Offensive Defense

* [Home](https://blog.compass-security.com/)
* [Archive](https://blog.compass-security.com/archive/)
* [Contact](https://blog.compass-security.com/contact/)
* [Newsletter](https://blog.compass-security.com/mailing-list-tigerinfo/)

* [Home](https://blog.compass-security.com/)
* [Archive](https://blog.compass-security.com/archive/)
* [Contact](https://blog.compass-security.com/contact/)
* [Newsletter](https://blog.compass-security.com/mailing-list-tigerinfo/)

# [Bypassing BitLocker Encryption: Bitpixie PoC and WinPE Edition](https://blog.compass-security.com/2025/05/bypassing-bitlocker-encryption-bitpixie-poc-and-winpe-edition/ "Bypassing BitLocker Encryption: Bitpixie PoC and WinPE Edition")

[May 13, 2025](https://blog.compass-security.com/2025/05/bypassing-bitlocker-encryption-bitpixie-poc-and-winpe-edition/ "Bypassing BitLocker Encryption: Bitpixie PoC and WinPE Edition")
 /
[Marc Tanner](https://blog.compass-security.com/author/mtanner/ "Posts by Marc Tanner")
 /
[1 Comment](https://blog.compass-security.com/2025/05/bypassing-bitlocker-encryption-bitpixie-poc-and-winpe-edition/#comments)

Depending on the customer’s preference, possible initial access vectors in our [red teaming exercises](https://www.compass-security.com/en/services/red-teaming) typically include deployment of dropboxes, [(device code) phishing](https://blog.compass-security.com/2024/01/device-code-phishing-add-your-own-sign-in-methods-on-entra-id/) or a stolen portable device. The latter is usually a Windows laptop protected by BitLocker for full disk encryption without pre-boot authentication i.e. without a configured PIN or an additional key file.

While hardware-based [TPM sniffing attacks](https://pulsesecurity.co.nz/articles/TPM-sniffing) are well known and covered in [public courses](https://hands-on-security.com/#trainings), they typically involve hunting down board schematics on Chinese websites and some prowess using a soldering iron. Physical craftsmanship is definitely not a strength of mine, which is why I was particularly interested when Thomas demonstrated a concrete software-only attack in his [38C3 talk: Windows BitLocker: Screwed without a Screwdriver](https://events.ccc.de/congress/2024/hub/en/event/windows-bitlocker-screwed-without-a-screwdriver/).

Even compared to other [software attacks](https://github.com/Wack0/bitlocker-attacks#software-attacks) such as the [“push button decrypt”](https://blog.scrt.ch/2023/08/14/cve-2022-41099-analysis-of-a-bitlocker-drive-encryption-bypass/), the exploitation of the abused bitpixie vulnerability is non-invasive, does not require any permanent device modifications and no complete disk image, thereby allowing a fast (~5 minutes) compromise and more flexible integration in certain social engineering scenarios.

## Bitpixie Linux Edition

While Thomas did release a [detailed blog post](https://neodyme.io/en/blog/bitlocker_screwed_without_a_screwdriver/), the concrete exploit code was not disclosed. To fully understand the attack, reproduce the original research, and demonstrate the concrete impact to our customers, I set out to develop a public proof of concept.

[![Bitpixie attack flow](https://blog.compass-security.com/wp-content/uploads/2025/03/image-18-459x1024.png)](https://blog.compass-security.com/wp-content/uploads/2025/03/image-18.png)

The Linux-based exploitation strategy roughly depicted on the above diagram (from Thomas’ presentation) is to:

1. Enter the Windows Recovery Environment by using *Shift+Reboot* from the power menu of the login screen
2. Downgrade to vulnerable Windows Boot Manager (`bootmgfw.efi`) via PXE boot
3. Specify broken default Boot Configuration Data (BCD) to force a `pxesoftreboot` fallback
4. PXE boot into signed Linux shim loader (`shimx64.efi`)
5. Load signed GRUB (`grubx64.efi`) boot loader
6. Load signed Linux kernel and initial ram filesystem
7. [Exploit Linux kernel lockdown mode](https://github.com/martanne/CVE-2024-1086-Bitpixie) to scan physical memory for BitLocker Volume Master Key (VMK)
8. Mount encrypted volume using the [dislocker FUSE driver](https://github.com/Aorimn/dislocker) and the extracted VMK

This video shows a full rundown of this technique:

[](https://blog.compass-security.com/wp-content/uploads/2025/04/bitpixie-linux.webm)

## Bitpixie WinPE Edition

As Thomas describes in his [second blog post](https://neodyme.io/en/blog/bitlocker_why_no_fix/#secure-boot---how-does-it-even-work) discussing possible remediation strategies, Microsoft uses different UEFI certificates to sign boot components based on their origin:

* *Microsoft 1st party certificate*, signs all Windows bootloaders
* *Microsoft 3rd party certificate*, signs everything else commonly understood to boot under Secure Boot, such as Linux shims

Vendors such as [Lenovo with their *secured-core* PCs](https://download.lenovo.com/pccbbs/mobiles_pdf/Enable_Secure_Boot_for_Linux_Secured-core_PCs.pdf) disable the latter by default.

[![UEFI Secure Boot Settings](https://blog.compass-security.com/wp-content/uploads/2025/03/image-51-1024x572.png)](https://blog.compass-security.com/wp-content/uploads/2025/03/image-51.png)

As a result, the above attack chain fails at step 4 because the third-party signing certificate used is not trusted. However, there is nothing conceptually stopping an attack flow where third-party signed components are replaced by their Windows native equivalents:

4. Boot into same Windows Boot Manager (`bootmgfw.efi`) a second time via PXE boot, but specify different BCD
5. Load a WinPE based boot image (`boot.wim`) and corresponding ram disk (`boot.sdi`)
6. Load signed Windows boot loader (`winload.efi`)
7. Load signed Windows Kernel (`ntoskrnl.exe`)
8. Scan physical memory for a VMK using a modified version of WinPmem which internally uses a signed driver (`winpmem_x64.sys`)
9. Use VMK to decrypt encrypted recovery password stored in BitLocker meta data
10. Use human-readable recovery password to unlock the encrypted volume

The second stage BCD used in step 4. is constructed according to the [official Microsoft documentation](https://learn.microsoft.com/en-us/windows/deployment/configure-a-pxe-server-to-load-windows-pe). Physical memory is scanned by incorporating the original pattern-matching code into a [modified version of WinPmem](https://github.com/martanne/WinPmem-BitLocker) (`winpmem.exe`). The [recovery of the human-readable recovery password](https://github.com/Aorimn/dislocker/issues/294#issuecomment-1299249928) is implemented in a [minimal Windows port of the dislocker-metadata utility](https://github.com/martanne/dislocker-metadata-win32) (`dislocker-metadata.exe`).

As presented, the WindowsPE-based attack flow uses only core components signed by Microsoft. At least in theory, it should therefore be applicable to all affected devices, as long as they trust the *Microsoft Windows Production PCA 2011* certificate used to sign the vulnerable boot manager. In practice, it seems to be somewhat less reliable than its Linux-based counter part. Nonetheless, the [provided automation scripts](https://github.com/martanne/bitpixie) are hopefully useful in case you want to investigate whether your devices are affected.

The following video demonstrates a successful exploitation attempt on the same device using the WinPE approach:

[](https://blog.compass-security.com/wp-content/uploads/2025/05/bitpixie-winpe.webm)

## Remediation

The Bitpixie vulnerability – and more generally both hardware and software-based attacks – can be [mitigated](https://neodyme.io/en/blog/bitlocker_screwed_without_a_screwdriver/#mitigation) by forcing pre-boot authentication, i.e., requiring an additional PIN and/or key file.

[Forensic](https://blog.compass-security.com/category/forensic/), [Red Teaming](https://blog.compass-security.com/category/red-teaming/)

[bitlocker](https:...