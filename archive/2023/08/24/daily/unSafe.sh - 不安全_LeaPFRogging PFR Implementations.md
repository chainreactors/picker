---
title: LeaPFRogging PFR Implementations
url: https://buaq.net/go-175206.html
source: unSafe.sh - 不安全
date: 2023-08-24
fetch_date: 2025-10-04T11:58:49.589287
---

# LeaPFRogging PFR Implementations

* [unSafe.sh - 不安全](https://unsafe.sh)
* [我的收藏](/user/collects)
* [今日热榜](/?hot=true)
* [公众号文章](/?gzh=true)
* [导航](/nav/index)
* [Github CVE](/cve)
* [Github Tools](/tools)
* [编码/解码](/encode)
* [文件传输](/share/index)
* [Twitter Bot](https://twitter.com/buaqbot)
* [Telegram Bot](https://t.me/aqinfo)
* [Search](/search/search)

[Rss](/rss.xml)

[ ]
黑夜模式

![](https://8aqnet.cdn.bcebos.com/1d068f0475e8bafd3d8c4751c357d045.jpg)

LeaPFRogging PFR Implementations

Back in October of 2022, this announcement by AMI caught my eye. AMI has co
*2023-8-23 21:51:37
Author: [research.nccgroup.com(查看原文)](/jump-175206.htm)
阅读量:23
收藏*

---

Back in October of 2022, [this announcement](https://www.prnewswire.com/news-releases/ami-contributes-its-tektagon-openedition-platform-root-of-trust-firmware-code-base-to-the-open-compute-project-301652435.html) by AMI caught my eye. AMI has contributed a product named “Tektagon Open Edition” to the [Open Compute Project](https://www.opencompute.org/) (OCP).

> *Tektagon OpenEdition is an open-source Platform Root of Trust (PRoT) solution with foundational firmware security features that detect platform firmware corruption, recover the firmware and protect firmware integrity. With its open-source code, Tektagon OpenEdition™ augments transparency, resulting in high-quality code […]*

I decided to dig in and audit the recently open sourced code. But first, some background: Tektagon is a hardware root-of-trust (HRoT) that implements Intel PFR 2.0. So… What exactly is PFR?

## Platform Firmware Resiliency

PFR, or Platform Firmware Resiliency, is a standard defined by everyone’s favorite standards body, NIST, in [SP 800-193](https://nvlpubs.nist.gov/nistpubs/SpecialPublications/NIST.SP.800-193.pdf). The specification describes guidelines that support the resiliency of platform firmware and data against destructive attacks or unauthorized changes. These security properties are upheld by a new HRoT device that implements the PFR logic.

At its core, PFR acknowledges that in addition to the boot firmware (e.g., the BIOS), a platform contains numerous other peripheral devices which execute firmware and therefore also require integrity verification. Examples of these peripherals typically include GPUs, network cards, storage controllers, display controllers, and so on. Many of these peripherals are highly privileged (e.g., DMA capable), and so they are attractive targets for an attacker. It is important that their firmware images are protected from tampering. That is, if an attacker could compromise one of these peripherals by tampering with its firmware, they might be able to:

1. Achieve persistence on the platform across reboots.
2. Pivot towards compromising other more highly privileged firmware components.
3. Violate multi-tenant isolation and confidentiality expectations in cloud environments.

Although these motivations sound like they are centered around only protecting the integrity of the platform firmware and its data assets, the SP 800-193 specification also describes how PFR is crucial for protecting firmware availability. Here, availability refers to the ability to recover from corrupted flash storage, which might occur due to a failed firmware update, or perhaps, cosmic rays that cause bit flips in flash.

In the PFR specification, these security requirements appear as three guiding principles:

1. **Protection**: How authenticity and integrity of firmware and data should be upheld.
2. **Detection**: How to detect when firmware or data integrity has been violated.
3. **Recovery**: How to restore the platform to a known good state.

This is a somewhat crowded technology space. In addition to AMI’s Tektagon product, many other vendors have created their own PFR (or PFR-like) solutions whose purpose is to help assure device firmware authenticity and availability, further complicating the already complex [x86 system boot process](https://depletionmode.com/uefi-boot.html). Examples include Microsoft’s [Project Cerberus](https://learn.microsoft.com/en-us/azure/security/fundamentals/project-cerberus) which is used in Azure, Intel [PFR](https://www.intel.com/content/www/us/en/products/docs/processors/xeon/platform-firmware-resilience.html), Google [Titan](https://keystone-enclave.org/workshop-website-2018/slides/Scott_Google_Titan.pdf), Lattice’s [Root of Trust](https://www.latticesemi.com/pfr) FPGA solution, and more.

## PFR Attack Surfaces

PFR introduces a new device, a microcontroller or FPGA, that positions itself as the man-in-the-middle on the flash memory SPI bus. By sitting on the bus, PFR chipsets can interpose all bus transactions. Whenever a device (such as the Board Management Controller (BMC) or Platform Controller Hub (PCH)) reads or writes SPI flash, the PFR chipset proxies that request. This grants PFR the crucial responsibility of verifying the authenticity and integrity of all code and data that resides in the persistent storage media.

![](https://i0.wp.com/research.nccgroup.com/wp-content/uploads/2023/04/Simple_PFR_Diagram_2.png?resize=523%2C403&ssl=1)

However, by interposing buses in this manner, PFR exposes itself to a rather large attack surface. It must read, parse, and verify various binary blobs (firmware and data) that exist in flash. Such parsing can be a tedious and delicate process. If the code is not written defensively (a challenge for even the best C programmers) then memory safety violations may arise. Another concern is race conditions such as time-of-check-time-of-use (TOCTOU) or double fetch problems.

The PFR attack surface is also expanded by the fact that it communicates with other devices via I2C or SMBus. The bus typically carries the [MCTP](https://www.dmtf.org/documents/pmci/management-component-transport-protocol-mctp-base-specification-131) and [SPDM](https://www.dmtf.org/standards/spdm) protocols. Without going into too much detail about these specifications, these protocols are used to:

1. Establish a secure messaging channel between devices and IP blocks.
2. Perform device firmware attestation.
3. Detect and recover from TCB (Trusted Computing Base) failures.

Within the HRoT, these command handlers may accept variable length arguments, and so memory safety is again required when managing the message queues.

So, with that in mind, I decided to jump into the recently open-sourced AMI Tektagon project and hunt for bugs.

## Vulnerability #1: I2C Command Handler

This [first vulnerability](https://github.com/opencomputeproject/Tektagon-OpenEdition/issues/2) occurs in the PCH/BMC command handler. This is the same I2C communication interface that was mentioned above. Two of the command handlers violate memory safety.

```
uint8_t gUfmFifoData[64];
uint8_t gReadFifoData[64];
...
uint8_t gFifoData;
...
static unsigned int mailBox_index;

uint8_t PchBmcCommands(unsigned char *CipherText, uint8_t ReadFlag)
{
    byte DataToSend = 0;
    uint8_t i = 0;

    switch (CipherText[0]) {
        ...
        case UfmCmdTriggerValue:
            if (ReadFlag == TRUE) {
                DataToSend = get_provision_commandTrigger();
            } else {
                if (CipherText[1]   EXECUTE_UFM_COMMAND) {
                    ...
                } else if (CipherText[1]   FLUSH_WRITE_FIFO) {
                    memset( gUfmFifoData, 0, sizeof(gUfmFifoData));
                    gFifoData = 0;
                } else if (CipherText[1]   FLUSH_READ_FIFO) {
                    memset( gReadFifoData, 0, sizeof(gReadFifoData));
                    gFifoData = 0;
                    mailBox_index = 0;
                }
            }
            break;

        case UfmWriteFIFO:
            gUfmFifoData[gFifoData++] = CipherText[1];
            break;

        case UfmReadFIFO:
            DataToSend = gReadFifoData[mailBox_index];
            mailBox_index++;
            break;
        ...
```

Above, the `UfmWriteFIFO` command can eventually write data past the end of the `gUfmFifoData[]` array. This m...