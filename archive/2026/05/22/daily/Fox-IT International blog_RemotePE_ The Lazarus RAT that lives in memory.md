---
title: RemotePE: The Lazarus RAT that lives in memory
url: https://blog.fox-it.com/2026/05/22/remotepe-the-lazarus-rat-that-lives-in-memory/
source: Fox-IT International blog
date: 2026-05-22
fetch_date: 2026-05-23T05:39:06.178517
---

# RemotePE: The Lazarus RAT that lives in memory

[Skip to content](#content)

[![Fox-IT International blog](https://blog.fox-it.com/wp-content/uploads/2019/02/fox-it-logo.png)](https://blog.fox-it.com/)

[Fox-IT International blog](https://blog.fox-it.com/)

News and opinions from Fox-IT

Menu

* [Home](https://blog.fox-it.com/)
* [Archive](https://blog.fox-it.com/archive/)
* [Back to Fox-IT](http://www.fox-it.com)

# RemotePE: The Lazarus RAT that lives in memory

[Fox-SRT](https://blog.fox-it.com/author/foxsrt/)

[Blog](https://blog.fox-it.com/category/blog/), [Threat Intelligence](https://blog.fox-it.com/category/threat-intelligence/)

May 22, 2026
17 Minutes

**Authors:** Yun Zheng Hu and Mick Koomen

![](https://blog.fox-it.com/wp-content/uploads/2026/05/remotepe.png)

# Summary

Last year, we published research[1](#76199bc1-3846-41cc-8a07-85e8de66bf97) about a North Korean Lazarus subgroup targeting financial and cryptocurrency organizations, encountered during multiple incident response engagements. This Lazarus subgroup overlaps with activity linked to AppleJeus[2](#83c30f4e-5fdd-486f-9172-5cbe566cc416), Citrine Sleet[3](#f575332d-ce4b-4167-bec1-a01051debe40), UNC4736[4](#41c37b52-f2e3-4237-bac5-6197cff9f2fe), and Gleaming Pisces[5](#97258f48-7465-44c6-8b02-7f97f9b4f721). In one investigation, we observed that the actor had replaced ThemeForestRAT and PondRAT with a more sophisticated memory-only toolset. This follow-up post covers all three malware families from that toolset: DPAPILoader, RemotePELoader and RemotePE.

The three form a chain. DPAPILoader decrypts and loads RemotePELoader from disk using the Windows Data Protection API (DPAPI). RemotePELoader beacons to a C2 server and waits until it receives the next stage: RemotePE, a RAT executed entirely in memory and never written to disk, leaving no filesystem artifacts. At the time of writing, we have not found samples of RemotePELoader or RemotePE on VirusTotal.

The toolset’s environmental keying, memory-only execution, EDR evasion, and low forensic footprint suggest it is purpose-built for long-term observation campaigns. This allows the actor to quietly maintain access over an extended period before moving to a high-impact final objective such as data theft or a large-scale financial heist, consistent with this actor’s known history.
We are sharing samples with detection rules and indicators of compromise (IOCs) to help defenders identify and respond to this toolset in their environments.

[![](https://blog.fox-it.com/wp-content/uploads/2026/05/remotepe_diagram-4.png)](https://blog.fox-it.com/wp-content/uploads/2026/05/remotepe_diagram-4.png)

*Figure 1: The three-stage chain: DPAPILoader decrypts and loads RemotePELoader from disk, which retrieves and executes RemotePE in memory*

# DPAPILoader: First-stage, environmentally keyed loader

DPAPILoader is implemented as a DLL whose purpose is to decrypt and load an encrypted payload from disk using DPAPI. In the incident response case, it was found as `C:\Windows\System32\Iassvc.dll`, installed under the service name “Internet Authentication Service.” This service runs `Iassvc.dll` automatically on system startup, providing persistence for the toolset. The filename and service name are chosen to mimic the legitimate Windows Server Internet Authentication Service (IAS) and its accompanying DLL `C:\Windows\System32\iassvcs.dll` (*note the extra ‘s’ in the filename*).

In Listing 1, we list a Windows service record, extracted from the forensic image using Dissect[6](#0e9c979d-d7dd-4044-a560-b55f2092df4b), that shows the masquerading in detail.

```
          name (string) = Ias
   displayname (string) = Internet Authentication Service
   description (string) = Internet Authentication Service (IAS) is a component of Windows Server operating systems that provides centralized user authentication, authorization and accounting.
      servicedll (path) = %SystemRoot%\system32\Iassvc.dll
       imagepath (path) = %systemroot%\system32\svchost.exe
imagepath_args (string) = -k netsvcs -p
    objectname (string) = LocalSystem
         start (string) = Auto Start (2)
          type (string) = Service - Own Process (0x10)
  errorcontrol (string) = Normal (1)
```

*Listing 1: Service record from Dissect showing Windows service that runs DPAPILoader*

The sample from our investigation first checks whether it is running under `C:\Windows\System32\Svchost.exe`. It then loops over all files matching the wildcard path `C:\ProgramData\Microsoft\Windows\DeviceMetadataStore\en-US*.*`. This directory normally contains Microsoft Cabinet files used for device metadata packages. DPAPILoader skips any file beginning with the Cabinet magic bytes (`MSCF` / `4D 53 43 46`), filtering out legitimate metadata packages. Any file that passes this check and is larger than 51200 bytes (50 KiB) is decrypted using DPAPI and loaded into memory using libpeconv[7](#2ef238e7-a5ca-45b0-b14a-80dcb452d0d1) , an open-source reflective PE loading library.

Across the DPAPILoader samples we observed, the loading mechanism and host process differ, as documented in the Observed Samples section, but the core behaviour is consistent.

## DPAPI Encryption

DPAPILoader uses the Windows Data Protection API (DPAPI) to decrypt its payload. DPAPI ties cryptographic keys to a specific user account, with key management handled entirely by the OS. The caller only invokes encrypt and decrypt functions.

This offers the actor two advantages. First, the encrypted payload on disk is never in plaintext: if a sample is uploaded to VirusTotal, it is useless without the victim’s DPAPI keys. Static analysis is effectively impossible without them. Second, each deployment produces a unique encrypted blob, meaning the payload hash differs across victims and evades hash-based detection. The only prerequisite is prior access to the target machine to encrypt and drop the payload, something the actor has at this stage of the intrusion.

After DPAPI decryption, the payload is additionally XORed with `0x8D` before loading. This is consistent across all observed DPAPILoader samples. This approach is an instance of environmental keying[8](#54c10f72-56ea-4345-9990-a59a2f1979a9), where malware is bound to a specific victim environment and cannot be analysed or executed elsewhere.

## Observed Samples

We identified three DPAPILoader samples spanning roughly nine months, with differences in loading mechanism, host process, and payload storage.

The first sample (`Iassvc.dll`) is loaded as a Windows service via Svchost.exe, the second (`sspicli.dll`) is sideloaded by ESET’s edp.exe, and the third (`wmiclnt.dll`) uses the `WmiOpenBlock` export with no identified host process.

| PE timestamp | DLL name | Export | String obfuscation |
| --- | --- | --- | --- |
| 2023-11-14 | `Iassvc.dll` | `ServiceMain` | XOR `0x8D` |
| 2024-02-21 | `sspicli.dll` | `InitSecurityInterfaceW` | XOR `0x8D` |
| 2024-08-21 | `wmiclnt.dll` | `WmiOpenBlock` | DPAPI + XOR `0x8D` |

*Table 1: Observed DPAPILoader samples by PE timestamp*

The first two samples load the DPAPI-encrypted payload from the `DeviceMetadataStore` path. The third embeds the encrypted payload directly in the DLL, removing the dependency on a separate file on disk.

The second and third samples were found on VirusTotal. Without the victims’ DPAPI keys, we are unable to decrypt them. Both are a practical demonstration of the environmental keying discussed earlier.

The first sample comes from our incident response case, where a full forensic image of the compromised machine gave us access to the victim’s DPAPI keys, allowing us to trivially decrypt the payload using a Dissect[9](#24d63753-4eae-46d7-9774-7e68a734be37) shell:

[![](https://blog.fox-it.com/wp-content/uploads/2026/05/dpapi_payload_dissect.png)](https://blog.fox-it.com/wp-content/uploads/2026/05/dpapi_payload_dissect.png)

*Figure 2: Decrypting the DPAPI-encrypted PE payload using Dissect*

It turns out the decrypted payload is another loader, which we named Re...