---
title: slot2
url: https://kitploit.com/en/tools/github/cenobyte-vincit/slot2
source: Kitploit
date: 2026-08-19
fetch_date: 2026-08-20T02:55:06.470868
---

# slot2

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

slot2 — UEFI GRUB2 bootkit that installs a pre-boot networked implant via NVRAM boot option, chainloads a UKI, executes a dracut payload, and kexecs the stock kernel. | Kitploit

[Tools](/en/tools)/![GitHub](/providers/github.png)GitHub/cenobyte-vincit/slot2

![](/_next/image?url=https%3A%2F%2Fassets.kitploit.com%2Fproduction%2Fpublic%2Ftools%2F50499%2F2a3168710925744b8e5d293552febfe66a8b3ee0dcad0d153f84281dfd0f30d3.png&w=3840&q=75)

[Persistence Mechanisms](/en/categories/persistence-mechanisms)[Data Exfiltration](/en/categories/data-exfiltration)[Post-Exploitation](/en/categories/post-exploitation)[Cloud Security](/en/categories/cloud-security)[Command and Control](/en/categories/command-and-control)[Red Teaming](/en/categories/red-teaming)[Payload Development](/en/categories/payload-development)[Remote Access Trojan](/en/categories/remote-access-trojan)

![GitHub](/providers/github.png)cenobyte-vincit/slot2

# slot2

UEFI GRUB2 bootkit that installs a pre-boot networked implant via NVRAM boot option, chainloads a UKI, executes a dracut payload, and kexecs the stock kernel.

[View Repository](https://github.com/cenobyte-vincit/slot2)

61 day ago![Not yet reviewed](/_next/image?url=%2Fbadges%2Fkitploit_badge_not_reviewed_full.png&w=48&q=75)

### Most Popular

[View all →](/en/tools)

Discover the most used tools by our community.

Last 7 DaysLast 30 Days

Explore all tools

Browse our collection of tools

[View all tools →](/en/tools)

Share

# slot2

slot2: a two-stage UEFI GRUB2 bootkit that persists a pre-OS networked implant on Amazon Linux 2023 on AWS EC2 UEFI x86\_64.

by cenobyte [[email protected]](/cdn-cgi/l/email-protection#f2849b9c919b86939f9d80829386809b9397b2959f939b9edc919d9f) 2026

<https://github.com/cenobyte-vincit/slot2>

## Summary

slot2 is a bootkit for Amazon Linux 2023 on EC2. The AWS EC2 UEFI firmware loads it first. An embedded implant runs in the bootkit UKI (Unified Kernel Image: one EFI file with a bootkit kernel and initrd) before the stock OS boots, network included, then `kexec` is used to start the stock kernel a normal boot would have used. The operating system that comes up is the real, stock one.

Persistence is via a UEFI NVRAM load option and two files, a bootkit ESP file and a bootkit UKI; no userspace helper/rootkit service is used/required, and not a replaced vendor bootloader. In slot2, `98-payload.sh` is the implant that's used for pre-boot C2/infil/exfil and arbitrary disk writes to insert payloads such as RATs or kernel-based rootkits on the target's filesystems. The implant in this tree is a demonstration: it writes `/root/HELLO.TXT` and brings up the network to establish an Internet/network connection, which in an operation could be a network infil or exfil.

## Boot chain

UEFI firmware does not pick a kernel by itself. It walks a BootOrder of NVRAM load options, each a numbered slot (Boot0001, Boot0002, ...) that points at one EFI executable on the ESP. On EC2, Boot0001 is always present: the Amazon EBS entry that starts stock `\EFI\BOOT\BOOTX64.EFI`. slot2 adds Boot0002, pointing at a second file on that same ESP, and puts Boot0002 first on BootOrder. Firmware still has Boot0001 as fallback.

That second file has to be something firmware can execute, and it has to reach the bootkit UKI on the root filesystem, which firmware cannot see. GRUB is used because it can read GPT and XFS, find the UKI, and chainload it. The image is a custom `grub2-mkimage`, not the packaged Amazon GRUB; stock `BOOTX64.EFI` stays where the vendor put it. GRUB's only job here is to hand off to the UKI.

The UKI kernel then runs `98-payload.sh`, then `99-kexec-stock.sh` uses `kexec` to start the stock kernel and initrd a normal BLS boot would have used.

root@kitploit:~

```
  EC2 UEFI NVRAM
  ├── Boot0001 -> stock \EFI\BOOT\BOOTX64.EFI     (untouched)
  └── Boot0002 -> bootkit \EFI\BOOT\.BOOTX64.EFI  (created; first on BootOrder)
       |
       v
  ESP (VFAT)  /boot/efi
  └── /EFI/BOOT/
      ├── BOOTX64.EFI          stock (untouched) <- Boot0001
      └── .BOOTX64.EFI         bootkit GRUB2 PE  --chainload--+  <- Boot0002
                                                              |
  root FS (XFS, typical AL2023)                               |
  └── /var/lib/systemd/boot/                                  |
      └── uki.efi  <------------------------------------------+
            |
            |  98-payload.sh, then 99-kexec-stock.sh
            |  resolve stock target under /sysroot/boot/:
            |    loader/entries/*.conf  (BLS + grubenv; AL2023 primary)
            |    grub2/grub.cfg         (legacy fallback)
            |
            +-- kexec ----------------------------------------+
                                                              |
  /boot (stock, untouched)                                    |
  ├── vmlinuz-*  <--------------------------------------------+
  └── initramfs-*.img
            |
            +-- stock initrd -> stage-2 stock userspace
```

If `kexec` fails, stage 1 continues on the UKI kernel. The box stays bootable.

## Payload

The implant is `98-payload.sh`, a dracut pre-pivot hook inside the bootkit UKI. It is not a post-boot userspace service. This tree's implementation is a demo: remount `/sysroot` read-write, write `/root/HELLO.TXT`, bring NICs up, DHCP, then `wget` ifconfig.me (5s budget). Network failure does not block `kexec`.

Stage 1 has the real root at `/sysroot` (typically XFS, remounted rw). `/boot` is `/sysroot/boot`. Extra EBS volumes are not mounted unless the hook mounts them. The slim initrd ships busybox `udhcpc` and `wget`. `ip(8)` is the real-root binary, run via the initrd loader.

## Requirements

### Runtime host

The runtime host is the **target** (the EC2 instance that runs `deploy` and then reboots into the bootkit).

* Amazon Linux 2023 x86\_64
* EC2 instances that support UEFI with AMI boot mode `uefi` or `uefi-preferred`
* Root
* ESP mounted at `/boot/efi` (systemd automount is fine; `deploy` will trigger it)
* `libefivar` and `libefiboot` (`deploy` is dynamically linked; both come with the stock OS)

ARM64 / Graviton is not tested and thus not supported (yet?).

### Build host

Amazon Linux 2023 x86\_64.

* Root for `./install-dependencies.sh`
* The running kernel's `/boot/vmlinuz-$(uname -r)` and `/boot/initramfs-$(uname -r).img` (those files are packed into the UKI)
* `cc`, `make`, `pkg-config`, `grub2-mkimage`, `objcopy`, `kexec`, `openssl`, `xxd`

`./install-dependencies.sh` is the bootstrap. It installs the dnf packages above (plus `grub2-efi-x64-modules`, `systemd-boot-unsigned`, `efivar-devel`, `dracut`) and fetches the pinned busybox `udhcpc` and `wget` binaries.

## Build

On the **build host**:

root@kitploit:~

```
./install-dependencies.sh
make
```

Bare `make` writes `uki.efi`, `BOOTX64.EFI`, and `deploy`. It does not write the ESP, `/var/lib/systemd/boot`, or NVRAM. Trailer magic and `SOURCE_DATE_EPOCH` are in ARCHITECTURE.md.

## Deploy

Copy the shipped `deploy` ELF onto the **target**. No compiler. `uki.efi` and `BOOTX64.EFI` are already inside the trailer.

root@kitploit:~

```
scp deploy user@target-host:~/
```

On a colocated AL2023 instance the copy is optional; run `./deploy` from the build tree.

On the next reboot, firmware Boot...