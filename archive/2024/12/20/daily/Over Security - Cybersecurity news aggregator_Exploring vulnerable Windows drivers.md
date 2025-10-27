---
title: Exploring vulnerable Windows drivers
url: https://blog.talosintelligence.com/exploring-vulnerable-windows-drivers/
source: Over Security - Cybersecurity news aggregator
date: 2024-12-20
fetch_date: 2025-10-06T19:41:29.475703
---

# Exploring vulnerable Windows drivers

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

![](/content/images/2024/12/GenericCiscoTalos-Header-1.webp)

# Exploring vulnerable Windows drivers

By
[Vanja Svajcer](https://blog.talosintelligence.com/author/vanja-svajcer/),
[James Nutland](https://blog.talosintelligence.com/author/james/),
[Nicole Hoffman](https://blog.talosintelligence.com/author/nicole/),
[Chris Neal](https://blog.talosintelligence.com/author/chris-neal/)

Thursday, December 19, 2024 06:04

[Threats](/category/threats/)
[vulnerability](/category/vulnerability/)
[drivers](/category/drivers/)

This post is the result of research into the real-world application of the Bring Your Own Vulnerable Driver (BYOVD) technique along with Cisco Talos’ series of posts about  [malicious Windows drivers.](https://malicious%20windows%20drivers./) Some of this research was presented at the [AVAR conference](https://aavar.org/cybersecurity-conference/) in Chennai at the beginning of December 2024.

We would like to send a special thanks to [Connor McGarr](https://connormcgarr.github.io/), [Russell Sanford](https://www.linkedin.com/in/russell-sanford-759b3561/), [Ryan Warns](https://www.linkedin.com/in/ryan-warns-7a8415b3/), [Tim Harrison](https://www.linkedin.com/in/tharrison0/) and [Michal Poslušný](https://www.welivesecurity.com/en/our-experts/michal-poslusny/) for their previous work on analyzing vulnerabilities in drivers.

During our research into vulnerable Windows drivers, we investigated classes of vulnerabilities typically exploited by threat actors as well as the payloads they typically deploy post-exploitation. The attacks in which attackers are deliberately installing known vulnerable drivers only to later exploit them is a technique referred to as Bring Your Own Vulnerable Driver (BYOVD).

# How are threat actors using BYOVD?

Malicious actors use these drivers to perform a myriad of actions that help them achieve their goals. In our research, we identified three major payloads used, which we describe below.  Along with these payloads, we also identified recent activity linked to ransomware groups, which demonstrates real-world cases of malicious actors exploiting vulnerable Windows drivers to achieve their objectives.

## Vulnerable drivers and common payloads

### Local escalation of privileges (admin to kernel/system)

One of the most common payloads, when we consider vulnerable drivers with arbitrary kernel memory write vulnerabilities, is escalating the privileges of a malicious process. The access privileges for any process are stored in the primary access token structure, which is contained at an undocumented offset in the \_EPROCESS structure, the kernel mode structure used to maintain information about each individual process by the Windows kernel. Vergilius Project contains the documentation and offsets of almost all undocumented Windows structures, including [\_EPROCESS](https://_eprocess/), and can be used as a reference, equally by offensive researchers and defenders.

A common strategy for escalating privileges of an unprivileged process is to find the \_EPROCESS structure of a higher privileged process in kernel memory and replace the access token of the unprivileged process with the access token of the privileged process, which is relatively simple if a vulnerable drivers can be used for reading and writing kernel memory space.

![](https://blog.talosintelligence.com/content/images/2024/12/data-src-image-fdf49e55-a18d-497c-8eab-4bf1e3941fc7.png)

**\_EPROCESS structure contains Windows Process Primary access token (credit: Windows Internals 7****th** **edition)**

For example, a privilege escalation may be done by following the steps below:

1. Find one \_EPROCESS structure/object
2. For example, load ntoskernel.exe in user mode and calculate RVA to PsInitialSystemProcess, which points to the System process (id: 0x04) \_EPROCESS structure when ntoskernel.exe is loaded in memory during the boot process.
3. Use NtQuerySystemInformation((SYSTEM\_INFORMATION\_CLASS) 11, ModuleInfo, 1024 \* 1024, NULL))) // 11 = SystemModuleInformation to find ntoskernel VA – use the vuln driver to read the offset, add the RVA to find the \_EPROCESS structure in kernel memory.
4. Read the token from the known offset using the vulnerable driver read or memory copy functionality.
5. Parse \_EPROCESS to find the  ActiveProcess links member that points to a linked list of other \_EPROCESSES and iterate until the low privilege process is found.
6. Overwrite the unprivileged process access token with the one previously saved from the SYSTEM process, using a vulnerable driver kernel memory write functionality.

### Loading of unsigned kernel code

Arbitrary kernel memory write vulnerabilities in drivers can be used to deploy unsigned malicious code into the kernel memory space, either in the shellcode format or a format of the unsigned malicious driver. There are several open-source unsigned device drivers loading utilities. In one instance, [Lenovo Mapper](https://github.com/estimated1337/lenovo_mapper) was used as a base to develop a game cheat utility “sexy\_girl\_addy.exe”, which was uploaded to VirusTotal in May 2024. The utility used the code in Lenovo Mapper to load a driver which seems to attempt to disable the TPM-based license check in the game Valorant.

![A computer screen shot of a program code  Description automatically generated](https://blog.talosintelligence.com/content/images/2024/12/data-src-image-1243c5d7-3c6e-4501-a899-113301888421.png)

**Lenovo Mapper code is used to deploy an unsigned cheat driver using the previously mentioned arbitrary memory write vulnerability CVE-2022-3699**

![A screen shot of a computer program  Description automatically generated](https://blog.talosintelligence.com/content/images/2024/12/data-src-image-6da63766-bd24-4414-b0ea-c68ff9485025.png)

**TPM driver functionality was disab...