---
title: UAT-10147 deploys SPECTRE: A cross-platform implant with Linux rootkit and BYOVD capabilities
url: https://blog.talosintelligence.com/uat-10147-deploys-spectre-a-cross-platform-implant-with-linux-rootkit-and-byovd-capabilities/
source: Over Security
date: 2026-08-20
fetch_date: 2026-08-21T03:04:57.813136
---

# UAT-10147 deploys SPECTRE: A cross-platform implant with Linux rootkit and BYOVD capabilities

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

![](https://storage.ghost.io/c/af/a0/afa04ee3-414f-4481-8d23-7e7c146f192e/content/images/2026/08/Fig-0-.jpg)

# UAT-10147 deploys SPECTRE: A cross-platform implant with Linux rootkit and BYOVD capabilities

By
[Joey Chen](https://blog.talosintelligence.com/author/joey/)

Thursday, August 20, 2026 06:00

[Threat Spotlight](/category/threat-spotlight/)
[AI](/category/ai/)

* UAT-10147 is a highly capable Chinese-speaking intrusion actor operating a multi-platform post-exploitation ecosystem targeting IIS and Linux servers, combining search engine optimization (SEO) fraud monetization with advanced persistence and defense evasion techniques.
* The newly identified SPECTRE implant represents a significant evolution in commodity intrusion tooling, integrating cross-platform command-and-control (C2) operations, process injection, credential theft, anti-analysis protections, and kernel-level endpoint detection and response (EDR) bypass functionality.
* The actor demonstrates operational maturity through the combined use of custom malware, open-source offensive tooling, Bring Your Own Virtual Driver (BYOVD) based EDR neutralization, Linux kernel rootkits, and sophisticated in-memory web shell deployment techniques.
* Cisco Talos’ analysis of recovered source code suggests portions of the Linux rootkit development may have incorporated AI-assisted code generation workflows, highlighting the growing role of generative AI in accelerating offensive malware development.

---

In our [previous blog](https://blog.talosintelligence.com/uat-10147-chinese-speaking-adversary-integrates-agentic-ai-into-post-compromise-operations), Cisco Talos documented how UAT-10147 operationalized AI-assisted exploitation workflows to compromise internet-facing IIS and Linux servers at scale. This blog discusses how UAT-10147 is employing a diverse arsenal of tools, including SEO fraud utilities, local privilege escalation tools, and both off-the-shelf and custom developed backdoors.

To thoroughly analyze their toolkit, the following section is divided into three parts, detailing the specific tools used and their respective capabilities. We also assess that UAT-10147 is gradually incorporating AI-assisted development into its operations, likely to support the creation and refinement of tools used across its campaigns. Specifically, both its custom-developed backdoor, SPECTRE, and custom-developed rootkit, Specter, exhibit indications of AI-assisted development.

![](https://storage.ghost.io/c/af/a0/afa04ee3-414f-4481-8d23-7e7c146f192e/content/images/2026/08/Fig-0-1.jpg)

Figure 1. Gradual adoption of AI-assisted development workflows.

Talos also observed several SEO fraud-related components used in this campaign that we assess with medium confidence to be associated with “x神” (“xshen”), who is mentioned in a previously released [Talos post](https://blog.talosintelligence.com/from-pdb-strings-to-maas-tracking-a-commodity-badiis-ecosystem/). This assessment is supported by multiple development artifacts embedded in the BadIIS malware and related tooling.

The BadIIS samples used in this activity contain the following PDB paths:

* C:\Users\Administrator\Desktop\2025-11-21 (x神订制全站劫持按浏览器语言跳转)\dll\Release\demo.pdb
* C:\Users\Administrator\Desktop\2025-11-21 (x神订制全站劫持按浏览器语言跳转)\dll\x64\Release\demo.pdb

We also identified that the BadIIS installer embeds a service installer containing an additional PDB string referencing “x神”:

* C:\Users\Administrator\Desktop\x神的自安装服务\svchost\x64\Release\service.pdb

Beyond these xshen-related development artifacts, other components in the campaign also contain references to “X.” The ASHX SEO engine configuration includes a string named “X-seo,” while the web shell uses an “X-ID” HTTP header to transmit a specific token. This header appears to support covert authentication by blending the web shell’s control traffic into otherwise routine HTTP communications.

## SPECTRE: A new cross-platform backdoor

SPECTRE is a cross-platform backdoor written in C.

![](https://storage.ghost.io/c/af/a0/afa04ee3-414f-4481-8d23-7e7c146f192e/content/images/2026/08/Fig-10-1.png)

Figure 2. Windows version of SPECTRE.

![](https://storage.ghost.io/c/af/a0/afa04ee3-414f-4481-8d23-7e7c146f192e/content/images/2026/08/Fig-11-1.png)

Figure 3. Linux version of SPECTRE.

Talos named this backdoor "SPECTRE" based on a debug log recovered from one of the observed samples. This log meticulously records each step of the malware's execution process and explicitly displays its name in the header. The contents of the observed log file are provided in Figure 4.

![](https://storage.ghost.io/c/af/a0/afa04ee3-414f-4481-8d23-7e7c146f192e/content/images/2026/08/Fig-12-2.png)

Figure 4. SPECTRE debug log.

## Windows version

The Windows variant of SPECTRE distinguishes itself from the stock Havoc framework through custom post-exploitation and defense evasion capabilities compiled directly into the binary. Furthermore, the implant heavily prioritizes obfuscation and anti-analysis by utilizing a dual layered defense strategy. First, API resolution is executed entirely at runtime via PEB hash walking, using a DJB2 variant algorithm. Second, string encryption relies on a per-string xorshift32 pseudorandom number generator (PRNG) scheme. Sensitive literals are encrypted at compile time with unique 32-bit seeds, decrypted to thread local storage immediately before execution, and never stored in plaintext within the “.text” or “.rdata” sections. Consequently, static detection methods are largely ineffective against the implant's indicators.

![](https://storage.ghost.io/c/af/a0/afa04ee3-414f-4481-8d23-7e7c146f192e/content/images/2026/08/Fig-13-1.png)

Figure 5. Xorshift32 PRNG scheme.

SPECTRE has a feature to execute a weighted anti-analysis scoring routine that evaluates process name block...