---
title: Undocumented driver-based browser hijacker RedDriver targets Chinese speakers and internet cafes
url: https://blog.talosintelligence.com/undocumented-reddriver/
source: Over Security - Cybersecurity news aggregator
date: 2023-07-12
fetch_date: 2025-10-04T11:57:37.219325
---

# Undocumented driver-based browser hijacker RedDriver targets Chinese speakers and internet cafes

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

# Undocumented driver-based browser hijacker RedDriver targets Chinese speakers and internet cafes

By
[Chris Neal](https://blog.talosintelligence.com/author/chris-neal/)

Tuesday, July 11, 2023 13:04

[Threat Advisory](https://blog.talosintelligence.com/category/threat-advisory/)

* Cisco Talos has identified multiple versions of an undocumented malicious driver named “RedDriver,” a driver-based browser hijacker that uses the Windows Filtering Platform (WFP) to intercept browser traffic. RedDriver has been active since at least 2021.
* RedDriver utilizes HookSignTool to forge its signature timestamp to bypass Windows driver-signing policies.
* Code from multiple open-source tools has been used in the development of RedDriver's infection chain, including HP-Socket and a custom implementation of ReflectiveLoader.
* The authors of RedDriver appear to be skilled in driver development and have deep knowledge of the Windows operating system.
* This threat appears to target native Chinese speakers, as it searches for Chinese language browsers to hijack. Additionally, the authors are likely Chinese speakers themselves.

## RedDriver targets Chinese-speaking users

There are clear indications that the intended victims of this threat are native Chinese speakers. Firstly, the driver contains a hardcoded list of Chinese language browser process names, which are searched for and hijacked. Additionally, in one instance RedDriver contained a list of driver names, many of which were related to multiple Chinese language internet cafe management software products. There are also many indications that the authors of RedDriver are native Chinese speakers themselves.

## Multi-stage infection chain leads to RedDriver

RedDriver’s infection chain begins with a single executable packed with Ultimate Packer for eXecutables (UPX), named “DnfClientShell32.exe.” The resource section of the DnfClientShell32 binary contains two DLLs, one named “DnfClient” and another, aptly named “ReflectiveLoader32.”

* DnfClientShell32 - 5a13091832ef2fd837c33acb44b97c37d4f1f412f31f093faf0ce83dcd7c314e
* DnfClient - 9e59eba805c361820d39273337de070efaf2bf804c6ea88bbafc5f63ce3028b1
* ReflectiveLoader32 - c96320c7b57adf6f73ceaf2ae68f1661c2bfab9d96ffd820e3cfc191fcdf0a9b

The filename “DnfClient” is likely used to masquerade as an identically named executable from a game called “[Dungeon Fighter Online](https://dnf.qq.com/cp/a20230615index/index.html),” also referred to as “DNF.” The Dungeon Fighter games are immensely [popular in China](https://www.gamesindustry.biz/dungeon-fighter-online-passes-3-million-concurrent-users).

Once executed, DnfClientShell32 uses the ReflectiveLoader32 binary in its resource section to inject the DnfClient resource into a remote process. After the injection process is completed, DnfClient begins encrypted communications with the command and control (C2) infrastructure to initiate the download of the RedDriver payload. DnfClient then opens a listening port to receive redirected browser traffic from RedDriver. To facilitate network communications, DnfClient utilizes code from the open-source library [HP-Socket](https://www.oschina.net/p/hp-socket).

## Introducing: RedDriver

During our research into [HookSignTool](https://blog.talosintelligence.com/old-certificate-new-signature/), Cisco Talos observed the deployment of an undocumented malicious driver utilizing stolen certificates to forge signature timestamps, effectively bypassing driver signature enforcement policies within Windows. Its name originates from the string “RedDriver” which is contained within the binary and the file name in its PDB file path: "E:\\Project\\PTU\\PTU\\Bin\\x64\\Release\\RedDriver.pdb”.

![](https://lh5.googleusercontent.com/GS3J8b56IJNLJdR4wpu4sZ5czge9Z-AchsAUO1X5USo3yDO-s8PnVV18Q1Kf1vwMdhNRzkgkL5nnVnZlhHMPCDx4zlXtHOTTOTvlxW-VEbh2kfmH4Uo_Hvfj5eaPmMNoOMsUcvtpCVLUDDppoPIRTrI)

*RedDriver name within disassembly.*

RedDriver is a critical component of a multi-stage infection chain that ultimately hijacks browser traffic and redirects it to localhost (127.0.0.1). The target browser is chosen from a hardcoded list containing the process names of many popular Chinese language browsers as well as Google Chrome and Microsoft Edge.

![](https://lh6.googleusercontent.com/R1gLZGtmTeZDOUIhbHRtUgDuAsFo0p0r0982HTwUec6fv5BNJBel8eA2PjOdrZlgv76Z2hepkzeGVb3nVDMwswECb6ErwDnufRz0ACJd32aNbavMLtSjVL6cwJQgIA2TUf-LRXfpE5jn7jWj6Rs8jgw)

*Hard-coded list of browser names within RedDriver.*

RedDriver imports several functions from FWPKCLNT.sys, a component of the [Windows Filtering Platform](https://learn.microsoft.com/en-us/windows/win32/fwp/windows-filtering-platform-start-page):

> *“Windows Filtering Platform (WFP) is a set of API and system services that provide a platform for creating network filtering applications. The WFP API allows developers to write code that interacts with the packet processing that takes place at several layers in the networking stack of the operating system. Network data can be filtered and also modified before it reaches its destination,” from Microsoft MSDN.*

![](https://lh5.googleusercontent.com/qgHLL_JKTXvdGesvhn5zJ2IaexxLnZd62kcaPlZNnjL9iCUsa42QjOEJrR3xVJkvZ2hzyBYx9bohJ8CNA3RUkqwFffxGK1xrRDt-IdP-YbMKhUxLEDl53JDkvDRCi99IZVlpjNXPYWVCb8qhyPngQsA)

*RedDriver FWPKCLNT.sys imports.*

Using these imported functions, RedDriver redirects traffic from the hijacked browser and replaces the destination IP address with 127.0.0.1, thereby redirecting it to the listening port DnfClient opens. A root certificate is also silently installed on the target system without user interaction, as made evident by the registry entry that is added:

“MACHINE\SOFTWARE\MICROSOFT\SYSTEMCERTIFICATES\ROOT\CERTIFICATES\9743EE39882EFD63036E6EAD3AFFD6D765628161”

As of publication time, the end ...