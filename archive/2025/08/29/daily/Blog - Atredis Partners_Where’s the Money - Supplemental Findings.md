---
title: Where’s the Money - Supplemental Findings
url: https://www.atredis.com/blog/2025/8/26/24nrgne4dqbwjxyip7txn8ep6zj057
source: Blog - Atredis Partners
date: 2025-08-29
fetch_date: 2025-10-07T00:17:56.711279
---

# Where’s the Money - Supplemental Findings

[0](/cart)

[Skip to Content](#page)

[![Atredis Partners](//images.squarespace-cdn.com/content/v1/576323cfd482e984e113fe9c/1566943528908-J56DPCZRQ9SVG4TFPP27/WhiskeyBirdTextOverlayWhite.png?format=1500w)](/)

[About](/)

[Ownership](/ownership)

[Team](/team)

[Pentesting](/pentesting)

[Embedded](/embedded)

[OCP SAFE](/ocp-safe)

[Risk](/risk)

[Contact](/contact)

[Blog](/blog)

Open Menu
Close Menu

[![Atredis Partners](//images.squarespace-cdn.com/content/v1/576323cfd482e984e113fe9c/1566943528908-J56DPCZRQ9SVG4TFPP27/WhiskeyBirdTextOverlayWhite.png?format=1500w)](/)

[About](/)

[Ownership](/ownership)

[Team](/team)

[Pentesting](/pentesting)

[Embedded](/embedded)

[OCP SAFE](/ocp-safe)

[Risk](/risk)

[Contact](/contact)

[Blog](/blog)

Open Menu
Close Menu

[About](/)

[Ownership](/ownership)

[Team](/team)

[Pentesting](/pentesting)

[Embedded](/embedded)

[OCP SAFE](/ocp-safe)

[Risk](/risk)

[Contact](/contact)

[Blog](/blog)

# Where’s the Money - Supplemental Findings

Aug 28

Written By [Matt Burch](/blog?author=680bdf13ef244e65c37b4e41)

While creating the content for my DefCon 32 talk, [Where’s the Money: Defeating ATM Disk Encryption](https://media.defcon.org/DEF%20CON%2032/DEF%20CON%2032%20presentations/DEF%20CON%2032%20-%20Matt%20Burch%20-%20Where%E2%80%99s%20the%20Money%20-%20Defeating%20ATM%20Disk%20Encryption-white%20paper.pdf), I observed two additional vulnerabilities that had been overlooked in the heat of the research. These issues were reported to Diebold Nixdorf and later identified as low impact issues and, thus, did not receive additional patching. The impact of these issues vary across the different versions of Superschaf, the Linux architecture supporting the FDE module of Diebold Nixdorf’s Vynamic Security Suite (VSS), detailed in my white-paper. As of VSS v3.3.0 SR16, they are little more than information discovery tools but provide some additional insight to the remediation controls implemented by Diebold Nixdorf. In this article I plan to publicly disclose these additional details as supplemental content to my white-paper, linked above.

As a refresher, Diebold Nixdorf’s Vynamic Security Suite (VSS) employs the software solution [*CryptoPro Security Disk for BitLocker*](https://www.cpsd.at/), aka *CryptoPro*. This solution introduces an abstraction layer to the system through the addition of a small Linux partition aka Superschaf, located at the end of a GUID partition table. The purpose of this environment is to conduct file integrity checks to assert a known system state, performing a number cryptographic routines with a SHA256 index table. This index table is hardcoded into the EFI binary `Bootxsa.efi` and contains a SHA sum for a number of files, within the Linux partition, that should be validated to assert system integrity. These sum values are represented as a double hash, where the SHA256 sum of the target file is generated and then that value is summed again. Additionally, this software solution is designed to work with or without a TPM and supports TPMs of version 1.1, 1.2, and 2.0.

Once CryptoPro is installed, the system will operate in a dual-boot state, switching between Linux and Windows. Each boot sequence will run through both operating systems before the ATM becomes fully operational. In this architecture, system integrity validation is done between UEFI and Linux - this process is defined as Pre-Boot Authorization (PBA) Phase I and Phase II. Additionally, CryptoPro updates the firmware keychain information and activates SecureBoot, disabling the execution of unsigned or untrusted EFI binaries.

From an information security perspective, exploitation of the secured architecture requires bypassing of PBA Phase I, or the UEFI initialization process, and obtaining code execution prior to the initialization of PBA Phase II. The following graphic depicts this circular boot sequence:

![](https://images.squarespace-cdn.com/content/v1/576323cfd482e984e113fe9c/2bf8b56c-26e3-4220-b6cd-c8375d736642/signal-2025-08-26-193917.jpeg)

Vynamic Security Suite - PBA Boot Cycle

## CVE-2024-46916

In my original content, I described an attack surface where `/etc/fstab` could be moved and linked from `/etc/mtab`, labeled as [CVE-2023-24063](https://cve.mitre.org/cgi-bin/cvename.cgi?name=2023-24063). This slight system change disabled the creation of several temporary file systems and gave persistence to `/root`. From this vantage point, root’s `.profile` script could be modified - allowing for code execution during system initialization. This path of compromise was removed from the next patch release of VSS, version 3.3.0 SR10, as the `rm /etc/mtab` instruction was removed from `/etc/rc.d/init.d/mountfs`. However, there were two additional delete instructions that perpetuated this attack `/fastboot` and `/forcefsck`, also located in `/etc/rc.d/init.d/mountfs`:

```
# Remove fsck-related file system watermarks.
rm -f /fastboot /forcefsck

...

boot_mesg "Recording existing mounts in /etc/mtab..."
> /etc/mtab
mount -f / || failed=1
mount -f /proc || failed=1
mount -f /sys || failed=1
mount -f /sys/kernel/security ||  failed=1
(exit ${failed})
evaluate_retval
```

Before I continue with the details surrounding this attack surface, I would like to highlight that the PBA Phase I EFI index table for v3.3.0 SR9 and SR10 only contains about 58 elements that are validated as part of the Linux file system. Extraction of this index is elementary with the use of `strings` and a filter:

```
$ strings /EFI/CPSD/Bootxsa.efi | awk '/^\/[a-z]+\// && !/(main|debug)/ {print $0}'
/bin/bash
/bin/cat
/bin/chmod
/bin/dmesg
/bin/echo
/bin/grep
/bin/keyctl
/bin/mkdir
/bin/mknod
/bin/mount
/bin/sh
...
```

Having visibility of this content is critical to properly construct an exploit against the platform. As this list represents the Linux integrity SHA256 index table, contained in `Bootxsa.efi`. However, the full partition is not integrity validated and only the files that physically exist or selected are checked. Therefore, content that does not already exist or is not indexed, is fair game. As a result, there is a fairly large file based attack surface for the Linux partition. The default `rootfs` is listed below, notice it only contains a list of directories:

```
$ ls -l ./
total 84
drwxr-xr-x  2 root root  4096 Sep 14  2022 bin
drwxr-xr-x  3 root root  4096 Nov 10  2022 boot
drwxr-xr-x  2 root root  4096 Apr 18  2008 dev
drwxr-xr-x 22 root root  4096 Sep 14  2022 etc
drwxr-xr-x  2 root root  4096 Apr 21  2008 home
drwxr-xr-x  8 root root  4096 Sep 14  2022 lib
drwxr-xr-x  3 root root  4096 Sep 14  2022 libexec
drwxr-xr-x  2 root root  4096 Nov 17  2022 LOG
drwx------  2 root root 16384 Sep 14  2022 lost+found
drwxr-xr-x  2 root root  4096 Nov 17  2022 mnt
drwxr-xr-x  2 root root  4096 Apr 18  2008 proc
drwxr-xr-x  2 root root  4096 Nov 17  2022 root
drwxr-xr-x  4 root root  4096 Aug 19  2021 run
drwxr-xr-x  2 root root  4096 Sep 14  2022 sbin
drwxr-xr-x  2 root root  4096 Apr 18  2008 sys
drwxr-xr-x  2 root root  4096 Nov 17  2022 tmp
drwxr-xr-x 13 root root  4096 Sep 14  2022 usr
drwxr-xr-x  2 root root  4096 Nov 17  2022 var
```

Since `/fastboot` and `/forcefsck` don’t exist, they are open targets. As you may have guessed, yes, this vulnerability does provide an alternative code execution path in both VSS v3.3.0 SR9 and SR10, overlapping both [CVE-2023-24063](https://cve.mitre.org/cgi-bin/cvename.cgi?name=2023-24063) and [CVE-2023-24062](https://cve.mitre.org/cgi-bin/cvename.cgi?name=2023-24062). This vantage point of code execution is ultimately disabled with the introduction of SR12, where an `rm` and `mkdir` instruction set is introduced to `/etc/rc.d/init.d/mountfs`. This, of course, superseeds the `rm` instruction for `/fastboot` and `/forcefsck`.

```
# remove and re-create /root /var /tmp /mnt
rm -rf /root /var /tmp /mnt
mkdir /root /var /tmp /mnt

# Remove fsck-related file system watermarks.
rm -f /fastboot /forcefsck
```...