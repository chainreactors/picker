---
title: catdoc zero-day, NVIDIA, High-Logic FontCreator and Parallel vulnerabilities
url: https://blog.talosintelligence.com/catdoc-zero-day-nvidia-high-logic-fontcreator-and-parallel-vulnerabilities/
source: Over Security - Cybersecurity news aggregator
date: 2025-06-12
fetch_date: 2025-10-06T22:54:53.932593
---

# catdoc zero-day, NVIDIA, High-Logic FontCreator and Parallel vulnerabilities

# Cisco Talos Blog

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

![](/content/images/2025/06/vuln-roundup.webp)

# catdoc zero-day, NVIDIA, High-Logic FontCreator and Parallel vulnerabilities

By
[Kri Dontje](https://blog.talosintelligence.com/author/kri/)

Wednesday, June 11, 2025 09:47

[Vulnerability Roundup](/category/vulnerability-roundup/)

Cisco Talos’ Vulnerability Discovery & Research team recently disclosed three zero-day vulnerabilities in catdoc, as well as vulnerabilities in Parallel, NVIDIA and High-Logic FontCreator 15.

The vulnerabilities mentioned in this blog post have been patched by their respective vendors, in adherence to [Cisco’s third-party vulnerability disclosure policy](https://sec.cloudapps.cisco.com/security/center/resources/vendor_vulnerability_policy.html), except in the case of the catdoc zero-day vulnerabilities, which were patched by our researcher ([patches found in this repository](https://github.com/Cisco-Talos/catdoc-talos-fixes/releases/tag/talos-fixes.2025-05)). This is an unusual case, because the vendor could not be reached to fix these high-risk bugs; our policy does not include fixing third-party vulnerabilities.

For Snort coverage that can detect the exploitation of these vulnerabilities, download the latest rule sets from [Snort.org](https://snort.org/), and our latest Vulnerability Advisories are always posted on [Talos Intelligence’s website](https://talosintelligence.com/vulnerability_reports).

## catdoc zero-day vulnerabilities

*Discovered by Ali Rizvi-Santiago of Cisco Talos.*

The catdoc program pulls plain text content from Microsoft Word, Excel, PowerPoint and Rich Text Format files. The vendor was unreachable, Debian will be merging our patches into their distribution. <https://github.com/Cisco-Talos/catdoc-talos-fixes/releases/tag/talos-fixes.2025-05>

[TALOS-2024-2128](https://talosintelligence.com/vulnerability_reports/TALOS-2024-2128) (CVE-2024-48877) is a memory corruption vulnerability in the Shared String Table Record Parser implementation in xls2csv utility version 0.95. A specially crafted malformed file can lead to a heap buffer overflow. An attacker can provide a malicious file to trigger this vulnerability.

[TALOS-2024-2131](https://talosintelligence.com/vulnerability_reports/TALOS-2024-2131) (CVE-2024-52035) is an integer overflow vulnerability which exists in the OLE Document File Allocation Table Parser functionality of catdoc 0.95., and [TALOS-2024-2132](https://talosintelligence.com/vulnerability_reports/TALOS-2024-2132) (CVE-2024-54028) is an integer underflow vulnerability in the OLE Document DIFAT Parser functionality. A specially crafted malformed file can lead to heap-based memory corruption for either vulnerability, and an attacker can provide a malicious file as a trigger.

## Parallel integer overflow vulnerability

*Discovered by KPC of Cisco Talos.*

Parallels is a desktop emulator for Mac computers that enables virtual Windows applications.

[TALOS-2025-2160](https://talosintelligence.com/vulnerability_reports/TALOS-2025-2160) (CVE-2025-31359) is a directory traversal vulnerability exists in the PVMP package unpacking functionality of Parallels Desktop for Mac version 20.2.2 (55879). This vulnerability can be exploited by an attacker to write to arbitrary files, potentially leading to privilege escalation.

There are three privilege escalation vulnerabilities in the virtual machine archive restoration functionality of Parallels Desktop for Mac version 20.1.1 (55740).

* [TALOS-2024-2126](https://talosintelligence.com/vulnerability_reports/TALOS-2024-2126) (CVE-2024-36486): When an archived virtual machine is restored, the prl\_vmarchiver tool decompresses the file and writes the content back to its original location using root privileges. An attacker can exploit this process by using a hard link to write to an arbitrary file, potentially resulting in privilege escalation.
* [TALOS-2024-2124](https://talosintelligence.com/vulnerability_reports/TALOS-2024-2124) (CVE-2024-54189): When a snapshot of a virtual machine is taken, a root service writes to a file owned by a normal user. By using a hard link, an attacker can write to an arbitrary file, potentially leading to privilege escalation.
* [TALOS-2024-2123](https://talosintelligence.com/vulnerability_reports/TALOS-2024-2123) (CVE-2024-52561): When a snapshot of a virtual machine is deleted, a root service verifies and modifies the ownership of the snapshot files. By using a symlink, an attacker can change the ownership of files owned by root to a lower-privilege user, potentially leading to privilege escalation.

## NVIDIA integer overflow vulnerability

*Discovered by Dimitrios Tatsis of Cisco Talos.*

NVIDIA cuobjdump is a command-line utility included in the NVIDIA CUDA Toolkit. Similar to the standard `objdump` utility, it parses CUDA executable files and displays information like PTX disassembly, section headers, relocations etc.

[TALOS-2025-2151](https://talosintelligence.com/vulnerability_reports/TALOS-2025-2151) (CVE-2025-23247) is an integer overflow in the ELF Section Parsing functionality of NVIDIA cuobjdump 12.8.55. A specially crafted fatbin file can lead to an out-of-bounds write. An attacker can provide a malicious file to trigger this vulnerability.

## High-Logic out-of-bounds read vulnerability

*Discovered by KPC of Cisco Talos.*

High-Logic FontCreator is a font editor for Windows & macOS. The program allows you to create, edit and export OpenType, TrueType and responsive variable fonts.

An out-of-bounds read vulnerability, [TALOS-2025-2157](https://talosintelligence.com/vulnerability_reports/TALOS-2025-2157) (CVE-2025-20001), exists in High-Logic FontCreator 15.0.0.3015. A specially crafted font file can trigger this vulnerability which can lead to disclosure of sensitive information. An attacker needs to trick the user into opening the mali...