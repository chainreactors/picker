---
title: PowMix botnet targets Czech workforce
url: https://blog.talosintelligence.com/powmix-botnet-targets-czech-workforce/
source: Over Security - Cybersecurity news aggregator
date: 2026-04-16
fetch_date: 2026-04-17T04:50:52.156972
---

# PowMix botnet targets Czech workforce

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

# PowMix botnet targets Czech workforce

By
[Chetan Raghuprasad](https://blog.talosintelligence.com/author/chetan/)

Thursday, April 16, 2026 06:00

[Threat Spotlight](https://blog.talosintelligence.com/category/threat-spotlight/)

* Cisco Talos discovered an ongoing malicious campaign, operating since at least December 2025, affecting a broader workforce in the Czech Republic with a previously undocumented botnet we call “PowMix.”
* PowMix employs randomized command-and-control (C2) beaconing intervals, rather than persistent connection to the C2 server, to evade the network signature detections.
* PowMix embeds the encrypted heartbeat data along with unique identifiers of the victim machine into the C2 URL paths, mimicking legitimate REST API URLs.
* PowMix has the capability to remotely update the new C2 domain to the botnet configuration file dynamically.
* Talos observed a few tactical similarities of the current campaign with the [ZipLine](https://research.checkpoint.com/2025/zipline-phishing-campaign/#:~:text=This%20suggests%20that%20the%20malicious,agent%2C%20or%20other%20contextual%20indicators.) campaign, including the payload delivery mechanism and the misuse of the legitimate cloud platform Heroku for C2 operations.

---

## Victimology

Talos observed that an attacker targeted Czech organizations across various levels, based on the contents of the lure documents used by the attacker in the current campaign.

Impersonating the legitimate EDEKA brand and authentic regulatory frameworks such as the Czech Data Protection Act, the attacker deploys decoy documents with compliance-themed lures, potentially aimed at compromising victims from human resources (HR), legal, and recruitment agencies. In the lure documents, the attacker also used compensation data, as well as the legitimate legislative references, to enhance the authenticity of these decoy documents and to entice the job aspirants across diverse sectors like IT, finance, and logistics.

![](https://storage.ghost.io/c/af/a0/afa04ee3-414f-4481-8d23-7e7c146f192e/content/images/2026/04/image-6.png)

![](https://storage.ghost.io/c/af/a0/afa04ee3-414f-4481-8d23-7e7c146f192e/content/images/2026/04/image-7-1.png)

Figures 1 (left) and 2 (right). First pages of two decoy documents.

## TTPs overlaps with the ZipLine campaign

Talos observed a few tactical similarities employed in the current campaign with that of the [ZipLine](https://research.checkpoint.com/2025/zipline-phishing-campaign/#:~:text=This%20suggests%20that%20the%20malicious,agent%2C%20or%20other%20contextual%20indicators.) campaign, reported by researchers from Check Point in August 2025.

In the current campaign, the PowMix botnet payload is delivered via an LNK triggered PowerShell loader that extracts it from a ZIP archive data blob, bypasses AMSI, and executes the decrypted script directly in memory. This campaign shares tactical overlaps with the older [ZipLine](https://research.checkpoint.com/2025/zipline-phishing-campaign/#:~:text=This%20suggests%20that%20the%20malicious,agent%2C%20or%20other%20contextual%20indicators.) campaign (which deployed the MixShell malware), including identical ZIP-based payload concealment, Windows-scheduled task persistence, CRC32-based BOT ID generation, and the abuse of “herokuapp.com” for command-and-control (C2) infrastructure. Although there are overlaps in the tactics, the attacker’s final payload was unobserved, and the intent remains unknown in this campaign.

## Attack summary

![](https://storage.ghost.io/c/af/a0/afa04ee3-414f-4481-8d23-7e7c146f192e/content/images/2026/04/PowMix.jpg)

Figure 3. Attack summary flow chart.

The attack begins when a victim runs the Windows shortcut file contained within the received malicious ZIP file, potentially through a phishing email. This shortcut file triggers the execution of an embedded PowerShell loader script, which initially creates a copy of the ZIP file along with its contents in the victim's “ProgramData” folder. Subsequently, it loads the malicious ZIP file, extracts, and executes the embedded PowMix botnet payload directly in the victim's machine memory and starts to communicate with the botnet C2.

## PowerShell loader executes PowMix in memory

The first stage PowerShell script functions as a loader, and its execution routine is designed to bypass security controls and deliver a secondary payload. It begins by defining several obfuscated variables, including file name of the malicious ZIP file that was likely received via a phishing email. Then, the script dynamically constructs paths to the folders such as “ProgramData” and the user’s “Downloads” folder to locate this ZIP file. Once the ZIP file is found, it extracts the contents to the “ProgramData”folder, effectively staging the environment for the next phase of the attack.

![](https://storage.ghost.io/c/af/a0/afa04ee3-414f-4481-8d23-7e7c146f192e/content/images/2026/04/data-src-image-129c9a39-fe3e-49a6-bf04-62e51d487f36-1-1.png)

Figure 4. Excerpt of the deobfuscated PowerShell Loader main function.

To evade detection, the script employs an AMSI (Antimalware Scan Interface) bypass technique. It uses a reflection technique to browse the loaded assemblies in the current process, specifically searching for the `AmsiUtils` class. Once located, it identifies the `amsiInitFailed` field and manually sets its value to true. This action deceives the Windows security subsystem into thinking that AMSI has not initialized, which disables real-time scanning of subsequent commands, enabling the script to run malicious code in memory without being detected by Windows Defender or other endpoint detection and response (EDR) solutions.

![](https://storage.ghost.io/c/af/a0/afa04ee3-414f-4481-8d23-7e7c146f192e/content/images/2026/04/data-src-image-7a4fc13c-9eaf-4b6a-a3c6-ff048060f0e0-1.png)

Fi...