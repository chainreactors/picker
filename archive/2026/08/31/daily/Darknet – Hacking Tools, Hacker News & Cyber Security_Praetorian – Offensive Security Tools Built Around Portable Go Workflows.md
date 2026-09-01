---
title: Praetorian – Offensive Security Tools Built Around Portable Go Workflows
url: https://www.darknet.org.uk/2026/08/praetorian-offensive-security-go-tools/
source: Darknet – Hacking Tools, Hacker News & Cyber Security
date: 2026-08-31
fetch_date: 2026-09-01T06:59:36.827830
---

# Praetorian – Offensive Security Tools Built Around Portable Go Workflows

* [Skip to main content](#genesis-content)
* [Skip to primary sidebar](#genesis-sidebar-primary)
* [Skip to footer](#genesis-footer-widgets)

* [Home](https://www.darknet.org.uk/)
* [About Darknet](https://www.darknet.org.uk/about/)
* [Hacking Tools](https://www.darknet.org.uk/category/hacking-tools/)
* [Popular Posts](https://www.darknet.org.uk/popular-posts/)
* [Darknet Archives](https://www.darknet.org.uk/darknet-archives/)
* [Contact Darknet](https://www.darknet.org.uk/contact-darknet/)
  + [Advertise](https://www.darknet.org.uk/contact-darknet/advertise/)
  + [Submit a Tool](https://www.darknet.org.uk/contact-darknet/submit-a-tool/)

[![darknet.org.uk logo](https://www.darknet.org.uk/wp-content/uploads/2026/03/darknet_header_hacking_cybersec_vF-scaled.png)](https://www.darknet.org.uk/)

Darknet - Hacking Tools, Hacker News & Cyber Security

Darknet is your best source for the latest hacking tools, hacker news, cyber security best practices, ethical hacking & pen-testing.

You are here: [Home](https://www.darknet.org.uk/) / [Hacking Tools](https://www.darknet.org.uk/category/hacking-tools/) / Praetorian – Offensive Security Tools Built Around Portable Go Workflows

# Praetorian – Offensive Security Tools Built Around Portable Go Workflows

Published August 31, 2026 |

Views: 168

Praetorian’s Roman names suggest a coordinated offensive security suite. The repository dependency graph shows a looser and more useful structure: independently installed Go tools, several direct workflow connections, and a shared SDK used by part of the collection

![Praetorian, Portable Go Offensive Security Tools, beside a modular toolchain illustration with the darknet.org.uk watermark.](https://www.darknet.org.uk/wp-content/uploads/2026/08/praetorian-portable-go-offensive-security-tool-640x360.webp)

In the ten repositories assessed on 9 August 2026, four imported [`capability-sdk`](https://github.com/praetorian-inc/capability-sdk): Brutus, Pius, Vespasian and Trajan. The other six did not. Brutus also imported Nerva directly, while Aurelian imported Titus. The shared SDK arrived after the tools it now connects.

Advertisement

That result sets the boundary. These projects cover familiar parts of an assessment, including service fingerprinting, credential testing, secrets scanning, asset discovery, API assessment, Bluetooth Low Energy testing and cloud security. They fit Darknet’s [Hacking Tools](https://www.darknet.org.uk/category/hacking-tools/) coverage, but a Roman name alone says nothing about whether two tools exchange data or share an implementation.

The strongest case for the collection appears where Praetorian has reduced deployment work or removed translation between stages.

## Titus packages secrets scanning for several environments

[Titus](https://github.com/praetorian-inc/titus) is a secrets scanner with 487 detection rules drawn from NoseyParker and Kingfisher. It can inspect source trees, Git history, container images, archives and documents, then validate supported credentials against their source services. The same detection engine is exposed through a command-line tool, a Go library, a Burp Suite extension and a Chrome extension.

Its build options also show what “portable” means in practice. The accelerated build uses Hyperscan or Vectorscan through CGO, while a pure-Go target remains available for systems where those native dependencies are unsuitable. The current source instructions build it with:

make build

|  |  |
| --- | --- |
| 1 | make build |

The output is written under `dist/titus`. Prebuilt releases are available as a separate route. Those are the installation claims the repository supports; its Vectorscan clone command installs a build dependency, not Titus itself.

Titus therefore consolidates detection, file handling and credential validation behind one interface. The rule count does not establish coverage by itself, and successful validation proves that a credential works at the time of the check, not what access its owner intended. Those questions still belong in the assessment around the tool.

Advertisement

## Nerva and Brutus form the clearest pipeline

[Nerva](https://github.com/praetorian-inc/nerva) fingerprints more than 170 protocols across TCP, UDP and SCTP. It expects another scanner to find open ports, then identifies the services behind them and emits structured results. Checks for common service misconfigurations require an explicit option and are absent from its default fingerprinting pass.

[Brutus](https://github.com/praetorian-inc/brutus) consumes those results and tests credentials across 27 protocols. Its documentation includes a complete pipeline from network discovery through service identification to credential testing:

naabu -host 10.0.0.0/24 -silent | nerva --json | brutus creds -P passwords.txt

|  |  |
| --- | --- |
| 1 | naabu -host 10.0.0.0/24 -silent | nerva --json | brutus creds -P passwords.txt |

On an authorised assessment, that command lets Naabu identify exposed ports, Nerva determine what is listening, and Brutus apply an agreed password set to the relevant services. This is the collection’s most concrete integration: Brutus imports Nerva, and the documented data path removes a parsing step between them.

The Brutus name also collides with Darknet’s own archive. [Brutus AET2](https://www.darknet.org.uk/2006/09/brutus-password-cracker-download-brutus-aet2zip-aet2/) appeared here in 2006 as a Windows remote login cracker, while [THC Hydra](https://www.darknet.org.uk/2007/02/thc-hydra-the-fast-and-flexible-network-login-hacking-tool/) followed in 2007. Praetorian’s Brutus addresses the same broad job with a maintained Go binary and an input path from current discovery tooling. The shared name does not indicate a relationship between the projects.

## Caeruleus consolidates a fragmented Bluetooth workflow

[Caeruleus](https://github.com/praetorian-inc/caeruleus) applies the same engineering approach to Bluetooth Low Energy assessments. Its documentation starts from a workflow split across bettercap, deprecated BlueZ utilities and custom Bleak scripts. Caeruleus combines discovery, interaction and assessment functions in one Linux binary, with JSON and JSONL output for later processing.

This is useful consolidation because the underlying task normally crosses several utilities with different interfaces. It is still bound to Linux, compatible Bluetooth hardware and the operating system’s Bluetooth stack. One binary reduces setup without removing those environmental constraints.

The remaining repositories spread across other stages of an engagement. Pius maps organisations to internet assets, Vespasian discovers API surfaces, Hadrian tests API authorisation, Augustus targets large-language-model applications, and Aurelian examines cloud environments. They need to be assessed against the established tool in each category; their common authorship and implementation language do not supply that comparison.

## The shared SDK marks a partial product boundary

Praetorian describes [`capability-sdk`](https://github.com/praetorian-inc/capability-sdk) as a shared Go SDK for building security capabilities for the Guard platform. It supplies common `Target`, `Finding` and `Capability` types. Its architecture diagram shows a “Chariot Adapter” in a separate `chariot` repository. Both the Guard and Chariot names appear in the project’s own documentation; the public material does not explain the difference.

The four imports measured on 9 August establish a real integration layer, with six assessed repositories still operating outside it. Direct dependencies add another layer: Brutus uses Nerva, and Aurelian uses Titus. This produces a partially connected collection in which some tools can run independently, some hand work directly to another repository, and some can also emit types intended for Praetorian’s platform.

That architecture leaves a practical test for each project. A portable binary matters when...