---
title: Inside KeyDrift: Analyzing historical UAT-11473 activity on Cisco SD-WAN
url: https://blog.talosintelligence.com/uat-11473-keydrift/
source: Over Security
date: 2026-10-28
fetch_date: 2026-10-29T07:52:32.036100
---

# Inside KeyDrift: Analyzing historical UAT-11473 activity on Cisco SD-WAN

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

# Inside KeyDrift: Analyzing historical UAT-11473 activity on Cisco SD-WAN

By
[Cisco Talos](https://blog.talosintelligence.com/author/cisco/)

Wednesday, October 28, 2026 17:32

[Threat Advisory](https://blog.talosintelligence.com/category/threat-advisory/)
[APT](https://blog.talosintelligence.com/category/apt/)
[malware](https://blog.talosintelligence.com/category/malware/)

* Cisco Talos has identified UAT-11473, a highly sophisticated advanced persistent threat (APT) actor, who exploited [CVE-2026-20127](https://sec.cloudapps.cisco.com/security/center/content/CiscoSecurityAdvisory/cisco-sa-sdwan-rpa-EHchtZk), an authentication bypass vulnerability in Cisco SD-WAN Catalyst Controller instances to bypass authentication and gain unauthorized access to affected systems.
* UAT-11473 then installed a custom malware framework we track as “KeyDrift” consisting of multiple components geared towards collecting sensitive keying information, acting as backdoors and intermediate command-and-control (C2) hosts.
* Observed targeting spans across space and satellite services, defense and aerospace technology, and policy research.

---

Talos assesses with high confidence that UAT-11473’s operating infrastructure overlaps considerably with [Volt Typhoon’s “Silent Train” covert access network](https://www.lumen.com/blog/en-us/silent-train-volt-typhoon-operational-framework).

KeyDrift is a custom malware framework that is designed to operate in Cisco SD-WAN controller environments. Talos assesses with high confidence that the framework is designed to provide long-term persistent access and automated exfiltration of sensitive keying material. KeyDrift operates inside SD-WAN control-plane processes and is capable of intercepting decrypted control traffic, extracting control-session metadata and data-plane keying material, and staging or transmitting the collected material using encrypted records.

The framework's primary component is PolyFlame, a memory-resident module deployed through modified runit service paths. PolyFlame is injected into legitimate running vdaemon processes, and it can also masquerade as a packed “aaamgrd” loader variant. Once resident, PolyFlame interposes socket, DTLS, and runtime-linker behavior through functions such as recvfrom, sendto, getpeername, dlopen, dlsym, mprotect, and “/proc/%d/maps” parsing. This gives KeyDrift access to SD-WAN control-plane traffic from inside legitimate controller daemon execution rather than through a conventional endpoint beacon.

LittleFilch, another component of the KeyDrift framework, provides the collection and exfiltration capability identified in the framework. The module hooks “SSL\_read” inside vdaemon, inspects decrypted control-plane buffers, extracts keying material for a list of predefined edge nodes, and stages the data locally in encrypted format for exfiltration.

Talos assesses with high confidence that KeyDrift's intended operational purpose is Cisco SD-WAN control-plane collection: persistent controller residence, in-band traffic access, key-material extraction from decrypted control messages, and encrypted staging or exfiltration of the recovered material. Observed variations of the KeyDrift modules and deployment mechanisms suggest active development of the framework’s capabilities.

## KeyDrift analysis

KeyDrift uses Cisco SD-WAN runit service paths as its primary execution anchor. In the PolyFlame sshd deployment, the actor modifies the service run script, remounts /rootfs.rw executable, launches a malicious script “conf\_sshd” in the background, and then starts the legitimate sshd service. The loader script enumerates running vdaemon PIDs, records them in “/tmp/system-vdaemon”, and invokes the injector component “rsshd” to inject PolyFlame (“libdssl.so”) into each process.

Recovered conf\_sshd logic uses the same control flow across reviewed samples:

![](https://storage.ghost.io/c/af/a0/afa04ee3-414f-4481-8d23-7e7c146f192e/content/images/2026/10/data-src-image-f3958e3d-b846-45c7-8526-550bb5a4c34d.png)

Figure 1. conf\_sshd control flow logic.

### Runit launchers

The observed sshd runit launcher preserves normal Cisco SD-WAN sshd startup logic while adding two malicious lines before service execution, which remount “/rootfs.rw” executable and background execution of conf\_sshd, which then drives rsshd injection into vdaemon.

![](https://storage.ghost.io/c/af/a0/afa04ee3-414f-4481-8d23-7e7c146f192e/content/images/2026/10/data-src-image-52ca1586-b9e0-4a7c-8767-e8f362f8371a.png)

Figure 2. conf\_sshd execution logic.

The recovered aaamgr runit launcher from an affected vBond appliance uses a parallel service-wrapper pattern, but it executes the packed aaamgrd PolyFlame loader directly. The deletion of the writable-overlay PAM configurations for sshd and login before remounting “/rootfs.rw” executable if part of the legitimate script, along with the invocation of the aaamgrd daemon via Python:

![](https://storage.ghost.io/c/af/a0/afa04ee3-414f-4481-8d23-7e7c146f192e/content/images/2026/10/data-src-image-7c670c4f-818e-478d-aa59-705b8c657f16.png)

Figure 3. aamgrd daemon launch.

### PolyFlame

PolyFlame is the primary operational module in the KeyDrift framework. PolyFlame operates at the socket and DTLS control-plane layer. PolyFlame serves two primary purposes:

* Command execution via a TinyShell-styled backdoor
* Intermediate C2 that can forward commands to and from the C2 to other peers

PolyFlame is primarily injected into the vdaemon process, providing operational obfuscation and access to all in-process state: DTLS session keys, vEdge topology, OMP routes, and policy tables. No hardcoded IPv4 addresses, binding ports, callback domains, URLs, host headers, or polling interval were recovered from the analyzed PolyFlame samples. PolyFlame is designed for in-band control or ...