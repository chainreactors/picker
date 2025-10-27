---
title: Finding vulnerabilities in ClipSp, the driver at the core of Windows’ Client License Platform
url: https://blog.talosintelligence.com/finding-vulnerabilities-in-clipsp-the-driver-at-the-core-of-windows-client-license-platform/
source: Over Security - Cybersecurity news aggregator
date: 2024-11-26
fetch_date: 2025-10-06T19:21:50.093992
---

# Finding vulnerabilities in ClipSp, the driver at the core of Windows’ Client License Platform

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

# Finding vulnerabilities in ClipSp, the driver at the core of Windows’ Client License Platform

By
[Philippe Laulheret](https://blog.talosintelligence.com/author/philippe/)

Monday, November 25, 2024 08:00

[Vulnerability Deep Dive](https://blog.talosintelligence.com/category/vulnerability-deep-dive/)

By Philippe Laulheret

ClipSP (clipsp.sys) is a Windows driver used to implement client licensing and system policies on Windows 10 and 11 systems.

Cisco Talos researchers have discovered eight vulnerabilities related to clipsp.sys ranging from signature bypass to elevation of privileges and sandbox escape:

* [TALOS-2024-1964](https://talosintelligence.com/vulnerability_reports/TALOS-2024-1964) (CVE-2024-38184)
* [TALOS-2024-1965](https://talosintelligence.com/vulnerability_reports/TALOS-2024-1965) (CVE-2024-38185)
* [TALOS-2024-1966](https://talosintelligence.com/vulnerability_reports/TALOS-2024-1966) (CVE-2024-38186)
* [TALOS-2024-1968](https://talosintelligence.com/vulnerability_reports/TALOS-2024-1968) (CVE-2024-38062)
* [TALOS-2024-1969](https://talosintelligence.com/vulnerability_reports/TALOS-2024-1969) (CVE-2024-38187)
* [TALOS-2024-1970](https://talosintelligence.com/vulnerability_reports/TALOS-2024-1970) (CVE-2024-38062)
* [TALOS-2024-1971](https://talosintelligence.com/vulnerability_reports/TALOS-2024-1971) (CVE-2024-38062)
* [TALOS-2024-1988](https://talosintelligence.com/vulnerability_reports/TALOS-2024-1988) (CVE-2024-38062)

This research project was also presented at both HITCON and Hexacon. A recording of the latter’s presentation is embedded at the end of this article.

## **What is ClipSp?**

ClipSp is a first-party driver on Microsoft Windows 10 and 11 that is responsible for implementing licensing features and system policies, and as such it is one of the main components of the Client Licensing Platform (CLiP). Little is known about this driver; while most Microsoft drivers and DLLs have publicly available debug symbols, in the case of ClipSp, those were removed from Microsoft's symbol server. Debug symbols provide function names and other related debug information that can be leveraged by security researchers to infer the intent behind the many functions of a binary; their absence hinders that. Surprisingly, the driver is also obfuscated, a very rare occurrence in Microsoft binaries, likely to deter reverse engineering even further. Limited public research exists, much of which either [predates](https://github.com/KiFilterFiberContext/windows-software-policy) our findings or [was released](https://massgrave.dev/blog/keyhole) in response to our reports. The latter research also shares [symbols](https://massgrave.dev/blog/keyhole#giving-season) from an older version of ClipSp, which could be a useful springboard for anyone wanting to research this driver. The most interesting aspect of this software involves implementing features related to licensing Windows applications from the Windows App store and activation services for Windows itself.

## **Deobfuscation**

The driver is obfuscated with Warbird, which is Microsoft’s proprietary obfuscator. Luckily, past [research](https://github.com/KiFilterFiberContext/windows-software-policy/blob/master/clipsp-unpack.py) comes in handy, and we can adapt to suit our needs. The plan to deobfuscate the driver is to leverage the binary emulation framework [Qiling](https://github.com/qilingframework/qiling), to emulate the part of the driver responsible for deobfuscating the obfuscated sections, and dump the executable memory range to import it into our favorite reversing tool.

During normal operation, the obfuscation appears as follows:

![](https://lh7-rt.googleusercontent.com/docsz/AD_4nXenEX2YKLHXedvaDKcaCjKexROQkPacab06CJE2Xrjn_VcZiZLoh03r1KD7ghoVbk83rXU7vNqFmflYQ7N05GklWZYn5ErXc7qhveiLjviYb3oJWamQOd_C0KbiuLqFmWdNb9azIn_7N-kqQqMVZrXh_UU6?key=fxEy1OcE6M5HCWwt6qTH9A)

We can see that a decrypt function is called twice with different parameters, followed by a call to the actual function being deobfuscated and, finally, two calls to re-obfuscate the relevant section.

Using Ida Python, we can track all the references to the decrypt functions (there are actually two distinct functions), and recover their arguments by looking at the instructions that precede the function call where the RCX and RDX registers are being assigned. Per calling conventions, these two registers are the first and second arguments of the function. Then, we can feed this information to our modified Qiling script to emulate the decryption functions and dump the whole deobfuscated binary. Once the driver is deobfuscated, we can start reversing it to understand how Windows communicates with the driver, understand various business logic elements, and look for vulnerabilities.

## **Driver communication**

Usually, drivers either register a device that can be reached from userland or export the functions that are meant to be used by other drivers. In the ClipSp case, things behave slightly differently. The driver exports a “ClipSpInitialize” function that takes a pointer to an array of callback functions that get populated by ClipSp, to then be used by the calling driver to invoke ClipSp functionalities. Grepping for “ClipSpInitialize” throughout the System32 folder shows that the best candidate for using ClipSp is “ntoskrnl.exe”, followed by a handful of filesystem drivers that use a limited amount of ClipSp functions. For the rest of this report, we will focus on how “ntoskrnl” interacts with ClipSp.

Analyzing the cross-references within the Windows’ kernel to ClipSp functions, it becomes clear that, to interact with them, a call to “NtQuerySystemInformation” with the SystemPolicy class is required. Other binaries in the CLiP ecosystem will issue these system calls, while also providing a remote procedure c...