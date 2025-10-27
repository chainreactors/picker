---
title: MaaS operation using Emmenhtal and Amadey linked to threats against Ukrainian entities
url: https://blog.talosintelligence.com/maas-operation-using-emmenhtal-and-amadey-linked-to-threats-against-ukrainian-entities/
source: Over Security - Cybersecurity news aggregator
date: 2025-07-18
fetch_date: 2025-10-06T23:54:27.295293
---

# MaaS operation using Emmenhtal and Amadey linked to threats against Ukrainian entities

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

# MaaS operation using Emmenhtal and Amadey linked to threats against Ukrainian entities

By
[Chris Neal](https://blog.talosintelligence.com/author/chris-neal/),
[Craig Jackson](https://blog.talosintelligence.com/author/craig/)

Thursday, July 17, 2025 06:00

[Threat Advisory](https://blog.talosintelligence.com/category/threat-advisory/)

* In April 2025 Cisco Talos identified a Malware-as-a-Service (MaaS) operation that utilized Amadey to deliver payloads.
* The MaaS operators used fake GitHub accounts to host payloads, tools and Amadey plug-ins, likely as an attempt to bypass web filtering and for ease of use.
* Several operator tactics, techniques and procedures (TTPs) overlap with a SmokeLoader phishing campaign, identified in early 2025, that targeted Ukrainian entities.
* The same variant of Emmenhtal identified in the SmokeLoader campaign was used by the MaaS operation to download Amadey payloads and other tooling.

---

In early February 2025, Talos observed a cluster of invoice payment and billing-themed phishing emails that appeared to target Ukrainian entities. These emails included compressed archive attachments (e.g., ZIP, 7Zip or RAR) containing at least one JavaScript file that used several layers of obfuscation to disguise a PowerShell downloader. The execution of the JavaScript and PowerShell script resulted in the download and execution of SmokeLoader on the victim system. Talos assessed the JavaScript downloaders to be the Emmenthal loader, based on notable similarities between the obfuscation methods observed in the collected samples and those described by [Orange Cyberdefense](https://www.orangecyberdefense.com/global/blog/cert-news/emmenhtal-a-little-known-loader-distributing-commodity-infostealers-worldwide).

During analysis of the Emmenhtal loaders collected from this phishing campaign, Talos identified additional samples on VirusTotal that were highly similar in structure, but did not appear to be part of the original activity cluster. Most notably, these samples were not delivered via email but were instead found in several public GitHub repositories. They also did not deliver SmokeLoader as a next-stage payload. Instead, the Emmenhtal samples were being used to deliver Amadey, which in turn downloaded a variety of custom payloads from certain public GitHub repositories.

Further review of the associated GitHub accounts and the files hosted within related repositories showed that they may be part of a larger MaaS operation that uses public GitHub repositories as open directories for staging custom payloads.

## MaaS operation leverages GitHub public repositories

MaaS is a business model in which the operators of the service sell access to malware or pre-existing infrastructure. In the operation Talos identified, the operators utilized Amadey to download a variety of malware families from fake GitHub repositories onto infected hosts. Initial activity appeared in February 2025, around the same time as the SmokeLoader campaign.

This distribution of several disparate malware families from a single infrastructure suggests that the threat actors behind the instances of Amadey are distributing payloads for other individuals or groups. In addition, the command and control (C2) infrastructures for the secondary payloads do not overlap with that of Amadey.

### Emmenhtal and Amadey

The Emmenhtal loader is a multistage downloader that has been reported by [Kroll](https://www.kroll.com/en/publications/cyber/idatloader-distribution) and [Orange Cyberdefense](https://www.orangecyberdefense.com/global/blog/cert-news/emmenhtal-a-little-known-loader-distributing-commodity-infostealers-worldwide). It was given the name “Emmenhtal” by Orange Cyberdefense in August 2024, though it is sometimes referred to as “PEAKLIGHT”, which is how [Mandiant](https://cloud.google.com/blog/topics/threat-intelligence/peaklight-decoding-stealthy-memory-only-malware/) refers to the final stage PowerShell downloader. Orange and [Talos](https://blog.talosintelligence.com/suspected-coralraider-continues-to-expand-victimology-using-three-information-stealers/) have observed activity that appears to involve elements of the Emmenhtal loader dating back to April 2024.

Emmenhtal variants have been found embedded in other files and deployed in a standalone format. Each loader typically includes four layers — three that act as obfuscation and the final PowerShell downloader script. These layers are described in the “Emmenhtal similarities between activity clusters” section below.

Amadey (or Amadey bot) originally appeared in late 2018 on Russian-speaking hacking forums with a $500 price tag. It was initially used by various threat actors to establish botnets. Amadey has also been observed dropping other malware including Redline, Lumma, StealC and SmokeLoader.

Amadey’s primary functions are to collect system information and download secondary payloads on an infected host. However, Amadey is modular and its functionality can be expanded with an assortment of plugins. These plugins come in the form of dynamic link libraries (DLLs) that can be selected based on desired functionality, such as screenshot capabilities or credential harvesting. Despite its common use as a downloader, Amadey can pose a serious threat.

### GitHub as an open directory

During Talos’ research into the MaaS operation, we uncovered three GitHub accounts being used as open directories for hosting tools, secondary payloads and Amadey plugins:

* Legendary99999
* DFfe9ewf
* Milidmdds

In addition to being an easy means of file hosting, downloading files from a GitHub repository may bypass web filtering that is not configured to block the GitHub domain. While some organizations can block GitHub in their environment to curb the use of open-source offensive tooling and other malware, m...