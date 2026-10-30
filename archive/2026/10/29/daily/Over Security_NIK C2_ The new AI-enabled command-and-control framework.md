---
title: NIK C2: The new AI-enabled command-and-control framework
url: https://blog.talosintelligence.com/nik-c2-new-ai-enabled-framework/
source: Over Security
date: 2026-10-29
fetch_date: 2026-10-30T07:56:08.618609
---

# NIK C2: The new AI-enabled command-and-control framework

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

![](https://storage.ghost.io/c/af/a0/afa04ee3-414f-4481-8d23-7e7c146f192e/content/images/2026/10/NIKC2-Header.jpg)

# NIK C2: The new AI-enabled command-and-control framework

By
[Chetan Raghuprasad](https://blog.talosintelligence.com/author/chetan/)

Thursday, October 29, 2026 06:00

[Threats](/category/threats/)
[AI](/category/ai/)

* Cisco Talos observed a new AI-integrated command-and-control (C2) framework in the wild called “NIK C2.”
* NIK C2 contains a Windows implant, using which, an actor can dump credentials, stream the victim's keystrokes to collect the targeted victim’s sensitive data, and instruct an integrated AI model to analyze the harvested data, all within the compromised session.
* In this framework, the actor has abused the OpenAI Chat Completions application programming interface (API), which is a HTTP endpoint that enables ChatGPT-style conversations programmatically.
* In addition to the features that enable theft, an actor can also deploy desktop screen-locking ransomware via the NIK C2 implant onto the victim machine, leading to a ransom demand in Bitcoin or USDT cryptocurrencies.
* NIK C2 reshapes adversary tradecraft by collapsing collection and exploitation into a single continuous session, effectively erasing the offline processing delays that historically granted defenders critical detection windows.
* Such AI-enabled adversarial frameworks require defenders to move beyond traditional detection and embrace continuous behavioral vigilance as the new baseline.

---

## NIK C2 implant: AI-integrated remote access tool

The NIK C2 implant is a Go-based, 64-bit Windows remote access tool that grants persistent control over compromised hosts using a resilient dual-channel C2 architecture. It communicates over TLS-secured WebSockets on port 443 alongside an HTTP fallback polling loop every 250 milliseconds, protecting all traffic with AES-256-GCM encryption derived from a hardcoded seed. To survive takedowns, the implant routes traffic across three prioritized C2 tiers, which are runtime-updated URLs, an embedded encrypted server list, and a hardcoded fallback address. Beyond standard operations, the implant features surveillance, theft, lateral movement, and evasion capabilities, including credential dumping, RDP session hijacking, process hollowing, and a C2-driven screen lock ransomware module.

Notably, the NIK C2 implant embeds a fully integrated OpenAI API client via its `ai_generate` command, allowing operators to route arbitrary prompts to the OpenAI Chat Completions API directly through the infected host. The NIK C2 implant manages API key resolution, request assembly, and response parsing locally, returning the encrypted generative AI results to the actor's C2.

The observed NIK C2 implant samples in the wild contains an embedded build path (/opt/nik\_panel/data/build\_52b79724a1fc4b8f/main.go), which identifies the project as "nik\_panel" and indicates that the implant was cross compiled for Windows from a Linux development environment. Furthermore, the embedded eight-byte hex token matching the build identifier highlights that the threat actor's infrastructure actively tracking and versioning the implants.

![](https://storage.ghost.io/c/af/a0/afa04ee3-414f-4481-8d23-7e7c146f192e/content/images/2026/10/NIK-C2-architecture.jpg)

Figure 1. NIK C2 implant’s operational architecture.

## NIK C2 implant evolution timeline

Talos observed that the NIK C2 implant development trajectory spans at least three distinct versions. All binaries observed in the wild were compiled with Go 1.23.4 (which was released in December 2024), placing the entire sample set compiled no earlier than late 2024. The actor has Zeroed PE TimeDateStamp fields and near-epoch filesystem timestamps (manifesting as Nov 29, 1979) are applied consistently across all samples.

We developed a timeline based on the initial sighting dates of NIK C2 implant variants in OSINT.

![](https://storage.ghost.io/c/af/a0/afa04ee3-414f-4481-8d23-7e7c146f192e/content/images/2026/10/NIK-C2-timeline.jpg)

Figure 2. NIK C2 implant evolution timeline.

The pace of capability addition across the three versions indicates a technically proficient team with prior malware operations experience is actively expanding NIK C2 towards a full-service adversarial framework.

## Active NIK C2 server seen in the wild

During our research, we observed that a threat actor hosted the NIK C2 framework on a server at IP address “87.120.196[.]120”, resolving the domain “total-sitevv[.]lol”. The C2 server hosted an SSL/TLS certificate (serial number *7d16381a9de823943b5a0987dbd0f26edf22052b* and *jarm:"28d28d28d00000000042d42d0000001f361a1bf80ed39a1e352adeb016a07b"* ) with the Common Name (CN) set to `nik-panel`. This CN value matches strings embedded within the implant binary. Observing the NIK C2 infrastructure active in the wild allowed us to assess with moderate confidence that NIK C2 is not merely a proof of concept, but a fully functional, AI-integrated C2 framework.

![](https://storage.ghost.io/c/af/a0/afa04ee3-414f-4481-8d23-7e7c146f192e/content/images/2026/10/data-src-image-8013d92a-d618-4286-901e-9303970117b5.png)

Figure 3. NIK C2 was observed in the wild during the research period.

## NIK C2 implant integrates OpenAI’s API

AI integration is one of the most architecturally distinct features of NIK C2 implant. It constructs a fully formed HTTP request to OpenAI’s production inference endpoint, transmits it from the victim machine IP address, parses the JSON response, and returns the AI-generated text to the actor’s panel. The entire operation from receiving the actor prompt to returning the large language model (LLM) reply is executed synchronously with a 60-second timeout.

The implant begins by extracting three fields from the command payload received from the C2. The firs...