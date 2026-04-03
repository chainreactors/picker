---
title: Qilin EDR killer infection chain
url: https://blog.talosintelligence.com/qilin-edr-killer/
source: Over Security - Cybersecurity news aggregator
date: 2026-04-02
fetch_date: 2026-04-03T04:29:10.479370
---

# Qilin EDR killer infection chain

[Blog](/)

[ ]

* [Intelligence Center](https://talosintelligence.com/reputation)

  [ ]

  + [# Intelligence Center](https://talosintelligence.com/reputation)
  + BACK
  + [Intelligence Search](https://talosintelligence.com/reputation_center)
  + [Email & Spam Trends](https://talosintelligence.com/reputation_center/email_rep)
* [Vulnerability Research](https://talosintelligence.com/vulnerability_info)

  [ ]

  + [# Vulnerability Research](https://talosintelligence.com/vulnerability_info)
  + BACK
  + [Vulnerability Reports](https://talosintelligence.com/vulnerability_reports)
  + [Microsoft Advisories](https://talosintelligence.com/ms_advisories)
* [Incident Response](https://talosintelligence.com/incident_response)

  [ ]

  + [# Incident Response](/incident_response)
  + BACK
  + [Reactive Services](https://talosintelligence.com/incident_response/services#reactive-services)
  + [Proactive Services](https://talosintelligence.com/incident_response/services#proactive-services)
  + [Emergency Support](https://talosintelligence.com/incident_response/contact)
* [Blog](https://blog.talosintelligence.com)
* [Support](https://support.talosintelligence.com)

More

* Security Resources

  [ ]

  # Security Resources

  + BACK

  Security Resources
  + [Open Source Security Tools](https://talosintelligence.com/software)
  + [Intelligence Categories Reference](https://talosintelligence.com/categories)
  + [Secure Endpoint Naming Reference](https://talosintelligence.com/secure-endpoint-naming)
* Media

  [ ]

  # Media

  + BACK

  Media
  + [Talos Intelligence Blog](https://blog.talosintelligence.com)
  + [Threat Source Newsletter](https://blog.talosintelligence.com/category/threat-source-newsletter/)
  + [Beers with Talos Podcast](https://talosintelligence.com/podcasts/shows/beers_with_talos)
  + [Talos Takes Podcast](https://talosintelligence.com/podcasts/shows/talos_takes)
  + [Talos Videos](https://www.youtube.com/channel/UCPZ1DtzQkStYBSG3GTNoyfg/featured)
* Company

  [ ]

  # Company

  + BACK

  Company
  + [About Talos](https://talosintelligence.com/about)
  + [Careers](https://talosintelligence.com/careers)

![](/content/images/2026/03/EDR-Killer-header-1.jpg)

# Qilin EDR killer infection chain

By
[Takahiro Takeda](https://blog.talosintelligence.com/author/takahiro/),
[Holger Unterbrink](https://blog.talosintelligence.com/author/holger-unterbrink/)

Thursday, April 2, 2026 06:00

[Threat Spotlight](/category/threat-spotlight/)
[Reverse Engineering](/category/reverse-engineering/)
[malware](/category/malware/)

* Endpoint detection and response (EDR) tools are widely deployed and far more capable than traditional antivirus. As a result, attackers use EDR killers to disable or bypass them.
* Disabling telemetry collection (process, memory, network activity) limits what defenders can see and analyze.
* As defenders improve behavioral detection, attackers increasingly target the defense layer itself as part of their initial access or early execution stages.
* This blog provides an in-depth analysis of the malicious “msimg32.dll” used in Qilin ransomware attacks, which is a multi-stage infection chain targeting EDR systems. It can terminate over 300 different EDR drivers from almost every vendor in the market.
* We present multiple techniques used by the malware to evade and ultimately disable EDR solutions, including SEH/VEH-based obfuscation, kernel object manipulation, and various API and system call bypass methods.

---

This blog post provides an in-depth technical analysis of the malicious dynamic-link library (DLL) “msimg32.dll”, which Cisco Talos observed being deployed in Qilin ransomware attacks. The broader activities and attacks of Qilin was previously introduced and described in the blog post [here](https://blog.talosintelligence.com/an-overview-of-ransomware-threats-in-japan-in-2025-and-early-detection-insights-from-qilin-cases).

This DLL represents the initial stage of a sophisticated, multi-stage infection chain designed to disable local endpoint detection and response (EDR) solutions present on compromised systems. Figure 1 shows a high-level diagram demonstrating the overall execution flow of this infection chain.

![](https://blog.talosintelligence.com/content/images/2026/03/image1-1.jpg)

Figure 1. Infection chain overview.

The first stage consists of a PE loader responsible for preparing the execution environment for the EDR killer component. This secondary payload is embedded within the loader in an encrypted form.

The loader implements advanced EDR evasion techniques. It neutralizes user-mode hooks and suppresses Event Tracing for Windows (ETW) event generation at runtime by leveraging a -like approach. Additionally, it makes extensive use of structured exception handling (SEH) and vectored exception handling (VEH) to obscure control flow and conceal API invocation patterns. This enables the EDR killer payload to be decrypted, loaded, and executed entirely in memory without triggering detection by the locally installed EDR solution.

Once active, the EDR killer component loads two helper drivers. The first driver (“rwdrv.sys”) provides access to the system’s physical memory, while the second driver (“hlpdrv.sys”) is used to terminate EDR processes. Prior to loading the second driver, the EDR killer component unregisters monitoring callbacks established by the EDR, ensuring that process termination can proceed without interference.

Overall, the malware is capable of disabling over 300 different EDR drivers across a wide range of vendors. While the campaign has been previously reported by , , and others at a higher level, this analysis focuses on previously undocumented technical details of the infection chain (e.g., the SEH/VEH tricks and the overwriting of certain kernel objects).

## PE loader section (“msimg32.dll”)

The malicious DLL is most likely side-loaded by a legitimate application that imports functions from “msimg32.dll”. To preserve expected functionality, the original API calls are forwarded to the legitimate library located in “C:\Windows\System32”.

The version of “msimg32.dll” deployed by the threat actor triggers its malicious logic from within its `DllMain` function. As a result, the payload is executed as soon as the legitimate application loads the DLL.

![](https://blog.talosintelligence.com/content/images/2026/03/image2.png)

Figure 2. Malicious version of “msimg32.dll”.

Sophos also gave some technical and historical insights into this loader in their earlier blog, in which it is referred to as Shanya.

### Initialization phase

During initialization, the loader allocates a heap buffer in process memory that acts as a slot-policy table.

![](https://blog.talosintelligence.com/content/images/2026/03/image3.png)

Figure 3a. Allocating buffer for slot-policy table.

The size of this buffer is computed as "ntdll.dll" `OptionalHeader.SizeOfCode` divided by 16 ( `SizeOfCode >> 4`), resulting in one byte per 16-byte code slot covering the code region as defined by `OptionalHeader.SizeOfCode` (typically the .text range). Each entry in the table corresponds to a fixed 16-byte block relative to `BaseOfCode`.

The loader then iterates over the export table of “ntdll.dll”. For each exported function whose name begins with "Nt", the virtual address of the corresponding syscall stub is resolved. From this address, a slot index is calculated as: slot\_idx = (FuncVA - BaseOfCode)/16

This index is used to mark the corresponding entry in the slot-policy table. All Nt\* stubs are assigned a default policy, while selected functions are explicitly marked with special policies, including:

* `NtTraceEvent`
* `NtTraceControl`
* `NtAlpcSendWaitReceivePort`

The result is a data-driven classification of relevant syscall stubs without modifying the executable code of “ntdll.dll”. The resulting slot-policy-table appears as follows:

![](https://blog.talosintelligence.com/content/images/2026/03/image4.png)

Figure 3b. Slot-polic...