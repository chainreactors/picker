---
title: Old certificate, new signature: open-source tools forge signature timestamps on Windows drivers
url: https://blog.talosintelligence.com/old-certificate-new-signature/
source: Over Security - Cybersecurity news aggregator
date: 2023-07-12
fetch_date: 2025-10-04T11:57:36.806976
---

# Old certificate, new signature: open-source tools forge signature timestamps on Windows drivers

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

# Old certificate, new signature: Open-source tools forge signature timestamps on Windows drivers

By
[Chris Neal](https://blog.talosintelligence.com/author/chris-neal/)

Tuesday, July 11, 2023 13:04

[Threat Advisory](https://blog.talosintelligence.com/category/threat-advisory/)

* Cisco Talos has observed threat actors taking advantage of a Windows policy loophole that allows the signing and loading of cross-signed kernel mode drivers with signature timestamp prior to July 29, 2015.
* Actors are leveraging multiple open-source tools that alter the signing date of kernel mode drivers to load malicious and unverified drivers signed with expired certificates.
* We have observed over a dozen code signing certificates with keys and passwords contained in a PFX file hosted on GitHub used in conjunction with these open source tools.
* The majority of drivers we identified that contained a language code in their metadata have the Simplified Chinese language code, suggesting the actors using these tools are frequently used by native Chinese speakers.
* Cisco Talos has further identified an instance of one of these open-source tools being used to re-sign cracked drivers to bypass digital rights management (DRM).
* We have released a second blog post alongside this one demonstrating real-world abuse of this loophole by an undocumented malicious driver named [RedDriver](https://blog.talosintelligence.com/undocumented-reddriver/).

*During the research phase for this blog post we reached out to Microsoft to notify them of our findings. In response, Microsoft has blocked all certificates discussed in this blog and has released an* [*advisory*](https://msrc.microsoft.com/update-guide/vulnerability/ADV230001)*. We would like to thank the Microsoft team for their assistance and cooperation in mitigating this threat.*

## Malicious drivers pose a significant threat

The Windows operating system (OS) is split into two layers, or “modes”: user mode, where the files and applications that users interact with reside, and the kernel mode, where kernel mode drivers and the underpinnings of Windows perform the necessary functions to run the system. Drivers can facilitate communication between these modes via the Windows API through a series of functions contained within system libraries.

Splitting the operating system into two modes creates a highly controlled logical barrier between the average user and the Windows kernel. This barrier is critical to maintaining the integrity and security of the OS, as access to the kernel provides complete access to a system. As such, leveraging a malicious driver can allow an attacker to pass through this barrier, resulting in total compromise of the target system.

![](https://lh5.googleusercontent.com/6VXtrWYFrX4eBwgobAcXMFbk92HoMDIhopZDprDnDCPmB4dQzmmbqo6Z0JlYbca2G6wZYM0EBqKaSoBLjnrIie8_bh6Z5YADuELQHPQy3BC3HMEXmNyToipvSCGfdatgMVJFcgN7htxHLXPQzeYQHaU)

*Windows kernel architecture*

Starting in Windows Vista 64-bit to combat the threat of malicious drivers, Microsoft began to require kernel-mode drivers to be digitally signed with a certificate from a verified certificate authority. Without signature enforcement, malicious drivers would be extremely difficult to defend against as they can easily evade anti-malware software and endpoint detection. Requiring signatures on drivers is the most critical component of defending against malicious kernel mode drivers.

Another issue that malicious drivers pose is the difficulty of conducting analysis of samples. Typical sandboxes used to analyze malware do not have the capability to monitor all of the behavior of a driver, meaning much of the analysis must be conducted manually. To further the difficulties posed by driver analysis, threat actors have begun to use code obfuscation on the drivers they deploy with tools such as VMProtect.

From an attacker's perspective, the advantages of leveraging a malicious driver include, but are not limited to, evasion of endpoint detection, the ability to manipulate system and user mode processes, and maintained persistence on an infected system. These advantages provide a significant incentive for attackers to discover ways to bypass the Windows driver signature policies.

Cisco Talos has observed threat actors taking advantage of a Windows policy loophole that allows the forging of signatures on kernel-mode drivers, thereby bypassing the certificate policies within Windows. As we will demonstrate below, this is facilitated by the use of open-source tooling and non-revoked certificates that either expired before or were issued prior to July 29, 2015.

## Windows driver policy loophole allows signature timestamp forging

Starting with Windows 10 version 1607, Microsoft updated its [driver signing policy](https://learn.microsoft.com/en-us/windows-hardware/drivers/install/kernel-mode-code-signing-policy--windows-vista-and-later-) to no longer allow new kernel-mode drivers that have not been submitted to, and signed by its Developer Portal. This process is intended to ensure that drivers meet Microsoft’s requirements and security standards. In an effort to maintain the functionality and compatibility of older drivers, Microsoft created exceptions for the following:

1. ***The PC was upgraded from an earlier release of Windows to Windows 10, version 1607.***
2. ***Secure Boot is off in the BIOS.***
3. ***Drivers was* [sic] *signed with an end-entity certificate issued prior to July 29th 2015 that chains to a supported cross-signed CA.***

The third exception creates a loophole that allows a newly compiled driver to be signed with non-revoked certificates issued prior to or expired before July 29, 2015, provided that the certificate chains to a supported cross-signed certificate authority. If a driver is successfully signed this way, it will not ...