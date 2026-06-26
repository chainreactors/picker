---
title: Introduction to COM usage by Windows threats
url: https://blog.talosintelligence.com/introduction-to-com-usage-by-windows-threats/
source: Over Security
date: 2026-06-25
fetch_date: 2026-06-26T06:09:23.013443
---

# Introduction to COM usage by Windows threats

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

![](https://storage.ghost.io/c/af/a0/afa04ee3-414f-4481-8d23-7e7c146f192e/content/images/2026/06/GenericCiscoTalos-Header-1.webp)

# Introduction to COM usage by Windows threats

By
[Vanja Svajcer](https://blog.talosintelligence.com/author/vanja-svajcer/)

Thursday, June 25, 2026 06:00

[Threats](/category/threats/)

* Component Object Model (COM) is a fundamental Windows technology used by legitimate applications for object activation, inter-process communication, automation and language-independent component reuse. Those same qualities make it useful to threat actors.
* Malware frequently uses COM interfaces for lateral movement, execution, download and exfiltration, persistence, evasion, system discovery and automation of built-in Windows and Office functionality.
* Reverse engineering COM-heavy binaries requires researchers to move from opaque GUIDs and indirect vtable calls to meaningful classes, interfaces and method names.
* This post is based on research conducted for presentations at AVAR 2025 conference in Kuala Lumpur and a CARO 2026 workshop in Innsbruck.

---

[Component Object Model (COM)](https://learn.microsoft.com/en-us/windows/win32/com/component-object-model--com--portal) is one of the Windows technologies that analysts regularly encounter but may not always prioritize during triage, as the manual analysis of COM functionality in binary executable files can be labor-intensive.

The post starts with a brief introduction into COM, following how binaries utilizing COM can be analyzed, and some examples of malware families and their usage of COM. The post concludes with a list of further resources.

## COM as Windows glue

COM is an application binary interface (ABI) model for reusing software components. COM objects expose interfaces to client applications, and those interfaces can be consumed by multiple programming languages because the contract exists at the binary interface level rather than at a single language runtime level. COM is a fundamental, principal way for components written in different languages to communicate.

Microsoft describes COM as a distributed, object-oriented system for creating binary software components that can interact with each other. COM is also the foundation for technologies such as OLE and ActiveX.

![](https://storage.ghost.io/c/af/a0/afa04ee3-414f-4481-8d23-7e7c146f192e/content/images/2026/06/windows-threats-COM.jpg)

**Figure 1. COM acts as** **glue** **between** **component** **consumers and** **component** **providers written in different languages.** **Credit** **for original figure: James Forshaw, Google Project Zero.**

This language independence is visible in common scripting and automation patterns. The same [COM object](https://learn.microsoft.com/en-us/windows/win32/com/com-clients-and-servers) may be created from VBScript, PowerShell, Python, or C/C++. For example, a script can instantiate the `WScript.Shell` COM object and use it to read or write registry values, execute a command, create shortcuts, or access environment variables — and it can do it in a very similar way using different scripting languages supporting COM automation.

![](https://storage.ghost.io/c/af/a0/afa04ee3-414f-4481-8d23-7e7c146f192e/content/images/2026/06/data-src-image-53238f08-d97e-4b97-812a-eeeecbd9b9df.png)

**Figure 2. As a glue between** **component** **consumers and** **component** **providers, languages such as VBS, PowerShell and Python can use it to access Windows services.**

## DCOM extends the same model across the network

[Distributed COM (DCOM)](https://learn.microsoft.com/en-us/openspecs/windows_protocols/ms-dcom/4a893f3d-bd29-48cd-9f43-d9777a4415b0) extends COM so a client can activate and use COM objects on another system. At a high level, the local client talks to a proxy, the remote server exposes a stub, and the COM runtime transports the method invocation over Microsoft RPC.

![](https://storage.ghost.io/c/af/a0/afa04ee3-414f-4481-8d23-7e7c146f192e/content/images/2026/06/windows-threats-DCOM.jpg)

**Figure 2. DCOM uses proxy and stub classes with the COM and RPC runtimes to carry method calls between** **component** **consumers and providers.** **Credit for original figure: James Forshaw, Google Project Zero.**

The existence of [CoCreateInstanceEx](https://learn.microsoft.com/en-us/windows/win32/api/combaseapi/nf-combaseapi-cocreateinstanceex) API in a binary, with the appropriate parameters, can be used to distinguish between local COM and DCOM. DCOM extends local COM activation by allowing an object to be associated with a specified remote computer. DCOM is also explicitly represented in MITRE ATT&CK as one of the techniques and is described in [Remote Services: Distributed Component Object Model, T1021.003](https://attack.mitre.org/techniques/T1021/003/).

## Classes, interfaces, and the registry

Classes and interfaces are two foundational COM concepts.

COM classes are templates for creating COM objects. A class is identified by a class identifier (CLSID), a GUID that uniquely identifies the component.

[GUID](https://learn.microsoft.com/en-us/windows/win32/com/com-technical-overview) is a 128-bit identifier used to uniquely identify COM-related objects and interfaces. The string representation of a GUID is common in the Windows registry, scripts, and configuration text. It is typically formatted as:

```
{XXXXXXXX-XXXX-XXXX-XXXX-XXXXXXXXXXXX}
```

A GUID can also appear as a binary structure in a compiled executable. In a binary, the first three fields are typically stored in little-endian byte order, which is why byte-pattern searches for GUIDs differ from the familiar string form. Readers should be aware that many malware families assemble GUID structure dynamically on the stack before attempting to create a new object in order to make the analysis process harder.

Interfaces...