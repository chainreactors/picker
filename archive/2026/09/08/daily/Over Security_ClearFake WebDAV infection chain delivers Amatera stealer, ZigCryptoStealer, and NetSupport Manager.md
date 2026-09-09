---
title: ClearFake WebDAV infection chain delivers Amatera stealer, ZigCryptoStealer, and NetSupport Manager
url: https://blog.talosintelligence.com/clearfake-webdav-infection-chain/
source: Over Security
date: 2026-09-08
fetch_date: 2026-09-09T06:56:41.248634
---

# ClearFake WebDAV infection chain delivers Amatera stealer, ZigCryptoStealer, and NetSupport Manager

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

![](https://storage.ghost.io/c/af/a0/afa04ee3-414f-4481-8d23-7e7c146f192e/content/images/2026/09/threat_spotlight-1.jpg)

# ClearFake WebDAV infection chain delivers Amatera stealer, ZigCryptoStealer, and NetSupport Manager

By
[Vanja Svajcer](https://blog.talosintelligence.com/author/vanja-svajcer/)

Tuesday, September 8, 2026 06:01

[Threats](/category/threats/)
[Threat Spotlight](/category/threat-spotlight/)

* Cisco Talos began an investigation after observing a DLL named "verification.google" executing from WebDAV at a Ukrainian government organization. We assess with moderate confidence that the attacks are not targeted at a particular organization, but are a part of a cryptocurrency and credentials-stealing operation using the Amatera stealer as the primary payload.
* Pivoting around the similar WebDAV behavior led to a second loader named "pf.ch" and allowed us to reconstruct its earlier delivery stages. The chain uses a Cloudflare Worker to inject JavaScript code stored on BNB Smart Chain and a ClickFix prompt impersonating Google CAPTCHA, leading to download and execution of Amatera stealer. The chain is likely very similar to what has caused the WebDAV-based execution at the Ukraininan government organization.
* The two Amatera builds were tasked with different secondary payloads by their respective command-and-control (C2) infrastructure: the "pf.ch" loader was instructed to deploy a NativeAOT loader running ZigCryptoStealer and a Go-based reverse proxy, while the "verification.google" loader was instructed to install an unauthorized instance of NetSupport Manager.
* The NetSupport Manager installation contained configuration with the C2 server using an IP address based in Russia. With moderate confidence, we assess that "verification.google" branch attack was conducted by a Russian threat actor.

 In April 2026, Cisco Talos identified an unusual WebDAV DLL execution in endpoint telemetry from a Ukrainian government organization. The remote file was named "verification.google" and was launched through the 32-bit version of "rundll32.exe". This initial finding led us to two similar delivery chains, two different DLL loaders and two ACR/Amatera stealer payloads. Talos tracks the actor behind the observed "verification.google" activity as UAT-10820.

Following the initial investigation, we decided to hunt for similar WebDAV and ordinal-execution patterns in an attempt to recover the full infection chain. Using VirusTotal, we were able to identify a full chain from a second DLL loader named "pf.ch".

These two examples are a part of a wider set of recent campaigns delivering Amatera through different infection chains. In July 2026, Malwarebytes [documented](https://www.malwarebytes.com/blog/threat-intel/2026/07/fake-games-spread-stealers-with-renpy-loader-msbuild-and-etherhiding) fake game and software downloads that used RenPy Loader, MSBuild and EtherHiding before delivering Amatera. Blackpoint Cyber [described](https://blackpointcyber.com/blog/novel-fake-captcha-chain-delivering-amatera-stealer/) another fake-verification chain that used a signed Microsoft App-V script, configuration stored in Google Calendar and a payload concealed in a PNG image. Apart from the main payload malware family, we found no common infrastructure or other evidence linking those activities to the chains described in this post.

## Initial finding in endpoint telemetry

The initial event that started the investigation was recorded in April 2026 and it showed an execution of a DLL file through a WebDAV UNC path together with startup of the Windows WebClient service. Apart from the initial command line, we had details of the checksum of the executed DLL but it was not clear what started the execution chain. It was time for hunting in open source intelligence repositories and Talos analytical platform. We wanted to find a similar execution with the similar loader and the payload family and ideally recover the whole infection chain which would likely point to how "verification.google" execution was triggered. This lead us to the "pf.ch" loader and the chain we discovered.

## Hunting reveals a second WebDAV delivery chain

The "pf.ch" sample uses the same combination of WebDAV, a disguised DLL filename and ordinal execution through "rundll32.exe". We were also able to recover the full ClickFake related sequence leading to this loader. Figure 1 shows both chains, with dashed elements marking stages that were not directly recovered. With low to medium confidence, we assess that the two delivery chains are identical.

![](https://storage.ghost.io/c/af/a0/afa04ee3-414f-4481-8d23-7e7c146f192e/content/images/2026/09/WebDAV-parallel-chains.jpg)

Figure 1. Parallel WebDAV infection chains and Amatera secondary payloads.

The discovered "pf.ch" loader chain was initiated by ClearFake Javascript injected into the content of a compromised site by a malicious Cloudflare worker.

The C2 server returned configuration instructing the stealer to download a DLL side-loading package in which a signed Chrome component sideloads a malicious NativeAOT DLL, "secur32.dll". The DLL loads ZigCryptoStealer and uses a vulnerable driver to terminate EDR software. A separate x86 shellcode loader with a Go reverse TCP proxy is also downloaded as a secondary payload by the Amatera configuration sent by the C2 server.

The secondary payload of the "verification.google" branch as instructed by its own C2, is a PowerShell script which attempts to install a sample of NetSupport Manager remote access tool.

### ClearFake retrieves browser code from BNB Smart Chain

The "pf.ch" branch begins likely on a compromised website. A Cloudflare Worker injects a malicious JavaScript which queries BNB Smart Chain testnet contract 0x886d310Ac23e05EA705e24E513D19f53793832A9 through "bsc-testnet-rpc[.]publicno...