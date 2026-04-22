---
title: Apple Watch forensics acquisition techniques and evidentiary artifacts
url: https://andreafortuna.org/2026/04/21/apple-watch-forensics/
source: Instapaper: Unread
date: 2026-04-21
fetch_date: 2026-04-22T04:45:09.527261
---

# Apple Watch forensics acquisition techniques and evidentiary artifacts

[Andrea Fortuna](/)
[ ]

[About](/about/)

Tools

[DFIR Toolkit](https://dfir-toolkit.andreafortuna.org)
[OSINT Toolkit](https://osint-toolkit.andreafortuna.org)

# Apple Watch forensics: acquisition techniques and evidentiary artifacts

Apr 21, 2026

by [Andrea Fortuna](/about/)

In most digital investigations involving Apple devices, the iPhone gets all the attention. It is the backup target, the iCloud anchor, the logical endpoint of every iOS acquisition workflow. The Apple Watch, by contrast, tends to be treated as a peripheral: something to photograph, bag, and note down in the chain of custody before focus shifts back to the phone. That attitude is increasingly difficult to justify.

![cover](/assets/2026/apple-watch-forensics-cover.jpg)

Cases where Apple Watch data provided evidence that the phone alone could not have supplied are no longer rare. There are now several documented instances where heart rate spikes and activity readings from a wearable were used to reconstruct the timeline of a physical struggle or to challenge alibis that appeared consistent when relying solely on phone logs. These instances established something investigators should now treat as a working principle: a watch worn daily accumulates a continuous, hard-to-falsify record of its wearer’s physiological state and physical location. That record has a different evidentiary character from anything an iPhone can produce on its own, and extracting it requires understanding a platform that follows its own acquisition rules.

This post provides a comprehensive map of these rules. It examines the hardware and OS landscape, the three primary data sources (the watch, the paired iPhone, and iCloud), and the acquisition techniques available across different hardware generations. It also details key forensic artifacts and the realistic limitations of what an examiner can expect to retrieve.

## The hardware and OS landscape

Apple Watch runs watchOS, a derivative of iOS that shares the same kernel, APFS filesystem, and security model but diverges significantly in its connectivity model and physical interface. There is no built-in USB port. The available acquisition path depends primarily on the SoC generation and the resulting security vulnerabilities:

| Series | SoC | Vulnerability | Acquisition Method |
| --- | --- | --- | --- |
| 0 - 3 | S1, S1P, S2 | checkm8 | Full Filesystem |
| 4 - 5 | S4, S5 | None | Logical |
| 6 | S6 | None | Logical (Wired Adapter) |
| 7 - 10, SE2, Ultra | S7 - S9 | None | Logical (Wireless Adapter) |

Because checkm8 targets the read-only boot ROM, it cannot be patched by software updates. This means that regardless of the watchOS version running on these legacy models, a full filesystem and keychain extraction is possible without knowing the passcode, as long as the examiner can establish a physical connection to the device. For Series 4 and later, the acquisition ceiling is logical, and it depends heavily on the device’s lock state and pairing status.

watchOS, like iOS, implements data protection classes that tie file encryption to the device passcode and unlock state. The distinction between BFU (Before First Unlock) and AFU (After First Unlock) applies here in the same way it does on an iPhone: in BFU, the protection class keys are not loaded into memory, and most user data is cryptographically inaccessible. The watch enters BFU state after a restart or after the wrist detection sensor determines the watch has been removed and a configurable timeout has elapsed. An examiner who receives a watch that is already in BFU state, without the passcode, faces significant constraints on modern hardware.

## Acquisition paths: a tiered map

The most effective way to structure Apple Watch acquisition is into three distinct tiers, defined by the depth of access they provide.

**Checkm8-based full filesystem extraction (Series 0 through Series 3)**

For legacy models, [Elcomsoft iOS Forensic Toolkit](https://blog.elcomsoft.com/2023/11/forensic-insights-into-apple-watch-data-extraction/) implements what the vendor describes as “perfect acquisition” on Series 0 and full filesystem extraction with keychain on Series 0 through Series 3. The procedure requires a Mac or Linux workstation, a compatible cable or dock adapter depending on the model, and the watch to be placed in Device Firmware Update (DFU) mode. Once the bootrom exploit is active, the toolkit mounts a custom ramdisk that bypasses the normal boot sequence, then images the APFS container. The resulting image includes the full `/private/var/` user partition, the keychain database, and all the application sandboxes. Crucially, this extraction does not require the passcode because the bootrom exploit bypasses the Secure Enclave’s enforcement of data protection at the filesystem level, and decryption keys can be derived without user intervention.

The practical implication is that a Series 0, 1, 2, or 3 Apple Watch can yield complete data even from a locked device seized without any cooperation from its owner. This is the closest Apple Watch forensics gets to a true physical acquisition in the classic sense, and it is likely to remain available for these models indefinitely since the vulnerability is in hardware.

**Logical and advanced logical extraction (Series 4 and later)**

For devices Series 4 and later, the checkm8 path does not exist. The only direct extraction available from the watch itself is logical, using the same USB multiplexer (usbmuxd) protocol that governs iPhone forensic acquisition. The watch must be unlocked for the connection to be established, a requirement that parallels the restriction iOS devices operate under in the context of Lockdown Mode. If the watch is locked and no pairing trust has been established with the forensic workstation, the acquisition cannot proceed.

When the watch is unlocked and connection is possible, the following data is available through the Apple File Conduit (AFC) protocol: device information (hardware model, UDID, serial number, Bluetooth and Wi-Fi MAC addresses, disk capacity breakdown, watchOS version), the list of installed applications with installation timestamps, media files in the DCIM folder including photos synced from the paired iPhone and any audio recordings, and the `iTunes_Control/iTunes/MediaLibrary.sqlitedb` file, which contains iCloud account identifiers and the catalog of media purchases associated with the account.

The AFC path does not provide access to application sandboxes, health databases, or the keychain. It is useful for establishing device context and recovering media, but it is far from a complete picture of what the watch holds.

For Series 6 and newer, Elcomsoft’s [May 2025 update to iOS Forensic Toolkit](https://blog.elcomsoft.com/2025/05/ios-forensic-toolkit-now-supports-all-models-of-apple-watch/) extended logical acquisition support to the full current lineup. Series 6 requires a wired third-party adapter; Series 7 through 10, SE2, Ultra, and Ultra 2 use a wireless adapter. The process must be performed on macOS or Linux, not Windows, and on macOS requires a helper command running in a separate terminal session throughout the acquisition. The device must be unlocked, the connection is sensitive to physical positioning of the adapter, and repeated reconnection attempts may be necessary before the device is recognized.

**Cloud-based acquisition**

The third tier is cloud extraction via iCloud. This is often the most productive avenue in practice, precisely because it is not constrained by the physical state of the watch, the availability of a pairing record, or the device generation. Apple Watch syncs most of its collected data to iCloud through the paired iPhone’s iCloud account. When an examiner can authenticate to the Apple ID associated with the watch, cloud acquisition through tools such as Elcomsoft Phone Breaker or Cellebrite’s cloud extraction modules provides access to health data, activity records, heart rat...